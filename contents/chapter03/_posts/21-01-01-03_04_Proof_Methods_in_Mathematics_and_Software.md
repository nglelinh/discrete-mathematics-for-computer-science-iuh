---
layout: post
title: "Các Phương pháp Chứng minh trong Toán học và Phần mềm"
categories: chapter03
date: 2021-01-01
order: 4
required: false
lang: en
---

Trong khoa học máy tính,
không phải mọi câu hỏi quan trọng đều là “chạy được chưa”.
Có những lúc ta cần câu hỏi khó hơn:
“nó luôn đúng không”,
“nó sai trong trường hợp nào”,
“ta biết chắc bằng cách nào”.

Đó là nơi các phương pháp chứng minh bước vào.
Từ *Elements* của Euclid,
đến loop invariants,
Hoare logic,
chứng minh giao thức mật mã,
và tranh luận muôn thuở giữa testing với formal proof,
bài học này kể câu chuyện của một kỹ năng cổ điển
nhưng vẫn sống ở lõi của engineering hiện đại.

---

## Phần 1: Euclid và tiêu chuẩn vàng của lập luận

### 1.1. Vì sao *Elements* sống hơn 2000 năm

Khoảng năm 300 TCN,
Euclid viết *Elements*.
Đây không chỉ là sách hình học.
Nó là một cỗ máy tổ chức tri thức.

Euclid bắt đầu bằng định nghĩa,
tiên đề,
khái niệm chung,
rồi từ đó xây từng định lý bằng chuỗi lập luận chặt chẽ.

Điểm đặc biệt không nằm ở từng kết quả riêng lẻ.
Điểm đặc biệt nằm ở mô hình tư duy:

- nêu giả thiết rõ ràng,
- xác định điều cần chứng minh,
- đi từng bước hợp lệ,
- kết thúc bằng kết luận tất yếu.

Chính mô hình này trở thành “gold standard” của chứng minh trong hơn hai thiên niên kỷ.

![Euclid và Elements]
*Hình 1: *Elements* của Euclid là một trong những mô hình thành công nhất của tri thức suy diễn có cấu trúc.*

### 1.2. Tại sao khoa học máy tính phải học tinh thần Euclid

Máy tính hiện đại không đọc hình học Hy Lạp.
Nhưng phần mềm đúng đắn vẫn cần thứ mà Euclid dạy:

- phát biểu chính xác,
- suy luận từng bước,
- không dựa vào trực giác mơ hồ,
- không nhầm ví dụ với chân lý phổ quát.

Trong ngôn ngữ software,
đó là nền của specification,
verification,
type soundness,
algorithm correctness,
và security proofs.

---

## Phần 2: Từ chứng minh toán học đến program correctness

### 2.1. Chạy đúng vài test chưa đủ

Giả sử bạn viết hàm sắp xếp.
Bạn test với 10 bộ dữ liệu,
100 bộ dữ liệu,
thậm chí 10.000 bộ dữ liệu.
Hàm đều chạy ổn.

Liệu điều đó có chứng minh hàm đúng với mọi input không?

Không.

Testing cho ta niềm tin mạnh hơn,
nhưng không phải chứng minh tổng quát.
Muốn đi xa hơn,
ta cần reasoning về toàn bộ hành vi có thể xảy ra.

### 2.2. Loop invariant: linh hồn của chứng minh vòng lặp

Một trong những ý tưởng đẹp nhất của correctness proofs là **loop invariant**.

Invariant là mệnh đề luôn đúng:

- trước khi vào vòng lặp,
- sau mỗi lần lặp,
- và giúp ta suy ra điều đúng khi vòng lặp kết thúc.

Ví dụ,
xét thuật toán tìm phần tử lớn nhất:

```python
max_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
```

Invariant tự nhiên là:

“Sau khi xử lý đến chỉ số `i`,
`max_val` là giá trị lớn nhất trong đoạn `arr[0..i]`.”

Nếu invariant đúng lúc bắt đầu,
được bảo toàn sau mỗi vòng,
và đủ mạnh tại thời điểm kết thúc,
ta có chứng minh đúng đắn cho thuật toán.

### 2.3. Hoare logic: biến chứng minh thành cú pháp

Hoare logic đưa ra ký hiệu nổi tiếng:

$$
\{P\}\ C\ \{Q\}
$$

Đọc là:

“Nếu điều kiện trước `P` đúng,
và ta chạy chương trình `C`,
thì khi kết thúc,
điều kiện sau `Q` sẽ đúng.”

Ý tưởng này cực mạnh,
vì nó biến chương trình thành đối tượng có thể phân tích toán học.

Ví dụ nhỏ:

$$
\{x = 5\}\ x := x + 1\ \{x = 6\}
$$

Nghe đơn giản,
nhưng từ đây người ta xây dựng logic cho assignment,
conditionals,
loops,
và procedure calls.

### 2.4. Nơi correctness proofs được dùng thật

Program correctness không chỉ nằm trong giáo trình.
Nó xuất hiện trong:

- compiler verification,
- verified kernels,
- smart contract auditing,
- cryptographic libraries,
- avionics software,
- safety-critical controllers.

Các dự án như CompCert,
seL4,
và nhiều verified components khác
cho thấy formal proof không còn là giấc mơ xa vời.

![Loop invariant và Hoare triple]
*Hình 2: Từ loop invariant đến Hoare logic, chứng minh chương trình nối lập trình với suy luận toán học.*

---

## Phần 3: Chứng minh trong mật mã học

### 3.1. Mật mã không thể dựa vào cảm giác

Bạn không muốn một giao thức bảo mật được đánh giá bằng câu:
“có vẻ khó hack”.

Trong cryptography,
người ta cần lập luận chặt chẽ hơn nhiều.
Ví dụ:

- giao thức này có chống nghe lén không,
- chữ ký số này có chống giả mạo không,
- scheme mã hóa này có an toàn dưới chosen-plaintext attack không.

### 3.2. Security proof thường là gì

Một security proof hay đi theo dạng reduction.

Ta chứng minh rằng:
nếu có attacker phá được hệ A,
thì ta có thể dùng attacker đó để phá một bài toán nền B
được tin là rất khó.

Ví dụ:

- phá RSA liên quan tới phân tích thừa số lớn,
- phá Diffie–Hellman liên quan tới discrete logarithm,
- phá hash construction liên quan tới collision resistance.

Chứng minh kiểu này không làm hệ thống “bất khả chiến bại”.
Nhưng nó cho ta khung lý luận rõ ràng:
hệ mạnh đến đâu,
phụ thuộc giả định nào,
và attacker được cấp quyền gì.

### 3.3. Protocol proofs và mô hình đối thủ

Trong security,
chi tiết mô hình rất quan trọng.

Bạn phải nói rõ:

- attacker có thấy toàn bộ traffic không,
- attacker có sửa message được không,
- attacker có truy cập oracle nào không,
- khóa có lộ một phần không.

Nếu không nói rõ mô hình,
“proof” dễ thành thứ đẹp trên giấy nhưng vô dụng ngoài đời.

Đó là bài học lớn mà sinh viên CS nên ghi nhớ:
chứng minh mạnh chỉ có ý nghĩa khi giả định được phát biểu trung thực.

---

## Phần 4: Những chứng minh nổi tiếng của toán học

### 4.1. Chứng minh $\sqrt{2}$ là vô tỉ

Một trong những ví dụ kinh điển cho proof by contradiction là chứng minh $\sqrt{2}$ vô tỉ.

Ý tưởng:
giả sử $\sqrt{2} = a/b$ với $a,b$ tối giản.
Suy ra $a^2 = 2b^2$,
nên $a$ chẵn.
Viết $a = 2k$,
thế vào thì suy ra $b$ cũng chẵn.
Mâu thuẫn với giả thiết tối giản.

Điểm đáng nhớ không chỉ là kết quả.
Điểm đáng nhớ là cách contradiction cho phép ta loại bỏ những khả năng tưởng hợp lý.

### 4.2. Chứng minh có vô hạn số nguyên tố

Euclid lại xuất hiện.

Giả sử chỉ có hữu hạn số nguyên tố:
$p_1, p_2, ..., p_n$.
Xét số:

$$
N = p_1p_2\cdots p_n + 1
$$

Khi chia $N$ cho bất kỳ $p_i$ nào,
đều dư 1.
Vậy hoặc $N$ là nguyên tố mới,
hoặc nó có ước nguyên tố mới.
Mâu thuẫn.

Đây là mẫu mực của một proof ngắn,
đẹp,
sạch,
và giàu sức gợi.

### 4.3. Vì sao các proof cổ điển vẫn quan trọng với dân CS

Chúng dạy ta nhiều điều:

- cách chọn chiến lược chứng minh,
- cách biến trực giác thành lập luận,
- cách dùng contradiction đúng chỗ,
- cách xây đối tượng phản ví dụ,
- cách phân biệt “đúng trong ví dụ” với “đúng với mọi trường hợp”.

Đó đều là kỹ năng hữu ích khi thiết kế thuật toán,
đọc paper,
hoặc debug giả định sai trong phần mềm.

![Chứng minh vô hạn số nguyên tố]
*Hình 3: Các proof kinh điển của toán học không chỉ đẹp; chúng huấn luyện thói quen suy luận bền vững cho dân khoa học máy tính.*

---

## Phần 5: Testing và formal proof — vì sao cả hai đều cần

### 5.1. Testing làm gì tốt

Testing mạnh ở chỗ:

- gần hành vi runtime thật,
- rẻ hơn trong nhiều dự án,
- tích hợp tốt với CI/CD,
- bắt được regression,
- minh họa bug cụ thể rất nhanh.

Ví dụ,
unit test,
integration test,
property-based test,
fuzzing,
end-to-end test
đều cực kỳ thực dụng.

### 5.2. Proof làm gì tốt

Formal proof mạnh ở chỗ:

- cho bảo đảm tổng quát hơn,
- không phụ thuộc vào sampling của test cases,
- tìm được lỗi ở trạng thái hiếm,
- đặc biệt giá trị trong hệ thống sống còn.

Nếu test hỏi:
“ta đã thử những trường hợp nào?”,
thì proof hỏi:
“với mọi trường hợp phù hợp giả thiết, điều gì luôn đúng?”

### 5.3. Vì sao đối lập testing với proof là sai

Thực tế engineering tốt thường kết hợp:

- proof cho lõi critical,
- tests cho integration và regression,
- monitoring cho môi trường thật,
- review cho chất lượng thiết kế,
- static analysis cho lớp bảo vệ bổ sung.

Nói cách khác,
testing và proof không loại trừ nhau.
Chúng là hai lớp phòng thủ khác nhau.

### 5.4. Góc nhìn thực tế cho sinh viên

Không phải dự án nào cũng cần Coq hay Isabelle.
Nhưng dự án nào cũng cần tư duy chứng minh ở một mức nào đó.

Khi bạn giải thích vì sao thuật toán đúng,
vì sao loop không phá invariant,
vì sao API không thể tạo trạng thái mâu thuẫn,
hay vì sao optimization không đổi kết quả,
bạn đang dùng tinh thần của proof.

---

## Phần 6: Tương lai của chứng minh trong computing

Khi phần mềm chi phối ngày càng nhiều lĩnh vực quan trọng,
nhu cầu correctness sẽ tăng theo.

Ta sẽ thấy nhiều hơn:

- proof assistants dùng trong công nghiệp,
- AI hỗ trợ viết proof,
- verified components trong chuỗi cung ứng phần mềm,
- đặc tả hình thức đi kèm code,
- tool tự tìm invariant và counterexample.

Điều thú vị là:
AI có thể giúp con người viết proof nhanh hơn,
nhưng tiêu chuẩn “lập luận hợp lệ” vẫn không đổi.
Đó là di sản của Euclid sống lại trong thế kỷ XXI.

---

## Kết luận

Từ *Elements* đến Hoare logic,
từ proof by contradiction đến security reductions,
phương pháp chứng minh đã đi một chặng đường rất dài.

Nhưng lõi của nó vẫn giống nhau:
không chấp nhận mơ hồ,
không nhầm trực giác với chân lý,
và luôn đòi hỏi mỗi bước suy luận phải có lý do.

Trong toán học,
đó là tiêu chuẩn của tri thức.
Trong khoa học máy tính,
đó là nền của correctness,
security,
và engineering có trách nhiệm.

---

## Bài tập thực hành

### Bài tập 1: Chọn phương pháp chứng minh phù hợp

Với mỗi phát biểu sau, chọn phương pháp chứng minh tốt nhất và giải thích ngắn gọn:

1. $$\sqrt{3}$$ là số vô tỷ.
2. Mọi số nguyên tố lớn hơn 2 đều là số lẻ.
3. $$n^3 + 2n$$ chia hết cho 3 với mọi $$n \in \N$$.

<details>
<summary>Đáp án</summary>

1. Proof by contradiction (giả sử hữu tỷ → dẫn đến mâu thuẫn).
2. Proof by cases hoặc direct proof (chia 2 trường hợp chẵn/lẻ).
3. Mathematical induction hoặc direct proof (chia 3 trường hợp theo modulo 3).

</details>

### Bài tập 2: Hoàn thiện chứng minh bằng mâu thuẫn

Chứng minh: Nếu $$a^2$$ là số chẵn thì $$a$$ là số chẵn (dùng proof by contradiction).

<details>
<summary>Đáp án</summary>

Giả sử $$a$$ lẻ → $$a = 2k+1$$ → $$a^2 = 4k^2 + 4k + 1$$ (lẻ) → mâu thuẫn với giả thiết $$a^2$$ chẵn. Vậy $$a$$ phải chẵn.

</details>

### Bài tập 3: Ứng dụng Hoare Logic

Viết điều kiện tiền đề (precondition) và hậu đề (postcondition) cho đoạn code sau:

```python
x = x + 1
```

<details>
<summary>Đáp án</summary>

- Precondition: `x = n`
- Postcondition: `x = n + 1`

</details>

## Tóm tắt

Chứng minh là ngôn ngữ của toán học và cũng là tiêu chuẩn của tri thức. Trong khoa học máy tính, đó là nền của correctness, security, và engineering có trách nhiệm. Các phương pháp direct proof, contradiction, induction và Hoare logic là những công cụ thiết yếu để xây dựng phần mềm đáng tin cậy.
