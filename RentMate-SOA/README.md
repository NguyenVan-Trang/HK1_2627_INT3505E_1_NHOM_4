
# RentMate — Nền tảng cho thuê đồ dùng giữa các cá nhân

RentMate là nền tảng kết nối những người có đồ dùng chưa được sử dụng thường xuyên với những người có nhu cầu thuê. Hệ thống cho phép người dùng đăng tải đồ dùng, tìm kiếm sản phẩm, gửi yêu cầu thuê và theo dõi các giao dịch thuê.

Dự án được thực hiện trong khuôn khổ học phần **Kiến trúc hướng dịch vụ (Service-Oriented Architecture - SOA)**, tập trung vào phân tích yêu cầu, thiết kế RESTful API và xây dựng hệ thống có khả năng mở rộng.

---

## 1. Tổng quan dự án

### 1.1. Bài toán

Nhiều cá nhân sở hữu những đồ dùng chỉ sử dụng trong một khoảng thời gian ngắn như máy ảnh, thiết bị điện tử, dụng cụ thể thao hoặc đồ gia dụng.

Trong khi đó, những người có nhu cầu sử dụng các vật dụng này thường phải mua mới dù thời gian sử dụng không dài.

RentMate hướng đến giải quyết vấn đề bằng cách xây dựng một nền tảng kết nối người có đồ dùng cần cho thuê với người có nhu cầu thuê.

### 1.2. Chức năng chính

- Xem danh sách và tìm kiếm đồ dùng cho thuê.
- Xem thông tin chi tiết của từng món đồ.
- Gửi yêu cầu thuê với khoảng thời gian cụ thể.
- Chấp nhận hoặc từ chối yêu cầu thuê.
- Theo dõi thông tin các giao dịch thuê.

### 1.3. Các vai trò người dùng

- **Người thuê (Renter):** Tìm kiếm đồ dùng và gửi yêu cầu thuê.
- **Người cho thuê (Owner):** Đăng tải đồ dùng và xử lý các yêu cầu thuê.
- **Quản trị viên (Admin):** Quản lý và giám sát hoạt động của hệ thống.

Một tài khoản thông thường có thể vừa đóng vai trò người thuê, vừa đóng vai trò người cho thuê tùy theo thao tác.

---

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Giao diện người dùng | React |
| Backend | Python Flask |
| Kiểu API | RESTful API |
| Đặc tả API | OpenAPI 3.0.3 |
| Tài liệu API | Swagger UI |
| Cơ sở dữ liệu | SQLite |
| Kiểm thử API | Postman |
| Kiểm tra đặc tả API | Spectral |
| Quản lý mã nguồn | Git và GitHub |

---

## 3. Kiến trúc hệ thống

RentMate sử dụng kiến trúc **Modular Monolith kết hợp Layered Architecture**.

Các chức năng nghiệp vụ được tổ chức thành những module riêng biệt trong cùng một ứng dụng Backend. Đồng thời, hệ thống được chia thành các tầng để phân tách trách nhiệm và giúp việc bảo trì thuận tiện hơn.

### 3.1. Sơ đồ kiến trúc

```text
                 Người dùng
                     |
                     v
              React Frontend
                     |
                     v
                RESTful API
                     |
                     v
                Flask Backend
                     |
           +---------+---------+
           |         |         |
           v         v         v
         Item    RentalRequest Rental
         Module     Module     Module
           |         |         |
           +---------+---------+
                     |
                     v
                Service Layer
                     |
                     v
              Repository Layer
                     |
                     v
                  SQLite
```

### 3.2. Các tầng trong hệ thống

- **Presentation Layer:** Tiếp nhận yêu cầu từ giao diện React và trả kết quả cho người dùng.
- **Service Layer:** Xử lý logic nghiệp vụ như tạo yêu cầu thuê, kiểm tra lịch thuê và phê duyệt yêu cầu.
- **Repository Layer:** Thực hiện các thao tác truy vấn và cập nhật dữ liệu.
- **Database Layer:** Lưu trữ thông tin người dùng, đồ dùng, yêu cầu thuê và giao dịch thuê.

---

## 4. Các API chính

Địa chỉ cơ sở của API: `http://localhost:5000/api/v1`. Mock server (Prism) chạy tại `http://localhost:4010`.

| Nhóm | Phương thức | Endpoint | Chức năng |
|---|---|---|---|
| Auth | POST | `/auth/register` | Đăng ký tài khoản |
| Auth | POST | `/auth/login` | Đăng nhập, nhận Bearer token |
| Items | GET | `/items` | Tìm kiếm, lọc, sắp xếp, phân trang đồ cho thuê |
| Items | POST | `/items` | Đăng đồ cho thuê |
| Items | GET | `/items/{itemId}` | Xem chi tiết một món đồ |
| Items | PATCH | `/items/{itemId}` | Cập nhật hoặc ngừng đăng (ACTIVE/INACTIVE) |
| Rental Requests | GET | `/rental-requests` | Danh sách yêu cầu của tôi (renter hoặc owner) |
| Rental Requests | POST | `/rental-requests` | Tạo yêu cầu thuê |
| Rental Requests | PATCH | `/rental-requests/{requestId}` | Duyệt, từ chối hoặc hủy yêu cầu |
| Rentals | GET | `/rentals` | Danh sách giao dịch thuê của tôi |
| Rentals | GET | `/rentals/{rentalId}` | Xem giao dịch thuê |
| Rentals | PATCH | `/rentals/{rentalId}` | Xác nhận bàn giao, hoàn trả hoặc hủy |

Quy ước: dữ liệu trả về nằm trong `data`, danh sách có thêm `pagination`; mọi lỗi dùng chung `ErrorResponse` (`error.code`, `error.message`, `error.details`). Mã lỗi: 400 sai định dạng, 401 chưa xác thực, 403 không có quyền, 404 không tìm thấy, 409 xung đột trạng thái hoặc lịch thuê, 422 vi phạm quy tắc nghiệp vụ.

Đặc tả chi tiết: `api/openapi.yaml`.

## 5. Luồng nghiệp vụ chính

Quy trình thuê đồ dùng trên RentMate gồm các bước:

1. Người thuê truy cập danh sách đồ dùng thông qua API `GET /items`.
2. Người thuê lựa chọn một món đồ và xem thông tin chi tiết.
3. Người thuê gửi yêu cầu thuê thông qua API `POST /rental-requests`.
4. Người cho thuê xem xét và chấp nhận hoặc từ chối yêu cầu.
5. Nếu yêu cầu được chấp nhận, hệ thống tạo một giao dịch thuê tương ứng.
6. Người thuê và người cho thuê có thể xem thông tin giao dịch thông qua API `GET /rentals/{rentalId}`.

---

## 6. Cấu trúc dự án

```text
RentMate-SOA/
├── README.md
├── .spectral.yaml
├── api/
│   ├── openapi.yaml
│   └── swagger-ui.html
├── docs/
│   ├── project-brief.md
│   ├── resource-model.md
│   ├── erd.md
│   ├── architecture.md
│   └── project-plan.md
└── project/
    ├── backlog.md
    ├── team-assignment.md
    ├── milestone.md
    └── project-progress.md
```

Trong quá trình phát triển, nhóm sẽ bổ sung các thư mục `frontend/` và `backend/`.

---

## 7. Phạm vi phiên bản MVP

### 7.1. Chức năng nằm trong phạm vi

- Xem và tìm kiếm đồ dùng cho thuê.
- Xem thông tin chi tiết đồ dùng.
- Gửi yêu cầu thuê.
- Chấp nhận hoặc từ chối yêu cầu thuê.
- Tạo và xem thông tin giao dịch thuê.
- Kiểm tra khoảng thời gian thuê và các điều kiện nghiệp vụ cơ bản.

### 7.2. Chức năng chưa triển khai

- Tích hợp thanh toán trực tuyến.
- Quản lý vận chuyển và giao nhận.
- Trò chuyện thời gian thực.
- Xác minh danh tính người dùng.
- Bảo hiểm và xử lý tranh chấp phức tạp.
- Hệ thống gợi ý đồ dùng.
- Ứng dụng di động độc lập.

---

## 8. Kế hoạch phát triển

| Tuần | Nội dung công việc |
|---|---|
| Tuần 1 | Phân tích yêu cầu và thiết kế API |
| Tuần 2 | Xây dựng Backend và Frontend |
| Tuần 3 | Hoàn thiện nghiệp vụ và tích hợp hệ thống |
| Tuần 4 | Kiểm thử và hoàn thiện sản phẩm |

Chi tiết công việc và phân công thành viên được quản lý trong:

```text
project/backlog.md
project/team-assignment.md
```

---

## 9. Hướng dẫn xem đặc tả API

Chạy từ thư mục `RentMate-SOA/`.

**Swagger UI:**

```bash
cd api
python -m http.server 8080
```

Mở `http://localhost:8080/swagger-ui.html`.

**Mock server (Prism), không cần backend:**

```bash
npx @stoplight/prism-cli mock api/openapi.yaml -p 4010
curl "http://localhost:4010/items"
```

**Kiểm tra chất lượng contract (Spectral):**

```bash
npx @stoplight/spectral-cli lint api/openapi.yaml --ruleset .spectral.yaml
```

Hướng dẫn cài đặt và chạy Frontend, Backend sẽ được bổ sung khi nhóm hoàn thành phần triển khai.

---

## 10. Phân công thành viên

| Thành viên | Nhiệm vụ chính |
|---|---|
| Thành viên 1 | Thiết kế API và xây dựng Backend quản lý đồ dùng |
| Thành viên 2 | Xây dựng nghiệp vụ yêu cầu thuê và giao dịch thuê |
| Thành viên 3 | Xây dựng Frontend, tích hợp hệ thống và tài liệu |

---

## 11. Trạng thái dự án

**Giai đoạn hiện tại:** Phân tích yêu cầu và thiết kế hệ thống (Design Review).

### Các nội dung đã chuẩn bị

- [x] Đề cương dự án (Project Brief).
- [x] Mô hình tài nguyên (Resource Model).
- [x] Sơ đồ thực thể và mối quan hệ (ERD).
- [x] Thiết kế kiến trúc hệ thống.
- [x] Đặc tả API bằng OpenAPI (12 operation, Spectral không lỗi).
- [x] Swagger UI và mock server (Prism).
- [x] Phân công công việc nhóm.
- [x] Danh sách công việc cần thực hiện (Backlog).
- [x] Kế hoạch tuần 13–15 và mốc dự án.

### Các nội dung chưa thực hiện

- [ ] Xây dựng Backend.
- [ ] Xây dựng Frontend.
- [ ] Tích hợp các module.
- [ ] Kiểm thử toàn bộ luồng nghiệp vụ.
- [ ] Hoàn thiện bản trình diễn cuối cùng.

---

## 12. Mục đích dự án

RentMate được xây dựng nhằm vận dụng kiến thức của học phần SOA vào quá trình phân tích, thiết kế và phát triển một hệ thống phần mềm thực tế.

Thông qua dự án, nhóm hướng đến việc xây dựng một hệ thống có API rõ ràng, các module nghiệp vụ được phân chia hợp lý và có khả năng mở rộng trong tương lai.

**Dự án phục vụ mục đích học tập và nghiên cứu trong khuôn khổ học phần Service-Oriented Architecture.**
