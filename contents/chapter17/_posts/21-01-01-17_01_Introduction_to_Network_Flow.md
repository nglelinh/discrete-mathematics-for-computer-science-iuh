---
layout: post
title: "Luồng trong Mạng và Định lý Max-Flow Min-Cut"
categories: chapter17
date: 2021-01-01
order: 1
required: true
lang: en
---

# Luồng trong Mạng và Định lý Max-Flow Min-Cut

Hãy tưởng tượng bạn vận hành một mạng đường ống dẫn dầu từ một mỏ ở Vũng Tàu đến nhà máy lọc dầu ở Quy Nhơn. Mỗi đoạn ống có một **giới hạn lưu lượng** (capacity) khác nhau. Câu hỏi: bao nhiêu thùng dầu mỗi giờ có thể chảy từ mỏ đến nhà máy? Cùng cấu trúc bài toán này xuất hiện trong định tuyến gói tin Internet, lập lịch chuyến bay, phân công công việc, thậm chí trong phân tích đoạn văn bản để phát hiện đạo văn.

Lý thuyết **luồng trong mạng** (network flow) cho ta một ngôn ngữ chung để mô hình hóa và giải tất cả những bài toán đó. Trong bài này chúng ta sẽ định nghĩa thế nào là mạng, thế nào là luồng, thế nào là lát cắt, và phát biểu một trong những định lý đẹp nhất của lý thuyết đồ thị - **định lý Max-Flow Min-Cut** - khẳng định rằng luồng cực đại bằng đúng lát cắt cực tiểu.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** mạng luồng (flow network), luồng (flow), lát cắt (cut) và giá trị của chúng.
- **Tính** giá trị luồng và dung lượng lát cắt trên một mạng nhỏ.
- **Phát biểu** và **giải thích trực giác** Định lý Max-Flow Min-Cut.
- **Nhận diện** các bài toán thực tế có thể mô hình hóa bằng luồng trong mạng.

**Từ khóa**: mạng luồng (flow network), nguồn (source), đích (sink), dung lượng (capacity), luồng (flow), bảo toàn luồng (flow conservation), lát cắt (cut), luồng cực đại (max-flow), lát cắt cực tiểu (min-cut).

## 1. Mạng Luồng

**Định nghĩa**: Một **mạng luồng** (flow network) là một bộ $$(G, c, s, t)$$ gồm:

- Một đồ thị có hướng $$G = (V, E)$$.
- Một hàm dung lượng $$c: E \to \mathbb{R}_{\geq 0}$$ gán cho mỗi cạnh $$(u, v) \in E$$ một số không âm $$c(u, v)$$ - **dung lượng** tối đa có thể đi qua cạnh đó.
- Hai đỉnh đặc biệt: **nguồn** $$s \in V$$ (source) và **đích** $$t \in V$$ (sink), $$s \neq t$$.

Quy ước: nếu $$(u, v) \notin E$$ thì $$c(u, v) = 0$$.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: Mạng đường ống đơn giản với 4 đỉnh và 5 cạnh:

- Nguồn $$s$$, đỉnh trung gian $$a$$, $$b$$, đích $$t$$.
- Cạnh và dung lượng: $$c(s, a) = 10$$, $$c(s, b) = 5$$, $$c(a, b) = 4$$, $$c(a, t) = 7$$, $$c(b, t) = 8$$.

Đồ thị này mô tả một mạng có hai con đường chính từ $$s$$ đến $$t$$, với một cạnh tắt $$a \to b$$ ở giữa.
</div>

## 2. Luồng

**Định nghĩa**: Một **luồng** (flow) trên mạng $$(G, c, s, t)$$ là một hàm $$f: V \times V \to \mathbb{R}$$ thỏa mãn:

1. **Ràng buộc dung lượng** (capacity constraint): với mọi $$u, v \in V$$, $$0 \leq f(u, v) \leq c(u, v)$$.
2. **Bảo toàn luồng** (flow conservation): với mọi đỉnh $$u \in V \setminus \{s, t\}$$,

$$\sum_{v \in V} f(v, u) = \sum_{v \in V} f(u, v).$$

Tức là: lượng chảy **vào** mỗi đỉnh trung gian bằng lượng chảy **ra** khỏi nó. Nguồn $$s$$ và đích $$t$$ được miễn ràng buộc này - $$s$$ chỉ sinh ra luồng, $$t$$ chỉ hấp thụ luồng.

**Giá trị của luồng** $$f$$, ký hiệu $$|f|$$, là tổng luồng đi ra khỏi nguồn:

$$|f| = \sum_{v \in V} f(s, v) - \sum_{v \in V} f(v, s).$$

Theo bảo toàn luồng, $$|f|$$ cũng bằng tổng luồng đi vào đích.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Tiếp tục mạng ở Ví dụ 1. Một luồng hợp lệ có thể là:

$$f(s, a) = 7, \quad f(s, b) = 5, \quad f(a, b) = 0, \quad f(a, t) = 7, \quad f(b, t) = 5.$$

Kiểm tra:

- Bảo toàn tại $$a$$: vào $$7$$, ra $$0 + 7 = 7$$. OK.
- Bảo toàn tại $$b$$: vào $$5 + 0 = 5$$, ra $$5$$. OK.
- $$|f| = 7 + 5 = 12$$.

Nhưng đây có phải là luồng lớn nhất? Câu trả lời sẽ rõ sau khi ta học về **lát cắt**.
</div>

## 3. Bài toán Luồng Cực đại

**Bài toán Max-Flow**: Cho mạng $$(G, c, s, t)$$, tìm luồng $$f$$ có giá trị $$|f|$$ **lớn nhất**.

Đây là một bài toán **tối ưu** (optimization problem). Không hiển nhiên rằng luồng cực đại tồn tại, hay rằng có cách hiệu quả để tìm nó. Hai câu hỏi lý thuyết quan trọng:

1. **Cận trên**: làm thế nào để biết một luồng đã là cực đại, hay vẫn còn cải tiến được?
2. **Thuật toán**: có cách hệ thống nào để xây dựng luồng cực đại?

Câu hỏi (1) được trả lời bằng khái niệm **lát cắt**. Câu hỏi (2) được giải trong bài 17_02 bằng thuật toán Ford-Fulkerson.

## 4. Lát cắt

**Định nghĩa**: Một **lát cắt s-t** (s-t cut) của mạng là một phân hoạch $$V = S \cup T$$ với $$s \in S$$, $$t \in T$$, $$S \cap T = \emptyset$$.

**Dung lượng của lát cắt** $$(S, T)$$ là tổng dung lượng các cạnh đi từ $$S$$ sang $$T$$:

$$c(S, T) = \sum_{u \in S} \sum_{v \in T} c(u, v).$$

Chú ý: chỉ tính các cạnh đi từ $$S$$ sang $$T$$, không tính ngược lại.

<div class="content-box example-box" markdown="1">
**Ví dụ 3**: Trong mạng Ví dụ 1, xét lát cắt $$S = \{s, a\}$$, $$T = \{b, t\}$$.

Các cạnh đi từ $$S$$ sang $$T$$:

- $$(s, b)$$ với dung lượng $$5$$.
- $$(a, b)$$ với dung lượng $$4$$.
- $$(a, t)$$ với dung lượng $$7$$.

Vậy $$c(S, T) = 5 + 4 + 7 = 16$$.

Một lát cắt khác $$S' = \{s\}$$, $$T' = \{a, b, t\}$$:

- $$(s, a)$$: $$10$$.
- $$(s, b)$$: $$5$$.

$$c(S', T') = 10 + 5 = 15$$.

Lát cắt thứ hai có dung lượng nhỏ hơn.
</div>

## 5. Bổ đề: Luồng không vượt Lát cắt

**Bổ đề (Cận trên cho luồng)**: Với mọi luồng $$f$$ và mọi lát cắt $$(S, T)$$,

$$|f| \leq c(S, T).$$

**Trực giác**: mọi luồng từ $$s$$ đến $$t$$ phải **vượt qua** lát cắt ít nhất một lần (đi từ phía $$S$$ sang phía $$T$$). Lượng luồng vượt qua không thể quá tổng dung lượng các cạnh nối $$S$$ với $$T$$.

**Chứng minh phác thảo**: Từ bảo toàn luồng, ta có thể viết

$$|f| = \sum_{u \in S} \sum_{v \in T} f(u, v) - \sum_{u \in S} \sum_{v \in T} f(v, u).$$

Mỗi $$f(u, v) \leq c(u, v)$$ và mỗi $$f(v, u) \geq 0$$. Suy ra

$$|f| \leq \sum_{u \in S} \sum_{v \in T} c(u, v) = c(S, T). \square$$

**Hệ quả**: Nếu tồn tại luồng $$f$$ và lát cắt $$(S, T)$$ với $$|f| = c(S, T)$$, thì $$f$$ là luồng cực đại và $$(S, T)$$ là lát cắt cực tiểu.

## 6. Định lý Max-Flow Min-Cut

Định lý sau đây - chứng minh bởi Ford và Fulkerson năm 1956 - là một trong những kết quả đẹp nhất của lý thuyết đồ thị.

<div class="content-box insight-box" markdown="1">
**Định lý Max-Flow Min-Cut**: Trong mọi mạng luồng $$(G, c, s, t)$$,

$$\max_{f \text{ là luồng}} |f| = \min_{(S, T) \text{ là lát cắt}} c(S, T).$$

Tức là **giá trị luồng cực đại bằng dung lượng lát cắt cực tiểu**.
</div>

**Trực giác**: Bổ đề trên cho thấy mọi luồng đều bị chặn trên bởi mọi lát cắt. Định lý nói thêm rằng cận này là **chặt**: luôn tồn tại một cặp luồng-lát cắt mà luồng đạt đúng dung lượng lát cắt.

**Ý nghĩa thuật toán**: định lý cho ta một **chứng nhận tối ưu** (optimality certificate). Khi ta tìm được luồng $$f$$ cùng lát cắt $$(S, T)$$ với $$|f| = c(S, T)$$, ta có thể **chắc chắn** rằng $$f$$ là cực đại - không cần thử thêm.

**Chứng minh** sẽ được trình bày trong bài 17_02 qua thuật toán Ford-Fulkerson: thuật toán này khi kết thúc luôn cho ra một luồng và một lát cắt với giá trị bằng nhau.

<div class="content-box example-box" markdown="1">
**Ví dụ 4**: Quay lại mạng Ví dụ 1 với luồng $$|f| = 12$$ ở Ví dụ 2.

Xét lát cắt $$S = \{s, a, b\}$$, $$T = \{t\}$$. Cạnh từ $$S$$ sang $$T$$: $$(a, t)$$ dung lượng $$7$$, $$(b, t)$$ dung lượng $$8$$. Vậy $$c(S, T) = 15$$.

Lát cắt $$S' = \{s\}$$, $$T' = \{a, b, t\}$$: $$c(S', T') = 10 + 5 = 15$$.

Cả hai lát cắt đều có dung lượng $$15$$. Có thể chứng minh không có lát cắt nào nhỏ hơn $$15$$, nên min-cut $$= 15$$.

Vậy luồng cực đại cũng $$= 15$$, và luồng $$|f| = 12$$ ở Ví dụ 2 **chưa** tối ưu. Có thể tăng thêm $$3$$ đơn vị nữa.
</div>

## 7. Ứng dụng Mở đầu

Luồng trong mạng không chỉ là toán học trừu tượng - nó là công cụ thực tiễn:

- **Mạng máy tính**: dung lượng băng thông tối đa giữa hai máy chủ.
- **Giao thông**: lưu lượng xe tối đa qua một mạng đường.
- **Phân công công việc**: ghép cặp nhân viên với công việc (bài 17_03).
- **Phân khúc ảnh** (image segmentation): tách foreground/background trong xử lý ảnh.
- **Phát hiện gian lận**: tách cộng đồng trong đồ thị giao dịch.

Mỗi ứng dụng đều có thể quy về bài toán Max-Flow bằng cách xây dựng một mạng phù hợp.

## Tổng kết

- Mạng luồng = đồ thị có hướng + dung lượng + nguồn + đích.
- Luồng phải thỏa mãn ràng buộc dung lượng và bảo toàn luồng.
- Lát cắt $$(S, T)$$ chia $$V$$ thành hai phần với $$s \in S$$, $$t \in T$$; dung lượng lát cắt là tổng dung lượng cạnh đi từ $$S$$ sang $$T$$.
- Bổ đề: $$|f| \leq c(S, T)$$ với mọi luồng và mọi lát cắt.
- **Định lý Max-Flow Min-Cut**: cận trên này là chặt - max-flow = min-cut.

## Bài tập

1. Vẽ một mạng có $$5$$ đỉnh và $$6$$ cạnh, gán dung lượng tùy ý. Tìm bằng tay một luồng có giá trị bất kỳ và kiểm tra bảo toàn luồng tại các đỉnh trung gian.
2. Trong mạng ở Ví dụ 1, tìm một luồng có giá trị $$15$$ (tối ưu).
3. Chứng minh rằng nếu mọi cạnh có dung lượng nguyên, thì luôn tồn tại luồng cực đại có giá trị nguyên (sử dụng định lý Max-Flow Min-Cut).
4. Trong một mạng, có thể có **nhiều** luồng cực đại khác nhau cùng đạt giá trị max-flow không? Nêu ví dụ.
5. Liệt kê tất cả các lát cắt $$s$$-$$t$$ của mạng ở Ví dụ 1 và tính dung lượng từng lát cắt. Lát cắt cực tiểu là gì?

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.), Chương 10 (Graphs).
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., Stein, C. (2022). *Introduction to Algorithms* (4th ed.), Chương 24 (Maximum Flow).
- Ford, L. R., Fulkerson, D. R. (1956). *Maximal Flow Through a Network*. Canadian Journal of Mathematics, 8, 399-404.
- Schrijver, A. (2003). *Combinatorial Optimization: Polyhedra and Efficiency*. Springer.
</div>
