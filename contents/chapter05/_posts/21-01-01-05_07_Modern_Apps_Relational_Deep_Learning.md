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


Trong suốt nhiều thập kỷ, mỗi khi muốn đưa dữ liệu doanh nghiệp vào mô hình học máy như XGBoost, các kỹ sư dữ liệu phải viết hàng trăm dòng SQL `JOIN`, `GROUP BY` và `AVG` thủ công để ép một cơ sở dữ liệu gồm hàng chục bảng liên kết nhau thành một bảng phẳng duy nhất—làm rơi rớt vô số thông tin cấu trúc. **Học sâu Quan hệ (Relational Deep Learning — ICML 2024)** đảo ngược hoàn toàn cách làm đó: giữ nguyên các mối quan hệ khóa chính–khóa ngoại thành một đồ thị để mạng nơ-ron học trực tiếp.

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite properties of relations, closures, or orders.

Bài ghi chú ứng dụng song ngữ. Nội dung này **không** thay thế hay viết lại các bài về tính chất quan hệ, bao đóng hay thứ tự.

</div>

## Bản đồ kiến thức nền: Ba trụ cột của Học sâu Quan hệ (Relational Deep Learning)

1. **Từ bảng phẳng (Flat Table) sang Đồ thị Quan hệ Dị thể (Heterogeneous Graph)**:
   Mỗi dòng dữ liệu trong bảng là một **đỉnh** (có kiểu theo tên bảng: Khách hàng, Đơn hàng, Sản phẩm), còn mỗi liên kết khóa chính–khóa ngoại $R_{\text{FK}} \subseteq T_{\text{con}} \times T_{\text{cha}}$ là một **cung có hướng**.

2. **Dấu thời gian (Temporal Constraints) chống rò rỉ tương lai**:
   Vì các giao dịch phát sinh theo dòng thời gian, mỗi đỉnh/cạnh đều gắn mốc thời gian $t$. Khi dự đoán hành vi tại thời điểm $t_0$, mô hình chỉ được phép truyền thông tin từ các liên kết xảy ra ở quá khứ $t \le t_0$.

3. **Truyền thông điệp (Message Passing) chính là Hợp thành Quan hệ nhiều bước**:
   Ở mỗi tầng mạng GNN, một đỉnh tổng hợp vector đặc trưng từ các láng giềng đi dọc theo $R_{\text{FK}}$ và quan hệ ngược $R_{\text{FK}}^{-1}$. Chạy $L$ tầng truyền thông điệp tương đương với việc tự động học các đặc trưng dọc theo mọi đường đi quan hệ độ dài tối đa $L$—không cần kỹ sư viết tay phép tổng hợp!

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

### Khung giải thích (nên đọc chậm): Chuyển tay 3 bảng dữ liệu thành đồ thị quan hệ và tính 1 bước truyền thông điệp

Xét cơ sở dữ liệu mini gồm 3 bảng:
- **`Users`**: `U1 (An)`, `U2 (Bình)`
- **`Orders`** (có khóa ngoại `user_id` $\to$ `Users` và `prod_id` $\to$ `Products`):
  - `O1`: `U1` mua `P1`, giá trị `200` nghìn đồng
  - `O2`: `U1` mua `P2`, giá trị `500` nghìn đồng
  - `O3`: `U2` mua `P2`, giá trị `300` nghìn đồng
- **`Products`**: `P1 (Sách)`, `P2 (Tai nghe)`

1. **Dựng hai quan hệ khóa ngoại $R_1 \subseteq \text{Orders} \times \text{Users}$ và $R_2 \subseteq \text{Orders} \times \text{Products}$**:
   - $R_1 = \{(\text{O1}, \text{U1}), (\text{O2}, \text{U1}), (\text{O3}, \text{U2})\}$ (mỗi đơn thuộc đúng 1 người dùng $\Rightarrow$ quan hệ nhiều–một).
   - $R_2 = \{(\text{O1}, \text{P1}), (\text{O2}, \text{P2}), (\text{O3}, \text{P2})\}$.
2. **Bước truyền thông điệp tầng 1 vào đỉnh `U1` (đi theo quan hệ ngược $R_1^{-1}$)**:
   Các láng giềng của `U1` là `O1 (200)` và `O2 (500)`. Với phép gộp trung bình (`MEAN`), đặc trưng cập nhật của `U1` nhận thông điệp $\frac{200 + 500}{2} = \mathbf{350}$ (tương đương tự động học `AVG(amount)` mà không cần viết SQL thủ công).
3. **Quan hệ hợp thành 2 bước (`Users` $\to$ `Products`) qua $R_2 \circ R_1^{-1}$**:
   Đi từ `U1` theo $R_1^{-1}$ tới `{O1, O2}`, rồi đi tiếp theo $R_2$ tới `{P1, P2}` $\implies$ `U1` nhận tín hiệu ngữ nghĩa từ cả `Sách` lẫn `Tai nghe` ở tầng GNN thứ 2—đúng bản chất phép hợp thành quan hệ bạn vừa học trong Chương 5!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eGoszzMkGfU">Graph Neural Networks Explained: A Clear Guide to GNN Basics &amp; Models</a> — IBM Technology, tiếng Anh. Giới thiệu mạng nơ-ron đồ thị, kiến trúc được áp dụng cho đồ thị quan hệ khóa.
- <a href="https://www.youtube.com/watch?v=1DmNdMUbDkg">Message Passing: How Graph Neural Networks Actually Work</a> — The Synthetic Mind, tiếng Anh. Giải thích cơ chế truyền thông điệp trên cạnh trong quá trình học trên đồ thị quan hệ.
- <a href="https://www.youtube.com/watch?v=aFnHYEv71U4">An Introduction to Graph Neural Networks</a> — DataMListic, tiếng Anh. Minh họa cách GNN biểu diễn bảng và khóa ngoại dưới dạng đồ thị dị thể.
