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

Khi hệ thống tăng quy mô, câu hỏi không còn chỉ là "có những phần tử nào" mà còn là "có bao nhiêu phần tử". Một nền tảng có bao nhiêu người dùng hoạt động, một bộ test có bao nhiêu trường hợp khác nhau, hay hai tập điều kiện chồng lấn nhau ở mức nào, tất cả đều là bài toán đếm.


Tư duy tập hợp giúp ta mô tả dữ liệu, miền giá trị và ràng buộc một cách chính xác, nên phần này là nền cho cả lập trình lẫn mô hình hóa.
Khái niệm **lực lượng của tập hợp** cho ta cách đo kích thước của một tập, kể cả khi tập đó vô hạn. Từ đây, ta bắt đầu thấy vì sao toán rời rạc không chỉ nói về cấu trúc, mà còn nói về quy mô và giới hạn của cấu trúc đó.

Nhưng việc đếm hiếm khi thẳng băng. Khi các tập chồng lấn, cộng riêng từng phần rồi cộng lại thường dẫn đến đếm trùng. **Nguyên lý bao hàm, loại trừ** ra đời đúng để sửa lỗi tự nhiên đó, và nó xuất hiện rất nhiều trong combinatorics, xác suất và phân tích thuật toán.

Trong bài này, chúng ta sẽ đi từ việc đo kích thước tập hợp đến kỹ thuật đếm chính xác khi nhiều tập giao nhau, một kỹ năng rất quan trọng cho các bài toán rời rạc và CS.

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

## Định lý Schröder–Bernstein

**Định lý**: Nếu tồn tại hai hàm đơn ánh \( f: A \to B \) và \( g: B \to A \), thì tồn tại một song ánh giữa \( A \) và \( B \). Nói cách khác:
$$
|A| \leq |B| \quad \text{và} \quad |B| \leq |A| \quad \implies \quad |A| = |B|.
$$

**Chứng minh (phác thảo)**:

1. Vì \( f \) là đơn ánh, \( A \) "nhúng" được vào \( B \), nên \( |A| \leq |B| \).

2. Tương tự, \( g \) đơn ánh nên \( |B| \leq |A| \).

3. Ý tưởng chứng minh: Xây dựng một song ánh \( h: A \to B \) bằng cách "ghép" \( f \) và \( g^{-1} \) trên các tập con thích hợp (dùng chuỗi tiền ảnh dưới \( g \circ f \)).

   (Chi tiết chứng minh thường dùng định lý điểm cố định hoặc phân hoạch \( A \) thành các chuỗi và chọn \( f \) hoặc \( g^{-1} \) trên từng chuỗi.)

**Hệ quả**:
- \( |\N| = |2\N| = |\Z| = |\Q| = \aleph_0 \) (tập đếm được).
- \( |\R| = |(0,1)| = |[0,1]| = 2^{\aleph_0} \) (lực lượng continuum).

**Ý nghĩa CS**:
- So sánh độ phức tạp của không gian trạng thái mà không cần xây dựng song ánh tường minh.
- Dùng trong chứng minh một số bài toán NP-đầy đủ có cùng độ khó.

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

## Bài tập thực hành

### Bài tập 1: So sánh lực lượng

Chứng minh rằng tập hợp các số tự nhiên $$\N$$ và tập hợp các số chẵn dương có cùng lực lượng.

<details>
<summary>Đáp án</summary>

Ánh xạ $$f: \N \to 2\N$$, $$f(n) = 2n$$ là song ánh. Do đó $$|\N| = |2\N| = \aleph_0$$.

</details>

### Bài tập 2: Lực lượng tập con

Tính lực lượng của tập hợp tất cả tập con của $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

$$2^3 = 8$$ tập con (bao gồm cả tập rỗng và tập đầy đủ).

</details>

### Bài tập 3: Ứng dụng bao hàm - loại trừ

Có 50 sinh viên học Python, 40 học Java, 30 học cả hai. Hỏi có bao nhiêu sinh viên học ít nhất một ngôn ngữ?

<details>
<summary>Đáp án</summary>

$$|P \cup J| = 50 + 40 - 30 = 60$$.

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Lực lượng đo kích thước tập hợp. Với tập hữu hạn, lực lượng là số phần tử; với tập lũy thừa, số tập con là $$2^n$$. Nguyên lý bao hàm - loại trừ sửa lỗi đếm trùng khi các tập giao nhau. Với tập vô hạn, khái niệm đếm được và không đếm được mở đường cho các giới hạn căn bản của tính toán.
