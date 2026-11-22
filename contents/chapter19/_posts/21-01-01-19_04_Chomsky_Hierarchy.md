---
layout: post
title: "Phân cấp Chomsky"
categories: chapter19
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Bốn lớp văn phạm Chomsky (Type 0 đến Type 3), dạng luật sinh, mô hình máy nhận dạng tương ứng và quan hệ bao hàm chặt."
---

<div class="textbook-epigraph" markdown="1">

"Four types of rules, four kinds of machines."

<span class="epigraph-attribution">— Chomsky hierarchy</span>

</div>

![Chomsky](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_chomsky_nested.svg)

<p class="textbook-figure-caption" data-figure="19.2">Quan hệ lồng nhau giữa bốn lớp ngôn ngữ: Type-3 ⊂ Type-2 ⊂ Type-1 ⊂ Type-0.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân loại** luật sinh theo bốn cấp của phân cấp Chomsky.
- **Nêu** mô hình máy nhận dạng tương ứng với từng cấp văn phạm.
- **Phát biểu** quan hệ bao hàm chặt giữa các lớp ngôn ngữ.

</div>

## Bảng phân loại Chomsky

| Loại | Tên lớp ngôn ngữ | Dạng luật sinh (ý chính) | Mô hình máy tương ứng |
|:---:|:---|:---|:---|
| 3 | Chính quy (Regular) | $$A\to aB$$ hoặc $$A\to a$$ | DFA / NFA |
| 2 | Phi ngữ cảnh (Context-Free) | $$A\to\alpha$$ | Ô-tô-mát đẩy xuống (PDA) |
| 1 | Cảm ngữ cảnh (Context-Sensitive) | $$\lvert\alpha\rvert\le\lvert\beta\rvert$$ | Ô-tô-mát giới hạn tuyến tính (LBA) |
| 0 | Đệ quy liệt kê (RE) | Tự do | Máy Turing (TM) |

<div class="textbook-theorem" markdown="1">

**Định lý** (Quan hệ bao hàm cổ điển). Các lớp ngôn ngữ trong phân cấp Chomsky lồng chặt vào nhau:

$$\mathcal{L}_3\subset\mathcal{L}_2\subset\mathcal{L}_1\subset\mathcal{L}_0$$

(với quy ước xử lý chuẩn cho luật sinh chuỗi rỗng $$\varepsilon$$).

</div>

## Bài tập

1. Xác định cấp Chomsky của văn phạm $$S\to aS\mid b$$.
2. Thảo luận trực giác vì sao ngôn ngữ $$a^nb^nc^n$$ không thuộc loại 2 (chuẩn bị cho bổ đề bơm CFL ở bài sau).
3. Liên hệ lớp ngôn ngữ loại 3 với các kết quả về ngôn ngữ chính quy ở Chương 18.

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman; các công trình lịch sử của Chomsky (1956, 1959).

## Tóm tắt

Phân cấp Chomsky chia văn phạm thành bốn loại lồng nhau, mỗi loại tương ứng trực tiếp với một mô hình bộ nhớ và máy nhận dạng riêng biệt.

**Bài tiếp theo:** Văn phạm chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu bốn bậc phân cấp Chomsky và mô hình bộ nhớ tương ứng.
- <a href="https://www.youtube.com/watch?v=VygeACNATI4">The Chomsky Hierarchy: Every Grammar Buys a Different Memory</a> — DataMListic, tiếng Anh. Giải thích trực quan mối liên hệ giữa từng lớp văn phạm và loại bộ nhớ máy.
- <a href="https://www.youtube.com/watch?v=9idnQ2C6HfA">Chomsky Hierarchy - Explained in Detail with examples</a> — Advanced CS IT for GATE, tiếng Anh. Bảng phân cấp chi tiết kèm các ví dụ ngôn ngữ cụ thể.
