---
layout: home
title: Home
lang: vi
permalink: /
---

<div class="textbook-epigraph" markdown="1">

"Mathematics is the art of giving the same name to different things."

<span class="epigraph-attribution">— Henri Poincaré</span>

</div>

Giáo trình *Toán Rời Rạc cho Khoa học Máy tính* trình bày các công cụ toán học cần thiết để mô hình hóa, phân tích và chứng minh các vấn đề trong khoa học máy tính. Khác với giải tích — nơi ta nghiên cứu các đại lượng thay đổi liên tục — toán rời rạc làm việc với các đối tượng **đếm được**, **hữu hạn** hoặc **rời rệt**: bit và byte, tập hợp, quan hệ, đồ thị, chuỗi ký tự, và các bước thuật toán có thể liệt kê từng bước một.

Máy tính, về bản chất, là một cỗ máy rời rạc. Mỗi thanh ghi chỉ lưu một trong hai trạng thái; mỗi lệnh `if` buộc chương trình phải chọn nhánh đúng hay sai; mỗi truy vấn SQL lọc một tập bản ghi thỏa điều kiện logic; mỗi thuật toán sắp xếp thực hiện một số hữu hạn phép so sánh và hoán đổi. Giáo trình này xây dựng ngôn ngữ hình thức để mô tả những hiện tượng đó một cách chính xác, và cung cấp các phương pháp suy luận để chứng minh rằng một chương trình, một giao thức hay một thiết kế dữ liệu thực sự đúng như mong đợi.

Cuốn sách được sắp xếp theo trình tự từ nền tảng đến chuyên sâu. Chúng ta bắt đầu bằng **logic** và **chứng minh** — hai công cụ không thể thiếu khi đọc hiểu thuật toán, viết đặc tả phần mềm, hay phân tích độ phức tạp. Tiếp theo là **tập hợp**, **quan hệ** và **hàm số**, ngôn ngữ chung của cơ sở dữ liệu, cấu trúc dữ liệu và lập trình hàm. Phần **đếm và tổ hợp** trang bị cho ta các kỹ thuật ước lượng số cấu hình, số khóa, số đường đi — những con số quyết định tính khả thi của thuật toán và độ an toàn của hệ thống. Các chương sau mở rộng sang **đại số Boole**, **lý thuyết số**, **mô hình tính toán** và **độ phức tạp**, tức những lĩnh vực nơi toán rời rạc gặp phần cứng, mật mã, trình biên dịch và giới hạn căn bản của tính toán.

## Đối tượng và yêu cầu đầu vào

Giáo trình dành cho sinh viên ngành khoa học máy tính và các chương trình liên quan, ở bậc đại học. Người đọc được giả định đã quen với đại số sơ cấp và có kinh nghiệm lập trình cơ bản — đủ để đọc hiểu các ví dụ minh họa bằng mã nguồn hay truy vấn. Không yêu cầu kiến thức giải tích; mọi khái niệm mới đều được định nghĩa và minh họa từ đầu.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau khi đọc và làm bài tập trong giáo trình, sinh viên có thể:

- **Vận dụng** logic mệnh đề và logic vị từ để biểu diễn điều kiện, ràng buộc và suy luận trong lập trình và cơ sở dữ liệu.
- **Chứng minh** các mệnh đề toán học bằng phương pháp trực tiếp, phản chứng và quy nạp; áp dụng tư duy tương tự khi lập luận về tính đúng của thuật toán.
- **Mô hình hóa** bài toán bằng tập hợp, quan hệ, hàm số và đồ thị; chọn cấu trúc dữ liệu phù hợp với mô hình đã xây dựng.
- **Đếm** và ước lượng số cấu hình, xác suất va chạm, độ phức tạp tổ hợp trong thiết kế hệ thống.
- **Phân tích** thuật toán bằng ký hiệu asymptotic; nhận biết các lớp độ phức tạp và ý nghĩa thực tiễn của chúng.

</div>

## Cấu trúc giáo trình

Giáo trình gồm hai mươi chương, nhóm thành sáu phần logic-tính toán. Mỗi chương chia thành các mục (bài học) được đánh số liên tục; mục lục chi tiết nằm ở cuối trang này.

**Phần I — Logic và chứng minh** (Chương 1–3) xây dựng nền tảng suy luận hình thức: mệnh đề, vị từ, lượng từ, quy tắc suy diễn, và các phương pháp chứng minh toán học.

**Phần II — Tập hợp, quan hệ, hàm số** (Chương 4–6) cung cấp ngôn ngữ mô tả dữ liệu và cấu trúc: phép toán tập hợp, quan hệ tương đương, thứ tự, tính chất hàm số, hàm hợp và hàm nghịch đảo.

**Phần III — Đếm và tổ hợp** (Chương 7–11) trình bày nguyên lý cộng, nguyên lý nhân, hoán vị, tổ hợp, nguyên lý bao hàm–loại trừ, nguyên lý Dirichlet, quan hệ truy hồi và hàm sinh.

**Phần IV — Ứng dụng và cấu trúc rời rạc** (Chương 9, 12–13) liên kết lý thuyết với thực hành kỹ thuật — biểu diễn nhị phân, mạch logic, đại số Boole — và giới thiệu lý thuyết đồ thị.

**Phần V — Thuật toán và lý thuyết số** (Chương 14–15) xét phân tích độ phức tạp, thiết kế thuật toán, chia hết, đồng dư và mật mã học cơ bản.

**Phần VI — Mô hình tính toán và độ phức tạp** (Chương 18–20) nghiên cứu máy hữu hạn trạng thái, ngôn ngữ hình thức, máy Turing, lớp P và NP.

Một số chương (12, 16, 17) đang được bổ sung nội dung; mục lục đánh dấu các chương này là *đang cập nhật*.

## Toán rời rạc và toán liên tục

<div class="textbook-definition" markdown="1">

**Định nghĩa.** *Toán rời rạc* (discrete mathematics) là nhánh toán học nghiên cứu các cấu trúc rời rệt — tức các đối tượng có thể đếm được hoặc phân tách thành các phần riêng biệt, không tạo thành một continuum.

</div>

Sự đối lập với toán liên tục có thể minh họa như sau:

| | Toán rời rạc | Toán liên tục |
|:---|:---|:---|
| Đối tượng điển hình | Số nguyên, tập hợp hữu hạn, đỉnh đồ thị | Số thực, hàm liên tục, đường cong |
| Công cụ | Logic, tập hợp, đồ thị, tổ hợp | Giới hạn, đạo hàm, tích phân |
| Bối cảnh CNTT | Thuật toán, mạng, mã hóa, cơ sở dữ liệu | Mô phỏng vật lý, xử lý tín hiệu |

Trong phạm vi khoa học máy tính, toán rời rạc chiếm vai trò trung tâm vì mọi biểu diễn dữ liệu trong máy đều hữu hạn, và mọi chương trình thực thi đều gồm một chuỗi hữu hạn các bước.

## Cách sử dụng giáo trình

<div class="note-box" markdown="1">

Mỗi mục trong giáo trình tuân theo cùng một khung: *mục tiêu học tập*, *định nghĩa*, *ví dụ*, *ứng dụng trong khoa học máy tính*, và *bài tập* có lời giải. Các định nghĩa và định lý được đánh dấu rõ ràng; ví dụ minh họa gắn với tình huống lập trình, cơ sở dữ liệu hoặc hệ thống thực tế. Sinh viên nên đọc tuần tự từ Chương 1, làm đầy đủ bài tập trước khi chuyển mục tiếp theo, và quay lại mục lục bên dưới để điều hướng khi ôn tập.

</div>

Phần còn lại của trang liệt kê đầy đủ hai mươi chương cùng tóm tắt nội dung từng chương. Chúng ta bắt đầu từ **Chương 1 — Logic Mệnh đề**.