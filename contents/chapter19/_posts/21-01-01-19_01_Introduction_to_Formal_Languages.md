---
layout: post
title: "Giới thiệu Ngôn ngữ Hình thức"
categories: chapter19
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Ngôn ngữ Hình thức

Mỗi khi bạn gõ một câu lệnh vào terminal, một dòng mã Python, hay một biểu thức tìm kiếm `grep`, máy tính phải quyết định xem chuỗi ký tự đó có **hợp lệ** hay không trước khi thực thi. Trình biên dịch Python từ chối `def 1foo():` nhưng chấp nhận `def foo1():`. Lệnh `grep "^[A-Z].*\.$"` tìm các dòng bắt đầu bằng chữ hoa và kết thúc bằng dấu chấm. Cả hai đều dựa trên cùng một câu hỏi nền tảng: **chuỗi ký tự này có thuộc về ngôn ngữ mà ta định nghĩa hay không?**

**Ngôn ngữ hình thức** (formal language) là khung lý thuyết trả lời câu hỏi đó. Khác với ngôn ngữ tự nhiên - đầy mơ hồ và ngữ cảnh - ngôn ngữ hình thức được định nghĩa bằng các quy tắc toán học chính xác, có thể kiểm tra bằng thuật toán. Chương này xây dựng nền tảng đó: bảng chữ cái, chuỗi, ngôn ngữ, và các phép toán trên chúng. Đây là ngôn ngữ chung của Chương 18 (máy tính toán) và Chương 20 (lý thuyết độ phức tạp).

## Mục tiêu học tập

- Định nghĩa chính xác bảng chữ cái, chuỗi, và ngôn ngữ.
- Thực hiện các phép toán cơ bản trên chuỗi và ngôn ngữ.
- Phân biệt ngôn ngữ hữu hạn và vô hạn, đếm được và không đếm được.
- Hiểu mối quan hệ giữa ngôn ngữ và máy chấp nhận chúng.
- Nhận diện vai trò của ngôn ngữ hình thức trong khoa học máy tính.

**Từ khóa**: alphabet, string, language, concatenation, Kleene star, regular language, context-free language.

## 1. Bảng chữ cái và Chuỗi

### Định nghĩa: Bảng chữ cái

Một **bảng chữ cái** (alphabet), ký hiệu $$\Sigma$$, là một **tập hữu hạn, khác rỗng** các ký hiệu.

**Ví dụ**:

- $$\Sigma_1 = \{0, 1\}$$ - bảng chữ cái nhị phân, dùng trong lý thuyết tính toán.
- $$\Sigma_2 = \{a, b, c, \ldots, z\}$$ - bảng chữ cái Latin thường.
- $$\Sigma_3$$ = tập tất cả ký tự ASCII (128 ký hiệu).
- $$\Sigma_4 = \{\texttt{if}, \texttt{else}, \texttt{while}, \texttt{=}, \texttt{;}, \ldots\}$$ - các token trong ngôn ngữ lập trình.

Mỗi phần tử của $$\Sigma$$ gọi là một **ký hiệu** (symbol) hoặc **chữ cái** (letter).

### Định nghĩa: Chuỗi

Một **chuỗi** (string, word) trên $$\Sigma$$ là một dãy hữu hạn các ký hiệu lấy từ $$\Sigma$$.

- **Chuỗi rỗng** (empty string), ký hiệu $$\epsilon$$ (đôi khi $$\lambda$$), là chuỗi không có ký hiệu nào.
- **Độ dài** của chuỗi $$w$$, ký hiệu $$\lvert w \rvert$$, là số ký hiệu trong chuỗi. $$\lvert \epsilon \rvert = 0$$.

**Ví dụ** với $$\Sigma = \{0, 1\}$$: $$\epsilon, 0, 1, 00, 01, 10, 11, 000, \ldots$$ Chuỗi $$w = 10110$$ có $$\lvert w \rvert = 5$$.

<div class="content-box info-box" markdown="1">
**Ký hiệu thường gặp**

- $$\Sigma$$ - bảng chữ cái (alphabet).
- $$w, x, y, z$$ - chuỗi (string).
- $$a, b, c$$ - ký hiệu (symbol).
- $$\epsilon$$ - chuỗi rỗng.
- $$\lvert w \rvert$$ - độ dài chuỗi $$w$$.
- $$\lvert w \rvert_a$$ - số lần ký hiệu $$a$$ xuất hiện trong $$w$$.
</div>

### Phép nối chuỗi (concatenation)

Cho hai chuỗi $$x = a_1 a_2 \ldots a_m$$ và $$y = b_1 b_2 \ldots b_n$$, **phép nối** của chúng là:

$$xy = a_1 a_2 \ldots a_m b_1 b_2 \ldots b_n$$

**Tính chất**:

- Kết hợp: $$(xy)z = x(yz)$$.
- Phần tử trung hòa: $$\epsilon x = x \epsilon = x$$.
- Độ dài: $$\lvert xy \rvert = \lvert x \rvert + \lvert y \rvert$$.
- **Không giao hoán**: nói chung $$xy \neq yx$$.

### Lũy thừa và chuỗi đảo ngược

- **Lũy thừa**: $$x^0 = \epsilon$$, $$x^{n+1} = x^n x$$. Ví dụ $$(01)^3 = 010101$$.
- **Đảo ngược**: $$w^R$$ là chuỗi viết ngược. Ví dụ $$(abc)^R = cba$$, $$\epsilon^R = \epsilon$$.

### Tiền tố, hậu tố, chuỗi con

Cho chuỗi $$w = xyz$$ với $$x, y, z$$ là chuỗi (có thể rỗng):

- $$x$$ là **tiền tố** (prefix) của $$w$$.
- $$z$$ là **hậu tố** (suffix) của $$w$$.
- $$y$$ là **chuỗi con** (substring) của $$w$$.

**Ví dụ** với $$w = abcde$$: $$abc$$ là tiền tố, $$cde$$ là hậu tố, $$bcd$$ là chuỗi con.

## 2. Tập tất cả các chuỗi: $$\Sigma^*$$

### Định nghĩa: Kleene closure

Tập tất cả chuỗi (kể cả chuỗi rỗng) trên $$\Sigma$$ ký hiệu là $$\Sigma^*$$, gọi là **bao đóng Kleene** (Kleene closure) của $$\Sigma$$:

$$\Sigma^* = \{\epsilon\} \cup \Sigma \cup \Sigma^2 \cup \Sigma^3 \cup \ldots = \bigcup_{n \geq 0} \Sigma^n$$

trong đó $$\Sigma^n$$ là tập chuỗi có độ dài đúng $$n$$.

Tập chuỗi **khác rỗng** ký hiệu $$\Sigma^+ = \Sigma^* \setminus \{\epsilon\} = \bigcup_{n \geq 1} \Sigma^n$$.

<div class="content-box example-box" markdown="1">
**Ví dụ**

Với $$\Sigma = \{0, 1\}$$:

- $$\Sigma^0 = \{\epsilon\}$$ (1 chuỗi).
- $$\Sigma^1 = \{0, 1\}$$ (2 chuỗi).
- $$\Sigma^2 = \{00, 01, 10, 11\}$$ (4 chuỗi).
- $$\Sigma^n$$ có $$2^n$$ chuỗi.
- $$\Sigma^* = \{\epsilon, 0, 1, 00, 01, 10, 11, 000, \ldots\}$$ - tập **vô hạn đếm được**.
</div>

### Định lý: $$\Sigma^*$$ đếm được

Với $$\Sigma$$ hữu hạn, $$\Sigma^*$$ là tập **vô hạn đếm được**.

**Chứng minh**: Sắp xếp chuỗi theo thứ tự độ dài tăng dần, trong cùng độ dài sắp xếp theo thứ tự từ điển. Mỗi $$\Sigma^n$$ hữu hạn (có $$\lvert \Sigma \rvert^n$$ chuỗi), nên hợp của chúng đếm được.

Hệ quả quan trọng: tập tất cả chương trình hợp lệ (trên bảng chữ cái ASCII) là **đếm được**. Nhưng tập tất cả hàm $$f: \mathbb{N} \to \{0, 1\}$$ là **không đếm được** (định lý Cantor). Suy ra: **có nhiều hàm hơn chương trình** - tồn tại hàm không thể tính được. Đây là gốc rễ của bài toán không quyết định được (Chương 20).

## 3. Ngôn ngữ

### Định nghĩa: Ngôn ngữ

Một **ngôn ngữ** (language) trên bảng chữ cái $$\Sigma$$ là một tập con bất kỳ của $$\Sigma^*$$:

$$L \subseteq \Sigma^*$$

Vì $$\Sigma^*$$ đếm được, một ngôn ngữ có thể **hữu hạn** hoặc **vô hạn đếm được**.

<div class="content-box example-box" markdown="1">
**Một số ngôn ngữ trên $$\Sigma = \{0, 1\}$$**

- $$L_1 = \emptyset$$ - ngôn ngữ rỗng (không chứa chuỗi nào).
- $$L_2 = \{\epsilon\}$$ - ngôn ngữ chỉ chứa chuỗi rỗng. **Lưu ý**: $$L_2 \neq \emptyset$$.
- $$L_3 = \{0, 01, 011, 0111, \ldots\} = \{0\,1^n : n \geq 0\}$$ - vô hạn.
- $$L_4 = \{w \in \Sigma^* : \lvert w \rvert_0 = \lvert w \rvert_1\}$$ - các chuỗi có số 0 bằng số 1.
- $$L_5 = \{w : w = w^R\}$$ - các chuỗi đối xứng (palindrome).
- $$L_6 = \{0^n 1^n : n \geq 0\}$$ - chuỗi $$n$$ số 0 theo sau bởi $$n$$ số 1.
</div>

### Ngôn ngữ trong thực tế

| Ngôn ngữ thực tế | Bảng chữ cái | Ý nghĩa |
|---|---|---|
| Số nguyên thập phân hợp lệ | $$\{0,1,\ldots,9,-\}$$ | Không bắt đầu bằng 0 (trừ $$0$$ riêng). |
| Tên biến Python hợp lệ | ký tự ASCII | Bắt đầu chữ/`_`, theo sau chữ/số/`_`. |
| Địa chỉ email hợp lệ | ASCII | Theo RFC 5322. |
| Mã nguồn C hợp lệ | ASCII | Theo chuẩn C17. |
| HTML hợp lệ | Unicode | Theo HTML5 spec. |

## 4. Phép toán trên ngôn ngữ

Vì ngôn ngữ là tập hợp, ta có ngay các phép toán tập hợp: $$L_1 \cup L_2$$, $$L_1 \cap L_2$$, $$L_1 \setminus L_2$$, $$\overline{L} = \Sigma^* \setminus L$$.

Ngoài ra còn các phép toán đặc thù cho ngôn ngữ:

### Phép nối ngôn ngữ

$$L_1 L_2 = \{xy : x \in L_1, y \in L_2\}$$

**Ví dụ**: $$L_1 = \{a, ab\}$$, $$L_2 = \{b, c\}$$. Khi đó $$L_1 L_2 = \{ab, ac, abb, abc\}$$.

### Lũy thừa và Kleene star

- $$L^0 = \{\epsilon\}$$.
- $$L^{n+1} = L^n L$$.
- **Kleene star**: $$L^* = \bigcup_{n \geq 0} L^n = \{\epsilon\} \cup L \cup L^2 \cup \ldots$$
- **Kleene plus**: $$L^+ = \bigcup_{n \geq 1} L^n = L L^*$$.

**Trực giác**: $$L^*$$ là tập tất cả chuỗi tạo được bằng cách nối **không hoặc nhiều** chuỗi từ $$L$$. Đây là cách viết $$\Sigma^*$$ (khi coi $$\Sigma$$ như ngôn ngữ các chuỗi độ dài 1).

<div class="content-box example-box" markdown="1">
**Ví dụ**

Cho $$L = \{ab, cd\}$$.

- $$L^0 = \{\epsilon\}$$.
- $$L^1 = \{ab, cd\}$$.
- $$L^2 = \{abab, abcd, cdab, cdcd\}$$.
- $$L^* = \{\epsilon, ab, cd, abab, abcd, cdab, cdcd, ababab, \ldots\}$$.
</div>

### Đảo ngược ngôn ngữ

$$L^R = \{w^R : w \in L\}$$.

## 5. Phân loại ngôn ngữ: Phân cấp Chomsky

Câu hỏi trung tâm của lý thuyết ngôn ngữ hình thức: **một ngôn ngữ có thể được mô tả gọn gàng đến mức nào?** Câu trả lời tổng quát do **Noam Chomsky** (1956) đề xuất, gọi là **phân cấp Chomsky** (Chomsky hierarchy):

| Cấp | Loại ngôn ngữ | Văn phạm | Máy nhận | Ví dụ |
|:---:|---|---|---|---|
| 3 | Chính quy (regular) | RG | DFA / NFA | $$a^* b^*$$ |
| 2 | Phi ngữ cảnh (context-free) | CFG | PDA | $$\{a^n b^n\}$$ |
| 1 | Nhạy ngữ cảnh (context-sensitive) | CSG | LBA | $$\{a^n b^n c^n\}$$ |
| 0 | Đệ quy đếm được (recursively enumerable) | Unrestricted | Turing Machine | Mọi ngôn ngữ "tính được" |

Mỗi cấp bao gồm cấp cao hơn: $$\text{Reg} \subsetneq \text{CFL} \subsetneq \text{CSL} \subsetneq \text{RE}$$.

<div class="content-box insight-box" markdown="1">
**Ý nghĩa thực tế của phân cấp**

- **Chính quy**: đủ cho biểu thức chính quy (regex), lexer, tìm kiếm văn bản.
- **Phi ngữ cảnh**: đủ cho cú pháp ngôn ngữ lập trình (parser).
- **Nhạy ngữ cảnh**: đủ cho kiểm tra ngữ nghĩa nông (type checking nông).
- **Đệ quy đếm được**: tất cả những gì máy Turing có thể "liệt kê" - tức tất cả ngôn ngữ "tính được".
</div>

Phân cấp này được khảo sát chi tiết trong Bài 19.2.

## 6. Ngôn ngữ và Máy chấp nhận

Mỗi cấp trong phân cấp Chomsky tương ứng với một loại **máy chấp nhận** (acceptor):

- **DFA/NFA** (Bài 18.3) - chấp nhận chính xác lớp ngôn ngữ chính quy.
- **Pushdown automata** (PDA) - chấp nhận chính xác lớp ngôn ngữ phi ngữ cảnh.
- **Linear bounded automata** (LBA) - chấp nhận lớp ngôn ngữ nhạy ngữ cảnh.
- **Turing machine** (Bài 18.5) - chấp nhận lớp ngôn ngữ đệ quy đếm được.

**Định nghĩa**: ngôn ngữ $$L(M)$$ được **chấp nhận** bởi máy $$M$$ là tập tất cả chuỗi $$w$$ khiến $$M$$ dừng ở trạng thái chấp nhận.

Hai ngôn ngữ nổi tiếng nằm ngoài lớp chính quy nhưng trong lớp phi ngữ cảnh:

$$L_{a^n b^n} = \{a^n b^n : n \geq 0\}$$

$$L_{\text{paren}} = \text{tập các dãy ngoặc cân bằng}$$

Cả hai đòi hỏi "đếm" - mà DFA hữu hạn trạng thái không đếm được - nhưng PDA với stack thì làm được. Đây là lý do parser ngôn ngữ lập trình dùng stack.

<div class="content-box warning-box" markdown="1">
**Chấp nhận khác Quyết định**

Một ngôn ngữ là **đệ quy** (recursive) hay **quyết định được** (decidable) nếu có máy Turing **luôn dừng** và quyết định đúng "có/không".

Một ngôn ngữ là **đệ quy đếm được** (recursively enumerable, RE) nếu có máy Turing **dừng và chấp nhận** mọi chuỗi trong ngôn ngữ - nhưng có thể không dừng trên chuỗi ngoài ngôn ngữ.

Tồn tại ngôn ngữ RE nhưng không recursive: **bài toán dừng** (halting problem - Bài 20.4). Đây là ranh giới giữa "tính được" và "quyết định được".
</div>

## 7. Tại sao học Ngôn ngữ Hình thức?

Ngôn ngữ hình thức là **xương sống lý thuyết** của khoa học máy tính ứng dụng:

| Ứng dụng | Lớp ngôn ngữ | Công cụ |
|---|---|---|
| Tìm kiếm văn bản | Chính quy | `grep`, `sed`, `awk` |
| Lexer | Chính quy | `flex`, `lex` |
| Phân tích từ vựng | Chính quy | `re.match` trong Python |
| Parser | Phi ngữ cảnh | `yacc`, `bison`, ANTLR |
| Cú pháp HTML/XML/JSON | Phi ngữ cảnh | `xml.etree`, `json` |
| Mô hình hóa giao thức | Tự động hữu hạn | `model checking` |
| Sinh ngôn ngữ tự nhiên | Phi ngữ cảnh / xác suất | NLP, GPT |
| Phân tích DNA | Phi ngữ cảnh | `BioPython` |

Mỗi khi bạn dùng `grep`, viết file `.l`/`.y`, hay parse JSON, bạn đang vận hành kết quả của lý thuyết này.

## Tổng kết

- **Bảng chữ cái** $$\Sigma$$ là tập hữu hạn ký hiệu; **chuỗi** là dãy ký hiệu hữu hạn; **ngôn ngữ** là tập con của $$\Sigma^*$$.
- Phép toán cơ bản trên chuỗi: nối, đảo ngược, lũy thừa.
- Phép toán trên ngôn ngữ: tập hợp ($$\cup, \cap, \overline{\cdot}$$), nối, Kleene star $$L^*$$.
- $$\Sigma^*$$ luôn vô hạn đếm được, nhưng tập tất cả ngôn ngữ trên $$\Sigma$$ là **không đếm được** - nên có ngôn ngữ không mô tả được bằng bất kỳ chương trình nào.
- **Phân cấp Chomsky** sắp xếp ngôn ngữ theo độ phức tạp: chính quy $$\subsetneq$$ phi ngữ cảnh $$\subsetneq$$ nhạy ngữ cảnh $$\subsetneq$$ đệ quy đếm được.
- Mỗi lớp ngôn ngữ ứng với một loại máy nhận, từ DFA đến máy Turing.

## Bài tập

**Bài 1.** Cho $$\Sigma = \{a, b\}$$. Liệt kê $$\Sigma^3$$. Có bao nhiêu chuỗi?

**Bài 2.** Tính $$\lvert w \rvert$$, $$\lvert w \rvert_a$$, $$w^R$$ với $$w = aabbab$$.

**Bài 3.** Cho $$L_1 = \{a, ab\}$$, $$L_2 = \{b, ba\}$$. Tính $$L_1 L_2$$, $$L_2 L_1$$. So sánh.

**Bài 4.** Cho $$L = \{0, 1\}$$. Tính $$L^0, L^1, L^2$$, và đếm $$\lvert L^n \rvert$$.

**Bài 5.** Mô tả bằng lời các ngôn ngữ sau trên $$\Sigma = \{a, b\}$$:
- $$L_a = \{w : \lvert w \rvert \leq 3\}$$
- $$L_b = a^* b^*$$
- $$L_c = (ab)^*$$
- $$L_d = \{w : \lvert w \rvert \text{ chẵn}\}$$

**Bài 6.** Chứng minh $$(L^*)^* = L^*$$ với mọi ngôn ngữ $$L$$.

**Bài 7.** Cho $$L_1 = \{\epsilon\}$$, $$L_2 = \emptyset$$. Tính $$L_1 L_2$$, $$L_2 L_2$$, $$L_1^*$$, $$L_2^*$$.

**Bài 8.** Chứng minh tập tất cả ngôn ngữ trên $$\Sigma = \{0, 1\}$$ là **không đếm được**. (Gợi ý: dùng đường chéo Cantor lên ánh xạ từ ngôn ngữ sang dãy nhị phân $$\Sigma^* \to \{0,1\}$$.)

**Bài 9.** Cho ngôn ngữ $$L = \{a^n b^n : n \geq 0\}$$ trên $$\{a, b\}$$. Giải thích trực giác tại sao không thể có DFA hữu hạn trạng thái nhận đúng $$L$$.

**Bài 10.** Viết bằng tiếng Việt định nghĩa "địa chỉ email hợp lệ" theo dạng ngôn ngữ hình thức (bảng chữ cái, dạng tổng quát của chuỗi).

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, 8e, Chương 13.1-13.2.
- Michael Sipser, *Introduction to the Theory of Computation*, 3e, Chương 0-1.
- John Hopcroft, Rajeev Motwani, Jeffrey Ullman, *Introduction to Automata Theory, Languages, and Computation*, 3e, Chương 1.
- Noam Chomsky, "Three Models for the Description of Language" (1956) - bài báo gốc đề xuất phân cấp Chomsky.
</div>
