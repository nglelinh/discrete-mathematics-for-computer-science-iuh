---
layout: post
title: "Văn phạm Phi ngữ cảnh (CFG)"
categories: chapter19
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Định nghĩa văn phạm phi ngữ cảnh (CFG), dẫn xuất trái nhất, ví dụ chuỗi ngoặc cân bằng, biểu thức số học và chứng minh L(G)={aⁿbⁿ}."
---

<div class="textbook-epigraph" markdown="1">

"One nonterminal rewrite at a time — that is context-free."

<span class="epigraph-attribution">— CFG</span>

</div>

![CFG](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_cfg_parens.svg)

<p class="textbook-figure-caption" data-figure="19.3">Ngôn ngữ ngoặc cân bằng — ví dụ kinh điển của văn phạm phi ngữ cảnh.</p>

Mỗi khi bạn viết một biểu thức toán học `(3 + 5) * (2 - 1)` hay một khối lệnh `if (...) { if (...) { ... } }` trong C/Java/Python, dấu ngoặc có thể lồng sâu bao nhiêu tầng tùy ý. Biểu thức chính quy bất lực trước cấu trúc đệ quy này — và đó là lúc **văn phạm phi ngữ cảnh (Context-Free Grammar — CFG)** bước ra sân khấu. Tên gọi "phi ngữ cảnh" bắt nguồn từ quy tắc cực kỳ gọn: vế trái luôn chỉ là **một biến duy nhất** $$A \to \alpha$$, nghĩa là ta có thể thay thế $$A$$ mà không cần nhìn sang hàng xóm hai bên.

## Kiến thức cần nhớ: Ba trụ cột của Văn phạm Phi ngữ cảnh (CFG)

1. **Định nghĩa bộ bốn $$G = (V, \Sigma, R, S)$$**:
   Mọi luật sinh đều có dạng $$A \to \alpha$$ với $$A \in V$$ và $$\alpha \in (V \cup \Sigma)^*$$, cho phép mô tả đệ quy tự nhiên các cấu trúc lồng nhau (biểu thức số học, JSON, XML, cú pháp lập trình).
2. **Dẫn xuất trái nhất (Leftmost) và Phải nhất (Rightmost)**:
   Để tránh việc cùng một cấu trúc lại có nhiều thứ tự thay thế lộn xộn, trình biên dịch luôn cố định thứ tự mở rộng: bộ phân tích từ trên xuống (LL) bám theo dẫn xuất trái nhất, còn bộ phân tích từ dưới lên (LR) tái tạo ngược dẫn xuất phải nhất.
3. **Ký hiệu BNF (Backus–Naur Form)**:
   Chính là dạng viết kỹ thuật của CFG được dùng trong tài liệu đặc tả chính thức của hầu hết mọi ngôn ngữ lập trình hiện đại.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm phi ngữ cảnh (*Context-Free Grammar*, CFG).
- **Viết** dẫn xuất trái nhất (*leftmost derivation*) cho một chuỗi cho trước.
- **Chứng minh** $$L(G)=\{a^nb^n\}$$ đối với văn phạm chuẩn.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Văn phạm $$G=(V,\Sigma,P,S)$$ là **văn phạm phi ngữ cảnh (CFG)** nếu mọi luật sinh đều có dạng $$A\to\alpha$$, trong đó vế trái là đúng một ký hiệu không kết thúc $$A\in V$$ và vế phải $$\alpha\in(V\cup\Sigma)^*$$.

</div>

## Ví dụ

- Văn phạm ngoặc cân bằng: $$S\to(S)S\mid\varepsilon$$.
- Văn phạm $$S\to aSb\mid\varepsilon$$ sinh ra ngôn ngữ $$\{a^nb^n : n \ge 0\}$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Văn phạm $$G: S\to aSb\mid\varepsilon$$ sinh ra đúng ngôn ngữ $$L(G)=\{a^nb^n:n\ge 0\}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
Chiều ($$\subseteq$$): Quy nạp theo số bước dẫn xuất: mỗi lần áp dụng luật $$S\to aSb$$ đều thêm đồng thời một ký tự $$a$$ bên trái và một ký tự $$b$$ bên phải, sau cùng kết thúc bằng $$S\to\varepsilon$$.  
Chiều ($$\supseteq$$): Để sinh chuỗi $$a^nb^n$$ bất kỳ, áp dụng $$n$$ lần luật $$S\to aSb$$ rồi áp dụng một lần luật $$S\to\varepsilon$$.

</div>

### Giải thích: So sánh dẫn xuất trái nhất và phải nhất cho biểu thức `id + id * id`

Xét văn phạm biểu thức số học có thứ tự ưu tiên chuẩn (nhân chặt hơn cộng):
$$E \to E + T \mid T, \qquad T \to T * F \mid F, \qquad F \to (E) \mid \mathrm{id}.$$

**Dẫn xuất trái nhất (luôn thay biến ngoài cùng bên trái):**
1. $$E \Rightarrow_{\mathrm{lm}} E + T \Rightarrow_{\mathrm{lm}} T + T \Rightarrow_{\mathrm{lm}} F + T \Rightarrow_{\mathrm{lm}} \mathrm{id} + T$$
2. $$\Rightarrow_{\mathrm{lm}} \mathrm{id} + T * F \Rightarrow_{\mathrm{lm}} \mathrm{id} + F * F \Rightarrow_{\mathrm{lm}} \mathrm{id} + \mathrm{id} * F \Rightarrow_{\mathrm{lm}} \mathrm{id} + \mathrm{id} * \mathrm{id}.$$

**Dẫn xuất phải nhất (luôn thay biến ngoài cùng bên phải):**
1. $$E \Rightarrow_{\mathrm{rm}} E + T \Rightarrow_{\mathrm{rm}} E + T * F \Rightarrow_{\mathrm{rm}} E + T * \mathrm{id} \Rightarrow_{\mathrm{rm}} E + F * \mathrm{id}$$
2. $$\Rightarrow_{\mathrm{rm}} E + \mathrm{id} * \mathrm{id} \Rightarrow_{\mathrm{rm}} T + \mathrm{id} * \mathrm{id} \Rightarrow_{\mathrm{rm}} F + \mathrm{id} * \mathrm{id} \Rightarrow_{\mathrm{rm}} \mathrm{id} + \mathrm{id} * \mathrm{id}.$$

Cả hai cách viết trông khác thứ tự nhưng đều sinh ra **đúng một cây phân tích duy nhất**, trong đó `id * id` được gom nhóm trước khi cộng với `id` bên trái!

## Bài tập

1. Viết dẫn xuất cho chuỗi $$()(())$$ bằng văn phạm ngoặc cân bằng.
2. Xét văn phạm biểu thức $$E\to E+E\mid E*E\mid(E)\mid\mathrm{id}$$ và chỉ ra hiện tượng mơ hồ (*ambiguity*).
3. Giải thích vì sao ngôn ngữ $$\{a^nb^n\}$$ là phi ngữ cảnh nhưng không chính quy.

## Tài liệu đọc thêm

Sipser §2.1.

## Tóm tắt

Văn phạm phi ngữ cảnh cho phép viết lại độc lập từng ký hiệu không kết thúc, đủ sức biểu diễn các cấu trúc lồng nhau như ngoặc cân bằng và $$a^nb^n$$.

**Bài tiếp theo:** Cây phân tích và sự mơ hồ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. Giới thiệu văn phạm và ngôn ngữ phi ngữ cảnh.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Hướng dẫn dẫn xuất trái nhất và phải nhất từ các luật sinh.
- <a href="https://www.youtube.com/watch?v=htoFbcwES28">Method to find whether a String belongs to a Grammar or not</a> — Neso Academy, tiếng Anh. Cách kiểm tra một chuỗi có thuộc ngôn ngữ sinh bởi văn phạm hay không.
