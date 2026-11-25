---
layout: post
title: "Rút gọn Đồ thị: IS, CLIQUE, Vertex Cover"
categories: chapter20
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Chứng minh đầy đủ các phép rút gọn 3SAT≤ₚIS, IS≡CLIQUE và IS≤ₚVC với tính đúng đắn hai chiều và thời gian đa thức."
---

<div class="textbook-epigraph" markdown="1">

"One careful graph gadget unlocks a family of NP-complete problems."

<span class="epigraph-attribution">— Combinatorial reduction craft</span>

</div>

Tập độc lập (Independent Set), Clique và Phủ đỉnh (Vertex Cover) là ba bài toán đồ thị cốt lõi, làm nền cho nhiều chứng minh độ khó NP-complete khác.

Làm sao biến một công thức logic khô khan đầy dấu $$\lor, \land, \neg$$ thành một đồ thị gồm các đỉnh và cạnh? Phép rút gọn kinh điển từ `3SAT` sang `INDEPENDENT-SET` (tập độc lập), rồi nối tiếp sang `CLIQUE` (đồ thị đầy đủ con) và `VERTEX-COVER` (tập phủ đỉnh) là kiệt tác đầu tiên của nghệ thuật **thiết kế mảnh ghép (gadget design)** trong lý thuyết độ phức tạp.

## Kiến thức cần nhớ: Chuỗi rút gọn Tam giác Vàng trên Đồ thị

1. **Rút gọn $$\mathrm{3SAT} \le_p \mathrm{IS}$$ (Mỗi mệnh đề = 1 tam giác)**:
   Với $$m$$ mệnh đề, dựng $$m$$ tam giác (mỗi tam giác 3 đỉnh ứng với 3 literal). Nối cạnh xung đột giữa mọi cặp literal mâu thuẫn $$x_i$$ và $$\neg x_i$$. Chọn được tập độc lập cỡ $$m$$ tương đương chọn đúng 1 literal Đúng trong mỗi mệnh đề mà không có hai literal nào mâu thuẫn nhau!
2. **Đồ thị bù $$\overline{G}$$ nối $$\mathrm{IS} \equiv \mathrm{CLIQUE}$$**:
   Tập đỉnh $$S$$ là tập độc lập trong $$G$$ (không có cạnh nào giữa các đỉnh trong $$S$$) **khi và chỉ khi** $$S$$ là một clique trong đồ thị bù $$\overline{G}$$ (mọi cặp đỉnh trong $$S$$ đều có cạnh nối).
3. **Quan hệ bù tập đỉnh nối $$\mathrm{IS} \equiv \mathrm{VC}$$**:
   $$S$$ là tập độc lập trong $$G = (V, E)$$ **khi và chỉ khi** $$V \setminus S$$ là tập phủ đỉnh (chạm ít nhất một đầu mút của mọi cạnh). Do đó: $$\alpha(G) + \tau(G) = \vert V \vert$$.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** $$3\mathrm{SAT}\le_p\mathrm{IS}$$.
- **Chứng minh** sự tương đương IS ≡ CLIQUE thông qua đồ thị bù.
- **Chứng minh** $$\mathrm{IS}\le_p\mathrm{VC}$$.

</div>

## Rút gọn $$3\mathrm{SAT}\le_p\mathrm{INDEPENDENT\text{-}SET}$$

**Phép dựng:** Cho công thức 3CNF gồm $$m$$ mệnh đề $$C_j=\{\ell_{j1},\ell_{j2},\ell_{j3}\}$$. Ta dựng đồ thị $$G$$ gồm $$3m$$ đỉnh $$v_{j,r}$$ (mỗi đỉnh ứng với một literal trong một mệnh đề) với hai loại cạnh: (i) nối thành tam giác giữa 3 đỉnh trong cùng một mệnh đề, và (ii) nối mọi cặp đỉnh ứng với hai literal mâu thuẫn nhau (như $$x$$ và $$\neg x$$) thuộc hai mệnh đề khác nhau. Đặt ngưỡng kích thước tập độc lập $$k=m$$.

**Tính đúng đắn:**  
- *Nếu $$\varphi$$ thỏa mãn được:* trong mỗi mệnh đề chọn đúng một literal nhận giá trị đúng. Tập $$m$$ đỉnh tương ứng không chứa hai đỉnh cùng tam giác và không chứa cặp literal mâu thuẫn, nên là một tập độc lập kích thước $$m$$.  
- *Nếu $$G$$ có tập độc lập kích thước $$m$$:* vì mỗi tam giác đóng góp tối đa 1 đỉnh nên mỗi mệnh đề có đúng 1 đỉnh được chọn. Gán các literal tương ứng bằng đúng là nhất quán vì giữa các đỉnh được chọn không có cạnh mâu thuẫn; do đó $$\varphi$$ thỏa mãn được.

**Thời gian dựng:** $$O(m^2)$$, là thời gian đa thức.

<div class="textbook-theorem" markdown="1">

**Định lý.** $$3\mathrm{SAT}\le_p\mathrm{IS}$$. Vì $$\mathrm{IS}\in NP$$, suy ra Independent Set là bài toán NP-complete.

</div>

## Tương đương IS ≡ CLIQUE

Xét đồ thị bù $$\overline{G}$$ (có cạnh giữa hai đỉnh khi và chỉ khi $$G$$ không có cạnh giữa chúng). Khi đó một tập đỉnh $$S$$ là tập độc lập trong $$G$$ khi và chỉ khi $$S$$ là một clique trong $$\overline{G}$$. Phép biến đổi $$f(G,k)=(\overline{G},k)$$ chạy trong thời gian $$O(n^2)$$ và khả nghịch, chứng minh $$\mathrm{IS}\le_p\mathrm{CLIQUE}$$ và ngược lại.

## Rút gọn $$\mathrm{IS}\le_p\mathrm{VC}$$

<div class="textbook-lemma" markdown="1">

**Bổ đề.** Tập đỉnh $$S$$ là một tập độc lập của $$G=(V,E)$$ khi và chỉ khi phần bù $$V\setminus S$$ là một phủ đỉnh (*vertex cover*) của $$G$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** $$S$$ là tập độc lập tương đương với việc không có cạnh nào có cả hai đầu mút cùng thuộc $$S$$, điều này tương đương với việc mọi cạnh đều có ít nhất một đầu mút thuộc $$V\setminus S$$ — tức là $$V\setminus S$$ là phủ đỉnh.

</div>

**Phép rút gọn:** ánh xạ $$(G,k)\mapsto(G,n-k)$$ trong thời gian đa thức. Khi đó $$G$$ có tập độc lập kích thước $$\ge k$$ khi và chỉ khi $$G$$ có phủ đỉnh kích thước $$\le n-k$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Vertex Cover (VC) là bài toán NP-complete.

</div>

### Thử nghiệm: tập độc lập, clique và phủ đỉnh

Quan sát mối liên hệ qua phép lấy phần bù giữa tập độc lập cực đại, clique của đồ thị bù và phủ đỉnh cực tiểu:

<div class="interactive-demo" markdown="1">
<div data-demo="reduction-explainer" data-tab="clique"></div>
</div>
<script src="{{ '/public/js/explainers/complexity-explainer.js' | relative_url }}"></script>

### Giải thích: Dựng tay đồ thị cho công thức 3SAT có 2 mệnh đề

Xét công thức $$\varphi = (x_1 \lor \neg x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor x_3)$$ ($$m = 2$$ mệnh đề):
1. **Dựng 2 tam giác (6 đỉnh):**
   - Tam giác 1: đỉnh $$a_1(x_1)$$, $$a_2(\neg x_2)$$, $$a_3(x_3)$$ (nối đôi một với nhau).
   - Tam giác 2: đỉnh $$b_1(\neg x_1)$$, $$b_2(x_2)$$, $$b_3(x_3)$$ (nối đôi một với nhau).
2. **Nối cạnh xung đột giữa 2 tam giác:**
   - Nối $$a_1(x_1)$$ với $$b_1(\neg x_1)$$ (mâu thuẫn $$x_1$$ và $$\neg x_1$$).
   - Nối $$a_2(\neg x_2)$$ với $$b_2(x_2)$$ (mâu thuẫn $$\neg x_2$$ và $$x_2$$).
3. **Tìm tập độc lập cỡ $$k = m = 2$$:**
   - Chọn $$a_1(x_1)$$ ở Tam giác 1 và $$b_2(x_2)$$ ở Tam giác 2: không có cạnh nối giữa $$a_1$$ và $$b_2$$! Suy ra phép gán thỏa mãn $$x_1 = \text{True}, x_2 = \text{True}$$ ($$x_3$$ tùy ý).
   - Ngược lại, không thể chọn đồng thời $$a_1(x_1)$$ và $$b_1(\neg x_1)$$ vì giữa chúng có cạnh xung đột!
4. **Kiểm tra ngay sang `VERTEX-COVER`:** Vì $$\vert V \vert = 6$$ và có tập độc lập $$S = \{a_1, b_2\}$$ cỡ $$2$$, phần bù $$V \setminus S = \{a_2, a_3, b_1, b_3\}$$ cỡ $$6 - 2 = \mathbf{4}$$ chắc chắn là một tập phủ đỉnh hợp lệ của đồ thị!

## Bài tập

1. Vẽ đồ thị gadget tương ứng với công thức gồm 2 mệnh đề $$(x\lor y\lor z)\land(\neg x\lor y\lor w)$$.
2. Chứng minh rằng nếu bỏ qua các cạnh nối cặp literal mâu thuẫn thì phép dựng rút gọn $$3\mathrm{SAT}\le_p\mathrm{IS}$$ sẽ sai.
3. Trình bày đầy đủ suy luận chứng minh CLIQUE là NP-complete từ IS.

## Tài liệu đọc thêm

Sipser; CLRS; Garey–Johnson.

## Tóm tắt

Chuỗi rút gọn 3SAT → IS → CLIQUE và VC minh họa khuôn mẫu kinh điển để chứng minh tính NP-complete cho các bài toán trên đồ thị.

**Bài tiếp theo:** 20.10 — Chu trình Hamilton và bài toán TSP quyết định.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=u5W32YxmnL8">NP-Complete Reductions:  Clique, Independent Set, Vertex Cover, and Dominating Set</a> — Algorithms with Attitude, tiếng Anh. Giới thiệu họ rút gọn giữa Clique, Independent Set và Vertex Cover.
- <a href="https://www.youtube.com/watch?v=j6-e_iuE9fA">3SAT to independent set reduction</a> — Nickvash Kani, tiếng Anh. Chi tiết phép rút gọn từ 3SAT sang tập độc lập.
- <a href="https://www.youtube.com/watch?v=9rzrJ4rKwPw">Independent set to vertex cover reduction</a> — Nickvash Kani, tiếng Anh. Phép rút gọn từ tập độc lập sang phủ đỉnh.
