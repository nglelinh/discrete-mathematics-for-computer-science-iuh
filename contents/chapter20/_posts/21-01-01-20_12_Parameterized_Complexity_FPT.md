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
