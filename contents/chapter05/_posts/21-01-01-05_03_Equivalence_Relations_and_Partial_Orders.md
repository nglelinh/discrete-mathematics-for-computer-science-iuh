---
layout: post
title: "Quan hệ Tương đương và Thứ tự Bộ phận"
categories: chapter05
date: 2021-01-01
order: 3
required: true
lang: en
---

Một số quan hệ giúp ta gom các đối tượng "giống nhau" theo một tiêu chí nào đó. Một số quan hệ khác giúp ta nói đối tượng nào đứng trước, bao hàm hơn, hoặc phụ thuộc vào đối tượng nào khác. Hai hướng này xuất hiện khắp nơi trong khoa học máy tính.


Khi đọc phần này, hãy nghĩ đến các liên kết giữa đối tượng trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, vì quan hệ chính là cách ta mô tả những liên kết đó.
Khi phân nhóm sinh viên theo lớp, gom chuỗi theo độ dài, hay coi hai trạng thái là tương đương theo một chuẩn nào đó, ta đang tiến gần đến **quan hệ tương đương**. Khi sắp xếp tác vụ theo phụ thuộc, so sánh tập quyền, hay mô hình hóa thứ bậc thư mục, ta gặp **thứ tự bộ phận**.

Điểm thú vị là cả hai đều được xây từ những tính chất cơ bản của quan hệ, nhưng dẫn đến hai kiểu cấu trúc rất khác nhau. Một bên tạo ra các lớp tương đương, bên kia tạo ra các poset và sơ đồ Hasse.

Trong bài này, chúng ta sẽ xem từ các tính chất quen thuộc có thể dựng nên hai khái niệm mạnh như thế nào, và vì sao chúng xuất hiện dày đặc trong mô hình dữ liệu lẫn thuật toán.

## 1. Quan hệ tương đương

**Định nghĩa**: Quan hệ $$R$$ trên tập $$A$$ là **quan hệ tương đương** nếu thỏa ba tính chất:

1. **Phản xạ**: $$\forall a\in A,\ aRa$$.
2. **Đối xứng**: $$\forall a,b\in A,\ aRb\to bRa$$.
3. **Bắc cầu**: $$\forall a,b,c\in A,\ (aRb\land bRc)\to aRc$$.

**Ký hiệu**: Ta thường viết $$a\sim b$$ thay cho $$(a,b)\in R$$ khi nói về quan hệ tương đương.

**Ví dụ**: Quan hệ đồng dư modulo $$n$$ trên $$\mathbb{Z}$$:

$$a\equiv b\pmod n \quad\text{khi và chỉ khi}\quad n\mid(a-b).$$

### Chứng minh đồng dư modulo là quan hệ tương đương

- Phản xạ: $$a-a=0$$ chia hết cho $$n$$.
- Đối xứng: nếu $$n\mid(a-b)$$ thì $$n\mid-(a-b)=b-a$$.
- Bắc cầu: nếu $$n\mid(a-b)$$ và $$n\mid(b-c)$$ thì $$n\mid((a-b)+(b-c))=a-c$$.

Vậy đồng dư modulo $$n$$ là quan hệ tương đương.

![Quan hệ tương đương và phân hoạch](https://commons.wikimedia.org/wiki/Special:FilePath/Set_partitions_4;_Hasse;_matrices.svg?width=640)

*Hình 5.13: Quan hệ tương đương chia tập thành các lớp rời nhau — mỗi ma trận tương ứng một phân hoạch.*

## 2. Lớp tương đương và phân hoạch

**Định nghĩa**: Với quan hệ tương đương $$\sim$$ trên $$A$$, **lớp tương đương** của $$a$$ là:

$$[a]=\{x\in A\mid x\sim a\}.$$

**Định lý**: Mỗi quan hệ tương đương trên $$A$$ tạo ra một phân hoạch của $$A$$ thành các lớp tương đương rời nhau; ngược lại, mỗi phân hoạch xác định một quan hệ tương đương.

**Ví dụ**: Trên $$\mathbb{Z}$$ với modulo 3, có ba lớp:

- $$[0]=\{\ldots,-6,-3,0,3,6,\ldots\}$$.
- $$[1]=\{\ldots,-5,-2,1,4,7,\ldots\}$$.
- $$[2]=\{\ldots,-4,-1,2,5,8,\ldots\}$$.

![Lưới phân hoạch theo modulo](https://commons.wikimedia.org/wiki/Special:FilePath/Hasse_diagram_of_powerset_of_3.svg?width=640)

*Hình 5.14: Phân hoạch tạo các lớp tương đương rời nhau — tương tự cách sắp xếp phần tử theo cấu trúc thứ tự.*

## 3. Quan hệ thứ tự bộ phận

**Định nghĩa**: Quan hệ $$R$$ trên $$A$$ là **thứ tự bộ phận** (partial order) nếu thỏa:

1. **Phản xạ**: $$aRa$$.
2. **Phản đối xứng**: nếu $$aRb$$ và $$bRa$$ thì $$a=b$$.
3. **Bắc cầu**: nếu $$aRb$$ và $$bRc$$ thì $$aRc$$.

Khi đó cặp $$(A,R)$$ được gọi là một **poset**.

**Ví dụ**:

- $$(\mathcal{P}(S),\subseteq)$$ là poset.
- $$(\mathbb{N},\mid)$$ với quan hệ chia hết là poset.
- Quan hệ "module A phải biên dịch trước module B" thường là thứ tự bộ phận nếu không có vòng phụ thuộc.

## 4. Vì sao gọi là "bộ phận"?

Trong một thứ tự toàn phần, mọi cặp phần tử đều so sánh được. Trong thứ tự bộ phận, có thể có hai phần tử không so sánh được.

**Ví dụ**: Với $$S=\{a,b\}$$, trong $$(\mathcal{P}(S),\subseteq)$$, hai tập $$\{a\}$$ và $$\{b\}$$ không tập nào là tập con của tập kia. Vì vậy chúng không so sánh được.

![Thứ tự bộ phận trên tập lũy thừa](https://commons.wikimedia.org/wiki/Special:FilePath/Hasse_diagram_of_powerset_of_3.svg?width=640)

*Hình 5.15: Poset $$(\mathcal{P}(S), \subseteq)$$ — không phải mọi cặp phần tử đều so sánh được (ví dụ {a} và {b}).*

## 5. Biểu đồ Hasse

**Định nghĩa**: Biểu đồ Hasse là cách vẽ poset bằng cách:

- Bỏ các vòng phản xạ.
- Bỏ các cạnh suy ra từ bắc cầu.
- Vẽ phần tử lớn hơn ở phía trên.

**Ví dụ**: Poset các ước dương của 12 theo quan hệ chia hết gồm $$\{1,2,3,4,6,12\}$$. Các cạnh phủ là: $$1-2$$, $$1-3$$, $$2-4$$, $$2-6$$, $$3-6$$, $$4-12$$, $$6-12$$.

![Biểu đồ Hasse đơn giản](https://commons.wikimedia.org/wiki/Special:FilePath/Simple_hasse_diagram.svg?width=640)

*Hình 5.16: Biểu đồ Hasse bỏ vòng phản xạ và các cạnh suy ra từ bắc cầu, chỉ giữ các cặp phủ trực tiếp.*

## Định lý: Quan hệ tương đương ⇔ Phân hoạch

**Định lý**: Cho tập \( A \).  
- Nếu \( R \) là quan hệ tương đương trên \( A \), thì các lớp tương đương của \( R \) tạo thành một **phân hoạch** của \( A \) (các tập con rời nhau, hợp lại bằng \( A \)).  
- Ngược lại, nếu \( \{A_i\} \) là một phân hoạch của \( A \), thì quan hệ “cùng nằm trong một \( A_i \)” là một quan hệ tương đương.

**Chứng minh** (chiều thuận):

1. **Phản xạ**: \( a R a \) vì \( a \) cùng lớp với chính nó.  
2. **Đối xứng**: Nếu \( a R b \) thì \( a, b \) cùng lớp ⇒ \( b R a \).  
3. **Bắc cầu**: Nếu \( a R b \) và \( b R c \) thì cả ba cùng lớp ⇒ \( a R c \).  
4. Các lớp rời nhau: nếu \( a \in [b] \cap [c] \) thì \( b R c \), nên \( [b] = [c] \).  
5. Hợp các lớp = \( A \): mọi \( a \) thuộc lớp \( [a] \).

Chiều ngược cũng dễ chứng minh tương tự.

**Hệ quả CS**:
- **Hash table**: mỗi bucket là một lớp tương đương (cùng hash).
- **Database sharding**: mỗi shard là một lớp.
- **Type equivalence** trong compiler.

![Định lý: quan hệ tương đương ⇔ phân hoạch](https://commons.wikimedia.org/wiki/Special:FilePath/Set_partitions_4;_Hasse;_matrices.svg?width=640)

*Hình 5.17: Mỗi quan hệ tương đương tương ứng duy nhất với một phân hoạch, và ngược lại.*

## 8. Ứng dụng trong Khoa học Máy tính

- **Union-Find**: quản lý các lớp tương đương trong bài toán thành phần liên thông.
- **Type checking**: các biểu thức cùng kiểu tạo thành nhóm tương đương theo kiểu.
- **Dependency graph**: thứ tự bộ phận mô hình hóa quan hệ phụ thuộc giữa task.
- **Version control**: lịch sử commit tạo DAG, thường được xem qua quan hệ tổ tiên.

![Đồ thị phụ thuộc — thứ tự bộ phận](https://commons.wikimedia.org/wiki/Special:FilePath/Directed_graph.svg?width=640)

*Hình 5.18: Dependency graph là poset — dùng topological sort để sắp xếp tác vụ theo thứ tự phụ thuộc.*

## Tổ chức dữ liệu và AI

Quan hệ tương đương tạo ra **phân hoạch** nên rất hợp với bài toán gom nhóm dữ liệu: hash bucket, data sharding theo khóa, hoặc chia người dùng thành các nhóm có cùng thuộc tính. Trong xử lý dữ liệu lớn, mỗi lớp tương đương có thể được xử lý như một partition độc lập.

Quan hệ thứ tự bộ phận xuất hiện khi không phải mọi đối tượng đều so sánh trực tiếp được. Priority queue và task scheduling dựa trên quan hệ “phải làm trước”, còn dependency graph trong `npm` hay `pip` dùng thứ tự này để giải bài toán cài đặt gói.

Khi mọi phần tử đều so sánh được, ta có **thứ tự toàn phần**. Đây là nền tảng của sorting algorithms, binary search trees và mọi cấu trúc cần sắp xếp tuyến tính.

Trong recommendation systems, quan hệ giữa người dùng và sản phẩm thường được lưu như ma trận user-item. Quan hệ này không phải tương đương hay thứ tự, nhưng ý tưởng tổ chức dữ liệu theo tập cặp vẫn là nền để suy ra người dùng giống nhau, sản phẩm liên quan và điểm gợi ý.

## Bài tập thực hành

### Bài tập 1: Kiểm tra quan hệ tương đương

Xét quan hệ $$R$$ trên $$\Z$$: $$aRb \iff a - b$$ chia hết cho 3. Chứng minh $$R$$ là quan hệ tương đương.

<details>
<summary>Đáp án</summary>

- Phản xạ: $$a-a=0$$ chia hết cho 3.
- Đối xứng: Nếu $$a-b$$ chia hết cho 3 thì $$b-a = -(a-b)$$ cũng chia hết.
- Bắc cầu: Nếu $$a-b$$ và $$b-c$$ chia hết cho 3 thì $$a-c$$ cũng chia hết.

</details>

### Bài tập 2: Phân hoạch

Tìm các lớp tương đương của quan hệ "cùng số dư khi chia 4" trên tập $$\{0,1,2,3,4,5,6,7\}$$.

<details>
<summary>Đáp án</summary>

Lớp: [0,4], [1,5], [2,6], [3,7].

</details>

### Bài tập 3: Thứ tự bộ phận

Vẽ Hasse diagram cho tập $$\{1,2,3,6,12\}$$ với quan hệ chia hết.

<details>
<summary>Đáp án</summary>

1 → 2 → 6 → 12  
1 → 3 → 6 → 12  
1 → 6 → 12 (các cạnh bao hàm rút gọn)

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Quan hệ tương đương dùng để phân loại và tạo phân hoạch. Quan hệ thứ tự bộ phận dùng để sắp xếp khi không phải mọi cặp đều so sánh được. Ba tính chất phản xạ, đối xứng/phản đối xứng và bắc cầu quyết định cấu trúc của từng loại quan hệ.
