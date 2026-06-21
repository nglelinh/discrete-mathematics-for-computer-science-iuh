---
layout: post
title: "Biểu thức chính quy và Ngôn ngữ chính quy"
categories: chapter18
date: 2021-01-01
order: 4
required: true
lang: en
---

Lệnh `grep "^[A-Z][a-z]*ing$" file.txt` tìm các dòng bắt đầu bằng một chữ hoa, theo sau là các chữ thường, kết thúc bằng `ing`. Cú pháp ngắn gọn đó là một **biểu thức chính quy** (regular expression, regex), và nó được dùng khắp nơi: trong trình soạn thảo (`vim`, `vscode`), trình biên dịch, ngôn ngữ kịch bản (`sed`, `awk`, JavaScript, Python). Mọi regex đều **tương đương** với một automat hữu hạn nào đó - đây là nội dung **định lý Kleene**, một trong những kết quả nền tảng của lý thuyết automat.

Bài này định nghĩa hình thức regex, trình bày định lý Kleene (regex $$\Leftrightarrow$$ FSM), đưa ra hai cấu trúc đối ngẫu - **Thompson** (regex sang $$\varepsilon$$-NFA) và **state elimination** (DFA sang regex), và kết thúc bằng **bổ đề bơm** (pumping lemma) - công cụ chứng minh một ngôn ngữ **không** chính quy. Đây là điểm gặp nhau giữa **lý thuyết** (lớp ngôn ngữ chính quy có cấu trúc đại số đẹp) và **thực hành** (thư viện regex của mọi ngôn ngữ lập trình hiện đại).

![Biểu thức chính quy](/discrete-mathematics-for-computer-science-iuh/img/course/DFA-powerset-construction-example.svg)

*Hình 18.16: Regex mô tả ngôn ngữ chính quy — cùng lớp với DFA và NFA.*

![Thompson construction](/discrete-mathematics-for-computer-science-iuh/img/course/DFA-powerset-construction-example.svg)

*Hình 18.17: Xây NFA từ regex — mỗi toán tử regex tương ứng mẫu NFA nhỏ.*

![Kleene star](/discrete-mathematics-for-computer-science-iuh/img/course/Finite_state_machine_example_with_comments.svg)

*Hình 18.18: Toán tử $*$ (lặp 0 hoặc nhiều lần) — nền tảng cú pháp regex.*

![Lexical analysis](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

*Hình 18.19: Trình biên dịch dùng FSM/regex để phân tích từ vựng — tokenize mã nguồn.*

![Lớp ngôn ngữ chính quy](/discrete-mathematics-for-computer-science-iuh/img/course/Chomsky_hierarchy.svg)

*Hình 18.20: Regular languages nằm ở tầng thấp nhất phân cấp Chomsky.*

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** hình thức biểu thức chính quy và ngôn ngữ mà nó biểu diễn.
- **Phát biểu** định lý Kleene: regex và FSM cùng định nghĩa lớp ngôn ngữ chính quy.
- **Áp dụng** thuật toán Thompson để chuyển regex thành $$\varepsilon$$-NFA.
- **Áp dụng** bổ đề bơm để chứng minh một ngôn ngữ không chính quy.
- **Nhận ra** các tính chất đóng của lớp ngôn ngữ chính quy.

**Từ khóa**: biểu thức chính quy (regular expression), ngôn ngữ chính quy (regular language), định lý Kleene (Kleene's theorem), bao đóng Kleene (Kleene closure), Thompson construction, bổ đề bơm (pumping lemma), tính chất đóng (closure property).

## 1. Định nghĩa biểu thức chính quy

Cho bảng chữ cái $$\Sigma$$. **Biểu thức chính quy** trên $$\Sigma$$ được định nghĩa đệ quy:

**Cơ sở**:
- $$\emptyset$$ là regex, biểu diễn ngôn ngữ rỗng $$\emptyset$$.
- $$\varepsilon$$ là regex, biểu diễn ngôn ngữ $$\{\varepsilon\}$$ chỉ chứa chuỗi rỗng.
- Với mỗi $$a \in \Sigma$$, $$a$$ là regex, biểu diễn $$\{a\}$$.

**Đệ quy**: nếu $$r$$ và $$s$$ là regex biểu diễn ngôn ngữ $$L(r), L(s)$$ thì:
- $$r + s$$ (hợp / alternation) là regex, $$L(r + s) = L(r) \cup L(s)$$.
- $$rs$$ (ghép / concatenation) là regex, $$L(rs) = \{xy : x \in L(r), y \in L(s)\}$$.
- $$r^*$$ (sao Kleene / Kleene star) là regex, $$L(r^*) = \bigcup_{n=0}^{\infty} L(r)^n = \{\varepsilon, w_1, w_1 w_2, w_1 w_2 w_3, \ldots : w_i \in L(r)\}$$.

Một số ký hiệu phái sinh:
- $$r^+ = r r^*$$ (một lần trở lên).
- $$r^k$$ (ghép $$k$$ lần).
- $$(r)$$ dùng để gom nhóm.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: Một vài regex trên $$\{0, 1\}$$:

- $$(0+1)^*$$ - mọi chuỗi nhị phân.
- $$0^* 1^*$$ - một số `0`, theo sau một số `1`. Chấp nhận `001`, `1`, `0`, $$\varepsilon$$.
- $$(0+1)^* 01$$ - các chuỗi kết thúc bằng `01`.
- $$(01)^*$$ - $$\varepsilon$$, `01`, `0101`, `010101`, ...
- $$(0+1)^* 1 (0+1)^4$$ - bit thứ 5 từ cuối là `1`.
</div>

## 2. Định lý Kleene

**Định lý (Kleene, 1956)**: Một ngôn ngữ $$L \subseteq \Sigma^*$$ là chính quy khi và chỉ khi tồn tại một biểu thức chính quy biểu diễn $$L$$.

Tương đương:

$$\text{regex} \;\Longleftrightarrow\; \varepsilon\text{-NFA} \;\Longleftrightarrow\; \text{NFA} \;\Longleftrightarrow\; \text{DFA}$$

Tất cả các mô hình này cùng định nghĩa **lớp ngôn ngữ chính quy**.

### Chiều thứ nhất: regex $$\to$$ $$\varepsilon$$-NFA (Thompson construction)

Cho regex $$r$$, ta xây dựng $$\varepsilon$$-NFA $$N_r$$ chấp nhận $$L(r)$$ bằng **quy nạp cấu trúc**:

- Cơ sở $$\emptyset$$, $$\varepsilon$$, $$a$$: các NFA nhỏ với 1 hoặc 2 trạng thái.
- $$r + s$$: tạo trạng thái mới $$q_{\text{start}}$$ với hai $$\varepsilon$$-chuyển đến $$N_r$$ và $$N_s$$; nối hai trạng thái chấp nhận của $$N_r, N_s$$ vào một trạng thái chấp nhận mới bằng $$\varepsilon$$.
- $$rs$$: nối trạng thái chấp nhận của $$N_r$$ vào trạng thái khởi đầu của $$N_s$$ bằng $$\varepsilon$$.
- $$r^*$$: tạo cặp trạng thái mới; thêm $$\varepsilon$$-chuyển tạo vòng lặp qua $$N_r$$ và chuyển tắt khi $$r$$ xuất hiện 0 lần.

NFA Thompson cho regex độ dài $$n$$ có không quá $$2n$$ trạng thái - rất gọn.

### Chiều thứ hai: DFA $$\to$$ regex (state elimination)

Cho DFA, ta lần lượt **loại bỏ trạng thái trung gian**, mỗi lần thay các cạnh đi qua bằng regex tổng hợp các đường đi qua đó. Sau khi loại hết các trạng thái trung gian, regex còn lại trên cạnh nối $$q_0$$ với trạng thái chấp nhận chính là regex của ngôn ngữ.

<div class="content-box insight-box" markdown="1">
**Trực giác**: bất kỳ ngôn ngữ nào ta có thể **mô tả** bằng các phép hợp - ghép - sao Kleene từ các ký hiệu cơ bản, ta cũng có thể **nhận diện** bằng một máy hữu hạn trạng thái, và ngược lại. Hai cách nhìn (sản sinh chuỗi vs nhận diện chuỗi) cho cùng một lớp ngôn ngữ. Đây là kiểu kết quả "đối ngẫu" rất hay gặp trong toán học và khoa học máy tính.
</div>

## 3. Tính chất đóng của ngôn ngữ chính quy

Lớp ngôn ngữ chính quy **đóng** dưới nhiều phép toán:

| Phép toán | Đóng? | Cách xây dựng |
|---|---|---|
| Hợp $$L_1 \cup L_2$$ | Có | Regex: $$r_1 + r_2$$ hoặc NFA hợp |
| Giao $$L_1 \cap L_2$$ | Có | DFA tích (Cartesian product) |
| Bù $$\Sigma^* \setminus L$$ | Có | DFA: đảo tập chấp nhận |
| Ghép $$L_1 L_2$$ | Có | Regex: $$r_1 r_2$$ |
| Sao Kleene $$L^*$$ | Có | Regex: $$r^*$$ |
| Đảo ngược $$L^R$$ | Có | Đảo cạnh và đổi vai trò start/accept |
| Đồng cấu (homomorphism) | Có | Thay mỗi ký hiệu bằng chuỗi tương ứng |

Các tính chất đóng cho ta cách **chứng minh** một ngôn ngữ là chính quy bằng cách xây dựng nó từ các ngôn ngữ chính quy đã biết.

## 4. Bổ đề bơm: chứng minh không chính quy

Làm sao chứng minh một ngôn ngữ **không** chính quy? Công cụ kinh điển là **bổ đề bơm**.

**Bổ đề (Pumping Lemma)**: Nếu $$L$$ là chính quy, thì tồn tại số nguyên $$p \geq 1$$ (gọi là **độ dài bơm**) sao cho mọi chuỗi $$w \in L$$ với $$|w| \geq p$$ có thể phân tích $$w = xyz$$ thỏa mãn:

1. $$|y| \geq 1$$ (đoạn giữa không rỗng).
2. $$|xy| \leq p$$ (đoạn $$xy$$ ngắn).
3. Với mọi $$i \geq 0$$: $$xy^i z \in L$$ ("bơm" $$y$$ bao nhiêu lần cũng được).

**Trực giác**: nếu một DFA $$p$$ trạng thái đọc chuỗi dài hơn $$p$$, theo nguyên lý chuồng bồ câu nó phải lặp lại một trạng thái. Đoạn đường đi giữa hai lần đó tạo thành một "vòng lặp" có thể đi 0, 1, 2, ... lần - tương ứng với đoạn $$y$$.

### Cách dùng bổ đề bơm (chứng minh phản chứng)

Để chứng minh $$L$$ **không** chính quy:
1. Giả sử $$L$$ chính quy, gọi $$p$$ là độ dài bơm.
2. Chọn một chuỗi $$w \in L$$, $$|w| \geq p$$, "khó nhất" để bơm.
3. Với mọi cách phân tích $$w = xyz$$ thỏa mãn $$|y| \geq 1, |xy| \leq p$$, chỉ ra một $$i$$ sao cho $$xy^i z \notin L$$.
4. Mâu thuẫn $$\Rightarrow$$ $$L$$ không chính quy.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Chứng minh $$L = \{0^n 1^n : n \geq 0\}$$ không chính quy.

Giả sử có. Gọi $$p$$ là độ dài bơm. Chọn $$w = 0^p 1^p \in L$$, $$|w| = 2p \geq p$$.

Mọi phân tích $$w = xyz$$ với $$|xy| \leq p$$ phải có $$y$$ nằm hoàn toàn trong khối `0` đầu tiên: $$y = 0^k$$ với $$1 \leq k \leq p$$.

Bơm $$i = 2$$: $$xy^2 z = 0^{p+k} 1^p$$, có $$p + k$$ chữ `0` nhưng chỉ $$p$$ chữ `1`. Vậy $$xy^2 z \notin L$$.

Mâu thuẫn. Vậy $$L$$ không chính quy.
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 3**: $$L = \{w \in \{0,1\}^* : w \text{ là số nguyên tố ở dạng nhị phân}\}$$ cũng không chính quy. Một chứng minh tinh tế hơn dùng bổ đề bơm và định lý số học.
</div>

## 5. Ý nghĩa thực tiễn

- **`grep`, `sed`, `awk`**: chuyển regex thành DFA hoặc mô phỏng NFA để khớp dòng nhanh.
- **Phân tích từ vựng**: các trình sinh lexer như `flex`, `lex` chuyển định nghĩa regex thành DFA tối thiểu, sinh mã C khớp token rất nhanh.
- **Lập chỉ mục Lucene/Elasticsearch**: tìm kiếm văn bản nâng cao dựa trên các automat hữu hạn.
- **Kiểm tra giao thức**: đặc tả giao thức an toàn (ví dụ SSL handshake) bằng regex và kiểm tra tính tuân thủ.

<div class="content-box warning-box" markdown="1">
**Cảnh báo về regex "thực tế"**: các thư viện regex như PCRE (Perl Compatible Regular Expressions) bổ sung **backreference** (`\1`, `\2`), **lookahead/lookbehind**, vốn **không** thuộc lớp regex chính quy về mặt lý thuyết. Backreference cho phép biểu diễn các ngôn ngữ không chính quy (ví dụ $$ww$$), nhưng cũng làm bài toán khớp trở thành NP-khó trong trường hợp xấu nhất.
</div>

## Tổng kết

- **Biểu thức chính quy** định nghĩa đệ quy từ $$\emptyset, \varepsilon, a$$ với ba phép toán: hợp, ghép, sao Kleene.
- **Định lý Kleene**: regex, NFA, $$\varepsilon$$-NFA, DFA cùng định nghĩa lớp **ngôn ngữ chính quy**.
- **Thompson construction**: regex $$\to$$ $$\varepsilon$$-NFA gọn (không quá $$2n$$ trạng thái).
- **State elimination**: DFA $$\to$$ regex.
- **Bổ đề bơm**: công cụ chứng minh một ngôn ngữ không chính quy (ví dụ $$0^n 1^n$$).

## Bài tập

1. Viết regex cho ngôn ngữ "các chuỗi nhị phân có **chẵn** số chữ `0`".
2. Viết regex cho ngôn ngữ "các chuỗi trên $$\{a, b\}$$ **không chứa** chuỗi con `aa`".
3. Áp dụng Thompson construction cho regex $$(a + b)^* abb$$.
4. Chứng minh $$L = \{a^n b^m c^n : n, m \geq 0\}$$ không chính quy.
5. Chứng minh $$L = \{w \in \{0,1\}^* : |w| \text{ là số chính phương}\}$$ không chính quy. Gợi ý: bơm và so sánh độ dài.
6. Cho hai regex $$r = a^* b^*$$ và $$s = (ab)^*$$. Mô tả $$L(r) \cap L(s)$$.
7. Chứng minh lớp ngôn ngữ chính quy đóng dưới phép giao bằng cách dùng DFA tích.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. Section 13.3, 13.4.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3rd ed. Sections 1.3, 1.4.
- Hopcroft, J., Motwani, R., & Ullman, J. (2007). *Introduction to Automata Theory*, 3rd ed. Chapters 3-4.
- Kleene, S. C. (1956). "Representation of events in nerve nets and finite automata." *Automata Studies*, Princeton University Press.
</div>
