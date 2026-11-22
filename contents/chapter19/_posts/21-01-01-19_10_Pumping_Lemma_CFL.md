---
layout: post
title: "Bổ đề Bơm CFL"
categories: chapter19
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "Phát biểu bổ đề bơm cho ngôn ngữ phi ngữ cảnh (CFL), ý tưởng chứng minh từ cây phân tích và ứng dụng chứng minh {aⁿbⁿcⁿ} không phải CFL."
---

<div class="textbook-epigraph" markdown="1">

"Long parse trees repeat a nonterminal on a root-to-leaf path."

<span class="epigraph-attribution">— CFL pumping</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** bổ đề bơm cho ngôn ngữ phi ngữ cảnh (CFL).
- **Chứng minh** ngôn ngữ $$\{a^nb^nc^n\}$$ không phải là ngôn ngữ phi ngữ cảnh.
- **Nắm vững** quy trình lập luận phản chứng khi áp dụng bổ đề bơm CFL.

</div>

## Phát biểu định lý

<div class="textbook-theorem" markdown="1">

**Bổ đề bơm cho CFL.** Nếu $$L$$ là một ngôn ngữ phi ngữ cảnh thì tồn tại hằng số bơm $$p \ge 1$$ sao cho mọi chuỗi $$w\in L$$ có $$\lvert w\rvert\ge p$$ đều phân tích được thành $$w=uvxyz$$ thỏa mãn ba điều kiện:  
(1) $$uv^kxy^kz\in L$$ với mọi $$k\ge 0$$;  
(2) $$\lvert vy\rvert\ge 1$$;  
(3) $$\lvert vxy\rvert\le p$$.

</div>

**Ý tưởng chứng minh.** Đưa văn phạm về dạng chuẩn Chomsky (CNF); khi chuỗi đủ dài, cây phân tích có chiều cao lớn nên trên một đường đi từ gốc xuống lá chắc chắn có một ký hiệu không kết thúc lặp lại, cho phép lặp lại hoặc rút gọn cây con tương ứng với cặp đoạn $$v$$ và $$y$$. $$\square$$

### Thử nghiệm: bổ đề bơm cho CFL

Duyệt mọi cách chia $$w = uvxyz$$ thỏa mãn $$\lvert vxy\rvert \le p$$ và $$\lvert vy\rvert \ge 1$$ để kiểm tra khả năng bơm:

<div class="interactive-demo" markdown="1">
<div data-demo="pumping-explainer" data-kind="cfl" data-lang="anbncn" data-p="2"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Ứng dụng

<div class="textbook-theorem" markdown="1">

**Định lý.** Ngôn ngữ $$L=\{a^nb^nc^n:n\ge 0\}$$ không phải là ngôn ngữ phi ngữ cảnh.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử phản chứng $$L$$ là CFL với hằng số bơm $$p$$, và xét chuỗi $$w=a^pb^pc^p \in L$$. Vì đoạn $$vxy$$ có độ dài không vượt quá $$p$$, nó không thể đồng thời chứa cả ba ký tự $$a, b, c$$. Do đó khi bơm với $$k=2$$ (hoặc $$k=0$$), số lượng của ít nhất một trong ba ký tự sẽ thay đổi không đồng đều với các ký tự còn lại, phá vỡ điều kiện cân bằng ba nhóm (chi tiết phân tích từng trường hợp xem trong Sipser).

</div>

## Bài tập

1. Chứng minh ngôn ngữ $$\{ww : w \in \{a,b\}^*\}$$ không phải là ngôn ngữ phi ngữ cảnh.
2. So sánh bổ đề bơm cho ngôn ngữ chính quy (bơm một đoạn $$y$$) với bổ đề bơm cho CFL (bơm đồng thời hai đoạn $$v$$ và $$y$$).
3. Tìm hiểu định hướng mở rộng sang bổ đề Ogden (*Ogden’s lemma*).

## Tài liệu đọc thêm

Sipser §2.3.

## Tóm tắt

Bổ đề bơm CFL dựa trên sự lặp lại ký hiệu không kết thúc trên đường đi của cây phân tích, giúp bác bỏ tính phi ngữ cảnh của những ngôn ngữ như $$\{a^nb^nc^n\}$$.

**Bài tiếp theo:** Tính đóng của CFL, dạng chuẩn Chomsky (CNF) và thuật toán CYK.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=jRhqx1_KcCk">Pumping Lemma (For Context Free Languages)</a> — Neso Academy, tiếng Anh. Giới thiệu phát biểu và ý nghĩa của bổ đề bơm cho ngôn ngữ phi ngữ cảnh.
- <a href="https://www.youtube.com/watch?v=eQ0XkUk3qGk">Pumping Lemma (For Context Free Languages) - Examples (Part 1)</a> — Neso Academy, tiếng Anh. Ví dụ chứng minh một ngôn ngữ không phải là CFL.
- <a href="https://www.youtube.com/watch?v=DPs8sBcIjs8">Pumping Lemma (For Context Free Languages) - Examples (Part 2)</a> — Neso Academy, tiếng Anh. Ví dụ bổ sung giúp luyện kỹ năng chọn chuỗi và phân chia các đoạn $$uvxyz$$.
