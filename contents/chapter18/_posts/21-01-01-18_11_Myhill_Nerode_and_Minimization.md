---
layout: post
title: "Myhill–Nerode và DFA Tối tiểu"
categories: chapter18
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Quan hệ tương đương Myhill–Nerode ~L, định lý Myhill–Nerode, chứng minh ngôn ngữ không chính quy và thuật toán tối tiểu hóa DFA."
---

> **Câu chuyện mở đầu:** Cho cùng một ngôn ngữ chính quy, hai lập trình viên có thể thiết kế hai DFA trông rất khác nhau — một cái 4 trạng thái, một cái 9 trạng thái. Liệu có tồn tại một **DFA nhỏ nhất duy nhất** giống như phân số tối giản trong số học không? **Định lý Myhill–Nerode** (1957–1958) trả lời **CÓ một cách tuyệt đối**: mọi ngôn ngữ chính quy đều có **đúng 1 DFA tối tiểu duy nhất (sai khác đổi tên trạng thái)** — và số trạng thái tối tiểu đó chính là số lớp tương đương của quan hệ phân biệt hậu tố $$\equiv_L$$!

<div class="textbook-epigraph" markdown="1">

"The number of states you need is the number of distinguishable futures."

<span class="epigraph-attribution">— Myhill–Nerode</span>

</div>

Định lý Myhill–Nerode là công cụ **mạnh hơn bổ đề bơm**, vừa cung cấp điều kiện cần và đủ cho tính chính quy vừa xác định chính xác cận dưới số trạng thái của DFA tối tiểu.

## Mục tiêu

![Định lý Myhill–Nerode & Tối tiểu hóa DFA](/discrete-mathematics-for-computer-science-iuh/img/course/myhill_nerode_min.svg)

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** quan hệ tương đương không phân biệt hậu tố $$x\sim_L y$$.
- **Phát biểu** định lý Myhill–Nerode.
- **Áp dụng** định lý để chứng minh ngôn ngữ không chính quy và tìm cận dưới số trạng thái DFA.

</div>

## Kiến thức cần nhớ: Định lý Myhill–Nerode & Tối tiểu hóa DFA

### 1. Quan hệ Tương đương Myhill–Nerode ($$x \equiv_L y$$)
- **Bản chất:** Hai chuỗi tiền tố $$x, y \in \Sigma^*$$ gọi là **không phân biệt được theo $$L$$** ($$x \equiv_L y$$) nếu với **MỌI** hậu tố $$z \in \Sigma^*$$:
  $$
  xz \in L \quad\Longleftrightarrow\quad yz \in L.
  $$
  Ngược lại, chỉ cần tồn tại **1 hậu tố phân cách** $$z$$ sao cho đúng 1 trong 2 chuỗi $$xz, yz$$ thuộc $$L$$, thì $$x \not\equiv_L y$$ — nghĩa là mọi DFA nhận $$L$$ **bắt buộc phải đưa $$x$$ và $$y$$ vào 2 trạng thái KHÁC NHAU**!

### 2. Định lý Myhill–Nerode (Điều kiện CẦN VÀ ĐỦ — mạnh hơn cả Bổ đề Bơm!)
- **Định lý:** Ngôn ngữ $$L$$ là chính quy **khi và chỉ khi** số lớp tương đương (chỉ số) của $$\equiv_L$$ là **hữu hạn**! Hơn nữa, số lớp tương đương $$k$$ chính là **số trạng thái của DFA tối tiểu duy nhất** nhận $$L$$!

### 3. Thuật toán Tối tiểu hóa DFA (Table-Filling / Hopcroft)
- **Bản chất:** Loại bỏ các trạng thái không đạt tới được từ $$q_0$$, rồi chia đôi dần các nhóm trạng thái (bắt đầu từ 2 nhóm $$F$$ và $$Q \setminus F$$) bất cứ khi nào hai trạng thái trong cùng nhóm chuyển sang hai nhóm khác nhau trên cùng một ký tự $$a$$!

## Ví dụ tính tay làm từng bước

### Ví dụ 1: Tìm số trạng thái tối tiểu của $$L = \{\text{chuỗi nhị phân kết thúc bằng } 01\}$$
Xét 3 chuỗi đại diện $$\varepsilon,\; 0,\; 01$$ và kiểm tra từng cặp bằng hậu tố phân cách:
- $$\varepsilon$$ vs. $$0$$: chọn hậu tố $$z = 1$$ $$\implies \varepsilon\cdot 1 = 1 \notin L$$, nhưng $$0\cdot 1 = 01 \in L \implies \varepsilon \not\equiv_L 0$$!
- $$\varepsilon$$ vs. $$01$$: chọn hậu tố $$z = \varepsilon$$ $$\implies \varepsilon \notin L$$, nhưng $$01 \in L \implies \varepsilon \not\equiv_L 01$$!
- $$0$$ vs. $$01$$: chọn hậu tố $$z = \varepsilon$$ $$\implies 0 \notin L$$, nhưng $$01 \in L \implies 0 \not\equiv_L 01$$!

Mọi chuỗi bất kỳ $$w \in \{0,1\}^*$$ đều rơi vào đúng 1 trong 3 lớp: (1) kết thúc bằng `01` ($$[01]$$), (2) kết thúc bằng `0` ($$[0]$$), hoặc (3) phần còn lại ($$[\varepsilon]$$). Vậy **DFA tối tiểu bắt buộc có đúng 3 trạng thái**!

### Ví dụ 2: Chứng minh 2 dòng $$L = \{0^n 1^n\}$$ KHÔNG chính quy bằng Myhill–Nerode
Xét tập vô hạn các chuỗi $$S = \{\varepsilon, 0, 0^2, 0^3, \dots\}$$. Với hai chỉ số bất kỳ $$i \neq j$$, chọn hậu tố phân cách $$z = 1^i$$:
$$
0^i \cdot 1^i \in L, \qquad \text{nhưng} \qquad 0^j \cdot 1^i \notin L \;(\text{vì } j \neq i)!
$$
Vậy vô hạn chuỗi trong $$S$$ đôi một **không tương đương nhau** $$\implies \equiv_L$$ có **vô hạn lớp tương đương** $$\implies$$ theo Myhill–Nerode, $$L$$ **KHÔNG chính quy**! (Nhanh và gọn hơn Bổ đề Bơm gấp nhiều lần!)

### Giải thích: 4 bước áp dụng Myhill–Nerode & Tối tiểu hóa DFA
#### Bước 1: Dùng Myhill–Nerode như công cụ chứng minh "Không chính quy" sắc bén nhất
Chỉ cần tìm một tập vô hạn $$S$$ mà mọi cặp $$x \neq y \in S$$ đều có 1 hậu tố phân cách $$z$$ — không bao giờ bị vướng trường hợp như Bổ đề Bơm!

#### Bước 2: Dùng Myhill–Nerode để tìm cận dưới số trạng thái DFA
Chỉ ra $$k$$ chuỗi đôi một phân biệt được bằng hậu tố $$\implies$$ mọi DFA nhận $$L$$ phải có ít nhất $$k$$ trạng thái!

#### Bước 3: Chạy thuật toán Phân hoạch (Partition Refinement) để tối tiểu hóa DFA
Bước 0: Xóa mọi trạng thái không đi tới được từ $$q_0$$. Bước 1: Tách $$P_0 = \{F, Q\setminus F\}$$. Bước lặp: tách nhóm nếu hai trạng thái dẫn sang hai nhóm khác nhau trên cùng 1 ký tự $$a$$, dừng khi phân hoạch ổn định!

#### Bước 4: Kiểm tra tính duy nhất của DFA tối tiểu
Gộp mỗi nhóm cuối thành 1 trạng thái: kết quả là DFA tối tiểu **duy nhất** — cho phép kiểm tra hai DFA có tương đương không bằng cách tối tiểu hóa cả hai rồi so sánh đẳng cấu!

$$
\text{Ngôn ngữ }L
\;\xrightarrow{\;x \equiv_L y \iff (\forall z:\; xz\in L \Leftrightarrow yz\in L)\;}\;
\begin{cases}
\text{Vô hạn lớp} \implies L \text{ KHÔNG chính quy} \\
k\text{ lớp hữu hạn} \implies \text{DFA tối tiểu duy nhất (}k\text{ trạng thái)}
\end{cases}
$$

## Quan hệ tương đương Myhill–Nerode

<div class="textbook-definition" markdown="1">

Cho ngôn ngữ $$L \subseteq \Sigma^*$$. Hai chuỗi $$x, y \in \Sigma^*$$ gọi là tương đương theo $$L$$, ký hiệu $$x\sim_L y$$, nếu và chỉ nếu với mọi hậu tố $$z\in\Sigma^*$$:

$$xz\in L\Leftrightarrow yz\in L.$$

</div>

Quan hệ $$\sim_L$$ là một quan hệ tương đương trên $$\Sigma^*$$, phân hoạch tập chuỗi thành các lớp tương đương $$[x]$$.

## Định lý Myhill–Nerode

<div class="textbook-theorem" markdown="1">

**Định lý (Myhill–Nerode).** Ngôn ngữ $$L$$ là chính quy khi và chỉ khi số lớp tương đương của quan hệ $$\sim_L$$ là hữu hạn. Khi đó, DFA tối tiểu nhận $$L$$ có số trạng thái đúng bằng số lớp tương đương này (mỗi lớp ứng với một trạng thái).

</div>

**Ý tưởng chứng minh.**  
Chiều ($$\Rightarrow$$): Nếu có DFA nhận $$L$$, quan hệ “đưa máy về cùng một trạng thái” $$\hat\delta(q_0,x)=\hat\delta(q_0,y)$$ làm mịn quan hệ $$\sim_L$$ (cùng trạng thái thì mọi hậu tố đều cho cùng kết quả), nên số lớp của $$\sim_L$$ không vượt quá $$\lvert Q\rvert$$.  
Chiều ($$\Leftarrow$$): Nếu số lớp hữu hạn, ta dựng trực tiếp DFA trên tập các lớp tương đương với $$\delta([x],a)=[xa]$$ (xác định tốt) và $$F=\{[x]:x\in L\}$$. $$\square$$

## Ứng dụng

Với ngôn ngữ $$L = \{0^n1^n : n \ge 0\}$$, mọi cặp $$0^i$$ và $$0^j$$ ($$i \neq j$$) đều không tương đương vì hậu tố $$z=1^i$$ cho $$0^i1^i \in L$$ nhưng $$0^j1^i \notin L$$. Do đó $$\sim_L$$ có vô hạn lớp tương đương, suy ra $$L$$ không chính quy.

## Tối tiểu hóa DFA

Trong thực hành, ta tối tiểu hóa DFA bằng phương pháp điền bảng (*table-filling*) hoặc tinh chỉnh phân hoạch (*partition refinement*) để gộp các trạng thái không phân biệt được; thuật toán Hopcroft thực hiện việc này trong thời gian $$O(n\log n)$$.

### Minh họa tương tác

Minh họa quá trình tối tiểu hóa DFA bằng cách gộp dần các nhóm trạng thái tương đương:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa101" data-tab="minimize"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh $$\sim_L$$ là một quan hệ tương đương trên $$\Sigma^*$$.
2. Xác định số lớp tương đương của ngôn ngữ “chuỗi nhị phân có số bit 1 chẵn”.
3. Xét ngôn ngữ $$\{a^ib^jc^k:i=j\text{ hoặc }j=k\}$$ — nên dùng định lý Myhill–Nerode hay bổ đề bơm để chứng minh không chính quy?

## Tài liệu đọc thêm

Sipser (mục bổ sung Myhill–Nerode); Hopcroft (thuật toán tối tiểu hóa); Kozen.

## Tóm tắt

Định lý Myhill–Nerode gắn trực tiếp số trạng thái tối tiểu của DFA với số lớp chuỗi có thể phân biệt bằng hậu tố, đồng thời cung cấp tiêu chuẩn cần và đủ cho tính chính quy.

**Bài tiếp theo:** Máy Turing.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=hOzc4BUIXRk">Minimization of Deterministic Finite Automata (DFA)</a> — Neso Academy, tiếng Anh. Giới thiệu bài toán tối tiểu hóa DFA, ứng dụng trực tiếp của Myhill–Nerode.
- <a href="https://www.youtube.com/watch?v=fWDOqJoKY3k">Myhill-Nerode Theorem for DFA Minimization</a> — Neso Academy, tiếng Anh. Trình bày định lý Myhill–Nerode và quan hệ không phân biệt trạng thái.
- <a href="https://www.youtube.com/watch?v=0XaGAkY09Wc">Minimization of DFA (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ cụ thể về gộp các trạng thái tương đương.
