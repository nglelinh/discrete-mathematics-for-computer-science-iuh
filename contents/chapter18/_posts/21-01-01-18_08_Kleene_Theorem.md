---
layout: post
title: "Định lý Kleene"
categories: chapter18
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Sự tương đương giữa biểu thức chính quy, ε-NFA, NFA và DFA; phép dựng Thompson và phương pháp loại bỏ trạng thái."
---

<div class="textbook-epigraph" markdown="1">

"Three notations, one class: regular languages."

<span class="epigraph-attribution">— Kleene’s theorem</span>

</div>

![Kleene](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_kleene_triangle.svg)

<p class="textbook-figure-caption" data-figure="18.5">Ba biểu diễn tương đương nhau của lớp ngôn ngữ chính quy.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** định lý Kleene.
- **Mô tả** phép dựng Thompson và phương pháp loại bỏ trạng thái (*state elimination*).
- **Trình bày** khung chứng minh tương đương theo hai chiều.

</div>

## Định lý Kleene

<div class="textbook-theorem" markdown="1">

**Định lý (Kleene).** Ba lớp ngôn ngữ sau trùng nhau hoàn toàn:  
(1) các ngôn ngữ $$L(r)$$ biểu diễn bởi biểu thức chính quy $$r$$;  
(2) các ngôn ngữ $$L(N)$$ chấp nhận bởi ε-NFA hoặc NFA;  
(3) các ngôn ngữ $$L(M)$$ chấp nhận bởi DFA.

</div>

## Chiều biểu thức chính quy → ε-NFA (Thompson)

Phép dựng Thompson thực hiện theo quy nạp cấu trúc của biểu thức $$r$$: xây dựng các mẫu ε-NFA cơ sở cho $$\emptyset, \varepsilon, a$$, sau đó ghép nối chúng cho các phép toán hợp, nối và sao bằng các cạnh chuyển ε. Số trạng thái sinh ra thuộc $$O(\lvert r\rvert)$$.

**Tính đúng đắn:** chứng minh bằng quy nạp cấu trúc rằng $$L(N_r)=L(r)$$.

### Thử nghiệm: Thompson từng khối

Quan sát quá trình dựng ε-NFA theo từng khối từ biểu thức chính quy:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="thompson"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Chiều NFA → DFA

Thực hiện bằng phép xây dựng tập con (*subset construction*) đã trình bày ở Bài 18.5.

## Chiều DFA → biểu thức chính quy

Ta sử dụng phương pháp loại bỏ trạng thái (*state elimination*) hoặc giải hệ phương trình ngôn ngữ bằng bổ đề Arden: phương trình $$X=A X+B$$ có nghiệm $$X=A^*B$$ (khi $$\varepsilon\notin L(A)$$, hoặc cần xử lý cẩn thận trường hợp chứa $$\varepsilon$$).

### Thử nghiệm: loại trạng thái để thu biểu thức chính quy

Thêm trạng thái đầu $$S$$ và trạng thái cuối $$F$$ mới rồi loại dần từng trạng thái trung gian; bạn có thể thử hai thứ tự loại khác nhau để thấy biểu thức chính quy thu được khác dạng nhưng vẫn tương đương về ngôn ngữ:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="eliminate" data-preset="dfa01"></div>
</div>

## Bài tập

1. Áp dụng phép dựng Thompson cho biểu thức $$(0+1)^*01$$.
2. Chọn một DFA gồm 2 trạng thái và chuyển sang biểu thức chính quy bằng phương pháp loại bỏ trạng thái.
3. Đọc và đối chiếu phát biểu chính thức của bổ đề Arden.

## Tài liệu đọc thêm

Sipser; Kozen; Hopcroft–Ullman.

## Tóm tắt

Định lý Kleene khép kín vòng tròn tương đương giữa biểu thức chính quy, NFA và DFA thông qua phép dựng Thompson, xây dựng tập con và loại bỏ trạng thái.

**Bài tiếp theo:** Bổ đề bơm (*pumping lemma*) cho ngôn ngữ chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=OKFrju0HB7k">NFA to Regular Expression Conversion</a> — Neso Academy, tiếng Anh. Minh họa một chiều của định lý Kleene: chuyển NFA sang biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=SmT1DXLl3f4">DFA to Regular Expression Conversion</a> — Neso Academy, tiếng Anh. Chuyển đổi từ DFA sang biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=RxfXyvfTsgQ">Conversion of Regular Expression to Finite Automata</a> — Neso Academy, tiếng Anh. Chiều ngược lại: chuyển biểu thức chính quy sang ô-tô-mát hữu hạn.
