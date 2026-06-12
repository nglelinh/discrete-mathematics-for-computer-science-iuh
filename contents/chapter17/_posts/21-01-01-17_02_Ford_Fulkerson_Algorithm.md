---
layout: post
title: "Thuật toán Ford-Fulkerson"
categories: chapter17
date: 2021-01-01
order: 2
required: true
lang: en
---

# Thuật toán Ford-Fulkerson

Ở bài trước, ta đã **chứng minh** sự tồn tại của luồng cực đại qua định lý Max-Flow Min-Cut. Nhưng làm sao để **tìm** nó? Một cách ngây thơ là thử mọi cách phân bổ luồng có thể - nhưng số lượng đó nhiều vô hạn nếu dung lượng là số thực. Ngay cả khi dung lượng nguyên, không gian tìm kiếm vẫn quá lớn.

Thuật toán **Ford-Fulkerson** (1956) đưa ra một ý tưởng đơn giản nhưng mạnh: bắt đầu từ luồng $$0$$, lặp lại việc **tìm một con đường còn dư dung lượng** từ nguồn đến đích và **đẩy thêm luồng** qua con đường đó. Khi không còn con đường nào nữa, ta đã có luồng cực đại. Toàn bộ vẻ đẹp lý thuyết của Max-Flow Min-Cut sẽ xuất hiện như một **hệ quả** của thuật toán này.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** đồ thị thặng dư (residual graph) và đường tăng luồng (augmenting path).
- **Thực thi từng bước** thuật toán Ford-Fulkerson trên một mạng nhỏ.
- **Giải thích** vì sao thuật toán đúng và biết khi nào nó kết thúc.
- **Phân biệt** Ford-Fulkerson tổng quát và biến thể Edmonds-Karp dùng BFS.

**Từ khóa**: đồ thị thặng dư (residual graph), dung lượng thặng dư (residual capacity), đường tăng luồng (augmenting path), Ford-Fulkerson, Edmonds-Karp.

## 1. Ý tưởng Trực giác

Trong mạng ở bài trước, giả sử ta đã đẩy $$7$$ đơn vị luồng qua cạnh $$(s, a)$$ có dung lượng $$10$$. Cạnh đó còn **dư** $$3$$ đơn vị có thể đẩy thêm. Nếu ta tìm được một con đường từ $$s$$ đến $$t$$ mà **mọi cạnh** trên đó còn dư dung lượng, ta có thể đẩy thêm luồng theo con đường đó.

Nhưng có một điều tinh tế: đôi khi để đạt luồng cực đại, ta cần **rút luồng** đã đẩy trên một cạnh và đẩy lại theo đường khác. Khái niệm **đồ thị thặng dư** dưới đây sẽ làm việc đó một cách hệ thống.

## 2. Đồ thị Thặng dư

Cho mạng $$(G, c, s, t)$$ và một luồng $$f$$. **Dung lượng thặng dư** từ $$u$$ đến $$v$$ được định nghĩa:

$$c_f(u, v) = \begin{cases} c(u, v) - f(u, v) & \text{nếu } (u, v) \in E, \\ f(v, u) & \text{nếu } (v, u) \in E, \\ 0 & \text{nếu không có cạnh nào.} \end{cases}$$

Trường hợp đầu là phần **chưa dùng** của cạnh thuận. Trường hợp thứ hai là cạnh **ngược** - ta có thể "hoàn" lại lượng luồng đã đẩy. Trường hợp cộng dồn được khi có cả $$(u, v)$$ và $$(v, u)$$ trong $$E$$.

**Đồ thị thặng dư** $$G_f$$ có cùng tập đỉnh với $$G$$ và tập cạnh

$$E_f = \{ (u, v) : c_f(u, v) > 0 \}.$$

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: Mạng có cạnh $$(s, a)$$ với $$c(s, a) = 10$$ và luồng hiện tại $$f(s, a) = 7$$.

- $$c_f(s, a) = 10 - 7 = 3$$ (đẩy thêm tối đa $$3$$ đơn vị).
- $$c_f(a, s) = 7$$ (hoàn lại tối đa $$7$$ đơn vị - cạnh ngược trong $$G_f$$).
</div>

## 3. Đường Tăng Luồng

**Định nghĩa**: Một **đường tăng luồng** (augmenting path) là một đường đi đơn từ $$s$$ đến $$t$$ trong đồ thị thặng dư $$G_f$$.

**Dung lượng đường tăng** là dung lượng thặng dư nhỏ nhất dọc theo đường:

$$\Delta = \min_{(u, v) \in P} c_f(u, v),$$

trong đó $$P$$ là tập các cạnh trên đường.

**Phép đẩy luồng**: cập nhật luồng theo công thức

$$f'(u, v) = \begin{cases} f(u, v) + \Delta & \text{nếu } (u, v) \in P \text{ và } (u, v) \in E, \\ f(v, u) - \Delta & \text{nếu } (u, v) \in P \text{ và } (v, u) \in E, \\ f(u, v) & \text{nếu không thay đổi.} \end{cases}$$

Có thể kiểm chứng $$f'$$ vẫn là luồng hợp lệ và $$|f'| = |f| + \Delta$$.

## 4. Thuật toán Ford-Fulkerson (Tổng quát)

```
Input: mạng (G, c, s, t)
Output: luồng cực đại f

1. Khởi tạo f(u, v) = 0 cho mọi (u, v) ∈ E.
2. while (tồn tại đường tăng luồng P trong G_f) do
3.     Tính Δ = min{c_f(u, v) : (u, v) ∈ P}.
4.     Cập nhật f theo P và Δ.
5. end while
6. return f.
```

**Câu hỏi**: thuật toán có **kết thúc** không? Có cho ra luồng **cực đại** không?

- Nếu dung lượng nguyên, mỗi lần lặp $$|f|$$ tăng thêm ít nhất $$1$$. Vì $$|f|$$ bị chặn trên (bởi min-cut), thuật toán kết thúc sau hữu hạn bước.
- Nếu dung lượng vô tỉ, có ví dụ (Zwick 1995) cho thấy Ford-Fulkerson có thể không kết thúc. Tuy nhiên, nếu chọn đường tăng theo BFS (Edmonds-Karp, mục 7), thuật toán luôn kết thúc.

## 5. Worked Example

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Mạng từ bài 17_01:

- Đỉnh: $$\{s, a, b, t\}$$.
- Cạnh: $$c(s, a) = 10$$, $$c(s, b) = 5$$, $$c(a, b) = 4$$, $$c(a, t) = 7$$, $$c(b, t) = 8$$.

**Lần lặp 1**: $$f = 0$$. Trong $$G_f$$, đường $$s \to a \to t$$ có $$c_f(s, a) = 10$$, $$c_f(a, t) = 7$$. $$\Delta = 7$$.

Cập nhật: $$f(s, a) = 7$$, $$f(a, t) = 7$$. $$|f| = 7$$.

**Lần lặp 2**: Đường $$s \to b \to t$$. $$c_f(s, b) = 5$$, $$c_f(b, t) = 8$$. $$\Delta = 5$$.

Cập nhật: $$f(s, b) = 5$$, $$f(b, t) = 5$$. $$|f| = 12$$.

**Lần lặp 3**: Đường $$s \to a \to b \to t$$. $$c_f(s, a) = 3$$, $$c_f(a, b) = 4$$, $$c_f(b, t) = 3$$. $$\Delta = 3$$.

Cập nhật: $$f(s, a) = 10$$, $$f(a, b) = 3$$, $$f(b, t) = 8$$. $$|f| = 15$$.

**Lần lặp 4**: Trong $$G_f$$, tất cả cạnh ra khỏi $$s$$ đã bão hòa ($$c_f(s, a) = 0$$, $$c_f(s, b) = 0$$). Không còn đường tăng. **Kết thúc**.

**Luồng cực đại** $$= 15$$. Đúng bằng min-cut đã tính ở bài 17_01.
</div>

## 6. Tính đúng đắn - Chứng minh Max-Flow Min-Cut

Giả sử thuật toán kết thúc với luồng $$f^*$$. Định nghĩa

$$S = \{v \in V : \text{tồn tại đường } s \to v \text{ trong } G_{f^*}\}, \quad T = V \setminus S.$$

Khi đó:

- $$s \in S$$ hiển nhiên.
- $$t \in T$$ vì nếu $$t \in S$$ thì còn đường tăng - mâu thuẫn với điều kiện kết thúc.

Với mọi cạnh $$(u, v) \in E$$ có $$u \in S$$ và $$v \in T$$:

- $$c_{f^*}(u, v) = 0$$, suy ra $$f^*(u, v) = c(u, v)$$ (cạnh **bão hòa**).

Với mọi cạnh $$(v, u) \in E$$ có $$v \in T$$ và $$u \in S$$:

- $$c_{f^*}(u, v) = f^*(v, u) = 0$$.

Suy ra $$|f^*| = c(S, T)$$. Kết hợp với bổ đề $$|f| \leq c(S, T)$$ cho mọi luồng, ta được

$$|f^*| = \max_f |f| = \min_{(S, T)} c(S, T) = c(S, T). \square$$

Vậy thuật toán Ford-Fulkerson không chỉ tìm ra luồng cực đại mà còn cung cấp **lát cắt cực tiểu** - chứng minh trực tiếp định lý Max-Flow Min-Cut.

## 7. Edmonds-Karp: Chọn Đường ngắn nhất

Ford-Fulkerson không quy định **chọn đường tăng nào**. Edmonds và Karp (1972) đề xuất luôn chọn đường tăng **ngắn nhất** (ít cạnh nhất) bằng BFS.

**Định lý (Edmonds-Karp 1972)**: Số lần lặp của thuật toán này là $$O(|V| \cdot |E|)$$, và mỗi lần BFS tốn $$O(|E|)$$, nên tổng độ phức tạp là

$$O(|V| \cdot |E|^2).$$

Đây là cận **đa thức** không phụ thuộc dung lượng. Trong khi Ford-Fulkerson tổng quát với dung lượng lớn có thể chạy $$O(|E| \cdot |f^*|)$$ - phụ thuộc giá trị luồng cực đại, có thể rất lớn nếu dung lượng lớn.

<div class="content-box warning-box" markdown="1">
**Bẫy quan trọng**: nếu dung lượng có giá trị rất lớn (ví dụ $$10^9$$) và thuật toán Ford-Fulkerson chọn đường tăng không cẩn thận, nó có thể tăng luồng từng $$1$$ đơn vị mỗi lần và lặp $$10^9$$ lần. Edmonds-Karp tránh được điều này bằng cách chọn đường ngắn nhất.
</div>

## 8. Các Cải tiến và Thuật toán Hiện đại

Sau Edmonds-Karp, nhiều thuật toán nhanh hơn đã ra đời:

- **Dinic's algorithm** (1970): $$O(|V|^2 |E|)$$, dùng tầng (layered network).
- **Push-Relabel** (Goldberg-Tarjan 1986): $$O(|V|^2 |E|)$$ hoặc $$O(|V|^3)$$.
- **Orlin's algorithm** (2013): $$O(|V| \cdot |E|)$$ - tối ưu trên đồ thị thưa.

Năm 2022, một bước đột phá quan trọng: **Chen et al.** công bố thuật toán max-flow chạy trong thời gian $$O(|E|^{1+o(1)})$$ - gần tuyến tính theo số cạnh.

## Tổng kết

- Đồ thị thặng dư $$G_f$$ mã hóa các thay đổi luồng còn có thể thực hiện.
- Một đường $$s \to t$$ trong $$G_f$$ là đường tăng luồng; đẩy thêm $$\Delta$$ đơn vị làm $$|f|$$ tăng $$\Delta$$.
- Ford-Fulkerson lặp: tìm đường tăng, đẩy luồng, đến khi không còn đường.
- Khi kết thúc, định nghĩa $$S$$ = đỉnh đến được từ $$s$$ trong $$G_f$$; lát cắt $$(S, V \setminus S)$$ có dung lượng bằng $$|f|$$ - chứng minh Max-Flow Min-Cut.
- Edmonds-Karp: chọn đường ngắn nhất bằng BFS, đảm bảo độ phức tạp đa thức $$O(|V| |E|^2)$$.

## Bài tập

1. Áp dụng Ford-Fulkerson cho mạng có $$c(s, a) = 16, c(s, c) = 13, c(a, b) = 12, c(c, b) = 9, c(c, d) = 14, c(d, b) = 7, c(b, t) = 20, c(d, t) = 4$$. Tìm luồng cực đại và lát cắt cực tiểu.
2. Vẽ một mạng có $$4$$ đỉnh trong đó thuật toán Ford-Fulkerson, nếu chọn đường tăng "xấu", phải lặp đến $$|f^*|$$ lần. (Gợi ý: dùng dung lượng lớn và một cạnh giữa có dung lượng $$1$$.)
3. Chứng minh chi tiết bổ đề: nếu mọi dung lượng đều là số nguyên, mọi luồng tạo ra bởi Ford-Fulkerson cũng là số nguyên (định lý tính nguyên).
4. Đối với mạng có $$|V| = n$$ và $$|E| = m$$, viết pseudocode hoàn chỉnh của Edmonds-Karp dùng BFS.
5. Giải thích vì sao việc thêm cạnh ngược trong $$G_f$$ là cần thiết (xây ví dụ mà nếu không có cạnh ngược, thuật toán sẽ kẹt ở luồng dưới tối ưu).

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Ford, L. R., Fulkerson, D. R. (1956). *Maximal Flow Through a Network*. Canadian Journal of Mathematics.
- Edmonds, J., Karp, R. M. (1972). *Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems*. Journal of the ACM.
- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.), Chương 24.
- Chen, L. et al. (2022). *Maximum Flow and Minimum-Cost Flow in Almost-Linear Time*. FOCS 2022.
</div>
