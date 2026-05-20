---
layout: post
title: "Lực lượng Tập hợp và Nguyên lý Bao hàm - Loại trừ"
categories: chapter04
date: 2021-01-01
order: 3
required: true
lang: en
---

# Lực lượng Tập hợp và Nguyên lý Bao hàm - Loại trừ

Đếm số phần tử của một danh sách hữu hạn là chuyện quen thuộc. Nhưng điều gì xảy ra khi ta hỏi có bao nhiêu số nguyên, bao nhiêu số hữu tỉ, hay có phải mọi vô hạn đều “to” như nhau? Đây là chỗ toán rời rạc bắt đầu chuyển từ trực giác đời thường sang những ý tưởng đủ lạ để thay đổi cả nền tảng toán học hiện đại.

Khái niệm **lực lượng tập hợp** giúp ta đo kích thước của tập, còn các tập vô hạn buộc ta suy nghĩ lại về từ “nhiều”. Chủ đề này không chỉ đẹp về mặt lý thuyết; nó còn liên hệ đến khả năng biểu diễn dữ liệu, đếm trạng thái của hệ thống và hiểu giới hạn của những gì máy tính có thể duyệt hết hay mô tả hết.

## 1. Lực lượng của tập hợp

**Định nghĩa**: **Lực lượng** (cardinality) của tập hữu hạn $$A$$, ký hiệu $$|A|$$, là số phần tử phân biệt trong $$A$$.

**Ký hiệu**:

- $$|A|$$: số phần tử của $$A$$.
- $$\emptyset$$: tập rỗng, có lực lượng 0.
- $$A\subseteq B$$: $$A$$ là tập con của $$B$$.

**Ví dụ**:

- Nếu $$A=\{1,3,5,7,9\}$$ thì $$|A|=5$$.
- Nếu $$B=\{x\in\mathbb{N}\mid 1\le x\le 100\}$$ thì $$|B|=100$$.
- $$|\emptyset|=0$$.

**Tính chất cơ bản**:

- Nếu $$A\subseteq B$$ và $$A,B$$ hữu hạn thì $$|A|\le |B|$$.
- Nếu $$A\cap B=\emptyset$$ thì $$|A\cup B|=|A|+|B|$$.
- Tổng quát, nếu hai tập chồng lấn, không được cộng đơn giản.

## 2. Tập lũy thừa

**Định nghĩa**: **Tập lũy thừa** của $$A$$, ký hiệu $$\mathcal{P}(A)$$, là tập tất cả các tập con của $$A$$.

$$\mathcal{P}(A)=\{X\mid X\subseteq A\}.$$

**Định lý**: Nếu $$|A|=n$$ thì $$|\mathcal{P}(A)|=2^n$$.

### Chứng minh

Mỗi phần tử của $$A$$ có hai lựa chọn khi tạo một tập con: hoặc được chọn, hoặc không được chọn. Với $$n$$ phần tử độc lập, số cách chọn là:

$$2\cdot 2\cdots 2 = 2^n.$$

Vì mỗi cách chọn tương ứng đúng một tập con, nên $$|\mathcal{P}(A)|=2^n$$.

**Ví dụ**: Nếu $$A=\{a,b,c\}$$ thì:

$$\mathcal{P}(A)=\{\emptyset,\{a\},\{b\},\{c\},\{a,b\},\{a,c\},\{b,c\},\{a,b,c\}\}.$$

Có $$2^3=8$$ tập con.

## 3. Nguyên lý bao hàm - loại trừ cho hai tập

**Định lý**:

$$|A\cup B|=|A|+|B|-|A\cap B|.$$

### Diễn giải

Khi cộng $$|A|+|B|$$, các phần tử thuộc $$A\cap B$$ bị đếm hai lần. Vì vậy ta phải trừ đi một lần.

**Ví dụ**: Trong lớp có 40 sinh viên, 25 sinh viên học Python, 18 sinh viên học Java, 10 sinh viên học cả hai. Số sinh viên học ít nhất một trong hai ngôn ngữ là:

$$25+18-10=33.$$

## 4. Nguyên lý bao hàm - loại trừ cho ba tập

**Định lý**:

$$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.$$

### Khối suy luận

- Cộng $$|A|+|B|+|C|$$: vùng giao đôi bị đếm thừa.
- Trừ các giao đôi: vùng giao ba bị trừ quá nhiều.
- Cộng lại $$|A\cap B\cap C|$$ để cân bằng.

**Ví dụ**: Có 100 sinh viên. 50 học Python, 40 học Java, 30 học C++; 20 học Python và Java, 15 học Python và C++, 10 học Java và C++; 5 học cả ba. Số sinh viên học ít nhất một ngôn ngữ là:

$$50+40+30-20-15-10+5=80.$$

## 5. Tập vô hạn đếm được

**Định nghĩa**: Một tập $$A$$ là **đếm được** nếu các phần tử của nó có thể liệt kê thành một dãy $$a_1,a_2,a_3,\ldots$$, tức tồn tại song ánh giữa $$A$$ và một tập con của $$\mathbb{N}$$.

**Ví dụ**:

- $$\mathbb{N}$$ là đếm được.
- $$\mathbb{Z}$$ là đếm được: $$0,1,-1,2,-2,3,-3,\ldots$$.
- $$\mathbb{Q}$$ là đếm được, dù dày đặc trên trục số.

## 6. Tập không đếm được

**Định nghĩa**: Một tập là **không đếm được** nếu không thể liệt kê tất cả phần tử của nó bằng một dãy vô hạn đánh số bởi $$\mathbb{N}$$.

**Ý tưởng đường chéo Cantor**: Tập số thực trong đoạn $$(0,1)$$ không đếm được. Nếu giả sử liệt kê được mọi số thực trong $$(0,1)$$, ta có thể tạo một số mới khác số thứ nhất ở chữ số thập phân thứ nhất, khác số thứ hai ở chữ số thứ hai, và cứ thế. Số mới này không nằm trong danh sách, mâu thuẫn.

## 7. Công cụ tương tác

<div class="interactive-tool" data-tool="venn-counter">
  <p><strong>Demo đề xuất:</strong> nhập kích thước ba tập và các giao, công cụ vẽ Venn diagram và tính $$|A\cup B\cup C|$$ theo bao hàm - loại trừ.</p>
</div>

## 8. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Cộng $$|A|+|B|$$ ngay cả khi hai tập giao nhau. Phải trừ $$|A\cap B|$$.

**Nhầm lẫn 2**: Nghĩ mọi vô hạn đều bằng nhau. Trong lý thuyết tập hợp, có vô hạn đếm được và vô hạn không đếm được.

**Nhầm lẫn 3**: Với tập lũy thừa, nhầm $$|\mathcal{P}(A)|=2|A|$$ thay vì $$2^{|A|}$$.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

```python
python = {'An', 'Binh', 'Chi'}
java = {'Binh', 'Dung'}
learns_any = python | java
learns_both = python & java
print(len(learns_any))
```

- **Tìm kiếm và lọc dữ liệu**: `COUNT`, `DISTINCT`, `UNION`, `INTERSECT` đều là thao tác lực lượng.
- **Phân tích thuật toán**: số tập con của một tập $$n$$ phần tử là $$2^n$$, dẫn đến thuật toán vét cạn theo cấp số mũ.
- **Kiểm thử phần mềm**: bao hàm - loại trừ giúp ước lượng số ca test phủ nhiều điều kiện.
- **Lý thuyết tính toán**: tính không đếm được giải thích vì sao có nhiều bài toán hơn số chương trình có thể viết.

## Tóm tắt

Lực lượng đo kích thước tập hợp. Với tập hữu hạn, lực lượng là số phần tử; với tập lũy thừa, số tập con là $$2^n$$. Nguyên lý bao hàm - loại trừ sửa lỗi đếm trùng khi các tập giao nhau. Với tập vô hạn, khái niệm đếm được và không đếm được mở đường cho các giới hạn căn bản của tính toán.
