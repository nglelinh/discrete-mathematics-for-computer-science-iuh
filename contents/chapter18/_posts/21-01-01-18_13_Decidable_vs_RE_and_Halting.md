---
layout: post
title: "Decidable, RE và Bài toán Dừng"
categories: chapter18
date: 2021-01-01
order: 13
required: true
lang: en
excerpt: "Phân biệt ngôn ngữ quyết định được (decidable) và đệ quy liệt kê (RE); bài toán A_TM và tính không quyết định được của bài toán dừng (Halting Problem)."
---

<div class="textbook-epigraph" markdown="1">

"Some problems are not merely hard — they are impossible."

<span class="epigraph-attribution">— Computability</span>

</div>

Bài học này đóng vai trò cầu nối giữa Chương 18 và Chương 20: ngoài những bài toán khó giải trong thời gian đa thức, tồn tại những bài toán hoàn toàn **không thể quyết định được** bằng bất kỳ thuật toán nào.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân biệt** ngôn ngữ quyết định được (*decidable*) và ngôn ngữ đệ quy liệt kê (*RE*).
- **Phác thảo** lý do bài toán $$A_{\mathrm{TM}}$$ thuộc lớp RE nhưng không quyết định được.
- **Nêu** hệ quả của tính không quyết định được đối với kiểm chứng phần mềm (*verification*).

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

- **Decidable (quyết định được / đệ quy):** tồn tại một máy Turing luôn dừng trên mọi đầu vào và chấp nhận đúng các chuỗi thuộc $$L$$.
- **RE (đệ quy liệt kê / Turing-recognizable):** tồn tại một máy Turing chấp nhận đúng các chuỗi thuộc $$L$$, nhưng có thể lặp vô hạn đối với các chuỗi không thuộc $$L$$.

</div>

Quan hệ bao hàm chặt giữa các lớp ngôn ngữ là: $$\mathrm{decidable}\subsetneq\mathrm{RE}\subsetneq$$ tập mọi ngôn ngữ.

## Bài toán $$A_{\mathrm{TM}}$$

Xét ngôn ngữ $$A_{\mathrm{TM}}=\{\langle M,w\rangle:M\text{ chấp nhận }w\}$$. Ngôn ngữ này thuộc lớp **RE** vì máy Turing phổ dụng có thể mô phỏng $$M$$ trên đầu vào $$w$$ và chấp nhận khi $$M$$ chấp nhận. Tuy nhiên, $$A_{\mathrm{TM}}$$ **không quyết định được** (chứng minh bằng lập luận đường chéo, xem Sipser §4–5).

## Bài toán Dừng (*Halting Problem*)

Bài toán dừng $$\mathrm{HALT}=\{\langle M,w\rangle:M\text{ dừng trên }w\}$$ cũng là bài toán không quyết định được (có thể chứng minh bằng phép quy giảm từ $$A_{\mathrm{TM}}$$).

## Bài tập

1. Chứng minh mọi ngôn ngữ quyết định được đều thuộc lớp RE ($$\mathrm{decidable} \subseteq \mathrm{RE}$$).
2. Nếu giả sử $$A_{\mathrm{TM}}$$ quyết định được thì điều gì sẽ xảy ra?
3. Liên hệ tính không quyết định được của bài toán dừng với bài toán kiểm chứng chương trình tự động trong thực tế.

## Tài liệu đọc thêm

Sipser §4–5; Davis, *Computability and Unsolvability*.

## Tóm tắt

Lớp ngôn ngữ quyết định được là tập con thực sự của lớp RE, và bài toán dừng khẳng định giới hạn tuyệt đối của khả năng tính toán bằng thuật toán.

**Bài tiếp theo:** Lộ trình nghiên cứu ô-tô-mát và lý thuyết khả tính.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=macM_MtS_w4">Turing &amp; The Halting Problem - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu bài toán dừng và lý do không tồn tại thuật toán giải tổng quát.
- <a href="https://www.youtube.com/watch?v=6XZvw9W9QSc">The Halting Problem</a> — Neso Academy, tiếng Anh. Đặt bài toán dừng vào khung khái niệm decidable và undecidable.
- <a href="https://www.youtube.com/watch?v=_eM0-KfAmhQ">Undecidability of the Halting Problem</a> — Neso Academy, tiếng Anh. Chứng minh tính không quyết định được bằng kỹ thuật tự áp dụng.
