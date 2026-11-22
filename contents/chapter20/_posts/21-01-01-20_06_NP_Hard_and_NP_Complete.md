---
layout: post
title: "NP-hard và NP-complete"
categories: chapter20
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Định nghĩa NP-hard và NP-complete, chứng minh hệ quả nếu một bài toán NP-complete thuộc P thì P=NP, quy trình 2 bước chứng minh NP-complete và định lý Ladner."
---

<div class="textbook-epigraph" markdown="1">

"NP-complete problems are the hardest problems in NP — under polynomial reductions."

<span class="epigraph-attribution">— Garey & Johnson spirit</span>

</div>

![P NP](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_p_np_sets.svg)

<p class="textbook-figure-caption" data-figure="20.4">Các bài toán NP-complete là nhóm “khó nhất” trong lớp NP theo thứ tự rút gọn $$\le_p$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** bài toán NP-hard và NP-complete.
- **Chứng minh** các hệ quả chuẩn liên kết NP-complete với câu hỏi $$P$$ và $$NP$$.
- **Áp dụng** quy trình kiểm chứng 2 bước để chứng minh một bài toán là NP-complete.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

- Bài toán $$B$$ là **NP-hard** nếu với mọi ngôn ngữ $$A\in NP$$, ta có $$A\le_p B$$.
- Bài toán $$B$$ là **NP-complete** nếu $$B$$ vừa là NP-hard vừa thuộc $$NP$$.

</div>

## Định lý then chốt

<div class="textbook-theorem" markdown="1">

**Định lý.** Cho $$B$$ là một bài toán NP-complete. Khi đó:

1. Nếu $$B\in P$$ thì $$P=NP$$.
2. Nếu $$P\neq NP$$ thì $$B\notin P$$.
3. Nếu $$A\in NP$$ và $$B\le_p A$$ thì $$A$$ cũng là NP-complete.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh (1).** Với mọi $$L\in NP$$, vì $$B$$ là NP-hard nên $$L\le_p B$$; kết hợp với $$B\in P$$ suy ra $$L\in P$$. Do đó $$NP\subseteq P$$, kéo theo $$P=NP$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh (3).** Với mọi $$L\in NP$$, ta có $$L\le_p B$$ (do $$B$$ NP-hard) và $$B\le_p A$$, theo tính bắc cầu suy ra $$L\le_p A$$. Vậy $$A$$ là NP-hard; kết hợp với $$A\in NP$$ ta được $$A$$ là NP-complete.

</div>

## Quy trình chứng minh $$A$$ là NP-complete

1. **Chứng minh $$A\in NP$$:** chỉ ra chứng chỉ ngắn và bộ kiểm chứng thời gian đa thức.
2. **Chọn một bài toán nguồn $$B$$ đã biết là NP-complete** (thường là 3SAT) và xây dựng phép biến đổi $$f$$ rút gọn $$B\le_p A$$.
3. **Chứng minh tính đúng đắn hai chiều:** $$x\in B\Leftrightarrow f(x)\in A$$.
4. **Chứng minh thời gian chạy:** hàm $$f$$ tính được trong thời gian đa thức theo $$\lvert x\rvert$$.

## Định lý Ladner

<div class="textbook-theorem" markdown="1">

**Định lý** (Ladner, 1975). Nếu $$P\neq NP$$ thì tồn tại ngôn ngữ $$L\in NP\setminus P$$ nhưng không phải là NP-complete.

</div>

Nói cách khác, dưới giả thuyết $$P\neq NP$$, tồn tại những bài toán có độ khó “trung gian” nằm giữa $$P$$ và NP-complete.

## Một số hiểu lầm thường gặp

- $$NP$$ **không** có nghĩa là “không giải được” (mọi bài toán trong $$NP$$ đều quyết định được trong thời gian hàm mũ).
- Một bài toán **NP-hard** không nhất thiết phải thuộc $$NP$$.
- Bài toán phân tích thừa số nguyên tố (Factoring) hiện chưa được biết là NP-complete.

## Bài tập

1. Trình bày lại đầy đủ chứng minh hai ý (1) và (3) của định lý then chốt.
2. Giả sử đã biết Independent Set (IS) là NP-complete và có rút gọn $$\mathrm{IS}\le_p\mathrm{VC}$$ (xem Bài 20.9), hãy suy ra Vertex Cover (VC) là NP-complete.
3. Đọc phần phác thảo chứng minh định lý Ladner trong Arora–Barak.

## Tài liệu đọc thêm

Garey–Johnson; Sipser; Ladner (1975).

## Tóm tắt

Một bài toán NP-complete vừa thuộc $$NP$$ vừa là NP-hard; chỉ cần một bài trong lớp này có thuật toán đa thức thì $$P=NP$$.

**Bài tiếp theo:** 20.7 — Định lý Cook–Levin.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Minh họa vị trí lớp NP-complete ở giao của NP và NP-hard.
- <a href="https://www.youtube.com/watch?v=e2cF8a5aAhE">8. NP-Hard and NP-Complete Problems</a> — Abdul Bari, tiếng Anh. Định nghĩa NP-hard, NP-complete cùng các ví dụ kinh điển.
- <a href="https://www.youtube.com/watch?v=W9G_1xG77LE">NP-Complete Explained (Cook-Levin Theorem)</a> — Undefined Behavior, tiếng Anh. Định lý Cook–Levin xác lập SAT là bài toán NP-complete đầu tiên.
