---

layout: post
title: "Giới thiệu Hàm số"
categories: chapter06
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Trong chương này, chúng ta tìm hiểu hàm số — ánh xạ gán mỗi phần tử trong miền xác định với đúng một phần tử trong miền đích, cùng các cách biểu diễn và ứng dụng trong khoa học máy tính."
---


Hãy tưởng tượng một máy bán nước tự động: nếu bạn bấm nút `B3`, lúc thì máy nhả chai nước suối, lúc lại nhả lon cà phê, hoặc tệ hơn là im bặt không trả ra gì cả—chiếc máy đó bị lỗi nghiêm trọng. Lời cam kết khắt khe rằng **mỗi đầu vào hợp lệ phải tương ứng với đúng một đầu ra xác định** chính là linh hồn của **Hàm số (Function)**—viên gạch nền chung cho cả toán học hiện đại, hàm lập trình, cơ sở dữ liệu và mạng nơ-ron AI.

<div class="textbook-epigraph" markdown="1">

"A function is a rule that assigns to each input exactly one output."

<span class="epigraph-attribution">— Dirichlet (paraphrased)</span>

</div>

Trong chương này, chúng ta nghiên cứu **hàm số** — ánh xạ gán cho mỗi phần tử thuộc miền xác định đúng một phần tử thuộc miền đích. Từ một mã định danh người dùng (user ID) trả về hồ sơ tương ứng, từ một chuỗi đầu vào tính ra giá trị băm, đến việc dùng chỉ số mảng để truy xuất đúng một phần tử, tất cả đều dựa trên cùng một ý tưởng toán học. Mục 6.1 bắt đầu từ định nghĩa hàm số, miền xác định, miền đích và các cách biểu diễn cơ bản.

Trong toán rời rạc, hàm là một quan hệ đặc biệt thỏa mãn tính tồn tại và tính duy nhất; còn trong khoa học máy tính, hàm là mô hình đứng sau lời gọi hàm, ánh xạ khóa–giá trị, biến đổi dữ liệu và mã hóa. Điểm cốt lõi của hàm số là tính xác định: cùng một đầu vào phải luôn cho ra đúng một đầu ra.

## Kiến thức cần nhớ: Bốn trụ cột định nghĩa nên khái niệm Hàm số

1. **Hàm số là một Quan hệ đặc biệt (Tính duy nhất & Tính toàn phần)**:
   Một hàm $$f: A \to B$$ là một tập con của $$A \times B$$ thỏa mãn hai ràng buộc chặt: mỗi $$a \in A$$ phải có ảnh (*không bỏ sót đầu vào*) và ảnh đó phải là **duy nhất** (*một đầu vào không thể phân nhánh ra hai đầu ra*).

2. **Phân biệt rạch ròi ba tập: Domain, Codomain và Range**:
   - **Domain ($$A$$)**: tập toàn bộ đầu vào hợp lệ.
   - **Codomain ($$B$$)**: tập các giá trị đầu ra *được khai báo* (kiểu trả về trong lập trình).
   - **Range ($$f(A) \subseteq B$$)**: tập các giá trị đầu ra *thực sự đạt được*. Nhiều nhầm lẫn trong bài tập xuất phát từ việc đánh đồng Codomain với Range!

3. **Hàm toàn phần (Total) vs. Hàm bộ phận (Partial)**:
   Hàm toàn phần xác định trên mọi $$x \in A$$; hàm bộ phận có thể không xác định tại một số đầu vào (ví dụ $$f(x) = 1/x$$ tại $$x = 0$$, hay hàm tra cứu khóa trong `dict` không tìm thấy key).

4. **Số lượng hàm giữa hai tập hữu hạn ($$\lvert B\rvert^{\lvert A\rvert}$$)**:
   Mỗi phần tử trong số $$\lvert A\rvert$$ phần tử của $$A$$ có độc lập $$\lvert B\rvert$$ cách chọn đầu ra, nên có đúng $$\lvert B\rvert^{\lvert A\rvert}$$ hàm từ $$A$$ vào $$B$$—công thức giải thích vì sao có tới $$2^{2^n}$$ hàm Boolean $$n$$ biến.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm số $$f: A \to B$$ và phân biệt miền xác định (domain), miền đích (codomain) và tập giá trị (range).
- **Biểu diễn** hàm số bằng bảng, công thức, tập cặp có thứ tự và sơ đồ mũi tên.
- **Liên hệ** hàm toán học với hàm trong lập trình và học máy.

**Từ khóa**: hàm số (function), domain, codomain, range (ảnh), ánh xạ.
</div>

## Định nghĩa hàm số
<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho hai tập hợp $$A$$ và $$B$$. Một **hàm số** $$f$$ từ $$A$$ đến $$B$$, ký hiệu $$f:A\to B$$, là một quy tắc gán cho mỗi phần tử $$x\in A$$ đúng một phần tử $$y\in B$$.
</div>

**Ký hiệu**:

- $$A$$: miền xác định (domain).
- $$B$$: miền đích hay đối miền (codomain).
- $$f(x)$$: giá trị của hàm tại $$x$$.
- $$f(A)=\{f(x)\mid x\in A\}$$: ảnh hay tập giá trị thực sự đạt được (range/image).

<div class="textbook-example" markdown="1">
**Ví dụ**: Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ có cả domain lẫn codomain là $$\mathbb{R}$$, nhưng ảnh (range) của nó chỉ là $$[0,\infty)$$.

![Hàm số như máy ánh xạ đầu vào → đầu ra](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.1">Hàm số ánh xạ mỗi phần tử miền xác định đến đúng một phần tử miền đích — mô hình "hộp hàm".</p>
</div>

## Hàm số như một quan hệ đặc biệt

Một quan hệ $$R\subseteq A\times B$$ là một hàm từ $$A$$ đến $$B$$ nếu thỏa mãn đồng thời hai điều kiện:

1. **Tính tồn tại**: với mọi $$a\in A$$, tồn tại $$b\in B$$ sao cho $$(a,b)\in R$$.
2. **Tính duy nhất**: nếu $$(a,b_1)\in R$$ và $$(a,b_2)\in R$$ thì $$b_1=b_2$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$R=\{(1,a),(2,b),(3,b)\}$$ là một hàm từ $$\{1,2,3\}$$ đến $$\{a,b\}$$. Ngược lại, $$S=\{(1,a),(1,b),(2,b)\}$$ không phải là hàm vì đầu vào $$1$$ có tới hai đầu ra khác nhau.

![Hàm song ánh — mỗi đầu vào một đầu ra](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.2">Hàm là quan hệ đặc biệt — mỗi phần tử domain có đúng một mũi tên đi ra (tồn tại và duy nhất).</p>
</div>

## Domain, codomain và range

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Domain (miền xác định)**: tập tất cả các đầu vào hợp lệ.
- **Codomain (miền đích)**: tập mà đầu ra được khai báo là thuộc về.
- **Range/Image (tập giá trị/ảnh)**: tập các đầu ra thực sự xuất hiện.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Với hàm $$f:\mathbb{Z}\to\mathbb{Z}$$, $$f(n)=2n$$:

- Domain: $$\mathbb{Z}$$.
- Codomain: $$\mathbb{Z}$$.
- Range: tập các số nguyên chẵn.
</div>

<div class="content-box warning-box textbook-block" markdown="1">
**Nhầm lẫn phổ biến**: Codomain và range không nhất thiết trùng nhau. Codomain là tập được khai báo chứa giá trị trả về, còn range là tập các giá trị mà hàm thực sự đạt tới.
</div>

## Các cách biểu diễn hàm

### Bằng công thức

<div class="textbook-equation" markdown="1">
$$f(x)=3x+1.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bằng bảng

| $$x$$ | 1 | 2 | 3 |
|---|---:|---:|---:|
| $$f(x)$$ | 4 | 7 | 10 |

### Bằng tập cặp có thứ tự

<div class="textbook-equation" markdown="1">
$$f=\{(1,4),(2,7),(3,10)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bằng sơ đồ mũi tên

Mỗi phần tử thuộc miền xác định có đúng một mũi tên đi ra.

![Sơ đồ mũi tên — biểu diễn hàm số](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="6.3">Sơ đồ mũi tên thể hiện ánh xạ từ tập A sang tập B — mỗi phần tử của A có đúng một cung đi ra.</p>
## Hàm toàn phần và hàm bộ phận

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong toán rời rạc, hàm thường được hiểu là **hàm toàn phần** (total function), tức mọi phần tử của domain đều có ảnh. Trong lập trình, ta còn gặp **hàm bộ phận** (partial function), tức chỉ xác định trên một tập con của domain.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: $$g(x)=1/x$$ là hàm toàn phần từ $$\mathbb{R}\setminus\{0\}$$ đến $$\mathbb{R}$$, nhưng không phải là hàm toàn phần từ $$\mathbb{R}$$ đến $$\mathbb{R}$$ vì không xác định tại $$x=0$$.

![Hàm đơn ánh — không gộp hai đầu vào](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

<p class="textbook-figure-caption" data-figure="6.4">Hàm bộ phận chỉ xác định trên một phần domain — khác với hàm toàn phần vốn gán đầu ra cho mọi phần tử trong domain.</p>
</div>

## Hàm trong lập trình

```python
def square(x):
    return x * x
```

Nếu xét kiểu `int -> int`, đoạn mã trên mô phỏng trực tiếp một hàm toán học. Tuy nhiên, trong lập trình thực tế, hàm còn có thể phát sinh ngoại lệ, phụ thuộc vào trạng thái toàn cục, thực hiện thao tác nhập/xuất (I/O) hoặc không dừng; những yếu tố này khiến hàm lập trình phức tạp hơn hàm toán học thuần túy.

## Định lý: Số hàm từ tập hữu hạn sang tập hữu hạn

<div class="textbook-theorem" markdown="1">
**Định lý**: Số hàm từ tập $$A$$ ($$\lvert A \rvert = n$$) sang tập $$B$$ ($$\lvert B \rvert = m$$) là $$m^n$$.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh**:

Mỗi hàm $$f: A \to B$$ được xác định hoàn toàn bởi giá trị $$f(a)$$ gán cho từng phần tử $$a \in A$$. Với mỗi $$a$$, có đúng $$m$$ lựa chọn trong $$B$$. Do đó, tổng số hàm có thể tạo thành là $$m \times m \times \cdots \times m$$ ($$n$$ thừa số) $$= m^n$$.
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**:

- Số hàm từ $$\{0,1\}^n$$ sang $$\{0,1\}$$ là $$2^{2^n}$$ (đúng bằng số hàm Boolean trên $$n$$ biến đã gặp ở bài 01_01).
- Số hàm từ một tập $$n$$ phần tử sang chính nó là $$n^n$$ (trong khi số hoán vị chỉ là $$n!$$).
</div>

**Ý nghĩa trong Khoa học Máy tính**:

- **Không gian hàm** trong học máy có kích thước rất lớn, do đó cần có cơ chế điều chuẩn (regularization) hoặc thiên kiến quy nạp (inductive bias) để thu hẹp không gian tìm kiếm.
- **Liệt kê (enumeration)** tất cả các hàm khả dĩ chỉ khả thi khi $$n$$ rất nhỏ.

## Hàm số trong AI và Machine Learning

Trong trí tuệ nhân tạo, một mô hình thường được xem như một hàm ánh xạ đầu vào sang đầu ra: ảnh $$\to$$ nhãn lớp, văn bản $$\to$$ cảm xúc, hoặc dữ liệu lịch sử $$\to$$ giá trị dự đoán. Nhờ góc nhìn này, cả bài toán phân loại (classification) lẫn hồi quy (regression) đều có thể hiểu là bài toán tìm một hàm xấp xỉ từ dữ liệu.

Mạng nơ-ron (neural network) là hợp của nhiều hàm đơn giản: phép nhân ma trận, cộng bias và áp dụng hàm kích hoạt (activation function) như ReLU hay sigmoid. Vì đầu ra của tầng trước là đầu vào của tầng sau, toàn bộ mạng chính là một hàm hợp (composition of functions).

![Mạng neural — hợp của nhiều hàm](/discrete-mathematics-for-computer-science-iuh/img/course/Neural_network.svg)

<p class="textbook-figure-caption" data-figure="6.5">Mạng nơ-ron là hàm hợp (composition of functions) — mỗi tầng là một hàm ánh xạ vector đầu vào sang vector đầu ra.</p>
Trong các hệ thống gợi ý (recommendation systems), ta thường xây dựng hàm $$f(user, item)\to rating$$ để dự đoán mức độ phù hợp giữa người dùng và sản phẩm.

```python
def classify(score):
    return "pass" if score >= 0.5 else "fail"

class MockModel:
    def predict(self, X):
        return [classify(x[0]) for x in X]
```

Đoạn mã trên mô phỏng giao diện `predict()` quen thuộc trong `sklearn`: nhận một tập đầu vào và trả về đầu ra xác định tương ứng cho từng mẫu.

### Phân biệt quan hệ với hàm số, tách bạch Domain–Codomain–Range và đếm số hàm trên tập nhỏ

Xét hai tập hữu hạn $$A = \{1, 2, 3\}$$ và $$B = \{a, b\}$$.

**Phần A — Kiểm tra 3 quan hệ $$R \subseteq A \times B$$ xem cái nào là hàm toàn phần $$A \to B$$**:
- $$R_1 = \{(1, a), (2, b), (3, a)\}$$: **Là hàm số!** Mọi phần tử của $$A$$ đều xuất hiện đúng 1 lần ở tọa độ đầu (hai đầu vào `1` và `3` có thể trỏ chung về `a` mà không hề vi phạm định nghĩa hàm).
- $$R_2 = \{(1, a), (1, b), (2, a), (3, b)\}$$: **Không phải hàm số**, vì đầu vào `1` bắn ra tới hai đầu ra khác nhau là `a` và `b`.
- $$R_3 = \{(1, a), (2, a)\}$$: **Không phải hàm toàn phần trên $$A$$**, vì phần tử `3` bị bỏ rơi không có ảnh (đây là một *hàm bộ phận*).

**Phần B — Phân biệt Codomain và Range trên hàm quen thuộc**:
Với $$f: \mathbb{Z} \to \mathbb{Z}$$ định nghĩa bởi $$f(x) = x^2$$:
- $$\text{Domain} = \mathbb{Z}$$ (mọi số nguyên).
- $$\text{Codomain} = \mathbb{Z}$$ (tập đích khai báo).
- $$\text{Range} = \{0, 1, 4, 9, 16, \dots\}$$ (chỉ gồm các số chính phương không âm — nhỏ hơn rất nhiều so với Codomain $$\mathbb{Z}$$!).

**Phần C — Đếm số hàm giữa $$A = \{1, 2, 3\}$$ ($$\lvert A \rvert=3$$) và $$B = \{a, b\}$$ ($$\lvert B \rvert=2$$)**:
- Số hàm từ $$A \to B$$: mỗi phần tử $$1, 2, 3$$ có 2 lựa chọn $$\implies 2 \times 2 \times 2 = 2^3 = \mathbf{8}$$ hàm.
- Số hàm từ $$B \to A$$: mỗi phần tử $$a, b$$ có 3 lựa chọn $$\implies 3 \times 3 = 3^2 = \mathbf{9}$$ hàm.
Chú ý thứ tự cơ số và số mũ: luôn là $$\lvert \text{Đích} \rvert^{\lvert \text{Nguồn} \rvert}$$!

## Ứng dụng trong Khoa học Máy tính

- **API**: ánh xạ mỗi yêu cầu (request) hợp lệ đến một phản hồi (response).
- **Hàm băm (Hash function)**: ánh xạ dữ liệu đầu vào sang một giá trị băm cố định.
- **Khóa cơ sở dữ liệu (Database key)**: ánh xạ khóa chính đến đúng bản ghi tương ứng.
- **Lập trình hàm (Functional programming)**: ưu tiên dùng hàm thuần túy để dễ kiểm thử và lập luận.
- **Học máy (Machine learning)**: mô hình học máy là hàm xấp xỉ ánh xạ từ đặc trưng đầu vào đến kết quả dự đoán.

![Hàm băm — ánh xạ khóa vào ngăn bảng, có va chạm](/discrete-mathematics-for-computer-science-iuh/img/course/hash_function_mapping.svg)

<p class="textbook-figure-caption" data-figure="6.6">Hàm băm h(k) = k mod 5 gán mỗi khóa vào đúng một ngăn trong bảng. Hai khóa MSSV 2101 và MSSV 2106 cùng rơi vào ngăn 1 (va chạm) — vẫn là hàm, nhưng không đơn ánh.</p>

### Minh hoạ tương tác

Minh hoạ hàm số: điều chỉnh các mũi tên giữa hai tập hợp để quan sát xem ánh xạ tạo thành có phải là hàm đơn ánh, toàn ánh hay song ánh không.

<div class="interactive-demo" markdown="1">
<div data-demo="function-explainer" data-preset="inj"></div>
</div>
<script src="{{ '/public/js/explainers/function-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Kiểm tra hàm

Xét quan hệ $$R = \{(1,2),(2,4),(3,6)\}$$ trên $$\N$$. Hỏi $$R$$ có phải là hàm không? Giải thích.

<details>
<summary>Đáp án</summary>

Nếu xét miền xác định là $\{1, 2, 3\}$ thì $R$ là hàm toàn phần, vì mỗi phần tử được ánh xạ đến đúng một giá trị. Tuy nhiên, nếu xét trên toàn tập $\N$ thì $R$ không phải hàm toàn phần (chỉ là hàm bộ phận), vì các phần tử khác ngoài $\{1, 2, 3\}$ không có ảnh.

</details>

### Bài tập 2: Xác định domain, codomain, range

Cho hàm $$f: \N \to \N$$, $$f(x) = x^2 + 1$$. Hãy xác định domain, codomain và range.

<details>
<summary>Đáp án</summary>

- Domain: $\N$
- Codomain: $\N$
- Range: $\{2,5,10,17,...\}$ (các số có dạng $n^2+1$, với quy ước $\N = \{1, 2, 3, \dots\}$; nếu tính cả $0 \in \N$ thì tập giá trị bắt đầu từ $1$).

</details>

### Bài tập 3: Hàm trong Python

Viết hàm Python tương ứng với $$f(x) = 2x + 1$$ và kiểm tra kết quả với đầu vào là 3.

<details>
<summary>Đáp án</summary>

```python
def f(x):
    return 2 * x + 1

print(f(3))  # 7
```

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Hàm số** $$f: A \to B$$: mỗi $$a \in A$$ được gán đúng một giá trị $$f(a) \in B$$.
- Phân biệt rõ **domain** (miền xác định), **codomain** (miền đích) và **range** (ảnh thực sự đạt được).
- Các cách biểu diễn phổ biến: công thức, bảng giá trị, tập cặp có thứ tự và sơ đồ mũi tên.
- Số hàm từ tập $$n$$ phần tử sang tập $$m$$ phần tử là $$m^n$$.
- **Ứng dụng trong Khoa học Máy tính**: API, hàm băm, khóa cơ sở dữ liệu, mô hình học máy.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các tính chất đơn ánh, toàn ánh và song ánh.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=OixshZzH8t0">FUNCTIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu hàm như một quan hệ đặc biệt, trong đó mỗi đầu vào có đúng một đầu ra.
- <a href="https://www.youtube.com/watch?v=G8qvOZ9DE3c">The intuitive idea of a function</a> — Dr. Trefor Bazett, tiếng Anh. Trực giác về hàm số trước khi tiếp cận định nghĩa bằng tích Descartes.
- <a href="https://www.youtube.com/watch?v=-a5FaFp87N4">Formal Definition of a Function using the Cartesian Product</a> — Dr. Trefor Bazett, tiếng Anh. Định nghĩa hình thức của hàm số, khớp với phần định nghĩa trong bài.
