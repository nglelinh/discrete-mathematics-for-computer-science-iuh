---
layout: post
title: "Lớp P và Time Hierarchy"
categories: chapter20
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Ví dụ trong P; đóng dưới phép toán cơ bản; định lý time hierarchy và hệ quả P ⊊ EXPTIME."
---

<div class="textbook-epigraph" markdown="1">

"P is robust — and strictly smaller than exponential time."

<span class="epigraph-attribution">— Time hierarchy spirit</span>

</div>

Sau định nghĩa $$P$$, ta cần: (i) biết **cư dân** điển hình; (ii) biết $$P$$ **đóng** dưới một số phép; (iii) biết có ngôn ngữ **ngoài** $$P$$ nhờ hierarchy — *không* giải quyết $$P$$ vs $$NP$$.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Liệt kê** bài trong $$P$$ và lập luận ngắn.
- **Chứng minh** một số tính đóng của $$P$$.
- **Phát biểu** deterministic time hierarchy và suy $$P\subsetneq\mathrm{EXPTIME}$$.

</div>

## 1. Cư dân của $$P$$

| Bài | Lý do ngắn |
|:---|:---|
| Connectivity | BFS $$O(V+E)$$ |
| Shortest path $$w\ge 0$$ | Dijkstra |
| Matching (cận) | Edmonds — đa thức |
| Linear programming | Khachiyan / Karmarkar (bit model) |
| Primality | AKS (2002) ∈ $$P$$ |

## 2. Tính đóng

<div class="textbook-theorem" markdown="1">

**Định lý.** Nếu $$A,B\in P$$ thì $$A\cup B$$, $$A\cap B$$, $$\overline{A}\in P$$.  
Nếu $$L\in P$$ thì $$L^*\in P$$ (Kleene star).

</div>

**Chứng minh (star).**  
Cho thuật toán $$M$$ quyết định $$L$$ trong $$n^k$$. Với $$w$$ độ dài $$n$$, DP: $$S[0]=\mathrm{true}$$; $$S[j]=\bigvee_{i<j}\bigl(S[i]\land M(w_{i+1..j})\bigr)$$.  
$$O(n^2)$$ ô, mỗi ô gọi $$M$$ trên chuỗi $$\le n$$: tổng $$O(n^{k+2})$$. $$\square$$

*(Hợp/giao/bù: chạy song song hoặc đảo output.)*

## 3. Time hierarchy

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$t$$ **time-constructible** nếu có TM trên $$1^n$$ chạy khoảng $$t(n)$$ bước và ghi $$t(n)$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Hartmanis–Stearns, dạng dùng).  
Nếu $$t_1,t_2$$ time-constructible và $$t_1(n)\log t_1(n)=o(t_2(n))$$ thì

$$
\mathrm{TIME}(t_1(n))\subsetneq\mathrm{TIME}(t_2(n)).
$$

</div>

**Ý chứng minh:** diagonalization — máy “mô phỏng rồi đảo” mọi máy thời gian $$t_1$$ (Sipser/Arora–Barak).

**Hệ quả.** $$P\subsetneq\mathrm{EXPTIME}=\bigcup_k\mathrm{TIME}(2^{n^k})$$.

**Hệ quả nghiên cứu.** Hierarchy **không** tách $$P$$ khỏi $$NP$$: kỹ thuật diagonal “đơn giản” relativize / không đủ tinh.

## Bài tập

1. Chứng minh $$A,B\in P\Rightarrow A\cap B\in P$$.  
2. Vì sao $$n^{100}\in P$$ nhưng có thể vô dụng?  
3. Đọc phác hierarchy trong Sipser: diagonalization khác Cook–Levin chỗ nào?

## Đọc

Arora–Barak §1.4 (hierarchy); Sipser advanced time hierarchy.

## Tóm tắt

$$P$$ đóng · hierarchy ⇒ có bài ngoài $$P$$ · chưa phải $$P$$ vs $$NP$$.

**Tiếp:** 20.3 — định nghĩa $$NP$$.

## Video tham khảo

- **xem trước** <a href="https://www.youtube.com/watch?v=XV6f7XYUMg8">What Makes P vs. NP So Hard? (P ≠ EXPTIME, Time Hierarchy, Baker-Gill-Solovay)</a> — Undefined Behavior, tiếng Anh. Xem trước vì sao phân cấp thời gian tách P khỏi lớp mũ.
- <a href="https://www.youtube.com/watch?v=l2aXF0B2E9M">What is the Time Hierarchy Theorem? - Easy Theory</a> — Easy Theory, tiếng Anh. Định lý phân cấp thời gian, đúng mục 3 của bài.
- <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Lớp P nằm ở đâu trong sở thú độ phức tạp.
