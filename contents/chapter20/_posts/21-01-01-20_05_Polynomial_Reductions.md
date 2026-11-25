---
layout: post
title: "Rút gọn Đa thức (Karp Reduction)"
categories: chapter20
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định nghĩa phép rút gọn thời gian đa thức A≤ₚB, chứng minh tính phản xạ, bắc cầu, tính bảo toàn lớp P và so sánh rút gọn Karp với rút gọn Cook."
---

<div class="textbook-epigraph" markdown="1">

"Reductions are the comparative method of complexity theory."

<span class="epigraph-attribution">— Karp tradition</span>

</div>

Phép rút gọn là **công cụ so sánh độ khó giữa các bài toán**: biến đổi nhanh một thể hiện của bài toán $$A$$ thành một thể hiện của bài toán $$B$$ sao cho câu trả lời Có/Không được bảo toàn nguyên vẹn.

![Reduction](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_reduction.svg)

<p class="textbook-figure-caption" data-figure="20.3">Phép biến đổi đa thức $$f$$ bảo toàn tính thuộc ngôn ngữ: $$x\in A\Leftrightarrow f(x)\in B$$.</p>

Nếu bạn không biết cách giải bài toán $$A$$, nhưng bạn biết cách *dịch nhanh* mọi dữ liệu của $$A$$ thành bài toán $$B$$ rồi nhờ thuật toán giải $$B$$ trả lời hộ, thì có hai kết luận cực kỳ sâu sắc cùng lúc: nếu $$B$$ dễ thì $$A$$ cũng dễ; và ngược lại, nếu $$A$$ đã nổi tiếng là khó thì $$B$$ **ít nhất phải khó ngang $$A$$**! Phép dịch nhanh đó chính là **rút gọn đa thức Karp ($$A \le_p B$$)** — chiếc cân so sánh độ khó giữa hàng nghìn bài toán tính toán.

## Kiến thức cần nhớ: Ba trụ cột của Rút gọn Đa thức

1. **Định nghĩa Rút gọn Nhiều–Một Đa thức (Karp Reduction $$A \le_p B$$)**:
   Tồn tại hàm tính được trong thời gian đa thức $$f: \{0,1\}^* \to \{0,1\}^*$$ sao cho với **mọi** đầu vào $$x$$:
   $$x \in A \iff f(x) \in B.$$
   Chú ý hai chiều của dấu $$\iff$$: phải chứng minh cả chiều thuận (YES $$\implies$$ YES) lẫn chiều đảo (YES ở $$B \implies$$ YES ở $$A$$, tương đương NO $$\implies$$ NO)!
2. **Tính bắc cầu & Bảo toàn lớp $$P, NP$$**:
   Nếu $$A \le_p B$$ và $$B \le_p C$$ thì $$A \le_p C$$ (vì hợp thành hai đa thức vẫn là đa thức). Nếu $$B \in P$$ thì $$A \in P$$; nếu $$A \notin P$$ thì $$B \notin P$$.
3. **Rút gọn Karp ($$\le_p$$) vs. Rút gọn Cook/Turing ($$\le_T^p$$)**:
   Karp chỉ cho phép gọi "nhà tiên tri" $$B$$ đúng **1 lần ở cuối** và giữ nguyên câu trả lời (không đảo ngược), nên giữ chặt ranh giới giữa $$NP$$ và $$\mathrm{coNP}$$. Cook cho gọi $$B$$ nhiều lần và được phép phủ định kết quả (nên $$\mathrm{SAT} \le_T^p \overline{\mathrm{SAT}}$$).

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** phép rút gọn đa thức $$A\le_p B$$.
- **Chứng minh** tính phản xạ, tính bắc cầu và tính chất “$$B\in P\Rightarrow A\in P$$”.
- **Phân biệt** rút gọn Karp (*many-one*) và rút gọn Cook (*Turing*).

</div>

## Định nghĩa rút gọn Karp

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Ta nói $$A$$ rút gọn đa thức được về $$B$$, ký hiệu $$A\le_p B$$, nếu tồn tại một hàm $$f$$ tính được trong thời gian đa thức sao cho:

$$
\forall x:\quad x\in A\iff f(x)\in B.
$$

</div>

## Các tính chất cơ bản

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính phản xạ). $$A\le_p A$$ với hàm đồng nhất $$f=\mathrm{id}$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính bắc cầu). Nếu $$A\le_p B$$ và $$B\le_p C$$ thì $$A\le_p C$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử $$f$$ rút gọn $$A$$ về $$B$$ và $$g$$ rút gọn $$B$$ về $$C$$; xét hàm hợp $$h=g\circ f$$. Tính tương đương Có/Không suy trực tiếp từ tính bắc cầu của phép tương đương $$\Leftrightarrow$$. Về thời gian, vì mỗi bước của $$f$$ ghi ra tối đa một ký hiệu nên $$\lvert f(x)\rvert\le\mathrm{poly}(\lvert x\rvert)$$, do đó thời gian tính $$g(f(x))$$ là đa thức theo $$\lvert f(x)\rvert$$ và suy ra là đa thức theo $$\lvert x\rvert$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Bảo toàn lớp $$P$$). Nếu $$A\le_p B$$ và $$B\in P$$ thì $$A\in P$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Với đầu vào $$x$$, ta tính $$y=f(x)$$ trong thời gian đa thức, sau đó chạy thuật toán đa thức quyết định $$y\in B$$ rồi trả về đúng kết quả đó.

</div>

<div class="textbook-theorem" markdown="1">

**Hệ quả.** Nếu $$A\le_p B$$ và $$A\notin P$$ thì $$B\notin P$$.

</div>

## So sánh rút gọn Karp và rút gọn Cook

| Tiêu chí | Rút gọn Karp (*many-one*) | Rút gọn Cook (*Turing*) |
|:---|:---|:---|
| Số lần gọi lời giải cho $$B$$ | Đúng 1 lần (sau khi tính $$f(x)$$) | Có thể gọi nhiều lần như một chương trình con (*oracle*) |
| Dùng để định nghĩa NP-complete cổ điển | **Có** | Hiếm dùng làm định nghĩa chuẩn cho NPC |

Mọi phép rút gọn Karp đều là một phép rút gọn Cook, nhưng chiều ngược lại nói chung không tầm thường.

### Giải thích: Chiều rút gọn — Lỗi sai kinh điển nhất của sinh viên khi chứng minh NP-hard

Giả sử bạn đã biết `3SAT` là bài toán rất khó (NP-complete) và muốn chứng minh bài toán mới `MY-PROB` cũng khó tương đương. Bạn phải chọn **đúng chiều mũi tên**:

| Chiều rút gọn | Ý nghĩa trực giác | Kết luận rút ra | Đúng hay Sai cho mục tiêu chứng minh `MY-PROB` khó? |
| :--- | :--- | :--- | :---: |
| `MY-PROB` $$\le_p$$ `3SAT` | `MY-PROB` *không khó hơn* `3SAT` | `MY-PROB` $$\in NP$$ (chỉ chặn trên!) | **SAI** (ngay cả bài toán tầm thường `1+1=2` cũng $$\le_p$$ `3SAT`!) |
| `3SAT` $$\le_p$$ `MY-PROB` | `MY-PROB` *khó ít nhất bằng* `3SAT` | `MY-PROB` là **NP-hard**! | **ĐÚNG!** |

**Mẹo nhớ không bao giờ nhầm:** Dấu $$\le_p$$ đọc là *"dễ hơn hoặc bằng"*. Muốn chứng minh $$B$$ khó, phải đặt bài toán **ĐÃ BIẾT KHÓ ở bên TRÁI** ($$\text{Đã biết khó} \le_p B$$) để đẩy độ khó sang $$B$$!

## Bài tập

1. Chứng minh định lý bắc cầu với chặn cụ thể khi $$f$$ chạy trong thời gian $$n^2$$ và $$g$$ chạy trong thời gian $$m^3$$.
2. Chứng minh rằng nếu $$A\le_p B$$ thì $$\overline{A}\le_p\overline{B}$$.
3. Nêu ý tưởng về một phép rút gọn Cook nhưng không phải rút gọn many-one (thảo luận).

## Tài liệu đọc thêm

Sipser; Arora–Barak §2.2; Garey–Johnson §5.

## Tóm tắt

Phép rút gọn đa thức $$\le_p$$ có tính bắc cầu, truyền khả năng giải đa thức ngược về bài toán nguồn và là nền tảng để định nghĩa NP-hard, NP-complete.

**Bài tiếp theo:** 20.6 — NP-hard và NP-complete.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=tPRYHkp21YU">Polynomial Time Reductions: Karp Reductions &amp; NP-Completeness Explained!</a> — CodeLucky, tiếng Anh. Giới thiệu phép rút gọn Karp trong thời gian đa thức.
- <a href="https://www.youtube.com/watch?v=O7pq43hIE_0">What is a polynomial-time reduction? (NP-Hard + NP-complete)</a> — Easy Theory, tiếng Anh. Vai trò của rút gọn đa thức trong việc kết nối NP-hard và NP-complete.
- <a href="https://www.youtube.com/watch?v=sr9KJwaZH1A">Karp Reductions</a> — Computer Science Theory Explained, tiếng Anh. Phân tích chi tiết phép rút gọn kiểu many-one của Karp.
