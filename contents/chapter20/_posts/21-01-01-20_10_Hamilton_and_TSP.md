---
layout: post
title: "Hamilton Cycle và TSP Quyết định"
categories: chapter20
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "Chứng minh HC và TSP-DEC thuộc NP, chứng minh đầy đủ HC≤ₚTSP-DEC, cấu trúc gadget cho 3SAT≤ₚHC và liên hệ với Chương 12."
---

<div class="textbook-epigraph" markdown="1">

"Euler is easy; Hamilton is hard — the difference is edges versus vertices."

<span class="epigraph-attribution">— Graph algorithms folklore</span>

</div>

Ở Chương 12, ta đã thấy bài toán chu trình Euler giải được trong thời gian đa thức trong khi chu trình Hamilton lại khó. Bài học này đặt chu trình Hamilton và bài toán người du lịch (TSP) vào khung lý thuyết NP-complete.

Một người giao hàng cần đi qua tất cả $$n$$ thành phố, mỗi thành phố đúng một lần rồi quay về điểm xuất phát với tổng quãng đường ngắn nhất — đó là **Bài toán Người bán hàng (TSP)**, có lẽ là bài toán NP-complete nổi tiếng nhất ngoài phòng thí nghiệm toán học. Điều thú vị là nếu chỉ cần *kiểm tra* có tồn tại chu trình đi qua mọi đỉnh đúng một lần hay không (**Hamilton Cycle**), độ khó đã đạt trần NP-complete; và chỉ cần gán trọng số `1` cho cạnh thật, `2` cho cạnh giả là ta kéo ngay độ khó đó sang TSP!

## Bản đồ kiến thức nền: Ba trụ cột của Hamilton Cycle và TSP

1. **Chu trình Euler (Thuộc $$P$$) vs. Chu trình Hamilton (NP-complete)**:
   Đi qua mỗi *cạnh* đúng 1 lần (Euler) kiểm tra trong $$O(V+E)$$ chỉ bằng cách đếm bậc chẵn; đi qua mỗi *đỉnh* đúng 1 lần (Hamilton) lại là NP-complete! Một thay đổi nhỏ từ "cạnh" sang "đỉnh" tạo ra vực thẳm độ phức tạp.
2. **Rút gọn $$\mathrm{HC} \le_p \mathrm{TSP\text{-}DEC}$$ bằng trọng số $$\{1, 2\}$$**:
   Cho đồ thị $$G = (V, E)$$ gồm $$n$$ đỉnh, xây đồ thị đầy đủ $$K_n$$ với trọng số $$w(u,v) = 1$$ nếu $$(u,v) \in E$$ và $$w(u,v) = 2$$ nếu $$(u,v) \notin E$$, đặt ngân sách $$B = n$$. Đặc biệt: hàm trọng số $$\{1, 2\}$$ thỏa **bất đẳng thức tam giác**, nên ngay cả **Metric TSP** vẫn là NP-complete!
3. **Ý tưởng rút gọn $$\mathrm{3SAT} \le_p \mathrm{HC}$$ (Mảnh ghép kim cương)**:
   Mỗi biến $$x_i$$ trở thành một hành lang đi từ trái sang phải (chọn True) hoặc từ phải sang trái (chọn False); mỗi mệnh đề là một nút rẽ nhánh chỉ có thể ghé thăm nếu ít nhất một biến đi đúng chiều thỏa mãn mệnh đề đó.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** hai bài toán HC và TSP-DEC thuộc lớp $$NP$$.
- **Chứng minh** đầy đủ phép rút gọn $$\mathrm{HC}\le_p\mathrm{TSP\text{-}DEC}$$.
- **Mô tả** cấu trúc phép rút gọn $$3\mathrm{SAT}\le_p\mathrm{HC}$$ bằng gadget (tham khảo Garey–Johnson).

</div>

## Chứng minh thuộc lớp $$NP$$

- **HC:** chứng chỉ là một hoán vị các đỉnh; bộ kiểm chứng kiểm tra xem $$n$$ cạnh liên tiếp khép kín có đều thuộc $$E$$ hay không.
- **TSP-DEC:** chứng chỉ là một hành trình qua đủ $$n$$ đỉnh; bộ kiểm chứng cộng tổng trọng số các cạnh và so sánh với ngưỡng $$K$$. $$\square$$

## Chứng minh đầy đủ $$\mathrm{HC}\le_p\mathrm{TSP\text{-}DEC}$$

**Phép dựng:** Từ đồ thị $$G=(V,E)$$ có $$\lvert V\rvert=n$$ đỉnh, ta xây dựng đồ thị đầy đủ có trọng số $$K_n$$ trên cùng tập đỉnh $$V$$ với hàm trọng số:

$$
w(e)=\begin{cases}1&e\in E\\2&e\notin E.\end{cases}
$$

Ta đặt câu hỏi TSP-DEC: đồ thị đầy đủ này có hành trình Hamilton với tổng trọng số $$\le n$$ hay không?

**Tính đúng đắn:**  
- Nếu $$G$$ có chu trình Hamilton thì hành trình đó gồm $$n$$ cạnh đều thuộc $$E$$ (mỗi cạnh có trọng số 1), nên tổng trọng số đúng bằng $$n$$.  
- Ngược lại, nếu $$K_n$$ có hành trình tổng trọng số $$\le n$$ thì vì mọi cạnh đều có trọng số $$\ge 1$$, hành trình buộc phải dùng đúng $$n$$ cạnh có trọng số 1 — nghĩa là tất cả các cạnh đều thuộc $$E$$ và tạo thành một chu trình Hamilton trong $$G$$.

Phép dựng chỉ tốn thời gian đa thức $$O(n^2)$$. $$\square$$

## Cấu trúc rút gọn $$3\mathrm{SAT}\le_p\mathrm{HC}$$

Phép rút gọn sử dụng các gadget đỉnh/cạnh để mô phỏng từng biến, từng literal và từng mệnh đề (xem Garey–Johnson hoặc mục bổ sung trong Sipser). Khi trình bày seminar, nên đọc kỹ một nguồn chuẩn, tự vẽ lại gadget và viết tường minh lập luận hai chiều trong khoảng 2 trang thay vì tự đoán cấu trúc gadget.

<div class="textbook-theorem" markdown="1">

**Định lý.** Cả HC và TSP-DEC đều là bài toán NP-complete (HC suy từ phép rút gọn gadget 3SAT→HC và TSP-DEC suy từ phép rút gọn HC→TSP-DEC ở trên).

</div>

### Khung giải thích (nên đọc chậm): Kiểm tra tay phép rút gọn $$\mathrm{HC} \le_p \mathrm{TSP\text{-}DEC}$$ trên đồ thị 4 đỉnh

Cho đồ thị 4 đỉnh $$G$$ có các cạnh $$\{(1,2), (2,3), (3,4), (4,1), (1,3)\}$$ ($$n = 4$$). Ta xây ma trận khoảng cách $$K_4$$ với trọng số `1` cho cạnh có trong $$G$$ và `2` cho cạnh thiếu `(2,4)`, đặt ngưỡng $$B = n = 4$$:
- **Nếu $$G$$ có chu trình Hamilton** (ví dụ $$1 \to 2 \to 3 \to 4 \to 1$$): cả 4 cạnh đều thuộc $$G$$ nên đều có trọng số `1`. Tổng chi phí hành trình = $$1 + 1 + 1 + 1 = \mathbf{4} \le B$$!
- **Nếu ta xóa cạnh $$(3,4)$$ khỏi $$G$$** (khiến $$G$$ không còn chu trình Hamilton): bất kỳ hành trình nào đi qua cả 4 đỉnh trong $$K_4$$ đều phải dùng ít nhất **1 cạnh không có trong $$G$$** (trọng số `2`), nên tổng chi phí ít nhất là $$1 + 1 + 1 + 2 = \mathbf{5} > 4$$!
- **Kiểm tra bất đẳng thức tam giác:** Với mọi bộ ba đỉnh $$(u,v,w)$$, tổng hai cạnh luôn $$\ge 1 + 1 = 2 \ge w(u,w)$$. Vậy phép rút gọn chứng minh luôn **Metric TSP** là NP-complete!

## Bài tập

1. Trình bày lại đầy đủ chứng minh $$\mathrm{HC}\le_p\mathrm{TSP\text{-}DEC}$$.
2. Giải thích vì sao chọn trọng số $$2$$ cho các cạnh không thuộc $$E$$ là đủ lớn (nếu dùng ít nhất một cạnh “giả”, tổng trọng số sẽ $$\ge n+1$$).
3. Đối chiếu chu trình Euler và chu trình Hamilton về mặt chứng chỉ và thuật toán giải.

## Tài liệu đọc thêm

Garey–Johnson (phần Hamilton); Vazirani (thuật toán xấp xỉ cho Metric TSP ở Bài 20.11).

## Tóm tắt

Chu trình Hamilton và bài toán TSP phiên bản quyết định đều là NP-complete, kết nối trực tiếp lý thuyết đồ thị ở Chương 12 với lý thuyết độ phức tạp.

**Bài tiếp theo:** 20.11 — Thuật toán xấp xỉ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=1pmBjIZ20pE">What is the Traveling Salesman Problem?</a> — AlphaOpt, tiếng Anh. Giới thiệu bài toán TSP và phiên bản quyết định được chứng minh NP-complete trong bài.
- <a href="https://www.youtube.com/watch?v=4r78NtOnWWA">Hamiltonian Path is NP-Complete (Directed, Reduction from 3SAT)</a> — Easy Theory, tiếng Anh. Chứng minh đường đi Hamilton có hướng là NP-complete bằng rút gọn từ 3SAT.
- <a href="https://www.youtube.com/watch?v=OHnX-R_SBpM">Hamiltonian Cycle is NP-Complete (Algorithms 24)</a> — Professor Bryce, tiếng Anh. Chứng minh chu trình Hamilton là NP-complete.
