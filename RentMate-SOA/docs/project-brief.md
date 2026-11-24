
# RentMate — Đề cương dự án (Project Brief)

**Tuần 12 — Phân tích yêu cầu và thiết kế API (Design Review)**

---

## 1. Tổng quan dự án

**RentMate** là nền tảng cho thuê đồ dùng giữa các cá nhân (*Peer-to-Peer Rental Platform*), kết nối những người sở hữu đồ dùng chưa được sử dụng thường xuyên với những người có nhu cầu thuê và sử dụng chúng trong một khoảng thời gian nhất định.

Người sở hữu có thể đăng đồ dùng lên nền tảng để cho thuê, trong khi người thuê có thể tìm kiếm sản phẩm, lựa chọn thời gian thuê, gửi yêu cầu thuê và theo dõi quá trình thuê. Hệ thống hướng đến việc giúp người dùng tiếp cận đồ dùng cần thiết mà không phải bỏ ra chi phí mua mới.

## 2. Bài toán thực tế (Problem Statement)

Trong cuộc sống, nhiều người có nhu cầu sử dụng các đồ dùng như máy ảnh, thiết bị điện tử, dụng cụ thể thao, đồ cắm trại hoặc dụng cụ sửa chữa nhưng chỉ trong thời gian ngắn. Việc mua mới những đồ dùng này có thể tốn kém và không hiệu quả khi chúng chỉ được sử dụng một vài lần.

Ngược lại, nhiều người sở hữu các đồ dùng có giá trị nhưng không sử dụng thường xuyên, dẫn đến lãng phí tài nguyên và không tận dụng được giá trị của chúng.

Việc cho thuê và thuê đồ giữa các cá nhân cũng có thể gặp khó khăn trong việc tìm kiếm đồ dùng phù hợp, xác định thời gian sẵn sàng, quản lý yêu cầu thuê, xác nhận giao nhận và theo dõi trạng thái hoàn trả.

RentMate giải quyết vấn đề trên bằng cách cung cấp một nền tảng tập trung, hỗ trợ quản lý danh sách đồ dùng cho thuê và quy trình thuê từ lúc gửi yêu cầu đến khi hoàn tất trả đồ.

## 3. Giải pháp đề xuất (Proposed Solution)

RentMate cung cấp một nền tảng trực tuyến cho phép người dùng tham gia vào hai hoạt động chính: cho thuê đồ dùng và thuê đồ dùng.

Các chức năng chính của hệ thống:

- **Quản lý tài khoản:** Người dùng có thể đăng ký, đăng nhập và quản lý thông tin cá nhân.
- **Quản lý đồ cho thuê:** Chủ sở hữu có thể đăng tải, cập nhật và ngừng đăng tải các món đồ.
- **Tìm kiếm đồ dùng:** Người thuê có thể tìm kiếm và lọc đồ dùng theo tên, danh mục và mức giá.
- **Gửi yêu cầu thuê:** Người thuê lựa chọn món đồ, khoảng thời gian thuê và gửi yêu cầu đến chủ sở hữu.
- **Xử lý yêu cầu:** Chủ sở hữu có thể chấp nhận hoặc từ chối yêu cầu thuê.
- **Quản lý giao dịch:** Hệ thống theo dõi trạng thái giao dịch từ khi được xác nhận đến khi bàn giao và hoàn trả đồ dùng.

## 4. Người dùng và API Consumers

### 4.1. Nhóm người dùng (User Roles)

| Đối tượng | Vai trò | Quyền hạn chính |
|---|---|---|
| Renter | Người thuê | Tìm kiếm đồ dùng, gửi yêu cầu thuê và theo dõi giao dịch |
| Owner | Người cho thuê | Đăng tải đồ dùng, quản lý danh sách và xử lý yêu cầu thuê |
| Admin | Quản trị viên | Quản lý và giám sát hoạt động của hệ thống |

Một người dùng có thể vừa là người thuê vừa là người cho thuê tùy theo từng giao dịch.

### 4.2. API Consumers

Các đối tượng sử dụng API của RentMate:

- **Web Frontend:** Ứng dụng giao diện chính dành cho người thuê và người cho thuê, sử dụng REST API để lấy dữ liệu và thực hiện các thao tác nghiệp vụ.
- **Admin Web:** Giao diện quản trị dành cho Admin, sử dụng các API phục vụ quản lý và giám sát hệ thống trong phạm vi được triển khai.
- **Mobile Application:** Ứng dụng di động có thể sử dụng chung API trong tương lai, nhưng chưa nằm trong phạm vi MVP.

Web Frontend là API Consumer chính trong phiên bản đầu tiên của RentMate.

## 5. Các trường hợp sử dụng chính (Use Cases)

### UC01 — Tìm kiếm đồ dùng

Người thuê có thể xem danh sách đồ dùng đang được đăng tải và tìm kiếm theo tên, danh mục hoặc khoảng giá.

**Luồng cơ bản:**

1. Người thuê truy cập danh sách đồ dùng.
2. Hệ thống trả về các món đồ đang hoạt động.
3. Người thuê nhập từ khóa hoặc chọn bộ lọc.
4. Hệ thống trả về danh sách kết quả phù hợp.
5. Người thuê chọn một món đồ để xem thông tin chi tiết.

### UC02 — Quản lý đồ cho thuê

Chủ sở hữu có thể đăng tải và quản lý các món đồ của mình.

**Luồng cơ bản:**

1. Chủ sở hữu đăng nhập vào hệ thống.
2. Chủ sở hữu tạo một tin đăng mới.
3. Hệ thống kiểm tra dữ liệu và lưu thông tin món đồ.
4. Chủ sở hữu có thể cập nhật thông tin hoặc ngừng đăng tải món đồ.

### UC03 — Gửi yêu cầu thuê

Người thuê có thể gửi yêu cầu thuê một món đồ trong khoảng thời gian mong muốn.

**Luồng cơ bản:**

1. Người thuê chọn món đồ cần thuê.
2. Người thuê lựa chọn ngày bắt đầu và ngày kết thúc.
3. Người thuê nhập lời nhắn nếu cần.
4. Hệ thống kiểm tra trạng thái món đồ và tính hợp lệ của khoảng thời gian thuê.
5. Hệ thống tạo yêu cầu thuê với trạng thái PENDING.
6. Chủ sở hữu có thể xem yêu cầu mới.

### UC04 — Chấp nhận hoặc từ chối yêu cầu

Chủ sở hữu có thể xem và xử lý các yêu cầu thuê đối với món đồ của mình.

**Luồng cơ bản:**

1. Chủ sở hữu xem danh sách yêu cầu thuê.
2. Chủ sở hữu chọn một yêu cầu đang chờ xử lý.
3. Chủ sở hữu chấp nhận hoặc từ chối yêu cầu.
4. Hệ thống cập nhật trạng thái yêu cầu.
5. Nếu yêu cầu được chấp nhận, hệ thống tạo một giao dịch thuê tương ứng.

### UC05 — Quản lý quá trình thuê và hoàn trả

Người thuê và chủ sở hữu có thể theo dõi trạng thái giao dịch thuê.

**Luồng cơ bản:**

1. Giao dịch được tạo sau khi yêu cầu thuê được chấp nhận.
2. Chủ sở hữu xác nhận việc bàn giao đồ dùng.
3. Hệ thống chuyển trạng thái giao dịch sang ACTIVE.
4. Sau khi kết thúc thời gian thuê, chủ sở hữu xác nhận việc hoàn trả.
5. Hệ thống chuyển trạng thái giao dịch sang COMPLETED.

## 6. Phạm vi MVP (Minimum Viable Product)

MVP tập trung xây dựng các chức năng thiết yếu để hoàn thành quy trình cho thuê cơ bản.

### 6.1. Chức năng trong phạm vi MVP

| Nhóm chức năng | Nội dung |
|---|---|
| Xác thực | Đăng ký, đăng nhập và xác thực người dùng |
| Quản lý tài khoản | Lưu trữ thông tin người dùng cơ bản |
| Quản lý đồ cho thuê | Tạo, xem, cập nhật và ngừng đăng tải món đồ |
| Tìm kiếm | Tìm kiếm và lọc đồ dùng theo tên, danh mục và giá |
| Yêu cầu thuê | Tạo và xem yêu cầu thuê |
| Xử lý yêu cầu | Chấp nhận hoặc từ chối yêu cầu thuê |
| Quản lý giao dịch | Xác nhận bàn giao và hoàn trả đồ dùng |
| API Contract | Đặc tả API bằng OpenAPI và kiểm thử qua Swagger UI |

### 6.2. Chức năng ngoài phạm vi MVP (Out of Scope)

Các chức năng sau chưa được triển khai trong phiên bản đầu tiên:

- Thanh toán trực tuyến và hoàn tiền.
- Tích hợp dịch vụ vận chuyển và giao hàng.
- Nhắn tin thời gian thực giữa người thuê và người cho thuê.
- Xác minh danh tính người dùng.
- Bảo hiểm đồ dùng cho thuê.
- Quản lý khiếu nại và tranh chấp phức tạp.
- Hệ thống gợi ý đồ dùng dựa trên sở thích người dùng.
- Ứng dụng di động độc lập.

## 7. Quy trình nghiệp vụ chính (Main Business Flow)

Quy trình thuê đồ cơ bản của RentMate gồm các bước:

1. Người cho thuê đăng tải một món đồ lên hệ thống.
2. Người thuê tìm kiếm và xem thông tin món đồ.
3. Người thuê gửi yêu cầu thuê với khoảng thời gian cụ thể.
4. Chủ sở hữu xem và chấp nhận hoặc từ chối yêu cầu.
5. Nếu được chấp nhận, hệ thống tạo giao dịch thuê.
6. Chủ sở hữu xác nhận bàn giao đồ dùng.
7. Sau khi sử dụng, chủ sở hữu xác nhận hoàn trả.
8. Hệ thống cập nhật giao dịch sang trạng thái hoàn tất.

**Luồng trạng thái yêu cầu thuê:**

`PENDING → APPROVED`

`PENDING → REJECTED`

`PENDING → CANCELLED`

**Luồng trạng thái giao dịch:**

`CONFIRMED → ACTIVE → COMPLETED`

`CONFIRMED → CANCELLED`

## 8. Định hướng thiết kế hệ thống

### 8.1. Kiến trúc

RentMate sử dụng kiến trúc **Modular Monolith kết hợp Layered Architecture**.

Các module nghiệp vụ chính:

- Authentication Module: Xác thực và quản lý tài khoản.
- Item Module: Quản lý đồ dùng cho thuê.
- Rental Request Module: Quản lý yêu cầu thuê.
- Rental Module: Quản lý giao dịch thuê.

Các module được tổ chức trong cùng một ứng dụng backend nhưng phân tách trách nhiệm rõ ràng.

### 8.2. Công nghệ dự kiến

| Thành phần | Công nghệ |
|---|---|
| Frontend | React |
| Backend | Python Flask |
| API Style | RESTful API |
| API Specification | OpenAPI 3.0.3 |
| API Documentation | Swagger UI |
| Database | SQLite (MVP) |
| Kiểm thử API | Postman / Swagger UI |
| Kiểm tra API Contract | Spectral |
| Quản lý mã nguồn | Git / GitHub |

### 8.3. Các tài nguyên chính

API tập trung vào bốn tài nguyên cốt lõi:

- `/users`: Quản lý người dùng.
- `/items`: Quản lý đồ dùng cho thuê.
- `/rental-requests`: Quản lý yêu cầu thuê.
- `/rentals`: Quản lý giao dịch thuê.

Các API xác thực được tổ chức dưới đường dẫn `/auth`.

## 9. Ràng buộc và giả định

- Hệ thống được phát triển trong phạm vi một bài tập lớn học phần SOA.
- Thời gian triển khai dự kiến là 4 tuần.
- Quy mô nhóm gồm 3 thành viên.
- Phiên bản MVP ưu tiên hoàn thiện quy trình nghiệp vụ cốt lõi thay vì triển khai đầy đủ các chức năng thương mại.
- Một người dùng có thể tham gia với vai trò người thuê hoặc người cho thuê.
- Việc xác nhận giao nhận và hoàn trả được đơn giản hóa, do chủ sở hữu thực hiện trong MVP.
- Hệ thống chưa xử lý thanh toán thực tế.
- SQLite được sử dụng trong giai đoạn MVP nhằm đơn giản hóa quá trình phát triển và kiểm thử.

## 10. Tiêu chí đánh giá thành công

Dự án được xem là đạt mục tiêu MVP khi đáp ứng các tiêu chí sau:

- Người dùng có thể đăng ký và đăng nhập.
- Chủ sở hữu có thể đăng tải và quản lý đồ dùng.
- Người thuê có thể tìm kiếm và xem chi tiết đồ dùng.
- Người thuê có thể gửi yêu cầu thuê với khoảng thời gian cụ thể.
- Chủ sở hữu có thể chấp nhận hoặc từ chối yêu cầu.
- Hệ thống có thể tạo giao dịch sau khi yêu cầu được chấp nhận.
- Hệ thống hỗ trợ cập nhật trạng thái bàn giao và hoàn trả.
- API được đặc tả đầy đủ bằng OpenAPI.
- Các API chính có thể được kiểm thử thông qua Swagger UI hoặc Postman.
- Có tài liệu hướng dẫn, sơ đồ thiết kế và báo cáo tiến độ dự án.

## 11. Kết luận

RentMate hướng đến giải quyết nhu cầu thuê và cho thuê đồ dùng giữa các cá nhân thông qua một nền tảng trực tuyến tập trung.

Trong phạm vi MVP, dự án tập trung vào quy trình nghiệp vụ cốt lõi từ đăng tải đồ dùng, tìm kiếm, gửi yêu cầu thuê, xử lý yêu cầu đến quản lý giao dịch và hoàn trả.

Việc xác định rõ người dùng, API Consumers, Use Cases và phạm vi MVP tạo cơ sở cho các bước tiếp theo, bao gồm thiết kế mô hình tài nguyên, xây dựng ERD, thiết kế kiến trúc và đặc tả API Contract bằng OpenAPI.
