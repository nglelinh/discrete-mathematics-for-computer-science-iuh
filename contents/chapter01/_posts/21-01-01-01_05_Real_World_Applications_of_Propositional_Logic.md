---
layout: post
title: "Logic Mệnh đề và Thế giới Thực: Từ Aristotle đến Trí tuệ Nhân tạo"
categories: chapter01
date: 2021-01-01
order: 5
required: false
lang: en
---

Có bao giờ bạn tự hỏi: tại sao một lý thuyết toán học ra đời từ hơn 2300 năm trước — khi chưa có máy tính, chưa có điện, chưa có Internet — lại trở thành nền tảng của mọi hệ thống máy tính hiện đại? Câu trả lời nằm ở một sự thật đơn giản nhưng sâu sắc: **logic mệnh đề không chỉ là công cụ của toán học — nó là ngôn ngữ của tư duy chính xác**, và máy tính, xét cho cùng, chỉ là cỗ máy thực thi tư duy chính xác đó với tốc độ khủng khiếp.

Hành trình của logic mệnh đề trải dài từ những cuộc tranh luận triết học ở Athens cổ đại, qua cuộc cách mạng công nghiệp với đại số Boole, đến kỷ nguyên số với hàng tỷ transistor trong chip xử lý, và xa hơn nữa — đến những hệ thống trí tuệ nhân tạo có khả năng suy luận, chứng minh định lý và thậm chí viết code. Trong bài học đặc biệt này, chúng ta sẽ không học công thức hay làm bài tập. Chúng ta sẽ **du hành xuyên thời gian** để thấy logic mệnh đề đã định hình thế giới như thế nào — và vẫn đang tiếp tục định hình tương lai ra sao.

---

## Phần 1: Lịch sử — Hành trình 2300 năm của Logic

### 1.1. Aristotle và ngọn lửa đầu tiên (384–322 TCN)

Mọi câu chuyện về logic đều bắt đầu từ Aristotle. Sống ở Athens thế kỷ thứ 4 trước Công nguyên, Aristotle là học trò của Plato và là thầy của Alexander Đại đế. Nhưng di sản lớn nhất của ông không nằm ở những mối quan hệ quyền lực đó — mà ở một bộ sách được gọi chung là *Organon* (Công cụ).

Trong *Organon*, Aristotle đã hệ thống hóa lần đầu tiên trong lịch sử nhân loại các quy luật của suy luận hợp lệ. Ông phát hiện ra rằng một số hình thức lập luận luôn cho kết quả đúng, bất kể nội dung cụ thể là gì. Ví dụ kinh điển nhất là **tam đoạn luận** (syllogism):

> *Mọi người đều phải chết.*  
> *Socrates là người.*  
> *Vậy Socrates phải chết.*

Điều kỳ diệu ở đây là: bạn không cần biết Socrates là ai, "người" là gì, hay "chết" nghĩa là gì. Chỉ cần cấu trúc lập luận đúng, kết luận buộc phải đúng. Đây chính là tiền thân của khái niệm **hằng đúng** (tautology) mà chúng ta đã học.

![Aristotle - cha đẻ của logic học phương Tây]
*Hình 1: Tượng Aristotle tại Đại học Aristotle, Thessaloniki, Hy Lạp. Ông là người đầu tiên hệ thống hóa các quy luật suy luận.*

#### Minh họa trực quan: Tam đoạn luận của Aristotle

**Cấu trúc tam đoạn luận** (syllogism) có thể được biểu diễn như một **cây suy luận**:

```
              Socrates phải chết
                     ↑
         (Mọi người đều phải chết)
                     ↑
              Socrates là người
```

**Bốn kiểu mệnh đề** Aristotle phân loại:

| Kiểu | Dạng | Ví dụ | Ký hiệu |
|:---|:---|:---|:---|
| A | Mọi A là B | Mọi người đều phải chết | ∀x (A(x) → B(x)) |
| E | Không A nào là B | Không ai là bất tử | ∀x (A(x) → ¬B(x)) |
| I | Một số A là B | Một số người là triết gia | ∃x (A(x) ∧ B(x)) |
| O | Một số A không là B | Một số người không phải triết gia | ∃x (A(x) ∧ ¬B(x)) |

**Lưu ý**: Kiểu A và E là **phổ quát** (universal), kiểu I và O là **riêng lẻ** (particular). Đây chính là nguồn gốc của các lượng từ ∀ và ∃ mà chúng ta sẽ học ở chương 2.

### 1.2. Leibniz và giấc mơ về "ngôn ngữ phổ quát" (1646–1716)

Phải đến thế kỷ 17, một thiên tài khác mới đưa logic lên một tầm cao mới: **Gottfried Wilhelm Leibniz** — nhà toán học, triết học, luật sư, nhà ngoại giao, và là người đồng phát minh ra vi tích phân (cùng với Newton).

Leibniz có một giấc mơ vĩ đại: tạo ra một **"calculus ratiocinator"** — một "phép tính suy luận" — hoạt động giống như đại số. Ý tưởng của ông là: nếu mọi khái niệm đều có thể được biểu diễn bằng ký hiệu, và mọi suy luận đều có thể được thực hiện bằng các phép toán trên ký hiệu đó, thì **mọi tranh cãi triết học đều có thể được giải quyết bằng cách… tính toán**.

> *"Nếu có tranh cãi, hai triết gia sẽ không cần tranh luận nữa, cũng như hai kế toán viên không cần tranh luận. Thay vào đó, họ sẽ lấy bút ra, ngồi xuống, và nói với nhau: Hãy tính toán xem."*  
> — Gottfried Wilhelm Leibniz

Nghe quen không? Đó chính xác là những gì máy tính làm ngày nay! Leibniz đã hình dung ra máy tính 300 năm trước khi chiếc máy tính đầu tiên ra đời. Ông thậm chí còn thiết kế một cỗ máy tính cơ học có thể thực hiện bốn phép tính số học — một trong những tiền thân của máy tính hiện đại.

#### Minh họa trực quan: Giấc mơ của Leibniz

Leibniz hình dung một **"máy tính suy luận"** hoạt động như sau:

```
Tranh cãi triết học
        ↓
Chuyển thành ký hiệu logic
        ↓
Áp dụng phép tính (như đại số)
        ↓
Kết quả: Đúng / Sai (không cần tranh cãi!)
```

**So sánh với máy tính hiện đại**:

| Leibniz (1646–1716) | Máy tính ngày nay |
|:---|:---|
| `calculus ratiocinator` | CPU + ALU |
| Ký hiệu logic | Bit (0/1) |
| Phép tính suy luận | AND, OR, NOT gates |
| Giải tranh cãi triết học | Kiểm chứng phần mềm, SAT solver |

Leibniz đã **hình dung trước máy tính 300 năm**! Ông thậm chí còn thiết kế một cỗ máy tính cơ học thực hiện 4 phép tính số học — tiền thân của máy tính hiện đại.

### 1.3. George Boole và cuộc cách mạng đại số (1815–1864)

Năm 1847, một thầy giáo tự học người Anh tên là **George Boole** xuất bản một cuốn sách mỏng với tựa đề khiêm tốn: *"The Mathematical Analysis of Logic"*. Bảy năm sau, ông hoàn thiện ý tưởng của mình trong tác phẩm để đời: *"An Investigation of the Laws of Thought"* (1854).

#### Minh họa trực quan: Đại số Boole

Boole đã **gán số cho logic**:

| Logic | Số học (Boole) |
|:---|:---|
| Đúng (True) | 1 |
| Sai (False) | 0 |

**Bảng phép toán**:

| AND (∧) | OR (∨) | NOT (¬) |
|:---:|:---:|:---:|
| 1 ∧ 1 = 1 | 1 ∨ 1 = 1 | ¬1 = 0 |
| 1 ∧ 0 = 0 | 1 ∨ 0 = 1 | ¬0 = 1 |
| 0 ∧ 1 = 0 | 0 ∨ 1 = 1 | |
| 0 ∧ 0 = 0 | 0 ∨ 0 = 0 | |

**Nhận xét**: 
- AND giống như **phép nhân** thông thường
- OR giống như **phép cộng** nhưng 1+1=1 (không tràn)
- NOT giống như **phép trừ 1 − x**

Đây chính là nền tảng của **mạch logic** trong mọi con chip ngày nay!

![George Boole - nhà toán học Anh thế kỷ 19]
*Hình 2: Chân dung George Boole. Đại số của ông là nền tảng toán học cho toàn bộ khoa học máy tính hiện đại.*

Với hệ thống của Boole, lần đầu tiên trong lịch sử, các lập luận logic có thể được **tính toán** thay vì chỉ được **tranh luận**. Một mệnh đề phức tạp có thể được rút gọn, đơn giản hóa, và kiểm tra tính đúng đắn bằng các phép biến đổi đại số — giống hệt như giải phương trình.

Điều trớ trêu là: trong suốt cuộc đời mình, công trình của Boole bị xem là một sự tò mò toán học ít có ứng dụng thực tế. Phải đến gần 100 năm sau, khi Claude Shannon — một sinh viên MIT 22 tuổi — đọc được công trình của Boole, mọi thứ mới thực sự thay đổi.

### 1.4. Claude Shannon — Người kết nối Logic với Điện (1937)

Năm 1937, **Claude Shannon** — khi đó đang là nghiên cứu sinh tại MIT — xuất bản luận văn thạc sĩ của mình với tựa đề: *"A Symbolic Analysis of Relay and Switching Circuits"*. Luận văn này sau đó được gọi là **"luận văn thạc sĩ quan trọng nhất mọi thời đại"**.

Ý tưởng của Shannon đơn giản đến mức thiên tài: **các mạch điện với công tắc đóng/mở có thể được mô tả bằng đại số Boole**. Một công tắc đóng tương ứng với 1 (dòng điện chạy qua), công tắc mở tương ứng với 0. Hai công tắc nối tiếp là phép AND, hai công tắc song song là phép OR.

![Claude Shannon và sơ đồ mạch chuyển mạch]
*Hình 3: Claude Shannon (trái) và sơ đồ mạch điện tương đương với biểu thức Boolean (phải).*

Phát hiện này có ý nghĩa gì? Nó có nghĩa là **bất kỳ biểu thức logic nào cũng có thể được "xây dựng" bằng mạch điện thực tế**. Và ngược lại, bất kỳ mạch điện nào cũng có thể được phân tích và tối ưu bằng các quy luật đại số Boole.

Từ thời điểm đó, logic không còn là môn học của riêng các triết gia và nhà toán học nữa. Nó trở thành công cụ thiết kế cho các kỹ sư điện — những người đang xây dựng nền móng của kỷ nguyên máy tính.

Shannon sau này còn sáng lập ra **lý thuyết thông tin** (Information Theory) — một lý thuyết định lượng hóa khái niệm "thông tin" và đặt nền móng cho truyền thông số, nén dữ liệu, và mật mã học hiện đại. Nhưng đó là câu chuyện cho một bài học khác.

---

## Phần 2: Logic trong Thiết kế Mạch Số — Trái tim của mọi máy tính

### 2.1. Từ transistor đến cổng logic

Mỗi con chip xử lý hiện đại chứa **hàng tỷ transistor** — những công tắc điện tử siêu nhỏ chỉ có hai trạng thái: dẫn điện (ON, tương ứng với 1) hoặc không dẫn điện (OFF, tương ứng với 0). Các transistor này được tổ chức thành các **cổng logic** — những mạch điện nhỏ thực hiện các phép toán Boolean cơ bản.

![Cấu trúc transistor và cổng logic]
*Hình 4: Sơ đồ transistor (trái) và ký hiệu các cổng logic AND, OR, NOT (phải).*

Hãy thử hình dung: bộ vi xử lý Intel Core i9 có khoảng **10 tỷ transistor**. Nếu mỗi cổng logic trung bình dùng 3-4 transistor, thì con chip này chứa khoảng **2-3 tỷ cổng logic**. Tất cả những cổng đó — từ cổng AND đơn giản nhất đến những tổ hợp phức tạp nhất — đều vận hành theo cùng một đại số Boole mà chúng ta đang học.

### 2.2. Từ bảng chân trị đến vi mạch

Quy trình thiết kế một vi mạch hiện đại diễn ra như sau:

1. **Đặc tả logic**: Kỹ sư mô tả chức năng mong muốn bằng bảng chân trị hoặc biểu thức Boolean.
2. **Tối thiểu hóa**: Dùng các kỹ thuật như bản đồ Karnaugh (học ở chương 13) hoặc thuật toán Quine-McCluskey để rút gọn biểu thức.
3. **Tổng hợp logic**: Chuyển biểu thức đã rút gọn thành sơ đồ mạch với các cổng logic thực tế.
4. **Tối ưu vật lý**: Sắp xếp vị trí các cổng trên chip để giảm khoảng cách, giảm trễ, giảm nhiệt.
5. **Sản xuất**: "In" thiết kế lên tấm silicon bằng công nghệ quang khắc (photolithography).

Mỗi bước trong quy trình này tiêu tốn hàng triệu đô la và hàng tháng trời làm việc của các đội kỹ sư — và tất cả đều bắt đầu từ... bảng chân trị!

### 2.3. Tại sao tối thiểu hóa quan trọng?

Một con chip hiện đại như Apple M2 Ultra có giá thành sản xuất khoảng 100-150 USD cho mỗi con chip. Với hàng trăm triệu thiết bị được sản xuất, **tiết kiệm dù chỉ 1% diện tích chip cũng có nghĩa là tiết kiệm hàng tỷ đô la**. Đó là lý do các kỹ sư tại Intel, AMD, NVIDIA, Apple, Qualcomm đầu tư khổng lồ vào việc tối ưu mạch logic.

Và đoán xem? Công cụ toán học đứng sau tất cả những điều này chính là **logic mệnh đề** — thứ mà bạn đang học ngay bây giờ.

---

## Phần 3: Logic trong Lập trình — Mọi điều kiện if-else đều là logic

### 3.1. Cấu trúc điều khiển — "Bộ não" của chương trình

Mỗi chương trình máy tính, từ app Hello World đơn giản nhất đến hệ điều hành phức tạp nhất, đều được xây dựng từ ba cấu trúc cơ bản:

1. **Tuần tự** (sequence): thực hiện từng lệnh một
2. **Rẽ nhánh** (selection): `if-else`, `switch-case` — **đây chính là logic mệnh đề!**
3. **Lặp** (iteration): `for`, `while` — cũng dựa trên điều kiện logic

Khi bạn viết:

```python
if (score >= 5) and (attempts < 3):
    print("Pass")
else:
    print("Fail")
```

Bạn đang sử dụng trực tiếp logic mệnh đề: `(score >= 5)` và `(attempts < 3)` là hai mệnh đề đơn, được nối với nhau bằng phép AND. Máy tính đánh giá từng mệnh đề thành True hoặc False, rồi áp dụng bảng chân trị của phép AND để quyết định rẽ nhánh nào.

### 3.2. Short-circuit evaluation — Tối ưu thông minh dựa trên logic

Hầu hết các ngôn ngữ lập trình hiện đại sử dụng **short-circuit evaluation** (đánh giá ngắn mạch): khi đã biết kết quả cuối cùng, các biểu thức con còn lại sẽ không được tính. Đây là một ứng dụng trực tiếp của các luật logic:

- Với `A and B`: nếu A sai thì kết quả luôn sai, không cần tính B → **luật nuốt**: `False ∧ B ≡ False`
- Với `A or B`: nếu A đúng thì kết quả luôn đúng, không cần tính B → **luật nuốt**: `True ∨ B ≡ True`

Điều này không chỉ tiết kiệm thời gian tính toán mà còn được các lập trình viên tận dụng một cách có chủ đích:

```python
# Kiểm tra an toàn: nếu user là None, không gọi .is_admin()
if user is not None and user.is_admin():
    grant_access()
```

### 3.3. De Morgan trong refactoring

Định luật De Morgan — $$\neg(p \land q) \equiv \neg p \lor \neg q$$ — là một trong những công cụ refactoring mạnh nhất. Nó cho phép bạn biến đổi điều kiện phức tạp thành dạng dễ đọc hơn:

```python
# Khó đọc
if not (is_admin and is_active):
    deny_access()

# Dễ đọc hơn nhờ De Morgan
if not is_admin or not is_active:
    deny_access()
```

Các IDE hiện đại như IntelliJ IDEA hay Visual Studio Code thậm chí còn tự động đề xuất áp dụng De Morgan để cải thiện chất lượng code!

---

## Phần 4: Logic trong Cơ sở Dữ liệu — SQL và hơn thế nữa

### 4.1. Mệnh đề WHERE — Logic lọc dữ liệu

Mỗi câu lệnh SQL với mệnh đề `WHERE` chính là một biểu thức logic. Khi bạn viết:

```sql
SELECT * FROM students
WHERE (gpa >= 3.0) AND (major = 'CS' OR major = 'Math');
```

Database engine sẽ:
1. Đánh giá `gpa >= 3.0` cho từng hàng → True/False
2. Đánh giá `major = 'CS'` và `major = 'Math'` cho từng hàng → True/False
3. Áp dụng OR giữa hai kết quả trên
4. Áp dụng AND giữa kết quả bước 1 và bước 3
5. Chỉ giữ lại những hàng có kết quả cuối cùng là True

Đây chính xác là **đánh giá biểu thức logic trên tập dữ liệu lớn** — điều mà chúng ta làm thủ công với bảng chân trị 2-3 biến, nhưng database làm tự động với hàng triệu bản ghi.

### 4.2. Query optimization — Đại số quan hệ

Database engine không thực thi truy vấn theo đúng thứ tự bạn viết. Nó sử dụng **đại số quan hệ** — một mở rộng của logic mệnh đề — để biến đổi truy vấn của bạn thành dạng tối ưu nhất:

- Đẩy điều kiện lọc xuống sớm (predicate pushdown)
- Sắp xếp lại thứ tự JOIN
- Loại bỏ điều kiện thừa

Tất cả những biến đổi này đều dựa trên các luật tương đương logic mà chúng ta đã học!

---

## Phần 5: Logic trong Trí tuệ Nhân tạo — Khi máy học "suy nghĩ"

### 5.1. Symbolic AI và Hệ chuyên gia

Trước khi có deep learning và mạng neural, AI hoạt động dựa trên **logic hình thức**. Các hệ chuyên gia (expert systems) như MYCIN (chẩn đoán y khoa, 1976) hay XCON (cấu hình máy tính, 1980) lưu trữ tri thức dưới dạng các luật logic:

```
IF (sốt cao) AND (ho kéo dài) AND (đau ngực)
THEN (nghi ngờ viêm phổi)
```

Hệ thống sau đó sử dụng **suy diễn tiến** (forward chaining) hoặc **suy diễn lùi** (backward chaining) để rút ra kết luận từ các luật và dữ kiện — đúng như cách chúng ta chứng minh trong logic mệnh đề.

### 5.2. SAT Solvers — "Vũ khí bí mật" của khoa học máy tính

**SAT** (Boolean Satisfiability) là bài toán: cho một biểu thức logic, hỏi có tồn tại cách gán giá trị True/False cho các biến để biểu thức đó đúng không? Nghe đơn giản, nhưng SAT là một trong những bài toán quan trọng nhất trong khoa học máy tính:

- **Kiểm chứng phần mềm**: liệu có đầu vào nào làm chương trình crash không?
- **Lập lịch**: sắp xếp ca làm việc cho nhân viên thỏa mọi ràng buộc
- **Giải Sudoku**: mỗi ô Sudoku là một biến Boolean
- **Thiết kế vi mạch**: kiểm tra mạch có hoạt động đúng không
- **AI planning**: lập kế hoạch hành động cho robot

Các SAT solver hiện đại như MiniSAT, Glucose, CaDiCaL có thể xử lý biểu thức với **hàng triệu biến** trong vài giây. Sức mạnh này đến từ các thuật toán thông minh kết hợp với... logic mệnh đề!

![Minh họa SAT solver hoạt động]
*Hình 5: Quá trình tìm kiếm của SAT solver qua không gian các phép gán giá trị. Mỗi nút là một biến, mỗi nhánh là True hoặc False.*

### 5.3. Logic trong Học máy

Ngay cả trong kỷ nguyên deep learning, logic vẫn đóng vai trò quan trọng:

- **Cây quyết định** (Decision Trees): mỗi nút trong cây là một điều kiện logic (if-then)
- **Neuro-symbolic AI**: kết hợp mạng neural với suy luận logic để đạt cả khả năng học từ dữ liệu lẫn khả năng suy luận chính xác
- **Explainable AI**: dùng logic để giải thích tại sao mô hình đưa ra quyết định

---

## Phần 6: Logic trong Bảo mật và Kiểm chứng

### 6.1. Kiểm chứng hình thức (Formal Verification)

Làm sao để chắc chắn một phần mềm — đặc biệt là phần mềm điều khiển máy bay, thiết bị y tế, hay hệ thống tài chính — không có lỗi? Câu trả lời là **kiểm chứng hình thức**: dùng toán học, cụ thể là logic, để chứng minh rằng chương trình thỏa mãn đặc tả.

Các công cụ như **TLA+**, **Coq**, **Isabelle** cho phép kỹ sư viết đặc tả bằng logic và chứng minh rằng code thỏa mãn đặc tả đó. Amazon dùng TLA+ để kiểm chứng các thuật toán phân tán trong AWS. Microsoft dùng Z3 (một SMT solver — "SAT on steroids") để kiểm tra driver thiết bị. Intel dùng formal verification để đảm bảo chip không có lỗi thiết kế trước khi sản xuất hàng triệu đơn vị.

### 6.2. Logic điều kiện trong An ninh mạng

Mỗi firewall rule, mỗi access control policy, mỗi authentication flow đều có thể được biểu diễn dưới dạng biểu thức logic:

```
ALLOW ACCESS IF
    (user.authenticated = TRUE)
    AND (user.role IN {'admin', 'moderator'})
    AND (request.ip IN trusted_networks)
    AND (request.time BETWEEN 08:00 AND 22:00)
```

Sai một điều kiện — và bạn có thể vô tình mở cửa cho kẻ tấn công. Đây là lý do các công ty bảo mật sử dụng formal methods để kiểm tra chính sách bảo mật.

---

## Kết luận: Từ Chân lý Đơn giản đến Thế giới Phức tạp

Hành trình của logic mệnh đề là một trong những câu chuyện vĩ đại nhất của tri thức nhân loại. Từ những suy tư của Aristotle về tam đoạn luận, qua giấc mơ "máy tính suy luận" của Leibniz, qua cuộc cách mạng đại số của Boole, qua phát hiện thiên tài của Shannon kết nối logic với điện tử — và giờ đây, logic mệnh đề vận hành trong từng transistor của chiếc điện thoại bạn đang cầm, trong từng câu truy vấn database, trong từng dòng code bạn viết, và trong những hệ thống AI thông minh nhất hành tinh.

Khi bạn học về bảng chân trị, về phép AND, OR, NOT, về De Morgan và các dạng chuẩn tắc — bạn không chỉ học một môn toán trừu tượng. Bạn đang học **ngôn ngữ nền tảng của kỷ nguyên số** — ngôn ngữ mà mọi máy tính, mọi hệ thống, mọi thuật toán trên thế giới đều phải "nói" để hoạt động.

Và ai biết được? Có thể chính bạn, với những kiến thức nền tảng này, sẽ là người viết nên chương tiếp theo của câu chuyện — một thuật toán mới, một kiến trúc chip mới, hay một hệ thống AI có khả năng suy luận như con người.

Logic mệnh đề bắt đầu từ một câu hỏi đơn giản: **"Điều này đúng hay sai?"** Nhưng chính câu hỏi đơn giản ấy đã — và đang — thay đổi thế giới.

---

## Hình ảnh tham khảo

Để có trải nghiệm học tập phong phú hơn, bạn có thể tìm kiếm các hình ảnh sau trên Internet:

1. **Chân dung Aristotle** — tượng hoặc tranh vẽ cổ điển
2. **Chân dung George Boole** — ảnh chụp hoặc tranh vẽ
3. **Claude Shannon** bên cạnh mạch điện hoặc sơ đồ
4. **Sơ đồ cổng logic AND/OR/NOT** với ký hiệu điện tử
5. **Die shot của CPU hiện đại** — ảnh chụp cận cảnh bề mặt chip
6. **Minh họa SAT solver** — cây tìm kiếm với các nút True/False
7. **Sơ đồ kiểm chứng hình thức** — pipeline từ đặc tả đến chứng minh

## Bài tập thực hành

### Bài tập 1: Mô hình hóa điều kiện bảo mật

Viết mệnh đề cho quy tắc: "Truy cập được cấp nếu (admin OR (manager VÀ active)) VÀ NOT banned". Sau đó rút gọn nếu có thể.

<details>
<summary>Đáp án</summary>

$$(A \lor (M \land C)) \land \lnot B$$

Không rút gọn thêm được mà không thay đổi nghĩa.

</details>

### Bài tập 2: Ứng dụng trong SQL

Viết điều kiện WHERE tương đương với NOT (status = 'inactive' AND role != 'guest') theo hai cách.

<details>
<summary>Đáp án</summary>

```sql
WHERE NOT (status = 'inactive' AND role != 'guest')
-- hoặc De Morgan
WHERE status <> 'inactive' OR role = 'guest'
```

</details>

### Bài tập 3: Thiết kế mạch đơn giản

Mô tả một mạch 3 input với output TRUE khi ít nhất hai input TRUE (majority). Viết công thức DNF.

<details>
<summary>Đáp án</summary>

DNF: $$(A \land B \land \lnot C) \lor (A \land \lnot B \land C) \lor (\lnot A \land B \land C) \lor (A \land B \land C)$$

Rút gọn thành $$(A \land B) \lor (A \land C) \lor (B \land C)$$.

</details>


