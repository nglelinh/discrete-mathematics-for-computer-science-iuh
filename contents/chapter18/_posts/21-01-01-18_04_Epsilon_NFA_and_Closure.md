---
layout: post
title: "ε-NFA và Epsilon-closure"
categories: chapter18
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Chuyển trạng thái ε, định nghĩa bao đóng epsilon E(S), thuật toán tính bao đóng và điều kiện chấp nhận của ε-NFA."
---

> **Câu chuyện mở đầu:** Nếu bạn đã thiết kế xong một NFA nhận số nguyên và một NFA nhận số thập phân, làm sao **nối hai cỗ máy đó lại với nhau** thành một máy duy nhất nhận "số nguyên HOẶC số thập phân" mà không phải vẽ lại từ đầu? Câu trả lời là thêm **mũi tên chuyển rỗng ($$\varepsilon$$-transition)** — cho phép máy nhảy sang trạng thái khác mà **không cần đọc bất kỳ ký tự nào**! Đó là **$$\varepsilon$$-NFA**, mảnh ghép hoàn hảo để chứng minh Định lý Kleene!

<div class="textbook-epigraph" markdown="1">

"ε-moves stitch machines together — Kleene’s algebra becomes automata."

<span class="epigraph-attribution">— Thompson construction spirit</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** ε-NFA và bao đóng epsilon $$E(S)$$.
- **Chứng minh** các tính chất cơ bản của phép lấy bao đóng.
- **Tính** $$E(S)$$ bằng thuật toán DFS hoặc BFS trên các cạnh ε.

</div>

## Kiến thức cần nhớ: $$\varepsilon$$-NFA và Bao đóng Epsilon ($$\mathrm{ECLOSE}$$)

### 1. Chuyển trạng thái Rỗng ($$\varepsilon$$-transition)
- **Bản chất:** Mở rộng hàm chuyển lên $$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)$$. Một cung gắn nhãn $$\varepsilon$$ cho phép máy tự do "dịch chuyển tức thời" mà không tiêu thụ ký tự đầu vào nào.

### 2. Bao đóng Epsilon $$\mathrm{ECLOSE}(q)$$
- **Bản chất:** $$\mathrm{ECLOSE}(q)$$ là tập hợp **tất cả** các trạng thái có thể đi tới từ $$q$$ chỉ bằng **0, 1, 2, ... bước cung $$\varepsilon$$** (tính bằng DFS/BFS chỉ đi trên các cạnh $$\varepsilon$$!). Lưu ý: luôn có $$q \in \mathrm{ECLOSE}(q)$$ (0 bước)!

### 3. Quy tắc "Kẹp Bánh mì ECLOSE" cho $$\hat{\delta}$$
- **Bản chất:** Khởi đầu tại $$\mathrm{ECLOSE}(q_0)$$. Mỗi khi đọc 1 ký tự $$a$$ từ tập trạng thái $$S$$, ta đi theo mũi tên $$a$$ rồi **lập tức lấy $$\mathrm{ECLOSE}$$ lần nữa**:
  $$
  \hat{\delta}(S, a) = \mathrm{ECLOSE}\!\left(\bigcup_{p \in S} \delta(p, a)\right).
  $$

## Ví dụ tính tay làm từng bước: Tính $$\mathrm{ECLOSE}$$ và 1 bước chuyển trên $$\varepsilon$$-NFA 4 trạng thái

Xét $$\varepsilon$$-NFA có các cung: $$q_0 \xrightarrow{\varepsilon} q_1$$, $$q_1 \xrightarrow{\varepsilon} q_2$$, $$q_1 \xrightarrow{a} q_3$$, $$q_2 \xrightarrow{a} q_2$$, $$q_3 \xrightarrow{\varepsilon} q_2$$.
1. **Tính $$\mathrm{ECLOSE}$$ cho từng trạng thái:**
   - $$\mathrm{ECLOSE}(q_0) = \{q_0, q_1, q_2\}$$ (0 bước: $$q_0$$; 1 bước: $$q_1$$; 2 bước: $$q_2$$).
   - $$\mathrm{ECLOSE}(q_1) = \{q_1, q_2\}$$.
   - $$\mathrm{ECLOSE}(q_2) = \{q_2\}$$.
   - $$\mathrm{ECLOSE}(q_3) = \{q_3, q_2\}$$.
2. **Tính bước đọc ký tự `a` từ trạng thái khởi đầu $$q_0$$:**
   - Tập khởi đầu sau bao đóng: $$S_0 = \mathrm{ECLOSE}(q_0) = \{q_0, q_1, q_2\}$$.
   - Đi theo mũi tên `a` từ từng phần tử của $$S_0$$: $$\delta(q_0, a) = \emptyset,\; \delta(q_1, a) = \{q_3\},\; \delta(q_2, a) = \{q_2\} \implies$$ hợp lại là $$\{q_2, q_3\}$$.
   - Lấy $$\mathrm{ECLOSE}$$ một lần nữa: $$\mathrm{ECLOSE}(\{q_2, q_3\}) = \{q_2\} \cup \{q_2, q_3\} = \{q_2, q_3\}$$!

### Giải thích: 4 bước khử cung $$\varepsilon$$ an toàn
#### Bước 1: Tính sẵn bảng $$\mathrm{ECLOSE}(q)$$ cho mọi trạng thái $$q$$
Chỉ đi theo cung $$\varepsilon$$; nhớ rằng mọi trạng thái luôn chứa chính nó trong $$\mathrm{ECLOSE}$$.

#### Bước 2: Không bao giờ quên bước $$\mathrm{ECLOSE}$$ ở trạng thái khởi đầu $$q_0$$
Ngay cả chuỗi rỗng $$\varepsilon$$ cũng được chấp nhận nếu $$\mathrm{ECLOSE}(q_0) \cap F \neq \emptyset$$!

#### Bước 3: Chuyển đổi $$\varepsilon$$-NFA $$\to$$ NFA thường trong 1 công thức
Thay $$\delta'(q, a) = \mathrm{ECLOSE}(\delta(\mathrm{ECLOSE}(q), a))$$ và đặt $$F' = \{q : \mathrm{ECLOSE}(q) \cap F \neq \emptyset\}$$ — toàn bộ cung $$\varepsilon$$ biến mất sạch!

#### Bước 4: Vai trò cầu nối cho Định lý Kleene
Nhờ cung $$\varepsilon$$, ghép nối hai ô-tô-mát (Hợp, Nối tiếp, Sao Kleene) chỉ tốn 2 trạng thái mới và vài mũi tên $$\varepsilon$$ — tạo ra thuật toán Thompson thanh lịch ở bài 18.08!

$$
\varepsilon\text{-NFA}
\;\xrightarrow{\;\mathrm{ECLOSE}(q)\;}\;
\text{NFA thường}
\;\xrightarrow{\;\text{Subset Construction}\;}\;
\text{DFA tương đương}.
$$

## Định nghĩa

![Chuyển đổi NFA sang DFA bằng tập lũy thừa](/discrete-mathematics-for-computer-science-iuh/img/course/DFA-powerset-construction-example.svg)

![Bảng và đồ thị chuyển trạng thái](/discrete-mathematics-for-computer-science-iuh/img/course/state_transition.svg)

Trong ε-NFA, hàm chuyển được mở rộng để cho phép dịch chuyển mà không cần đọc ký hiệu đầu vào: $$\delta:Q\times(\Sigma\cup\{\varepsilon\})\to\mathcal{P}(Q)$$.

<div class="textbook-definition" markdown="1">

**Bao đóng epsilon** (*epsilon-closure*) $$E(S)$$ là tập tất cả các trạng thái có thể đi tới từ ít nhất một trạng thái trong $$S$$ chỉ bằng không hoặc nhiều bước chuyển ε (luôn bao gồm chính $$S$$).

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** Với mọi tập trạng thái $$S, T \subseteq Q$$, ta có $$E(E(S))=E(S)$$, $$S\subseteq E(S)$$, và nếu $$S\subseteq T$$ thì $$E(S)\subseteq E(T)$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Ba tính chất trên suy trực tiếp từ bản chất bao đóng phản xạ và bắc cầu của quan hệ “có đường đi chỉ gồm các cạnh ε”.

</div>

## Điều kiện chấp nhận

Khi đang ở tập trạng thái $$S$$ và đọc ký hiệu $$a \in \Sigma$$, tập trạng thái mới là $$S' = E\bigl(\bigcup_{q\in S}\delta(q,a)\bigr)$$. Máy bắt đầu từ tập trạng thái $$E(\{q_0\})$$ và chấp nhận chuỗi nếu tập trạng thái cuối cùng có giao khác rỗng với $$F$$.

## Thuật toán tính bao đóng

Để tính $$E(S)$$, ta dùng ngăn xếp (DFS) hoặc hàng đợi (BFS) khởi tạo từ $$S$$, chỉ duyệt dọc theo các cạnh ε và đánh dấu các trạng thái đã thăm. Độ phức tạp thời gian là $$O(\lvert Q\rvert+\lvert E_\varepsilon\rvert)$$.

### Minh họa tương tác

Quan sát hoạt động của ε-NFA và cách tính bao đóng ε ngay từ trạng thái khởi đầu:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="enfa" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh đầy đủ ba tính chất của phép toán $$E(S)$$ trong định lý trên.
2. Vẽ một ε-NFA nhận hợp của hai DFA bằng cách tạo một trạng thái khởi đầu mới nối bằng cạnh ε tới hai trạng thái khởi đầu cũ.
3. Giải thích trực giác vì sao bước chuyển ε không làm tăng sức mạnh biểu diễn của ô-tô-mát hữu hạn (chuẩn bị cho phép xây dựng tập con ở bài sau).

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman (phần khử chuyển ε).

## Tóm tắt

Bao đóng epsilon $$E(S)$$ cho phép định nghĩa chặt chẽ việc chấp nhận chuỗi trên ε-NFA và là công cụ thuận tiện để ghép nối các ô-tô-mát thành phần.

**Bài tiếp theo:** Xây dựng tập con (*subset construction*).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=84oNUttWlN4">Epsilon NFA</a> — Neso Academy, tiếng Anh. Giới thiệu bước chuyển ε và lý do cần khái niệm epsilon-closure.
- <a href="https://www.youtube.com/watch?v=WSGcmaHNBFM">Conversion of Epsilon NFA to NFA</a> — Neso Academy, tiếng Anh. Cách khử chuyển ε để thu được NFA thông thường.
- <a href="https://www.youtube.com/watch?v=I6GFKekMr7s">Conversion of Epsilon NFA to NFA - Examples (Part 1)</a> — Neso Academy, tiếng Anh. Ví dụ cụ thể về tính bao đóng và dựng lại bảng chuyển trạng thái.
