---

layout: post
title: "Giới thiệu Logic Mệnh đề"
categories: chapter01
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Trong chương này chúng ta xây dựng nền tảng logic mệnh đề — hệ thống hình thức cho phép biểu diễn, phân tích và suy luận về các phát biểu có giá trị đúng hoặc…"
---

<div class="textbook-epigraph" markdown="1">

"Logic is the beginning of wisdom, not the end of it."

<span class="epigraph-attribution">— Leonard Nimoy (as Spock)</span>

</div>

Trong chương này chúng ta xây dựng nền tảng **logic mệnh đề** — hệ thống hình thức cho phép biểu diễn, phân tích và suy luận về các phát biểu có giá trị đúng hoặc sai. Trong khoa học máy tính, mọi quyết định nhị phân từ điều kiện `if` trong chương trình, truy vấn `WHERE` trong cơ sở dữ liệu, đến quy tắc phân quyền và kiểm thử tự động, đều dựa trên cùng một nguyên lý: mỗi phát biểu phải được đánh giá là đúng hoặc sai tại một thời điểm cho trước. Mục 1.1 bắt đầu từ khái niệm cốt lõi nhất: **mệnh đề** (proposition).

Mỗi lần lập trình viên viết `if (score >= 5)` hay thêm điều kiện `WHERE status = "active"`, máy tính buộc phải trả lời câu hỏi cổ điển: mệnh đề này đúng hay sai? Kiểu quyết định nhị phân — đúng hoặc sai, 1 hoặc 0, `true` hoặc `false` — là viên gạch đầu tiên của toàn bộ nền tảng tính toán.

Khi hệ thống phức tạp hơn, trực giác của con người dễ dẫn đến sai lầm: một điều kiện nhìn hợp lý vẫn có thể cho kết quả ngược ở đúng một trường hợp biên; yêu cầu nghiệp vụ bằng ngôn ngữ tự nhiên có thể được hiểu theo nhiều cách; đoạn mã "chạy được" chưa chắc đúng với mọi đầu vào. Logic mệnh đề chuyển các câu khẳng định mơ hồ thành đối tượng có thể **kiểm tra, phân tích và tính toán** một cách chính xác. Nắm vững khái niệm này giúp chúng ta viết điều kiện ít mơ hồ hơn, thiết kế test case bao phủ đủ trường hợp, đọc hiểu yêu cầu nghiệp vụ chính xác hơn, và hiểu cách máy tính đánh giá logic ở tầng thấp nhất.

Mục này trả lời hai câu hỏi căn bản: **mệnh đề là gì**, và **vì sao không phải mọi câu đều là mệnh đề**.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** câu nào là mệnh đề và câu nào không phải mệnh đề.
- **Gán** ký hiệu logic cho các mệnh đề trong bài toán thực tế.
- **Phân biệt** mệnh đề sơ cấp và mệnh đề phức hợp.
- **Giải thích** vì sao logic mệnh đề quan trọng trong lập trình, cơ sở dữ liệu, AI và bảo mật.
- **Chuyển đổi** một yêu cầu nghiệp vụ đơn giản thành điều kiện logic để dùng trong code.


**Từ khóa**: Mệnh đề (proposition), giá trị chân lý (truth value), mệnh đề sơ cấp (atomic proposition), mệnh đề phức hợp (compound proposition), logic trong lập trình.
</div>


## Mệnh đề là gì?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Mệnh đề (proposition) là một câu khẳng định có thể xác định được tính đúng hoặc sai, nhưng không thể vừa đúng vừa sai.
</div>


![Aristotle - cha đẻ của logic](/discrete-mathematics-for-computer-science-iuh/img/course/Aristotle_Altemps_Inv8575.jpg)

<p class="textbook-figure-caption" data-figure="1.1">Tượng bán thân Aristotle tại Palazzo Altemps, Roma — người đầu tiên hệ thống hóa các quy luật suy luận</p>
![George Boole — cha đẻ logic Boolean](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="1.2">George Boole (1815–1864), nhà toán học người Anh, người đặt nền móng cho logic Boolean dùng trong máy tính hiện đại.</p>
![Bảng tứ đối — nền tảng suy luận cổ điển](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__set_diagrams.svg)

<p class="textbook-figure-caption" data-figure="1.3">Bảng tứ đối (square of opposition) — mô hình quan hệ giữa các mệnh đề trong logic cổ điển, tiền thân của logic hình thức.</p>
<div class="textbook-example" markdown="1">
**Ví dụ** (về mệnh đề):
- "2 + 3 = 5" (đúng)
- "Hà Nội là thủ đô của Việt Nam" (đúng)  
- "5 > 10" (sai)
- "Tất cả số nguyên tố đều là số lẻ" (sai, vì 2 là số nguyên tố chẵn)
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (KHÔNG phải mệnh đề):
- "x + 1 = 5" (phụ thuộc vào giá trị của x)
- "Hôm nay trời đẹp quá!" (mang tính chủ quan)
- "Mấy giờ rồi?" (câu hỏi)
- "Hãy đóng cửa!" (câu mệnh lệnh)
</div>


## Logic học nghiên cứu cái gì?

**Logic học** (logic) là ngành khoa học nghiên cứu các quy tắc suy luận hợp lý — làm thế nào để từ những tiền đề đúng rút ra kết luận đúng.

### Đối tượng nghiên cứu của logic học

Logic học không quan tâm đến **nội dung** cụ thể của các phát biểu, mà chỉ quan tâm đến **hình thức** (cấu trúc) của chúng:

| Khía cạnh | Logic học quan tâm | Logic học KHÔNG quan tâm |
|:---|:---|:---|
| Hình thức | Cấu trúc "Nếu P thì Q" | Nội dung cụ thể của P và Q |
| Giá trị chân lý | Mối quan hệ đúng/sai | Ý nghĩa thực tế của câu |
| Suy luận | Quy tắc từ tiền đề đến kết luận | Chủ đề của cuộc tranh luận |

<div class="textbook-example" markdown="1">
**Ví dụ**: Cả hai câu sau đều có cùng hình thức logic:
- "Nếu trời mưa thì đường ướt"
- "Nếu n chẵn thì n² chẵn"

Logic học chỉ quan tâm đến cấu trúc `Nếu P thì Q`, không quan tâm P là "trời mưa" hay "n chẵn".
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (thực tế): Tranh cãi trên mạng xã hội

Xét cuộc trao đổi sau:

> **Người A**: "Nếu bạn yêu nước thì phải ủng hộ chính sách X."
> **Người B**: "Tôi không ủng hộ chính sách X, nhưng tôi vẫn yêu nước!"

Hai phát biểu trên cùng mang cấu trúc logic **Nếu P thì Q**. Đặt ký hiệu: $$p$$ — yêu nước; $$q$$ — ủng hộ chính sách X. Người A ngụ ý $$p \to q$$; người B phản bác bằng trường hợp $$\neg q \land p$$ (không ủng hộ X nhưng vẫn yêu nước). Câu "Nếu yêu nước thì phải ủng hộ X" là một **mệnh đề kéo theo** (implication); người B phủ nhận nó bằng cách chỉ ra $$p$$ đúng trong khi $$q$$ sai — đúng theo định nghĩa kéo theo (sẽ trình bày ở mục sau). Cuộc tranh cãi thực chất xoay quanh **nội dung** của $$p$$ và $$q$$, không phải **hình thức** suy luận. Logic học giúp chúng ta tách biệt hai khía cạnh này để phân tích lập luận rõ ràng hơn.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (thực tế): Luật an toàn giao thông

Theo quy định, khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 m trên xe ô tô gia đình hoặc xe cá nhân, người lái **phải lắp ghế trẻ em**. Đặt ký hiệu:
- $$p$$: Trẻ em dưới 10 tuổi
- $$q$$: Trẻ em chiều cao dưới 1,35 m
- $$r$$: Xe ô tô gia đình hoặc xe cá nhân
- $$s$$: Lắp ghế trẻ em

**Điều kiện bắt buộc**:

<div class="textbook-equation" markdown="1">
$$(p \land q \land r) \to s$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
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

Luật giao thông thường được diễn đạt dưới dạng **mệnh đề kéo theo**. Hiểu logic giúp chúng ta viết điều kiện kiểm tra chính xác trong phần mềm, tránh nhầm lẫn giữa `and`/`or` khi chuyển luật thành mã nguồn, và thiết kế test case bao phủ các trường hợp biên (tuổi = 10, chiều cao = 1,35 m, loại xe công vụ, v.v.).
</div>


## Định lý bất toàn (Gödel)

Năm 1931, nhà toán học **Kurt Gödel** chứng minh hai định lý cách mạng, cho thấy **giới hạn cơ bản của mọi hệ thống logic hình thức**.

### Định lý bất toàn thứ nhất

> **Trong mọi hệ thống logic đủ mạnh để biểu diễn số học, luôn tồn tại những mệnh đề đúng nhưng không thể chứng minh được trong hệ thống đó.**

Nói cách khác: Không có hệ thống logic nào có thể chứng minh được **tất cả** các mệnh đề đúng. Luôn có "khe hở" — những sự thật toán học đúng nhưng không thể chứng minh từ các tiên đề của hệ thống.

### Định lý bất toàn thứ hai

> **Một hệ thống logic nhất quán không thể chứng minh được tính nhất quán của chính nó.**

Nếu một hệ thống có thể chứng minh rằng nó không mâu thuẫn, thì chính nó đã mâu thuẫn. Nói cách khác: một hệ thống không thể "tự chứng minh tính nhất quán của chính mình" từ bên trong.

### Ý nghĩa thực tiễn

| Ý nghĩa | Ứng dụng trong khoa học máy tính |
|:---|:---|
| Không thể tự động hóa mọi chứng minh | Không có thuật toán nào kiểm tra được mọi chương trình đúng/sai |
| Luôn có "lỗ hổng" trong hệ thống | Cần kiểm tra thủ công hoặc dùng nhiều hệ thống |
| Liên hệ với bài toán dừng (Halting Problem) | Không thể viết chương trình dự đoán mọi chương trình có dừng hay không |

**Liên hệ với lập trình**: Định lý bất toàn giải thích tại sao không thể viết một "siêu trình biên dịch" tự động phát hiện mọi lỗi logic trong code — luôn có những trường hợp không thể quyết định được.

## Ký hiệu mệnh đề

Chúng ta thường dùng các chữ cái như p, q, r, s,... để ký hiệu các mệnh đề.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- p: "Hôm nay là thứ hai"
- q: "Trời đang mưa"
- r: "2 + 2 = 4"
</div>


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

Nắm vững logic mệnh đề giúp chúng ta đọc được điều kiện phức tạp, phát hiện lỗi `and`/`or`, và viết test case hiệu quả hơn.

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

<div class="content-box example-box textbook-block" markdown="1">
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

<div class="textbook-equation" markdown="1">
$$p \land q \land (r \lor s)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong code:

```python
can_register = paid_tuition and account_active and (passed_prerequisite or advisor_approved)
```
</div>

## Định lý quan trọng: Số lượng hàm Boolean

<div class="textbook-theorem" markdown="1">
**Định lý**: Trên một tập hợp gồm \( n \) biến mệnh đề, có **đúng \( 2^{2^n} \)** hàm Boolean khác nhau.
</div>


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
- **Kiểm thử phần mềm** cần chiến lược thông minh (pairwise, symbolic execution) thay vì kiểm tra vét cạn mọi tổ hợp đầu vào.

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

### Bài tập 4: Phân biệt mệnh đề và không phải mệnh đề

Trong các câu sau, câu nào là mệnh đề? Nếu là mệnh đề, cho biết giá trị chân lý.

(a) $$1 + 1 = 3$$.
(b) Hãy đóng cửa lại!
(c) Hôm nay là thứ Hai.
(d) $$x + 5 = 10$$.
(e) Nếu tam giác có ba cạnh bằng nhau thì nó là tam giác đều.
(f) 2026 là năm nhuận.
(g) Câu này là sai.
(h) Có vô hạn số nguyên tố.

<details>
<summary>Đáp án</summary>

(a) **Mệnh đề** — Giá trị: F (sai, vì 1+1=2, không phải 3).
(b) **Không phải mệnh đề** — Câu mệnh lệnh, không có giá trị chân lý.
(c) **Mệnh đề** — Giá trị phụ thuộc vào ngày hiện tại. Nếu hôm nay là thứ Hai thì T, ngược lại F.
(d) **Không phải mệnh đề** — Câu chứa biến $$x$$, chưa xác định được đúng/sai (vị từ, không phải mệnh đề).
(e) **Mệnh đề** — Giá trị: T (theo định nghĩa tam giác đều).
(f) **Mệnh đề** — 2026 không chia hết cho 4, nên không phải năm nhuận → F.
(g) **Không phải mệnh đề** — Nghịch lý tự tham chiếu (nếu cho là đúng thì hóa ra sai và ngược lại).
(h) **Mệnh đề** — Giá trị: T (đây là định lý Euclid đã được chứng minh).

</details>

### Bài tập 5: Xác định mệnh đề sơ cấp

Phân tích các mệnh đề phức hợp sau thành các mệnh đề sơ cấp:

(a) "Nếu trời mưa và tôi có ô thì tôi sẽ đi làm."
(b) "Số chia hết cho 2 và cho 3 khi và chỉ khi số đó chia hết cho 6."
(c) "Hoặc bạn làm bài tập hoặc bạn sẽ không qua môn."
(d) "Người dùng không phải admin và tài khoản đã bị khóa."

<details>
<summary>Đáp án</summary>

(a) $$p$$: "Trời mưa", $$q$$: "Tôi có ô", $$r$$: "Tôi sẽ đi làm".
    Mệnh đề phức hợp: $$(p \land q) \to r$$

(b) $$p$$: "Số chia hết cho 2", $$q$$: "Số chia hết cho 3", $$r$$: "Số chia hết cho 6".
    Mệnh đề phức hợp: $$(p \land q) \leftrightarrow r$$

(c) $$p$$: "Bạn làm bài tập", $$q$$: "Bạn sẽ qua môn".
    Mệnh đề phức hợp: $$p \lor \neg q$$ (hoặc dạng tương đương $$\neg p \to \neg q$$)

(d) $$p$$: "Người dùng là admin", $$q$$: "Tài khoản đã bị khóa".
    Mệnh đề phức hợp: $$\neg p \land q$$

</details>

### Bài tập 6: Chuyển đổi câu tự nhiên thành logic

Viết các câu sau dưới dạng ký hiệu logic với các biến mệnh đề được đặt tên phù hợp:

(a) "Bạn được phép vào câu lạc bộ nếu bạn trên 18 tuổi và có thẻ thành viên."
(b) "Hệ thống gửi cảnh báo khi nhiệt độ vượt quá 100°C hoặc áp suất dưới mức an toàn."
(c) "Sinh viên được nhận học bổng nếu (điểm trung bình >= 8.0 và hạnh kiểm Tốt) hoặc (có thành tích nghiên cứu đặc biệt)."
(d) "Không thể vừa đăng nhập thành công vừa đăng nhập thất bại tại cùng một thời điểm."
(e) "Nếu hôm nay là cuối tuần và không có deadline thì tôi sẽ đi chơi, nếu không tôi sẽ học bài."

<details>
<summary>Đáp án</summary>

(a) Đặt $$p$$: "Bạn trên 18 tuổi", $$q$$: "Bạn có thẻ thành viên", $$r$$: "Bạn được phép vào câu lạc bộ".
    Công thức: $$(p \land q) \to r$$

(b) Đặt $$t$$: "Nhiệt độ > 100°C", $$p$$: "Áp suất < mức an toàn", $$w$$: "Hệ thống gửi cảnh báo".
    Công thức: $$(t \lor p) \to w$$

(c) Đặt $$g$$: "Điểm TB >= 8.0", $$h$$: "Hạnh kiểm Tốt", $$r$$: "Có thành tích nghiên cứu", $$s$$: "Được nhận học bổng".
    Công thức: $$((g \land h) \lor r) \to s$$

(d) Đặt $$p$$: "Đăng nhập thành công", $$q$$: "Đăng nhập thất bại".
    Công thức: $$\neg(p \land q)$$ — không thể cả hai cùng xảy ra (luật phi mâu thuẫn).

(e) Đặt $$w$$: "Hôm nay là cuối tuần", $$d$$: "Có deadline", $$g$$: "Tôi đi chơi", $$s$$: "Tôi học bài".
    Công thức: $$((w \land \neg d) \to g) \land (\neg(w \land \neg d) \to s)$$

</details>

### Bài tập 7: Mệnh đề trong kiểm thử phần mềm

Một hàm kiểm tra đầu vào có điều kiện:

```python
def validate_input(x, y, z):
    if (x > 0 and y < 100) or (z == "active" and x > 0):
        return "Hợp lệ"
    else:
        return "Không hợp lệ"
```

(a) Đặt ký hiệu cho từng mệnh đề sơ cấp trong điều kiện.
(b) Viết mệnh đề phức hợp hoàn chỉnh.
(c) Liệt kê tất cả các tổ hợp đầu vào cần kiểm thử để đảm bảo bao phủ 100% điều kiện (có thể dùng bảng liệt kê).

<details>
<summary>Đáp án</summary>

(a)
- $$p$$: "$$x > 0$$"
- $$q$$: "$$y < 100$$"
- $$r$$: "$$z = \text{"active"}$$"

(b) Mệnh đề phức hợp: $$(p \land q) \lor (r \land p)$$
    Rút gọn: $$p \land (q \lor r)$$ (tính phân phối)

(c) Các tổ hợp kiểm thử cần thiết (để bao phủ mọi nhánh):

| $$p$$ (x>0) | $$q$$ (y<100) | $$r$$ (z=active) | $$p \land (q \lor r)$$ | Kết quả |
|:---:|:---:|:---:|:---:|:---|
| F | F | F | F | Không hợp lệ |
| F | F | T | F | Không hợp lệ |
| F | T | F | F | Không hợp lệ |
| F | T | T | F | Không hợp lệ |
| T | F | F | F | Không hợp lệ |
| T | F | T | T | Hợp lệ |
| T | T | F | T | Hợp lệ |
| T | T | T | T | Hợp lệ |

Từ bảng, ta thấy điều kiện chỉ cần $$p$$ (x>0) và ít nhất một trong $$q$$ hoặc $$r$$. Các test case tối thiểu: một case với $$p=T, (q \lor r)=T$$ và một case với $$p=F$$.

</details>

### Bài tập 8: Dịch ngược — từ code sang logic

Đoạn code sau kiểm tra quyền truy cập vào một tài liệu:

```python
if user.is_authenticated:
    if user.is_admin or (doc.is_public and not doc.is_archived):
        allow_access()
    else:
        show_preview()
else:
    redirect_to_login()
```

(a) Đặt ký hiệu cho các mệnh đề sơ cấp.
(b) Viết biểu thức logic cho từng hành động (allow_access, show_preview, redirect_to_login).
(c) Với người dùng đã xác thực nhưng không phải admin, tài liệu public nhưng đã archived — hành động nào xảy ra?

<details>
<summary>Đáp án</summary>

(a)
- $$a$$: "user.is_authenticated"
- $$i$$: "user.is_admin"
- $$p$$: "doc.is_public"
- $$r$$: "doc.is_archived"

(b)
- **allow_access**: $$a \land (i \lor (p \land \neg r))$$
- **show_preview**: $$a \land \neg(i \lor (p \land \neg r))$$ (đã xác thực nhưng không đủ quyền)
- **redirect_to_login**: $$\neg a$$ (chưa xác thực)

(c) Với $$a = T$$ (đã xác thực), $$i = F$$ (không admin), $$p = T$$ (public), $$r = T$$ (đã archived):
    $$i \lor (p \land \neg r) = F \lor (T \land F) = F$$
    Vậy **show_preview** được thực thi: người dùng chỉ thấy bản xem trước, không được truy cập đầy đủ.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Mệnh đề** là câu khẳng định có giá trị chân lý xác định (đúng hoặc sai); câu hỏi, mệnh lệnh, câu chứa biến tự do, và phát biểu chủ quan không phải mệnh đề.
- Logic học nghiên cứu **hình thức** và **giá trị chân lý** của phát biểu, không quan tâm nội dung cụ thể.
- Mệnh đề được ký hiệu bằng chữ cái ($$p, q, r, \ldots$$) và phân thành **mệnh đề sơ cấp** (nguyên tử) và **mệnh đề phức hợp** (ghép từ các mệnh đề khác).
- Logic mệnh đề là nền tảng của lập trình điều kiện, truy vấn cơ sở dữ liệu, phân quyền, kiểm thử và trí tuệ nhân tạo.
- Trên $$n$$ biến mệnh đề có đúng $$2^{2^n}$$ hàm Boolean — lý do bảng chân trị chỉ khả thi khi $$n$$ nhỏ.

Trong bài tiếp theo, chúng ta giới thiệu các **phép toán logic** dùng để ghép mệnh đề sơ cấp thành biểu thức phức hợp.
