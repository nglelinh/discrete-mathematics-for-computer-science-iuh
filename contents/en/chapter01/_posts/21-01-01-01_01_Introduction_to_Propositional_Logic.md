---
layout: post
title: "Giới thiệu Logic Mệnh đề"
categories: chapter01
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Logic Mệnh đề

Logic mệnh đề là nền tảng của toán học rời rạc và khoa học máy tính. Nó cung cấp các công cụ để phân tích và xây dựng các lập luận logic một cách chính xác.

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
- **T** (True) hoặc **1**: mệnh đề đúng
- **F** (False) hoặc **0**: mệnh đề sai

## Tại sao Logic Mệnh đề quan trọng?

### 1. Trong Toán học
- Xây dựng các chứng minh logic
- Phân tích tính đúng đắn của các lập luận
- Nền tảng cho các phương pháp chứng minh

### 2. Trong Khoa học Máy tính
- Thiết kế mạch logic
- Lập trình (câu lệnh điều kiện if-then-else)
- Cơ sở dữ liệu (truy vấn SQL)
- Trí tuệ nhân tạo (hệ chuyên gia)

### 3. Trong Lập trình
```python
# Ví dụ trong Python
age = 18
is_student = True

# Logic mệnh đề trong điều kiện
if age >= 18 and is_student:
    print("Được giảm giá học phí")
```

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

## Tóm tắt

- **Mệnh đề** là câu khẳng định có thể xác định được tính đúng/sai
- Mỗi mệnh đề có **giá trị chân lý**: T (đúng) hoặc F (sai)
- Logic mệnh đề là nền tảng cho toán học và khoa học máy tính
- Ký hiệu mệnh đề bằng các chữ cái: p, q, r,...

Trong bài tiếp theo, chúng ta sẽ học về các **phép toán logic** để kết hợp các mệnh đề đơn giản thành các mệnh đề phức tạp hơn.
