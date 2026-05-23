---
layout: post
title: "Quan hệ Tương đương và Thứ tự Bộ phận"
categories: chapter05
date: 2021-01-01
order: 3
required: true
lang: en
---

# Quan hệ Tương đương và Thứ tự Bộ phận

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

## 2. Lớp tương đương và phân hoạch

**Định nghĩa**: Với quan hệ tương đương $$\sim$$ trên $$A$$, **lớp tương đương** của $$a$$ là:

$$[a]=\{x\in A\mid x\sim a\}.$$

**Định lý**: Mỗi quan hệ tương đương trên $$A$$ tạo ra một phân hoạch của $$A$$ thành các lớp tương đương rời nhau; ngược lại, mỗi phân hoạch xác định một quan hệ tương đương.

**Ví dụ**: Trên $$\mathbb{Z}$$ với modulo 3, có ba lớp:

- $$[0]=\{\ldots,-6,-3,0,3,6,\ldots\}$$.
- $$[1]=\{\ldots,-5,-2,1,4,7,\ldots\}$$.
- $$[2]=\{\ldots,-4,-1,2,5,8,\ldots\}$$.

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

## 5. Biểu đồ Hasse

**Định nghĩa**: Biểu đồ Hasse là cách vẽ poset bằng cách:

- Bỏ các vòng phản xạ.
- Bỏ các cạnh suy ra từ bắc cầu.
- Vẽ phần tử lớn hơn ở phía trên.

**Ví dụ**: Poset các ước dương của 12 theo quan hệ chia hết gồm $$\{1,2,3,4,6,12\}$$. Các cạnh phủ là: $$1-2$$, $$1-3$$, $$2-4$$, $$2-6$$, $$3-6$$, $$4-12$$, $$6-12$$.

## 6. Công cụ tương tác

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div class="interactive-tool" data-demo="relation-classifier" data-tool="relation-classifier">
  <p><strong>Demo đề xuất:</strong> nhập ma trận quan hệ, công cụ kiểm tra phản xạ, đối xứng, phản đối xứng, bắc cầu và kết luận quan hệ tương đương hay thứ tự bộ phận.</p>
</div>

<script src="{{ '/public/js/relation-properties-checker.js' | relative_url }}"></script>

## 7. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Đối xứng và phản đối xứng không phải là phủ định của nhau. Một quan hệ có thể vừa đối xứng vừa phản đối xứng trong trường hợp đặc biệt.

**Nhầm lẫn 2**: Nghĩ thứ tự bộ phận phải so sánh được mọi cặp. Điều đó là thứ tự toàn phần, mạnh hơn thứ tự bộ phận.

**Nhầm lẫn 3**: Lớp tương đương không phải một phần tử; nó là một tập các phần tử tương đương với nhau.
</div>

## 8. Ứng dụng trong Khoa học Máy tính

- **Union-Find**: quản lý các lớp tương đương trong bài toán thành phần liên thông.
- **Type checking**: các biểu thức cùng kiểu tạo thành nhóm tương đương theo kiểu.
- **Dependency graph**: thứ tự bộ phận mô hình hóa quan hệ phụ thuộc giữa task.
- **Version control**: lịch sử commit tạo DAG, thường được xem qua quan hệ tổ tiên.

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Quan hệ tương đương dùng để phân loại và tạo phân hoạch. Quan hệ thứ tự bộ phận dùng để sắp xếp khi không phải mọi cặp đều so sánh được. Ba tính chất phản xạ, đối xứng/phản đối xứng và bắc cầu quyết định cấu trúc của từng loại quan hệ.
