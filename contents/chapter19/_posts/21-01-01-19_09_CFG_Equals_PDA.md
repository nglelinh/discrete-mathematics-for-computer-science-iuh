---
layout: post
title: "Văn phạm phi ngữ cảnh ≡ PDA"
categories: chapter19
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Phép chuyển đổi hai chiều giữa văn phạm phi ngữ cảnh (CFG) và ô-tô-mát đẩy xuống (PDA), cùng khung chứng minh L(G)=L(P)."
---

<div class="textbook-epigraph" markdown="1">

"CFGs and PDAs define the same languages."

<span class="epigraph-attribution">— Fundamental theorem of CFLs</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Mô tả** hai phép dựng chuyển đổi qua lại giữa CFG và PDA.
- **Trình bày** khung chứng minh sự tương đương $$L(G)=L(P)$$.

</div>

## Chiều CFG → PDA

Ý tưởng là dùng PDA mô phỏng một dẫn xuất trái nhất của văn phạm: ngăn xếp lưu giữ dạng câu (*sentential form*) đang dẫn xuất; khi đỉnh ngăn xếp là ký hiệu không kết thúc, máy đoán không đơn định một luật sinh để thay thế; khi đỉnh ngăn xếp là ký hiệu kết thúc, máy khớp trực tiếp với ký tự tiếp theo của chuỗi đầu vào.

### Thử nghiệm: PDA mô phỏng dẫn xuất của CFG

Quan sát ngăn xếp thay thế biến bằng vế phải của luật sinh và khớp ký hiệu kết thúc với chuỗi đầu vào:

<div class="interactive-demo" markdown="1">
<div data-demo="cfgpda-explainer" data-preset="paren"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Chiều PDA → CFG

Ta đưa vào các ký hiệu không kết thúc dạng $$A_{pq}$$ đại diện cho mọi chuỗi làm máy đi từ trạng thái $$p$$ đến trạng thái $$q$$ với ngăn xếp ban đầu và kết thúc cùng rỗng (độ cao ròng bằng 0). Các luật sinh được xây dựng tương ứng theo từng cặp thao tác đẩy–lấy trên ngăn xếp của PDA (xem Sipser).

<div class="textbook-theorem" markdown="1">

**Định lý.** Một ngôn ngữ $$L$$ là ngôn ngữ phi ngữ cảnh (CFL) khi và chỉ khi tồn tại một PDA $$P$$ sao cho $$L=L(P)$$.

</div>

## Bài tập

1. Xây dựng PDA tương ứng với văn phạm $$S\to aSb\mid\varepsilon$$.
2. Đọc chứng minh đầy đủ cho một trong hai chiều trong giáo trình Sipser.
3. Tìm hiểu vì sao lớp ngôn ngữ phi ngữ cảnh đơn định (DCFL) là tập con thực sự của CFL.

## Tài liệu đọc thêm

Sipser §2.2; Hopcroft §6.

## Tóm tắt

Hai phép dựng hai chiều khẳng định văn phạm phi ngữ cảnh và ô-tô-mát đẩy xuống định nghĩa chính xác cùng một lớp ngôn ngữ (CFL).

**Bài tiếp theo:** Bổ đề bơm cho ngôn ngữ phi ngữ cảnh.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=FjGrU7vczyg">Equivalence of CFG and PDA (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu một chiều trong chứng minh tương đương giữa CFG và PDA.
- <a href="https://www.youtube.com/watch?v=kyvLetfjOhc">Equivalence of CFG and PDA (Part 2a)</a> — Neso Academy, tiếng Anh. Tiếp tục phép chuyển đổi giữa văn phạm và ô-tô-mát đẩy xuống.
- <a href="https://www.youtube.com/watch?v=DjbukiTf-48">Equivalence of CFG and PDA (Part 2b)</a> — Neso Academy, tiếng Anh. Hoàn thiện phần còn lại của chứng minh tương đương.
