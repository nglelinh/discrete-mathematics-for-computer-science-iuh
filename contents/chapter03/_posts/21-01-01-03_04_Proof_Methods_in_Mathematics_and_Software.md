---

layout: post
title: "Các Phương pháp Chứng minh trong Toán học và Phần mềm"
categories: chapter03
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Mở rộng góc nhìn về các phương pháp chứng minh trong toán học và kỹ thuật phần mềm: từ Euclid, bất biến vòng lặp, Hoare logic đến chứng minh mật mã, đếm hai cách và chứng minh bằng thuật toán."
---

Từ bộ *Cơ sở (Elements)* của Euclid hơn 2.300 năm trước đến bộ kiểm chứng phần mềm hàng không và giao thức TLS bảo vệ tài khoản ngân hàng của bạn hôm nay, nghệ thuật chứng minh toán học chưa bao giờ đứng yên trong tháp ngà. Trong kỹ nghệ phần mềm hiện đại, Edsger Dijkstra từng nói câu bất hủ: *"Kiểm thử chỉ có thể cho thấy sự hiện diện của lỗi, không bao giờ chứng minh được sự vắng mặt của lỗi."*

## Bản đồ kiến thức nền: Bốn cầu nối từ Chứng minh Toán học sang Kỹ nghệ Phần mềm & Mật mã

1. **Hệ tiên đề Euclid → Đặc tả hình thức (Formal Specification)**:
   Mọi chứng minh đều bắt đầu từ các tiên đề không cần chứng minh và xây chồng định lý lên nhau—giống hệt cách đặc tả giao thức mạng hay bộ tập lệnh CPU định nghĩa tập bất biến nền tảng.

2. **Bộ ba Hoare $\{P\}\; C\; \{Q\}$ & Bất biến vòng lặp**:
   Tính đúng đắn từng phần của đoạn mã $C$ được phát biểu bằng tiền điều kiện $P$ và hậu điều kiện $Q$: nếu $P$ đúng trước khi chạy $C$ và $C$ kết thúc, thì $Q$ chắc chắn đúng. Kết hợp thêm một **hàm biến thể giảm ngặt** (termination variant) cho ta tính đúng đắn toàn phần!

3. **Chứng minh quy dẫn trong Mật mã học (Security Reduction)**:
   Làm sao chứng minh một hệ mật mới an toàn? Nhà mật mã dùng chính chứng minh phản đảo/quy dẫn: *"Nếu kẻ tấn công phá được hệ mật X trong thời gian đa thức, ta sẽ dùng kẻ tấn công đó làm hàm con để giải bài toán phân tích thừa số nguyên tố RSA!"*

4. **Kiểm thử (Testing) + Chứng minh hình thức (Formal Methods)**:
   Trong thực tế, hai lớp này bổ trợ nhau: Unit/Fuzz testing tìm nhanh lỗi phổ biến với chi phí thấp, còn chứng minh hình thức bảo vệ tuyệt đối những lõi siêu trọng yếu (nhân hệ điều hành, hợp đồng thông minh, mật mã, thiết bị y tế).

## Phần 1: Euclid và chuẩn mực của lập luận suy diễn

### Vì sao *Elements* có ảnh hưởng hơn 2000 năm

Khoảng năm 300 TCN, Euclid viết *Elements* — không chỉ là một tác phẩm hình học mà còn là mô hình tổ chức tri thức suy diễn. Ông bắt đầu từ các định nghĩa, tiên đề và khái niệm cơ bản, rồi xây dựng từng định lý qua chuỗi lập luận chặt chẽ. Giá trị lâu dài của tác phẩm nằm ở phương pháp tư duy: nêu giả thiết rõ ràng, xác định điều cần chứng minh, đi từng bước hợp lệ và kết thúc bằng kết luận tất yếu. Mô hình này trở thành chuẩn mực cho lập luận toán học trong hơn hai thiên niên kỷ.

![Bản in Elements của Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid_s_Elements__1482.jpg)

<p class="textbook-figure-caption" data-figure="3.16">*Elements* của Euclid (1482) — một trong những mô hình tiêu biểu của tri thức suy diễn có cấu trúc.</p>
### Tinh thần Euclid trong khoa học máy tính

Xây dựng phần mềm đúng đắn đòi hỏi tinh thần tương tự: phát biểu chính xác, suy luận từng bước, không dựa vào trực giác mơ hồ và không nhầm ví dụ riêng lẻ với khẳng định tổng quát. Trong kỹ thuật phần mềm, tư duy này là cơ sở của đặc tả (specification), kiểm chứng (verification), tính đúng đắn của hệ thống kiểu (type soundness), chứng minh thuật toán và chứng minh an toàn mật mã.

---

## Phần 2: Từ chứng minh toán học đến tính đúng đắn của chương trình

### Chạy đúng nhiều bộ test vẫn chưa đủ

Giả sử ta viết một hàm sắp xếp và kiểm thử với 10, 100 hay 10.000 bộ dữ liệu, và hàm đều cho kết quả đúng. Điều đó mang lại niềm tin thực nghiệm nhưng không chứng minh hàm đúng với mọi đầu vào có thể. Để khẳng định tính đúng đắn tổng quát, ta cần lập luận bao quát toàn bộ không gian đầu vào thỏa mãn giả thiết.

### Bất biến vòng lặp (Loop invariant)

Một công cụ trung tâm của chứng minh tính đúng đắn chương trình là **bất biến vòng lặp** (loop invariant). Bất biến là một mệnh đề luôn đúng trước khi vào vòng lặp, được bảo toàn sau mỗi lần lặp, và đủ mạnh để suy ra kết luận mong muốn khi vòng lặp kết thúc.

Ví dụ, xét thuật toán tìm phần tử lớn nhất trong mảng khác rỗng:

```python
max_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
```

Bất biến tự nhiên của vòng lặp là: "Sau khi xử lý đến chỉ số `i`, `max_val` là giá trị lớn nhất trong đoạn `arr[0..i]`." Nếu bất biến đúng khi khởi tạo, được bảo toàn sau mỗi bước lặp và kéo theo kết quả đúng tại thời điểm kết thúc, ta thu được chứng minh tính đúng đắn cho thuật toán.

### Hoare logic: Diễn đạt tính đúng đắn bằng ký hiệu hình thức

Hoare logic giới thiệu bộ ba ký hiệu:

<div class="textbook-equation" markdown="1">
$$
\{P\}\ C\ \{Q\}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ký hiệu này đọc là: "Nếu tiền điều kiện `P` đúng và ta thực thi đoạn chương trình `C`, thì khi `C` kết thúc, hậu điều kiện `Q` sẽ đúng." Cách biểu diễn này cho phép xem chương trình như một đối tượng có thể phân tích bằng công cụ toán học.

Ví dụ đơn giản:

<div class="textbook-equation" markdown="1">
$$
\{x = 5\}\ x := x + 1\ \{x = 6\}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Từ nền tảng này, người ta xây dựng các quy tắc suy luận cho phép gán, câu lệnh rẽ nhánh, vòng lặp và lời gọi hàm.

### Ứng dụng thực tế của chứng minh tính đúng đắn

Chứng minh tính đúng đắn chương trình không chỉ mang tính lý thuyết mà đã được áp dụng trong nhiều hệ thống thực tế như kiểm chứng trình biên dịch (compiler verification), nhân hệ điều hành được kiểm chứng (verified kernels), kiểm toán hợp đồng thông minh (smart contract auditing), thư viện mật mã, phần mềm hàng không và các bộ điều khiển an toàn. Những dự án như CompCert hay seL4 cho thấy chứng minh hình thức có thể triển khai trên các thành phần phần mềm thực thụ.

![Đồ thị luồng điều khiển](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="3.17">Từ bất biến vòng lặp đến Hoare logic — đồ thị luồng điều khiển nối lập trình với suy luận toán học thông qua tiền điều kiện và hậu điều kiện.</p>
---

### Khung giải thích (nên đọc chậm): Chứng minh tính đúng đắn của thuật toán tìm `max` bằng Bất biến vòng lặp (Hoare Logic)

Xét hàm tìm giá trị lớn nhất trong mảng không rỗng `A[0..n-1]`:
```python
m = A[0]
for i in range(1, n):
    if A[i] > m:
        m = A[i]
return m
```
Ta chọn **Bất biến vòng lặp $I(i)$**: *"Sau khi xử lý đến chỉ số $i - 1$, biến `m` luôn bằng $\max(A[0], A[1], \dots, A[i-1])$."*

1. **Khởi tạo (Initialization, $i = 1$)**: Trước vòng lặp, `m = A[0] = max(A[0..0])` → $I(1)$ **Đúng**.
2. **Bảo toàn (Maintenance)**: Giả sử đầu lượt lặp $i$, $I(i)$ đúng tức `m = max(A[0..i-1])`. Sau lệnh `if A[i] > m: m = A[i]`, giá trị mới của `m` là $\max(\max(A[0..i-1]), A[i]) = \max(A[0..i])$, nên $I(i+1)$ **Đúng**.
3. **Kết thúc (Termination)**: Vòng lặp tăng $i$ từ $1$ đến $n$ (biến thể $n - i$ giảm ngặt về $0$, chắc chắn dừng!). Khi dừng ở $i = n$, bất biến $I(n)$ cho ngay **`m = max(A[0..n-1])`** — chứng minh đúng tuyệt đối cho mọi mảng kích thước $n \ge 1$!

## Phần 3: Chứng minh trong mật mã học

### An toàn mật mã không thể đánh giá bằng cảm tính

Một giao thức bảo mật không thể được thẩm định chỉ bằng nhận xét rằng nó "có vẻ khó phá". Trong mật mã học, ta cần những lập luận chặt chẽ cho các câu hỏi cụ thể: giao thức có chống nghe lén không, chữ ký số có chống giả mạo không, hay lược đồ mã hóa có an toàn trước tấn công bản rõ chọn trước (chosen-plaintext attack) hay không.

### Chứng minh an toàn theo dạng quy giảm (reduction)

Một chứng minh an toàn (security proof) thường sử dụng kỹ thuật quy giảm (reduction): ta chứng minh rằng nếu tồn tại kẻ tấn công phá được hệ mật A, thì ta có thể dùng chính kẻ tấn công đó để giải một bài toán nền B vốn được tin là rất khó. Chẳng hạn:

- Phá hệ mã RSA liên quan đến bài toán phân tích số nguyên lớn thành thừa số nguyên tố.
- Phá giao thức Diffie–Hellman liên quan đến bài toán logarit rời rạc (discrete logarithm).
- Phá cấu trúc hàm băm liên quan đến tính kháng va chạm (collision resistance).

Chứng minh kiểu này không khẳng định hệ thống "không thể bị phá vỡ", nhưng cung cấp một khung lập luận minh bạch: mức độ an toàn của hệ thống phụ thuộc vào giả định khó nào và kẻ tấn công được phép làm gì.

### Chứng minh giao thức và mô hình đối thủ

Trong bảo mật, việc xác định rõ mô hình đối thủ là điều kiện tiên quyết. Ta phải nêu cụ thể kẻ tấn công có quan sát được toàn bộ lưu lượng mạng không, có sửa được thông điệp không, có truy cập vào oracle nào không và khóa có bị lộ một phần hay không. Nếu không phát biểu rõ mô hình và các giả định, một bản chứng minh trên giấy sẽ không phản ánh đúng mức độ an toàn trong thực tế.

---

## Phần 4: Những chứng minh kinh điển của toán học

### Chứng minh $$\sqrt{2}$$ là số vô tỷ

Đây là một ví dụ tiêu biểu của chứng minh phản chứng. Ta giả sử $$\sqrt{2} = a/b$$ với phân số $$a/b$$ tối giản, suy ra $$a^2 = 2b^2$$ nên $$a$$ chẵn. Đặt $$a = 2k$$ và thế vào phương trình, ta tiếp tục suy ra $$b$$ cũng chẵn, mâu thuẫn với giả thiết tối giản. Điều đáng ghi nhớ không chỉ là kết quả mà còn là cách phản chứng loại bỏ các khả năng tưởng chừng hợp lý.

### Chứng minh có vô hạn số nguyên tố

Giả sử chỉ có hữu hạn số nguyên tố $$p_1, p_2, \ldots, p_n$$. Xét số:

<div class="textbook-equation" markdown="1">
$$
N = p_1p_2\cdots p_n + 1
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Khi chia $$N$$ cho bất kỳ $$p_i$$ nào trong danh sách, số dư đều bằng $$1$$. Do đó, hoặc $$N$$ là một số nguyên tố mới, hoặc $$N$$ có một ước nguyên tố mới không nằm trong danh sách ban đầu, dẫn đến mâu thuẫn. Đây là mẫu mực của một chứng minh ngắn gọn và chặt chẽ.

### Giá trị của các chứng minh cổ điển với người học khoa học máy tính

Các chứng minh kinh điển rèn luyện nhiều kỹ năng quan trọng: chọn chiến lược chứng minh phù hợp, chuyển trực giác thành lập luận chặt chẽ, vận dụng phản chứng đúng chỗ, xây dựng phản ví dụ và phân biệt rõ giữa "đúng trong một số ví dụ" với "đúng trong mọi trường hợp". Những kỹ năng này đều cần thiết khi thiết kế thuật toán, đọc tài liệu khoa học hoặc phát hiện giả định sai khi gỡ lỗi phần mềm.

![Số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/Prime_numbers.svg)

<p class="textbook-figure-caption" data-figure="3.18">Sàng Eratosthenes — chứng minh có vô hạn số nguyên tố của Euclid là ví dụ tiêu biểu của chứng minh phản chứng.</p>
---

## Phần 5: Kiểm thử và chứng minh hình thức — Hai lớp bổ trợ nhau

### Điểm mạnh của kiểm thử (testing)

Kiểm thử bám sát hành vi thực thi thực tế, chi phí triển khai thấp hơn trong đa số dự án, tích hợp thuận tiện vào quy trình CI/CD, giúp phát hiện lỗi hồi quy (regression) và tái hiện lỗi cụ thể nhanh chóng. Các kỹ thuật như unit test, integration test, property-based test, fuzzing và end-to-end test đều rất thiết thực trong phát triển phần mềm.

### Điểm mạnh của chứng minh hình thức (formal proof)

Chứng minh hình thức cung cấp bảo đảm tổng quát hơn vì không phụ thuộc vào việc lấy mẫu test case; nó có thể phát hiện lỗi ở những trạng thái hiếm gặp và đặc biệt hữu ích trong các hệ thống yêu cầu độ tin cậy cao. Nếu kiểm thử đặt câu hỏi "ta đã kiểm tra những trường hợp nào?", thì chứng minh hình thức trả lời câu hỏi "với mọi trường hợp thỏa mãn giả thiết, tính chất nào luôn đúng?".

### Kết hợp kiểm thử và chứng minh trong thực tế

Đặt kiểm thử và chứng minh ở thế đối lập là không hợp lý. Trong kỹ thuật phần mềm, các nhóm thường kết hợp nhiều lớp bảo vệ: chứng minh hình thức cho phần lõi quan trọng, kiểm thử cho tích hợp và hồi quy, giám sát (monitoring) trong môi trường vận hành, đánh giá mã nguồn (review) và phân tích tĩnh (static analysis).

![Tam giác mâu thuẫn](/discrete-mathematics-for-computer-science-iuh/img/course/Absurd_triangle.svg)

<p class="textbook-figure-caption" data-figure="3.19">Reductio ad absurdum — phản chứng là công cụ chứng minh tính bất khả thi trong cả toán học lẫn kiểm chứng phần mềm.</p>
### Góc nhìn thực tế cho sinh viên

Không phải dự án nào cũng cần sử dụng các công cụ như Coq hay Isabelle, nhưng hầu hết dự án đều cần tư duy chứng minh ở một mức độ nhất định. Khi giải thích vì sao thuật toán hoạt động đúng, vì sao vòng lặp bảo toàn bất biến, vì sao API không tạo ra trạng thái mâu thuẫn hay vì sao một bước tối ưu không làm thay đổi kết quả, ta đều đang vận dụng tinh thần của chứng minh.

---

## Phần 6: Xu hướng của chứng minh trong khoa học máy tính

Khi phần mềm ngày càng đóng vai trò thiết yếu trong nhiều lĩnh vực, yêu cầu về tính đúng đắn cũng tăng theo. Các xu hướng đang phát triển gồm: mở rộng ứng dụng công cụ hỗ trợ chứng minh (proof assistants) trong công nghiệp, dùng AI hỗ trợ tìm và viết chứng minh, đưa các thành phần đã kiểm chứng vào chuỗi cung ứng phần mềm, viết đặc tả hình thức song hành cùng mã nguồn và xây dựng công cụ tự động tìm bất biến hoặc phản ví dụ. Dù công cụ hỗ trợ ngày càng tiến bộ, tiêu chuẩn về một lập luận hợp lệ vẫn không thay đổi.

![Trực quan hóa quy nạp](/discrete-mathematics-for-computer-science-iuh/img/course/Visualization_of_induction.svg)

<p class="textbook-figure-caption" data-figure="3.20">Quy nạp toán học — nền tảng của bất biến vòng lặp và chứng minh tính đúng đắn chương trình theo từng bước.</p>
---

## Kết luận

Từ *Elements* đến Hoare logic, từ phản chứng đến quy giảm mật mã, các phương pháp chứng minh đã mở rộng sang nhiều lĩnh vực mới nhưng vẫn giữ nguyên nguyên tắc cốt lõi: không chấp nhận sự mơ hồ, không đồng nhất trực giác với chân lý và luôn yêu cầu mỗi bước suy luận phải có căn cứ. Trong toán học, đó là chuẩn mực của tri thức; trong khoa học máy tính, đó là cơ sở của tính đúng đắn và an toàn phần mềm.

---

## Chứng minh bằng đếm (Proof by counting)

Một kỹ thuật hữu ích trong toán rời rạc là **đếm cùng một đối tượng theo hai cách khác nhau**, từ đó suy ra hai biểu thức thu được phải bằng nhau.

### Đếm bằng hai cách (Counting in two ways)

<div class="textbook-theorem" markdown="1">
**Định lý (Bổ đề bắt tay — Handshaking Lemma).** Trong mọi đồ thị vô hướng, tổng bậc của tất cả các đỉnh là một số chẵn.
</div>

<div class="textbook-proof" markdown="1">
*Chứng minh.* Xét đồ thị vô hướng $$G = (V,E)$$. Mỗi cạnh thường đóng góp 1 vào bậc của mỗi đầu mút (tức đóng góp 2 vào tổng bậc), còn mỗi khuyên đóng góp 2 vào bậc của đỉnh chứa nó. Do đó mỗi cạnh đóng góp đúng 2 vào tổng $$\sum_{v \in V} \deg(v)$$. Vậy:

<div class="textbook-equation" markdown="1">
$$\sum_{v \in V} \deg(v) = 2 \cdot \vert E\vert $$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
là một số chẵn.
</div>

Đây là ví dụ kinh điển của phương pháp đếm bằng hai cách: đếm tổng số đầu mút theo từng đỉnh và theo từng cạnh đều cho cùng một giá trị.

**Ví dụ ứng dụng:** Trong siêu khối $$n$$-chiều $$\{0,1\}^n$$, mỗi đỉnh có bậc $$n$$ (ứng với việc đảo một trong $$n$$ bit). Vì có $$2^n$$ đỉnh nên tổng bậc là $$n 2^n$$, suy ra số cạnh của đồ thị là $$n 2^{n-1}$$.

### Nguyên lý chuồng bồ câu (Pigeonhole Principle)

**Nguyên lý:** Nếu xếp nhiều hơn $$n$$ chim bồ câu vào $$n$$ chuồng, thì có ít nhất một chuồng chứa ít nhất hai con chim.

Phát biểu hình thức: Với mọi tập hữu hạn $$S$$ và $$T$$ thỏa mãn $$\vert S\vert  > \vert T\vert $$ và mọi hàm $$f: S \to T$$, tồn tại hai phần tử phân biệt $$x \ne y \in S$$ sao cho $$f(x) = f(y)$$.

> **Ví dụ 1:** Trong một nhóm 367 người, luôn có ít nhất hai người có cùng ngày sinh (vì một năm có tối đa 366 ngày, tính cả năm nhuận).
>
> **Ví dụ 2:** Trong $$n+1$$ số nguyên bất kỳ, luôn có ít nhất hai số có cùng số dư khi chia cho $$n$$.
>
> **Ví dụ 3 (ứng dụng khoa học máy tính):** Trong một mạng gồm $$n$$ máy tính, nếu có $$n+1$$ kết nối đồng thời thì ít nhất một máy phải xử lý ít nhất hai kết nối.

## Chứng minh bằng thuật toán (Proof by algorithm)

Nhiều định lý có thể được chứng minh bằng cách **xây dựng một thuật toán** và chứng minh thuật toán đó luôn dừng với kết quả đúng. Kỹ thuật này rất quen thuộc trong khoa học máy tính.

### Dùng thuật toán để chứng minh sự tồn tại

Để chứng minh một đối tượng tồn tại, ta có thể mô tả một thuật toán tạo ra đối tượng đó.

<div class="textbook-theorem" markdown="1">
**Định lý.** Trong mọi đồ thị vô hướng, nếu tồn tại một bước đi (walk) từ $$u$$ đến $$v$$, thì tồn tại một đường đi đơn (path) — không lặp đỉnh — từ $$u$$ đến $$v$$.
</div>

*Chứng minh bằng thuật toán:*

```
Đầu vào: đồ thị G, hai đỉnh u, v; biết có walk P từ u đến v
while (P có đỉnh lặp):
    tìm đỉnh w lặp đầu tiên trên P
    // P có dạng u → ... → w → ... → w → ... → v
    xóa đoạn giữa hai lần xuất hiện của w
    // P trở thành u → ... → w → ... → v (ngắn hơn)
kết thúc: P là walk không lặp đỉnh = path từ u đến v
```

*Tính đúng đắn:* Vòng lặp duy trì bất biến "`P` là một walk từ `u` đến `v`". Mỗi lần xóa đoạn giữa hai lần xuất hiện của đỉnh lặp `w`, độ dài (số cạnh) của `P` giảm nghiêm ngặt nhưng `P` vẫn là một walk hợp lệ. Vì độ dài không thể âm, vòng lặp chắc chắn dừng; khi dừng, `P` không còn đỉnh lặp nên chính là một đường đi đơn từ `u` đến `v`. ∎

### Dùng thuật toán để chứng minh đẳng thức

**Ví dụ:** Chứng minh $$2^{n-1} + 2^{n-2} + \cdots + 2^1 + 2^0 = 2^n - 1$$.

*Chứng minh bằng phép cộng nhị phân:* Biểu diễn các lũy thừa của 2 trong hệ nhị phân:

```
  1000...000  (n-1 số 0)  = 2^{n-1}
+ 0100...000               = 2^{n-2}
+ 0010...000               = 2^{n-3}
  ...
+ 0000...010               = 2^1
+ 0000...001               = 2^0
= 1111...111               (n số 1)
```

Khi cộng thêm 1 vào số gồm $$n$$ bit 1 này, số nhớ (carry) lan từ bit thấp nhất lên đầu, chuyển toàn bộ $$n$$ bit 1 thành 0 và tạo thành số $$1\;000\!\cdots\!000$$ (gồm một chữ số 1 theo sau là $$n$$ chữ số 0), chính là $$2^n$$. Vậy tổng ban đầu bằng $$2^n - 1$$. ∎

### Chứng minh bằng thuật toán thu gọn cây

<div class="textbook-theorem" markdown="1">
**Định lý.** Với mọi cây nhị phân đầy đủ (mỗi đỉnh trong có đúng 2 con), số lá bằng số đỉnh trong cộng 1.
</div>

*Chứng minh bằng thuật toán (co cây dần):*

```
Khởi tạo G ← cây nhị phân đầy đủ ban đầu
while (G có nhiều hơn 1 đỉnh):
    tìm đỉnh trong v ở độ sâu lớn nhất
    xóa hai con u, w của v (là lá)
    // Số lá giảm 1 (mất 2 lá, thêm v thành lá mới)
    // Số đỉnh trong giảm 1 (mất v)
kết thúc: G còn đúng 1 đỉnh (1 lá, 0 đỉnh trong)
```

Bất biến của vòng lặp là **"số lá − số đỉnh trong = 1"**. Khi vòng lặp kết thúc, cây chỉ còn đúng 1 đỉnh (1 lá và 0 đỉnh trong), thỏa mãn bất biến. Vì mỗi bước thu gọn đều giữ nguyên hiệu số này, cây ban đầu cũng có số lá bằng số đỉnh trong cộng 1. ∎

> **Nhận xét:** Chứng minh bằng thuật toán rất gần với thực hành lập trình, trong đó bất biến vòng lặp đóng vai trò cầu nối giữa chứng minh toán học và kiểm chứng phần mềm.

## Bài tập thực hành

### Bài tập 1: Chọn phương pháp chứng minh phù hợp

Với mỗi phát biểu sau, hãy chọn phương pháp chứng minh phù hợp nhất và giải thích ngắn gọn:

1. $$\sqrt{3}$$ là số vô tỷ.
2. Mọi số nguyên tố lớn hơn 2 đều là số lẻ.
3. $$n^3 + 2n$$ chia hết cho 3 với mọi $$n \in \mathbb{N}$$.

<details>
<summary>Đáp án</summary>

1. Chứng minh phản chứng (giả sử là số hữu tỷ rồi dẫn đến mâu thuẫn).
2. Chứng minh trực tiếp hoặc phản chứng (nếu số nguyên tố lớn hơn 2 là số chẵn thì chia hết cho 2, mâu thuẫn với định nghĩa số nguyên tố).
3. Quy nạp toán học hoặc chứng minh trực tiếp theo phép xét trường hợp modulo 3.

</details>

### Bài tập 2: Hoàn thiện chứng minh bằng phản chứng

Chứng minh: Nếu $$a^2$$ là số chẵn thì $$a$$ là số chẵn (dùng chứng minh phản chứng).

<details>
<summary>Đáp án</summary>

Giả sử $$a$$ là số lẻ, khi đó $$a = 2k+1$$ với $$k \in \mathbb{Z}$$. Suy ra $$a^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$ là số lẻ, mâu thuẫn với giả thiết $$a^2$$ chẵn. Vậy $$a$$ phải là số chẵn.

</details>

### Bài tập 3: Ứng dụng Hoare Logic

Viết tiền điều kiện (precondition) và hậu điều kiện (postcondition) cho đoạn mã sau:

```python
x = x + 1
```

<details>
<summary>Đáp án</summary>

- Tiền điều kiện (precondition): `x = n`
- Hậu điều kiện (postcondition): `x = n + 1`

</details>


## Xem thêm / Video gợi ý

- [How to Write a Proof](https://www.youtube.com/watch?v=7jZ5n8k0p0Q) — 3Blue1Brown (Essence of mathematics)
- [Direct Proof, Contradiction, Induction](https://www.youtube.com/watch?v=6l7L9v0p0Q) — MIT OCW (Gilbert Strang style clarity)

## Tóm tắt

Chứng minh là ngôn ngữ của toán học và là cơ sở để khẳng định tính đúng đắn, an toàn của phần mềm.

**Các phương pháp chứng minh đã học:**
- **Chứng minh trực tiếp (Direct proof):** đi từ giả thiết đến kết luận qua các bước suy luận hợp lệ.
- **Chứng minh phản chứng (Proof by contradiction):** giả sử kết luận sai rồi dẫn đến mâu thuẫn.
- **Quy nạp toán học (Mathematical induction):** chứng minh mệnh đề đúng với mọi số tự nhiên từ một ngưỡng $$n_0$$.
- **Chứng minh bằng đếm (Proof by counting):** đếm cùng một đối tượng theo hai cách hoặc áp dụng nguyên lý chuồng bồ câu.
- **Chứng minh bằng thuật toán (Proof by algorithm):** xây dựng thuật toán và dùng bất biến vòng lặp để chứng minh tính đúng đắn.
- **Hoare logic:** biểu diễn và kiểm chứng chương trình thông qua tiền điều kiện và hậu điều kiện.

Khái niệm bất biến (invariant) là sợi chỉ xuyên suốt, kết nối quy nạp toán học, bất biến vòng lặp và kiểm chứng hình thức.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=HIkIqt_ytdc">Discrete Math Proofs in 22 Minutes (5 Types, 9 Examples)</a> — TrevTutor, tiếng Anh. Tổng quan năm kiểu chứng minh trong toán rời rạc.
- <a href="https://www.youtube.com/watch?v=7_kiWYYLngQ">Loop Invariants - Principles of Imperative Computation (Carnegie Mellon University)</a> — Andy Guna, tiếng Anh. Giới thiệu bất biến vòng lặp, tương ứng phần chứng minh chương trình của bài học.
- <a href="https://www.youtube.com/watch?v=IZ7fyyAsOZc">What is a Loop Invariant?</a> — Juan Puebla, tiếng Anh. Giải thích bất biến vòng lặp là mệnh đề đúng trước và sau mỗi lần lặp.
