
# RentMate — Phân công công việc nhóm

## 1. Thông tin nhóm

- **Dự án:** RentMate — Peer-to-Peer Rental Platform
- **Quy mô:** 3 thành viên
- **Thời gian:** 4 tuần
- **Kiến trúc:** Modular Monolith + Layered Architecture
- **Backend:** Flask
- **Frontend:** React
- **API Contract:** OpenAPI 3.0.3

## 2. Phân công nhiệm vụ

### Thành viên 1 — API Design & Backend Core

**Trách nhiệm chính:** Thiết kế API contract và xây dựng các chức năng backend liên quan đến quản lý đồ cho thuê.

Công việc:

- Hoàn thiện OpenAPI contract.
- Xây dựng cấu trúc Flask backend.
- Thiết kế và triển khai model User, Item.
- Triển khai API:
  - GET /items
  - GET /items/{itemId}
- Xây dựng chức năng tìm kiếm và lọc đồ cho thuê.
- Kiểm tra API bằng Swagger UI hoặc Postman.

**Sản phẩm bàn giao:**

- `api/openapi.yaml`
- Backend Item module.
- Các API truy xuất danh sách và chi tiết Item.

### Thành viên 2 — Rental Business Logic

**Trách nhiệm chính:** Xây dựng nghiệp vụ yêu cầu thuê và quản lý giao dịch thuê.

Công việc:

- Thiết kế model RentalRequest và Rental.
- Triển khai API:
  - POST /rental-requests
  - PATCH /rental-requests/{requestId}
  - GET /rentals/{rentalId}
- Xử lý nghiệp vụ:
  - Tạo yêu cầu thuê.
  - Kiểm tra khoảng thời gian thuê.
  - Owner chấp nhận hoặc từ chối yêu cầu.
  - Tạo Rental khi yêu cầu được chấp nhận.
- Kiểm tra các trường hợp lỗi nghiệp vụ.

**Sản phẩm bàn giao:**

- RentalRequest module.
- Rental module.
- Các API xử lý nghiệp vụ thuê.

### Thành viên 3 — Frontend, Integration & Documentation

**Trách nhiệm chính:** Xây dựng giao diện demo, tích hợp API và chuẩn bị tài liệu dự án.

Công việc:

- Xây dựng giao diện React cơ bản.
- Tạo trang danh sách đồ cho thuê.
- Tạo trang chi tiết đồ cho thuê.
- Xây dựng giao diện gửi yêu cầu thuê.
- Xây dựng giao diện Owner duyệt yêu cầu.
- Tích hợp frontend với backend.
- Kiểm thử luồng nghiệp vụ end-to-end.
- Hoàn thiện README và tài liệu hướng dẫn demo.
- Chuẩn bị slide và kịch bản trình bày.

**Sản phẩm bàn giao:**

- React frontend.
- Giao diện demo các chức năng chính.
- README và tài liệu hướng dẫn.
- Slide Design Review và kịch bản demo.

## 3. Công việc chung

Cả ba thành viên cùng chịu trách nhiệm:

- Thống nhất API contract trước khi triển khai.
- Thống nhất quy ước đặt tên và cấu trúc dữ liệu.
- Sử dụng Git và GitHub để quản lý mã nguồn.
- Review code và hỗ trợ tích hợp giữa các module.
- Kiểm thử các chức năng trước khi bàn giao.
- Tham gia chuẩn bị và trình bày kết quả dự án.

## 4. Nguyên tắc phối hợp

- Mỗi thành viên làm việc trên branch riêng.
- Không tự ý thay đổi API contract đã thống nhất mà không trao đổi với nhóm.
- Mỗi chức năng cần được kiểm thử trước khi merge.
- Các module phải sử dụng chung định dạng response và error response.
- Thành viên phụ trách integration có trách nhiệm phối hợp kiểm tra toàn bộ luồng nghiệp vụ.

## 5. Kết quả mong đợi

Sau 4 tuần, nhóm cần hoàn thành:

- API contract có thể hiển thị và kiểm thử bằng Swagger UI.
- Backend triển khai được các chức năng cốt lõi.
- Frontend có thể thực hiện luồng thuê đồ cơ bản.
- Các module tích hợp và hoạt động thống nhất.
- Có tài liệu, kết quả kiểm thử và kịch bản demo hoàn chỉnh.
