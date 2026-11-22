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
