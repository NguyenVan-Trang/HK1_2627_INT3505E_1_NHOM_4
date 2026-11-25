
from flask import Flask, jsonify, request
from flask_cors import CORS
from uuid import UUID, uuid4
from datetime import date

app = Flask(__name__)
CORS(app)

# ==================================================
# 1. DEMO USERS AND TOKENS
# ==================================================

OWNER_ID = "11111111-1111-4111-8111-111111111111"
RENTER_ID = "22222222-2222-4222-8222-222222222222"
OTHER_USER_ID = "33333333-3333-4333-8333-333333333333"

# Demo authentication only. Not production JWT.
DEMO_TOKENS = {
    "owner-demo-token": OWNER_ID,
    "renter-demo-token": RENTER_ID,
    "other-demo-token": OTHER_USER_ID
}


def get_current_user():
    """Return user ID from demo Bearer token."""
    auth_header = request.headers.get("Authorization", "")

    if not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ", 1)[1].strip()
    return DEMO_TOKENS.get(token)


def error_response(code, message, status):
    return jsonify({
        "code": code,
        "message": message
    }), status


def is_valid_uuid(value):
    try:
        UUID(value)
        return True
    except (ValueError, TypeError, AttributeError):
        return False


def parse_date(value):
    try:
        return date.fromisoformat(value)
    except (ValueError, TypeError):
        return None


def dates_overlap(start1, end1, start2, end2):
    """Inclusive date-range overlap."""
    return start1 <= end2 and start2 <= end1


# ==================================================
# 2. IN-MEMORY DATA
# ==================================================

items = [
    {
        "itemId": "550e8400-e29b-41d4-a716-446655440001",
        "ownerId": OWNER_ID,
        "title": "Canon EOS M50",
        "description": "Máy ảnh mirrorless dùng cho chụp ảnh và quay video.",
        "category": "Electronics",
        "dailyPrice": 200000,
        "deposit": 1000000,
        "status": "ACTIVE"
    },
    {
        "itemId": "550e8400-e29b-41d4-a716-446655440002",
        "ownerId": OTHER_USER_ID,
        "title": "Camping Tent",
        "description": "Lều cắm trại dành cho 2-3 người.",
        "category": "Outdoor",
        "dailyPrice": 150000,
        "deposit": 500000,
        "status": "ACTIVE"
    }
]

rental_requests = []
rentals = []


# ==================================================
# 3. HOME AND HEALTH CHECK
# ==================================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "RentMate Backend is running",
        "version": "1.0.0"
    }), 200


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200


# ==================================================
# 4. GET /api/v1/items
# List and search available items
# ==================================================

@app.route("/api/v1/items", methods=["GET"])
def list_items():
    result = [
        item for item in items
        if item["status"] == "ACTIVE"
    ]

    keyword = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "").strip().lower()

    if keyword:
        result = [
            item for item in result
            if keyword in item["title"].lower()
        ]

    if category:
        result = [
            item for item in result
            if item["category"].lower() == category
        ]

    return jsonify({
        "data": result
    }), 200


# ==================================================
# 5. GET /api/v1/items/{itemId}
# Get item details
# ==================================================

@app.route("/api/v1/items/<item_id>", methods=["GET"])
def get_item(item_id):
    if not is_valid_uuid(item_id):
        return error_response(
            "INVALID_ITEM_ID",
            "itemId must be a valid UUID",
            400
        )

    item = next(
        (x for x in items if x["itemId"] == item_id),
        None
    )

    if item is None or item["status"] != "ACTIVE":
        return error_response(
            "ITEM_NOT_FOUND",
            "Item not found",
            404
        )

    return jsonify({
        "data": item
    }), 200


# ==================================================
# 6. POST /api/v1/rental-requests
# Create a rental request
# ==================================================

@app.route("/api/v1/rental-requests", methods=["POST"])
def create_rental_request():
    renter_id = get_current_user()

    if renter_id is None:
        return error_response(
            "UNAUTHORIZED",
            "Authentication required",
            401
        )

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return error_response(
            "INVALID_REQUEST",
            "Request body must be a JSON object",
            400
        )

    required_fields = ["itemId", "startDate", "endDate"]

    if any(
        field not in data or not isinstance(data[field], str)
        or not data[field].strip()
        for field in required_fields
    ):
        return error_response(
            "VALIDATION_ERROR",
            "itemId, startDate and endDate are required",
            400
        )

    item_id = data["itemId"]

    if not is_valid_uuid(item_id):
        return error_response(
            "INVALID_ITEM_ID",
            "itemId must be a valid UUID",
            400
        )

    item = next(
        (x for x in items if x["itemId"] == item_id),
        None
    )

    if item is None or item["status"] != "ACTIVE":
        return error_response(
            "ITEM_NOT_FOUND",
            "Item not found or unavailable",
            400
        )

    if item["ownerId"] == renter_id:
        return error_response(
            "INVALID_RENTAL",
            "You cannot rent your own item",
            400
        )

    start_date = parse_date(data["startDate"])
    end_date = parse_date(data["endDate"])

    if start_date is None or end_date is None:
        return error_response(
            "INVALID_DATE",
            "Dates must use YYYY-MM-DD format",
            400
        )

    if start_date < date.today() or end_date < start_date:
        return error_response(
            "INVALID_DATE_RANGE",
            "Rental dates must be valid and in the future",
            400
        )

    # Prevent overlap with approved or active rentals.
    for rental in rentals:
        if (
            rental["itemId"] == item_id
            and rental["status"] in ["CONFIRMED", "ACTIVE"]
            and dates_overlap(
                start_date,
                end_date,
                parse_date(rental["startDate"]),
                parse_date(rental["endDate"])
            )
        ):
            return error_response(
                "RENTAL_PERIOD_UNAVAILABLE",
                "Rental period is unavailable",
                409
            )

    # Prevent duplicate overlapping pending requests
    # from the same renter.
    for existing in rental_requests:
        if (
            existing["itemId"] == item_id
            and existing["renterId"] == renter_id
            and existing["status"] == "PENDING"
            and dates_overlap(
                start_date,
                end_date,
                parse_date(existing["startDate"]),
                parse_date(existing["endDate"])
            )
        ):
            return error_response(
                "RENTAL_REQUEST_CONFLICT",
                "You already have an overlapping pending request",
                409
            )

    new_request = {
        "requestId": str(uuid4()),
        "itemId": item_id,
        "renterId": renter_id,
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "status": "PENDING",
        "message": data.get("message", "")
    }

    rental_requests.append(new_request)

    return jsonify({
        "data": new_request
    }), 201


# ==================================================
# 7. PATCH /api/v1/rental-requests/{requestId}
# Owner approves or rejects a request
# ==================================================

@app.route("/api/v1/rental-requests/<request_id>", methods=["PATCH"])
def decide_rental_request(request_id):
    owner_id = get_current_user()

    if owner_id is None:
        return error_response(
            "UNAUTHORIZED",
            "Authentication required",
            401
        )

    rental_request = next(
        (x for x in rental_requests if x["requestId"] == request_id),
        None
    )

    if rental_request is None:
        return error_response(
            "REQUEST_NOT_FOUND",
            "Rental request not found",
            404
        )

    item = next(
        (x for x in items if x["itemId"] == rental_request["itemId"]),
        None
    )

    if item is None or item["ownerId"] != owner_id:
        return error_response(
            "FORBIDDEN",
            "Only the item owner can decide this request",
            403
        )

    if rental_request["status"] != "PENDING":
        return error_response(
            "REQUEST_ALREADY_PROCESSED",
            "Request is no longer pending",
            409
        )

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return error_response(
            "INVALID_REQUEST",
            "Request body must be a JSON object",
            400
        )

    decision = data.get("decision")

    if decision not in ["APPROVED", "REJECTED"]:
        return error_response(
            "INVALID_DECISION",
            "decision must be APPROVED or REJECTED",
            400
        )

    # Check for conflicting confirmed rentals before approval.
    if decision == "APPROVED":
        request_start = parse_date(rental_request["startDate"])
        request_end = parse_date(rental_request["endDate"])

        for rental in rentals:
            if (
                rental["itemId"] == rental_request["itemId"]
                and rental["status"] in ["CONFIRMED", "ACTIVE"]
                and dates_overlap(
                    request_start,
                    request_end,
                    parse_date(rental["startDate"]),
                    parse_date(rental["endDate"])
                )
            ):
                return error_response(
                    "RENTAL_PERIOD_CONFLICT",
                    "Rental period conflicts with another rental",
                    409
                )

        rental_request["status"] = "APPROVED"

        new_rental = {
            "rentalId": str(uuid4()),
            "requestId": rental_request["requestId"],
            "itemId": rental_request["itemId"],
            "renterId": rental_request["renterId"],
            "ownerId": owner_id,
            "startDate": rental_request["startDate"],
            "endDate": rental_request["endDate"],
            "status": "CONFIRMED"
        }

        rentals.append(new_rental)

        return jsonify({
            "data": {
                "request": rental_request,
                "rental": new_rental
            }
        }), 200

    # Reject request
    rental_request["status"] = "REJECTED"

    return jsonify({
        "data": {
            "request": rental_request,
            "rental": None
        }
    }), 200


# ==================================================
# 8. GET /api/v1/rentals/{rentalId}
# Get rental details
# ==================================================

@app.route("/api/v1/rentals/<rental_id>", methods=["GET"])
def get_rental(rental_id):
    user_id = get_current_user()

    if user_id is None:
        return error_response(
            "UNAUTHORIZED",
            "Authentication required",
            401
        )

    rental = next(
        (x for x in rentals if x["rentalId"] == rental_id),
        None
    )

    if rental is None:
        return error_response(
            "RENTAL_NOT_FOUND",
            "Rental not found",
            404
        )

    if user_id not in [rental["renterId"], rental["ownerId"]]:
        return error_response(
            "FORBIDDEN",
            "User is not involved in this rental",
            403
        )

    return jsonify({
        "data": rental
    }), 200


# ==================================================
# 9. RUN SERVER
# ==================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
