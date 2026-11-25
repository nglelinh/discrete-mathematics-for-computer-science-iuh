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

Làm thế nào để khẳng định chắc chắn rằng *không một ai trên thế giới* có thể viết ra một văn phạm phi ngữ cảnh cho ngôn ngữ $$L = \{a^n b^n c^n \mid n \ge 0\}$$? Ta không thể thử vô hạn văn phạm. Giống như Bổ đề Bơm cho ngôn ngữ chính quy khai thác chu trình trên đồ thị DFA, **Bổ đề Bơm cho CFL** khai thác nguyên lý Dirichlet trên **chiều cao của cây phân tích**: khi chuỗi đủ dài, một biến $$A$$ bắt buộc phải lặp lại trên cùng một đường đi từ gốc xuống lá, tạo ra hai đoạn bơm đối xứng $$v$$ và $$y$$.

## Kiến thức cần nhớ: Ba trụ cột của Bổ đề Bơm CFL

1. **Nguyên lý Dirichlet trên Cây phân tích (Phiên bản CNF)**:
   Nếu văn phạm ở dạng chuẩn Chomsky có $$\vert V \vert$$ biến, mọi cây phân tích có chiều cao $$\le \vert V \vert$$ chỉ sinh tối đa $$2^{\vert V \vert - 1}$$ lá. Vậy mọi chuỗi dài $$p = 2^{\vert V \vert}$$ trở lên bắt buộc có đường đi chứa một biến $$A$$ lặp lại ít nhất 2 lần.
2. **Tách năm phần $$s = uvxyz$$ với ba điều kiện vàng**:
   (1) $$\vert vy \vert \ge 1$$ (ít nhất một trong hai đoạn bơm khác rỗng), (2) $$\vert vxy \vert \le p$$ (cửa sổ bơm bị giới hạn chiều dài), và (3) $$u v^i x y^i z \in L$$ với mọi $$i \ge 0$$ (kể cả bơm xuống $$i = 0$$!).
3. **Cấu trúc trò chơi đối kháng (Adversary Game)**:
   Đối thủ chọn hằng số $$p$$ → Ta chọn chuỗi $$s \in L$$ phụ thuộc $$p$$ → Đối thủ chọn cách chia $$uvxyz$$ hợp lệ → Ta chỉ ra một giá trị $$i$$ (thường là $$i=0$$ hoặc $$i=2$$) làm $$u v^i x y^i z \notin L$$.

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

### Giải thích: Chứng minh từng bước $$L = \{a^n b^n c^n \mid n \ge 0\}$$ không phải CFL

Giả sử phản chứng $$L$$ là CFL với độ dài bơm $$p \ge 1$$. Ta chọn chuỗi thử cực sắc bén:
$$s = a^p b^p c^p \in L \qquad (\vert s \vert = 3p \ge p).$$

Theo Bổ đề Bơm, đối thủ chia $$s = uvxyz$$ với $$\vert vxy \vert \le p$$ và $$\vert vy \vert \ge 1$$.
- **Nhận xét then chốt từ $$\vert vxy \vert \le p$$:** Vì khối $$b^p$$ ở giữa dài đúng $$p$$, cửa sổ $$vxy$$ dài tối đa $$p$$ **không thể chạm đồng thời vào cả `a` lẫn `c`**! Do đó $$vxy$$ chứa tối đa **2 loại ký tự** (chỉ `a` và `b`, hoặc chỉ `b` và `c`, hoặc chỉ 1 loại).
- **Bơm lên với $$i = 2$$** để tạo chuỗi $$s' = u v^2 x y^2 z$$:
  - Vì $$\vert vy \vert \ge 1$$, số lượng của ít nhất 1 loại ký tự tăng thêm chặt ($$> p$$).
  - Vì $$vxy$$ thiếu ít nhất 1 loại ký tự (hoặc `a` hoặc `c`), loại ký tự bị bỏ sót đó vẫn giữ nguyên số lượng là $$p$$.
  - Suy ra trong $$s'$$, số lượng `a`, `b`, `c` **không thể bằng nhau cả ba** $$\implies s' \notin L$$!

Mâu thuẫn hoàn toàn với Bổ đề Bơm — vậy $$a^n b^n c^n$$ chắc chắn nằm ngoài lớp CFL!

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
