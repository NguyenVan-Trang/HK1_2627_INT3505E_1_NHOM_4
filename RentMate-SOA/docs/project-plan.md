# RentMate — Kế hoạch thực hiện tuần 13–15

## 1. Mục tiêu

Chuyển từ thiết kế (tuần 12) sang triển khai luồng nghiệp vụ trọng tâm: **xem đồ → gửi yêu cầu thuê → chủ đồ duyệt → tạo Rental → xác nhận bàn giao và hoàn trả**. Mọi bước bám theo `api/openapi.yaml`.

## 2. Kế hoạch theo tuần

| Tuần | Mục tiêu | Backlog | Kết quả cuối tuần |
|---|---|---|---|
| 13 | Nền tảng và API đọc dữ liệu | RM-07, RM-08, RM-09, RM-10, RM-14 | Flask + SQLite chạy được; `GET /items`, `GET /items/{itemId}` trả dữ liệu mẫu; React hiển thị danh sách và chi tiết |
| 14 | Nghiệp vụ thuê và tích hợp | RM-11, RM-12, RM-13, RM-15 | `POST /rental-requests`, `PATCH /rental-requests/{requestId}`, `GET /rentals/{rentalId}` chạy đúng quy tắc; frontend gọi API thật |
| 15 | Kiểm thử và hoàn thiện | RM-16, RM-17, RM-18, RM-20 | Test Postman và test trùng lịch; demo trọn luồng thuê; README, kịch bản demo |

## 3. Phân công

| Thành viên | Tuần 13 | Tuần 14 | Tuần 15 |
|---|---|---|---|
| TV1 — API Design & Backend Core | Khởi tạo Flask, SQLite, model User/Item; auth (`/auth/register`, `/auth/login`); `GET /items`, `GET /items/{itemId}` | `POST /items`, `PATCH /items/{itemId}`; hỗ trợ tích hợp | Test Postman cho Items và Auth; sửa lỗi |
| TV2 — Rental Business Logic | Model RentalRequest và Rental; quy tắc trạng thái | `POST /rental-requests`, `PATCH /rental-requests/{requestId}`, `GET /rentals/{rentalId}`, `PATCH /rentals/{rentalId}`; kiểm tra trùng lịch trong transaction | Test trùng lịch, test quyền Owner/Renter |
| TV3 — Frontend, Integration & Documentation | Khởi tạo React; trang danh sách và chi tiết | Form gửi yêu cầu, màn hình Owner duyệt; tích hợp API | Kiểm thử end-to-end, README, slide, kịch bản demo |

Cả nhóm: review PR chéo, giữ `openapi.yaml` là nguồn sự thật; mọi thay đổi contract phải qua PR.

## 4. Rủi ro và phương án xử lý

| Rủi ro | Mức độ | Phương án |
|---|---|---|
| Hai yêu cầu cùng khoảng ngày cùng được duyệt | Cao | Kiểm tra trùng lịch lại trong transaction khi duyệt; viết test hai yêu cầu đồng thời |
| Contract đổi giữa chừng làm vỡ tích hợp | Trung bình | Chỉnh `openapi.yaml` qua PR, chạy Spectral trước khi merge |
| Frontend phải chờ backend | Trung bình | Dùng mock server Prism theo contract đến khi API sẵn sàng |
| Phạm vi phình to (thanh toán, chat, vận chuyển) | Trung bình | Giữ các mục này ngoài MVP, chỉ làm khi toàn bộ P0 xong |
| Thành viên bị trễ tiến độ | Trung bình | Họp đầu và cuối tuần, theo dõi trạng thái trong `project/backlog.md` |

## 5. Quy ước làm việc

- Mỗi người một branch; mỗi chức năng một PR, có người review trước khi merge.
- Commit nhỏ, thông điệp rõ; báo cáo hằng tuần dẫn commit/PR làm bằng chứng.
- Mọi API phải khớp `api/openapi.yaml` và dùng chung `ErrorResponse`.
