# RentMate — Mô hình tài nguyên (Resource Model)

**Tuần 12 — Phân tích yêu cầu và thiết kế API (Design Review)**


## 1. Tổng quan

RentMate là nền tảng cho thuê đồ dùng giữa các cá nhân (*Peer-to-Peer Rental Platform*), cho phép người sở hữu đăng tải những món đồ chưa được sử dụng thường xuyên để cho người khác thuê trong một khoảng thời gian nhất định.

Hệ thống sử dụng thiết kế REST API theo hướng tài nguyên (*Resource-oriented API*). Mỗi thực thể nghiệp vụ chính được biểu diễn thành một tài nguyên riêng biệt, có định danh duy nhất và vòng đời cụ thể.

Các quy ước thiết kế API:

- Tên tài nguyên sử dụng danh từ số nhiều.
- Tên tài nguyên viết thường và sử dụng dấu gạch ngang nếu cần.
- Mỗi tài nguyên có một định danh duy nhất dạng UUID.
- Dữ liệu trao đổi giữa client và server sử dụng định dạng JSON.
- Đường dẫn API có tiền tố `/api/v1`.
- Tên thuộc tính JSON sử dụng quy tắc camelCase.

## 2. Các tài nguyên chính

Trong phạm vi MVP, hệ thống RentMate sử dụng bốn tài nguyên chính:

- User (Người dùng).
- Item (Đồ cho thuê).
- RentalRequest (Yêu cầu thuê).
- Rental (Giao dịch thuê).

### 2.1. User — Người dùng

Đại diện cho người dùng đã đăng ký tài khoản trên hệ thống. Một người dùng có thể đóng vai trò người thuê hoặc người cho thuê tùy theo hoạt động của họ trên nền tảng.

| Thuộc tính | Kiểu dữ liệu | Mô tả |
|---|---|---|
| userId | UUID | Định danh duy nhất của người dùng |
| fullName | String | Họ và tên |
| email | String | Địa chỉ email duy nhất |
| passwordHash | String | Mật khẩu đã được mã hóa |
| role | Enum | Vai trò: RENTER, OWNER, ADMIN |
| createdAt | DateTime | Thời điểm tạo tài khoản |

**Chức năng:**

- Đăng ký và xác thực tài khoản.
- Quản lý thông tin cá nhân cơ bản.
- Xác định người thuê và người cho thuê.
- Cung cấp thông tin người dùng phục vụ kiểm tra quyền truy cập.

### 2.2. Item — Đồ cho thuê

Đại diện cho một món đồ được chủ sở hữu đăng tải lên hệ thống để cho người khác thuê.

| Thuộc tính | Kiểu dữ liệu | Mô tả |
|---|---|---|
| itemId | UUID | Định danh duy nhất của món đồ |
| ownerId | UUID | ID của người sở hữu món đồ |
| title | String | Tên món đồ |
| description | String | Mô tả chi tiết |
| category | String | Danh mục món đồ |
| dailyPrice | Decimal | Giá thuê mỗi ngày |
| deposit | Decimal | Tiền đặt cọc |
| status | Enum | Trạng thái: ACTIVE, INACTIVE |
| createdAt | DateTime | Thời điểm đăng tải |

**Chức năng:**

- Cho phép chủ sở hữu đăng tải món đồ.
- Cập nhật thông tin và giá thuê.
- Ngừng cung cấp món đồ bằng cách chuyển trạng thái sang INACTIVE.
- Cho phép người thuê tìm kiếm và xem thông tin món đồ.
- Không cho phép tạo yêu cầu thuê đối với món đồ đã ngừng hoạt động.

### 2.3. RentalRequest — Yêu cầu thuê

Đại diện cho yêu cầu thuê một món đồ do người thuê gửi đến chủ sở hữu trong một khoảng thời gian cụ thể.

| Thuộc tính | Kiểu dữ liệu | Mô tả |
|---|---|---|
| requestId | UUID | Định danh duy nhất của yêu cầu |
| itemId | UUID | ID món đồ được yêu cầu thuê |
| renterId | UUID | ID người gửi yêu cầu |
| startDate | Date | Ngày bắt đầu thuê |
| endDate | Date | Ngày kết thúc thuê |
| status | Enum | PENDING, APPROVED, REJECTED, CANCELLED |
| message | String | Lời nhắn gửi chủ sở hữu (không bắt buộc) |
| createdAt | DateTime | Thời điểm tạo yêu cầu |

**Chức năng:**

- Ghi nhận yêu cầu thuê từ người dùng.
- Theo dõi trạng thái xử lý yêu cầu.
- Cho phép chủ sở hữu chấp nhận hoặc từ chối yêu cầu.
- Kiểm tra tính hợp lệ của khoảng thời gian thuê.
- Kiểm tra khả năng cho thuê của món đồ.
- Lưu trữ lịch sử các yêu cầu thuê.

### 2.4. Rental — Giao dịch thuê

Đại diện cho một giao dịch thuê thực tế được tạo ra sau khi chủ sở hữu chấp nhận yêu cầu thuê.

| Thuộc tính | Kiểu dữ liệu | Mô tả |
|---|---|---|
| rentalId | UUID | Định danh duy nhất của giao dịch |
| requestId | UUID | ID yêu cầu thuê ban đầu |
| itemId | UUID | ID món đồ được thuê |
| renterId | UUID | ID người thuê |
| ownerId | UUID | ID người cho thuê |
| startDate | Date | Ngày bắt đầu thuê |
| endDate | Date | Ngày kết thúc thuê |
| status | Enum | CONFIRMED, ACTIVE, COMPLETED, CANCELLED |
| approvedAt | DateTime | Thời điểm yêu cầu được chấp nhận |
| returnedAt | DateTime | Thời điểm xác nhận trả đồ |

**Chức năng:**

- Ghi nhận giao dịch thuê đã được xác nhận.
- Theo dõi quá trình giao nhận đồ dùng.
- Cập nhật trạng thái trong suốt thời gian thuê.
- Ghi nhận thời điểm hoàn trả đồ dùng.
- Lưu trữ thông tin người thuê, người cho thuê và món đồ liên quan.

## 3. Mối quan hệ giữa các tài nguyên

Các tài nguyên trong hệ thống có những mối quan hệ sau:

- Một User có thể sở hữu nhiều Item.
- Một User có thể gửi nhiều RentalRequest.
- Một Item có thể nhận nhiều RentalRequest.
- Một RentalRequest thuộc về một Item và một người thuê.
- Một RentalRequest có thể tạo ra tối đa một Rental.
- Một Rental liên kết với một Item, một người thuê và một người cho thuê.
- Người thuê và người cho thuê đều là các User trong hệ thống.

## 4. Các quy tắc nghiệp vụ (Business Rules)

### 4.1. Quy tắc đối với đồ cho thuê

- Chỉ người dùng đã đăng nhập mới được đăng tải đồ cho thuê.
- Chỉ chủ sở hữu mới có quyền chỉnh sửa hoặc ngừng đăng tải món đồ của mình.
- Món đồ có trạng thái INACTIVE không được nhận yêu cầu thuê mới.
- Chủ sở hữu không được gửi yêu cầu thuê đối với chính món đồ của mình.
- Việc ngừng đăng tải không xóa dữ liệu món đồ khỏi hệ thống nhằm bảo toàn lịch sử giao dịch.

### 4.2. Quy tắc đối với yêu cầu thuê

- Ngày bắt đầu thuê phải nhỏ hơn hoặc bằng ngày kết thúc thuê.
- Khoảng thời gian thuê phải hợp lệ và nằm trong tương lai tại thời điểm gửi yêu cầu.
- Chỉ những món đồ có trạng thái ACTIVE mới được nhận yêu cầu thuê.
- Chỉ chủ sở hữu của món đồ mới được chấp nhận hoặc từ chối yêu cầu thuê.
- Chỉ yêu cầu có trạng thái PENDING mới được phép xử lý.
- Không được chấp nhận hai giao dịch có khoảng thời gian thuê bị trùng nhau đối với cùng một món đồ.
- Người thuê không được tạo các yêu cầu trùng lặp có khoảng thời gian chồng lấn khi yêu cầu trước đó vẫn đang chờ xử lý hoặc đã được chấp nhận.

### 4.3. Quy tắc đối với giao dịch thuê

- Một yêu cầu thuê được chấp nhận sẽ tạo ra một giao dịch thuê tương ứng.
- Mỗi yêu cầu thuê chỉ được tạo tối đa một giao dịch.
- Giao dịch phải được xác nhận trước khi chuyển sang trạng thái đang thuê.
- Chỉ người cho thuê mới được xác nhận việc bàn giao và hoàn trả trong phạm vi MVP.
- Các thao tác bàn giao và hoàn trả chỉ được thực hiện khi giao dịch đang ở trạng thái hợp lệ.
- Giao dịch đã hoàn tất không được chuyển ngược về trạng thái đang thuê.

## 5. Vòng đời trạng thái (Resource Lifecycle)

### 5.1. Trạng thái Item

| Trạng thái | Ý nghĩa |
|---|---|
| ACTIVE | Món đồ đang được đăng tải và có thể nhận yêu cầu thuê |
| INACTIVE | Món đồ đã ngừng đăng tải và không nhận yêu cầu thuê mới |

Chuyển đổi trạng thái:

`ACTIVE → INACTIVE`

`INACTIVE → ACTIVE`

Chủ sở hữu có thể kích hoạt lại món đồ nếu món đồ vẫn đủ điều kiện cho thuê.

### 5.2. Trạng thái RentalRequest

| Trạng thái | Ý nghĩa |
|---|---|
| PENDING | Yêu cầu đang chờ chủ sở hữu xử lý |
| APPROVED | Yêu cầu đã được chấp nhận |
| REJECTED | Yêu cầu đã bị từ chối |
| CANCELLED | Yêu cầu đã bị hủy |

Các chuyển đổi trạng thái hợp lệ:

- `PENDING → APPROVED`
- `PENDING → REJECTED`
- `PENDING → CANCELLED`

Yêu cầu chỉ được chủ sở hữu xử lý khi đang ở trạng thái PENDING.

### 5.3. Trạng thái Rental

| Trạng thái | Ý nghĩa |
|---|---|
| CONFIRMED | Giao dịch đã được xác nhận sau khi yêu cầu thuê được chấp nhận |
| ACTIVE | Đồ dùng đã được bàn giao và đang trong thời gian thuê |
| COMPLETED | Đồ dùng đã được hoàn trả và giao dịch hoàn tất |
| CANCELLED | Giao dịch đã bị hủy theo quy tắc nghiệp vụ |

Các chuyển đổi trạng thái hợp lệ:

- `CONFIRMED → ACTIVE`
- `CONFIRMED → CANCELLED`
- `ACTIVE → COMPLETED`

Một Rental chỉ được tạo khi RentalRequest tương ứng được chấp nhận.

## 6. Các quyết định thiết kế (Design Decisions)

- **Tách RentalRequest và Rental:** RentalRequest đại diện cho quá trình gửi và xử lý yêu cầu thuê, trong khi Rental đại diện cho giao dịch đã được xác nhận. Việc tách riêng giúp quản lý vòng đời của hai hoạt động rõ ràng hơn.
- **Sử dụng UUID:** Giúp định danh tài nguyên duy nhất và tránh phụ thuộc vào ID tăng tuần tự.
- **Không xóa vật lý Item:** Sử dụng trạng thái INACTIVE để bảo toàn lịch sử yêu cầu thuê và giao dịch.
- **Sử dụng Modular Monolith:** Các chức năng được tổ chức thành những module riêng trong cùng một ứng dụng, phù hợp với quy mô MVP và thời gian phát triển.
- **Kiểm tra khả năng cho thuê:** Hệ thống kiểm tra các giao dịch đã được chấp nhận hoặc đang diễn ra để tránh trùng lặp thời gian thuê.
- **Chưa tích hợp thanh toán:** Các hoạt động thanh toán và hoàn tiền được loại khỏi phạm vi MVP để tập trung vào quy trình thuê cơ bản.

## 7. Các chức năng ngoài phạm vi MVP

Các chức năng sau chưa được triển khai trong phiên bản đầu tiên:

- Tích hợp thanh toán trực tuyến và hoàn tiền.
- Tích hợp vận chuyển và giao hàng.
- Nhắn tin thời gian thực giữa người thuê và người cho thuê.
- Xác minh danh tính người dùng.
- Bảo hiểm đồ dùng cho thuê.
- Quản lý khiếu nại và tranh chấp phức tạp.
- Hệ thống gợi ý đồ dùng dựa trên sở thích người dùng.


## 8. Kết luận

Mô hình tài nguyên của RentMate tập trung vào bốn thực thể cốt lõi: User, Item, RentalRequest và Rental. Các tài nguyên được phân tách theo trách nhiệm nghiệp vụ, có mối quan hệ và vòng đời trạng thái rõ ràng.

Mô hình này là cơ sở để xây dựng sơ đồ ERD, thiết kế kiến trúc hệ thống và đặc tả API bằng OpenAPI trong các bước tiếp theo.