---
layout: post
title: "Thiết kế DFA và Chứng minh Tính đúng"
categories: chapter18
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Phương pháp thiết kế DFA theo bất biến trạng thái, ví dụ kết thúc bằng 01 và chẵn số 1, cùng cách chứng minh L(M)=L theo hai chiều."
---

> **Câu chuyện mở đầu:** Vẽ đại một sơ đồ DFA rồi thử vài chuỗi thấy chạy đúng là thói quen rất dễ dính lỗi biên! Bí quyết thiết kế DFA chuẩn của các kỹ sư trình biên dịch cực kỳ khoa học: **đừng vẽ mũi tên trước — hãy định nghĩa Ý NGHĨA (bất biến) cho từng trạng thái trước**, rồi các mũi tên chuyển trạng thái sẽ tự động hiện ra duy nhất, kèm sẵn chứng minh tính đúng bằng quy nạp!

<div class="textbook-epigraph" markdown="1">

"A correct automaton is a theorem: states are invariants."

<span class="epigraph-attribution">— Design by invariant</span>

</div>

Thiết kế một DFA đúng bản chất là chọn **bất biến** rõ ràng cho từng trạng thái, sau đó chứng minh đẳng thức ngôn ngữ $$L(M)=L$$ theo cả hai chiều.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Thiết kế** DFA theo phương pháp bất biến trạng thái (*invariant*).
- **Chứng minh** tính đúng đắn hai chiều: $$L(M)\subseteq L$$ và $$L\subseteq L(M)$$.

</div>

## Bản đồ kiến thức nền: Nghệ thuật Thiết kế DFA & Chứng minh Tính đúng

### 1. Tư duy "Trạng thái = Tóm tắt Tối thiểu của Quá khứ"
- **Bản chất:** Khi đang đọc dở một chuỗi, bạn cần nhớ **đúng thông tin gì** để quyết định số phận của chuỗi về sau? Mỗi khả năng của thông tin cần nhớ ấy chính là **1 trạng thái** của DFA!

### 2. Bốn Mẫu Thiết kế DFA Kinh điển
- **Đếm theo modulo $$k$$:** Dùng $$k$$ trạng thái $$q_0, \dots, q_{k-1}$$ lưu số dư hiện tại.
- **Nhận chuỗi con / hậu tố cố định:** Trạng thái $$q_i$$ nghĩa là *"đã khớp đúng $$i$$ ký tự đầu của mẫu"* (nền tảng của thuật toán tìm chuỗi KMP!).
- **Trạng thái bẫy (Dead / Trap state):** Khi chuỗi đã vi phạm điều kiện vĩnh viễn, đẩy vào trạng thái bẫy tự lặp mãi mãi.
- **Kết hợp điều kiện (Ô-tô-mát tích):** Muốn thỏa đồng thời 2 điều kiện (ví dụ chẵn `0` VÀ lẻ `1`), dùng cặp trạng thái $$(p, q) \in Q_1 \times Q_2$$!

### 3. Chứng minh Tính đúng bằng Quy nạp theo Độ dài Chuỗi $$\lvert w\rvert$$
- **Bản chất:** Phát biểu mệnh đề bất biến $$P(w)$$: *"$$\hat{\delta}(q_0, w) = q_i \iff w$$ thỏa tính chất $$i$$"*, rồi chứng minh cơ sở $$\lvert w\rvert = 0$$ và bước quy nạp $$w \to wa$$!

## Ví dụ tính tay cầm tay chỉ việc: Thiết kế DFA nhận số nhị phân chia hết cho 3

Xây dựng DFA trên $$\Sigma = \{0, 1\}$$ nhận mọi chuỗi nhị phân có giá trị thập phân chia hết cho $$3$$:
1. **Định nghĩa ý nghĩa 3 trạng thái:** $$q_r$$ ($$r \in \{0, 1, 2\}$$) nghĩa là *"giá trị số của chuỗi đã đọc tới hiện tại chia 3 dư $$r$$"*. Trạng thái đầu $$q_0$$, trạng thái chấp nhận $$F = \{q_0\}$$.
2. **Suy ra hàm chuyển từ toán học sơ cấp:** Nếu chuỗi $$w$$ có giá trị $$N$$ (chia 3 dư $$r$$), khi đọc thêm bit $$b \in \{0, 1\}$$ ở bên phải, giá trị mới là $$2N + b$$, nên số dư mới là:
   $$
   \delta(q_r, b) = q_{(2r + b) \bmod 3}!
   $$
   Lập ngay bảng chuyển bằng tay:
   - Từ $$q_0$$: đọc `0` $$\to q_0$$, đọc `1` $$\to q_1$$.
   - Từ $$q_1$$: đọc `0` $$\to q_2$$ ($$2\cdot 1+0=2$$), đọc `1` $$\to q_0$$ ($$2\cdot 1+1=3\equiv 0$$).
   - Từ $$q_2$$: đọc `0` $$\to q_1$$ ($$2\cdot 2+0=4\equiv 1$$), đọc `1` $$\to q_2$$ ($$2\cdot 2+1=5\equiv 2$$).
3. **Kiểm tra trên `110` (số 6) và `101` (số 5):**
   - `110`: $$q_0 \xrightarrow{1} q_1 \xrightarrow{1} q_0 \xrightarrow{0} q_0 \in F$$ (6 chia hết cho 3!). ✓
   - `101`: $$q_0 \xrightarrow{1} q_1 \xrightarrow{0} q_2 \xrightarrow{1} q_2 \notin F$$ (5 chia 3 dư 2!). ✓

### Khung giải thích: Quy trình 4 bước thiết kế DFA chuẩn không lỗi (nên đọc chậm)

#### Bước 1: Xác định thông tin tối thiểu cần lưu (Đặt tên trạng thái rõ nghĩa)
Viết ra câu mô tả bằng lời cho từng trạng thái $$q_i$$ (như "dư 0, dư 1, dư 2" hay "đã khớp 0, 1, 2 ký tự").

#### Bước 2: Điền đầy đủ mọi mũi tên chuyển trạng thái
Kiểm tra từng cặp $$(q_i, a)$$ xem đọc thêm $$a$$ thì chuỗi mới rơi vào đúng phân loại trạng thái nào (nhớ cẩn thận trường hợp "lùi về hậu tố khớp dài nhất" khi tìm mẫu!).

#### Bước 3: Kiểm tra biên (chuỗi rỗng $$\varepsilon$$, độ dài 1, trạng thái bẫy)
Xem $$\varepsilon$$ có thuộc ngôn ngữ không để quyết định $$q_0 \in F$$ hay $$q_0 \notin F$$.

#### Bước 4: Chứng minh tính đúng bằng quy nạp theo $$\lvert w\rvert$$
Bước quy nạp chỉ cần kiểm tra đúng bảng chuyển $$\delta$$ khớp với định nghĩa trạng thái ở Bước 1!

$$
\text{Ngôn ngữ }L
\;\xrightarrow{\;\text{Phân loại trạng thái}\;}\;
\text{Bảng chuyển }\delta
\;\xrightarrow{\;\text{Quy nạp theo }\lvert w\rvert\;}\;
\text{DFA đúng 100\%}.
$$

## Quy trình thiết kế

1. Phát biểu rõ tính chất xác định ngôn ngữ $$L\subseteq\Sigma^*$$.
2. Phân lớp các tiền tố theo lượng “thông tin tối thiểu cần nhớ” (số lớp phải hữu hạn).
3. Gán mỗi lớp cho một trạng thái và xây dựng hàm chuyển $$\delta$$ sao cho bất biến được bảo toàn sau mỗi ký hiệu.
4. Chọn tập trạng thái kết thúc $$F$$ gồm các lớp thỏa mãn điều kiện thuộc $$L$$.
5. Chứng minh bất biến bằng quy nạp và suy ra $$L(M)=L$$.

## Ví dụ: chuỗi kết thúc bằng $$01$$

Ta dùng các trạng thái $$q_\varepsilon, q_0, q_{01}$$ (và trạng thái bẫy từ chối nếu cần cho bài toán khác). Bất biến của mỗi trạng thái là độ dài hậu tố dài nhất vừa đọc khớp với một tiền tố của $$01$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** DFA xây dựng theo bất biến trên chấp nhận đúng ngôn ngữ $$L=\{w:w\text{ kết thúc bằng }01\}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh (phác thảo).**  
Chiều ($$\Rightarrow$$): Theo bất biến trạng thái, máy ở trạng thái $$q_{01}$$ khi và chỉ khi chuỗi vừa đọc kết thúc bằng $$01$$.  
Chiều ($$\Leftarrow$$): Mọi chuỗi $$w\in L$$ đều buộc đường chạy kết thúc tại $$q_{01} \in F$$. Chi tiết bất biến được chứng minh bằng quy nạp theo độ dài chuỗi.

</div>

## Ví dụ: chuỗi có số bit $$1$$ chẵn

Ta chỉ cần hai trạng thái: $$q_0$$ (đã đọc số chẵn bit $$1$$) và $$q_1$$ (đã đọc số lẻ bit $$1$$), với $$F=\{q_0\}$$.

**Bất biến:** $$\hat\delta(q_0,w)=q_0\Leftrightarrow\#_1(w)$$ là số chẵn — có thể kiểm chứng trực tiếp bằng quy nạp theo độ dài chuỗi $$w$$.

### Minh họa tương tác

Thử nghiệm DFA nhận chuỗi có số bit 1 chẵn với nhiều chuỗi đầu vào khác nhau để kiểm chứng tính đúng đắn:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="even1" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Thiết kế DFA nhận các chuỗi “chứa chuỗi con $$aa$$” và chứng minh tính đúng đắn.
2. Thiết kế DFA nhận các chuỗi có “độ dài $$\equiv 0\pmod 3$$”.
3. Giải thích vì sao DFA không cần cơ chế “đoán”, và chuẩn bị đối chiếu với NFA ở bài tiếp theo.

## Tài liệu đọc thêm

Sipser, bài tập 1.1–1.6; Hopcroft–Ullman (các ví dụ thiết kế DFA).

## Tóm tắt

Mỗi trạng thái của DFA đại diện cho một bất biến hữu hạn; tính đúng đắn của thiết kế được chứng minh bằng đẳng thức hai chiều $$L(M)=L$$.

**Bài tiếp theo:** Ô-tô-mát hữu hạn không đơn định (NFA).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=40i4PKpM0cI">Deterministic Finite Automata (Example 1)</a> — Neso Academy, tiếng Anh. Minh họa quy trình thiết kế DFA cho một ngôn ngữ cụ thể.
- <a href="https://www.youtube.com/watch?v=2KindKcLjos">Deterministic Finite Automata (Example 2)</a> — Neso Academy, tiếng Anh. Ví dụ bổ sung giúp rèn luyện cách chọn trạng thái lưu đúng thông tin cần thiết.
- <a href="https://www.youtube.com/watch?v=_2cKtLkdwnc">Deterministic Finite Automata (Example 3)</a> — Neso Academy, tiếng Anh. Ví dụ phức tạp hơn, chỉ rõ vì sao thiếu trạng thái sẽ làm sai ngôn ngữ chấp nhận.
