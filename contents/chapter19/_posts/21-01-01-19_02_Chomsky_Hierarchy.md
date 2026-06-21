---
layout: post
title: "Phân cấp Chomsky"
categories: chapter19
date: 2021-01-01
order: 2
required: true
lang: en
---

Năm 1956, **Noam Chomsky** - khi đó là một nhà ngôn ngữ học trẻ tại MIT - công bố bài báo "Three Models for the Description of Language". Mục đích của Chomsky là phân tích **ngôn ngữ tự nhiên** (tiếng Anh, tiếng Việt), nhưng phát hiện của ông lại định hình toàn bộ khoa học máy tính: ngôn ngữ có thể được phân loại theo **độ phức tạp của quy tắc tạo ra chúng**, và mỗi cấp ứng với một loại máy nhận khác nhau.

Hệ phân cấp này - gọi là **phân cấp Chomsky** (Chomsky hierarchy) - giải thích vì sao **regex** không đủ mạnh để parse HTML, vì sao trình biên dịch C cần **parser** mạnh hơn lexer, và vì sao tồn tại bài toán mà **không máy tính nào** giải được trong thời gian hữu hạn. Bài học này khảo sát chi tiết bốn cấp đó.

![Phân cấp Chomsky](/discrete-mathematics-for-computer-science-iuh/img/course/Chomsky_hierarchy.svg)

*Hình 19.6: Bốn loại grammar: Type-0 (không ràng buộc) đến Type-3 (chính quy).*

![Type-3: Regular](/discrete-mathematics-for-computer-science-iuh/img/course/Formal_languages.svg)

*Hình 19.7: Regular grammar ↔ DFA/NFA ↔ regex — dùng trong lexical analysis.*

![Type-2: Context-free](/discrete-mathematics-for-computer-science-iuh/img/course/DFA-powerset-construction-example.svg)

*Hình 19.8: Context-free grammar — parse cú pháp ngôn ngữ lập trình (CFG, BNF).*

![Type-1: Context-sensitive](/discrete-mathematics-for-computer-science-iuh/img/course/DFA-powerset-construction-example.svg)

*Hình 19.9: Context-sensitive grammar — ràng buộc phụ thuộc ngữ cảnh khi sinh chuỗi.*

![Type-0: Recursively enumerable](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_a_Turing_machine.svg)

*Hình 19.10: Type-0 tương đương máy Turing — lớp mạnh nhất trong phân cấp Chomsky.*

## Mục tiêu học tập

- Hiểu định nghĩa văn phạm (grammar) và cách sinh chuỗi.
- Phân biệt 4 loại văn phạm theo phân cấp Chomsky.
- Nhận diện ngôn ngữ thuộc lớp nào dựa vào dạng quy tắc sinh.
- Hiểu mối liên hệ giữa văn phạm và máy nhận.
- Áp dụng phân cấp để chọn công cụ phù hợp (regex, parser, máy Turing).

**Từ khóa**: grammar, production, derivation, regular grammar, context-free grammar, context-sensitive grammar, unrestricted grammar.

## 1. Văn phạm: Hệ thống quy tắc sinh

### Định nghĩa: Văn phạm

Một **văn phạm** (grammar) là bộ tứ $$G = (V, T, S, P)$$ trong đó:

- $$V$$: tập hữu hạn **biến** (variable, hay **ký hiệu phi tận cùng**, non-terminal). Thường viết hoa: $$S, A, B, \ldots$$
- $$T$$: tập hữu hạn **ký hiệu tận cùng** (terminal), $$V \cap T = \emptyset$$. Thường viết thường: $$a, b, c, \ldots$$
- $$S \in V$$: **ký hiệu xuất phát** (start symbol).
- $$P$$: tập hữu hạn **luật sinh** (production rule), mỗi luật có dạng $$\alpha \to \beta$$ với $$\alpha, \beta \in (V \cup T)^*$$ và $$\alpha$$ chứa ít nhất một biến.

**Trực giác**: Văn phạm là "máy viết câu". Bắt đầu từ $$S$$, mỗi bước thay một chuỗi con khớp vế trái của một luật bằng vế phải. Khi chỉ còn ký hiệu tận cùng, ta được một chuỗi của ngôn ngữ.

### Phép sinh (derivation)

Cho văn phạm $$G$$ và luật $$\alpha \to \beta$$. Ta viết:

$$u \alpha v \Rightarrow u \beta v$$

(đọc: $$u \alpha v$$ sinh ra $$u \beta v$$ trong một bước). Ký hiệu $$\Rightarrow^*$$ là **phép sinh không hoặc nhiều bước** (bao đóng phản xạ-bắc cầu).

**Ngôn ngữ sinh bởi văn phạm**:

$$L(G) = \{w \in T^* : S \Rightarrow^* w\}$$

tức tập tất cả chuỗi ký hiệu tận cùng sinh được từ $$S$$.

<div class="content-box example-box" markdown="1">
**Ví dụ: Văn phạm sinh $$\{a^n b^n : n \geq 0\}$$**

$$G = (\{S\}, \{a, b\}, S, P)$$ với $$P$$ gồm:

$$S \to aSb \mid \epsilon$$

(ký hiệu $$\mid$$ ngăn cách các luật cùng vế trái).

**Sinh chuỗi $$aabb$$**:

$$S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aabb$$

Ngôn ngữ sinh: $$L(G) = \{\epsilon, ab, aabb, aaabbb, \ldots\} = \{a^n b^n : n \geq 0\}$$.
</div>

## 2. Bốn cấp của Phân cấp Chomsky

Chomsky phân loại văn phạm theo **dạng cho phép của vế trái và vế phải** trong các luật sinh:

| Cấp | Tên | Hạn chế trên $$\alpha \to \beta$$ | Máy nhận |
|:---:|---|---|---|
| **0** | Không hạn chế (unrestricted) | $$\alpha$$ chứa ít nhất 1 biến, $$\beta$$ bất kỳ. | Turing machine (TM) |
| **1** | Nhạy ngữ cảnh (context-sensitive) | $$\lvert \alpha \rvert \leq \lvert \beta \rvert$$ (trừ $$S \to \epsilon$$) | Linear bounded automaton (LBA) |
| **2** | Phi ngữ cảnh (context-free) | $$\alpha$$ chỉ là một biến đơn lẻ. | Pushdown automaton (PDA) |
| **3** | Chính quy (regular) | Luật dạng $$A \to aB$$, $$A \to a$$, hoặc $$A \to \epsilon$$ | Finite automaton (DFA/NFA) |

Mỗi cấp **bị bao hàm bởi cấp số nhỏ hơn**: cấp 3 ⊂ cấp 2 ⊂ cấp 1 ⊂ cấp 0.

<div class="content-box info-box" markdown="1">
**Ngữ pháp nhạy ngữ cảnh: tại sao tên gọi?**

Luật cấp 1 nhìn chung có dạng $$\alpha A \gamma \to \alpha \beta \gamma$$ với $$\beta \neq \epsilon$$. Nghĩa là biến $$A$$ được thay bằng $$\beta$$ **chỉ khi đứng trong ngữ cảnh** $$\alpha \cdots \gamma$$. Phép thay phụ thuộc ngữ cảnh, đối lập với cấp 2 (phi ngữ cảnh) - nơi luật $$A \to \beta$$ áp dụng được **bất kể** xung quanh $$A$$ là gì.
</div>

## 3. Cấp 3 - Văn phạm chính quy

### Định nghĩa

Một **văn phạm chính quy** (regular grammar, RG) là văn phạm với tất cả luật có dạng:

- $$A \to aB$$ (biến $$A$$ sinh ký hiệu $$a$$ rồi đến biến $$B$$), hoặc
- $$A \to a$$, hoặc
- $$A \to \epsilon$$.

Đây là **văn phạm chính quy phải** (right-linear). Có dạng đối ngẫu là **văn phạm chính quy trái** (left-linear) - cũng cho cùng lớp ngôn ngữ.

### Ví dụ

Văn phạm cho ngôn ngữ "chuỗi nhị phân kết thúc bằng $$01$$":

$$
\begin{aligned}
S &\to 0S \mid 1S \mid 0A \\
A &\to 1
\end{aligned}
$$

Sinh chuỗi $$10101$$:

$$S \Rightarrow 1S \Rightarrow 10S \Rightarrow 101S \Rightarrow 1010A \Rightarrow 10101$$

### Định lý (Kleene): Tương đương với DFA/NFA và Regex

Ba lớp sau **bằng nhau**:

1. Lớp ngôn ngữ sinh bởi văn phạm chính quy.
2. Lớp ngôn ngữ được nhận bởi DFA/NFA (Bài 18.3).
3. Lớp ngôn ngữ mô tả được bằng biểu thức chính quy (regex, Bài 18.4).

Đây là **ngôn ngữ chính quy** (regular language). Gọn, hiệu quả, nhưng **không đếm được**: không thể tạo $$\{a^n b^n\}$$.

### Ứng dụng

- **Lexer** trong trình biên dịch.
- `grep`, `sed`, `awk`.
- Tìm kiếm văn bản trong editor.
- Mô hình hóa giao thức trạng thái hữu hạn.

## 4. Cấp 2 - Văn phạm phi ngữ cảnh

### Định nghĩa

Một **văn phạm phi ngữ cảnh** (context-free grammar, CFG) có mọi luật dạng:

$$A \to \beta \quad (A \in V, \; \beta \in (V \cup T)^*)$$

Vế trái **chỉ là một biến đơn lẻ**, vế phải là chuỗi bất kỳ. "Phi ngữ cảnh" vì việc thay $$A$$ bằng $$\beta$$ không phụ thuộc ký hiệu xung quanh $$A$$.

### Ví dụ 1: Cặp ngoặc cân bằng

$$S \to (S) \mid SS \mid \epsilon$$

Sinh $$(())()$$:

$$S \Rightarrow SS \Rightarrow (S)S \Rightarrow ((S))S \Rightarrow (())S \Rightarrow (())(S) \Rightarrow (())()$$

### Ví dụ 2: Biểu thức số học

$$
\begin{aligned}
E &\to E + T \mid T \\
T &\to T * F \mid F \\
F &\to ( E ) \mid \text{num}
\end{aligned}
$$

Văn phạm này sinh tất cả biểu thức cộng/nhân hợp lệ.

### Định lý: Tương đương với PDA

Lớp ngôn ngữ sinh bởi CFG bằng lớp ngôn ngữ nhận bởi **pushdown automaton** (PDA) - tự động có ngăn xếp (stack).

**Trực giác**: Stack cho phép "nhớ" các ký hiệu chờ ghép. Đó là cách parse cặp ngoặc, hoặc nhận $$\{a^n b^n\}$$ (đẩy $$n$$ ký hiệu $$a$$ vào stack, rồi pop khi đọc $$b$$).

### Ứng dụng

- **Parser** ngôn ngữ lập trình (yacc, bison, ANTLR).
- Cú pháp HTML, XML, JSON.
- Phân tích cú pháp ngôn ngữ tự nhiên.

CFG được khảo sát chi tiết ở Bài 19.3.

## 5. Cấp 1 - Văn phạm nhạy ngữ cảnh

### Định nghĩa

Một **văn phạm nhạy ngữ cảnh** (context-sensitive grammar, CSG) có mọi luật $$\alpha \to \beta$$ thỏa $$\lvert \alpha \rvert \leq \lvert \beta \rvert$$ (trừ luật đặc biệt $$S \to \epsilon$$ nếu $$S$$ không xuất hiện ở vế phải bất kỳ luật nào).

Tương đương dạng "có ngữ cảnh": $$\alpha_1 A \alpha_2 \to \alpha_1 \beta \alpha_2$$ với $$\beta \neq \epsilon$$.

### Ví dụ: $$\{a^n b^n c^n : n \geq 1\}$$

Đây là ngôn ngữ **không phi ngữ cảnh** (chứng minh bằng pumping lemma cho CFL), nhưng **nhạy ngữ cảnh**:

$$
\begin{aligned}
S &\to aSBC \mid aBC \\
CB &\to BC \\
aB &\to ab \\
bB &\to bb \\
bC &\to bc \\
cC &\to cc
\end{aligned}
$$

Sinh chuỗi $$aabbcc$$ là bài tập (gợi ý: $$S \Rightarrow aSBC \Rightarrow aaBCBC \Rightarrow \ldots$$).

### Định lý: Tương đương với LBA

Lớp CSL bằng lớp ngôn ngữ nhận bởi **linear bounded automaton** (LBA) - máy Turing với băng giới hạn bằng độ dài đầu vào.

### Ứng dụng

CSL ít gặp trực tiếp trong thực tế vì:

- **Quá mạnh** so với cú pháp ngôn ngữ lập trình.
- **Quá yếu** so với mô hình tổng quát máy tính.

Nhưng CSL đủ mạnh để mô hình hóa nhiều ràng buộc ngữ nghĩa (semantic): "biến phải khai báo trước khi dùng", "số tham số khớp với số đối".

## 6. Cấp 0 - Văn phạm không hạn chế

### Định nghĩa

Một **văn phạm không hạn chế** (unrestricted grammar) có luật dạng $$\alpha \to \beta$$ với $$\alpha$$ chứa ít nhất một biến, $$\beta$$ bất kỳ trong $$(V \cup T)^*$$ (kể cả rỗng).

### Định lý: Tương đương với Máy Turing

Lớp ngôn ngữ sinh bởi văn phạm không hạn chế = lớp **ngôn ngữ đệ quy đếm được** (recursively enumerable, RE) = lớp ngôn ngữ nhận bởi máy Turing.

Cụ thể: $$L \in \text{RE}$$ khi và chỉ khi có máy Turing $$M$$ sao cho $$L = L(M)$$ (tức $$M$$ dừng và chấp nhận đúng các chuỗi của $$L$$; trên chuỗi ngoài $$L$$, $$M$$ có thể không dừng).

### Đệ quy vs Đệ quy đếm được

- **Recursive** (decidable): có máy Turing **luôn dừng** và quyết định "có/không".
- **Recursively enumerable**: có máy Turing chấp nhận mọi chuỗi của $$L$$, nhưng có thể không dừng trên chuỗi ngoài.

**Tồn tại** $$L \in \text{RE} \setminus \text{Recursive}$$: ví dụ kinh điển là **bài toán dừng** (halting problem - Bài 20.4). Đây là ranh giới sâu sắc nhất trong lý thuyết tính toán.

<div class="content-box warning-box" markdown="1">
**Lưu ý quan trọng**

Phân cấp Chomsky **không bao gồm** mọi ngôn ngữ. Có ngôn ngữ thậm chí không thuộc cấp 0 (không đệ quy đếm được). Ví dụ: bù của bài toán dừng. Đó là ngôn ngữ tồn tại (theo tập hợp) nhưng không máy tính nào liệt kê hết được.
</div>

## 7. Quan hệ bao hàm thực sự

$$\text{Reg} \subsetneq \text{CFL} \subsetneq \text{CSL} \subsetneq \text{RE}$$

Mỗi bao hàm là **thật sự** (proper) - tức tồn tại ngôn ngữ ở cấp lớn hơn nhưng không ở cấp nhỏ hơn:

| Ngôn ngữ | Thuộc | Không thuộc |
|---|---|---|
| $$a^* b^*$$ | Reg | (thuộc Reg) |
| $$\{a^n b^n\}$$ | CFL | Reg |
| $$\{a^n b^n c^n\}$$ | CSL | CFL |
| $$\{w \# w : w \in \{0,1\}^*\}$$ | CSL | CFL |
| Bài toán dừng | RE | Recursive |
| Bù bài toán dừng | (ngoài RE) | RE |

### Bằng chứng (sketch): $$\{a^n b^n\} \notin \text{Reg}$$

Dùng **bổ đề bơm cho ngôn ngữ chính quy** (pumping lemma, Bài 18.4): nếu $$L$$ chính quy với hằng số bơm $$p$$, thì chuỗi $$a^p b^p \in L$$ phải tách được $$xyz$$ với $$\lvert xy \rvert \leq p$$, $$\lvert y \rvert \geq 1$$, và $$xy^i z \in L$$ với mọi $$i$$. Vì $$\lvert xy \rvert \leq p$$ nên $$y$$ toàn $$a$$; bơm $$y$$ sẽ phá vỡ điều kiện "số $$a$$ = số $$b$$". Mâu thuẫn.

### Bằng chứng (sketch): $$\{a^n b^n c^n\} \notin \text{CFL}$$

Dùng **bổ đề bơm cho ngôn ngữ phi ngữ cảnh**: ý tưởng tương tự nhưng với $$uvxyz$$.

## 8. Bảng so sánh tổng hợp

| Tiêu chí | Reg | CFL | CSL | RE |
|---|:---:|:---:|:---:|:---:|
| Dạng luật | $$A \to aB \mid a \mid \epsilon$$ | $$A \to \beta$$ | $$\lvert \alpha \rvert \leq \lvert \beta \rvert$$ | $$\alpha \to \beta$$ tùy ý |
| Máy nhận | DFA/NFA | PDA | LBA | Turing |
| Bộ nhớ | Hữu hạn | Stack | Tuyến tính | Vô hạn |
| Đóng dưới $$\cup$$ | Có | Có | Có | Có |
| Đóng dưới $$\cap$$ | Có | Không | Có | Có |
| Đóng dưới bù $$\overline{L}$$ | Có | Không | Có | Không |
| Bài toán thuộc về | $$O(n)$$ | $$O(n^3)$$ (CYK) | $$\text{PSPACE}$$ | Không quyết định được |
| Bài toán rỗng $$L = \emptyset$$? | Quyết định được | Quyết định được | Không quyết định được | Không quyết định được |

<div class="content-box insight-box" markdown="1">
**Mẹo nhận diện cấp**

- Cần **đếm** (như $$a^n b^n$$)? → cần ít nhất CFL.
- Cần đếm **ba thứ trở lên** hoặc kiểm tra bằng nhau (như $$a^n b^n c^n$$, $$ww$$)? → cần ít nhất CSL.
- Chỉ cần "khớp mẫu" với độ phức tạp cố định? → Reg.
- Bài toán tổng quát (kiểm tra chương trình dừng)? → RE / ngoài Chomsky.
</div>

## 9. Chọn công cụ theo phân cấp

Phân cấp Chomsky cho ta **luật chọn công cụ**:

| Tác vụ | Cấp cần thiết | Công cụ thực tế |
|---|:---:|---|
| Tìm email trong file log | Reg | `grep`, regex Python |
| Tokenize mã nguồn | Reg | `flex`, `re.findall` |
| Parse HTML / XML | CFL (gần như) | `lxml`, `BeautifulSoup` |
| Parse JSON | CFL | `json.loads` |
| Parse C / Python | CFL + ngữ cảnh | `yacc`, `bison`, `ANTLR` |
| Kiểm tra kiểu (type check) | CSL gần như | trình biên dịch riêng |
| Kiểm tra chương trình dừng | Ngoài RE | Không tồn tại! (Bài 20.4) |

<div class="content-box warning-box" markdown="1">
**Sai lầm phổ biến**

Cố gắng parse HTML bằng regex là chuyện kinh điển - HTML có cấu trúc lồng nhau (`<div><div>...</div></div>`), tức cần **CFL**, không Reg. Bài đăng nổi tiếng trên Stack Overflow: ["You can't parse [X]HTML with regex"](https://stackoverflow.com/a/1732454/1736192) đã trở thành huyền thoại.
</div>

## Tổng kết

- **Văn phạm** $$G = (V, T, S, P)$$ sinh ngôn ngữ $$L(G)$$ bằng cách áp dụng luật sinh từ $$S$$.
- **Phân cấp Chomsky** sắp xếp 4 lớp văn phạm theo độ phức tạp luật:
  - Cấp 3: chính quy (regular), tương đương DFA/regex.
  - Cấp 2: phi ngữ cảnh (CFG), tương đương PDA.
  - Cấp 1: nhạy ngữ cảnh (CSG), tương đương LBA.
  - Cấp 0: không hạn chế, tương đương máy Turing.
- Bao hàm thực sự: $$\text{Reg} \subsetneq \text{CFL} \subsetneq \text{CSL} \subsetneq \text{RE}$$.
- Mỗi cấp ứng với một loại máy nhận với khả năng bộ nhớ khác nhau.
- Phân cấp là kim chỉ nam **chọn công cụ**: dùng regex cho lexer, dùng parser CFG cho cú pháp, không dùng regex cho HTML.

## Bài tập

**Bài 1.** Cho $$G$$: $$S \to aSb \mid \epsilon$$. Sinh chuỗi $$aaabbb$$. Liệt kê tất cả bước.

**Bài 2.** Văn phạm nào là chính quy? Phi ngữ cảnh? Nhạy ngữ cảnh?
- (a) $$S \to aS \mid \epsilon$$
- (b) $$S \to aSb \mid \epsilon$$
- (c) $$S \to aSbS \mid bSaS \mid \epsilon$$
- (d) $$aSb \to aabb$$
- (e) $$S \to SS \mid (S) \mid \epsilon$$

**Bài 3.** Xây dựng văn phạm chính quy cho ngôn ngữ "chuỗi nhị phân có **chẵn** số 1".

**Bài 4.** Xây dựng văn phạm phi ngữ cảnh cho ngôn ngữ palindrome trên $$\{0, 1\}$$.

**Bài 5.** Sinh chuỗi $$aabbcc$$ trong văn phạm nhạy ngữ cảnh cho $$\{a^n b^n c^n\}$$ ở Mục 5.

**Bài 6.** Giải thích vì sao $$\{ww : w \in \{0,1\}^*\}$$ không phi ngữ cảnh. (Gợi ý: pumping lemma cho CFL.)

**Bài 7.** Cho ngôn ngữ $$L = \{a^i b^j c^k : i = j \text{ hoặc } j = k\}$$. $$L$$ thuộc cấp nào? Cho lý do.

**Bài 8.** Bạn được giao nhiệm vụ kiểm tra "tất cả thẻ mở `<X>` trong file có thẻ đóng `</X>` tương ứng". Bạn dùng regex hay parser? Tại sao?

**Bài 9.** Chứng minh: lớp ngôn ngữ chính quy đóng dưới phép giao. (Gợi ý: tích Descartes của hai DFA.)

**Bài 10.** Tìm một ngôn ngữ $$L$$ sao cho cả $$L$$ và $$\overline{L}$$ đều thuộc RE. Chứng minh khi đó $$L$$ thuộc Recursive.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Noam Chomsky, "Three Models for the Description of Language", *IRE Transactions on Information Theory* (1956) - bài báo khởi đầu.
- Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, 8e, Chương 13.3-13.4.
- Michael Sipser, *Introduction to the Theory of Computation*, 3e, Chương 2-5.
- John Hopcroft, Rajeev Motwani, Jeffrey Ullman, *Introduction to Automata Theory*, 3e, Chương 5-9.
</div>
