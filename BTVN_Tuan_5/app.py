import os

import yaml
from flask import Flask, jsonify, request
from uuid import uuid4
from datetime import date

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "openapi.yaml"), encoding="utf-8") as f:
    SPEC = yaml.safe_load(f)

SWAGGER_HTML = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Tasks API - Swagger UI</title>
  <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.ui = SwaggerUIBundle({
      url: "/openapi.json",
      dom_id: "#swagger-ui",
      persistAuthorization: true
    });
  </script>
</body>
</html>"""

STATUSES = {"open", "done"}

TASKS = {
    "3fa85f64-5717-4562-b3fc-2c963f66afa6": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "title": "Họp nhóm API team",
        "status": "open",
        "priority": "high",
        "dueDate": "2026-10-15",
        "assigneeId": "u-1001",
    },
    "7c9e6679-7425-40de-944b-e07fc1f90ae7": {
        "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
        "title": "Viết tài liệu OpenAPI",
        "status": "done",
        "priority": "normal",
        "dueDate": "2026-10-10",
        "assigneeId": "u-1002",
    },
}


def error(status, title, detail):
    return jsonify({"title": title, "status": status, "detail": detail}), status


def has_bearer():
    header = request.headers.get("Authorization", "")
    return header.startswith("Bearer ") and len(header) > len("Bearer ")


@app.get("/openapi.json")
def spec_json():
    return jsonify(SPEC)


@app.get("/docs")
def docs():
    return SWAGGER_HTML


@app.get("/v1/tasks")
def list_tasks():
    limit = request.args.get("limit", default=20, type=int)
    if limit is None or limit < 1 or limit > 100:
        return error(400, "Bad request", "limit phải nằm trong khoảng 1 đến 100")
    status = request.args.get("status")
    if status and status not in STATUSES:
        return error(400, "Bad request", "status phải là open hoặc done")
    items = [t for t in TASKS.values() if not status or t["status"] == status]
    return jsonify({"items": items[:limit], "total": len(items)}), 200


@app.get("/v1/tasks/<task_id>")
def get_task_by_id(task_id):
    if not has_bearer():
        return error(401, "Unauthorized", "Thiếu hoặc sai Bearer token")
    task = TASKS.get(task_id)
    if task is None:
        return error(404, "Task not found", "Không tìm thấy task với id đã cho")
    return jsonify(task), 200

@app.post("/v1/tasks")
def create_task():
    if not has_bearer():
        return error(401, "Unauthorized", "Thiếu hoặc sai Bearer token")

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return error(400, "Bad request", "Request body phải là JSON object")

    allowed_fields = {"title", "status", "priority", "dueDate", "assigneeId"}
    if set(data) - allowed_fields:
        return error(400, "Bad request", "Request chứa trường không hợp lệ")

    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return error(400, "Bad request", "title là bắt buộc và không được để trống")

    status = data.get("status", "open")
    priority = data.get("priority", "normal")
    due_date = data.get("dueDate")
    assignee_id = data.get("assigneeId")

    if not isinstance(status, str) or status not in STATUSES:
        return error(400, "Bad request", "status phải là open hoặc done")

    if not isinstance(priority, str) or priority not in {"low", "normal", "high"}:
        return error(400, "Bad request", "priority phải là low, normal hoặc high")

    if due_date is not None:
        if not isinstance(due_date, str):
            return error(400, "Bad request", "dueDate phải có định dạng YYYY-MM-DD")
        try:
            date.fromisoformat(due_date)
        except ValueError:
            return error(400, "Bad request", "dueDate phải có định dạng YYYY-MM-DD")

    if assignee_id is not None and not isinstance(assignee_id, str):
        return error(400, "Bad request", "assigneeId phải là chuỗi hoặc null")

    task_id = str(uuid4())
    task = {
        "id": task_id,
        "title": title.strip(),
        "status": status,
        "priority": priority,
        "dueDate": due_date,
        "assigneeId": assignee_id,
    }

    TASKS[task_id] = task
    return jsonify(task), 201

@app.patch("/v1/tasks/<task_id>")
def update_task(task_id):
    if not has_bearer():
        return error(401, "Unauthorized", "Thiếu hoặc sai Bearer token")

    task = TASKS.get(task_id)
    if task is None:
        return error(404, "Task not found", "Không tìm thấy task với id đã cho")

    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not data:
        return error(400, "Bad request", "Request body phải là JSON object không rỗng")

    allowed_fields = {"title", "status", "priority", "dueDate", "assigneeId"}
    if set(data) - allowed_fields:
        return error(400, "Bad request", "Request chứa trường không hợp lệ")

    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return error(400, "Bad request", "title không được để trống")
        task["title"] = data["title"].strip()

    if "status" in data:
        if not isinstance(data["status"], str) or data["status"] not in STATUSES:
            return error(400, "Bad request", "status phải là open hoặc done")
        task["status"] = data["status"]

    if "priority" in data:
        if not isinstance(data["priority"], str) or data["priority"] not in {"low", "normal", "high"}:
            return error(400, "Bad request", "priority phải là low, normal hoặc high")
        task["priority"] = data["priority"]

    if "dueDate" in data:
        due_date = data["dueDate"]
        if due_date is not None:
            if not isinstance(due_date, str):
                return error(400, "Bad request", "dueDate phải có định dạng YYYY-MM-DD")
            try:
                date.fromisoformat(due_date)
            except ValueError:
                return error(400, "Bad request", "dueDate phải có định dạng YYYY-MM-DD")
        task["dueDate"] = due_date

    if "assigneeId" in data:
        assignee_id = data["assigneeId"]
        if assignee_id is not None and not isinstance(assignee_id, str):
            return error(400, "Bad request", "assigneeId phải là chuỗi hoặc null")
        task["assigneeId"] = assignee_id

    return jsonify(task), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)