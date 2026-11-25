---
layout: post
title: "Parameterized Complexity và FPT"
categories: chapter20
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "Độ phức tạp tham số hóa (FPT so với XP), chứng minh cây tìm kiếm 2ᵏ·poly(n) cho Vertex Cover, kỹ thuật kernelization, lớp W[1] với bài toán Clique và treewidth."
---

<div class="textbook-epigraph" markdown="1">

"n is large, k is small — that is the FPT contract."

<span class="epigraph-attribution">— Downey & Fellows spirit</span>

</div>

Độ phức tạp tham số hóa tách phần tăng trưởng hàm mũ khỏi kích thước đầu vào $$n$$: thuật toán có thời gian $$f(k)n^{O(1)}$$ vẫn thực thi nhanh khi tham số cấu trúc $$k$$ nhỏ (như kích thước lời giải hoặc *treewidth*), ngay cả khi $$n$$ rất lớn.

Thuật toán xấp xỉ đánh đổi độ chính xác để lấy tốc độ. Còn một lối thoát tinh tế thứ hai giữ nguyên **nghiệm chính xác 100%** cho bài toán NP-hard: **Độ phức tạp Tham số hóa (Parameterized Complexity)**. Ý tưởng cốt lõi: thay vì đo độ phức tạp chỉ theo một biến kích thước $$n$$, hãy tách riêng một tham số cấu trúc $$k$$ (như kích thước nghiệm cần tìm hoặc độ rộng cây) và **giam toàn bộ sự bùng nổ hàm mũ vào riêng $$k$$**, để phần phụ thuộc $$n$$ vẫn là đa thức nhỏ gọn!

## Bản đồ kiến thức nền: Ba trụ cột của Độ phức tạp Tham số hóa & FPT

1. **Lớp FPT (Fixed-Parameter Tractable — $$f(k) \cdot n^{O(1)}$$)**:
   Khác hẳn $$O(n^k)$$ (khi $$k = 10, n = 1000$$ thì $$1000^{10} = 10^{30}$$ vô phương cứu chữa), thuật toán FPT kiểu $$O(2^k \cdot n)$$ với $$k = 10, n = 1000$$ chỉ mất khoảng $$10^6$$ phép tính (chạy dưới 1 mili-giây!).
2. **Hai kỹ thuật thiết kế FPT kinh điển (Bounded Search Tree & Kernelization)**:
   - *Cây tìm kiếm bị chặn:* Với `Vertex Cover`, mọi cạnh $$(u,v)$$ bắt buộc phải chọn $$u$$ hoặc $$v$$ → rẽ 2 nhánh, mỗi nhánh giảm $$k$$ đi 1 → cây sâu tối đa $$k$$, tổng chỉ $$O(2^k \cdot (V+E))$$!
   - *Rút gọn hạt nhân (Kernelization):* Áp dụng quy tắc tiền xử lý đa thức để co đồ thị khổng lồ xuống "hạt nhân" cỡ chỉ phụ thuộc $$k$$ (ví dụ quy tắc Buss cho `Vertex Cover` thu gọn còn tối đa $$k^2$$ cạnh!).
3. **Phân cấp $$W[1]$$ & Độ rộng cây (Treewidth)**:
   Không phải bài nào cũng có thuật toán FPT: `CLIQUE` là $$W[1]$$-complete (khó có thể giải trong $$f(k) \cdot n^{O(1)}$$). Tuy nhiên, với các đồ thị giống cây (treewidth $$tw$$ nhỏ), định lý Courcelle cho phép giải rất nhiều bài toán NP-hard trong thời gian tuyến tính theo $$n$$!

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** lớp FPT (*Fixed-Parameter Tractable*).
- **Chứng minh** thuật toán FPT cho Vertex Cover chạy trong $$O(2^k n^{O(1)})$$.
- **Phân biệt** FPT với XP và nêu ý nghĩa của tính W[1]-hard.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

Cho bài toán đi kèm tham số $$k$$:

- **FPT** (*Fixed-Parameter Tractable*): tồn tại thuật toán chạy trong thời gian $$f(k)\cdot n^{O(1)}$$, với $$f$$ là hàm tính được chỉ phụ thuộc vào $$k$$ (số mũ của $$n$$ không phụ thuộc $$k$$).
- **XP**: thời gian chạy có dạng $$n^{g(k)}$$ — yếu hơn nhiều vì bậc đa thức theo $$n$$ tăng theo $$k$$.

</div>

## Thuật toán cây tìm kiếm cho Vertex Cover

```text
VC(G,k):
  if k<0: No
  if no edges: Yes
  if k=0 and edges remain: No
  pick edge {u,v}
  return VC(G-u,k-1) OR VC(G-v,k-1)
```

<div class="textbook-theorem" markdown="1">

**Định lý.** Thuật toán trên giải đúng bài toán Vertex Cover tham số hóa và chạy trong thời gian $$O(2^k\cdot\mathrm{poly}(n))$$.

</div>

**Tính đúng đắn:** với mọi cạnh $$\{u,v\}$$, bất kỳ phủ đỉnh hợp lệ nào cũng phải chứa ít nhất một trong hai đỉnh $$u$$ hoặc $$v$$; lập luận quy nạp theo $$k$$ khẳng định phép phân nhánh không bỏ sót nghiệm.  
**Thời gian chạy:** cây đệ quy nhị phân có độ sâu tối đa $$k$$ nên có không quá $$2^{k+1}$$ nút, và mỗi nút thực hiện thao tác trong thời gian đa thức theo $$n$$. $$\square$$

## Kỹ thuật rút gọn hạt nhân (*Kernelization*)

Theo quy tắc Buss cho Vertex Cover, mọi đỉnh có bậc lớn hơn $$k$$ bắt buộc phải thuộc phủ đỉnh kích thước $$\le k$$ (nếu không thì phải chọn hơn $$k$$ đỉnh kề của nó). Sau khi tiền xử lý trong thời gian đa thức và loại các đỉnh cô lập, đồ thị còn lại có kích thước chỉ phụ thuộc vào $$k$$ — cụ thể $$O(k^2)$$ (và có thể giảm sâu hơn bằng quy hoạch tuyến tính).

## Lớp W[1] và bài toán Clique

Khác với Vertex Cover, bài toán Clique tham số hóa theo kích thước $$k$$ là **W[1]-complete** — được tin là không thuộc FPT (trừ khi $$\mathrm{FPT}=\mathrm{W}[1]$$). Xem thêm Cygan et al. và Downey–Fellows.

## Độ rộng cây (*Treewidth*)

Nhiều bài toán biểu diễn được bằng logic bậc hai đơn ngôi (MSO) trên đồ thị có *treewidth* $$w$$ đều giải được trong thời gian $$f(w)n$$ theo định lý Courcelle; tuy hằng số lý thuyết rất lớn, quy hoạch động trực tiếp trên phân rã cây thường đạt $$2^{O(w)}n^{O(1)}$$ trong thực hành.

### Khung giải thích (nên đọc chậm): Chạy tay quy tắc Buss (Kernelization) thu gọn đồ thị `Vertex Cover`

Giả sử bạn cần kiểm tra xem một đồ thị khổng lồ $$G$$ có **10.000 đỉnh** có tồn tại tập phủ đỉnh cỡ $$k = 5$$ hay không. Quy tắc Buss làm hai bước cực đơn giản:
1. **Quy tắc đỉnh bậc cao:** Nếu có đỉnh $$v$$ nào có bậc $$\deg(v) > k$$ (tức $$\ge 6$$ cạnh nối vào $$v$$), thì **bắt buộc phải chọn $$v$$ vào tập phủ đỉnh**! (Vì nếu không chọn $$v$$, ta phải chọn toàn bộ $$\ge 6$$ hàng xóm của $$v$$, vượt ngay ngân sách $$k = 5$$!). Chọn $$v$$, xóa $$v$$ cùng các cạnh kề nó, và giảm $$k \leftarrow k - 1$$.
2. **Xóa đỉnh cô lập:** Mọi đỉnh bậc `0` không phủ cạnh nào nên xóa bỏ an toàn.
3. **Kiểm tra ngưỡng dừng:** Sau khi không còn đỉnh nào bậc $$> k'$$, mỗi đỉnh được chọn phủ tối đa $$k'$$ cạnh, nên nếu đồ thị còn lại có **nhiều hơn $$(k')^2$$ cạnh** (ví dụ $$> 25$$ cạnh) thì lập tức kết luận **KHÔNG có nghiệm**!

Từ đồ thị 10.000 đỉnh ban đầu, quy tắc Buss nén bài toán xuống một hạt nhân nhỏ xíu tối đa **25 cạnh** trong vài mili-giây trước khi chạy tìm kiếm!

## Bài tập

1. Viết đầy đủ chứng minh tính đúng đắn và độ phức tạp cho thuật toán VC-FPT.
2. Phân tích cải tiến phân nhánh khi ưu tiên chọn đỉnh có bậc $$\ge 3$$ (rẽ nhánh chọn đỉnh đó hoặc toàn bộ các đỉnh kề của nó).
3. Đọc chi tiết một chứng minh hạt nhân hóa (quy tắc Buss).

## Tài liệu đọc thêm

Cygan et al., *Parameterized Algorithms*; kỷ yếu hội nghị IPEC.

## Tóm tắt

Lớp FPT cô lập bùng nổ tổ hợp vào tham số $$k$$ (như cây tìm kiếm $$2^k$$ và hạt nhân $$O(k^2)$$ cho Vertex Cover), trong khi tính W[1]-hard đóng vai trò tương tự NP-hard để chỉ ra bài toán khó ngay cả khi tham số hóa.

**Bài tiếp theo:** 20.13 — ETH, độ phức tạp mịn (*fine-grained*) và độ khó trường hợp trung bình.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dxEfqyViCJI">Fixed Parameter Tractability - Intro to Theoretical Computer Science</a> — Udacity, tiếng Anh. Giới thiệu khái niệm FPT với thời gian $$f(k)\cdot\mathrm{poly}(n)$$.
- <a href="https://www.youtube.com/watch?v=kclZXaEqPjo">Fixed Parameter Tractability</a> — Alex Singh, tiếng Anh. Giải thích định nghĩa khả giải theo tham số cố định.
