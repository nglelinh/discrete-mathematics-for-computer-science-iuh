---

layout: post
title: "Chứng minh Phản chứng"
categories: chapter03
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Giới thiệu phương pháp chứng minh phản chứng (proof by contradiction), cách nhận diện mâu thuẫn và ứng dụng trong toán rời rạc cùng khoa học máy tính."
---

Có những chân lý sâu sắc nhất của toán học và khoa học máy tính mà con đường đi thẳng dường như bịt kín: làm sao chứng minh $$\sqrt{2}$$ **không thể** viết dưới dạng phân số, số nguyên tố là **vô hạn**, hay không tồn tại thuật toán nào giải được **Bài toán Dừng (Halting Problem)**? Khi đối mặt với các phát biểu phủ định hoặc "không tồn tại", **Chứng minh Phản chứng (Proof by Contradiction)** là vũ khí sắc bén nhất: tạm giả sử điều ta muốn chứng minh là *sai*, rồi đẩy giả thiết đó đến một mâu thuẫn không thể cứu vãn.

## Kiến thức cần nhớ: Bốn trụ cột của Chứng minh Phản chứng

1. **Cơ sở Logic ($$\neg P \to F \equiv P$$)**:
   Nếu giả sử $$\neg P$$ đúng mà qua các bước suy diễn hợp lệ ta dẫn tới một mâu thuẫn $$r \land \neg r$$ (luôn Sai), thì giả thiết $$\neg P$$ buộc phải Sai—suy ra $$P$$ chắc chắn Đúng!

2. **Bốn bước chuẩn mực**:
   (1) Giả sử ngược lại $$\neg P$$ đúng (với $$A \to B$$, phủ định là **$$A \land \neg B$$**!); (2) Suy diễn hợp lệ từ giả thiết đó; (3) Chỉ rõ mâu thuẫn tường minh (ví dụ số vừa chẵn vừa lẻ, phân số tối giản nhưng tử mẫu cùng chia hết cho 2); (4) Kết luận $$P$$ đúng.

3. **Khi nào nên nghĩ ngay đến Phản chứng?**:
   Khi định lý chứa từ khóa *"không tồn tại"*, *"vô tỉ"*, *"vô hạn"*, *"duy nhất"*, hoặc *"không có thuật toán nào..."*—nơi việc giả sử đối tượng đó *có tồn tại* cho ta ngay một công thức cụ thể để thao tác đại số.

4. **Dấu ấn lịch sử trong Khoa học Máy tính**:
   Định lý Euclid (vô hạn số nguyên tố), tính vô tỉ của $$\sqrt{2}$$, bài toán Dừng của Alan Turing (1936), và định lý CAP trong hệ phân tán đều là những kiệt tác của chứng minh phản chứng.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau khi học xong bài này, sinh viên có thể:

1. Phát biểu đúng nguyên lý của chứng minh phản chứng.
2. Phân biệt **giả sử phản chứng** với **giả thiết ban đầu** của bài toán.
3. Nhận diện mâu thuẫn (contradiction) dưới nhiều dạng khác nhau.
4. Viết một chứng minh phản chứng chặt chẽ, không nhảy bước.
5. Áp dụng phương pháp phản chứng cho các ví dụ toán học kinh điển và các bài toán trong khoa học máy tính.
6. Tránh những lỗi thường gặp khi sử dụng phản chứng.
</div>

## Ý tưởng cốt lõi (4 bước cơ bản)

Để chứng minh mệnh đề `P` đúng, ta thực hiện như sau:

#### Minh họa trực quan: Cấu trúc chứng minh phản chứng

```
Giả sử ¬P đúng
        ↓
Dẫn đến mâu thuẫn
        ↓
Vậy ¬P phải sai
        ↓
Kết luận: P đúng
```

**4 bước thực hiện**:

1. **Giả sử ngược lại** rằng `P` sai, tức là `¬P` đúng.
2. Từ giả sử đó, kết hợp với các giả thiết và kiến thức đã biết, suy ra một điều vô lý (mâu thuẫn).
3. Vì mâu thuẫn không thể xảy ra, giả sử `¬P` phải sai.
4. Do đó, `P` phải đúng.

![Tam giác mâu thuẫn](/discrete-mathematics-for-computer-science-iuh/img/course/Absurd_triangle.svg)

<p class="textbook-figure-caption" data-figure="3.6">Tam giác mâu thuẫn (reductio ad absurdum) — minh họa trực quan chứng minh phản chứng: giả sử phủ định dẫn đến điều vô lý.</p>
Nói ngắn gọn:

> Nếu giả sử "`P` sai" dẫn đến mâu thuẫn, thì `P` phải đúng.

## Vì sao phản chứng hoạt động?

Nhiều sinh viên mới học thường băn khoăn vì sao việc giả sử điều ngược lại dẫn đến vô lý lại cho phép ta kết luận mệnh đề ban đầu đúng. Cơ sở của phương pháp này nằm ở một nguyên lý logic cơ bản:

- Với một mệnh đề `P`, chỉ có hai khả năng: `P` đúng hoặc `P` sai (`¬P` đúng).
- Nếu kiểm tra khả năng `¬P` và thấy khả năng này dẫn đến mâu thuẫn logic (tức không thể tồn tại), thì chỉ còn lại khả năng `P` đúng.

### Trực giác đời thường

Giả sử có phát biểu: "Thiết bị này không thể cùng lúc vừa **tắt nguồn hoàn toàn** vừa **đang gửi dữ liệu qua mạng**."

Để kiểm tra phát biểu này bằng phản chứng, ta giả sử điều ngược lại xảy ra: thiết bị đang tắt nguồn hoàn toàn nhưng đồng thời vẫn truyền dữ liệu qua mạng. Hai trạng thái này mâu thuẫn trực tiếp với chính định nghĩa của "tắt nguồn hoàn toàn", nên giả sử đó không thể đúng.

Chứng minh phản chứng vận hành theo đúng nguyên tắc đó: ta kiểm tra xem hệ thống suy luận có thể nhất quán dưới giả sử phủ định hay không; nếu không thể, kết luận ban đầu được xác nhận.

### Cơ sở logic hình thức

Về mặt logic hình thức:

- Nếu `¬P → (Q ∧ ¬Q)`
- thì `¬P` không thể đúng
- suy ra `P` phải đúng.

Trong đó, `(Q ∧ ¬Q)` là một mâu thuẫn rõ ràng: một mệnh đề `Q` đồng thời vừa đúng vừa sai.

![Chứng minh Pythagore](/discrete-mathematics-for-computer-science-iuh/img/course/Pythagorean_proof.svg)

<p class="textbook-figure-caption" data-figure="3.7">Chứng minh hình học cổ điển — nền tảng của lập luận chặt chẽ mà phản chứng kế thừa khi cần loại bỏ khả năng ngược lại.</p>
## Khi nào nên nghĩ đến phản chứng?

Phản chứng đặc biệt phù hợp trong các tình huống sau:

### Kết luận mang tính phủ định

Ví dụ:

- Không tồn tại thuật toán thỏa mãn yêu cầu đã cho.
- Không có số nguyên lớn nhất thỏa mãn tính chất đó.
- Không thể xây dựng cấu hình như mô tả.

### Kết luận khó tiếp cận trực tiếp

Có những bài toán mà từ giả thiết đến kết luận không có lộ trình biến đổi trực tiếp rõ ràng, nhưng khi giả sử điều ngược lại, ta có thêm thông tin cụ thể để khai thác và cấu trúc bài toán sớm lộ ra.

### Chứng minh tính bất khả thi (impossibility)

Nhiều phát biểu trong khoa học máy tính có dạng này:

- Không thể quyết định một bài toán trong mọi trường hợp.
- Không thể có cấu trúc dữ liệu đồng thời thỏa mãn mọi yêu cầu đặt ra.
- Không thể có thuật toán nhanh hơn một giới hạn nhất định dưới giả thiết đã cho.

### Mâu thuẫn rút ra trực tiếp từ định nghĩa

Đôi khi chỉ cần bám sát định nghĩa là đủ để phát hiện mâu thuẫn, chẳng hạn:

- Một số vừa chẵn vừa lẻ.
- Một phần tử vừa thuộc tập hợp vừa không thuộc tập hợp đó.
- Một trạng thái hệ thống vừa đạt được ("reachable") vừa không đạt được ("unreachable").

### Giải thích: Theo dõi từng bước chứng minh kinh điển $$\sqrt{2}$$ là số vô tỉ

Để thấy rõ sức mạnh của việc "tạm giả sử có tồn tại", hãy kiểm tra từng dòng của chứng minh 2.500 năm tuổi này:

1. **Giả sử phản chứng**: Giả sử $$\sqrt{2}$$ là số **hữu tỉ**. Khi đó tồn tại hai số nguyên $$a, b \in \mathbb{Z}$$ ($$b \neq 0$$) sao cho $$\sqrt{2} = \frac{a}{b}$$ và phân số này **tối giản**, tức $$\gcd(a, b) = 1$$ (không cùng chia hết cho 2).
2. **Bình phương hai vế**:
   $$2 = \frac{a^2}{b^2} \implies a^2 = 2b^2.$$
3. **Suy ra $$a$$ chẵn**: Vì $$a^2 = 2b^2$$ là số chẵn nên $$a$$ phải chẵn (nếu $$a$$ lẻ thì $$a^2$$ lẻ). Do đó $$a = 2k$$ với $$k \in \mathbb{Z}$$.
4. **Thế ngược lại để suy ra $$b$$ chẵn**:
   $$(2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2.$$
   Suy ra $$b^2$$ chẵn, kéo theo $$b$$ cũng là số **chẵn**!
5. **Bắt quả tang mâu thuẫn**: Cả $$a$$ và $$b$$ đều chia hết cho $$2 \implies \gcd(a, b) \ge 2$$, mâu thuẫn trực diện với giả thiết $$\gcd(a, b) = 1$$ ở Bước 1!
6. **Kết luận**: Giả sử ban đầu sai, vậy $$\sqrt{2}$$ chắc chắn là **số vô tỉ**.

## Quy trình viết chứng minh phản chứng

Một khuôn mẫu an toàn gồm năm bước:

1. **Nêu rõ điều cần chứng minh.**
2. **Đặt giả sử phản chứng**: viết chính xác phủ định của kết luận.
3. **Suy luận từng bước** từ giả sử phản chứng kết hợp với các dữ kiện đã biết.
4. **Chỉ rõ mâu thuẫn** nằm ở đâu.
5. **Kết luận** giả sử phản chứng sai, suy ra mệnh đề ban đầu đúng.

### Mẫu trình bày

> Ta cần chứng minh `P`.
>
> Giả sử ngược lại rằng `¬P` đúng.
>
> Từ giả sử này, suy ra ...
>
> Tuy nhiên, điều này mâu thuẫn với ...
>
> Vậy giả sử `¬P` sai. Do đó `P` đúng. ∎

## Ví dụ 1: Chứng minh √2 là số vô tỷ

Đây là ví dụ kinh điển cho thấy phản chứng có thể chuyển một khẳng định phủ định ("không phải số hữu tỷ") thành một chuỗi suy luận ngắn gọn và chặt chẽ.

<div class="textbook-theorem" markdown="1">
**Định lý:** `√2` là số vô tỷ (irrational number).
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh:**

Giả sử phản chứng rằng `√2` là số hữu tỷ. Khi đó, tồn tại các số nguyên `a, b` sao cho:

- `b ≠ 0`,
- `gcd(a, b) = 1` (tức phân số `a / b` tối giản),
- và `√2 = a / b`.

Bình phương hai vế, ta được `2 = a² / b²`, hay `a² = 2b²`.

Từ đây suy ra `a²` là số chẵn, nên `a` cũng phải là số chẵn. Do đó tồn tại số nguyên `k` sao cho `a = 2k`.

Thế `a = 2k` vào phương trình `a² = 2b²`:

`(2k)² = 2b²`

`4k² = 2b²`

`b² = 2k²`.

Vậy `b²` là số chẵn, suy ra `b` cũng là số chẵn.

Như vậy, cả `a` và `b` đều chẵn. Điều này mâu thuẫn với điều kiện `gcd(a, b) = 1`, vì nếu cả hai cùng chẵn thì chúng có ước chung ít nhất là `2`.

Vậy giả sử `√2` là số hữu tỷ là sai. Do đó `√2` là số vô tỷ.
</div>

![Số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/Prime_numbers.svg)

<p class="textbook-figure-caption" data-figure="3.8">Sàng Eratosthenes — số nguyên tố là bối cảnh của nhiều chứng minh phản chứng kinh điển như tính vô tỷ của căn bậc hai và sự vô hạn của tập số nguyên tố.</p>
### Điều đáng học từ ví dụ này

Mâu thuẫn trong bài không xuất hiện ngay lập tức mà được dẫn ra qua hai bước: giả sử tồn tại một biểu diễn tối giản, sau đó chứng minh biểu diễn ấy thực chất vẫn còn rút gọn được. Mẫu lập luận này xuất hiện thường xuyên trong toán rời rạc và thiết kế thuật toán: giả sử một cấu trúc đã đạt cực trị hoặc tối ưu, rồi chỉ ra vẫn có thể cải thiện hoặc rút gọn nó, từ đó thu được mâu thuẫn.

### Thử nghiệm: Phản chứng từng dòng

Bấm **Bước tiếp** để xem chứng minh `√2` vô tỷ hiện dần với bước mâu thuẫn được tô đỏ; bạn cũng có thể thử với một phân số bất kỳ hoặc chuyển sang chứng minh vô hạn số nguyên tố của Euclid.

<div class="interactive-demo" markdown="1">
<div data-demo="contradiction-explainer" data-tab="sqrt2"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Ví dụ 2: Có vô hạn số nguyên tố

<div class="textbook-theorem" markdown="1">
**Định lý:** Có vô hạn số nguyên tố.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh:**

Giả sử phản chứng rằng chỉ có hữu hạn số nguyên tố. Gọi tất cả các số nguyên tố đó là:

`p₁, p₂, ..., pₙ`.

Xét số:

`N = p₁p₂...pₙ + 1`.

Vì `N > 1`, nên `N` phải có ít nhất một ước nguyên tố. Gọi `p` là một ước nguyên tố của `N`. Theo giả sử ban đầu, mọi số nguyên tố đều nằm trong danh sách `p₁, p₂, ..., pₙ`, nên `p` phải là một trong các số đó.

Khi đó, tích `p₁p₂...pₙ` chia hết cho `p` (tức `p` là ước của `p₁p₂...pₙ`), đồng thời `N` cũng chia hết cho `p`. Do đó hiệu của chúng cũng phải chia hết cho `p`:

`N - p₁p₂...pₙ = 1` chia hết cho `p`.

Tuy nhiên, `1` không chia hết cho bất kỳ số nguyên tố nào (vì mọi số nguyên tố đều lớn hơn `1`). Điều này dẫn đến mâu thuẫn.

Vậy giả sử chỉ có hữu hạn số nguyên tố là sai. Do đó có vô hạn số nguyên tố.
</div>

### Ý nghĩa sư phạm

Điểm nổi bật của chứng minh này là mâu thuẫn được tạo ra bằng cách **xây dựng một đối tượng mới phá vỡ giả sử**. Đây cũng là kỹ thuật phổ biến: giả sử đã liệt kê hết mọi đối tượng, sau đó xây dựng một đối tượng mới không thể thuộc danh sách đó.

## Ví dụ 3: Không tồn tại số nguyên tố lớn nhất

Ví dụ này cho thấy ta có thể kết hợp phản chứng với một định lý đã biết để suy ra mâu thuẫn một cách ngắn gọn.

<div class="textbook-lemma" markdown="1">
**Mệnh đề:** Không tồn tại số nguyên tố lớn nhất.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh bằng phản chứng:**

Giả sử tồn tại số nguyên tố lớn nhất, gọi là `p`.

Khi đó, mọi số nguyên tố đều nhỏ hơn hoặc bằng `p`, nên số lượng số nguyên tố là hữu hạn. Điều này mâu thuẫn với định lý "có vô hạn số nguyên tố" ở Ví dụ 2.

Vậy không tồn tại số nguyên tố lớn nhất.
</div>

### Bài học ở đây

Không phải lúc nào chứng minh phản chứng cũng phải xây dựng lại từ đầu; đôi khi ta có thể sử dụng trực tiếp một định lý đã chứng minh trước đó để chỉ ra mâu thuẫn.

## Ví dụ 4: Trực giác về Bài toán dừng (Halting Problem)

Đây là một ví dụ nổi tiếng trong khoa học máy tính. Ở đây ta trình bày trực giác chính xác về mặt khái niệm mà không đi sâu vào chi tiết của logic hình thức.

**Phát biểu:** Không tồn tại một thuật toán tổng quát quyết định đúng cho mọi chương trình `P` và mọi đầu vào `I` rằng `P(I)` có dừng hay không.

**Ý tưởng phản chứng:**

Giả sử tồn tại một bộ quyết định `H(P, I)` luôn trả về đúng kết quả:

- `YES` nếu chương trình `P` dừng trên đầu vào `I`,
- `NO` nếu chương trình `P` không dừng trên đầu vào `I`.

Ta xây dựng một chương trình mới `D(X)` như sau:

```text
if H(X, X) == YES:
    loop forever
else:
    halt immediately
```

Bây giờ xét lời gọi `D(D)`. Có hai khả năng xảy ra:

1. Nếu `H(D, D) = YES`, thì theo định nghĩa của `D`, chương trình `D(D)` sẽ lặp vô hạn.
2. Nếu `H(D, D) = NO`, thì theo định nghĩa của `D`, chương trình `D(D)` sẽ dừng ngay.

Trong cả hai trường hợp, `H` đều dự đoán sai hành vi của `D(D)`. Điều này mâu thuẫn với giả sử rằng `H` quyết định đúng cho **mọi** chương trình và **mọi** đầu vào.

Vậy không tồn tại thuật toán tổng quát như vậy. ∎

![Đồ thị luồng điều khiển](/discrete-mathematics-for-computer-science-iuh/img/course/Control_flow_graph_of_function_with_two_if_else_statements.svg)

<p class="textbook-figure-caption" data-figure="3.9">Đồ thị luồng điều khiển — mô hình hóa nhánh lặp vô hạn trong chứng minh Bài toán dừng bằng phản chứng.</p>
### Điều cần hiểu đúng

Kết quả này **không có nghĩa** là ta không thể phân tích xem một chương trình cụ thể nào đó có dừng hay không. Nó chỉ khẳng định:

> Không tồn tại một thuật toán duy nhất, tổng quát, luôn trả lời đúng cho mọi chương trình và mọi đầu vào.

Phân biệt rõ phạm vi khẳng định giúp ta tránh diễn giải quá mức nội dung của định lý.

## Ví dụ 5: Trạng thái bất khả thi trong thiết kế hệ thống

Trong thiết kế hệ thống (system design), phản chứng thường được dùng để chứng minh một trạng thái nào đó là **không thể xảy ra** khi các bất biến (invariants) của hệ thống được duy trì.

**Bối cảnh:** Xét một hàng đợi (queue) với hai bất biến:

1. `size` luôn bằng số phần tử thực sự đang có trong cấu trúc dữ liệu.
2. Khi `size = 0` thì con trỏ `front = null`.

<div class="textbook-lemma" markdown="1">
**Mệnh đề:** Nếu hai bất biến trên luôn được duy trì đúng sau mỗi thao tác, thì không thể xuất hiện trạng thái mà `size = 0` nhưng `front` lại trỏ đến một nút hợp lệ.
</div>

**Lập luận phản chứng:**

Giả sử tồn tại một thời điểm mà `size = 0` nhưng `front ≠ null`. Theo bất biến thứ hai, khi `size = 0` thì bắt buộc `front = null`. Như vậy, ta đồng thời có `front = null` và `front ≠ null`, đây là mâu thuẫn.

Do đó, khi các bất biến được bảo toàn, trạng thái trên không thể xảy ra. ∎

### Vì sao ví dụ này quan trọng?

Trong kiểm chứng chương trình (program verification), dạng lập luận này được dùng để phát hiện lỗi logic, chứng minh tính đúng đắn của cấu trúc dữ liệu và khẳng định rằng một nhánh xử lý lỗi không bao giờ bị rơi vào.

## Ví dụ 6: Trực giác phản chứng trong cận dưới độ phức tạp

**Phát biểu:** Bất kỳ thuật toán nào tìm phần tử lớn nhất trong một mảng chưa sắp xếp gồm `n` phần tử đều cần ít nhất `n - 1` phép so sánh trong trường hợp xấu nhất.

Đây là một kết quả cơ bản trong phân tích thuật toán, có thể giải thích trực quan bằng phản chứng.

**Lập luận:**

Giả sử tồn tại một thuật toán luôn tìm được phần tử lớn nhất với ít hơn `n - 1` phép so sánh. Mỗi phép so sánh giữa hai phần tử `a` và `b` chỉ loại bỏ được tối đa **một ứng viên** khỏi khả năng là lớn nhất (phần tử nhỏ hơn trong cặp so sánh).

Ban đầu có `n` ứng viên. Để xác định chắc chắn một phần tử là lớn nhất, thuật toán phải loại bỏ `n - 1` ứng viên còn lại. Nếu thực hiện ít hơn `n - 1` phép so sánh, vẫn còn ít nhất hai ứng viên chưa từng bị loại; khi đó thuật toán chưa đủ thông tin để khẳng định chắc chắn phần tử nào lớn nhất trong mọi trường hợp.

Điều này mâu thuẫn với giả sử rằng thuật toán luôn cho kết quả đúng. Vậy trong trường hợp xấu nhất, cần ít nhất `n - 1` phép so sánh. ∎

### Liên hệ với khoa học máy tính

Nhiều chứng minh cận dưới (lower bound) mang tinh thần phản chứng tương tự: giả sử tồn tại thuật toán chạy nhanh hơn giới hạn đặt ra, sau đó chỉ ra lượng thông tin thu được là không đủ để phân biệt hết các trường hợp đầu vào.

## Ứng dụng trong Khoa học Máy tính

Khi áp dụng lập luận toán học vào lập trình và hệ thống, cần chú ý rõ những yếu tố nào được đưa vào mô hình và những yếu tố nào đã được lược bỏ. Phản chứng xuất hiện thường xuyên trong nhiều lĩnh vực của khoa học máy tính:

### Chứng minh không tồn tại thuật toán tổng quát

Ví dụ tiêu biểu là Bài toán dừng (Halting Problem). Các chứng minh dạng này cho thấy tồn tại những giới hạn bản chất về mặt tính toán, không thể khắc phục chỉ bằng cách cải tiến kỹ thuật lập trình.

### Chứng minh trạng thái hệ thống là bất khả thi

Trong hệ điều hành, cơ sở dữ liệu, hệ phân tán hoặc cấu trúc dữ liệu, các hệ thống đều duy trì những bất biến nhất định. Chẳng hạn, không thể xảy ra tình huống:

- Một khóa (lock) vừa ở trạng thái khóa vừa ở trạng thái mở.
- Một giao dịch (transaction) vừa đã xác nhận (committed) vừa đã hủy bỏ (aborted).
- Một nút vừa thuộc cây vừa không nối với cây.

Nếu giả sử trạng thái bất thường đó xảy ra và suy ra mâu thuẫn với bất biến đã định nghĩa, ta kết luận trạng thái ấy là bất khả thi.

### Chứng minh tính đúng đắn của thuật toán

Một mẫu lập luận phổ biến là giả sử thuật toán kết thúc nhưng trả về kết quả sai, từ đó suy ra tồn tại một đối tượng vi phạm điều kiện mà thuật toán phải xử lý, dẫn đến mâu thuẫn với chính cơ chế hoạt động của thuật toán.

### Chứng minh cận dưới về độ phức tạp

Ta giả sử có một thuật toán thực hiện ít thao tác hơn mức cận dưới, rồi chỉ ra với lượng thông tin hạn chế như vậy, thuật toán không thể phân biệt đúng mọi trường hợp đầu vào.

### Chứng minh tính không thể đồng thời thỏa mãn nhiều yêu cầu

Trong thiết kế hệ thống, có những bộ yêu cầu tưởng chừng hợp lý nhưng không thể cùng đạt được trong mọi bối cảnh. Ta giả sử có một hệ thống thỏa mãn đồng thời tất cả các yêu cầu đó, rồi chỉ ra một tình huống khiến hai yêu cầu buộc hệ thống hành xử trái ngược nhau, dẫn đến mâu thuẫn.

Ở mức nhập môn, điểm cần nắm là phản chứng là công cụ quan trọng để lập luận về **tính bất khả thi (impossibility)**, **bất biến (invariant)** và **cận dưới (lower bound)**.

![Cây quyết định](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="3.10">Cây quyết định — các nhánh không khả thi trong thiết kế hệ thống thường được loại trừ bằng chứng minh phản chứng.</p>
## Cách nhận diện mâu thuẫn

Mâu thuẫn không phải lúc nào cũng xuất hiện dưới dạng tường minh `Q` và `¬Q`. Dưới đây là năm dạng thường gặp:

### Dạng 1: Trái với định nghĩa

Ví dụ: một số nguyên tố có nhiều hơn hai ước dương; một cây lại chứa chu trình; một hàng đợi ở trạng thái rỗng nhưng vẫn có phần tử đầu.

### Dạng 2: Trái với giả thiết ban đầu

Ví dụ: ban đầu giả sử `gcd(a, b) = 1`, sau đó suy ra cả `a` và `b` cùng chẵn.

### Dạng 3: Trái với định lý đã biết

Ví dụ: suy ra chỉ có hữu hạn số nguyên tố, mâu thuẫn với định lý về sự vô hạn của tập số nguyên tố.

### Dạng 4: Một đối tượng phải đồng thời thỏa hai điều loại trừ nhau

Ví dụ: chương trình `D(D)` vừa phải dừng vừa phải không dừng; một biến vừa bằng `null` vừa khác `null`.

### Dạng 5: Trái với tính cực trị hoặc tối giản

Ví dụ: giả sử phân số đã ở dạng tối giản, nhưng sau đó chứng minh tử số và mẫu số vẫn còn ước chung lớn hơn `1`.

## So sánh với chứng minh trực tiếp

### Chứng minh trực tiếp

Ta đi thẳng từ giả thiết đến kết luận. Cách này tự nhiên, dễ theo dõi và cho thấy rõ cơ chế tạo ra kết luận.

### Chứng minh phản chứng

Ta giả sử kết luận sai rồi dẫn đến mâu thuẫn. Cách này phù hợp khi kết luận mang tính phủ định, khi hướng trực tiếp khó triển khai hoặc khi cần chứng minh tính bất khả thi.

### Ghi chú khi lựa chọn phương pháp

Nếu bài toán có một chứng minh trực tiếp ngắn gọn và rõ ràng, nên ưu tiên trình bày theo hướng trực tiếp. Chứng minh phản chứng đặc biệt phát huy tác dụng khi hướng trực tiếp gặp bế tắc.

## Những lỗi thường gặp

### Phủ định sai mệnh đề cần chứng minh

Để phản chứng đúng, trước hết phải viết chính xác phủ định `¬P`. Ví dụ, phủ định của mệnh đề "mọi phần tử đều có tính chất T" là "tồn tại ít nhất một phần tử không có tính chất T", chứ không phải "mọi phần tử đều không có tính chất T".

### Giả sử ngược lại nhưng bỏ sót dữ kiện

Người viết đôi khi đặt giả sử phản chứng rồi suy luận cảm tính, quên khai thác các giả thiết ban đầu của bài toán.

### Kết thúc mà không chỉ rõ mâu thuẫn

Không nên kết luận chung chung kiểu "điều này vô lý". Cần chỉ ra cụ thể mâu thuẫn xảy ra với định nghĩa nào, giả thiết nào hoặc định lý nào.

### Dùng ví dụ riêng thay cho chứng minh tổng quát

Trong chứng minh phản chứng, ví dụ cụ thể chỉ có vai trò minh họa trực giác, không thay thế cho lập luận tổng quát.

### Nhầm phản chứng với phản đảo (contrapositive)

Hai kỹ thuật này có liên hệ nhưng khác nhau về cấu trúc:

- **Phản chứng**: giả sử kết luận sai (kết hợp với giả thiết) rồi dẫn đến một mâu thuẫn bất kỳ.
- **Phản đảo** (proof by contrapositive): để chứng minh `P → Q`, ta chứng minh trực tiếp mệnh đề tương đương `¬Q → ¬P`.

### Kết luận mạnh hơn điều đã chứng minh

Đặc biệt trong các ví dụ khoa học máy tính, cần phát biểu đúng phạm vi đã chứng minh. Với Bài toán dừng, phát biểu đúng là "không tồn tại bộ quyết định tổng quát luôn đúng cho mọi chương trình và mọi đầu vào", không nên diễn đạt quá mức thành "con người không thể biết một chương trình có dừng hay không".

### Mâu thuẫn phát sinh do tính toán sai

Nếu mâu thuẫn xuất hiện do biến đổi đại số hoặc suy luận sai, thì đó là lỗi kỹ thuật chứ không phải một chứng minh phản chứng hợp lệ.

## Mẹo viết lời giải rõ ràng

1. Mở đầu rõ ràng bằng câu "Giả sử ngược lại rằng ...".
2. Nêu chính xác phủ định của kết luận.
3. Đảm bảo mỗi bước suy luận đều có lý do cụ thể.
4. Ở cuối bài, chỉ rõ mâu thuẫn nằm ở đâu.
5. Kết thúc bằng câu khẳng định: "Vậy giả sử phản chứng là sai, do đó mệnh đề ban đầu đúng."

## Bài tập luyện tập

### Bài 1

Chứng minh bằng phản chứng rằng không tồn tại số hữu tỷ `r` sao cho `r² = 3`.

**Gợi ý:** Làm tương tự ví dụ `√2`, thay `2` bằng `3`.

### Bài 2

Chứng minh rằng không tồn tại số nguyên tố lớn hơn mọi số nguyên tố khác.

**Gợi ý:** Diễn đạt lại phát biểu dưới dạng "tồn tại số nguyên tố lớn nhất", rồi dùng kết quả "có vô hạn số nguyên tố".

### Bài 3

Cho một ngăn xếp (stack) thỏa mãn các bất biến:

- Khi `top = null` thì số phần tử bằng `0`.
- Khi số phần tử bằng `0` thì không có nút nào thuộc stack.

Hãy dùng phản chứng để giải thích vì sao trạng thái "số phần tử bằng `0` nhưng `top` vẫn trỏ tới một nút hợp lệ" là bất khả thi.

### Bài 4

Giả sử có một thuật toán khẳng định luôn tìm được phần tử nhỏ nhất của mảng gồm `n` phần tử với ít hơn `n - 1` phép so sánh trong mọi trường hợp. Hãy dùng ý tưởng phản chứng để giải thích vì sao điều này không thể đúng.

### Bài 5

Phân tích phát biểu sau và viết phủ định chính xác của nó:

> "Mọi đồ thị liên thông trong lớp đang xét đều có ít nhất một đỉnh bậc lẻ."

Sau đó, xác định giả sử phản chứng cần đặt nếu muốn chứng minh phát biểu này bằng phản chứng.

### Bài 6

Viết lại chứng minh về Bài toán dừng (Halting Problem) trong khoảng 8–12 dòng, đảm bảo không diễn đạt quá phạm vi định lý và thể hiện rõ mâu thuẫn tại `D(D)`.

### Bài 7

Cho mệnh đề:

> "Không thể tồn tại một trạng thái của hệ thống mà giao dịch (transaction) vừa ở trạng thái committed vừa ở trạng thái aborted."

Hãy viết một lập luận phản chứng ngắn dựa trên định nghĩa của hai trạng thái này.

## Tiêu chí chứng minh hợp lệ

Một chứng minh phản chứng hợp lệ cần đáp ứng các yêu cầu sau:

- Phủ định của kết luận được viết chính xác.
- Mâu thuẫn cuối cùng được chỉ rõ là trái với giả thiết, định nghĩa hay định lý nào.
- Mỗi bước suy luận chỉ sử dụng giả thiết đã cho và các kết quả trung gian đã được thiết lập.
- Không nhảy bước giữa giả thiết và mâu thuẫn.
- Kết luận quay về đúng mệnh đề ban đầu cần chứng minh.

---

## Xem thêm / Video gợi ý

- [How to Write a Proof](https://www.youtube.com/watch?v=7jZ5n8k0p0Q) — 3Blue1Brown (Essence of mathematics)
- [Direct Proof, Contradiction, Induction](https://www.youtube.com/watch?v=6l7L9v0p0Q) — MIT OCW (Gilbert Strang style clarity)


## Tóm tắt

- **Chứng minh phản chứng**: giả sử $$\neg P$$ đúng → suy ra mâu thuẫn → kết luận $$P$$ đúng.
- Đặc biệt hữu ích cho mệnh đề phủ định, chứng minh tính bất khả thi và chứng minh cận dưới độ phức tạp.
- Cần viết chính xác phủ định của kết luận và chỉ rõ mâu thuẫn cụ thể ở bước cuối.
- Phân biệt với chứng minh phản đảo (contrapositive): chứng minh $$\neg Q \to \neg P$$ để suy ra $$P \to Q$$.
- Các ví dụ kinh điển: $$\sqrt{2}$$ là số vô tỷ, có vô hạn số nguyên tố và Bài toán dừng (Halting Problem).

Trong bài tiếp theo, chúng ta sẽ học **quy nạp toán học** — phương pháp chứng minh cho các mệnh đề phụ thuộc vào số tự nhiên.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=sRDwsfNDXak">PROOF by CONTRADICTION - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu cách giả sử phủ định rồi dẫn tới mâu thuẫn.
- <a href="https://www.youtube.com/watch?v=huGWXh4l1M0">Proof by Contradiction | Method &amp; First Example</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày khuôn mẫu chứng minh phản chứng và ví dụ mở đầu.
- <a href="https://www.youtube.com/watch?v=inUkhh8-h-I">Proof: There are infinitely many primes numbers</a> — Dr. Trefor Bazett, tiếng Anh. Chứng minh có vô hạn số nguyên tố, mẫu phản chứng kinh điển.
