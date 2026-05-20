---
layout: post
title: "Chứng minh Trực tiếp"
categories: chapter03
date: 2021-01-01
order: 1
required: true
lang: en
---

# Chứng minh Trực tiếp

Chạy vài test case và thấy kết quả đúng không có nghĩa là mệnh đề luôn đúng. Một hàm có thể qua 100 bộ dữ liệu nhưng vẫn hỏng ở trường hợp thứ 101; một lập luận nghe hợp lý vẫn có thể sai vì thiếu đúng một bước trung gian. Toán học cần nhiều hơn niềm tin, và khoa học máy tính cũng vậy.

**Chứng minh trực tiếp** là cách đi thẳng từ giả thiết đến kết luận, từng bước một, không dựa vào cảm giác. Đây là kiểu tư duy đứng sau việc giải thích vì sao một thuật toán đúng, vì sao một điều kiện đủ chặt, hay vì sao một tính chất luôn giữ được sau mỗi bước xử lý. Học nó không chỉ để viết chứng minh đẹp, mà để tập suy nghĩ như người xây hệ thống đáng tin cậy.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Nhận dạng** mệnh đề dạng "Nếu P thì Q" phù hợp với chứng minh trực tiếp.
- **Tách** giả thiết, kết luận và các định nghĩa cần dùng.
- **Viết** chứng minh trực tiếp rõ ràng, từng bước.
- **Áp dụng** chứng minh trực tiếp để giải thích tính đúng đắn của code đơn giản.
- **Tránh** các lỗi thường gặp như dùng kết luận làm giả thiết hoặc bỏ qua định nghĩa.

**Từ khóa**: Chứng minh trực tiếp (direct proof), giả thiết (hypothesis), kết luận (conclusion), định nghĩa (definition), bất biến (invariant), correctness.

## Cấu trúc bài giảng (60 phút)

| Thời gian | Nội dung | Hoạt động |
|-----------|----------|-----------|
| 5 phút | Mở đầu | Vì sao test không thay thế chứng minh? |
| 10 phút | Cấu trúc chứng minh trực tiếp | P → Q, giả thiết, kết luận |
| 15 phút | Ví dụ số học | Số chẵn, số lẻ, chia hết |
| 15 phút | Ví dụ khoa học máy tính | Input validation, loop invariant, hàm lọc dữ liệu |
| 10 phút | Lỗi thường gặp | Suy luận ngược, thiếu định nghĩa |
| 5 phút | Tổng kết | Checklist viết chứng minh |

## 1. Định nghĩa

**Chứng minh trực tiếp** của mệnh đề có dạng "Nếu P thì Q" ($$P \to Q$$) là một chuỗi suy luận bắt đầu bằng việc giả sử $$P$$ đúng, sau đó dùng định nghĩa, định lý đã biết và quy tắc logic để suy ra $$Q$$.

### Cấu trúc chung

1. **Giả sử** $$P$$ đúng.
2. **Mở định nghĩa** của các khái niệm trong $$P$$.
3. **Biến đổi** hoặc suy luận từng bước.
4. **Đạt được** đúng dạng của $$Q$$.
5. **Kết luận** mệnh đề đã được chứng minh.

<div class="content-box warning-box" markdown="1">
**Nguyên tắc quan trọng**: Trong chứng minh trực tiếp, bạn không được giả sử kết luận $$Q$$ đúng. Bạn chỉ được bắt đầu từ giả thiết $$P$$ và những định nghĩa/định lý đã biết.
</div>

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter03/direct_proof_flow.svg" alt="Sơ đồ cấu trúc chứng minh trực tiếp: từ giả thiết đến kết luận qua các bước suy luận" width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 3.1: Cấu trúc chứng minh trực tiếp — bắt đầu từ giả thiết P, qua các bước suy luận (mỗi bước có lý do), đi đến kết luận Q</figcaption>
</p>
</figure>

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
### Công cụ tương tác: Các bước chứng minh

Sắp xếp các bước sau thành chứng minh trực tiếp đúng cho định lý "Nếu n là số lẻ thì n² là số lẻ":

<select id="step1" style="width: 100%; padding: 8px; margin: 5px 0;">
  <option value="">Chọn bước 1...</option>
  <option value="a">n² = (2k+1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1</option>
  <option value="b">Giả sử n là số lẻ</option>
  <option value="c">Vậy n² là số lẻ</option>
  <option value="d">Theo định nghĩa, tồn tại k∈ℤ sao cho n = 2k+1</option>
</select>
<button onclick="checkProofOrder()" style="margin: 10px 0;">Kiểm tra</button>
<div id="proof-result" style="margin-top: 10px; padding: 10px; background: #f8f9fa; border-radius: 6px;"></div>

<script>
function checkProofOrder() {
    const s1 = document.getElementById('step1').value;
    const result = document.getElementById('proof-result');
    if (s1 === 'b') {
        result.innerHTML = 'Đúng! Bước 1 là "Giả sử n là số lẻ". Hãy tiếp tục với: mở định nghĩa → biến đổi → kết luận.';
    } else {
        result.innerHTML = 'Hãy nhớ: chứng minh trực tiếp bắt đầu bằng giả thiết, không phải bằng kết luận hay biến đổi.';
    }
}
</script>
</div>

## 4. Checklist khi viết chứng minh trực tiếp

- Gạch chân giả thiết và kết luận.
- Viết lại các định nghĩa liên quan.
- Không bắt đầu bằng điều cần chứng minh.
- Mỗi bước phải có lý do: định nghĩa, tính chất đại số, định lý đã biết, hoặc suy luận logic.
- Kết luận cuối cùng phải đúng dạng của mệnh đề cần chứng minh.

## 5. Lỗi thường gặp

### Lỗi 1: Chứng minh ngược

Sai: Muốn chứng minh "n chẵn ⇒ n² chẵn", nhưng bắt đầu bằng "Giả sử n² chẵn".

Đó là chứng minh chiều ngược, không phải chứng minh trực tiếp cho mệnh đề ban đầu.

### Lỗi 2: Bỏ qua định nghĩa

Không nên viết: "n chẵn nên n² chẵn là hiển nhiên".

Cần mở định nghĩa: $$n = 2k$$, rồi biến đổi.

### Lỗi 3: Dùng ví dụ thay cho chứng minh

Kiểm tra $$n=2,4,6$$ không đủ để chứng minh cho mọi số chẵn. Ví dụ giúp hiểu; chứng minh cần bao quát mọi trường hợp.

## Ứng dụng trong Khoa học Máy tính

Chứng minh trực tiếp được dùng khi ta cần bảo đảm một đoạn logic luôn đúng. Ví dụ: chứng minh hàm kiểm tra quyền truy cập không cấp quyền sai, chứng minh một bộ lọc SQL không trả về dữ liệu ngoài phạm vi, hoặc chứng minh một thuật toán đơn giản luôn trả về kết quả thỏa điều kiện.

Trong kiểm thử phần mềm, test case chỉ kiểm tra một số đầu vào cụ thể. Chứng minh trực tiếp giúp ta hiểu lý do vì sao code đúng cho mọi đầu vào hợp lệ — đặc biệt quan trọng với bảo mật, tài chính, y tế và hệ thống nhúng.

## Bài tập thực hành

### Bài tập 1: Số chẵn và số lẻ

Chứng minh trực tiếp:

1. Nếu $$n$$ là số lẻ thì $$n^2$$ là số lẻ.
2. Nếu $$a$$ là số chẵn và $$b$$ là số lẻ thì $$a+b$$ là số lẻ.
3. Nếu $$a \mid b$$ thì $$a \mid bc$$ với mọi $$c \in \mathbb{Z}$$.

### Bài tập 2: Logic trong code

Cho đoạn code:

```python
can_view_grade = is_logged_in and is_in_class and grade_published
```

Chứng minh trực tiếp: nếu `can_view_grade` là `True`, thì sinh viên đã đăng nhập, thuộc lớp học phần, và điểm đã được công bố.

### Bài tập 3: Kiểm tra đầu vào

Một API chỉ nhận request hợp lệ nếu:

```python
valid_request = has_token and token_not_expired and payload_size <= 1024
```

1. Đặt các mệnh đề sơ cấp.
2. Viết mệnh đề logic.
3. Chứng minh trực tiếp: nếu `valid_request` đúng thì request có token, token chưa hết hạn, và payload không vượt quá 1024 bytes.

### Bài tập 4: Tìm lỗi chứng minh

Sinh viên viết: "Giả sử $$n^2$$ chẵn. Khi đó $$n$$ chẵn. Vậy nếu $$n$$ chẵn thì $$n^2$$ chẵn."

1. Lỗi nằm ở đâu?
2. Hãy viết lại chứng minh đúng.

### Bài tập 5: Bất biến nhỏ

Cho thuật toán tìm giá trị lớn nhất trong mảng. Chứng minh trực tiếp rằng sau mỗi lần cập nhật `max_value = a[i]`, biến `max_value` vẫn là một phần tử đã xuất hiện trong đoạn mảng đã duyệt.

## Tóm tắt

- Chứng minh trực tiếp bắt đầu từ giả thiết và đi đến kết luận.
- Công cụ quan trọng nhất là mở đúng định nghĩa.
- Trong CS, chứng minh trực tiếp giúp giải thích vì sao điều kiện, hàm, hoặc bước thuật toán luôn đúng.
- Test case rất hữu ích, nhưng không thay thế được chứng minh khi ta cần bảo đảm cho mọi đầu vào.

Trong bài tiếp theo, chúng ta sẽ học về **chứng minh phản chứng** — một phương pháp mạnh để chứng minh các mệnh đề khó đi thẳng từ giả thiết.
