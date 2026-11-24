
# RentMate — Product Backlog

## 1. Tổng quan

- **Project:** RentMate
- **Methodology:** Scrum-inspired
- **Timeline:** 4 tuần
- **Team size:** 3 thành viên

### Quy ước ưu tiên

| Priority | Ý nghĩa |
|---|---|
| P0 | Bắt buộc để hoàn thành MVP |
| P1 | Quan trọng, nên hoàn thành |
| P2 | Có thể bổ sung nếu còn thời gian |

### Trạng thái công việc

- TODO: Chưa thực hiện.
- IN PROGRESS: Đang thực hiện.
- REVIEW: Chờ kiểm tra.
- DONE: Hoàn thành.

## 2. Product Backlog

| ID | User Story / Task | Priority | Assignee |
|---|---|---|---|
| RM-01 | Phân tích bài toán và xác định phạm vi MVP | P0 | Cả nhóm |
| RM-02 | Xây dựng Project Brief | P0 | Thành viên 3 |
| RM-03 | Thiết kế Resource Model và ERD | P0 | Thành viên 1 |
| RM-04 | Thiết kế kiến trúc hệ thống | P0 | Cả nhóm |
| RM-05 | Xây dựng OpenAPI Contract | P0 | Thành viên 1 |
| RM-06 | Khởi tạo Git repository và cấu trúc dự án | P0 | Thành viên 3 |
| RM-07 | Xây dựng Flask backend cơ bản | P0 | Thành viên 1 |
| RM-08 | Xây dựng React frontend cơ bản | P0 | Thành viên 3 |
| RM-09 | Triển khai GET /items | P0 | Thành viên 1 |
| RM-10 | Triển khai GET /items/{itemId} | P0 | Thành viên 1 |
| RM-11 | Triển khai POST /rental-requests | P0 | Thành viên 2 |
| RM-12 | Triển khai PATCH /rental-requests/{requestId} | P0 | Thành viên 2 |
| RM-13 | Triển khai GET /rentals/{rentalId} | P0 | Thành viên 2 |
| RM-14 | Xây dựng chức năng tìm kiếm và lọc Item | P1 | Thành viên 1 |
| RM-15 | Tích hợp frontend với backend | P0 | Thành viên 3 |
| RM-16 | Kiểm thử các API và nghiệp vụ | P0 | Cả nhóm |
| RM-17 | Kiểm thử luồng thuê đồ end-to-end | P0 | Cả nhóm |
| RM-18 | Hoàn thiện README và tài liệu hướng dẫn | P1 | Thành viên 3 |
| RM-19 | Chuẩn bị slide Design Review | P0 | Cả nhóm |
| RM-20 | Chuẩn bị kịch bản demo | P0 | Thành viên 3 |

## 3. Kế hoạch thực hiện theo tuần

### Week 1 — Requirement Analysis & Design

**Mục tiêu:** Hoàn thành phân tích yêu cầu và thiết kế hệ thống.

- [ ] RM-01: Phân tích bài toán và phạm vi MVP.
- [ ] RM-02: Hoàn thiện Project Brief.
- [ ] RM-03: Thiết kế Resource Model và ERD.
- [ ] RM-04: Thiết kế kiến trúc hệ thống.
- [ ] RM-05: Xây dựng OpenAPI Contract.
- [ ] RM-06: Khởi tạo Git repository.

**Deliverables:**

- Project Brief.
- Resource Model.
- ERD.
- Architecture Diagram.
- OpenAPI Contract.
- Git repository.

### Week 2 — Backend & Frontend Development

**Mục tiêu:** Xây dựng các module cơ bản và triển khai API chính.

- [ ] RM-07: Khởi tạo Flask backend.
- [ ] RM-08: Khởi tạo React frontend.
- [ ] RM-09: Triển khai GET /items.
- [ ] RM-10: Triển khai GET /items/{itemId}.
- [ ] RM-11: Triển khai POST /rental-requests.
- [ ] RM-14: Xây dựng tìm kiếm và lọc Item.

**Deliverables:**

- Backend skeleton.
- Frontend skeleton.
- Item module.
- API tìm kiếm và tạo yêu cầu thuê ban đầu.

### Week 3 — Business Logic & Integration

**Mục tiêu:** Hoàn thiện nghiệp vụ thuê và tích hợp hệ thống.

- [ ] RM-12: Triển khai PATCH /rental-requests/{requestId}.
- [ ] RM-13: Triển khai GET /rentals/{rentalId}.
- [ ] RM-15: Tích hợp frontend với backend.
- [ ] RM-16: Kiểm thử API và nghiệp vụ.

**Deliverables:**

- RentalRequest module.
- Rental module.
- Frontend tích hợp backend.
- Kết quả kiểm thử API.

### Week 4 — Testing & Final Review

**Mục tiêu:** Hoàn thiện sản phẩm và chuẩn bị trình bày.

- [ ] RM-17: Kiểm thử luồng thuê đồ end-to-end.
- [ ] RM-18: Hoàn thiện README.
- [ ] RM-19: Chuẩn bị slide.
- [ ] RM-20: Chuẩn bị kịch bản demo.
- [ ] Review và sửa lỗi cuối cùng.

**Deliverables:**

- MVP hoàn chỉnh.
- README.
- Test results.
- Presentation slides.
- Demo scenario.

## 4. Definition of Done

Một công việc được xem là hoàn thành khi:

- Chức năng đáp ứng yêu cầu đã thống nhất.
- Code được commit và push lên GitHub.
- Không có lỗi nghiêm trọng trong quá trình kiểm thử.
- API tuân thủ OpenAPI contract.
- Có thể tích hợp với các module khác.
- Được thành viên phụ trách review.

## 5. MVP Acceptance Criteria

MVP được xem là đạt yêu cầu khi:

- Người dùng có thể xem danh sách đồ cho thuê.
- Người dùng có thể xem chi tiết một món đồ.
- Người thuê có thể gửi yêu cầu thuê với khoảng thời gian cụ thể.
- Chủ đồ có thể chấp nhận hoặc từ chối yêu cầu.
- Khi yêu cầu được chấp nhận, hệ thống tạo Rental tương ứng.
- Người dùng liên quan có thể xem thông tin giao dịch thuê.
- Hệ thống xử lý được các trường hợp dữ liệu không hợp lệ và xung đột lịch thuê.
    