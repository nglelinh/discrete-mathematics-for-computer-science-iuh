---
layout: post
title: "Cây: Từ Hệ thống Tệp đến Học máy"
categories: chapter16
date: 2021-01-01
order: 5
required: false
lang: en
---

# Cây: Từ Hệ thống Tệp đến Học máy

Nếu đồ thị là ngôn ngữ của kết nối tổng quát,
thì cây là ngôn ngữ của cấu trúc có thứ bậc.

Từ thư mục trong máy tính,
đến abstract syntax tree của compiler,
decision tree trong machine learning,
B-tree trong database,
và Huffman coding cho nén dữ liệu,
cây xuất hiện ở khắp nơi như một mô hình tổ chức thông tin cực tự nhiên.

Đó là lý do vì sao chương cuối về trees thường tạo cảm giác rất “gần đời sống phần mềm”.

---

## Phần 1: Lịch sử — Cayley và lý thuyết cây năm 1857

### 1.1. Arthur Cayley và việc trừu tượng hóa cấu trúc phân nhánh

Arthur Cayley nghiên cứu cây trong thế kỷ XIX,
ban đầu liên quan tới các công thức hóa học và cấu trúc phân nhánh.

Điều đáng chú ý là:
một mô hình toán học sinh ra để mô tả cấu trúc
lại trở thành công cụ cốt lõi của computing sau này.

### 1.2. Vì sao cây hấp dẫn

Cây cân bằng tốt giữa đơn giản và sức mạnh:

- có gốc,
- có cha/con,
- có mức sâu,
- có lá,
- không có chu trình.

Các tính chất này làm nó rất phù hợp để mô tả hierarchy,
decomposition,
và search.

![Arthur Cayley and tree theory]
*Hình 1: Cayley góp phần biến cấu trúc phân nhánh thành đối tượng toán học có thể nghiên cứu độc lập.*

---

## Phần 2: File systems như cây

### 2.1. Thư mục là ví dụ cây gần nhất với mọi sinh viên

Trong Unix,
Windows,
macOS,
ta có:

- thư mục gốc,
- thư mục con,
- file lá,
- đường dẫn từ gốc đến nút.

Đó là cấu trúc cây rất điển hình.

### 2.2. Vì sao cây hợp với file system

Nó cho phép:

- tổ chức theo hierarchy,
- tìm đường dẫn rõ ràng,
- phân quyền theo nhánh,
- nhóm nội dung liên quan,
- thao tác recursive tự nhiên.

### 2.3. Nhưng đời thực có thêm phức tạp

Shortcut,
symbolic links,
mount points,
versioned snapshots
có thể làm cấu trúc thực tế gần đồ thị hơn.

Điều đó lại là bài học hay:
cây là mô hình khởi đầu rất mạnh,
nhưng hệ thống thật đôi khi mở rộng vượt ra ngoài nó.

---

## Phần 3: Decision trees trong machine learning

### 3.1. Học máy đôi khi rất giống hỏi đáp phân nhánh

Decision tree phân loại bằng chuỗi câu hỏi:

- feature này lớn hơn ngưỡng không,
- thuộc nhóm nào,
- điều kiện nào đúng tiếp theo.

Mỗi nút là một phép tách,
mỗi lá là dự đoán.

### 3.2. Vì sao decision trees hấp dẫn

Chúng có vài ưu điểm rõ:

- dễ giải thích,
- trực quan,
- làm việc tốt với dữ liệu hỗn hợp trong nhiều tình huống,
- là nền cho random forest và gradient boosting trees.

### 3.3. Interpretable AI và vai trò của cây

Khi doanh nghiệp cần mô hình giải thích được,
tree-based approaches vẫn có vị trí rất mạnh.
Đây là ví dụ đẹp cho việc một cấu trúc rời rạc cổ điển
vẫn cạnh tranh được trong bối cảnh AI hiện đại.

![Decision tree model]
*Hình 2: Decision trees cho thấy cây không chỉ để tổ chức dữ liệu; nó còn là công cụ suy luận và dự đoán.*

---

## Phần 4: Binary search trees và B-trees trong database

### 4.1. Search tree giúp tra cứu nhanh

Binary search tree tổ chức dữ liệu sao cho mỗi bước so sánh loại bỏ một phần không gian tìm kiếm.

Đó là nguyên lý mạnh:
dùng cấu trúc để giảm chi phí truy vấn.

### 4.2. B-tree phù hợp lưu trữ ngoài bộ nhớ hơn

Trong database và file systems,
ta không chỉ quan tâm số phép so sánh.
Ta còn quan tâm số lần truy cập đĩa.

B-tree và các biến thể được thiết kế để giảm chiều cao cây,
tối ưu block access,
và hoạt động tốt với storage hierarchy.

### 4.3. Ảnh hưởng công nghiệp

Indexes trong DBMS,
metadata structures,
filesystem nodes
đều dựa vào tree structures hoặc biến thể của chúng.

---

## Phần 5: AST trong compiler và Huffman coding

### 5.1. Abstract syntax tree

Khi compiler đọc mã nguồn,
nó parse chương trình thành AST.

Ví dụ biểu thức:

```text
(a + b) * c
```

có thể được biểu diễn bằng cây,
trong đó nút gốc là `*`,
nhánh trái là `+`,
và các lá là biến.

AST giúp compiler:

- hiểu cấu trúc chương trình,
- phân tích ngữ nghĩa,
- tối ưu,
- sinh mã.

### 5.2. Huffman coding và cây tối ưu hóa độ dài mã

Huffman coding xây cây nhị phân từ tần suất ký hiệu,
để ký hiệu xuất hiện nhiều có mã ngắn hơn.

Đây là ví dụ kinh điển nơi cấu trúc cây trực tiếp dẫn đến hiệu quả nén.

### 5.3. Một cấu trúc, nhiều thế giới ứng dụng

Từ compiler đến compression,
cây chứng minh tính đa dụng hiếm có của mình.

---

## Phần 6: Tương lai — trees vẫn bền trong hệ thống mới

Ta sẽ còn thấy cây trong:

- hierarchical storage,
- ML ensembles,
- symbolic reasoning,
- parsers,
- scene graphs,
- UI component trees,
- structured document models.

Không phải vì cây là mô hình duy nhất,
mà vì thứ bậc và phân nhánh là pattern tự nhiên của rất nhiều bài toán.

---

## Kết luận

Từ Cayley,
đến file systems,
decision trees,
B-trees,
AST,
và Huffman coding,
cấu trúc cây cho thấy một ý tưởng toán học thanh lịch
có thể trở thành mô hình mặc định cho nhiều lớp công nghệ.

Nếu đồ thị giúp ta hiểu thế giới kết nối,
thì cây giúp ta hiểu thế giới có thứ bậc.
Và trong phần mềm,
cả hai thế giới đó xuất hiện gần như mỗi ngày.

---

## Bài tập thực hành

### Bài tập 1: Cây nhị phân

Một cây nhị phân đầy đủ có 7 nút. Hỏi có bao nhiêu lá?

<details>
<summary>Đáp án</summary>

Cây nhị phân đầy đủ có $$2^{h+1}-1$$ nút. Với 7 nút → chiều cao 2, số lá = 4.

</details>

### Bài tập 2: Cây quyết định

Giải thích tại sao cây quyết định (decision tree) trong ML thường được giới hạn độ sâu.

<details>
<summary>Đáp án</summary>

Để tránh overfitting. Cây quá sâu sẽ fit nhiễu trong dữ liệu huấn luyện.

</details>

### Bài tập 3: Hệ thống file

Mô tả cấu trúc thư mục dưới dạng cây. Giải thích tại sao dùng cây thay vì đồ thị.

<details>
<summary>Đáp án</summary>

Cây đảm bảo mỗi file chỉ có một đường dẫn duy nhất từ gốc. Đồ thị có thể tạo chu trình hoặc nhiều đường dẫn gây nhầm lẫn.

</details>

## Tóm tắt

Cây là cấu trúc dữ liệu linh hoạt nhất trong khoa học máy tính. Từ hệ thống file, AST, B-tree trong database, đến decision tree và random forest trong AI — cây giúp tổ chức dữ liệu phân cấp, hỗ trợ tìm kiếm nhanh và biểu diễn quy trình quyết định. Hiểu sâu về cây là nền tảng để làm việc với hầu hết các hệ thống phần mềm hiện đại.
