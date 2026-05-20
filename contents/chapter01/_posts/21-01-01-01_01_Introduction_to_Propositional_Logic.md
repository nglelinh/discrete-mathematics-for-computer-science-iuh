---
layout: post
title: "Giới thiệu Logic Mệnh đề"
categories: chapter01
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Logic Mệnh đề

Mỗi lần bạn viết `if (score >= 5)` hay thêm điều kiện `WHERE status = "active"`, bạn đang buộc máy tính phải trả lời một câu hỏi rất cổ điển: **mệnh đề này đúng hay sai?** 

Nghe có vẻ đơn giản, nhưng chính kiểu quyết định nhị phân này — đúng hoặc sai, 1 hoặc 0, true hoặc false — là viên gạch đầu tiên xây nên toàn bộ tòa nhà khoa học máy tính. Từ điều kiện `if` trong code, đến truy vấn SQL lọc hàng triệu bản ghi, đến mạch logic bên trong CPU quyết định mở hay đóng transistor, tất cả đều dựa trên một nền tảng chung: **logic mệnh đề**.

Nhưng tại sao một khái niệm nghe có vẻ "hiển nhiên" như vậy lại cần được học một cách chính thức? Câu trả lời nằm ở chỗ: khi hệ thống phức tạp lên, trực giác của con người rất dễ sai. Một điều kiện nhìn "hợp lý" vẫn có thể cho kết quả ngược lại ở đúng một trường hợp hiếm gặp. Một câu yêu cầu nghiệp vụ viết bằng tiếng Việt có thể bị hiểu theo nhiều cách khác nhau. Một đoạn code "chạy được" không có nghĩa là "đúng với mọi đầu vào".

Logic mệnh đề ra đời để biến những câu khẳng định đời thường — mơ hồ, chủ quan, dễ hiểu lầm — thành thứ có thể **kiểm tra, phân tích và tính toán** một cách chính xác tuyệt đối. Khi biết cách nhìn một phát biểu dưới lăng kính đúng/sai, bạn không chỉ học toán chặt chẽ hơn mà còn:

- Viết điều kiện ít mơ hồ hơn, giảm bug logic.
- Thiết kế test case bao phủ đủ trường hợp.
- Đọc hiểu yêu cầu nghiệp vụ chính xác hơn.
- Hiểu cách máy tính "suy nghĩ" ở tầng thấp nhất.

Trong bài học này, chúng ta sẽ bắt đầu từ câu hỏi căn bản nhất: **Mệnh đề là gì? Và tại sao không phải mọi câu đều là mệnh đề?**

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Nhận biết** câu nào là mệnh đề và câu nào không phải mệnh đề.
- **Gán** ký hiệu logic cho các mệnh đề trong bài toán thực tế.
- **Phân biệt** mệnh đề sơ cấp và mệnh đề phức hợp.
- **Giải thích** vì sao logic mệnh đề quan trọng trong lập trình, cơ sở dữ liệu, AI và bảo mật.
- **Chuyển đổi** một yêu cầu nghiệp vụ đơn giản thành điều kiện logic để dùng trong code.

**Từ khóa**: Mệnh đề (proposition), giá trị chân lý (truth value), mệnh đề sơ cấp (atomic proposition), mệnh đề phức hợp (compound proposition), logic trong lập trình.

## Mệnh đề là gì?

**Định nghĩa**: Mệnh đề (proposition) là một câu khẳng định có thể xác định được tính đúng hoặc sai, nhưng không thể vừa đúng vừa sai.

### Ví dụ về mệnh đề:
- "2 + 3 = 5" (đúng)
- "Hà Nội là thủ đô của Việt Nam" (đúng)  
- "5 > 10" (sai)
- "Tất cả số nguyên tố đều là số lẻ" (sai, vì 2 là số nguyên tố chẵn)

### Ví dụ KHÔNG phải mệnh đề:
- "x + 1 = 5" (phụ thuộc vào giá trị của x)
- "Hôm nay trời đẹp quá!" (mang tính chủ quan)
- "Mấy giờ rồi?" (câu hỏi)
- "Hãy đóng cửa!" (câu mệnh lệnh)

## Ký hiệu mệnh đề

Chúng ta thường dùng các chữ cái như p, q, r, s,... để ký hiệu các mệnh đề.

**Ví dụ**:
- p: "Hôm nay là thứ hai"
- q: "Trời đang mưa"
- r: "2 + 2 = 4"

## Giá trị chân lý

Mỗi mệnh đề có một **giá trị chân lý** (truth value):
- **1** (True/Đúng) hoặc ký hiệu T: mệnh đề đúng
- **0** (False/Sai) hoặc ký hiệu F: mệnh đề sai

Một mệnh đề chỉ có thể mang giá trị 1 hoặc 0, không thể đồng thời vừa đúng vừa sai.

## Phân loại mệnh đề

**Mệnh đề sơ cấp** (elementary/atomic proposition) là mệnh đề không thể xây dựng từ các mệnh đề khác thông qua liên từ hoặc trạng từ "không".

**Ví dụ về mệnh đề sơ cấp**:
- "2 là số nguyên tố."
- "p: Hà Nội là thủ đô của Việt Nam."
- "q: 5 > 10."

**Mệnh đề phức hợp** (compound proposition) là mệnh đề được xây dựng từ các mệnh đề sơ cấp bằng cách dùng các liên từ như "và", "hoặc", "nếu...thì...", "khi và chỉ khi" hoặc trạng từ "không".

**Ví dụ về mệnh đề phức hợp**:
- "2 là số nguyên tố **và** 3 là số lẻ" (kết hợp hai mệnh đề bằng "và")
- "**Nếu** trời mưa **thì** đường ướt"

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter01/proposition_venn.svg" alt="Sơ đồ phân loại câu thành mệnh đề và không phải mệnh đề" width="60%" height="60%">
  <figcaption style="text-align: center;">Hình 1.1: Phân loại câu — mệnh đề là những câu khẳng định có giá trị chân lý xác định</figcaption>
</p>
</figure>

## Những nhầm lẫn thường gặp

Khi mới học logic mệnh đề, sinh viên thường mắc những lỗi sau:

**Nhầm lẫn 1 — Câu hỏi tu từ**: "Ai mà chẳng biết điều đó?" tuy là câu hỏi nhưng mang hàm ý khẳng định. Tuy nhiên, trong logic mệnh đề, ta chỉ xét câu khẳng định trực tiếp, không xét hàm ý.

**Nhầm lẫn 2 — Câu có biến**: "x > 5" không phải mệnh đề vì chưa biết x là gì. Nhưng nếu ta nói "Tồn tại x sao cho x > 5" thì đó lại là một mệnh đề (sẽ học ở chương 2).

**Nhầm lẫn 3 — Tính chủ quan**: "Trà sữa ngon" không phải mệnh đề vì không có chuẩn khách quan để xác định đúng/sai. Đây là ý kiến cá nhân, không phải sự thật khách quan.

## Ứng dụng trong Khoa học Máy tính

### 1. Trong Lập trình

Mọi điều kiện trong câu lệnh `if`, `while`, hay biểu thức Boolean đều là mệnh đề:

```python
age = 18
is_student = True
has_valid_id = True

if age >= 18 and is_student and has_valid_id:
    print("Được nhận ưu đãi sinh viên")
```

Trong ví dụ này:

- `age >= 18` là một mệnh đề: đúng hoặc sai tại thời điểm chạy.
- `is_student` là một mệnh đề Boolean.
- `has_valid_id` là một mệnh đề Boolean.
- Toàn bộ điều kiện là một mệnh đề phức hợp.

Nếu bạn hiểu logic mệnh đề, bạn sẽ đọc được điều kiện phức tạp, phát hiện lỗi `and/or`, và viết test case tốt hơn.

### 2. Trong Cơ sở dữ liệu

Truy vấn SQL cũng là logic mệnh đề:

```sql
SELECT * FROM students
WHERE gpa >= 3.2 AND credits >= 60 AND status = 'active';
```

Mỗi dòng dữ liệu được kiểm tra bởi một mệnh đề. Nếu mệnh đề đúng, dòng đó xuất hiện trong kết quả; nếu sai, dòng đó bị loại.

### 3. Trong Bảo mật

Các hệ thống phân quyền dùng logic để quyết định ai được làm gì:

```python
can_delete = is_admin or (is_owner and not is_locked)
```

Câu này nghĩa là: người dùng được xóa nếu họ là admin, hoặc nếu họ là chủ sở hữu và tài nguyên chưa bị khóa. Một dấu ngoặc sai có thể tạo lỗ hổng bảo mật.

### 4. Trong Trí tuệ Nhân tạo

Hệ chuyên gia, kiểm chứng chương trình, SAT solver và nhiều kỹ thuật AI cổ điển đều dựa trên logic mệnh đề.

## Ví dụ thực tế: Từ yêu cầu đến điều kiện logic

<div class="content-box example-box" markdown="1">
**Yêu cầu nghiệp vụ**: Sinh viên được đăng ký môn học nếu:

1. Đã đóng học phí.
2. Không bị khóa tài khoản.
3. Đã học xong môn tiên quyết hoặc được cố vấn cho phép học song hành.

Ký hiệu:

- $$p$$: Sinh viên đã đóng học phí.
- $$q$$: Tài khoản không bị khóa.
- $$r$$: Đã học xong môn tiên quyết.
- $$s$$: Được cố vấn cho phép học song hành.

Điều kiện đăng ký:

$$p \land q \land (r \lor s)$$

Trong code:

```python
can_register = paid_tuition and account_active and (passed_prerequisite or advisor_approved)
```
</div>

<div class="interactive-tool" markdown="1">
### Công cụ tương tác: Kiểm tra mệnh đề

Nhập một câu vào ô dưới đây và thử xác định xem nó có phải mệnh đề không:

<input type="text" id="prop-check-input" placeholder="Ví dụ: 2 + 2 = 4" style="width: 80%; padding: 8px; margin: 10px 0;">
<button onclick="checkProposition()">Kiểm tra</button>
<div id="prop-check-result" style="margin-top: 10px; padding: 10px; background: #f8f9fa; border-radius: 6px;"></div>

<script>
function checkProposition() {
    const input = document.getElementById('prop-check-input').value.trim();
    const result = document.getElementById('prop-check-result');
    if (!input) {
        result.innerHTML = '<span style="color: #e63946;">Vui lòng nhập một câu!</span>';
        return;
    }
    result.innerHTML = 'Gợi ý: Hãy tự hỏi — câu này có thể xác định đúng/sai một cách khách quan không? Nếu có thể thì nó là mệnh đề. Nếu là câu hỏi, câu mệnh lệnh, hoặc ý kiến chủ quan thì không.';
}
</script>
</div>

## Bài tập thực hành

### Bài tập 1: Xác định mệnh đề
Xác định câu nào sau đây là mệnh đề và xác định giá trị chân lý:

1. "Python là ngôn ngữ lập trình"
2. "x² = 4"  
3. "Hãy học bài!"
4. "Nếu n là số chẵn thì n chia hết cho 2"
5. "Bạn có thích toán không?"

<details>
<summary>Đáp án</summary>

1. **Mệnh đề** - Giá trị: T (đúng)
2. **Không phải mệnh đề** - Phụ thuộc vào giá trị của x
3. **Không phải mệnh đề** - Câu mệnh lệnh
4. **Mệnh đề** - Giá trị: T (đúng)
5. **Không phải mệnh đề** - Câu hỏi

</details>

### Bài tập 2: Ký hiệu hóa
Cho các mệnh đề sau, hãy ký hiệu bằng các chữ cái:

- "Hôm nay là chủ nhật"
- "Tôi có bài kiểm tra"  
- "Thư viện mở cửa"
- "Tôi sẽ đi học"

Sau đó viết mệnh đề phức hợp: "Nếu hôm nay là chủ nhật và tôi có bài kiểm tra, thì tôi sẽ đi học nếu thư viện mở cửa"

### Bài tập 3: Logic trong hệ thống thực tế

Một website cho phép người dùng tải file nếu người đó đã đăng nhập, email đã xác thực, và dung lượng file nhỏ hơn 10MB hoặc người đó là tài khoản Premium.

1. Đặt ký hiệu cho từng mệnh đề sơ cấp.
2. Viết mệnh đề phức hợp biểu diễn điều kiện tải file.
3. Viết điều kiện tương ứng bằng Python hoặc JavaScript.

## Tóm tắt

- **Mệnh đề** là câu khẳng định có thể xác định được tính đúng/sai
- Mỗi mệnh đề có **giá trị chân lý**: T (đúng) hoặc F (sai)
- Logic mệnh đề là nền tảng cho toán học và khoa học máy tính
- Ký hiệu mệnh đề bằng các chữ cái: p, q, r,...
- Cần phân biệt mệnh đề với câu hỏi, câu mệnh lệnh, và ý kiến chủ quan

Trong bài tiếp theo, chúng ta sẽ học về các **phép toán logic** để kết hợp các mệnh đề đơn giản thành các mệnh đề phức tạp hơn.
