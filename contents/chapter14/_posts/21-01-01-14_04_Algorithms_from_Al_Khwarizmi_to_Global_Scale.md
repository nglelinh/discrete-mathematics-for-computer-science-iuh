---
layout: post
title: "Thuật toán: Từ Al-Khwarizmi đến Quy mô Toàn cầu"
categories: chapter14
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Khảo sát: nguồn gốc algorithm; sắp xếp/tìm kiếm; thuật toán trên mạng và dữ liệu lớn; trade-off độ phức tạp thực tế."
---

<div class="textbook-epigraph" markdown="1">

"Algorithms are the verbs of computation — and scale is where their cost becomes visible."

<span class="epigraph-attribution">— Systems + theory spirit</span>

</div>

Mục 14.1–14.3 đặt định nghĩa và Big-O. Mục khảo sát nối **lịch sử từ ngữ** và vài **bài toán quy mô lớn**: tìm kiếm web, sắp xếp phân tán, chi phí năng lượng/thời gian — không thay giáo trình cấu trúc dữ liệu đầy đủ.

![Al-Khwarizmi](/discrete-mathematics-for-computer-science-iuh/img/course/Al-Khwarizmi.jpg)

<p class="textbook-figure-caption" data-figure="14.6">Al-Khwarizmi — nguồn gốc từ *al-jabr* / *algorithm* trong truyền thống châu Âu trung cổ.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nêu** nguồn gốc thuật ngữ *algorithm*.
- **Liên hệ** Big-O với lựa chọn thuật toán khi $$n$$ lớn.
- **Mô tả** vài bài toán quy mô hệ thống (index, sort, graph).
- **Thảo luận** trade-off thời gian / không gian / đơn giản triển khai.

**Từ khóa**: scale, indexing, distributed sort, practical complexity.

</div>

## 1. Từ Al-Khwarizmi đến Knuth

Quy trình số học Ả Rập–Ba Tư được Latin hóa thành *algorismus*, rồi *algorithm*. Khoa học máy tính hiện đại (Knuth, CLRS, …) chuẩn hóa **phân tích tiệm cận** và mã giả — đúng tinh thần 14.1–14.3.

## 2. Khi $$n$$ tăng một bậc

| $$n$$ | $$n$$ | $$n\log n$$ | $$n^2$$ | $$2^n$$ |
|:---:|:---:|:---:|:---:|:---:|
| $$20$$ | nhỏ | nhỏ | nhỏ | ~1M |
| $$40$$ | nhỏ | nhỏ | vừa | khổng lồ |
| $$10^6$$ | OK | OK | nặng | không |

Bài toán “khả thi” phụ thuộc **bậc** chứ không chỉ “máy nhanh hơn năm ngoái”.

## 3. Hệ thống thực tế (ý)

- **Tìm kiếm**: index + cấu trúc (cây, hash) để tránh quét $$\Theta(n)$$ toàn corpus.
- **Sắp xếp**: merge/heap $$\Theta(n\log n)$$; external sort khi không lọt RAM.
- **Đồ thị** (Ch.12–17): BFS/Dijkstra/MST — chi phí theo $$V,E$$.
- **Heuristic**: khi bài NP-hard (Ch.20), chấp nhận xấp xỉ / timeout.

## 4. Trade-off kỹ nghệ

1. Đúng trước — rồi tối ưu chỗ hot path (đo đạc).
2. $$\Theta(n\log n)$$ ổn định thường tốt hơn average nhanh nhưng worst thảm họa (nếu SLA cần worst).
3. Bộ nhớ phụ rẻ hơn thời gian CPU trong nhiều hệ — nhưng không phải lúc nào cũng vậy (embedded).

## Bài tập

### Bài tập 1

Vì sao web search không linear-scan mọi trang mỗi truy vấn?

<details>
<summary>Đáp án</summary>

$$n$$ quá lớn; cần index / cấu trúc để tra gần $$O(\log n)$$ hoặc tốt hơn theo thiết kế, không $$\Theta(n)$$ mỗi lần.

</details>

### Bài tập 2

Chọn sort $$\Theta(n\log n)$$ worst vs sort average nhanh hơn nhưng $$O(n^2)$$ worst cho hệ thanh toán — ưu tiên gì?

<details>
<summary>Đáp án</summary>

Thường ưu tiên **chặn worst-case** (SLA, an toàn) — merge/heapsort-style hoặc sort thư viện đã kiểm chứng.

</details>

## Tóm tắt Chương 14

| Mục | Nội dung |
|:---|:---|
| 14.1 | Định nghĩa thuật toán |
| 14.2 | Big-O / Θ / Ω |
| 14.3 | Phân tích $$T(n)$$, $$S(n)$$ |
| 14.4 | Quy mô và trade-off |

Chương 15–17 áp dụng thuật toán trên số và đồ thị; Ch.20 hỏi **có** thuật toán đa thức hay không.
