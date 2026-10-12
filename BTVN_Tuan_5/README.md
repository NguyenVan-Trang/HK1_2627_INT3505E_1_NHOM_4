# Tasks API

## 1. Giới thiệu dự án
Tasks API là REST API phục vụ quản lý công việc (task), được xây dựng bằng Flask và mô tả giao diện API theo chuẩn OpenAPI 3.0.3. Dự án cung cấp các chức năng xem danh sách task, tạo task mới, xem chi tiết, cập nhật và xóa task.

Swagger UI được tích hợp để hiển thị tài liệu API và hỗ trợ kiểm thử trực tiếp thông qua chức năng **Try it out**.

### Công nghệ sử dụng
- **Python và Flask:** Xây dựng REST API.
- **OpenAPI 3.0.3:** Đặc tả các endpoint, tham số, request body và response.
- **PyYAML:** Đọc file `openapi.yaml`.
- **Swagger UI:** Hiển thị tài liệu và kiểm thử API.

### Các endpoint
| Method | Endpoint | Mô tả |
| :--- | :--- | :--- |
| `GET` | `/v1/tasks` | Lấy danh sách task, hỗ trợ lọc theo trạng thái và giới hạn số lượng |
| `POST` | `/v1/tasks` | Tạo task mới |
| `GET` | `/v1/tasks/{taskId}` | Lấy chi tiết task theo ID |
| `PATCH` | `/v1/tasks/{taskId}` | Cập nhật một phần thông tin task |
| `DELETE` | `/v1/tasks/{taskId}` | Xóa task theo ID |

### Cấu trúc dữ liệu task
Một task gồm các trường:
- `id`: Định danh duy nhất của task.
- `title`: Tiêu đề task.
- `status`: Trạng thái `open` hoặc `done`.
- `priority`: Mức độ ưu tiên `low`, `normal` hoặc `high`.
- `dueDate`: Ngày hết hạn, định dạng `YYYY-MM-DD`.
- `assigneeId`: Định danh người được giao task.

---

## 2. Cài đặt và chạy ứng dụng

### Yêu cầu
- Python 3.10 trở lên.
- pip.
- Kết nối Internet khi tải các thư viện hoặc khi trình duyệt tải Swagger UI từ CDN.

### Bước 1: Cài đặt thư viện
Mở terminal tại thư mục dự án:
```bash
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Cài đặt các thư viện:
```bash
python -m pip install -r requirements.txt
```

### Bước 2: Khởi chạy ứng dụng
```bash
python app.py
```
Ứng dụng mặc định chạy tại: `http://127.0.0.1:5000`

### Bước 3: Truy cập API và tài liệu
- **Swagger UI:** `http://127.0.0.1:5000/docs`
- **OpenAPI JSON:** `http://127.0.0.1:5000/openapi.json`
- **Danh sách task:** `http://127.0.0.1:5000/v1/tasks`

Trong Swagger UI, chọn endpoint, nhấn **Try it out**, nhập tham số hoặc request body rồi nhấn **Execute** để gửi request. 

Đối với các endpoint yêu cầu xác thực, nhấn **Authorize** và nhập Bearer token phù hợp với cấu hình ứng dụng.

---

## 3. Hai quyết định thiết kế khó nhất

### 3.1. Thống nhất đặc tả OpenAPI với cách triển khai Flask
- **Vấn đề:** Dự án có hai phần liên quan chặt chẽ là mã nguồn Flask và file `openapi.yaml`. Nếu đường dẫn, kiểu dữ liệu, request body hoặc response giữa hai phần không thống nhất, Swagger UI có thể gửi request không đúng hoặc mô tả kết quả khác với hành vi thực tế của API.
- **Quyết định thiết kế:** Nhóm thống nhất sử dụng OpenAPI 3.0.3 để mô tả năm endpoint của Tasks API. Các endpoint được nhóm theo tài nguyên `/tasks`, sử dụng `taskId` cho thao tác trên một task và khai báo các schema dùng chung như `Task`, `TaskList` và `Error`. Các thao tác tạo và cập nhật sử dụng lần lượt `CreateTaskInput` và `UpdateTaskInput`.
- **Trao đổi trong nhóm:** Các thành viên đối chiếu đường dẫn, trường dữ liệu, mã HTTP và ví dụ request/response giữa `app.py` và `openapi.yaml`. Thành viên phụ trách từng endpoint chịu trách nhiệm bảo đảm phần triển khai tương ứng với đặc tả chung.
- **Lý do lựa chọn:** Cách tiếp cận này giúp thống nhất hợp đồng API giữa các thành viên, hỗ trợ kiểm thử bằng Swagger UI và giảm sai lệch khi tích hợp các phần code.

### 3.2. Thiết kế xác thực và xử lý lỗi cho các endpoint
- **Vấn đề:** API cần phân biệt request hợp lệ, request thiếu thông tin xác thực, dữ liệu đầu vào không hợp lệ và task không tồn tại. Nếu các endpoint xử lý không thống nhất, client sẽ khó xác định nguyên nhân thất bại.
- **Quyết định thiết kế:** Nhóm sử dụng Bearer authentication cho các endpoint cần xác thực và thống nhất cấu trúc lỗi JSON gồm `title`, `status` và `detail`. Các mã HTTP chính gồm:
  - `201 Created`: Tạo task thành công.
  - `200 OK`: Truy vấn hoặc cập nhật thành công.
  - `400 Bad Request`: Tham số hoặc dữ liệu đầu vào không hợp lệ.
  - `401 Unauthorized`: Thiếu hoặc sai Bearer token theo kiểm tra của ứng dụng.
  - `404 Not Found`: Không tìm thấy task tương ứng.
- Đối với thao tác `PATCH`, nhóm cho phép cập nhật một phần trường dữ liệu thay vì yêu cầu gửi lại toàn bộ task. Những trường không được gửi trong request sẽ được giữ nguyên.
- **Trao đổi trong nhóm:** Các thành viên thống nhất cách biểu diễn lỗi và đối chiếu mã HTTP giữa các endpoint. Nhóm cũng kiểm thử những trường hợp như thiếu `title`, status không hợp lệ, thiếu token và `taskId` không tồn tại để kiểm tra hành vi của API.
- **Lý do lựa chọn:** Cách thiết kế này giúp API có phản hồi dễ hiểu, nhất quán và thuận tiện cho việc kiểm thử, tích hợp với client.

---

## 4. Kiểm thử
Các endpoint được kiểm thử bằng Swagger UI thông qua chức năng **Try it out**. Những trường hợp kiểm thử bao gồm:
- Tạo task với dữ liệu hợp lệ.
- Cập nhật task và kiểm tra lại dữ liệu.
- Tạo task thiếu trường bắt buộc.
- Gửi trạng thái không hợp lệ.
- Gửi request không có Bearer token.
- Truy cập task không tồn tại.

Kết quả kiểm thử được đối chiếu với mã HTTP và response body được mô tả trong OpenAPI.

---

## 5. Giới hạn hiện tại
- Dữ liệu task hiện được lưu trong bộ nhớ của ứng dụng, do đó không được bảo đảm tồn tại sau khi ứng dụng khởi động lại.
- Kiểm tra Bearer token hiện tại chỉ xác nhận định dạng header, chưa thực hiện xác minh JWT thực sự.

Các giới hạn này có thể được cải thiện trong những phiên bản tiếp theo bằng cách bổ sung cơ sở dữ liệu và cơ chế xác thực đầy đủ.