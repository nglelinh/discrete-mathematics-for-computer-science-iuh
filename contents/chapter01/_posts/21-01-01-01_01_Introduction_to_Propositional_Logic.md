---
layout: post
title: "Giới thiệu Logic Mệnh đề"
categories: chapter01
date: 2021-01-01
order: 1
required: true
lang: en
---

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

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/assets/img/01-01-propositional-logic/aristotle-logic.svg" alt="Aristotle - cha đẻ của logic" width="40%" height="40%">
  <figcaption style="text-align: center;">Hình 1.1: Aristotle (384–322 TCN) — người đầu tiên hệ thống hóa các quy luật suy luận</figcaption>
</p>
</figure>

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

## Logic học nghiên cứu cái gì?

**Logic học** (logic) là ngành khoa học nghiên cứu các quy tắc suy luận hợp lý — làm thế nào để từ những tiền đề đúng rút ra kết luận đúng.

### Đối tượng nghiên cứu của logic học

Logic học không quan tâm đến **nội dung** cụ thể của các phát biểu, mà chỉ quan tâm đến **hình thức** (cấu trúc) của chúng:

| Khía cạnh | Logic học quan tâm | Logic học KHÔNG quan tâm |
|:---|:---|:---|
| Hình thức | Cấu trúc "Nếu P thì Q" | Nội dung cụ thể của P và Q |
| Giá trị chân lý | Mối quan hệ đúng/sai | Ý nghĩa thực tế của câu |
| Suy luận | Quy tắc từ tiền đề đến kết luận | Chủ đề của cuộc tranh luận |

**Ví dụ**: Cả hai câu sau đều có cùng hình thức logic:
- "Nếu trời mưa thì đường ướt"
- "Nếu n chẵn thì n² chẵn"

Logic học chỉ quan tâm đến cấu trúc `Nếu P thì Q`, không quan tâm P là "trời mưa" hay "n chẵn".

### Ví dụ thực tế: Tranh cãi trên mạng xã hội

Một cuộc tranh cãi trên Facebook:

> **Người A**: "Nếu bạn yêu nước thì phải ủng hộ chính sách X."
> **Người B**: "Tôi không ủng hộ chính sách X, nhưng tôi vẫn yêu nước!"

Hai người đang nói về cùng một cấu trúc logic: **Nếu P thì Q**.

Ký hiệu:
- $$p$$: Yêu nước
- $$q$$: Ủng hộ chính sách X

**Người A** ngụ ý: $$p \to q$$ (Yêu nước → Ủng hộ X)

**Người B** phản bác: $$\neg q \land p$$ (Không ủng hộ X VÀ vẫn yêu nước)

**Phân tích logic**:
- Câu "Nếu yêu nước thì phải ủng hộ X" là một **mệnh đề kéo theo** (implication).
- Người A đang khẳng định $$p \to q$$ đúng.
- Người B đang phủ nhận điều này bằng cách đưa ra trường hợp $$p$$ đúng nhưng $$q$$ sai — đúng theo định nghĩa của implication (xem chương sau).
- Cuộc tranh cãi thực chất là về **nội dung** của p và q, không phải về **hình thức** logic.

**Bài học**: Nhiều tranh cãi trên mạng xã hội thực ra là tranh cãi về **ý nghĩa** của các mệnh đề, chứ không phải về **cấu trúc suy luận**. Logic học giúp ta tách biệt hai khía cạnh này để tranh luận rõ ràng hơn.

### Ví dụ thực tế: Luật an toàn giao thông (từ 1/7)

Từ ngày 1/7, khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 m, xe ô tô gia đình, xe cá nhân **phải lắp ghế trẻ em**.

**Phân tích logic**:

Ký hiệu:
- $$p$$: Trẻ em dưới 10 tuổi
- $$q$$: Trẻ em chiều cao dưới 1,35 m
- $$r$$: Xe ô tô gia đình hoặc xe cá nhân
- $$s$$: Lắp ghế trẻ em

**Điều kiện bắt buộc**:

$$(p \land q \land r) \to s$$

Nghĩa là: **Nếu** (trẻ dưới 10 tuổi **VÀ** cao dưới 1,35 m **VÀ** đi xe gia đình/cá nhân) **thì phải** lắp ghế trẻ em.

**Ứng dụng trong code** (hệ thống kiểm tra đăng ký xe):

```python
def can_register_without_child_seat(age, height, vehicle_type):
    """
    Kiểm tra điều kiện miễn lắp ghế trẻ em.
    Trả về True nếu KHÔNG cần lắp ghế.
    """
    is_child = age < 10
    is_short = height < 1.35
    is_personal = vehicle_type in ['family', 'personal']
    
    # Nếu là trẻ em dưới tiêu chuẩn VÀ đi xe cá nhân → BẮT BUỘC lắp ghế
    requires_child_seat = is_child and is_short and is_personal
    
    return not requires_child_seat
```

**Bài học**: Luật giao thông thường được viết dưới dạng **mệnh đề kéo theo** (implication). Hiểu logic giúp ta:
- Viết điều kiện kiểm tra chính xác trong phần mềm
- Tránh nhầm lẫn giữa `and`/`or` khi chuyển luật thành code
- Thiết kế test case bao phủ đủ trường hợp biên (tuổi = 10, cao = 1,35 m, xe công vụ...)

## Định lý bất toàn (Gödel)

Năm 1931, nhà toán học **Kurt Gödel** chứng minh hai định lý cách mạng, cho thấy **giới hạn cơ bản của mọi hệ thống logic hình thức**.

### Định lý bất toàn thứ nhất

> **Trong mọi hệ thống logic đủ mạnh để biểu diễn số học, luôn tồn tại những mệnh đề đúng nhưng không thể chứng minh được trong hệ thống đó.**

Nói cách khác: Không có hệ thống logic nào có thể chứng minh được **tất cả** các mệnh đề đúng. Luôn có "khe hở" — những sự thật toán học đúng nhưng không thể chứng minh từ các tiên đề của hệ thống.

### Định lý bất toàn thứ hai

> **Một hệ thống logic nhất quán không thể chứng minh được tính nhất quán của chính nó.**

Nếu một hệ thống có thể chứng minh rằng nó không mâu thuẫn, thì chính nó đã mâu thuẫn. Nói cách khác: Bạn không thể "tự chứng minh mình đúng" từ bên trong hệ thống.

### Ý nghĩa thực tiễn

| Ý nghĩa | Ứng dụng trong khoa học máy tính |
|:---|:---|
| Không thể tự động hóa mọi chứng minh | Không có thuật toán nào kiểm tra được mọi chương trình đúng/sai |
| Luôn có "lỗ hổng" trong hệ thống | Cần kiểm tra thủ công hoặc dùng nhiều hệ thống |
| Liên hệ với bài toán dừng (Halting Problem) | Không thể viết chương trình dự đoán mọi chương trình có dừng hay không |

**Liên hệ với lập trình**: Định lý bất toàn giải thích tại sao không thể viết một "siêu trình biên dịch" tự động phát hiện mọi lỗi logic trong code — luôn có những trường hợp không thể quyết định được.

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

## Định lý quan trọng: Số lượng hàm Boolean

**Định lý**: Trên một tập hợp gồm \( n \) biến mệnh đề, có **đúng \( 2^{2^n} \)** hàm Boolean khác nhau.

**Chứng minh**:

1. Mỗi assignment cho \( n \) biến có thể được xem như một vector trong \( \{T,F\}^n \). Có đúng \( 2^n \) vector như vậy.

2. Một hàm Boolean \( f \) được xác định hoàn toàn bởi giá trị của nó trên từng vector. Nghĩa là, ta cần chỉ định cho mỗi vector một giá trị \( T \) hoặc \( F \).

3. Với mỗi vector, có 2 lựa chọn. Do đó, tổng số cách chỉ định là:
   $$
   2 \times 2 \times \cdots \times 2 \quad (2^n \text{ lần}) = 2^{2^n}.
   $$

**Hệ quả quan trọng**:
- Với \( n = 1 \): có \( 2^{2} = 4 \) hàm Boolean (hằng đúng, hằng sai, identity, NOT).
- Với \( n = 2 \): có \( 2^{4} = 16 \) hàm Boolean (bao gồm AND, OR, XOR, implication, v.v.).
- Với \( n = 3 \): đã có \( 2^{8} = 256 \) hàm Boolean.
- Với \( n = 10 \): con số lên tới \( 2^{1024} \approx 10^{308} \), lớn hơn số nguyên tử trong vũ trụ.

**Ý nghĩa trong Khoa học Máy tính**:
- **Bảng chân trị** chỉ khả thi khi \( n \leq 5 \) hoặc 6. Với \( n \geq 10 \), không thể liệt kê hết.
- **SAT solver** phải dùng thuật toán thông minh (resolution, DPLL, CDCL) thay vì duyệt brute-force.
- **FPGA / LUT** (Look-Up Table) chỉ có thể hiện thực trực tiếp các hàm Boolean nhỏ (\( n \leq 6 \)). Các hàm lớn phải được phân rã.

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


