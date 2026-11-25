---
layout: post
title: "Định lý Cook–Levin (Tableau)"
categories: chapter20
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Chứng minh SAT là NP-complete bằng bảng cấu hình (tableau): xây dựng biến logic, bốn nhóm mệnh đề G1–G4 và chứng minh tính đúng đắn của rút gọn L≤ₚSAT."
---

<div class="textbook-epigraph" markdown="1">

"Every efficient verification becomes a Boolean formula."

<span class="epigraph-attribution">— Cook–Levin</span>

</div>

Định lý Cook–Levin là **kết quả trung tâm** khai sinh lý thuyết NP-đầy đủ: mọi ngôn ngữ $$L\in NP$$ đều có thể rút gọn đa thức về bài toán thỏa mãn công thức logic **SAT**.

Để chứng minh một bài toán mới là NP-complete, ta chỉ cần rút gọn từ một bài toán đã biết là NP-complete. Nhưng câu hỏi "con gà và quả trứng" hiện ra ngay lập tức: **làm sao tìm được bài toán NP-complete ĐẦU TIÊN khi trong tay chưa có bài nào để rút gọn?** Năm 1971, Stephen Cook (và độc lập bởi Leonid Levin năm 1973) đã làm được điều phi thường: dịch *trực tiếp* toàn bộ bảng tính toán của một máy Turing không đơn định bất kỳ thành một công thức Boolean CNF — khai sinh bài toán NP-complete đầu tiên trong lịch sử: **`SAT`**.

## Kiến thức cần nhớ: Bốn khối mệnh đề trong chứng minh Tableau của Cook–Levin

1. **Bảng tính toán (Computation Tableau) cỡ $$n^k \times n^k$$**:
   Ghi lại toàn bộ lịch sử chạy của NTM $$M$$ trên đầu vào $$x$$ thành một lưới ô: hàng $$i$$ là cấu hình tại bước thời gian $$i$$, cột $$j$$ là ô băng thứ $$j$$. Vì $$M$$ chạy trong $$n^k$$ bước, toàn bộ lịch sử nằm gọn trong đúng $$O(n^{2k})$$ ô.
2. **Biến Boolean chỉ báo $$x_{i, j, s}$$**:
   Mỗi biến trả lời câu hỏi *"Tại bước $$i$$, ô băng $$j$$ có chứa ký hiệu $$s$$ (ký tự băng hoặc trạng thái đầu đọc) hay không?"*. Tổng số biến là đa thức $$O(n^{2k} \cdot \vert C \vert)$$.
3. **Bốn nhóm mệnh đề CNF ép bảng là một tính toán hợp lệ**:
   - $$\varphi_{\text{cell}}$$: mỗi ô chứa **đúng 1** ký hiệu.
   - $$\varphi_{\text{start}}$$: hàng đầu tiên là cấu hình khởi đầu $$q_0 x_1 \dots x_n \sqcup \dots$$.
   - $$\varphi_{\text{accept}}$$: xuất hiện trạng thái chấp nhận $$q_A$$ ở đâu đó trong bảng.
   - $$\varphi_{\text{move}}$$: mọi **cửa sổ cục bộ $$2 \times 3$$** (3 ô liên tiếp ở hàng $$i$$ và 3 ô ngay dưới nó ở hàng $$i+1$$) phải tuân thủ đúng hàm chuyển $$\delta$$ của máy Turing!

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** $$\mathrm{SAT}\in NP$$.
- **Xây dựng** bảng cấu hình (*tableau*) và bốn nhóm mệnh đề logic mã hóa quá trình tính toán.
- **Chứng minh** $$L\le_p\mathrm{SAT}$$ cho một ngôn ngữ $$L\in NP$$ tùy ý.

</div>

## Bước 1: $$\mathrm{SAT}\in NP$$

Chọn chứng chỉ là một phép gán chân trị cho các biến của công thức $$\varphi$$. Bộ kiểm chứng chỉ cần thay giá trị vào và tính công thức trong thời gian tuyến tính theo $$\lvert\varphi\rvert$$. Vậy $$\mathrm{SAT}\in NP$$. $$\square$$

## Bước 2: Mã hóa tính toán của máy Turing thành công thức CNF

Xét một ngôn ngữ bất kỳ $$L\in NP$$ với bộ kiểm chứng (hoặc máy Turing không đơn định) $$M$$ chạy trong thời gian đa thức $$T=N^{O(1)}$$ trên đầu vào $$z=\langle x,c\rangle$$ độ dài $$N$$. Trong $$T$$ bước, đầu đọc/ghi chỉ có thể di chuyển trong cửa sổ băng $$[-T,T]$$.

### Tập biến bảng cấu hình (*tableau*)

Ta định nghĩa ba nhóm biến Boolean để mô tả toàn bộ lịch sử tính toán của $$M$$:

- $$C_{t,i,a}$$: tại thời điểm $$t$$, ô băng $$i$$ chứa ký hiệu $$a$$.
- $$H_{t,i}$$: tại thời điểm $$t$$, đầu đọc/ghi nằm ở ô $$i$$.
- $$Q_{t,q}$$: tại thời điểm $$t$$, máy đang ở trạng thái $$q$$.

Tổng số biến nằm trong $$O(T^2)$$.

### Bốn nhóm mệnh đề ràng buộc (CNF cục bộ)

- **G1 (Khởi tạo tại $$t=0$$):** nội dung băng ban đầu là $$z$$ (các ô ngoài là ký hiệu trống), đầu đọc đặt ở vị trí 0 và trạng thái là $$q_0$$.
- **G2 (Tính duy nhất):** tại mỗi thời điểm $$t$$, máy ở đúng một trạng thái, đầu đọc nằm ở đúng một vị trí và mỗi ô băng chứa đúng một ký hiệu.
- **G3 (Quy tắc chuyển trạng thái):** nếu đầu đọc không nằm tại ô $$i$$ thì ký hiệu ở ô $$i$$ giữ nguyên sang bước $$t+1$$; nếu đầu đọc ở ô $$i$$ với cấu hình $$(q,a)\mapsto(q',b,D)$$ thì cập nhật trạng thái mới $$q'$$, ghi ký hiệu $$b$$ và dịch đầu đọc theo hướng $$D$$. Mỗi phép kéo theo $$X\Rightarrow Y$$ được viết lại thành $$\neg X\lor Y$$ rồi biến đổi về dạng CNF.
- **G4 (Chấp nhận):** tồn tại ít nhất một thời điểm máy đạt trạng thái chấp nhận: $$\bigvee_t Q_{t,q_A}$$.

### Tính đúng đắn của phép rút gọn

Nếu $$M$$ có một đường chạy chấp nhận trên đầu vào, lịch sử các cấu hình tương ứng sẽ tạo ra một phép gán chân trị thỏa mãn $$\varphi_z$$. Ngược lại, mọi phép gán thỏa mãn $$\varphi_z$$ đều xác định một bảng cấu hình hợp lệ mô tả đúng một đường chạy chấp nhận của $$M$$. Vì công thức $$\varphi_z$$ có kích thước đa thức và dựng được trong thời gian đa thức, ta có $$L\le_p\mathrm{SAT}$$. Kết hợp với Bước 1, **SAT là NP-complete**. $$\square$$

## Ghi chú khi viết bài báo

Trong các công trình nghiên cứu, phép dựng này thường được trích dẫn gọn là *“by the standard tableau construction (Sipser / Arora–Barak)”*; tuy nhiên khi trình bày seminar, cần nêu rõ cả bốn nhóm ràng buộc G1–G4.

### Giải thích: Vì sao chỉ cần kiểm tra các cửa sổ nhỏ $$2 \times 3$$ là đủ đảm bảo cả bảng tính toán hợp lệ?

Đây là bước thiên tài nhất của định lý Cook–Levin. Giả sử tại bước $$i$$, đầu đọc đang ở ô $$j$$ với trạng thái $$q$$ đọc ký tự `a`, và luật chuyển $$\delta(q, a) = (q', b, R)$$ (ghi `b`, dịch phải sang ô $$j+1$$).
Hãy quan sát cửa sổ $$2 \times 3$$ gồm 3 cột $$(j-1, j, j+1)$$ ở hàng $$i$$ và hàng $$i+1$$:

| Hàng thời gian | Cột $$j-1$$ | Cột $$j$$ | Cột $$j+1$$ |
| :---: | :---: | :---: | :---: |
| **Hàng $$i$$** | `c` | $$(q, a)$$ | `d` |
| **Hàng $$i+1$$** | `c` | `b` | $$(q', d)$$ |

- Tại mọi vị trí *xa đầu đọc*, ký tự ở hàng $$i+1$$ giữ nguyên y hệt hàng $$i$$ — chỉ cần nhìn 3 ô phía trên là biết chắc đầu đọc không tới từ trái hay phải!
- Tại vị trí có đầu đọc, vì đầu đọc mỗi bước chỉ dịch tối đa **1 ô** (sang trái hoặc phải), toàn bộ thay đổi giữa hàng $$i$$ và hàng $$i+1$$ nằm gọn trong đúng **3 cột liên tiếp**!
- Số cửa sổ $$2 \times 3$$ trên toàn bảng là $$(n^k - 1)(n^k - 2) = O(n^{2k})$$, và mỗi cửa sổ chỉ cần một số hằng mệnh đề CNF để mô tả các cấu hình $$2 \times 3$$ hợp lệ. Vậy tổng kích thước công thức $$\varphi_{M,x}$$ chắc chắn là **đa thức**!

## Bài tập

1. Ước lượng bậc độ lớn của số biến nếu $$T=n^3$$ và $$\lvert\Gamma\rvert=10$$.
2. Viết công thức CNF biểu diễn ràng buộc “có đúng một trong ba biến $$x_1,x_2,x_3$$ nhận giá trị đúng”.
3. Đối chiếu cách dùng cửa sổ $$2\times 3$$ trong Sipser với cách trình bày trong Arora–Barak (tóm tắt khoảng 1 trang).

## Tài liệu đọc thêm

Sipser (chứng minh Cook–Levin); Arora–Barak §2; Cook (STOC 1971).

## Tóm tắt

Phép dựng bảng cấu hình kích thước $$O(T^2)$$ biến mọi tính toán đa thức của máy Turing thành công thức Boolean cục bộ, chứng minh SAT là bài toán NP-complete đầu tiên.

**Bài tiếp theo:** 20.8 — Rút gọn $$\mathrm{SAT}\le_p 3\mathrm{SAT}$$.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=W9G_1xG77LE">NP-Complete Explained (Cook-Levin Theorem)</a> — Undefined Behavior, tiếng Anh. Giới thiệu ý tưởng chính của định lý Cook–Levin trước khi đi vào chi tiết bảng cấu hình.
- <a href="https://www.youtube.com/watch?v=Kux0iFe2yyA">The Cook-Levin Theorem (part I)</a> — Computer Science Theory Explained, tiếng Anh. Phần đầu của chứng minh mã hóa quá trình tính toán thành SAT.
- <a href="https://www.youtube.com/watch?v=LW_37i96htQ">Cook-Levin Theorem: Full Proof (SAT is NP-complete)</a> — Easy Theory, tiếng Anh. Chứng minh đầy đủ định lý SAT là NP-complete.
