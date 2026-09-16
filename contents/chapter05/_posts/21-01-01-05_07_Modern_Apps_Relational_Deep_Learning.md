---
layout: post
title: "Optional note: Relations as graphs for learning (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại tính chất quan hệ, bao đóng hay thứ tự.

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

Cơ sở dữ liệu quan hệ là họ các tập (bảng) cộng **quan hệ** khóa chính–khóa ngoại — đúng quan hệ hai ngôi có kiểu theo schema. Fey và cộng sự (ICML 2024) cho rằng pipeline ML thông thường *phá* cấu trúc đó khi flatten join thành một bảng.

Khung của họ: mỗi dòng là một đỉnh; mỗi liên kết khóa ngoại là một cạnh có hướng; mốc thời gian làm đồ thị dị thể và có thời gian. GNN học biểu diễn **không** cần feature kết tập viết tay. RelBench (NeurIPS 2024) là benchmark kèm theo.

Không cần lý thuyết GNN để thấy lõi rời rạc: $$R_{\text{FK}} \subseteq T_{\text{con}} \times T_{\text{cha}}$$. Message passing là lặp theo quan hệ đó (và quan hệ ngược) — cùng kiểu đi trên quan hệ đường đi và bao đóng. RDL là ngữ cảnh tùy chọn: nghiên cứu ML 2024 tái sử dụng Chương 5 chứ không thay nó.

**Câu hỏi.** (1) Vì sao khóa ngoại thường là quan hệ *nhiều-một*, và điều đó ràng buộc đồ thị ra sao? (2) Bao đóng nào của $$R_{\text{FK}} \cup R_{\text{FK}}^{-1}$$ mô tả “mọi dòng tới được bằng join”?
