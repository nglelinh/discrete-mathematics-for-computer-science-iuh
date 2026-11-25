---

layout: post
title: "Giới thiệu Logic Mệnh đề"
categories: chapter01
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Xây dựng nền tảng logic mệnh đề — hệ thống hình thức cho phép biểu diễn, phân tích và suy luận về các phát biểu có giá trị đúng hoặc sai."
---


Một hợp đồng phần mềm ghi rằng *"Khách hàng VIP hoặc có hóa đơn trên 1 triệu và thanh toán trước hạn sẽ được hoàn tiền"*—chỉ một câu tiếng Việt tưởng chừng bình thường ấy lại có thể bị hai lập trình viên hiểu theo hai cách hoàn toàn khác nhau, dẫn đến thất thoát hàng tỷ đồng khi triển khai. **Logic mệnh đề (Propositional Logic)** ra đời chính để dập tắt sự mơ hồ đó: nó rút gọn mọi phát biểu khẳng định về đúng hai giá trị chân trị rạch ròi **Đúng (`True`)** hoặc **Sai (`False`)**, tạo nên nền móng chung cho toán học chặt chẽ, mạch điện tử silicon và mọi câu lệnh điều kiện trong lập trình.

<div class="textbook-epigraph" markdown="1">

"Logic is the beginning of wisdom, not the end of it."

<span class="epigraph-attribution">— Leonard Nimoy (as Spock)</span>

</div>

Trong chương này, chúng ta xây dựng nền tảng **logic mệnh đề** — hệ thống hình thức cho phép biểu diễn, phân tích và suy luận về các phát biểu có giá trị đúng hoặc sai. Trong thực tế lập trình, mọi điều kiện `if` hay mệnh đề `WHERE` trong truy vấn SQL đều chỉ trả về đúng hoặc sai, và logic mệnh đề nghiên cứu chính loại phát biểu đó. Mục 1.1 bắt đầu từ khái niệm cốt lõi nhất: **mệnh đề** (proposition).

Mỗi lần lập trình viên viết `if (score >= 5)` hay thêm điều kiện `WHERE status = "active"`, máy tính buộc phải trả lời một câu hỏi cơ bản: phát biểu này đúng hay sai? Kiểu quyết định nhị phân — đúng hoặc sai, `1` hoặc `0`, `true` hoặc `false` — là nền tảng của toàn bộ quá trình tính toán.

Khi hệ thống phức tạp hơn, trực giác của con người dễ dẫn đến sai sót: một điều kiện tưởng như hợp lý vẫn có thể cho kết quả ngược ở một trường hợp biên; yêu cầu nghiệp vụ viết bằng ngôn ngữ tự nhiên có thể bị hiểu theo nhiều cách; một đoạn mã chạy không báo lỗi chưa chắc đã đúng với mọi đầu vào. Logic mệnh đề chuyển các câu khẳng định mơ hồ thành đối tượng có thể **kiểm tra, phân tích và tính toán** một cách chính xác. Nắm vững khái niệm này giúp chúng ta viết điều kiện rõ ràng hơn, thiết kế bộ kiểm thử (test case) bao phủ đủ trường hợp, đọc hiểu yêu cầu nghiệp vụ chính xác hơn, và hiểu cách máy tính đánh giá logic ở tầng thấp nhất.

Mục này tập trung trả lời hai câu hỏi căn bản: **mệnh đề là gì**, và **vì sao không phải mọi câu đều là mệnh đề**.

Mọi dòng lệnh `if (x > 0 && !is_locked)` trong chương trình, mọi cổng logic bằng silicon bên trong CPU, và mọi câu truy vấn `WHERE` trong cơ sở dữ liệu đều bắt nguồn từ một ngôn ngữ tối giản nhưng cực kỳ sắc bén: **Logic Mệnh đề (Propositional Logic)**. Thay vì để ngôn ngữ tự nhiên gây mơ hồ ("sinh viên giỏi Toán hoặc Tin học"), logic mệnh đề chắt lọc mọi phát biểu thành đúng hai giá trị chân trị rạch ròi: **Đúng (`True` / `1`)** hoặc **Sai (`False` / `0`)**.

## Bản đồ kiến thức nền: Logic Mệnh đề đứng trên những trụ cột nào?

1. **Nguyên lý nhị trị (Law of Excluded Middle & Non-Contradiction)**:
   Một mệnh đề hợp lệ phải có giá trị chân trị xác định duy nhất—hoặc Đúng, hoặc Sai, không bao giờ vừa Đúng vừa Sai. Các câu hỏi, câu cảm thán, mệnh lệnh hay câu chứa biến tự do chưa gắn giá trị (như "$x + 2 = 5$") đều **không phải** mệnh đề.

2. **Cú pháp (Syntax) vs. Ngữ nghĩa (Semantics)**:
   **Cú pháp** quy định cách ghép biến mệnh đề ($p, q, r$) với các phép toán logic thành công thức hợp lệ (*well-formed formula*). **Ngữ nghĩa** gán giá trị chân trị `T`/`F` cho từng biến để định giá toàn bộ công thức.

3. **Cầu nối từ Logic đến Khoa học Máy tính**:
   Mỗi biến mệnh đề tương ứng với 1 bit (`0`/`1`), mỗi công thức tương ứng với một mạch tổ hợp (combinational circuit) hoặc biểu thức điều kiện Boolean—nền tảng trực tiếp cho thiết kế vi mạch, kiểm chứng phần mềm và truy vấn cơ sở dữ liệu.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">


**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận biết** câu nào là mệnh đề và câu nào không phải mệnh đề.
- **Gán** ký hiệu logic cho các mệnh đề trong bài toán thực tế.
- **Phân biệt** mệnh đề sơ cấp và mệnh đề phức hợp.
- **Giải thích** vai trò của logic mệnh đề trong lập trình, cơ sở dữ liệu, bảo mật và trí tuệ nhân tạo.
- **Chuyển đổi** một yêu cầu nghiệp vụ đơn giản thành điều kiện logic để sử dụng trong mã nguồn.


**Từ khóa**: Mệnh đề (proposition), giá trị chân lý (truth value), mệnh đề sơ cấp (atomic proposition), mệnh đề phức hợp (compound proposition), logic trong lập trình.
</div>


## Mệnh đề là gì?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Mệnh đề (proposition) là một câu khẳng định có thể xác định được tính đúng hoặc sai, nhưng không thể đồng thời vừa đúng vừa sai.
</div>


![Aristotle - cha đẻ của logic](/discrete-mathematics-for-computer-science-iuh/img/course/Aristotle_Altemps_Inv8575.jpg)

<p class="textbook-figure-caption" data-figure="1.1">Tượng bán thân Aristotle tại Palazzo Altemps, Roma — người đầu tiên hệ thống hóa các quy luật suy luận.</p>
![George Boole — cha đẻ logic Boolean](/discrete-mathematics-for-computer-science-iuh/img/course/George_Boole.jpg)

<p class="textbook-figure-caption" data-figure="1.2">George Boole (1815–1864), nhà toán học người Anh, người đặt nền móng cho logic Boolean dùng trong máy tính hiện đại.</p>
![Bảng tứ đối — nền tảng suy luận cổ điển](/discrete-mathematics-for-computer-science-iuh/img/course/Square_of_opposition__set_diagrams.svg)

<p class="textbook-figure-caption" data-figure="1.3">Bảng tứ đối (square of opposition) — mô hình quan hệ giữa các mệnh đề trong logic cổ điển, tiền thân của logic hình thức.</p>
<div class="textbook-example" markdown="1">
**Ví dụ** (về mệnh đề):
- "2 + 3 = 5" (đúng).
- "Hà Nội là thủ đô của Việt Nam" (đúng).
- "5 > 10" (sai).
- "Tất cả số nguyên tố đều là số lẻ" (sai, vì 2 là số nguyên tố chẵn).
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (không phải mệnh đề):
- "x + 1 = 5" (giá trị đúng/sai phụ thuộc vào x).
- "Hôm nay trời đẹp quá!" (mang tính cảm thán, chủ quan).
- "Mấy giờ rồi?" (câu hỏi).
- "Hãy đóng cửa!" (câu mệnh lệnh).
</div>


## Logic học nghiên cứu cái gì?

**Logic học** (logic) là ngành khoa học nghiên cứu các quy tắc suy luận hợp lệ — tức là cách rút ra kết luận đúng từ những tiền đề đúng.

### Đối tượng nghiên cứu của logic học

Logic học không xét đến **nội dung** cụ thể của các phát biểu, mà chỉ tập trung vào **hình thức** (cấu trúc) và mối quan hệ chân lý giữa chúng:

| Khía cạnh | Logic học quan tâm | Logic học không quan tâm |
|:---|:---|:---|
| Hình thức | Cấu trúc "Nếu P thì Q" | Nội dung cụ thể của P và Q |
| Giá trị chân lý | Mối quan hệ đúng/sai | Ý nghĩa thực tế của câu |
| Suy luận | Quy tắc đi từ tiền đề đến kết luận | Chủ đề của cuộc tranh luận |

<div class="textbook-example" markdown="1">
**Ví dụ**: Cả hai câu sau đều có cùng hình thức logic:
- "Nếu trời mưa thì đường ướt."
- "Nếu n chẵn thì n² chẵn."

Logic học chỉ xét cấu trúc `Nếu P thì Q`, không quan tâm P là "trời mưa" hay "n chẵn".
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (thực tế): Tranh cãi trên mạng xã hội

Xét cuộc trao đổi sau:

> **Người A**: "Nếu bạn yêu nước thì phải ủng hộ chính sách X."
> **Người B**: "Tôi không ủng hộ chính sách X, nhưng tôi vẫn yêu nước!"

Hai phát biểu trên cùng gắn với cấu trúc logic **Nếu P thì Q**. Đặt ký hiệu: $$p$$ là "yêu nước", $$q$$ là "ủng hộ chính sách X". Người A khẳng định $$p \to q$$; người B bác bỏ khẳng định này bằng cách chỉ ra trường hợp $$\neg q \land p$$ (không ủng hộ X nhưng vẫn yêu nước). Câu "Nếu yêu nước thì phải ủng hộ X" là một **mệnh đề kéo theo** (implication), và việc chỉ ra $$p$$ đúng trong khi $$q$$ sai chính là cách phủ định mệnh đề kéo theo (sẽ trình bày ở mục sau). Cuộc tranh cãi thực chất xoay quanh **nội dung** của $$p$$ và $$q$$, không phải **hình thức** suy luận. Logic học giúp tách biệt hai khía cạnh này để phân tích lập luận rõ ràng hơn.
</div>


<div class="textbook-example" markdown="1">
**Ví dụ** (thực tế): Luật an toàn giao thông

Theo quy định, khi chở trẻ em dưới 10 tuổi và chiều cao dưới 1,35 m trên xe ô tô gia đình hoặc xe cá nhân, người lái **phải lắp ghế trẻ em**. Đặt ký hiệu:
- $$p$$: Trẻ em dưới 10 tuổi.
- $$q$$: Trẻ em có chiều cao dưới 1,35 m.
- $$r$$: Xe ô tô gia đình hoặc xe cá nhân.
- $$s$$: Lắp ghế trẻ em.

**Điều kiện bắt buộc**:

<div class="textbook-equation" markdown="1">
$$(p \land q \land r) \to s$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nghĩa là: **Nếu** (trẻ dưới 10 tuổi **VÀ** cao dưới 1,35 m **VÀ** đi xe gia đình/cá nhân) **thì phải** lắp ghế trẻ em.

**Ứng dụng trong mã nguồn** (hệ thống kiểm tra đăng ký xe):

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

Các quy định pháp luật thường được diễn đạt dưới dạng **mệnh đề kéo theo**. Hiểu rõ cấu trúc logic giúp lập trình viên viết điều kiện kiểm tra chính xác, tránh nhầm lẫn giữa `and` và `or` khi chuyển quy định thành mã nguồn, đồng thời thiết kế bộ kiểm thử bao phủ các trường hợp biên (tuổi = 10, chiều cao = 1,35 m, xe công vụ, v.v.).
</div>


## Định lý bất toàn (Gödel)

Năm 1931, nhà toán học **Kurt Gödel** chứng minh hai định lý quan trọng, chỉ ra **giới hạn cơ bản của mọi hệ thống logic hình thức**.

<div class="textbook-theorem" id="định-lý-bất-toàn-thứ-nhất" markdown="1">
**Định lý bất toàn thứ nhất**:

> **Trong mọi hệ thống logic đủ mạnh để biểu diễn số học, luôn tồn tại những mệnh đề đúng nhưng không thể chứng minh được trong hệ thống đó.**
</div>

Nói cách khác, không có hệ thống logic nhất quán nào có thể chứng minh được **tất cả** các mệnh đề đúng: luôn tồn tại những mệnh đề đúng nhưng nằm ngoài khả năng chứng minh từ các tiên đề của hệ thống.

<div class="textbook-theorem" id="định-lý-bất-toàn-thứ-hai" markdown="1">
**Định lý bất toàn thứ hai**:

> **Một hệ thống logic nhất quán không thể chứng minh được tính nhất quán của chính nó.**
</div>

Nếu một hệ thống đủ mạnh có thể tự chứng minh rằng nó không mâu thuẫn, thì bản thân hệ thống đó lại mâu thuẫn. Nói cách khác, một hệ thống không thể tự bảo đảm tính nhất quán của chính mình từ bên trong.

### Ý nghĩa thực tiễn

| Ý nghĩa | Hệ quả trong khoa học máy tính |
|:---|:---|
| Không thể tự động hóa mọi chứng minh | Không có thuật toán nào kiểm tra được tính đúng/sai của mọi chương trình |
| Luôn có giới hạn trong một hệ thống hình thức | Cần kết hợp kiểm tra thủ công hoặc nhiều công cụ phân tích khác nhau |
| Liên hệ với bài toán dừng (Halting Problem) | Không thể viết một chương trình tổng quát dự đoán mọi chương trình khác có dừng hay không |

**Liên hệ với lập trình**: Định lý bất toàn giải thích vì sao không thể xây dựng một trình biên dịch tự động phát hiện mọi lỗi logic trong mọi chương trình — luôn tồn tại những trường hợp không thể quyết định được.

### Khung giải thích (nên đọc chậm): Phân loại 6 phát biểu thực tế bằng tiêu chuẩn mệnh đề

Để tránh nhầm lẫn phổ biến nhất khi mới học Logic, hãy tự kiểm tra bằng tay 6 phát biểu sau theo đúng 2 tiêu chí: *(1) có phải câu trần thuật không?* và *(2) có chân trị Đúng/Sai xác định độc lập với biến chưa biết không?*

| STT | Phát biểu | Là mệnh đề? | Giải thích cầm tay chỉ việc |
| :---: | :--- | :---: | :--- |
| 1 | `"17 là số nguyên tố."` | **Có (`True`)** | Câu trần thuật có chân trị xác định (17 chỉ chia hết cho 1 và 17). |
| 2 | `"2 + 2 = 5."` | **Có (`False`)** | Mệnh đề **sai** vẫn là mệnh đề! Đừng nhầm "mệnh đề" với "câu đúng". |
| 3 | `"Hãy đóng cửa lại!"` | **Không** | Câu mệnh lệnh, không có nghĩa Đúng/Sai. |
| 4 | `"x + 3 = 7."` | **Không** | Chứa biến tự do $x$: đúng khi $x = 4$, sai khi $x = 0$ (đây là *vị từ*, học ở Chương 2). |
| 5 | `"Trên sao Hỏa từng có nước lỏng."` | **Có** | Chân trị tồn tại khách quan dù con người đã biết hay chưa. |
| 6 | `"Câu này là sai."` | **Không** | Nghịch lý kẻ nói dối: nếu Đúng thì hóa Sai, nếu Sai thì hóa Đúng (vi phạm nguyên lý nhị trị). |

## Ký hiệu mệnh đề

Chúng ta thường dùng các chữ cái thường như $$p, q, r, s, \ldots$$ để ký hiệu các mệnh đề.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- $$p$$: "Hôm nay là thứ Hai."
- $$q$$: "Trời đang mưa."
- $$r$$: "2 + 2 = 4."
</div>


## Giá trị chân lý

Mỗi mệnh đề có một **giá trị chân lý** (truth value):
- **1** (True/Đúng), thường ký hiệu là T: mệnh đề đúng.
- **0** (False/Sai), thường ký hiệu là F: mệnh đề sai.

Một mệnh đề chỉ có thể nhận giá trị 1 hoặc 0, không thể đồng thời vừa đúng vừa sai.

## Phân loại mệnh đề

**Mệnh đề sơ cấp** (elementary/atomic proposition) là mệnh đề không thể xây dựng từ các mệnh đề khác thông qua các liên từ logic hoặc trạng từ "không".

**Ví dụ về mệnh đề sơ cấp**:
- "2 là số nguyên tố."
- $$p$$: "Hà Nội là thủ đô của Việt Nam."
- $$q$$: "5 > 10."

**Mệnh đề phức hợp** (compound proposition) là mệnh đề được xây dựng từ các mệnh đề sơ cấp bằng cách dùng các liên từ như "và", "hoặc", "nếu... thì...", "khi và chỉ khi" hoặc trạng từ "không".

**Ví dụ về mệnh đề phức hợp**:
- "2 là số nguyên tố **và** 3 là số lẻ" (kết hợp hai mệnh đề bằng "và").
- "**Nếu** trời mưa **thì** đường ướt."

## Ứng dụng trong Khoa học Máy tính

### Trong Lập trình

Mọi điều kiện trong câu lệnh `if`, `while` hay biểu thức Boolean đều là mệnh đề:

```python
age = 18
is_student = True
has_valid_id = True

if age >= 18 and is_student and has_valid_id:
    print("Được nhận ưu đãi sinh viên")
```

Trong ví dụ này:

- `age >= 18` là một mệnh đề có giá trị đúng hoặc sai tại thời điểm thực thi.
- `is_student` là một mệnh đề Boolean.
- `has_valid_id` là một mệnh đề Boolean.
- Toàn bộ điều kiện là một mệnh đề phức hợp.

Nắm vững logic mệnh đề giúp chúng ta đọc hiểu các điều kiện phức tạp, phát hiện sớm lỗi dùng sai `and`/`or`, và viết test case hiệu quả hơn.

### Trong Cơ sở dữ liệu

Mệnh đề lọc trong truy vấn SQL cũng vận hành theo logic mệnh đề:

```sql
SELECT * FROM students
WHERE gpa >= 3.2 AND credits >= 60 AND status = 'active';
```

Mỗi dòng dữ liệu được đánh giá bằng một mệnh đề. Nếu mệnh đề đúng, dòng đó xuất hiện trong kết quả; nếu sai, dòng đó bị loại.

### Trong Bảo mật

Các hệ thống phân quyền dùng biểu thức logic để quyết định quyền hạn của người dùng:

```python
can_delete = is_admin or (is_owner and not is_locked)
```

Điều kiện này có nghĩa là: người dùng được phép xóa nếu họ là admin, hoặc nếu họ là chủ sở hữu và tài nguyên chưa bị khóa. Chỉ một dấu ngoặc đặt sai vị trí cũng có thể tạo ra lỗ hổng bảo mật.

### Trong Trí tuệ Nhân tạo

Hệ chuyên gia, kiểm chứng chương trình, bộ giải SAT (SAT solver) và nhiều kỹ thuật trí tuệ nhân tạo cổ điển đều dựa trên logic mệnh đề.

## Ví dụ thực tế: Từ yêu cầu đến điều kiện logic

<div class="content-box example-box textbook-block" markdown="1">
**Yêu cầu nghiệp vụ**: Sinh viên được đăng ký môn học nếu thỏa mãn đồng thời các điều kiện sau:

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
Trong mã nguồn:

```python
can_register = paid_tuition and account_active and (passed_prerequisite or advisor_approved)
```
</div>

## Định lý quan trọng: Số lượng hàm Boolean

<div class="textbook-theorem" markdown="1">
**Định lý**: Trên một tập hợp gồm $$n$$ biến mệnh đề, có **đúng $$2^{2^n}$$** hàm Boolean khác nhau.
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh**:

1. Mỗi phép gán giá trị (assignment) cho $$n$$ biến có thể được xem như một vector trong $$\{T,F\}^n$$. Có đúng $$2^n$$ vector như vậy.

2. Một hàm Boolean $$f$$ được xác định hoàn toàn bởi giá trị của nó trên từng vector. Nghĩa là ta cần gán cho mỗi vector một giá trị $$T$$ hoặc $$F$$.

3. Với mỗi vector có 2 lựa chọn. Do đó, tổng số cách gán giá trị là:
   $$
   2 \times 2 \times \cdots \times 2 \quad (2^n \text{ lần}) = 2^{2^n}.
   $$
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả quan trọng**:
- Với $$n = 1$$: có $$2^{2} = 4$$ hàm Boolean (hằng đúng, hằng sai, hàm đồng nhất, NOT).
- Với $$n = 2$$: có $$2^{4} = 16$$ hàm Boolean (bao gồm AND, OR, XOR, kéo theo, v.v.).
- Với $$n = 3$$: có $$2^{8} = 256$$ hàm Boolean.
- Với $$n = 10$$: con số lên tới $$2^{1024} \approx 10^{308}$$, lớn hơn số nguyên tử trong vũ trụ quan sát được.
</div>

**Ý nghĩa trong Khoa học Máy tính**:
- **Bảng chân trị** chỉ thực tế khi $$n \leq 5$$ hoặc $$6$$; với $$n \geq 10$$, không thể liệt kê hết mọi hàng.
- **SAT solver** phải dùng các thuật toán chuyên biệt (resolution, DPLL, CDCL) thay vì duyệt vét cạn (brute-force).
- **Kiểm thử phần mềm** cần các chiến lược có chọn lọc (pairwise testing, symbolic execution) thay vì kiểm tra mọi tổ hợp đầu vào.

## Bài tập thực hành

### Bài tập 1: Xác định mệnh đề
Xác định câu nào sau đây là mệnh đề và cho biết giá trị chân lý của nó:

1. "Python là ngôn ngữ lập trình."
2. "x² = 4."
3. "Hãy học bài!"
4. "Nếu n là số chẵn thì n chia hết cho 2."
5. "Bạn có thích toán không?"

<details>
<summary>Đáp án</summary>

1. **Mệnh đề** — Giá trị: T (đúng).
2. **Không phải mệnh đề** — Phụ thuộc vào giá trị của x.
3. **Không phải mệnh đề** — Câu mệnh lệnh.
4. **Mệnh đề** — Giá trị: T (đúng).
5. **Không phải mệnh đề** — Câu hỏi.

</details>

### Bài tập 2: Ký hiệu hóa
Cho các mệnh đề sau, hãy ký hiệu bằng các chữ cái:

- "Hôm nay là Chủ nhật."
- "Tôi có bài kiểm tra."
- "Thư viện mở cửa."
- "Tôi sẽ đi học."

Sau đó viết mệnh đề phức hợp: "Nếu hôm nay là Chủ nhật và tôi có bài kiểm tra, thì tôi sẽ đi học nếu thư viện mở cửa."

### Bài tập 3: Logic trong hệ thống thực tế

Một website cho phép người dùng tải file nếu người đó đã đăng nhập, email đã xác thực, và (dung lượng file nhỏ hơn 10 MB hoặc người đó là tài khoản Premium).

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

(a) **Mệnh đề** — Giá trị: F (sai, vì $$1 + 1 = 2$$, không phải 3).
(b) **Không phải mệnh đề** — Câu mệnh lệnh, không có giá trị chân lý.
(c) **Mệnh đề** — Giá trị phụ thuộc vào ngày hiện tại (nếu hôm nay là thứ Hai thì T, ngược lại F).
(d) **Không phải mệnh đề** — Câu chứa biến $$x$$ chưa được gán giá trị, nên chưa xác định được đúng/sai (đây là vị từ, không phải mệnh đề).
(e) **Mệnh đề** — Giá trị: T (theo định nghĩa tam giác đều).
(f) **Mệnh đề** — Giá trị: F (2026 không chia hết cho 4 nên không phải năm nhuận).
(g) **Không phải mệnh đề** — Nghịch lý tự tham chiếu (nếu giả sử đúng thì suy ra sai, và ngược lại).
(h) **Mệnh đề** — Giá trị: T (định lý Euclid đã được chứng minh).

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
    Mệnh đề phức hợp: $$(p \land q) \to r$$.

(b) $$p$$: "Số chia hết cho 2", $$q$$: "Số chia hết cho 3", $$r$$: "Số chia hết cho 6".
    Mệnh đề phức hợp: $$(p \land q) \leftrightarrow r$$.

(c) $$p$$: "Bạn làm bài tập", $$q$$: "Bạn sẽ qua môn".
    Mệnh đề phức hợp: $$p \lor \neg q$$ (hoặc dạng tương đương $$\neg p \to \neg q$$).

(d) $$p$$: "Người dùng là admin", $$q$$: "Tài khoản đã bị khóa".
    Mệnh đề phức hợp: $$\neg p \land q$$.

</details>

### Bài tập 6: Chuyển đổi câu tự nhiên thành logic

Viết các câu sau dưới dạng ký hiệu logic với các biến mệnh đề phù hợp:

(a) "Bạn được phép vào câu lạc bộ nếu bạn trên 18 tuổi và có thẻ thành viên."
(b) "Hệ thống gửi cảnh báo khi nhiệt độ vượt quá 100°C hoặc áp suất dưới mức an toàn."
(c) "Sinh viên được nhận học bổng nếu (điểm trung bình >= 8.0 và hạnh kiểm Tốt) hoặc (có thành tích nghiên cứu đặc biệt)."
(d) "Không thể vừa đăng nhập thành công vừa đăng nhập thất bại tại cùng một thời điểm."
(e) "Nếu hôm nay là cuối tuần và không có deadline thì tôi sẽ đi chơi, nếu không tôi sẽ học bài."

<details>
<summary>Đáp án</summary>

(a) Đặt $$p$$: "Bạn trên 18 tuổi", $$q$$: "Bạn có thẻ thành viên", $$r$$: "Bạn được phép vào câu lạc bộ".
    Công thức: $$(p \land q) \to r$$.

(b) Đặt $$t$$: "Nhiệt độ > 100°C", $$p$$: "Áp suất < mức an toàn", $$w$$: "Hệ thống gửi cảnh báo".
    Công thức: $$(t \lor p) \to w$$.

(c) Đặt $$g$$: "Điểm TB >= 8.0", $$h$$: "Hạnh kiểm Tốt", $$r$$: "Có thành tích nghiên cứu", $$s$$: "Được nhận học bổng".
    Công thức: $$((g \land h) \lor r) \to s$$.

(d) Đặt $$p$$: "Đăng nhập thành công", $$q$$: "Đăng nhập thất bại".
    Công thức: $$\neg(p \land q)$$ — hai sự kiện không thể đồng thời xảy ra.

(e) Đặt $$w$$: "Hôm nay là cuối tuần", $$d$$: "Có deadline", $$g$$: "Tôi đi chơi", $$s$$: "Tôi học bài".
    Công thức: $$((w \land \neg d) \to g) \land (\neg(w \land \neg d) \to s)$$.

</details>

### Bài tập 7: Mệnh đề trong kiểm thử phần mềm

Một hàm kiểm tra đầu vào có điều kiện sau:

```python
def validate_input(x, y, z):
    if (x > 0 and y < 100) or (z == "active" and x > 0):
        return "Hợp lệ"
    else:
        return "Không hợp lệ"
```

(a) Đặt ký hiệu cho từng mệnh đề sơ cấp trong điều kiện.
(b) Viết mệnh đề phức hợp hoàn chỉnh.
(c) Liệt kê tất cả các tổ hợp đầu vào cần kiểm thử để bao phủ 100% điều kiện (có thể dùng bảng liệt kê).

<details>
<summary>Đáp án</summary>

(a)
- $$p$$: "$$x > 0$$"
- $$q$$: "$$y < 100$$"
- $$r$$: "$$z = \text{"active"}$$"

(b) Mệnh đề phức hợp: $$(p \land q) \lor (r \land p)$$.
    Rút gọn bằng tính phân phối: $$p \land (q \lor r)$$.

(c) Các tổ hợp kiểm thử để bao phủ toàn bộ 8 trường hợp:

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

Từ bảng trên, điều kiện chỉ đúng khi $$p$$ đúng ($$x > 0$$) và có ít nhất một trong hai mệnh đề $$q$$ hoặc $$r$$ đúng. Tập kiểm thử tối thiểu cho hai nhánh kết quả gồm một trường hợp có $$p = T, (q \lor r) = T$$ và một trường hợp có $$p = F$$ (hoặc $$q = r = F$$).

</details>

### Bài tập 8: Dịch ngược — từ mã nguồn sang logic

Đoạn mã sau kiểm tra quyền truy cập vào một tài liệu:

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
(b) Viết biểu thức logic cho từng hành động (`allow_access`, `show_preview`, `redirect_to_login`).
(c) Với người dùng đã xác thực nhưng không phải admin, tài liệu ở trạng thái public nhưng đã archived, hành động nào sẽ xảy ra?

<details>
<summary>Đáp án</summary>

(a)
- $$a$$: `user.is_authenticated`
- $$i$$: `user.is_admin`
- $$p$$: `doc.is_public`
- $$r$$: `doc.is_archived`

(b)
- **allow_access**: $$a \land (i \lor (p \land \neg r))$$.
- **show_preview**: $$a \land \neg(i \lor (p \land \neg r))$$ (đã xác thực nhưng không đủ quyền).
- **redirect_to_login**: $$\neg a$$ (chưa xác thực).

(c) Với $$a = T$$ (đã xác thực), $$i = F$$ (không phải admin), $$p = T$$ (public), $$r = T$$ (đã archived):
    $$i \lor (p \land \neg r) = F \lor (T \land F) = F$$.
    Do đó **show_preview** được thực thi: người dùng chỉ thấy bản xem trước và không được truy cập đầy đủ.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Mệnh đề** là câu khẳng định có giá trị chân lý xác định (đúng hoặc sai); câu hỏi, câu mệnh lệnh, câu chứa biến tự do và phát biểu cảm thán chủ quan không phải mệnh đề.
- Logic học nghiên cứu **hình thức** và **giá trị chân lý** của phát biểu, không phụ thuộc vào nội dung cụ thể.
- Mệnh đề được ký hiệu bằng các chữ cái ($$p, q, r, \ldots$$) và chia thành **mệnh đề sơ cấp** (nguyên tử) và **mệnh đề phức hợp** (ghép từ các mệnh đề khác).
- Logic mệnh đề là nền tảng của câu lệnh điều kiện trong lập trình, truy vấn cơ sở dữ liệu, phân quyền, kiểm thử và trí tuệ nhân tạo.
- Trên $$n$$ biến mệnh đề có đúng $$2^{2^n}$$ hàm Boolean, giải thích vì sao bảng chân trị chỉ khả thi khi $$n$$ nhỏ.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các **phép toán logic** dùng để ghép mệnh đề sơ cấp thành biểu thức phức hợp.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=yF9rupvF77U">[Toán rời rạc] MỆNH ĐỀ LOGIC</a> — Đinh Thái Sơn, tiếng Việt. Giới thiệu khái niệm mệnh đề là câu có giá trị chân lý trước khi đi vào ký hiệu hình thức.
- <a href="https://www.youtube.com/watch?v=itrXYg41-V0">INTRODUCTION to PROPOSITIONAL LOGIC - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Trình bày định nghĩa mệnh đề và các loại câu không phải mệnh đề, tương ứng phần mở đầu của bài.
- <a href="https://www.youtube.com/watch?v=q2eyZZK-OIk">Intro to Logical Statements</a> — Dr. Trefor Bazett, tiếng Anh. Minh họa các ví dụ mệnh đề đúng/sai, tạo bước đệm cho các phép toán ở mục sau.
