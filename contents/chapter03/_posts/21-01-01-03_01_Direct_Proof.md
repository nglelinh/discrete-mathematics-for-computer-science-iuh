---
layout: post
title: "Chứng minh Trực tiếp"
categories: chapter03
date: 2021-01-01
order: 1
required: true
lang: en
---

Từ bài toán kiểm tra điều kiện trong code đến việc chứng minh một thuật toán luôn cho kết quả đúng, ta đều gặp cùng một yêu cầu: nếu giả thiết đúng, kết luận phải đi ra một cách rõ ràng và không có khoảng trống lập luận.


Trong chứng minh, mục tiêu không chỉ là đi đến kết luận đúng mà còn cho thấy vì sao từng bước đều hợp lệ, giống như khi ta giải thích tính đúng đắn của một thuật toán.
**Chứng minh trực tiếp** là kỹ thuật cơ bản nhất để làm điều đó. Ta bắt đầu từ các giả thiết đã biết, dùng định nghĩa, tính chất và suy luận hợp lệ để tiến từng bước đến kết luận. Cách làm này rất gần với cách một lập trình viên giải thích vì sao một hàm hoạt động đúng với mọi đầu vào thỏa điều kiện tiền đề.

Điểm quan trọng là chứng minh trực tiếp rèn cho ta thói quen không nhảy bước. Trong toán rời rạc, chỉ một suy luận tưởng như hiển nhiên nhưng thiếu căn cứ cũng đủ làm hỏng toàn bộ chứng minh. Trong kỹ thuật phần mềm, đó cũng là khác biệt giữa một lập luận chắc chắn và một đoạn giải thích chỉ dựa vào trực giác.

Trong bài này, chúng ta sẽ bắt đầu với khuôn mẫu đơn giản nhất của chứng minh, rồi xem khi nào nên dùng nó và cách viết sao cho ngắn gọn nhưng chặt chẽ.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Nhận dạng** mệnh đề dạng "Nếu P thì Q" phù hợp với chứng minh trực tiếp.
- **Tách** giả thiết, kết luận và các định nghĩa cần dùng.
- **Viết** chứng minh trực tiếp rõ ràng, từng bước.
- **Áp dụng** chứng minh trực tiếp để giải thích tính đúng đắn của code đơn giản.
- **Tránh** các lỗi thường gặp như dùng kết luận làm giả thiết hoặc bỏ qua định nghĩa.

**Từ khóa**: Chứng minh trực tiếp (direct proof), giả thiết (hypothesis), kết luận (conclusion), định nghĩa (definition), bất biến (invariant), correctness.

## 1. Định nghĩa

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

**Chứng minh trực tiếp** của mệnh đề có dạng "Nếu P thì Q" ($$P \to Q$$) là một chuỗi suy luận bắt đầu bằng việc giả sử $$P$$ đúng, sau đó dùng định nghĩa, định lý đã biết và quy tắc logic để suy ra $$Q$$.

### Cấu trúc chung (5 bước trực quan)

**Bước 1**: **Giả sử** $$P$$ đúng.  
**Bước 2**: **Mở định nghĩa** của các khái niệm trong $$P$$.  
**Bước 3**: **Biến đổi** hoặc suy luận từng bước.  
**Bước 4**: **Đạt được** đúng dạng của $$Q$$.  
**Bước 5**: **Kết luận** mệnh đề đã được chứng minh.

![Chân dung Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid.jpg)

*Hình 3.1: Euclid — tác giả *Elements*, mô hình chứng minh trực tiếp từ giả thiết đến kết luận qua các bước suy luận hợp lệ.*

#### Minh họa trực quan: Cấu trúc chứng minh như một "đường hầm"

```
Giả thiết P ──────[các bước suy luận]──────▶ Kết luận Q
     ↑                                              ↑
  (đã biết)                                    (cần chứng minh)
```

**Mẹo thực tế**: Hãy tưởng tượng bạn đang **viết code** giải thích cho máy tính. Mỗi bước phải có "lý do" rõ ràng, giống như comment trong code.

<div class="content-box warning-box" markdown="1">
**Nguyên tắc quan trọng**: Trong chứng minh trực tiếp, bạn không được giả sử kết luận $$Q$$ đúng. Bạn chỉ được bắt đầu từ giả thiết $$P$$ và những định nghĩa/định lý đã biết.
</div>

## 2. Ví dụ toán học cơ bản

### Ví dụ 1: Số chẵn

**Định lý**: Nếu $$n$$ là số chẵn thì $$n^2$$ cũng là số chẵn.

**Chứng minh**:

1. Giả sử $$n$$ là số chẵn.
2. Theo định nghĩa số chẵn, tồn tại $$k \in \mathbb{Z}$$ sao cho $$n = 2k$$.
3. Khi đó:
   $$n^2 = (2k)^2 = 4k^2 = 2(2k^2)$$
4. Vì $$2k^2 \in \mathbb{Z}$$, nên $$n^2$$ có dạng $$2m$$ với $$m \in \mathbb{Z}$$.
5. Do đó $$n^2$$ là số chẵn. ∎

<div class="content-box insight-box" markdown="1">
**Phân tích**: Bước quan trọng nhất là bước 2 — mở định nghĩa "số chẵn" thành dạng $$n = 2k$$. Nếu không mở định nghĩa, bạn không có gì để biến đổi. Đây là kỹ năng cốt lõi của mọi chứng minh.
</div>

![Chứng minh định lý Pythagore](/discrete-mathematics-for-computer-science-iuh/img/course/Pythagorean_proof.svg)

*Hình 3.2: Chứng minh trực tiếp định lý Pythagore — minh họa cách đi từ giả thiết hình học đến kết luận bằng suy luận từng bước.*

### Ví dụ 2: Tổng của hai số lẻ

**Định lý**: Nếu $$a$$ và $$b$$ là hai số lẻ thì $$a+b$$ là số chẵn.

**Chứng minh**:

1. Giả sử $$a$$ và $$b$$ là số lẻ.
2. Theo định nghĩa, tồn tại $$m,n \in \mathbb{Z}$$ sao cho $$a = 2m+1$$ và $$b = 2n+1$$.
3. Khi đó:
   $$a+b = (2m+1)+(2n+1)=2m+2n+2=2(m+n+1)$$
4. Vì $$m+n+1 \in \mathbb{Z}$$, nên $$a+b$$ là số chẵn. ∎

### Ví dụ 3: Chia hết

**Định lý**: Nếu $$a \mid b$$ và $$b \mid c$$ thì $$a \mid c$$.

**Chứng minh**:

1. Giả sử $$a \mid b$$ và $$b \mid c$$.
2. Theo định nghĩa chia hết, tồn tại $$m,n \in \mathbb{Z}$$ sao cho $$b = am$$ và $$c = bn$$.
3. Thay $$b = am$$ vào $$c = bn$$, ta có:
   $$c = (am)n = a(mn)$$
4. Vì $$mn \in \mathbb{Z}$$, nên $$a \mid c$$. ∎

![Trang chứng minh Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid-proof.jpg)

*Hình 3.3: Trang chứng minh trong *Elements* — mẫu trình bày chứng minh trực tiếp cổ điển: giả thiết, định nghĩa, suy luận, kết luận.*

## 3. Ví dụ trong Khoa học Máy tính

### Ví dụ 4: Kiểm tra số chẵn trong code

Xét hàm Python:

```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

**Mệnh đề cần chứng minh**: Nếu `is_even(n)` trả về `True`, thì $$n$$ là số chẵn.

**Chứng minh trực tiếp**:

1. Giả sử `is_even(n)` trả về `True`.
2. Theo định nghĩa của hàm, điều này nghĩa là `n % 2 == 0`.
3. Theo định nghĩa phép chia có dư, tồn tại $$q \in \mathbb{Z}$$ sao cho $$n = 2q + 0 = 2q$$.
4. Do đó $$n$$ có dạng $$2q$$, nên $$n$$ là số chẵn. ∎

Điều này cho thấy chứng minh không chỉ dành cho toán: ta có thể chứng minh một hàm nhỏ làm đúng điều nó hứa.

![Đồ thị luồng điều khiển](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

*Hình 3.4: Đồ thị luồng điều khiển — mỗi nhánh tương ứng một bước suy luận trong chứng minh trực tiếp tính đúng đắn của code.*

### Ví dụ 5: Điều kiện phân quyền

```python
can_submit = is_enrolled and not is_locked and before_deadline
```

**Mệnh đề**: Nếu `can_submit` là `True`, thì sinh viên đang học lớp đó, tài khoản không bị khóa, và chưa quá hạn nộp bài.

**Chứng minh**:

1. Giả sử `can_submit` là `True`.
2. Biểu thức là phép hội của ba điều kiện: `is_enrolled`, `not is_locked`, `before_deadline`.
3. Một phép hội chỉ đúng khi tất cả thành phần đều đúng.
4. Do đó `is_enrolled = True`, `is_locked = False`, và `before_deadline = True`.
5. Vậy sinh viên đang học lớp, tài khoản không bị khóa, và chưa quá hạn. ∎

### Ví dụ 6: Bất biến vòng lặp đơn giản

```python
total = 0
for x in numbers:
    total += x
```

**Bất biến**: Sau khi xử lý $$k$$ phần tử đầu tiên, `total` bằng tổng của $$k$$ phần tử đó.

Chứng minh bất biến này thường dùng quy nạp, nhưng bước chuyển "nếu trước vòng lặp đúng thì sau khi cộng thêm phần tử kế tiếp vẫn đúng" là một chứng minh trực tiếp nhỏ:

1. Giả sử trước bước hiện tại, `total = numbers[0] + ... + numbers[k-1]`.
2. Bước hiện tại thực hiện `total += numbers[k]`.
3. Sau bước đó, `total = numbers[0] + ... + numbers[k-1] + numbers[k]`.
4. Vậy bất biến vẫn đúng cho $$k+1$$ phần tử.

<div class="interactive-tool" markdown="1">
## 4. Checklist khi viết chứng minh trực tiếp

- Gạch chân giả thiết và kết luận.
- Viết lại các định nghĩa liên quan.
- Không bắt đầu bằng điều cần chứng minh.
- Mỗi bước phải có lý do: định nghĩa, tính chất đại số, định lý đã biết, hoặc suy luận logic.
- Kết luận cuối cùng phải đúng dạng của mệnh đề cần chứng minh.

## 5. Phong cách viết chứng minh

Một chứng minh không chỉ đúng mà còn phải dễ đọc. Dưới đây là một số nguyên tắc từ tài liệu tham khảo *Discrete Math* (Watson, 2026):

### 5.1. Cân bằng giữa ký hiệu và văn xuôi

Khi viết chứng minh, hãy dùng câu tiếng Việt hoàn chỉnh, diễn đạt luồng logic bằng các từ như **"với mọi"** thay vì ∀, **"và"** thay vì ∧, **"nếu...thì"** thay vì ⇒. Ký hiệu và công thức như $$x+1$$ nên là một phần của câu.

Có sự đánh đổi: chứng minh sẽ khó đọc nếu quá dày đặc ký hiệu trong khi văn xuôi đơn giản đã đủ; nhưng chứng minh cũng sẽ nặng nề nếu dùng quá nhiều văn xuôi trong khi ký hiệu ngắn gọn, súc tích sẽ tốt hơn.

> **Ví dụ**: Thay vì viết:
> ```
> ∀x∈ℤ, x>0 ⇒ x+1>0
> ```
> Hãy viết:
> "Với mọi số nguyên dương $$x$$, ta có $$x+1 > 0$$."

### 5.2. Tính chặt chẽ (rigor)

Một chứng minh là một dãy các mệnh đề, mỗi mệnh đề hoặc là một sự thật hiển nhiên (như "$$x+y \le x$$ nếu $$y \le 0$$") hoặc suy ra từ các mệnh đề trước bằng một quy tắc logic hiển nhiên (như "nếu $$P \lor Q$$ và $$\lnot P$$ đã được thiết lập, thì $$Q$$ có thể suy ra").

Mặc dù từng bước có thể rất đơn giản, toàn bộ chứng minh có thể đáng ngạc nhiên và thanh lịch. Những nốt nhạc riêng lẻ có thể nhàm chán, nhưng khi kết hợp đúng cách sẽ tạo nên một giai điệu đẹp.

### 5.3. Ví dụ và phản ví dụ (Counterexamples)

Khi gặp mệnh đề dạng "với mọi $$x$$, $$P(x)$$ đúng", cách nhanh nhất để bác bỏ nó là tìm một **phản ví dụ** — một giá trị $$x$$ làm $$P(x)$$ sai.

> **Ví dụ**: Mệnh đề "mọi số nguyên tố đều là số lẻ" — phản ví dụ là $$2$$.
>
> **Ví dụ**: Mệnh đề "với mọi số thực $$a,b$$, $$(a+b)^2 = a^2 + b^2$$" — phản ví dụ là $$a=1, b=1$$ vì $$(1+1)^2 = 4 \ne 1+1 = 2$$.

Ngược lại, để khẳng định một mệnh đề tồn tại "có $$x$$ sao cho $$P(x)$$ đúng", chỉ cần đưa ra một **ví dụ cụ thể**.

> **Ví dụ**: "Tồn tại số nguyên $$n$$ sao cho $$n^2 - n + 41$$ là hợp số." Ví dụ: $$n = 41$$ cho $$41^2 - 41 + 41 = 41^2$$, là hợp số.

![Bản in Elements của Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid_s_Elements__1482.jpg)

*Hình 3.5: Bản in *Elements* (1482) — tiêu chuẩn vàng của chứng minh trực tiếp: mỗi bước phải có căn cứ, không nhảy cóc.*

Kỹ thuật này rất hữu ích trong khoa học máy tính: khi ai đó khẳng định "thuật toán này luôn chạy trong $$O(n)$$", một phản ví dụ về input làm nó chạy $$O(n^2)$$ là đủ để bác bỏ.

