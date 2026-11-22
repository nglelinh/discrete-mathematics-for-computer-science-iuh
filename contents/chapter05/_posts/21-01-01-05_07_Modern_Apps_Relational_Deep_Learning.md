---
layout: post
title: "Ghi chú mở rộng: Quan hệ như đồ thị trong học máy (2022–2026)"
categories: chapter05
date: 2021-01-01
order: 7
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Relational Deep Learning (ICML 2024) treats primary–foreign-key relations as a heterogeneous graph. Does not replace relation theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite properties of relations, closures, or orders.

Bài ghi chú ứng dụng song ngữ. Nội dung này **không** thay thế hay viết lại các bài về tính chất quan hệ, bao đóng hay thứ tự.

</div>

## English

A relational database is a family of sets (tables) plus **relations** given by primary–foreign keys — exactly the binary relations of this chapter, typed by schema. Fey et al., “Position: Relational Deep Learning — Graph Representation Learning on Relational Databases,” *ICML 2024*, [PMLR v235](https://proceedings.mlr.press/v235/fey24a.html), argue that the standard ML pipeline *destroys* that structure by flattening joins into one table.

Their blueprint: each row is a node; each foreign-key link is a directed edge; time stamps make the graph temporal and heterogeneous. A GNN then learns representations **without** hand-built aggregate features. RelBench (Robinson et al., NeurIPS 2024) is the accompanying benchmark ([relbench.stanford.edu](https://relbench.stanford.edu/)).

You do not need GNN theory to see the discrete core:

<div class="textbook-equation" markdown="1">
$$
R_{\text{FK}} \subseteq T_{\text{child}} \times T_{\text{parent}}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Message passing is iteration along that relation (and its converse) — the same walk you already used for path relations and closures. RDL is optional context for how 2024 ML research reused Chapter 5 instead of replacing it.

**Citations**

1. M. Fey et al., “Position: Relational Deep Learning — Graph Representation Learning on Relational Databases,” ICML 2024. [PMLR](https://proceedings.mlr.press/v235/fey24a.html)
2. J. Robinson et al., “RelBench: A Benchmark for Deep Learning on Relational Databases,” NeurIPS 2024. [Site](https://relbench.stanford.edu/)

**Questions.** (1) Why is a foreign key a *many-to-one* relation (usually), and how does that constrain the graph? (2) Which closure of $$R_{\text{FK}} \cup R_{\text{FK}}^{-1}$$ describes “all rows reachable by joins”?

## Tiếng Việt

Một cơ sở dữ liệu quan hệ gồm một họ các tập hợp (bảng) cùng các **quan hệ** khóa chính–khóa ngoại — chính là những quan hệ hai ngôi có kiểu xác định theo lược đồ. Trong bài báo tại *ICML 2024*, Fey và cộng sự chỉ ra rằng quy trình học máy truyền thống thường làm mất cấu trúc quan hệ đó khi làm phẳng các phép nối (join) thành một bảng duy nhất.

Hướng tiếp cận Học sâu Quan hệ (Relational Deep Learning) biểu diễn mỗi dòng dữ liệu thành một đỉnh, mỗi liên kết khóa ngoại thành một cung có hướng, và dùng dấu thời gian để tạo thành đồ thị dị thể theo thời gian (temporal heterogeneous graph). Khi đó, mạng nơ-ron đồ thị (GNN) có thể học trực tiếp biểu diễn dữ liệu mà không cần thiết kế thủ công các đặc trưng tổng hợp. Bộ chuẩn đánh giá đi kèm là RelBench (Robinson và cộng sự, *NeurIPS 2024*).

Không cần đi sâu vào lý thuyết GNN, ta vẫn thấy rõ phần lõi toán rời rạc: $$R_{\text{FK}} \subseteq T_{\text{con}} \times T_{\text{cha}}$$. Cơ chế truyền thông điệp (message passing) thực chất là phép lặp dọc theo quan hệ này và quan hệ ngược của nó — tương tự bước đi trên đồ thị khi xét lũy thừa quan hệ và bao đóng. Ghi chú này cung cấp thêm bối cảnh cho thấy nghiên cứu học máy năm 2024 tiếp tục khai thác trực tiếp các khái niệm của Chương 5.

**Câu hỏi.** (1) Vì sao liên kết khóa ngoại thường là quan hệ *nhiều–một*, và tính chất đó ràng buộc cấu trúc đồ thị như thế nào? (2) Loại bao đóng nào của $$R_{\text{FK}} \cup R_{\text{FK}}^{-1}$$ mô tả tập hợp "mọi dòng có thể đi tới được bằng các phép join"?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eGoszzMkGfU">Graph Neural Networks Explained: A Clear Guide to GNN Basics &amp; Models</a> — IBM Technology, tiếng Anh. Giới thiệu mạng nơ-ron đồ thị, kiến trúc được áp dụng cho đồ thị quan hệ khóa.
- <a href="https://www.youtube.com/watch?v=1DmNdMUbDkg">Message Passing: How Graph Neural Networks Actually Work</a> — The Synthetic Mind, tiếng Anh. Giải thích cơ chế truyền thông điệp trên cạnh trong quá trình học trên đồ thị quan hệ.
- <a href="https://www.youtube.com/watch?v=aFnHYEv71U4">An Introduction to Graph Neural Networks</a> — DataMListic, tiếng Anh. Minh họa cách GNN biểu diễn bảng và khóa ngoại dưới dạng đồ thị dị thể.
