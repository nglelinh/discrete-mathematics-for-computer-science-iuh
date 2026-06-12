---
layout: post
title: "PageRank và Phân tích Mạng có hướng"
categories: chapter17
date: 2021-01-01
order: 4
required: true
lang: en
---

# PageRank và Phân tích Mạng có hướng

Năm 1998, hai nghiên cứu sinh tại Stanford - **Larry Page** và **Sergey Brin** - công bố một thuật toán xếp hạng trang web mà sau này trở thành nền tảng của Google. Ý tưởng cốt lõi đơn giản đến bất ngờ: một trang web **quan trọng** không phải vì nó nói rằng nó quan trọng, mà vì **nhiều trang quan trọng khác liên kết đến nó**. Đây là một định nghĩa **đệ quy** - và toàn bộ vẻ đẹp của PageRank nằm ở việc đệ quy này có nghiệm duy nhất và có thể tính được bằng đại số tuyến tính cơ bản.

Bài này giới thiệu PageRank như một ví dụ minh họa cho một loạt khái niệm về **đồ thị có hướng nâng cao** (advanced directed graphs): bước ngẫu nhiên trên đồ thị (random walks), ma trận chuyển trạng thái, hội tụ về phân phối dừng. Những công cụ này không chỉ giải thích cách Google hoạt động mà còn xuất hiện trong phân tích mạng xã hội, hệ thống đề xuất, mô hình bệnh dịch và nhiều lĩnh vực khác.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Mô hình hóa** một mạng web (hoặc mạng xã hội) bằng đồ thị có hướng và ma trận chuyển trạng thái.
- **Định nghĩa** bước ngẫu nhiên trên đồ thị và phân phối dừng.
- **Phát biểu** công thức PageRank và giải thích vai trò của hệ số damping.
- **Tính** PageRank cho mạng nhỏ bằng phương pháp lặp.
- **Nhận diện** các ứng dụng của random walk trong khoa học mạng.

**Từ khóa**: đồ thị có hướng (directed graph), ma trận kề (adjacency matrix), ma trận chuyển trạng thái (transition matrix), bước ngẫu nhiên (random walk), phân phối dừng (stationary distribution), PageRank, damping factor, hội tụ (convergence).

## 1. Đồ thị có hướng và Ma trận Kề

Cho đồ thị có hướng $$G = (V, E)$$ với $$V = \{v_1, \ldots, v_n\}$$. **Ma trận kề** $$A \in \{0, 1\}^{n \times n}$$:

$$A_{ij} = \begin{cases} 1 & \text{nếu } (v_i, v_j) \in E, \\ 0 & \text{nếu không.} \end{cases}$$

Lưu ý quy ước: $$A_{ij} = 1$$ nếu có cạnh **từ $$v_i$$ sang $$v_j$$**. Một số sách dùng quy ước ngược.

**Bậc ra** (out-degree) của $$v_i$$: $$\deg^+(v_i) = \sum_j A_{ij}$$.

**Bậc vào** (in-degree) của $$v_j$$: $$\deg^-(v_j) = \sum_i A_{ij}$$.

## 2. Bước Ngẫu nhiên trên Đồ thị

Tưởng tượng một "lướt web" bắt đầu ở một trang ngẫu nhiên. Tại mỗi bước, người đó chọn một liên kết ngẫu nhiên trên trang hiện tại và đi đến trang đó. Đây là **bước ngẫu nhiên** (random walk) trên đồ thị web.

**Ma trận chuyển trạng thái** $$M \in [0, 1]^{n \times n}$$:

$$M_{ij} = \begin{cases} \dfrac{1}{\deg^+(v_i)} & \text{nếu } (v_i, v_j) \in E, \\ 0 & \text{nếu không.} \end{cases}$$

Mỗi hàng của $$M$$ tổng bằng $$1$$ - đây là **ma trận stochastic** (xác suất). Phần tử $$M_{ij}$$ = xác suất nhảy từ $$v_i$$ sang $$v_j$$ trong một bước.

Nếu $$\boldsymbol{x}^{(k)} \in \mathbb{R}^n$$ là vector xác suất sau bước $$k$$ ($$x_i^{(k)}$$ = xác suất đang ở $$v_i$$), thì

$$\boldsymbol{x}^{(k+1)} = M^T \boldsymbol{x}^{(k)}.$$

## 3. Phân phối Dừng

**Phân phối dừng** (stationary distribution) là vector $$\boldsymbol{\pi}$$ với:

$$\boldsymbol{\pi} = M^T \boldsymbol{\pi}, \quad \sum_i \pi_i = 1, \quad \pi_i \geq 0.$$

Tức là phân phối **không đổi** qua một bước random walk. Toán học: $$\boldsymbol{\pi}$$ là vector riêng của $$M^T$$ ứng với trị riêng $$1$$.

**Định lý Perron-Frobenius**: với ma trận stochastic **không phân rã** (irreducible) và **không tuần hoàn** (aperiodic), phân phối dừng tồn tại **duy nhất**, và bước ngẫu nhiên hội tụ về nó từ mọi phân phối khởi đầu.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: Mạng nhỏ với $$3$$ trang:

- Cạnh: $$1 \to 2$$, $$1 \to 3$$, $$2 \to 3$$, $$3 \to 1$$.
- Bậc ra: $$\deg^+(1) = 2, \deg^+(2) = 1, \deg^+(3) = 1$$.

Ma trận chuyển trạng thái:

$$M = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}.$$

Giải $$M^T \boldsymbol{\pi} = \boldsymbol{\pi}$$:

$$\begin{cases} \pi_3 = \pi_1 \\ \pi_1 / 2 = \pi_2 \\ \pi_1 / 2 + \pi_2 = \pi_3 \end{cases} \implies \pi_1 = \pi_3, \pi_2 = \pi_1 / 2.$$

Chuẩn hóa: $$\pi_1 + \pi_2 + \pi_3 = 2\pi_1 + \pi_1/2 = 5\pi_1/2 = 1 \implies \pi_1 = 2/5$$.

Vậy $$\boldsymbol{\pi} = (2/5, 1/5, 2/5)$$. Trang $$1$$ và $$3$$ "quan trọng" như nhau, trang $$2$$ có xác suất ghé thăm bằng nửa.
</div>

## 4. Vấn đề với Web Thực tế

Web thực có hai vấn đề mà random walk thuần túy không xử lý được:

**Vấn đề 1 - Dangling nodes**: có trang không liên kết ra ngoài ($$\deg^+ = 0$$). Người lướt sẽ "bị kẹt".

**Vấn đề 2 - Spider traps**: có cụm trang chỉ liên kết nhau, không liên kết ra ngoài. Random walk vào đó sẽ không bao giờ thoát.

Vì hai vấn đề này, $$M$$ không phải irreducible, và phân phối dừng không duy nhất hoặc không tồn tại.

## 5. PageRank: Damping Factor

**Ý tưởng** Page-Brin: thêm vào mô hình một xác suất nhỏ rằng tại mỗi bước, người lướt **nhảy đến một trang ngẫu nhiên bất kỳ** (không theo link). Đây là "**teleportation**".

Cho hệ số damping $$d \in (0, 1)$$ (thường $$d = 0.85$$). Ma trận PageRank:

$$\tilde{M} = d \cdot M + (1 - d) \cdot \frac{1}{n} \mathbf{J},$$

trong đó $$\mathbf{J}$$ là ma trận toàn $$1$$.

Phương trình PageRank:

$$\boldsymbol{\pi} = \tilde{M}^T \boldsymbol{\pi},$$

hoặc viết theo từng phần tử:

$$PR(v_j) = \frac{1 - d}{n} + d \sum_{v_i \to v_j} \frac{PR(v_i)}{\deg^+(v_i)}.$$

<div class="content-box insight-box" markdown="1">
**Giải thích trực giác**:

- $$\dfrac{1 - d}{n}$$: "điểm cơ sở" mọi trang nhận được (do teleportation).
- Phần tổng: điểm nhận từ các trang liên kết đến, chia đều theo bậc ra của nguồn.
- Một trang **quan trọng** = nhận được nhiều điểm từ các trang khác cũng quan trọng.
</div>

**Định lý**: với $$d < 1$$, ma trận $$\tilde{M}$$ là irreducible và aperiodic, nên PageRank tồn tại và duy nhất.

## 6. Phương pháp Lặp Power Iteration

Khó giải trực tiếp phương trình $$\boldsymbol{\pi} = \tilde{M}^T \boldsymbol{\pi}$$ trên web có hàng tỷ trang. Thay vào đó, dùng **power iteration**:

```
Khởi tạo π^(0) = (1/n, 1/n, ..., 1/n)
For k = 0, 1, 2, ...:
    π^(k+1) = ~M^T · π^(k)
    if ||π^(k+1) - π^(k)|| < ε then break
return π^(k+1)
```

**Tốc độ hội tụ**: số bước cần $$\approx O(\log(1/\varepsilon) / (1 - d))$$. Với $$d = 0.85$$ và $$\varepsilon = 10^{-6}$$, khoảng $$50-100$$ lần lặp.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Mạng Ví dụ 1 với $$d = 0.85$$.

$$\tilde{M} = 0.85 \cdot M + 0.15 \cdot \frac{1}{3} \mathbf{J}.$$

Khởi tạo $$\boldsymbol{\pi}^{(0)} = (1/3, 1/3, 1/3)$$.

Sau vài lần lặp, hội tụ đến $$\boldsymbol{\pi} \approx (0.388, 0.215, 0.397)$$.

Trang $$3$$ có PageRank cao nhất - vì có hai trang link đến ($$1$$ và $$2$$), nhiều hơn trang $$1$$ (một trang link đến).
</div>

## 7. Các Phân tích Mạng Khác

PageRank chỉ là một trong nhiều **đo lường trung tâm** (centrality measures):

- **Degree centrality**: số liên kết của một đỉnh.
- **Betweenness centrality**: tỷ lệ đường đi ngắn nhất đi qua đỉnh.
- **Closeness centrality**: nghịch đảo khoảng cách trung bình đến các đỉnh khác.
- **Eigenvector centrality**: vector riêng của ma trận kề - PageRank là một biến thể có damping.
- **HITS** (Kleinberg 1999): tách đỉnh thành "hub" và "authority", lặp luân phiên.

Mỗi đo lường nêu bật một khía cạnh khác nhau của tầm quan trọng - tùy bài toán mà ta chọn phù hợp.

## 8. Ứng dụng Mở rộng

PageRank và random walk được dùng rộng rãi ngoài tìm kiếm web:

- **Mạng xã hội**: xếp hạng người ảnh hưởng trên Twitter, Facebook.
- **Hệ thống đề xuất**: gợi ý phim/sản phẩm dựa trên đồ thị user-item.
- **Sinh học**: xếp hạng protein quan trọng trong mạng tương tác protein-protein.
- **Khoa học**: PageRank cho mạng trích dẫn (citation network), đánh giá ảnh hưởng bài báo.
- **Phân tích văn bản**: TextRank cho tóm tắt văn bản (đỉnh = câu, cạnh = độ tương đồng).
- **Phát hiện gian lận**: nhận diện cụm tài khoản giả lập trên ngân hàng/mạng xã hội.

## Tổng kết

- Đồ thị có hướng + ma trận chuyển trạng thái = mô hình bước ngẫu nhiên.
- Phân phối dừng $$\boldsymbol{\pi}$$ thỏa $$\boldsymbol{\pi} = M^T \boldsymbol{\pi}$$ - không đổi qua một bước.
- Web thực có dangling nodes và spider traps; damping factor $$d$$ giải quyết bằng teleportation.
- PageRank: $$PR(v) = (1-d)/n + d \sum_{u \to v} PR(u) / \deg^+(u)$$.
- Tính bằng power iteration - chỉ vài chục lần lặp với $$d = 0.85$$.
- Mô hình mở rộng cho nhiều lĩnh vực ngoài web: mạng xã hội, sinh học, NLP.

## Bài tập

1. Tính PageRank bằng tay cho mạng $$4$$ đỉnh: $$1 \to 2, 1 \to 3, 2 \to 3, 3 \to 1, 3 \to 4, 4 \to 1$$. Dùng $$d = 0.85$$ và lặp $$5$$ bước từ phân phối đều.
2. Một spider trap trong web: vẽ một ví dụ đồ thị có hướng $$4$$ đỉnh có spider trap, và giải thích tại sao random walk thuần (không damping) không cho phân phối dừng.
3. Chứng minh: nếu $$d = 1$$ và đồ thị có dangling node, phương trình PageRank không có nghiệm duy nhất.
4. Lập trình (Python/Java): cài đặt PageRank bằng power iteration cho đồ thị có hướng cho trước. Kiểm tra với đồ thị Wikipedia con (ví dụ $$100$$ trang).
5. So sánh PageRank với betweenness centrality trên một mạng xã hội mẫu nhỏ ($$10-20$$ nút). Khi nào hai đo lường này khác biệt rõ?

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Page, L., Brin, S., Motwani, R., Winograd, T. (1999). *The PageRank Citation Ranking: Bringing Order to the Web*. Stanford InfoLab Technical Report.
- Kleinberg, J. M. (1999). *Authoritative Sources in a Hyperlinked Environment*. Journal of the ACM.
- Easley, D., Kleinberg, J. (2010). *Networks, Crowds, and Markets: Reasoning About a Highly Connected World*. Cambridge.
- Newman, M. (2018). *Networks* (2nd ed.). Oxford University Press.
</div>
