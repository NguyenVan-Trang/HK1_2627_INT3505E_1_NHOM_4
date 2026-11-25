# RentMate — Mốc dự án (Milestones)

| Mốc | Tuần | Nội dung | Điều kiện hoàn thành | Trạng thái |
|---|---|---|---|---|
| M1 — Design Review | 12 | Project brief, resource model, ERD, kiến trúc, OpenAPI, Swagger UI/mock, repo, backlog, slide | Use case và MVP rõ; OpenAPI hợp lệ (Spectral không lỗi), demo được 3 operation trên Swagger UI hoặc mock | Hoàn thành |
| M2 — Nền tảng | 13 | Flask + SQLite, Item API, React cơ bản, auth | `GET /items`, `GET /items/{itemId}` đúng contract; frontend hiển thị danh sách và chi tiết | Chưa bắt đầu |
| M3 — Nghiệp vụ thuê | 14 | RentalRequest, Rental, kiểm tra trùng lịch, tích hợp frontend | Gửi yêu cầu, duyệt, tạo Rental đúng quy tắc; trả 409 khi trùng lịch | Chưa bắt đầu |
| M4 — Hoàn thiện và demo | 15 | Kiểm thử, README, kịch bản demo | Demo trọn luồng thuê; có kết quả test; mỗi thành viên có commit/PR riêng | Chưa bắt đầu |

## Kịch bản demo luồng trọng tâm

1. Renter đăng nhập, tìm máy ảnh (`GET /items`) và xem chi tiết (`GET /items/{itemId}`).
2. Renter gửi yêu cầu thuê 01–05/12 (`POST /rental-requests`) và nhận `PENDING`.
3. Một yêu cầu khác trùng ngày bị từ chối khi duyệt với mã 409.
4. Owner duyệt yêu cầu (`PATCH /rental-requests/{requestId}`) và hệ thống tạo Rental `CONFIRMED`.
5. Owner xác nhận bàn giao và hoàn trả (`PATCH /rentals/{rentalId}`); Rental chuyển `ACTIVE` rồi `COMPLETED`.
