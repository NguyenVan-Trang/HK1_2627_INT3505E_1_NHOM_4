import os

import yaml
from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)