# RentMate — Báo cáo tiến độ và kế hoạch tuần tiếp theo

**Dự án:** RentMate — Peer-to-Peer Rental Platform  
**Tuần báo cáo:** Tuần 12 — Design Review  
**Quy mô nhóm:** 3 thành viên  
**Thời gian dự án:** 4 tuần  

---

## 1. Mục tiêu trong tuần

- Phân tích bài toán và xác định đối tượng người dùng của RentMate.
- Xác định phạm vi MVP và các chức năng ưu tiên.
- Xây dựng mô hình tài nguyên và quan hệ dữ liệu.
- Lựa chọn kiến trúc phần mềm phù hợp với quy mô dự án.
- Thiết kế API Contract và phân chia nhiệm vụ cho các thành viên.
- Chuẩn bị nội dung Design Review.

---

## 2. Công việc đã thực hiện

### 2.1. Phân tích yêu cầu

- Xác định bài toán cho thuê đồ dùng giữa các cá nhân.
- Xác định các nhóm người dùng: Renter, Owner và Admin.
- Xác định các Use Case chính:
  - UC01: Browse/Search Items.
  - UC02: Manage Rental Listings.
  - UC03: Create Rental Request.
  - UC04: Approve/Reject Rental Request.
  - UC05: Track Rental.
- Xác định phạm vi MVP và các chức năng chưa triển khai trong phiên bản đầu.

### 2.2. Thiết kế hệ thống

- Lựa chọn kiến trúc Modular Monolith kết hợp Layered Architecture.
- Xác định các thành phần chính:
  - React Frontend.
  - Flask Backend.
  - Service Layer.
  - Repository Layer.
  - SQLite Database.
- Xây dựng Resource Model gồm:
  - User.
  - Item.
  - RentalRequest.
  - Rental.
- Xác định mối quan hệ giữa các tài nguyên và các quy tắc nghiệp vụ cơ bản.

### 2.3. Thiết kế API

- Xây dựng API Contract theo OpenAPI 3.0.3.
- Xác định các endpoint ưu tiên cho luồng nghiệp vụ thuê đồ.
- Thống nhất cách sử dụng RESTful API, JSON và UUID.
- Xác định cơ chế xác thực Bearer Token cho các API cần quyền truy cập.

### 2.4. Quản lý dự án

- Phân chia nhiệm vụ giữa 3 thành viên.
- Xác định backlog và mức độ ưu tiên.
- Xây dựng kế hoạch phát triển trong 4 tuần.
- Chuẩn bị nội dung trình bày Design Review.

---

## 3. Công việc chưa hoàn thành

| Công việc | Trạng thái | Ghi chú |
|---|---|---|
| Khởi tạo Backend Flask | Chưa hoàn thành | Cần tạo cấu trúc dự án |
| Thiết lập Database | Chưa hoàn thành | Dự kiến sử dụng SQLite |
| Triển khai Item API | Chưa hoàn thành | GET list và GET detail |
| Triển khai RentalRequest API | Chưa hoàn thành | Tạo và xử lý yêu cầu |
| Triển khai Rental API | Chưa hoàn thành | Xem giao dịch thuê |
| Khởi tạo React Frontend | Chưa hoàn thành | Xây dựng giao diện cơ bản |
| Tích hợp Frontend/Backend | Chưa hoàn thành | Chờ API và giao diện |
| Kiểm thử nghiệp vụ | Chưa hoàn thành | Thực hiện sau khi có API |
| Kiểm thử End-to-End | Chưa hoàn thành | Kiểm thử luồng thuê hoàn chỉnh |

---

## 4. Nhiệm vụ cá nhân

### Thành viên 1 — API Design & Backend Core

**Đã thực hiện:**
- Tham gia phân tích yêu cầu và phạm vi MVP.
- Xây dựng Resource Model và API Contract.
- Xác định cấu trúc Item và các quy tắc quản lý listing.

**Chưa hoàn thành:**
- Khởi tạo Backend.
- Thiết lập Flask và SQLite.
- Triển khai GET `/items`.
- Triển khai GET `/items/{itemId}`.
- Xây dựng chức năng tìm kiếm và lọc cơ bản.

**Kế hoạch tuần tới:**
- Khởi tạo Backend project.
- Thiết lập cấu trúc Layered Architecture.
- Tạo database và dữ liệu mẫu.
- Hoàn thiện Item API.
- Kiểm thử API bằng Postman.

---

### Thành viên 2 — Rental Business Logic

**Đã thực hiện:**
- Tham gia phân tích luồng thuê đồ dùng.
- Xác định tài nguyên RentalRequest và Rental.
- Xác định các trạng thái và quy tắc nghiệp vụ cơ bản.

**Chưa hoàn thành:**
- Triển khai POST `/rental-requests`.
- Triển khai PATCH `/rental-requests/{requestId}`.
- Triển khai GET `/rentals/{rentalId}`.
- Kiểm tra xung đột thời gian thuê.
- Xử lý việc tạo Rental sau khi yêu cầu được chấp nhận.

**Kế hoạch tuần tới:**
- Xây dựng RentalRequest và Rental Model.
- Triển khai chức năng tạo yêu cầu thuê.
- Xây dựng approve/reject request.
- Kiểm tra ngày thuê và xung đột lịch.
- Đảm bảo một yêu cầu được duyệt chỉ tạo tối đa một Rental.

---

### Thành viên 3 — Frontend, Integration & Documentation

**Đã thực hiện:**
- Tham gia xác định người dùng và luồng tương tác.
- Xây dựng Project Brief.
- Chuẩn bị cấu trúc tài liệu dự án.
- Phân chia backlog và kế hoạch phát triển.
- Chuẩn bị nội dung Design Review.

**Chưa hoàn thành:**
- Khởi tạo React Frontend.
- Xây dựng giao diện danh sách đồ dùng.
- Xây dựng trang chi tiết đồ dùng.
- Xây dựng form tạo yêu cầu thuê.
- Tích hợp với Backend.
- Hoàn thiện README và hướng dẫn chạy dự án.

**Kế hoạch tuần tới:**
- Khởi tạo React project.
- Xây dựng giao diện trang danh sách đồ dùng.
- Xây dựng trang chi tiết Item.
- Tạo form gửi yêu cầu thuê.
- Tích hợp GET `/items` và GET `/items/{itemId}` khi Backend sẵn sàng.
- Cập nhật README về cách cài đặt và chạy dự án.

---

## 5. Vấn đề cần hỗ trợ

- Thống nhất API Response Format và Error Response giữa các thành viên.
- Thống nhất cấu trúc thư mục và cách tổ chức các Layer.
- Xác định rõ quyền truy cập của Renter, Owner và Admin.
- Làm rõ cách xử lý các yêu cầu thuê có khoảng thời gian trùng nhau.
- Đảm bảo việc duyệt yêu cầu và tạo Rental được xử lý nhất quán.
- Hỗ trợ thành viên trong quá trình tích hợp Frontend và Backend.
- Review code và kiểm thử các API sau khi triển khai.

---

## 6. Kế hoạch thực tế cho tuần tiếp theo

### Mục tiêu tuần

Hoàn thiện nền tảng Backend và Frontend cơ bản, đồng thời triển khai các API trọng tâm để bắt đầu tích hợp luồng thuê đồ dùng.

| Nhiệm vụ | Người phụ trách | Kết quả mong đợi | Ưu tiên |
|---|---|---|---|
| Khởi tạo Flask Backend | Thành viên 1 | Backend chạy ổn định | P0 |
| Thiết lập SQLite và Model Item | Thành viên 1 | Database và dữ liệu mẫu | P0 |
| GET `/items` | Thành viên 1 | Trả về danh sách Item | P0 |
| GET `/items/{itemId}` | Thành viên 1 | Trả về chi tiết Item | P0 |
| RentalRequest Model | Thành viên 2 | Model và trạng thái request | P0 |
| POST `/rental-requests` | Thành viên 2 | Tạo Rental Request | P0 |
| PATCH `/rental-requests/{requestId}` | Thành viên 2 | Approve/Reject Request | P0 |
| Rental Model và GET `/rentals/{rentalId}` | Thành viên 2 | Tạo và xem Rental | P0 |
| Khởi tạo React | Thành viên 3 | Frontend chạy được | P0 |
| Trang danh sách Item | Thành viên 3 | Hiển thị Item | P0 |
| Trang chi tiết Item | Thành viên 3 | Hiển thị thông tin Item | P0 |
| Form Rental Request | Thành viên 3 | Gửi yêu cầu thuê từ UI | P1 |
| Tích hợp API và Frontend | Thành viên 3 + cả nhóm | Luồng dữ liệu cơ bản | P0 |
| Kiểm thử API | Cả nhóm | Các API chính hoạt động | P0 |
| Review và cập nhật tài liệu | Cả nhóm | Tài liệu đồng bộ với triển khai | P1 |

---

## 7. Tiêu chí hoàn thành cuối tuần

- Backend có thể khởi động và kết nối SQLite.
- Item API có thể trả về dữ liệu mẫu.
- Rental Request có thể được tạo và xử lý.
- Khi yêu cầu được chấp nhận, Rental được tạo theo đúng quy tắc.
- Frontend hiển thị được danh sách và chi tiết Item.
- Frontend có thể gọi Backend thông qua API.
- Các thành viên có thể chạy dự án trên môi trường local.
- Có kiểm thử các API trọng tâm bằng Postman.
- Các thay đổi được commit và push lên GitHub.

---

## 8. Kết luận

Trong tuần 12, nhóm tập trung vào phân tích yêu cầu,
xác định phạm vi MVP, thiết kế tài nguyên, kiến trúc hệ thống
và API Contract cho RentMate.

Trong tuần tiếp theo, nhóm chuyển trọng tâm sang triển khai,
ưu tiên Backend Core, Rental Business Logic và Frontend cơ bản.
Mục tiêu là tạo ra các thành phần có thể chạy độc lập,
sau đó tích hợp để hoàn thiện luồng thuê đồ dùng cốt lõi.

Các nhiệm vụ được phân chia theo trách nhiệm của từng thành viên,
đồng thời dành thời gian chung cho review, tích hợp và kiểm thử
để đảm bảo tiến độ dự án trong thời gian 4 tuần.