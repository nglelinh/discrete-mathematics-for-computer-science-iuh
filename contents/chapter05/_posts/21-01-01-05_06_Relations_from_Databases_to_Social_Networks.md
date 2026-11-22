---

layout: post
title: "Quan hệ: Từ Cơ sở Dữ liệu đến Mạng Xã hội"
categories: chapter05
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Trình bày các ứng dụng thực tế của lý thuyết quan hệ: mô hình cơ sở dữ liệu quan hệ của Codd, sơ đồ ER, khóa ngoại, mạng xã hội, phân hoạch tương đương trong kiểm thử và hệ thống gợi ý."
---

Ở các mục trước, chúng ta đã xây dựng nền tảng lý thuyết về quan hệ. Mục bổ sung này giới thiệu các ứng dụng của quan hệ trong cơ sở dữ liệu, mạng xã hội, kiểm thử phần mềm và hệ thống gợi ý.

Trong toán học rời rạc, quan hệ là một tập con của tích Descartes; trong khoa học máy tính, khái niệm đó là nền tảng của mô hình cơ sở dữ liệu quan hệ, đồ thị dữ liệu, hệ thống gợi ý và kỹ thuật phân vùng kiểm thử. Từ việc sinh viên đăng ký môn học, người dùng theo dõi nhau đến khách hàng mua sản phẩm, mọi tình huống đều có thể mô hình hóa bằng các cặp có cấu trúc.

## Phần 1: Lịch sử — Từ lý thuyết tập hợp đến mô hình quan hệ

### Quan hệ xuất phát từ nhu cầu mô tả liên kết

Khi lý thuyết tập hợp phát triển, các nhà toán học nhận thấy việc liệt kê đối tượng riêng lẻ là chưa đủ — cần một công cụ để mô tả cách các đối tượng liên kết với nhau. Khái niệm quan hệ đáp ứng nhu cầu đó: nó cho phép biểu diễn sinh viên nào học môn nào, đỉnh nào kề đỉnh nào, số nào chia hết cho số nào, hay trạng thái nào chuyển sang trạng thái nào.

### E. F. Codd và mô hình quan hệ năm 1970

Năm 1970, Edgar F. Codd công bố bài báo về mô hình quan hệ cho các ngân hàng dữ liệu lớn dùng chung — một cột mốc định hình ngành cơ sở dữ liệu. Thay vì gắn dữ liệu chặt với con trỏ và cách lưu trữ vật lý trên đĩa, Codd đề xuất biểu diễn dữ liệu như các quan hệ toán học có thể thao tác bằng đại số quan hệ. Cách tiếp cận này tách biệt rõ lớp logic ("dữ liệu biểu diễn điều gì") khỏi lớp lưu trữ vật lý ("dữ liệu được lưu như thế nào").

![Mô hình quan hệ của E. F. Codd](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="5.31">E. F. Codd (1970) đặt nền móng cho mô hình quan hệ — dữ liệu được tổ chức thành các bảng và thao tác bằng đại số quan hệ.</p>
---

## Phần 2: Thiết kế cơ sở dữ liệu — Khi quan hệ trở thành hạ tầng

### Sơ đồ ER mô tả thực thể và quan hệ

Khi thiết kế cơ sở dữ liệu, kỹ sư thường bắt đầu bằng sơ đồ thực thể–quan hệ (ER diagram) với các thực thể như `Student`, `Course`, `Instructor` và `Enrollment`. Trọng tâm của sơ đồ không chỉ là danh sách thực thể mà là các mối quan hệ giữa chúng: sinh viên đăng ký môn học, giảng viên phụ trách môn học, môn học có môn tiên quyết và khoa quản lý giảng viên.

![Sơ đồ ER — thực thể và quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/ERD_Representation.svg)

<p class="textbook-figure-caption" data-figure="5.32">Sơ đồ ER mô tả các thực thể (Student, Course, Instructor) và quan hệ giữa chúng trước khi chuyển sang bảng SQL.</p>
### Khóa ngoại (Foreign key) — Ràng buộc quan hệ được hệ thống thực thi

```sql
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);
```

Ở đây, ràng buộc khóa ngoại bảo đảm cặp `(student_id, course_id)` chỉ được phép tồn tại khi cả sinh viên và môn học tương ứng đều thực sự có mặt trong bảng `Students` và `Courses`. Nhờ đó, hệ quản trị cơ sở dữ liệu chuyển một khái niệm quan hệ trừu tượng thành ràng buộc bảo vệ tính toàn vẹn dữ liệu.

### Đại số quan hệ và thực thi truy vấn

Các phép toán như chọn (selection), chiếu (projection), kết nối (join), đổi tên (rename) và hợp (union) đều là phép toán trên quan hệ. Trình lập kế hoạch và tối ưu hóa truy vấn (query planner/optimizer) dựa vào các luật biến đổi của đại số quan hệ để chọn kế hoạch thực thi hiệu quả hơn. Vì vậy, một hệ quản trị cơ sở dữ liệu không chỉ lưu tệp tin mà còn vận hành trực tiếp trên đại số quan hệ.

![Phép JOIN trong đại số quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="5.33">Phép JOIN kết hợp hai quan hệ qua khóa chung — nền tảng của truy vấn SQL và trình tối ưu hóa truy vấn.</p>
---

## Phần 3: Quan hệ trong mạng xã hội và đồ thị

### Mạng xã hội dưới góc nhìn quan hệ

Trên các nền tảng như Facebook, LinkedIn hay X, mỗi người dùng là một đỉnh và mỗi tương tác giữa họ là một cặp thuộc một quan hệ, chẳng hạn `follows(A, B)`, `friends(A, B)`, `works_with(A, B)` hoặc `likes(A, Post42)`. Khi số lượng bản ghi tăng lên hàng tỷ, các quan hệ này trở thành đối tượng của phân tích đồ thị ở quy mô công nghiệp.

### Phân loại liên kết theo tính chất quan hệ

Các tính chất đã học trong toán rời rạc phản ánh trực tiếp đặc trưng của từng loại liên kết: quan hệ "theo dõi" trên X không đối xứng, quan hệ "bạn bè" trên Facebook có tính đối xứng, còn quan hệ "là tổ tiên của" có tính bắc cầu. Việc phân biệt đúng các tính chất này giúp chọn mô hình lưu trữ và thuật toán truy vấn phù hợp.

### Hệ thống gợi ý khai thác nhiều lớp quan hệ

Khi nền tảng gợi ý video, âm nhạc, sách hoặc việc làm, hệ thống khai thác đồng thời nhiều quan hệ giữa người dùng với nội dung, người dùng với người dùng, nội dung với nội dung, cũng như hành vi theo thời gian và ngữ cảnh. Do đó, bài toán gợi ý thường được biểu diễn bằng ma trận quan hệ hoặc đồ thị hai phía (bipartite graph).

![Mạng xã hội như đồ thị quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Social_Network_Analysis_Visualization.png)

<p class="textbook-figure-caption" data-figure="5.34">Mạng xã hội có thể xem là đồ thị quan hệ quy mô hàng tỷ cung như follows, friends và likes.</p>
---

## Phần 4: Lớp tương đương trong kiểm thử phần mềm và bảng băm

### Phân vùng tương đương trong kiểm thử (Equivalence partitioning)

Khi phần mềm nhận hàng triệu khả năng đầu vào, ta không thể kiểm thử vét cạn từng trường hợp. Thay vào đó, kỹ sư áp dụng kỹ thuật **phân vùng tương đương** (equivalence partitioning): chia tập đầu vào thành các lớp mà mọi giá trị trong cùng một lớp được kỳ vọng tạo ra hành vi xử lý giống nhau. Ví dụ, với trường nhập tuổi, ta có thể chia thành ba lớp: nhỏ hơn 0 (không hợp lệ), từ 0 đến 120 (hợp lệ) và lớn hơn 120 (không hợp lệ).

### Quan hệ tương đương và tư duy phân lớp

Một quan hệ tương đương thỏa mãn ba tính chất phản xạ, đối xứng và bắc cầu, từ đó phân hoạch tập đầu vào thành các lớp tương đương đôi một rời nhau. Nguyên tắc "chia không gian đầu vào thành các lớp xử lý tương tự nhau rồi chọn đại diện kiểm tra" là ứng dụng trực tiếp của định lý phân hoạch.

### Bảng băm cũng là một dạng phân lớp

Hàm băm ánh xạ không gian khóa rộng lớn vào một số lượng ngăn chứa (bucket) hữu hạn, tạo ra một phân hoạch trên tập khóa. Hai khóa có cùng giá trị băm nằm trong cùng một ngăn chứa ở tầng cài đặt; cách xử lý va chạm và mức độ phân bố đều giữa các ngăn quyết định hiệu năng thực tế của bảng băm.

![Equivalence partitioning — lớp tương đương trong testing](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.35">Phân vùng tương đương chia không gian đầu vào thành các lớp rời nhau, mỗi lớp đại diện cho một nhóm hành vi kỳ vọng giống nhau.</p>
---

## Phần 5: Hệ thống gợi ý và ma trận quan hệ

### Quan hệ người dùng – nội dung (User–item relation)

Xét bảng tương tác đơn giản sau:

| user | item | action |
|------|------|--------|
| U1   | M1   | watched |
| U1   | M2   | liked   |
| U2   | M1   | skipped |

Đây là một quan hệ giữa tập người dùng và tập nội dung. Từ dữ liệu quan hệ này, hệ thống học cách ước lượng mức độ tương đồng giữa người dùng, giữa các nội dung và dự đoán gợi ý phù hợp.

![Ma trận user-item — quan hệ gợi ý](/discrete-mathematics-for-computer-science-iuh/img/course/Hasse_diagram_of_powerset_of_3.svg)

<p class="textbook-figure-caption" data-figure="5.36">Hệ thống gợi ý lưu quan hệ user–item dưới dạng ma trận thưa; lọc cộng tác khai thác các mẫu liên kết giữa người dùng và sản phẩm.</p>
### Lọc cộng tác (Collaborative filtering)

Nếu hai người dùng có hành vi tương đồng trên nhiều sản phẩm, hệ thống có thể dự đoán họ sẽ quan tâm đến những sản phẩm giống nhau trong tương lai. Dù kỹ thuật triển khai sử dụng phân rã ma trận hay vector nhúng (embeddings), câu hỏi nền tảng vẫn xoay quanh cấu trúc quan hệ giữa các đối tượng.

### Từ dữ liệu quan hệ đến học biểu diễn

Học máy hiện đại thường ánh xạ các quan hệ vào không gian vector, nhưng dữ liệu đầu vào ban đầu vẫn là các quan hệ rời rạc như nhấp chuột, mua hàng, theo dõi hay cùng xem. Toán rời rạc vì vậy không tách rời khỏi học máy mà tiếp tục là nền tảng mô tả dữ liệu đầu vào.

---

## Phần 6: Mở rộng — Cơ sở dữ liệu đồ thị và tri thức liên kết

Khi dữ liệu ngày càng có nhiều liên kết phức tạp, vai trò của mô hình quan hệ càng thể hiện rõ trong cơ sở dữ liệu đồ thị (graph databases), phát hiện gian lận, theo dõi chuỗi cung ứng, tìm kiếm ngữ nghĩa, đồ thị tri thức doanh nghiệp và hệ thống gợi ý quy mô lớn.

---

## Kết luận

Từ mô hình quan hệ của Codd đến đồ thị mạng xã hội, phân vùng tương đương trong kiểm thử, bảng băm và hệ thống gợi ý, khái niệm quan hệ là cầu nối từ định nghĩa toán học cơ bản đến hạ tầng của nhiều hệ thống phần mềm hiện đại.

---

## Bài tập thực hành

### Bài tập 1: Mô hình hóa quan hệ xã hội

Viết công thức vị từ cho phát biểu: "Mọi người bạn của bạn tôi đều là bạn của tôi" (dùng vị từ $$\text{Friend}(x, y)$$ chỉ "$$x$$ là bạn của $$y$$" và hằng $$\text{me}$$ chỉ "tôi").

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$\forall x \forall y \bigl((\text{Friend}(\text{me}, x) \land \text{Friend}(x, y)) \to \text{Friend}(\text{me}, y)\bigr)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2: Sơ đồ ER

Mô tả mối quan hệ lực lượng giữa ba thực thể `User`, `Post` và `Comment`.

<details>
<summary>Đáp án</summary>

- `User` → `Post` (1:N — một người dùng có thể tạo nhiều bài viết)
- `Post` → `Comment` (1:N — một bài viết có thể có nhiều bình luận)
- `User` → `Comment` (1:N — một người dùng có thể viết nhiều bình luận)

</details>

### Bài tập 3: Kiểm thử phân vùng tương đương

Một hệ thống phân loại người dùng thành 3 nhóm độ tuổi hợp lệ. Hãy đề xuất các lớp tương đương đôi một rời nhau để kiểm thử.

<details>
<summary>Đáp án</summary>

Có thể chia thành 3 lớp tương đương hợp lệ đôi một rời nhau: `[0–17]`, `[18–59]` và `[60+]` (ngoài ra khi kiểm thử biên có thể xét thêm lớp không hợp lệ `< 0`). Chọn ít nhất một giá trị đại diện từ mỗi lớp để kiểm thử.

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Mô hình quan hệ** (Codd, 1970) tổ chức dữ liệu thành bảng và thao tác bằng đại số quan hệ.
- **Sơ đồ ER và khóa ngoại** mô hình hóa thực thể cùng các ràng buộc toàn vẹn liên kết trong cơ sở dữ liệu.
- **Mạng xã hội** biểu diễn các liên kết có hướng, đối xứng hoặc bắc cầu tùy đặc trưng từng quan hệ.
- **Phân vùng tương đương** chia miền đầu vào thành các lớp rời nhau trong kiểm thử phần mềm.
- **Hệ thống gợi ý** khai thác ma trận quan hệ user–item làm cơ sở cho lọc cộng tác.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=76v3gRns28U">Basics of Relational Algebra</a> — Neso Academy, tiếng Anh. Giới thiệu mô hình quan hệ trong cơ sở dữ liệu.
- <a href="https://www.youtube.com/watch?v=z9IceBT2_ws">Relational Algebra Explained: The Foundation of Databases! 🗄️</a> — CodeLucky, tiếng Anh. Các phép toán trên bảng, tương ứng phần ứng dụng cơ sở dữ liệu của bài học.
- <a href="https://www.youtube.com/watch?v=C7YrMRdLkqo">Intro to Graph Theory | Definitions &amp; Ex: 7 Bridges of Konigsberg</a> — Dr. Trefor Bazett, tiếng Anh. Đồ thị như biểu diễn quan hệ cặp, liên hệ trực tiếp với mô hình mạng xã hội.
