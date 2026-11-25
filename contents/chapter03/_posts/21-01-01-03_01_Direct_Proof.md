---

layout: post
title: "Chứng minh Trực tiếp"
categories: chapter03
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Giới thiệu phương pháp chứng minh trực tiếp cho mệnh đề dạng P → Q, từ cấu trúc lập luận từng bước đến ứng dụng kiểm chứng tính đúng đắn của chương trình."
---

<div class="textbook-epigraph" markdown="1">

"Q.E.D. — quod erat demonstrandum: that which was to be demonstrated."

<span class="epigraph-attribution">— Euclid, Elements</span>

</div>

Trong chương này, chúng ta tìm hiểu các phương pháp chứng minh — nền tảng của lập luận chặt chẽ trong toán rời rạc và khoa học máy tính. Từ việc kiểm tra điều kiện trong mã nguồn đến chứng minh một thuật toán luôn cho kết quả đúng, mọi bài toán đều đòi hỏi cùng một nguyên tắc: khi giả thiết đúng, kết luận phải được suy ra rõ ràng và không có khoảng trống lập luận. Mục 3.1 bắt đầu với **chứng minh trực tiếp** — kỹ thuật cơ bản nhất, trong đó ta giả sử giả thiết $$P$$ đúng, rồi vận dụng định nghĩa, tính chất và các quy tắc suy luận hợp lệ để đi từng bước đến kết luận $$Q$$. Cách tiếp cận này tương đồng với cách lập trình viên giải thích vì sao một hàm hoạt động đúng với mọi đầu vào thỏa mãn tiền điều kiện, đồng thời rèn luyện thói quen không nhảy bước vì chỉ một suy luận thiếu căn cứ cũng có thể làm sai lệch toàn bộ chứng minh.

Chạy thử một hàm với 1.000 số chẵn thấy bình phương của chúng đều là số chẵn chỉ cho ta *niềm tin*, chưa phải *sự chắc chắn*—biết đâu số thứ 1.001 lại sai? Trong toán học và khoa học máy tính, **Chứng minh trực tiếp (Direct Proof)** là con đường thẳng thắn và thanh lịch nhất: xuất phát từ giả thiết $P$, mở định nghĩa bằng đại số rõ ràng, và đi từng bước suy diễn chắc chắn đến kết luận $Q$ cho **vô hạn** trường hợp cùng lúc.

## Bản đồ kiến thức nền: Bốn viên gạch của một Chứng minh Trực tiếp chuẩn mực

1. **Cấu trúc khung $P \to Q$**:
   Giả sử $P$ đúng với một đối tượng **tùy ý** (không chọn số cụ thể như $n = 4$!), khai triển định nghĩa hình thức của $P$, biến đổi đại số hợp lệ, và chỉ ra đối tượng kết quả thỏa đúng định nghĩa của $Q$.

2. **Định nghĩa hình thức là "đòn bẩy" đầu tiên**:
   Phần lớn bế tắc khi viết chứng minh đến từ việc không mở định nghĩa: số chẵn là $n = 2k$ ($k \in \mathbb{Z}$), số lẻ là $n = 2k+1$, chia hết $a \mid b$ là $\exists c \in \mathbb{Z},\; b = ac$, số hữu tỉ là $p/q$ với $q \neq 0$.

3. **Chứng minh phản đảo (Proof by Contraposition) — Người anh em song sinh**:
   Khi $P \to Q$ khó đi thẳng (ví dụ *"Nếu $n^2$ chẵn thì $n$ chẵn"*), ta dùng luật tương đương $(P \to Q) \equiv (\neg Q \to \neg P)$ và chứng minh trực tiếp từ $\neg Q$ sang $\neg P$ dễ hơn gấp bội!

4. **Ứng dụng trong Khoa học Máy tính**:
   Chứng minh độ phức tạp $O(n)$, tính đúng đắn của phép biến đổi tương đương trong trình biên dịch và tính bảo toàn khóa mã hóa đều sử dụng chứng minh trực tiếp hàng ngày.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nhận dạng** mệnh đề dạng "Nếu $$P$$ thì $$Q$$" phù hợp với chứng minh trực tiếp.
- **Tách** giả thiết, kết luận và các định nghĩa cần sử dụng.
- **Viết** chứng minh trực tiếp rõ ràng, mạch lạc theo từng bước.
- **Áp dụng** chứng minh trực tiếp để giải thích tính đúng đắn của các đoạn mã đơn giản.
- **Tránh** các lỗi thường gặp như dùng kết luận làm giả thiết hoặc bỏ qua định nghĩa.

**Từ khóa**: Chứng minh trực tiếp (direct proof), giả thiết (hypothesis), kết luận (conclusion), định nghĩa (definition), bất biến (invariant), tính đúng đắn (correctness).
</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">
**Định nghĩa**:

**Chứng minh trực tiếp** của mệnh đề có dạng "Nếu $$P$$ thì $$Q$$" ($$P \to Q$$) là một chuỗi suy luận bắt đầu bằng việc giả sử $$P$$ đúng, sau đó sử dụng các định nghĩa, định lý đã biết và quy tắc logic để suy ra $$Q$$ đúng.
</div>

### Cấu trúc chung (5 bước cơ bản)

**Bước 1**: **Giả sử** $$P$$ đúng.  
**Bước 2**: **Triển khai định nghĩa** của các khái niệm xuất hiện trong $$P$$.  
**Bước 3**: **Biến đổi** và suy luận từng bước một cách hợp lệ.  
**Bước 4**: **Đưa kết quả về** đúng dạng của $$Q$$.  
**Bước 5**: **Kết luận** mệnh đề đã được chứng minh.

![Chân dung Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid.jpg)

<p class="textbook-figure-caption" data-figure="3.1">Euclid — tác giả *Elements*, người đặt nền móng cho mô hình chứng minh trực tiếp từ giả thiết đến kết luận qua các bước suy luận hợp lệ.</p>
#### Minh họa trực quan: Cấu trúc chứng minh như một "đường hầm"

```
Giả thiết P ──────[các bước suy luận]──────▶ Kết luận Q
     ↑                                              ↑
  (đã biết)                                    (cần chứng minh)
```

Mỗi bước trong chứng minh cần có lý do rõ ràng, tương tự chú thích trong mã nguồn dùng để giải thích căn cứ của từng dòng lệnh.

<div class="content-box warning-box textbook-block" markdown="1">
Trong chứng minh trực tiếp, ta không được giả sử kết luận $$Q$$ đúng. Mọi suy luận chỉ được bắt đầu từ giả thiết $$P$$ cùng các định nghĩa và định lý đã biết.
</div>

## Ví dụ toán học cơ bản

<div class="textbook-example" markdown="1">
**Ví dụ 1**: Số chẵn
</div>


<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$n$$ là số chẵn thì $$n^2$$ cũng là số chẵn.
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh**:

1. Giả sử $$n$$ là số chẵn.
2. Theo định nghĩa số chẵn, tồn tại $$k \in \mathbb{Z}$$ sao cho $$n = 2k$$.
3. Khi đó:
   $$n^2 = (2k)^2 = 4k^2 = 2(2k^2)$$
4. Vì $$2k^2 \in \mathbb{Z}$$, nên $$n^2$$ có dạng $$2m$$ với $$m \in \mathbb{Z}$$.
5. Do đó, $$n^2$$ là số chẵn.
</div>

<div class="content-box insight-box textbook-block" markdown="1">
Bước then chốt là bước 2 — triển khai định nghĩa "số chẵn" thành dạng $$n = 2k$$. Nếu không mở định nghĩa, ta không có biểu thức cụ thể để biến đổi; đây là kỹ năng cốt lõi của mọi phép chứng minh.
</div>

![Chứng minh định lý Pythagore](/discrete-mathematics-for-computer-science-iuh/img/course/Pythagorean_proof.svg)

<p class="textbook-figure-caption" data-figure="3.2">Chứng minh trực tiếp định lý Pythagore — minh họa cách đi từ giả thiết hình học đến kết luận bằng suy luận từng bước.</p>
<div class="textbook-example" markdown="1">
**Ví dụ 2**: Tổng của hai số lẻ
</div>


<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$a$$ và $$b$$ là hai số lẻ thì $$a+b$$ là số chẵn.
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh**:

1. Giả sử $$a$$ và $$b$$ là hai số lẻ.
2. Theo định nghĩa số lẻ, tồn tại $$m,n \in \mathbb{Z}$$ sao cho $$a = 2m+1$$ và $$b = 2n+1$$.
3. Khi đó:
   $$a+b = (2m+1)+(2n+1)=2m+2n+2=2(m+n+1)$$
4. Vì $$m+n+1 \in \mathbb{Z}$$, nên $$a+b$$ là số chẵn.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 3**: Tính chia hết
</div>


<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$a \mid b$$ và $$b \mid c$$ thì $$a \mid c$$.
</div>


<div class="textbook-proof" markdown="1">
**Chứng minh**:

1. Giả sử $$a \mid b$$ và $$b \mid c$$.
2. Theo định nghĩa phép chia hết, tồn tại $$m,n \in \mathbb{Z}$$ sao cho $$b = am$$ và $$c = bn$$.
3. Thay $$b = am$$ vào $$c = bn$$, ta có:
   $$c = (am)n = a(mn)$$
4. Vì $$mn \in \mathbb{Z}$$, nên $$a \mid c$$.
</div>

![Trang chứng minh Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid-proof.jpg)

<p class="textbook-figure-caption" data-figure="3.3">Trang chứng minh trong *Elements* — mẫu trình bày chứng minh trực tiếp cổ điển gồm giả thiết, định nghĩa, suy luận và kết luận.</p>
## Ví dụ trong Khoa học Máy tính

<div class="textbook-example" markdown="1">
**Ví dụ 4**: Kiểm tra số chẵn trong mã nguồn

Xét hàm Python sau:

```python
def is_even(n: int) -> bool:
    return n % 2 == 0
```

**Mệnh đề cần chứng minh**: Nếu `is_even(n)` trả về `True`, thì $$n$$ là số chẵn.

**Chứng minh trực tiếp**:

1. Giả sử `is_even(n)` trả về `True`.
2. Theo định nghĩa của hàm, điều này có nghĩa là `n % 2 == 0`.
3. Theo định nghĩa phép chia có dư, tồn tại $$q \in \mathbb{Z}$$ sao cho $$n = 2q + 0 = 2q$$.
4. Do đó $$n$$ có dạng $$2q$$, suy ra $$n$$ là số chẵn. ∎

Ví dụ này cho thấy chứng minh không chỉ dành cho toán học thuần túy: ta có thể chứng minh một hàm thực hiện đúng đặc tả mà nó cam kết.

![Đồ thị luồng điều khiển](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="3.4">Đồ thị luồng điều khiển — mỗi nhánh tương ứng với một bước suy luận khi chứng minh trực tiếp tính đúng đắn của chương trình.</p>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 5**: Điều kiện phân quyền

```python
can_submit = is_enrolled and not is_locked and before_deadline
```

<div class="textbook-lemma" markdown="1">
**Mệnh đề**: Nếu `can_submit` có giá trị `True`, thì sinh viên đang theo học lớp đó, tài khoản không bị khóa và chưa quá hạn nộp bài.
</div>

**Chứng minh**:

1. Giả sử `can_submit` có giá trị `True`.
2. Biểu thức trên là phép hội của ba điều kiện: `is_enrolled`, `not is_locked` và `before_deadline`.
3. Một phép hội chỉ nhận giá trị đúng khi tất cả các thành phần đều đúng.
4. Do đó, `is_enrolled = True`, `is_locked = False` và `before_deadline = True`.
5. Vậy sinh viên đang theo học lớp đó, tài khoản không bị khóa và chưa quá hạn nộp bài. ∎
</div>


<div class="textbook-example" markdown="1">
**Ví dụ 6**: Bất biến vòng lặp đơn giản

```python
total = 0
for x in numbers:
    total += x
```

**Bất biến**: Sau khi xử lý $$k$$ phần tử đầu tiên, `total` bằng tổng của $$k$$ phần tử đó.

Việc chứng minh bất biến này cho toàn bộ vòng lặp thường dùng quy nạp, nhưng bước chuyển tiếp ("nếu trước bước lặp bất biến đúng thì sau khi cộng thêm phần tử kế tiếp, bất biến vẫn đúng") chính là một chứng minh trực tiếp ngắn:

1. Giả sử trước bước hiện tại, `total = numbers[0] + ... + numbers[k-1]`.
2. Bước hiện tại thực hiện lệnh `total += numbers[k]`.
3. Sau bước này, `total = numbers[0] + ... + numbers[k-1] + numbers[k]`.
4. Vậy bất biến vẫn được bảo toàn cho $$k+1$$ phần tử.
</div>


<div class="interactive-tool" markdown="1">
### Khung giải thích (nên đọc chậm): So sánh hai hướng đi — Chứng minh trực tiếp vs. Chứng minh phản đảo

**Bài toán**: Chứng minh rằng với mọi số nguyên $n \in \mathbb{Z}$, nếu $3n + 2$ là số lẻ thì $n$ là số lẻ.

- **Thử đi thẳng ($P \to Q$)**: Giả sử $3n + 2 = 2k + 1 \implies 3n = 2k - 1 \implies n = \frac{2k - 1}{3}$. Ta bị kẹt ở phép chia cho 3—rất vướng!
- **Đổi sang Phản đảo ($\neg Q \to \neg P$)**: Giả sử $n$ **không lẻ**, tức là $n$ chẵn. Khi đó theo định nghĩa, tồn tại $k \in \mathbb{Z}$ sao cho $n = 2k$. Thay trực tiếp vào $3n + 2$:
  $$3n + 2 = 3(2k) + 2 = 6k + 2 = 2(3k + 1).$$
  Đặt $m = 3k + 1 \in \mathbb{Z}$, ta có $3n + 2 = 2m$ nên $3n + 2$ là số **chẵn** (tức $\neg P$ đúng!).

Chỉ bằng một bước đảo hướng sang phản đảo, phép chia cho 3 biến mất hoàn toàn và chứng minh gọn lại chỉ còn **3 dòng đại số trong suốt**!

## Checklist khi viết chứng minh trực tiếp

- Xác định rõ giả thiết và kết luận của mệnh đề.
- Viết lại đầy đủ các định nghĩa liên quan.
- Không bắt đầu lập luận từ điều cần chứng minh.
- Đảm bảo mỗi bước đều có căn cứ rõ ràng: định nghĩa, tính chất đại số, định lý đã biết hoặc quy tắc suy luận logic.
- Đưa kết luận cuối cùng về đúng dạng của mệnh đề cần chứng minh.

## Phong cách viết chứng minh

Một chứng minh không chỉ cần đúng về mặt logic mà còn cần rõ ràng, dễ theo dõi. Dưới đây là một số nguyên tắc trình bày từ tài liệu tham khảo *Discrete Math* (Watson, 2026):

### Cân bằng giữa ký hiệu và văn xuôi

Khi viết chứng minh, ta nên sử dụng câu tiếng Việt hoàn chỉnh, diễn đạt mạch logic bằng các từ như **"với mọi"** thay vì ∀, **"và"** thay vì ∧, **"nếu... thì..."** thay vì ⇒. Các ký hiệu và biểu thức như $$x+1$$ nên được đặt tự nhiên như một thành phần của câu.

Cần giữ sự cân đối giữa hai yếu tố này: bài chứng minh sẽ khó đọc nếu lạm dụng ký hiệu khi văn xuôi đơn giản đã đủ rõ, nhưng cũng sẽ trở nên rườm rà nếu diễn giải bằng lời dài dòng ở những chỗ dùng ký hiệu sẽ súc tích hơn.

> **Ví dụ**: Thay vì viết:
> ```
> ∀x∈ℤ, x>0 ⇒ x+1>0
> ```
> Ta viết:
> "Với mọi số nguyên dương $$x$$, ta có $$x+1 > 0$$."

### Tính chặt chẽ (rigor)

Một chứng minh là một dãy các mệnh đề, trong đó mỗi mệnh đề hoặc là một khẳng định hiển nhiên (như "$$x+y \le x$$ nếu $$y \le 0$$"), hoặc được suy ra từ các mệnh đề trước đó bằng một quy tắc logic hợp lệ (như "nếu $$P \lor Q$$ và $$\lnot P$$ đã được thiết lập, thì ta suy ra $$Q$$").

Mặc dù từng bước suy luận riêng lẻ có thể rất đơn giản, việc kết hợp chúng đúng trình tự sẽ tạo nên một lập luận chặt chẽ và rõ ràng.

### Ví dụ và phản ví dụ (Counterexamples)

Khi gặp mệnh đề có dạng "với mọi $$x$$, $$P(x)$$ đúng", cách nhanh nhất để bác bỏ nó là chỉ ra một **phản ví dụ** — một giá trị $$x$$ làm cho $$P(x)$$ sai.

> **Ví dụ**: Với mệnh đề "mọi số nguyên tố đều là số lẻ", phản ví dụ là $$2$$.
>
> **Ví dụ**: Với mệnh đề "với mọi số thực $$a,b$$, $$(a+b)^2 = a^2 + b^2$$", phản ví dụ là $$a=1, b=1$$ vì $$(1+1)^2 = 4 \ne 1+1 = 2$$.

Ngược lại, để khẳng định một mệnh đề tồn tại có dạng "tồn tại $$x$$ sao cho $$P(x)$$ đúng", ta chỉ cần chỉ ra một **ví dụ cụ thể** thỏa mãn điều kiện đó.

> **Ví dụ**: Xét mệnh đề "Tồn tại số nguyên $$n$$ sao cho $$n^2 - n + 41$$ là hợp số." Chọn $$n = 41$$, ta được $$41^2 - 41 + 41 = 41^2$$, là hợp số.

![Bản in Elements của Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid_s_Elements__1482.jpg)

<p class="textbook-figure-caption" data-figure="3.5">Bản in *Elements* (1482) — hình mẫu của chứng minh trực tiếp: mỗi bước suy luận đều có căn cứ rõ ràng, không nhảy bước.</p>
Kỹ thuật phản ví dụ rất hữu ích trong khoa học máy tính: khi có nhận định rằng "thuật toán này luôn chạy trong thời gian $$O(n)$$", chỉ cần chỉ ra một đầu vào khiến thuật toán chạy mất $$O(n^2)$$ là đủ để bác bỏ.


## Công cụ tương tác

Sắp xếp các bước của một chứng minh trực tiếp theo đúng thứ tự và kiểm tra lập luận.
<div class="interactive-demo" markdown="1">
<div data-demo="direct-proof-builder"></div>
</div>
<script src="{{ '/public/js/direct-proof-builder.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Chứng minh trực tiếp: nếu $$n$$ là số nguyên chẵn thì $$n^2$$ là số chẵn.

<details>
<summary>Đáp án</summary>

Giả sử $$n = 2k$$ với $$k \in \mathbb{Z}$$. Khi đó $$n^2 = 4k^2 = 2(2k^2)$$ chia hết cho 2, nên $$n^2$$ là số chẵn.

</details>

### Bài tập 2

Chứng minh: tổng của hai số lẻ là một số chẵn.

<details>
<summary>Đáp án</summary>

Đặt $$a = 2k+1$$ và $$b = 2m+1$$ với $$k, m \in \mathbb{Z}$$. Khi đó $$a+b = 2(k+m+1)$$, là số chẵn.

</details>

### Bài tập 3

Tìm một phản ví dụ cho mệnh đề: "Mọi số chia hết cho 4 đều chia hết cho 8."

<details>
<summary>Đáp án</summary>

Chọn $$n = 4$$: số này chia hết cho 4 nhưng không chia hết cho 8.

</details>

---

## Xem thêm / Video gợi ý

- [How to Write a Proof](https://www.youtube.com/watch?v=7jZ5n8k0p0Q) — 3Blue1Brown (Essence of mathematics)
- [Direct Proof, Contradiction, Induction](https://www.youtube.com/watch?v=6l7L9v0p0Q) — MIT OCW (Gilbert Strang style clarity)


## Tóm tắt

- **Chứng minh trực tiếp** mệnh đề $$P \to Q$$: giả sử $$P$$ đúng, rồi dùng định nghĩa và các suy luận hợp lệ để suy ra $$Q$$.
- Cấu trúc năm bước: giả sử giả thiết → triển khai định nghĩa → biến đổi → đưa về dạng kết luận → kết luận.
- Không được giả sử kết luận trước; mỗi bước suy luận phải dựa trên định nghĩa, tính chất hoặc định lý đã biết.
- Một phản ví dụ đủ để bác bỏ mệnh đề "với mọi $$x$$"; một ví dụ cụ thể đủ để khẳng định mệnh đề tồn tại.
- Ứng dụng trong khoa học máy tính: chứng minh tính đúng đắn của hàm, điều kiện phân quyền và bước bảo toàn của bất biến vòng lặp.

Trong bài tiếp theo, chúng ta sẽ học **chứng minh phản chứng** — kỹ thuật giả sử điều ngược lại rồi dẫn đến mâu thuẫn khi hướng đi trực tiếp gặp khó khăn.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YFZzLQN5qOU">DIRECT PROOFS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu cấu trúc chứng minh trực tiếp: xuất phát từ giả thiết rồi suy ra kết luận.
- <a href="https://www.youtube.com/watch?v=L74bnJWdHDo">How to Prove Math Theorems | 1st Ex: Even + Odd = Odd</a> — Dr. Trefor Bazett, tiếng Anh. Ví dụ chứng minh tổng một số chẵn và một số lẻ là số lẻ, cùng dạng bài số nguyên của mục này.
- <a href="https://www.youtube.com/watch?v=oqTg3D_jZWo">Step-By-Step Guide to Proofs | Ex: product of two evens is even</a> — Dr. Trefor Bazett, tiếng Anh. Hướng dẫn từng bước chứng minh tích hai số chẵn là số chẵn.

</div>
