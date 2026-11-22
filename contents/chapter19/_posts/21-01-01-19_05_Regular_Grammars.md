---
layout: post
title: "Văn phạm Chính quy ≡ Ngôn ngữ Chính quy"
categories: chapter19
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Văn phạm tuyến tính phải (right-linear grammar), chứng minh sự tương đương với NFA và kết nối trực tiếp với Chương 18."
---

<div class="textbook-epigraph" markdown="1">

"Right-linear rules are finite automata in disguise."

<span class="epigraph-attribution">— Grammar–automaton bridge</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm tuyến tính phải (*right-linear*) và tuyến tính trái (*left-linear*).
- **Trình bày** khung chứng minh sự tương đương giữa văn phạm chính quy và NFA.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Một văn phạm được gọi là **tuyến tính phải** (*right-linear*) nếu mọi luật sinh đều có dạng $$A\to wB$$ hoặc $$A\to w$$ với $$w\in\Sigma^*$$ (sau khi chuẩn hóa, ta thường đưa $$w$$ về một ký hiệu đơn hoặc chuỗi rỗng).

</div>

## Định lý tương đương

<div class="textbook-theorem" markdown="1">

**Định lý.** Ngôn ngữ $$L$$ là ngôn ngữ chính quy khi và chỉ khi tồn tại một văn phạm tuyến tính phải $$G$$ sao cho $$L=L(G)$$.

</div>

**Ý tưởng chứng minh.**  
Chiều từ văn phạm sang NFA: xem mỗi ký hiệu không kết thúc là một trạng thái; luật sinh $$A\to aB$$ tương ứng với cạnh chuyển từ $$A$$ sang $$B$$ mang nhãn $$a$$, còn luật $$A\to a$$ đi tới trạng thái kết thúc mới.  
Chiều từ NFA sang văn phạm: thực hiện phép biến đổi ngược lại từ tập trạng thái và cạnh chuyển sang tập luật sinh. $$\square$$

## Bài tập

1. Xây dựng văn phạm tuyến tính phải tương ứng với DFA kiểm tra tính chẵn lẻ số bit 1.
2. Viết chứng minh chi tiết cho một trong hai chiều của định lý trên.
3. Giải thích vì sao văn phạm tuyến tính trái (*left-linear*) cũng sinh ra đúng lớp ngôn ngữ chính quy.

## Tài liệu đọc thêm

Hopcroft–Ullman; Sipser (phần bài tập).

## Tóm tắt

Văn phạm loại 3 (tuyến tính phải hoặc tuyến tính trái) tương đương hoàn toàn với lớp ngôn ngữ chính quy ở Chương 18.

**Bài tiếp theo:** Văn phạm phi ngữ cảnh (CFG).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=WgEsPTAL55Q">Regular Grammar</a> — Neso Academy, tiếng Anh. Giới thiệu văn phạm chính quy và cấu trúc các luật sinh.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Cách thực hiện dẫn xuất chuỗi từ văn phạm.
- <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Biểu thức chính quy — một cách biểu diễn khác cho cùng lớp ngôn ngữ chính quy.
