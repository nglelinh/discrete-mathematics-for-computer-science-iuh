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
