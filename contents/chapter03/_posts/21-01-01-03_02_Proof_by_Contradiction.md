---
layout: post
title: "Chứng minh Phản chứng"
categories: chapter03
date: 2021-01-01
order: 2
required: true
lang: en
---

# Chứng minh Phản chứng

Có những mệnh đề rất khó đi thẳng từ giả thiết đến kết luận. Nhưng nếu giả sử điều ngược lại và hệ quả dẫn đến mâu thuẫn, ta biết ngay giả sử đó không thể đúng. Đây là kiểu tư duy xuất hiện không chỉ trong toán, mà cả trong debug và kiểm thử hệ thống.


Trong chứng minh, mục tiêu không chỉ là đi đến kết luận đúng mà còn cho thấy vì sao từng bước đều hợp lệ, giống như khi ta giải thích tính đúng đắn của một thuật toán.
Khi một chương trình được cho là không thể rơi vào trạng thái lỗi nào đó, ta thường thử dựng tình huống phản lại. Nếu giả định ấy kéo theo điều vô lý, vi phạm ràng buộc hoặc tự mâu thuẫn với dữ liệu ban đầu, ta đã có một lập luận mạnh. **Chứng minh phản chứng** vận hành đúng theo tinh thần đó.

Kỹ thuật này đặc biệt hữu ích với các mệnh đề phủ định, mệnh đề tồn tại duy nhất, hoặc những kết luận mà đường đi trực tiếp quá dài. Nó không thay thế chứng minh trực tiếp, nhưng mở thêm một lối vào khi bài toán tưởng như bế tắc.

Trong bài học này, chúng ta sẽ học cách đặt giả thiết phủ định đúng chỗ, lần theo hệ quả của nó, và nhận ra đâu là mâu thuẫn đủ để kết thúc chứng minh.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau khi học xong bài này, sinh viên có thể:

1. Phát biểu đúng ý tưởng của chứng minh phản chứng.
2. Phân biệt được **giả sử phản chứng** với **giả thiết ban đầu** của bài toán.
3. Nhận diện được mâu thuẫn (contradiction) dưới nhiều dạng khác nhau.
4. Viết được một chứng minh phản chứng chặt chẽ, không nhảy bước.
5. Áp dụng phương pháp này vào các ví dụ toán học cổ điển và các bối cảnh khoa học máy tính.
6. Tránh các lỗi thường gặp khi sử dụng phản chứng.

## Ý tưởng cốt lõi (4 bước trực quan)

Muốn chứng minh mệnh đề `P` đúng, ta làm như sau:

#### Minh họa trực quan: Chứng minh phản chứng như "phản chứng giả định"

```
Giả sử ¬P đúng
        ↓
Dẫn đến mâu thuẫn
        ↓
Vậy ¬P phải sai
        ↓
Kết luận: P đúng
```

**4 bước**:

1. **Giả sử ngược lại** rằng `P` là sai, tức là `¬P` đúng.
2. Từ giả sử đó, kết hợp với các sự kiện đã biết, ta suy ra một điều vô lý.
3. Vì điều vô lý không thể xảy ra, nên giả sử `¬P` phải sai.
4. Do đó, `P` phải đúng.

Nói ngắn gọn:

> Nếu giả sử "`P` sai" dẫn đến mâu thuẫn, thì `P` phải đúng.

## Vì sao phản chứng hoạt động? (why contradiction works)

Đây là phần rất quan trọng về mặt trực giác.

Nhiều sinh viên lúc đầu cảm thấy phản chứng hơi "ảo": tại sao chỉ vì giả sử ngược lại dẫn đến vô lý mà ta được quyền kết luận điều ban đầu đúng? Câu trả lời nằm ở nguyên lý logic rất cơ bản:

- Với một mệnh đề `P`, chỉ có hai khả năng: `P` đúng hoặc `P` sai.
- Nếu ta kiểm tra khả năng "`P` sai" và thấy khả năng này **không thể tồn tại**, thì chỉ còn lại khả năng "`P` đúng".

Ta có thể hình dung như sau:

- Bạn đứng trước hai cánh cửa: một cửa là `P`, cửa còn lại là `¬P`.
- Nếu bạn chứng minh được cửa `¬P` dẫn đến hố sâu logic, thì không còn đường nào khác ngoài cửa `P`.

### Trực giác đời thường

Giả sử ai đó nói: "Thiết bị này không thể cùng lúc vừa **tắt nguồn hoàn toàn** vừa **đang gửi dữ liệu qua mạng**."

Nếu muốn kiểm tra phát biểu này, ta có thể giả sử điều ngược lại xảy ra:

- thiết bị đang tắt nguồn hoàn toàn,
- nhưng đồng thời vẫn đang thực hiện truyền dữ liệu.

Hai trạng thái này mâu thuẫn với chính định nghĩa của "tắt nguồn hoàn toàn". Vì vậy, giả sử đó không thể đúng.

Phản chứng hoạt động chính xác theo kiểu như vậy: ta kiểm tra xem thế giới có thể tồn tại dưới giả sử phủ định hay không. Nếu không thể, kết luận ban đầu được xác nhận.

### Cơ sở logic ngắn gọn

Về mặt logic hình thức:

- Nếu `¬P → (Q ∧ ¬Q)`
- thì `¬P` không thể đúng
- nên `P` phải đúng.

Trong đó, `(Q ∧ ¬Q)` là một mâu thuẫn rõ ràng: một mệnh đề vừa đúng vừa sai cùng lúc.

## Khi nào nên nghĩ đến phản chứng?

Phản chứng đặc biệt hữu ích khi:

### 1. Kết luận mang tính phủ định

Ví dụ:

- Không tồn tại thuật toán như vậy.
- Không có số nguyên lớn nhất thỏa mãn tính chất đó.
- Không thể xây dựng cấu hình như mô tả.

### 2. Kết luận là một mệnh đề "khó đi thẳng"

Có những bài toán mà từ giả thiết đến kết luận không có lộ trình trực tiếp rõ ràng. Nhưng nếu giả sử điều ngược lại, cấu trúc của bài toán lại "lộ ra" rất nhanh.

### 3. Ta muốn chỉ ra sự bất khả thi (impossibility)

Trong khoa học máy tính, rất nhiều phát biểu quan trọng có dạng này:

- không thể quyết định bài toán đó trong mọi trường hợp,
- không thể có cấu trúc dữ liệu thỏa mọi yêu cầu cùng lúc,
- không thể có lời giải nhanh hơn giới hạn nào đó nếu giả thiết kia đúng.

### 4. Mâu thuẫn có thể khai thác từ định nghĩa

Đôi khi chỉ cần bám đúng định nghĩa là đã có mâu thuẫn.

Ví dụ:

- một số vừa chẵn vừa lẻ,
- một phần tử vừa thuộc tập vừa không thuộc tập,
- một trạng thái hệ thống vừa "reachable" vừa "unreachable".

## Quy trình viết chứng minh phản chứng

Một khuôn mẫu an toàn là:

1. **Nêu rõ điều cần chứng minh.**
2. **Giả sử phản chứng**: viết chính xác phủ định của kết luận.
3. **Suy luận từng bước** từ giả sử phản chứng cùng với dữ kiện đã biết.
4. **Chỉ rõ mâu thuẫn** nằm ở đâu.
5. **Kết luận** giả sử phản chứng sai, nên mệnh đề ban đầu đúng.

### Mẫu trình bày

> Ta cần chứng minh `P`.
>
> Giả sử ngược lại rằng `¬P` đúng.
>
> Từ giả sử này, suy ra ...
>
> Nhưng điều đó mâu thuẫn với ...
>
> Vậy giả sử `¬P` là sai. Do đó `P` đúng. ∎

## Ví dụ 1: Chứng minh √2 là số vô tỷ

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Đây là ví dụ kinh điển nhất, vì nó cho thấy phản chứng có thể biến một phát biểu trông rất khó thành một chuỗi suy luận ngắn và sắc bén.

**Định lý:** `√2` là số vô tỷ (irrational number).

**Chứng minh:**

Giả sử phản chứng rằng `√2` là số hữu tỷ. Khi đó tồn tại các số nguyên `a, b` sao cho:

- `b ≠ 0`,
- `gcd(a, b) = 1`,
- và `√2 = a / b`.

Bình phương hai vế, ta được:

`2 = a² / b²`, hay `a² = 2b²`.

Từ đây suy ra `a²` là số chẵn, nên `a` cũng phải là số chẵn. Do đó tồn tại số nguyên `k` sao cho `a = 2k`.

Thế vào phương trình `a² = 2b²`:

`(2k)² = 2b²`

`4k² = 2b²`

`b² = 2k²`.

Vậy `b²` là số chẵn, suy ra `b` cũng là số chẵn.

Như vậy, cả `a` và `b` đều chẵn. Điều này mâu thuẫn với điều kiện `gcd(a, b) = 1`, vì nếu cả hai cùng chẵn thì chúng có ước chung ít nhất là `2`.

Vậy giả sử `√2` là số hữu tỷ là sai. Do đó `√2` là số vô tỷ. ∎

### Điều đáng học từ ví dụ này

Mâu thuẫn không xuất hiện ngay lập tức. Nó được tạo ra bằng cách:

- giả sử tồn tại biểu diễn tối giản,
- rồi chứng minh biểu diễn đó thực ra chưa tối giản.

Đây là mẫu lập luận xuất hiện nhiều trong toán rời rạc và thuật toán: giả sử một cấu trúc "đã tối ưu", sau đó suy ra nó vẫn còn rút gọn được, dẫn đến vô lý.

## Ví dụ 2: Có vô hạn số nguyên tố

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Định lý:** Có vô hạn số nguyên tố.

**Chứng minh:**

Giả sử phản chứng rằng chỉ có hữu hạn số nguyên tố. Gọi tất cả các số nguyên tố đó là:

`p₁, p₂, ..., pₙ`.

Xét số:

`N = p₁p₂...pₙ + 1`.

Ta biết `N > 1`, nên `N` phải có ít nhất một ước nguyên tố.

Gọi `p` là một ước nguyên tố của `N`. Vì theo giả sử, mọi số nguyên tố đều nằm trong danh sách `p₁, p₂, ..., pₙ`, nên `p` phải là một trong các số đó.

Khi đó `p` chia hết cho tích `p₁p₂...pₙ`, nên `p` cũng chia hết cho:

`N - p₁p₂...pₙ = 1`.

Nhưng không có số nguyên tố nào chia hết cho `1`. Mâu thuẫn.

Vậy giả sử chỉ có hữu hạn số nguyên tố là sai. Do đó có vô hạn số nguyên tố. ∎

### Ý nghĩa sư phạm

Ví dụ này rất đẹp vì mâu thuẫn đến từ việc **tự xây một đối tượng phá vỡ giả sử**. Trong khoa học máy tính, đây cũng là một chiến lược quen thuộc:

- giả sử đã liệt kê hết mọi trường hợp,
- rồi xây một trường hợp mới không thuộc danh sách đó.

## Ví dụ 3: Không tồn tại số nguyên tố lớn nhất

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Ví dụ này giúp sinh viên thấy phản chứng không chỉ dùng cho số vô tỷ hay số nguyên tố, mà còn rất hợp với lập luận "cực tiểu" (minimal counterexample intuition).

**Mệnh đề:** Không tồn tại số nguyên tố lớn nhất.

**Chứng minh bằng phản chứng:**

Giả sử tồn tại số nguyên tố lớn nhất, gọi là `p`.

Theo Ví dụ 2, nếu có số nguyên tố lớn nhất thì số lượng số nguyên tố phải là hữu hạn. Nhưng điều đó mâu thuẫn với định lý "có vô hạn số nguyên tố".

Vậy không tồn tại số nguyên tố lớn nhất. ∎

### Bài học ở đây

Không phải lúc nào phản chứng cũng phải triển khai từ đầu. Đôi khi ta có thể dùng một định lý đã chứng minh trước đó để tạo mâu thuẫn nhanh gọn.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter03/contradiction_flow.svg" alt="Sơ đồ chứng minh phản chứng: giả sử ngược lại → suy luận → mâu thuẫn → kết luận" width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 3.2: Luồng của chứng minh phản chứng — giả sử điều ngược lại, suy luận đến mâu thuẫn, kết luận điều ban đầu đúng</figcaption>
</p>
</figure>

## Ví dụ 4: Trực giác về Bài toán dừng (Halting Problem)

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Đây là ví dụ khoa học máy tính rất nổi tiếng. Ở đây ta chỉ trình bày **trực giác chính xác về mặt khái niệm**, không đi quá sâu vào logic hình thức.

**Phát biểu:** Không tồn tại một thuật toán tổng quát quyết định đúng cho mọi chương trình `P` và input `I` rằng `P(I)` có dừng hay không.

**Ý tưởng phản chứng:**

Giả sử tồn tại một bộ quyết định hoàn hảo `H(P, I)` với đầu ra:

- `YES` nếu chương trình `P` dừng trên input `I`,
- `NO` nếu chương trình `P` không dừng trên input `I`.

Ta xây dựng một chương trình mới `D(X)` như sau:

```text
if H(X, X) == YES:
    loop forever
else:
    halt immediately
```

Bây giờ xét `D(D)`.

Có hai khả năng:

1. Nếu `H(D, D) = YES`, thì theo định nghĩa của `D`, chương trình `D(D)` sẽ lặp vô hạn.
2. Nếu `H(D, D) = NO`, thì theo định nghĩa của `D`, chương trình `D(D)` sẽ dừng ngay.

Trong cả hai trường hợp, `H` đều dự đoán sai về `D(D)`.

Mâu thuẫn xuất hiện vì ta đã giả sử `H` là bộ quyết định đúng cho **mọi** chương trình và **mọi** input.

Vậy không tồn tại thuật toán tổng quát như vậy. ∎

### Điều cần hiểu đúng

Ví dụ này **không nói** rằng ta không thể phân tích bất kỳ chương trình cụ thể nào.

Nó chỉ nói rằng:

> Không có một thuật toán duy nhất, tổng quát, luôn luôn đúng cho mọi chương trình và mọi input.

Đây là một điểm rất quan trọng để tránh overclaim.

## Ví dụ 5: Trạng thái bất khả thi trong thiết kế hệ thống

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Phản chứng không chỉ sống trong toán thuần túy. Trong thiết kế hệ thống (system design), ta thường dùng nó để chứng minh một trạng thái nào đó là **không thể xảy ra** nếu các bất biến (invariants) được giữ đúng.

**Bối cảnh:** Xét một hàng đợi (queue) với hai bất biến:

1. `size` luôn bằng số phần tử thực sự đang có trong cấu trúc dữ liệu.
2. Khi `size = 0` thì con trỏ `front = null`.

**Mệnh đề:** Không thể có trạng thái mà `size = 0` nhưng `front` lại trỏ đến một node hợp lệ, nếu hai bất biến trên luôn được duy trì đúng sau mỗi thao tác.

**Lập luận phản chứng:**

Giả sử tồn tại một thời điểm mà:

- `size = 0`,
- nhưng `front ≠ null`.

Theo bất biến thứ hai, khi `size = 0` thì bắt buộc `front = null`.

Vậy ta nhận được:

- `front = null`,
- và đồng thời `front ≠ null`.

Đó là mâu thuẫn.

Do đó, nếu các bất biến thực sự được duy trì đúng, trạng thái trên là bất khả thi. ∎

### Vì sao ví dụ này quan trọng?

Trong kiểm chứng chương trình (program verification), lập luận kiểu này được dùng để:

- phát hiện bug,
- chứng minh tính đúng đắn của cấu trúc dữ liệu,
- chỉ ra rằng một nhánh xử lý "không bao giờ xảy ra".

## Ví dụ 6: Trực giác phản chứng trong cận độ phức tạp

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Ta xét một ví dụ ở mức trực giác, phù hợp với sinh viên mới học.

**Phát biểu:** Bất kỳ thuật toán tìm phần tử lớn nhất trong một mảng chưa sắp xếp gồm `n` phần tử đều cần ít nhất `n - 1` phép so sánh trong trường hợp xấu nhất.

Đây là một định lý chuẩn trong phân tích thuật toán. Ta dùng phản chứng để hiểu trực giác.

**Lập luận:**

Giả sử tồn tại một thuật toán có thể luôn tìm ra phần tử lớn nhất với ít hơn `n - 1` phép so sánh.

Mỗi phép so sánh chỉ có thể loại bỏ tối đa **một ứng viên** khỏi khả năng là lớn nhất, vì khi so sánh `a` với `b`, ta chỉ biết phần tử nhỏ hơn không thể là lớn nhất.

Ban đầu có `n` ứng viên. Muốn xác định chắc chắn một phần tử là lớn nhất, ta phải loại `n - 1` ứng viên còn lại.

Nếu dùng ít hơn `n - 1` phép so sánh, sẽ còn ít nhất hai ứng viên chưa từng bị loại hoàn toàn theo thông tin hiện có. Khi đó thuật toán chưa có đủ cơ sở để khẳng định phần tử nào lớn nhất trong mọi trường hợp.

Mâu thuẫn với giả sử rằng thuật toán luôn đúng.

Vậy trong trường hợp xấu nhất, cần ít nhất `n - 1` phép so sánh. ∎

### Liên hệ với khoa học máy tính

Nhiều chứng minh lower bound (cận dưới) có tinh thần phản chứng như trên:

- giả sử thuật toán "quá nhanh",
- sau đó chỉ ra rằng lượng thông tin nó thu được là chưa đủ để quyết định đúng trong mọi trường hợp.

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Phản chứng xuất hiện tự nhiên trong rất nhiều nhánh của khoa học máy tính.

### 1. Chứng minh không tồn tại thuật toán tổng quát

Ví dụ tiêu biểu là Halting Problem. Các lập luận kiểu này giúp ta hiểu rằng có những giới hạn mang tính bản chất, không phải do "chưa đủ thông minh để lập trình".

### 2. Chứng minh trạng thái hệ thống là bất khả thi

Trong hệ điều hành, cơ sở dữ liệu, hệ phân tán, hoặc cấu trúc dữ liệu, ta thường có các bất biến:

- một khóa vừa ở trạng thái khóa vừa ở trạng thái mở,
- một transaction vừa committed vừa aborted,
- một node vừa trong cây vừa không nối với cây.

Nếu giả sử trạng thái đó xảy ra và nó mâu thuẫn với các bất biến đã định nghĩa, ta kết luận trạng thái ấy là bất khả thi.

### 3. Chứng minh tính đúng đắn của thuật toán

Một mẫu rất thường gặp:

- giả sử thuật toán kết thúc nhưng kết quả sai,
- từ đó suy ra tồn tại một đối tượng vi phạm điều kiện mà thuật toán đáng lẽ đã xử lý,
- mâu thuẫn với chính cơ chế hoạt động của thuật toán.

### 4. Chứng minh cận dưới về độ phức tạp

Ta giả sử có thuật toán nhanh hơn mức có thể, rồi chỉ ra rằng với lượng thông tin ít như vậy, không thể phân biệt hết các trường hợp cần thiết.

### 5. Chứng minh tính không thể đồng thời thỏa mãn nhiều yêu cầu

Trong thiết kế hệ thống thực tế, đôi khi ba yêu cầu tưởng như hợp lý nhưng không thể đồng thời đạt được trong mọi bối cảnh. Một cách tiếp cận là:

- giả sử có hệ thống thỏa cả ba,
- suy ra một tình huống mà hai yêu cầu ép hệ thống đi theo hai hướng đối lập,
- xuất hiện mâu thuẫn.

Ở mức nhập môn, sinh viên chỉ cần nhớ rằng phản chứng là công cụ rất mạnh để lập luận về **impossibility**, **invariant**, và **lower bound**.

## Cách nhận diện mâu thuẫn

Không phải mâu thuẫn lúc nào cũng có dạng hiển nhiên như `Q` và `¬Q`. Dưới đây là vài dạng thường gặp:

### Dạng 1: Trái với định nghĩa

Ví dụ:

- một số nguyên tố lại có nhiều hơn hai ước dương,
- một cây (tree) lại chứa chu trình,
- một trạng thái "empty" nhưng vẫn có phần tử đầu.

### Dạng 2: Trái với giả thiết ban đầu

Ví dụ:

- ban đầu giả sử `gcd(a, b) = 1`, sau đó suy ra cả `a` và `b` cùng chẵn.

### Dạng 3: Trái với định lý đã biết

Ví dụ:

- suy ra tồn tại số nguyên tố lớn nhất, mâu thuẫn với định lý vô hạn số nguyên tố.

### Dạng 4: Một đối tượng phải đồng thời thỏa hai điều không thể cùng đúng

Ví dụ:

- chương trình `D(D)` vừa phải dừng vừa phải không dừng,
- một biến vừa `null` vừa khác `null`.

### Dạng 5: Trái với cực trị hoặc tối ưu

Ví dụ:

- giả sử đã có biểu diễn tối giản nhất, rồi suy ra vẫn còn rút gọn được.

## So sánh với chứng minh trực tiếp

### Chứng minh trực tiếp

Ta đi từ giả thiết đến kết luận.

Ưu điểm:

- tự nhiên,
- thường dễ đọc,
- giúp thấy rõ cơ chế tạo ra kết luận.

### Chứng minh phản chứng

Ta giả sử kết luận sai rồi đi đến vô lý.

Ưu điểm:

- mạnh khi kết luận là phủ định,
- hữu ích khi chứng minh trực tiếp bị "bí đường",
- rất hợp với các bài toán bất khả thi.

### Ghi chú quan trọng

Nếu có một chứng minh trực tiếp ngắn, sáng, dễ hiểu thì thường nên ưu tiên chứng minh trực tiếp trong lần trình bày đầu tiên. Tuy nhiên, phản chứng thường là công cụ cứu nguy khi hướng trực tiếp không hiệu quả.

## Những lỗi thường gặp (common pitfalls)

Đây là phần cực kỳ quan trọng đối với người mới học.

### 1. Phủ định sai mệnh đề cần chứng minh

Muốn phản chứng tốt, trước tiên phải viết đúng `¬P`.

Ví dụ:

- Phủ định của "mọi phần tử đều có tính chất T" là "tồn tại ít nhất một phần tử không có tính chất T".
- Không phải là "mọi phần tử đều không có tính chất T".

### 2. Giả sử điều ngược lại nhưng không dùng hết dữ kiện

Sinh viên đôi khi viết "Giả sử phản chứng ..." rồi suy luận bằng cảm tính, bỏ quên các giả thiết thật sự của bài toán.

### 3. Kết thúc mà không chỉ ra mâu thuẫn cụ thể

Không nên viết mơ hồ kiểu "điều này vô lý" mà không nói rõ vô lý ở đâu.

Hãy chỉ ra chính xác:

- mâu thuẫn với định nghĩa nào,
- mâu thuẫn với giả thiết nào,
- hay mâu thuẫn với định lý nào.

### 4. Dùng ví dụ riêng để thay cho chứng minh tổng quát

Trong phản chứng, ví dụ chỉ giúp minh họa trực giác. Nó không thay thế được lập luận tổng quát.

### 5. Nhầm phản chứng với phản đảo (contrapositive)

Hai kỹ thuật này liên quan nhưng không giống nhau.

- **Phản chứng**: giả sử kết luận sai rồi đi đến mâu thuẫn.
- **Phản đảo** (proof by contrapositive): để chứng minh `P → Q`, ta chứng minh `¬Q → ¬P`.

### 6. Kết luận mạnh hơn điều đã chứng minh

Đặc biệt trong ví dụ khoa học máy tính, cần tránh phát biểu quá mức.

Ví dụ với Halting Problem:

- đúng: "không tồn tại bộ quyết định tổng quát luôn đúng cho mọi chương trình và mọi input",
- không nên nói quá: "con người không thể biết chương trình có dừng hay không".

### 7. Mâu thuẫn do tính toán sai chứ không phải do logic

Nếu mâu thuẫn xuất hiện vì bạn biến đổi đại số sai, thì đó không phải là thành công của phản chứng mà là lỗi kỹ thuật.

## Mẹo viết lời giải rõ ràng

1. Viết nguyên câu "Giả sử ngược lại rằng ...".
2. Nêu rõ phủ định của kết luận là gì.
3. Mỗi bước suy luận nên có lý do.
4. Đến cuối, gọi tên mâu thuẫn một cách minh bạch.
5. Kết bằng câu chuẩn: "Vậy giả sử phản chứng là sai, do đó mệnh đề ban đầu đúng."

## Bài tập luyện tập

### Bài 1

Chứng minh bằng phản chứng rằng không tồn tại số hữu tỷ `r` sao cho `r² = 3`.

**Gợi ý:** Làm tương tự ví dụ `√2`, nhưng thay `2` bằng `3`.

### Bài 2

Chứng minh rằng không tồn tại số nguyên tố nhỏ nhất lớn hơn mọi số nguyên tố khác.

**Gợi ý:** Hãy diễn đạt lại phát biểu cho chuẩn, rồi dùng kết quả "có vô hạn số nguyên tố".

### Bài 3

Cho một stack với bất biến:

- khi `top = null` thì số phần tử bằng `0`,
- khi số phần tử bằng `0` thì không có node nào thuộc stack.

Hãy dùng phản chứng để giải thích vì sao trạng thái "số phần tử bằng `0` nhưng `top` vẫn trỏ tới một node hợp lệ" là bất khả thi.

### Bài 4

Giả sử có thuật toán khẳng định luôn tìm được phần tử nhỏ nhất của mảng `n` phần tử với ít hơn `n - 1` phép so sánh trong mọi trường hợp. Hãy dùng ý tưởng phản chứng để giải thích vì sao điều này không thể đúng.

### Bài 5

Phân tích phát biểu sau và viết phủ định chính xác của nó:

> "Mọi đồ thị liên thông trong lớp đang xét đều có ít nhất một đỉnh bậc lẻ."

Sau đó, thảo luận xem nếu muốn phản chứng thì bạn sẽ bắt đầu bằng giả sử nào.

### Bài 6

Viết lại chứng minh về Halting Problem ở mức ngắn gọn 8–12 dòng, sao cho không overclaim và vẫn thể hiện rõ mâu thuẫn tại `D(D)`.

### Bài 7

Cho mệnh đề:

> "Không thể tồn tại một trạng thái của hệ thống mà transaction vừa committed vừa aborted."

Hãy viết một lập luận phản chứng ngắn dựa trên định nghĩa hai trạng thái này.

## Tự kiểm tra nhanh

Trước khi nộp một lời giải phản chứng, hãy tự hỏi:

- Mình có viết đúng phủ định của kết luận không?
- Mâu thuẫn cuối cùng là mâu thuẫn với cái gì?
- Mỗi bước suy luận có dùng đúng giả thiết không?
- Có chỗ nào mình đang "nhảy cóc" không?
- Kết luận cuối đã quay về đúng mệnh đề cần chứng minh chưa?

## Tổng kết

Chứng minh phản chứng là một kỹ thuật nền tảng vì nó cho phép ta lập luận về những điều **không thể xảy ra**, **không thể tồn tại**, hoặc **không thể luôn đúng**. Sức mạnh của nó đến từ một ý tưởng rất đơn giản nhưng rất sâu:

> Nếu thế giới giả định "điều cần chứng minh là sai" tự sụp đổ vì mâu thuẫn, thì điều cần chứng minh phải đúng.

Trong toán học, phản chứng giúp xử lý những mệnh đề khó chứng minh trực tiếp. Trong khoa học máy tính, nó đặc biệt quan trọng khi nói về:

- giới hạn của thuật toán,
- tính đúng đắn của cấu trúc dữ liệu,
- trạng thái bất khả thi trong hệ thống,
- và các cận dưới về độ phức tạp.

Học tốt phản chứng không chỉ giúp bạn giải toán tốt hơn, mà còn giúp bạn **lập luận chặt chẽ hơn như một người làm khoa học máy tính**. Khi gặp một phát biểu "không thể", "không tồn tại", hoặc "luôn luôn", hãy thử tự hỏi:

> Nếu điều ngược lại đúng, mình có thể dẫn nó tới mâu thuẫn nào?

Trong bài tiếp theo, chúng ta sẽ học về **quy nạp toán học** — một phương pháp chứng minh mạnh mẽ cho các mệnh đề liên quan đến số tự nhiên.
