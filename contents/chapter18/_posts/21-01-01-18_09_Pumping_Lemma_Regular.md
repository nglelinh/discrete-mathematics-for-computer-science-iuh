---
layout: post
title: "Bổ đề Bơm cho Ngôn ngữ Chính quy"
categories: chapter18
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Phát biểu và chứng minh bổ đề bơm từ DFA, ứng dụng chứng minh {0ⁿ1ⁿ} không chính quy và quy trình phản chứng."
---

<div class="textbook-epigraph" markdown="1">

"If it is regular, long enough strings pump — use that to kill candidates."

<span class="epigraph-attribution">— Pumping lemma</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** và **chứng minh** bổ đề bơm (*pumping lemma*) cho ngôn ngữ chính quy.
- **Chứng minh** ngôn ngữ $$\{0^n1^n\}$$ không chính quy.
- **Áp dụng** quy trình phản chứng chuẩn để bác bỏ tính chính quy của một ngôn ngữ.

</div>

## Phát biểu và chứng minh

<div class="textbook-theorem" markdown="1">

**Bổ đề bơm (cho ngôn ngữ chính quy).** Nếu $$L$$ là ngôn ngữ chính quy thì tồn tại hằng số bơm $$p\ge 1$$ sao cho mọi chuỗi $$w\in L$$ có độ dài $$\lvert w\rvert\ge p$$ đều phân tích được thành $$w=xyz$$ thỏa mãn đồng thời ba điều kiện:  
(1) $$xy^kz\in L$$ với mọi $$k\ge 0$$;  
(2) $$\lvert y\rvert\ge 1$$;  
(3) $$\lvert xy\rvert\le p$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử $$L$$ được chấp nhận bởi một DFA có $$p=\lvert Q\rvert$$ trạng thái. Xét chuỗi $$w=a_1\ldots a_n \in L$$ với $$n\ge p$$. Dãy $$p+1$$ trạng thái đầu tiên khi đọc tiền tố độ dài $$p$$ chắc chắn có ít nhất một trạng thái lặp lại theo nguyên lý Dirichlet: $$q_i=q_j$$ với $$0\le i<j\le p$$. Đặt $$x$$ là phần chuỗi đến $$q_i$$, $$y$$ là phần từ $$q_i$$ đến $$q_j$$ (tạo thành một vòng lặp khác rỗng) và $$z$$ là phần còn lại. Việc lặp vòng $$y$$ với số lần $$k \ge 0$$ bất kỳ đều giữ nguyên trạng thái kết thúc, nên $$xy^kz \in L$$.

</div>

### Thử nghiệm: trò chơi bổ đề bơm (ngôn ngữ chính quy)

Chọn hằng số $$p$$ và duyệt mọi cách phân tích $$w = xyz$$; nếu với mọi cách chia hợp lệ đều tồn tại giá trị $$k$$ phá vỡ điều kiện thuộc $$L$$ thì $$L$$ không chính quy:

<div class="interactive-demo" markdown="1">
<div data-demo="pumping-explainer" data-kind="regular" data-lang="anbn"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Ứng dụng

<div class="textbook-theorem" markdown="1">

**Định lý.** Ngôn ngữ $$L=\{0^n1^n:n\ge 0\}$$ không phải là ngôn ngữ chính quy.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử phản chứng rằng $$L$$ chính quy với hằng số bơm $$p$$. Chọn chuỗi $$w=0^p1^p \in L$$ (có $$\lvert w\rvert = 2p \ge p$$). Với mọi phân tích $$w=xyz$$ thỏa mãn $$\lvert xy\rvert\le p$$ và $$\lvert y\rvert\ge 1$$, phần $$y$$ chỉ chứa ký tự $$0$$, tức $$y=0^{t}$$ với $$t\ge 1$$. Khi chọn $$k=2$$, ta được $$xy^2z = 0^{p+t}1^p\notin L$$ — mâu thuẫn. Vậy $$L$$ không chính quy.

</div>

## Quy trình phản chứng chuẩn

1. Giả sử $$L$$ chính quy và tồn tại hằng số bơm $$p$$.
2. Chọn một chuỗi $$w \in L$$ phụ thuộc vào $$p$$ sao cho $$\lvert w\rvert \ge p$$.
3. Xét **mọi** phân tích $$w=xyz$$ thỏa mãn $$\lvert xy\rvert \le p$$ và $$\lvert y\rvert \ge 1$$.
4. Chỉ ra ít nhất một giá trị $$k \ge 0$$ khiến $$xy^kz \notin L$$ để rút ra mâu thuẫn.

## Bài tập

1. Chứng minh ngôn ngữ $$\{ww\}$$ không chính quy.
2. Xét ngôn ngữ $$\{0^{n!}\}$$ — hãy thử áp dụng bổ đề bơm và so sánh với cách dùng định lý Myhill–Nerode.
3. Thảo luận vì sao bổ đề bơm chỉ là điều kiện **cần** chứ không phải điều kiện đủ để một ngôn ngữ là chính quy (tham khảo Sipser).

## Tài liệu đọc thêm

Sipser §1.4; Hopcroft–Ullman.

## Tóm tắt

Bổ đề bơm xuất phát từ sự tồn tại của chu trình trạng thái trong DFA và cung cấp khuôn mẫu phản chứng chuẩn để bác bỏ tính chính quy của ngôn ngữ.

**Bài tiếp theo:** Tính đóng của ngôn ngữ chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dikEDuepOtI">Pumping Lemma (For Regular Languages)</a> — Neso Academy, tiếng Anh. Giới thiệu bổ đề bơm cho ngôn ngữ chính quy.
- <a href="https://www.youtube.com/watch?v=Ty9tpikilAo">Pumping Lemma (For Regular Languages) | Example 1</a> — Neso Academy, tiếng Anh. Ví dụ chứng minh một ngôn ngữ không chính quy bằng bổ đề bơm.
- <a href="https://www.youtube.com/watch?v=kZzH8E-s-9o">Pumping Lemma (For Regular Languages) | Example 2</a> — Neso Academy, tiếng Anh. Ví dụ thứ hai giúp luyện cách chọn chuỗi và xét mọi phân tích $$xyz$$.
