---
layout: post
title: "Quan hệ: Từ Cơ sở Dữ liệu đến Mạng Xã hội"
categories: chapter05
date: 2021-01-01
order: 6
required: false
lang: en
---

# Quan hệ: Từ Cơ sở Dữ liệu đến Mạng Xã hội

Chúng ta sống trong thế giới của các quan hệ.
Sinh viên đăng ký môn học.
Người dùng theo dõi nhau trên mạng xã hội.
Khách hàng mua sản phẩm.
Tài khoản được gắn quyền truy cập.
Video được đề xuất cho người xem.

Trong toán học rời rạc,
quan hệ có vẻ là một định nghĩa khô:
tập con của tích Descartes.
Nhưng trong khoa học máy tính,
đó là một ý tưởng cực sống:
nó là nền cho relational databases,
graph data,
recommendation systems,
và cả cách ta chia thế giới input thành các lớp tương đương để test phần mềm.

---

## Phần 1: Lịch sử — từ set theory đến mô hình quan hệ

### 1.1. Quan hệ sinh ra từ nhu cầu mô tả kết nối

Khi set theory trưởng thành,
các nhà toán học nhận ra rằng chỉ liệt kê đối tượng là chưa đủ.
Ta còn cần mô tả cách chúng liên kết với nhau.

Quan hệ là công cụ hoàn hảo cho việc đó.
Nó cho phép nói:

- sinh viên nào học môn nào,
- đỉnh nào kề đỉnh nào,
- số nào chia hết cho số nào,
- trạng thái nào chuyển sang trạng thái nào.

### 1.2. E. F. Codd và cuộc cách mạng năm 1970

Năm 1970,
Edgar F. Codd công bố bài báo nổi tiếng về mô hình quan hệ cho dữ liệu lớn được chia sẻ.
Đó là một trong những khoảnh khắc định hình toàn bộ ngành database.

Điểm mạnh của Codd là ông không chỉ đưa ra kỹ thuật lưu trữ.
Ông đưa ra một mô hình toán học.

Thay vì xem dữ liệu là các con trỏ và record phụ thuộc chặt vào cách lưu vật lý,
Codd xem dữ liệu như các quan hệ có thể thao tác bằng đại số.

Đó là một quyết định trí tuệ cực mạnh,
vì nó tách phần “dữ liệu là gì” khỏi phần “dữ liệu được lưu ra sao”.

![E. F. Codd và mô hình quan hệ]
*Hình 1: Bài báo năm 1970 của Codd biến khái niệm quan hệ thành nền móng thực dụng cho thế giới dữ liệu hiện đại.*

---

## Phần 2: Database design — nơi quan hệ thành hạ tầng

### 2.1. ER diagram là câu chuyện về thực thể và quan hệ

Khi thiết kế database,
kỹ sư thường bắt đầu bằng ER diagram:

- `Student`,
- `Course`,
- `Instructor`,
- `Enrollment`.

Điều quan trọng không chỉ là danh sách thực thể.
Điều quan trọng là quan hệ giữa chúng:

- sinh viên đăng ký môn học,
- giảng viên dạy môn học,
- môn học có tiên quyết,
- khoa quản lý giảng viên.

### 2.2. Foreign key là quan hệ được máy cưỡng chế

```sql
CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);
```

Ở đây,
foreign key đảm bảo rằng cặp `(student_id, course_id)`
chỉ tồn tại nếu các đối tượng liên quan tồn tại thật.

Đó là cách database biến một quan hệ trừu tượng thành ràng buộc sống còn cho chất lượng dữ liệu.

### 2.3. Relational algebra và query execution

Các thao tác như:

- selection,
- projection,
- join,
- rename,
- union,

đều là công cụ thao tác trên quan hệ.
Nhiều query planner và optimizer thực hiện các phép biến đổi dựa trên luật đại số để tìm kế hoạch chạy tốt hơn.

Điều này nhắc ta rằng:
DBMS không chỉ là phần mềm lưu file.
Nó là cỗ máy suy nghĩ bằng quan hệ.

---

## Phần 3: Quan hệ trong mạng xã hội và graphs

### 3.1. Facebook, LinkedIn, X nhìn dưới lăng kính quan hệ

Trên mạng xã hội,
mỗi người dùng có thể xem như một nút,
và mối liên hệ giữa hai người là một quan hệ.

Ví dụ:

- `follows(A, B)`
- `friends(A, B)`
- `works_with(A, B)`
- `likes(A, Post42)`

Khi các quan hệ này phình lên hàng tỷ bản ghi,
ta bước từ set theory sang graph analytics ở quy mô công nghiệp.

### 3.2. Quan hệ có thể có hướng, không đối xứng, không bắc cầu

Quan hệ “theo dõi” trên X không đối xứng.
Quan hệ “bạn bè” trên Facebook gần hơn với đối xứng.
Quan hệ “là tổ tiên của” có tính bắc cầu.

Những tính chất đã học trong toán rời rạc
trở nên cực thực khi bạn mô hình hóa hệ thống thật.

### 3.3. Recommendation systems dựa trên các lớp quan hệ dày đặc

Khi nền tảng gợi ý video,
nhạc,
sách,
hay công việc,
nó đang khai thác quan hệ giữa:

- user và item,
- user và user,
- item và item,
- hành vi và thời gian,
- nội dung và ngữ cảnh.

Đó là lý do vì sao các bài toán recommendation hay được mô tả như ma trận quan hệ hoặc bipartite graph.

![Mạng xã hội như đồ thị quan hệ]
*Hình 2: Quan hệ không chỉ sống trong bảng dữ liệu; nó còn là hình dạng của các mạng xã hội hiện đại.*

---

## Phần 4: Equivalence classes trong testing và hashing

### 4.1. Testing không thể thử mọi input

Nếu phần mềm nhận hàng triệu khả năng input,
ta không thể test từng trường hợp.
Vì vậy,
kỹ sư dùng **equivalence partitioning**:
chia input thành các lớp được xem là “tương đương về hành vi dự kiến”.

Ví dụ,
với ô nhập tuổi:

- nhỏ hơn 0,
- từ 0 đến 120,
- lớn hơn 120.

Ba lớp này là ba vùng quan hệ-hành-vi khác nhau.

### 4.2. Equivalence relation và suy nghĩ nhóm hóa

Một equivalence relation có ba tính chất:

- phản xạ,
- đối xứng,
- bắc cầu.

Khi có equivalence relation,
tập phần tử được chia thành các equivalence classes.

Trong computing,
ý tưởng “chia thế giới thành các lớp mà bên trong mỗi lớp xử lý giống nhau”
là cực kỳ thực dụng.

### 4.3. Hashing cũng là một kiểu phân lớp

Hash function ánh xạ nhiều khóa vào số lượng bucket hữu hạn.
Như vậy,
nó đang tạo một phân hoạch gần đúng của không gian keys.

Hai khóa có cùng hash value
thuộc cùng một “lớp bucket” ở mức triển khai.
Collision xử lý ra sao,
bucket phân bố đều đến đâu,
có ảnh hưởng trực tiếp tới hiệu năng.

---

## Phần 5: AI recommendation systems và ma trận quan hệ

### 5.1. User-item relation là trái tim của gợi ý

Hãy tưởng tượng bảng dữ liệu:

| user | item | action |
|------|------|--------|
| U1   | M1   | watched |
| U1   | M2   | liked   |
| U2   | M1   | skipped |

Đây là một quan hệ giữa người dùng và nội dung.
Từ quan hệ này,
hệ thống cố học xem ai giống ai,
nội dung nào giống nội dung nào,
và gợi ý nào có khả năng thành công.

### 5.2. Collaborative filtering nhìn rất “quan hệ”

Nếu hai người có hành vi tương tự trên nhiều item,
ta có thể dự đoán họ sẽ thích các item giống nhau trong tương lai.

Đây là cách nhìn đặc trưng của collaborative filtering.
Đằng sau các ma trận,
vector embeddings,
và factorization,
ta vẫn thấy một câu hỏi cũ:
“đối tượng nào liên hệ với đối tượng nào theo mẫu nào?”

### 5.3. Từ relation đến representation learning

Học máy hiện đại thường biến quan hệ thành vector spaces.
Nhưng điểm khởi đầu vẫn là relation data:

- click relations,
- purchase relations,
- follow relations,
- co-view relations.

Điều đó cho thấy:
toán rời rạc không biến mất khi AI vào cuộc.
Nó chỉ đổi hình thức biểu diễn.

---

## Phần 6: Tương lai — graph databases, knowledge systems, linked data

Khi dữ liệu ngày càng liên thông,
vai trò của quan hệ càng lớn.

Ta thấy điều này trong:

- graph databases,
- fraud detection,
- supply chain tracking,
- semantic search,
- enterprise knowledge graphs,
- recommendation at scale.

Tương lai sẽ không ít quan hệ đi.
Nó chỉ làm chúng dày hơn,
nhiều lớp hơn,
và cần công cụ tốt hơn để suy nghĩ về chúng.

---

## Kết luận

Quan hệ là cây cầu nối từ định nghĩa toán học đơn giản
đến những hệ thống dữ liệu và mạng hiện đại.

Từ Codd và relational databases,
đến social graphs,
equivalence partitioning,
hash buckets,
và recommendation systems,
khái niệm quan hệ âm thầm xuất hiện ở khắp nơi.

Hiểu quan hệ,
vì thế,
không chỉ giúp bạn giải bài tập chương 5.
Nó giúp bạn nhìn thấy xương sống của nhiều hệ thống số đang vận hành quanh mình.

---

## Bài tập thực hành

### Bài tập 1: Mô hình hóa quan hệ xã hội

Viết công thức vị từ cho: "Mọi người bạn của bạn đều là bạn của tôi".

<details>
<summary>Đáp án</summary>

$$\forall x \forall y (Friend(x,y) \to Friend(y,me))$$

</details>

### Bài tập 2: ER Diagram

Mô tả quan hệ giữa `User`, `Post`, `Comment` dưới dạng quan hệ (relation).

<details>
<summary>Đáp án</summary>

- `User` → `Post` (1:N)
- `Post` → `Comment` (1:N)
- `User` → `Comment` (1:N)

</details>

### Bài tập 3: Partition testing

Một hệ thống phân loại người dùng thành 3 nhóm theo độ tuổi. Mô tả các lớp tương đương dùng để test.

<details>
<summary>Đáp án</summary>

Lớp tương đương: [0-17], [18-35], [36-60], [60+]. Chọn một giá trị đại diện từ mỗi lớp để test.

</details>

## Tóm tắt

Quan hệ là cầu nối giữa toán học và thực tế. Từ mô hình quan hệ của Codd, ER diagram, mạng xã hội, đến partition testing và recommendation systems — tất cả đều dựa trên ý tưởng tổ chức dữ liệu thành các cặp có cấu trúc. Hiểu sâu về quan hệ giúp bạn thiết kế hệ thống rõ ràng, dễ bảo trì và dễ kiểm chứng hơn.
