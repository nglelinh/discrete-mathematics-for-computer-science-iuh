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
