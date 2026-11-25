---
layout: post
title: "Rút gọn SAT ≤ₚ 3SAT"
categories: chapter20
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Chứng minh đầy đủ phép rút gọn SAT≤ₚ3SAT bằng kỹ thuật chuẩn hóa các mệnh đề có 1, 2 và ≥4 literal, qua đó khẳng định 3SAT là NP-complete."
---

<div class="textbook-epigraph" markdown="1">

"3SAT is the workhorse source problem for combinatorial reductions."

<span class="epigraph-attribution">— Karp style</span>

</div>

Phần lớn các phép chứng minh NP-complete trên đồ thị đều xuất phát từ **3SAT**. Bài học này chứng minh $$3\mathrm{SAT}$$ là NP-complete dựa trên định lý Cook–Levin bằng phép rút gọn trực tiếp từ SAT.

Định lý Cook–Levin cho ta `SAT` là NP-complete, nhưng một công thức CNF tổng quát có thể chứa những mệnh đề dài hàng trăm literal, rất khó dùng để thiết kế các "mảnh ghép đồ thị" (gadget). Chỉ cần chuẩn hóa sao cho **mọi mệnh đề đều có đúng 3 literal** (`3SAT`), ta có ngay điểm xuất phát gọn gàng nhất cho hàng trăm phép rút gọn NP-complete trong suốt phần còn lại của lý thuyết độ phức tạp.

## Bản đồ kiến thức nền: Ba trụ cột của phép rút gọn $$\mathrm{SAT} \le_p 3\mathrm{SAT}$$

1. **Tính bảo toàn khả thỏa (Equisatisfiability) vs. Tương đương logic**:
   Khi thêm biến phụ $$y_1, y_2, \dots$$ để bẻ gãy mệnh đề dài, công thức mới $$\varphi'$$ **không** tương đương logic với $$\varphi$$ (vì có thêm biến mới), nhưng luôn **đồng khả thỏa**: $$\varphi$$ có nghiệm $$\iff \varphi'$$ có nghiệm!
2. **Kỹ thuật dây chuyền biến phụ (Tseitin Splitting)**:
   Một mệnh đề dài $$k \ge 4$$ literal $$(l_1 \lor l_2 \lor \dots \lor l_k)$$ được cắt thành chuỗi $$k-2$$ mệnh đề 3-literal bằng $$k-3$$ biến phụ:
   $$(l_1 \lor l_2 \lor y_1) \land (\neg y_1 \lor l_3 \lor y_2) \land \cdots \land (\neg y_{k-3} \lor l_{k-1} \lor l_k).$$
3. **Bổ sung biến đệm (Padding) cho mệnh đề ngắn ($$k = 1, 2$$)**:
   Mệnh đề 1 literal $$(l_1)$$ hay 2 literal $$(l_1 \lor l_2)$$ được đệm thêm biến phụ (hoặc lặp literal tùy quy ước) thành đúng 3 literal mà không đổi tính khả thỏa.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây dựng** phép biến đổi đa thức $$f$$ chuyển công thức CNF thành 3CNF mà vẫn bảo toàn tính thỏa mãn được.
- **Chứng minh** tính đúng đắn cho từng trường hợp độ dài mệnh đề.
- **Kết luận** $$3\mathrm{SAT}$$ là bài toán NP-complete.

</div>

## Bước 1: $$3\mathrm{SAT}\in NP$$

Tương tự SAT, chứng chỉ là một phép gán chân trị cho các biến và bộ kiểm chứng đánh giá công thức trong thời gian đa thức. $$\square$$

## Bước 2: Phép biến đổi từng mệnh đề

Cho công thức CNF $$\varphi=C_1\land\cdots\land C_m$$. Ta xử lý độc lập từng mệnh đề $$C$$ tùy theo số lượng literal $$\lvert C\rvert$$:

### Trường hợp $$\lvert C\rvert=3$$

Giữ nguyên mệnh đề.

### Trường hợp $$\lvert C\rvert=1$$: $$C=(\ell)$$

Đưa thêm hai biến phụ mới $$u,v$$ và thay $$C$$ bằng hội của bốn mệnh đề 3-literal:

$$
(\ell\lor u\lor v)\land(\ell\lor u\lor\neg v)\land(\ell\lor\neg u\lor v)\land(\ell\lor\neg u\lor\neg v).
$$

<div class="textbook-lemma" markdown="1">

**Bổ đề.** Hệ bốn mệnh đề trên thỏa mãn được khi và chỉ khi $$\ell$$ nhận giá trị đúng.  
*Chứng minh.* Nếu $$\ell$$ đúng thì cả bốn mệnh đề tự động đúng. Nếu $$\ell$$ sai thì với mọi cách gán $$(u,v)$$, luôn có đúng một trong bốn mệnh đề trở thành sai — mâu thuẫn. $$\square$$

</div>

### Trường hợp $$\lvert C\rvert=2$$: $$C=(\ell_1\lor\ell_2)$$

Đưa thêm một biến phụ $$u$$ và thay $$C$$ bằng $$(\ell_1\lor\ell_2\lor u)\land(\ell_1\lor\ell_2\lor\neg u)$$. Công thức này thỏa mãn được khi và chỉ khi $$\ell_1\lor\ell_2$$ đúng.

### Trường hợp $$\lvert C\rvert=k\ge 4$$: $$C=(\ell_1\lor\cdots\lor\ell_k)$$

Đưa thêm $$k-3$$ biến phụ mới $$y_1,\ldots,y_{k-3}$$ và tách thành chuỗi mệnh đề 3-literal:

$$
(\ell_1\lor\ell_2\lor y_1)
\land(\neg y_1\lor\ell_3\lor y_2)
\land\cdots
\land(\neg y_{k-3}\lor\ell_{k-1}\lor\ell_k).
$$

<div class="textbook-lemma" markdown="1">

**Bổ đề.** Chuỗi mệnh đề trên thỏa mãn được khi và chỉ khi tồn tại ít nhất một literal $$\ell_j$$ nhận giá trị đúng.  
*Chứng minh.*  
Chiều ($$\Rightarrow$$): Nếu mọi $$\ell_j$$ đều sai thì mệnh đề đầu buộc $$y_1$$ đúng, kế tiếp buộc $$y_2$$ đúng, kéo dây chuyền đến $$y_{k-3}$$ đúng, làm mệnh đề cuối cùng trở thành sai — mâu thuẫn.  
Chiều ($$\Leftarrow$$): Nếu $$\ell_j$$ đúng, ta gán $$y_1=\cdots=y_{j-2}=\mathrm{true}$$ và các biến $$y$$ còn lại bằng $$\mathrm{false}$$, mọi mệnh đề trong chuỗi đều đúng. $$\square$$

</div>

### Thử nghiệm: SAT → 3SAT

Quan sát cách tách từng mệnh đề thành các mệnh đề tối đa 3 literal bằng biến phụ và kiểm tra tính tương đương thỏa mãn được:

<div class="interactive-demo" markdown="1">
<div data-demo="reduction-explainer" data-tab="3sat"></div>
</div>
<script src="{{ '/public/js/explainers/complexity-explainer.js' | relative_url }}"></script>

## Tổng hợp kết quả

Công thức $$f(\varphi)$$ là hội của tất cả các mệnh đề 3-literal thu được sau khi chuẩn hóa từng mệnh đề của $$\varphi$$. Phép biến đổi chạy trong thời gian tuyến tính theo kích thước $$\varphi$$ và bảo toàn tính thỏa mãn được: $$\varphi$$ thỏa mãn được khi và chỉ khi $$f(\varphi)$$ thỏa mãn được.

<div class="textbook-theorem" markdown="1">

**Định lý.** $$\mathrm{SAT}\le_p 3\mathrm{SAT}$$. Kết hợp với định lý Cook–Levin, suy ra $$3\mathrm{SAT}$$ là bài toán NP-complete.

</div>

### Khung giải thích (nên đọc chậm): Chẻ tay một mệnh đề 5 literal $$(l_1 \lor l_2 \lor l_3 \lor l_4 \lor l_5)$$ thành 3 mệnh đề 3SAT

Với $$k = 5$$, ta cần $$k - 3 = 2$$ biến phụ $$y_1, y_2$$ để tạo ra $$k - 2 = 3$$ mệnh đề:
$$C' = (l_1 \lor l_2 \lor y_1) \;\land\; (\neg y_1 \lor l_3 \lor y_2) \;\land\; (\neg y_2 \lor l_4 \lor l_5).$$

**Kiểm tra cả hai chiều đồng khả thỏa bằng tay:**
- **Chiều thuận (giả sử đúng 1 literal, ví dụ $$l_3 = \text{True}$$, 4 literal kia đều False):**
  Ta chỉ cần đặt $$y_1 = \text{True}$$ (để thỏa mệnh đề 1) và $$y_2 = \text{False}$$ (để thỏa mệnh đề 3). Mệnh đề 2 có $$l_3 = \text{True}$$ nên cũng Đúng! Cả 3 mệnh đề đều Đúng.
- **Chiều đảo (giả sử cả 5 literal $$l_1, \dots, l_5$$ đều False):**
  - Mệnh đề 1 $$(F \lor F \lor y_1)$$ ép bắt buộc $$y_1 = \text{True}$$.
  - Thay $$y_1 = \text{True}$$ vào mệnh đề 2 $$(F \lor F \lor y_2)$$ ép bắt buộc $$y_2 = \text{True}$$.
  - Thay $$y_2 = \text{True}$$ vào mệnh đề 3 $$(F \lor F \lor F)$$ → **SAI!** Không có cách gán $$y_1, y_2$$ nào cứu được.

Một mệnh đề dài $$k$$ chỉ sinh thêm $$O(k)$$ mệnh đề mới, nên tổng kích thước tăng tuyến tính!

## Bài tập

1. Kiểm chứng đầy đủ phép tách cho mệnh đề độ dài $$k=5$$ bằng cách thử các trường hợp gán chân trị.
2. Ước lượng số lượng biến phụ mới được tạo ra theo tổng độ dài các mệnh đề $$\sum\lvert C_j\rvert$$.
3. Giải thích vì sao việc $$2\mathrm{SAT}\in P$$ không mâu thuẫn với kết quả $$3\mathrm{SAT}$$ là NP-complete.

## Tài liệu đọc thêm

Sipser; CLRS (chương NP-Completeness); Garey–Johnson.

## Tóm tắt

Kỹ thuật đệm và tách mệnh đề bằng biến phụ đưa mọi công thức CNF về 3CNF trong thời gian tuyến tính, xác lập 3SAT là bài toán nguồn chủ lực cho các phép rút gọn tổ hợp.

**Bài tiếp theo:** 20.9 — Các phép rút gọn trên đồ thị: Independent Set (IS), Clique và Vertex Cover (VC).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=GCw07nZckps">SAT and 3SAT</a> — Computer Science Theory Explained, tiếng Anh. Giới thiệu bài toán SAT và 3SAT làm nền cho phép rút gọn.
- <a href="https://www.youtube.com/watch?v=ylItc6O3A4Y">SAT to 3SAT</a> — Georgia Tech CS 3510, tiếng Anh. Hướng dẫn từng bước phép biến đổi từ SAT sang 3SAT.
- <a href="https://www.youtube.com/watch?v=egLlOOqQ5YY">3SAT is NP-complete Proof</a> — Easy Theory, tiếng Anh. Chứng minh hoàn chỉnh 3SAT là NP-complete từ SAT.
