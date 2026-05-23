---
layout: post
title: "Quy nạp Toán học"
categories: chapter03
date: 2021-01-01
order: 3
required: true
lang: en
---

# Quy nạp Toán học

Nhiều cấu trúc trong khoa học máy tính được xây theo từng bước: dãy Fibonacci, lời gọi đệ quy, số mức của cây, hay chi phí của một thuật toán khi kích thước đầu vào tăng dần. Nếu muốn chứng minh một tính chất đúng với mọi số tự nhiên, kiểm tra vài giá trị đầu tiên là chưa đủ.


Trong chứng minh, mục tiêu không chỉ là đi đến kết luận đúng mà còn cho thấy vì sao từng bước đều hợp lệ, giống như khi ta giải thích tính đúng đắn của một thuật toán.
**Quy nạp toán học** cho ta một cách rất mạnh để xử lý kiểu bài toán đó. Ta chứng minh mệnh đề đúng ở điểm khởi đầu, rồi chỉ ra rằng nếu nó đúng ở bước hiện tại thì nó cũng đúng ở bước kế tiếp. Một khi mắt xích này khép kín, toàn bộ chuỗi phía sau được kéo theo.

Cách nghĩ này rất gần với lập trình đệ quy. Muốn tin một hàm đệ quy là đúng, ta phải tin trường hợp cơ sở đúng và bước đệ quy bảo toàn tính đúng. Vì vậy, học quy nạp không chỉ để chứng minh công thức, mà còn để hiểu sâu hơn cách xây dựng và kiểm tra lời giải đệ quy.

Trong bài này, chúng ta sẽ đi từ ý tưởng trực quan của hiệu ứng domino đến dạng phát biểu chuẩn của quy nạp, rồi áp dụng vào những mệnh đề quen thuộc trong toán rời rạc.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

1. Phát biểu đúng nguyên lý quy nạp toán học.
2. Phân biệt được **bước cơ sở** và **bước quy nạp**.
3. Viết được một chứng minh quy nạp hoàn chỉnh, chặt chẽ và dễ đọc.
4. Nhận ra khi nào nên dùng quy nạp thay vì biến đổi trực tiếp hay phản chứng.
5. Áp dụng quy nạp cho công thức, bất đẳng thức, chia hết, và các cấu trúc rời rạc.
6. Liên hệ quy nạp với đệ quy, quan hệ truy hồi, vòng lặp và cấu trúc dữ liệu trong khoa học máy tính.

## Trực giác: vì sao quy nạp hợp lý?

### Hình ảnh domino

Hãy tưởng tượng một hàng domino vô hạn được xếp ngay ngắn.

- Nếu viên đầu tiên ngã,
- và mỗi khi viên thứ $k$ ngã thì nó luôn làm viên thứ $k+1$ ngã,

thì toàn bộ dãy domino sẽ ngã.

Trong quy nạp toán học:

- mệnh đề $P(n)$ giống như trạng thái "viên domino thứ $n$ đã ngã",
- chứng minh $P(n_0)$ đúng là làm đổ **viên đầu tiên**,
- chứng minh $P(k) \Rightarrow P(k+1)$ là chứng minh **một viên kéo theo viên tiếp theo**.

Domino giúp ta nhìn ra trực giác; phần chứng minh vẫn phải viết bằng ngôn ngữ toán học chính xác.

### Trực giác thứ hai: xây dựng từng tầng

Một cách hiểu khác rất gần với khoa học máy tính là xem quy nạp như quá trình xây một đối tượng theo từng tầng:

- ta biết đối tượng nhỏ nhất hoạt động đúng,
- ta chỉ ra rằng nếu đối tượng kích thước $k$ đúng thì đối tượng kích thước $k+1$ cũng đúng.

Ví dụ:

- xâu độ dài $k+1$ được tạo từ xâu độ dài $k$ bằng cách thêm một ký tự,
- danh sách kích thước $k+1$ được tạo từ danh sách kích thước $k$ bằng cách thêm một phần tử,
- cây lớn hơn được xây từ những cây con nhỏ hơn.

Quy nạp vì thế không chỉ là một mẹo chứng minh; nó phản ánh cách nhiều cấu trúc rời rạc được hình thành.

### Trực giác thứ ba: cấu trúc đệ quy

Trong lập trình, nhiều đối tượng được định nghĩa đệ quy:

- giai thừa: $n! = n \cdot (n-1)!$
- dãy Fibonacci: $F_n = F_{n-1} + F_{n-2}$
- cây nhị phân: một cây gồm nút gốc và hai cây con trái/phải

Khi đối tượng được định nghĩa đệ quy, kỹ thuật chứng minh tự nhiên nhất thường cũng là quy nạp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter03/domino_induction.svg" alt="Hình ảnh domino minh họa quy nạp: viên đầu ngã và mỗi viên kéo theo viên tiếp" width="60%" height="60%">
  <figcaption style="text-align: center;">Hình 3.3: Domino — phép ẩn dụ kinh điển cho quy nạp: bước cơ sở (đổ viên đầu) và bước quy nạp (mỗi viên kéo theo viên kế)</figcaption>
</p>
</figure>

## Nguyên lý quy nạp toán học

Giả sử $P(n)$ là một mệnh đề phụ thuộc vào số tự nhiên $n$, và ta muốn chứng minh:

$$P(n) \text{ đúng với mọi } n \ge n_0$$

Ta thực hiện hai bước:

1. **Bước cơ sở**: Chứng minh $P(n_0)$ đúng.
2. **Bước quy nạp**: Với giả thiết $P(k)$ đúng cho một $k \ge n_0$ bất kỳ, chứng minh $P(k+1)$ cũng đúng.

Khi đó, theo nguyên lý quy nạp toán học, $P(n)$ đúng với mọi $n \ge n_0$.

### Dạng logic

$$P(n_0) \wedge \forall k \ge n_0\,[P(k) \Rightarrow P(k+1)] \Rightarrow \forall n \ge n_0\, P(n)$$

Trong bước quy nạp, câu mở đầu chuẩn thường là:

> Giả sử với một $k \ge n_0$ bất kỳ, mệnh đề $P(k)$ đúng.

Sau đó, mục tiêu là:

> Cần chứng minh $P(k+1)$ đúng.

Ta **không được** chọn một giá trị cụ thể của $k$ như $k=5$, vì bước quy nạp phải đúng với mọi $k \ge n_0$.

## Mẫu trình bày một chứng minh quy nạp

Khi viết bài, nên theo khuôn sau:

1. Nêu rõ mệnh đề $P(n)$ và miền của $n$.
2. Chứng minh bước cơ sở.
3. Viết giả thiết quy nạp: "Giả sử $P(k)$ đúng".
4. Chứng minh $P(k+1)$.
5. Kết luận theo nguyên lý quy nạp.

## Sai lầm thường gặp khi học quy nạp

1. **Quên bước cơ sở**: Không có viên domino đầu tiên thì cả chuỗi không khởi động được.
2. **Dùng giả thiết quy nạp sai chỗ**: Giả thiết quy nạp chỉ cho phép dùng $P(k)$, không cho phép tự động dùng $P(k+2)$ hay một điều mạnh hơn.
3. **Không nêu rõ mục tiêu**: Nhiều bài biến đổi dài nhưng không nói rõ đang chứng minh điều gì.
4. **Chứng minh bằng ví dụ**: Kiểm tra vài giá trị đầu không thay thế được chứng minh quy nạp.
5. **Nhầm chiều suy luận**: Cần đi từ giả thiết $P(k)$ để suy ra $P(k+1)$, không phải giả sử cả hai cùng đúng.
6. **Bỏ qua điều kiện miền giá trị**: Có bài đúng với mọi $n \ge 4$ nhưng sai với $n=1,2,3$; khi đó bước cơ sở phải bắt đầu đúng chỗ.

## Ví dụ 1: Tổng của $n$ số tự nhiên đầu tiên

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Với mọi $n \ge 1$,

$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$

**Chứng minh.**

**Bước cơ sở**: Với $n=1$,

$$1 = \frac{1(1+1)}{2} = 1$$

Mệnh đề đúng tại $n=1$.

**Bước quy nạp**: Giả sử với một $k \ge 1$ bất kỳ, ta có

$$1 + 2 + \cdots + k = \frac{k(k+1)}{2}$$

Cần chứng minh:

$$1 + 2 + \cdots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$

Thật vậy,

$$1 + 2 + \cdots + k + (k+1) = \frac{k(k+1)}{2} + (k+1)$$

$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

Suy ra mệnh đề đúng với $k+1$.

Vậy theo nguyên lý quy nạp toán học, công thức đúng với mọi $n \ge 1$. $\square$

Đây là ví dụ mẫu vì biểu thức ở $k+1$ tách thành "phần cũ" cộng "phần mới".

## Ví dụ 2: Tổng cấp số nhân

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Với mọi $n \ge 0$,

$$1 + 2 + 2^2 + \cdots + 2^n = 2^{n+1} - 1$$

**Chứng minh.**

**Bước cơ sở**: Với $n=0$,

$$1 = 2^{0+1} - 1 = 1$$

Đúng.

**Bước quy nạp**: Giả sử với một $k \ge 0$ bất kỳ,

$$1 + 2 + 2^2 + \cdots + 2^k = 2^{k+1} - 1$$

Cần chứng minh:

$$1 + 2 + 2^2 + \cdots + 2^k + 2^{k+1} = 2^{k+2} - 1$$

Ta có:

$$1 + 2 + 2^2 + \cdots + 2^k + 2^{k+1} = (2^{k+1} - 1) + 2^{k+1} = 2^{k+2} - 1$$

Vậy mệnh đề đúng với mọi $n \ge 0$. $\square$

Tổng này thường xuất hiện khi đếm số nút của cây nhị phân đầy đủ theo từng mức, hoặc khi phân tích các thuật toán tách đôi dữ liệu.

## Ví dụ 3: Tính chia hết

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Với mọi $n \ge 1$, số $7^n - 1$ chia hết cho $6$.

**Chứng minh.**

**Bước cơ sở**: Với $n=1$,

$$7^1 - 1 = 6$$

nên chia hết cho $6$.

**Bước quy nạp**: Giả sử với một $k \ge 1$ bất kỳ, $7^k - 1$ chia hết cho $6$.

Điều đó có nghĩa là tồn tại số nguyên $m$ sao cho:

$$7^k - 1 = 6m$$

Cần chứng minh $7^{k+1} - 1$ chia hết cho $6$.

Ta có:

$$7^{k+1} - 1 = 7 \cdot 7^k - 1 = 7(7^k - 1) + 6$$

Theo giả thiết quy nạp, $7^k - 1 = 6m$, do đó:

$$7^{k+1} - 1 = 7 \cdot 6m + 6 = 6(7m + 1)$$

Nên $7^{k+1} - 1$ chia hết cho $6$.

Vậy mệnh đề đúng với mọi $n \ge 1$. $\square$

Trong các bài chia hết, sau khi áp dụng giả thiết quy nạp, ta thường cố gắng đưa biểu thức về dạng:

$$d \times (\text{số nguyên})$$

với $d$ là số cần chứng minh chia hết.

## Ví dụ 4: Bất đẳng thức Bernoulli

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Với mọi $n \in \mathbb{N}$ và mọi $x \ge -1$,

$$ (1+x)^n \ge 1 + nx $$

**Chứng minh.**

**Bước cơ sở**: Với $n=0$,

$$ (1+x)^0 = 1 = 1 + 0x $$

Đúng.

**Bước quy nạp**: Giả sử với một $k \ge 0$ bất kỳ,

$$ (1+x)^k \ge 1 + kx $$

Cần chứng minh:

$$ (1+x)^{k+1} \ge 1 + (k+1)x $$

Ta có:

$$ (1+x)^{k+1} = (1+x)^k(1+x) \ge (1+kx)(1+x) $$

vì $1+x \ge 0$.

Tiếp tục biến đổi:

$$ (1+kx)(1+x) = 1 + (k+1)x + kx^2 \ge 1 + (k+1)x $$

do $kx^2 \ge 0$.

Vậy mệnh đề đúng với mọi $n \in \mathbb{N}$. $\square$

Ở bài này, điều kiện $x \ge -1$ không phải trang trí. Nó đảm bảo $1+x \ge 0$, nhờ đó khi nhân hai vế của bất đẳng thức với $(1+x)$, chiều bất đẳng thức không đổi.

## Ví dụ 5: Tổng các số lẻ đầu tiên

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Với mọi $n \ge 1$,

$$1 + 3 + 5 + \cdots + (2n-1) = n^2$$

**Chứng minh.**

**Bước cơ sở**: Với $n=1$,

$$1 = 1^2$$

Đúng.

**Bước quy nạp**: Giả sử với một $k \ge 1$ bất kỳ,

$$1 + 3 + 5 + \cdots + (2k-1) = k^2$$

Cần chứng minh:

$$1 + 3 + 5 + \cdots + (2k-1) + (2k+1) = (k+1)^2$$

Ta có:

$$1 + 3 + 5 + \cdots + (2k-1) + (2k+1) = k^2 + (2k+1) = (k+1)^2$$

Vậy mệnh đề đúng với mọi $n \ge 1$. $\square$

Mỗi khi từ hình vuông cạnh $k$ sang hình vuông cạnh $k+1$, ta chỉ cần thêm một "viền" gồm đúng $2k+1$ ô vuông. Đây là một ví dụ đẹp cho thấy quy nạp không chỉ là đại số mà còn có trực giác hình học.

## Ví dụ 6: Ứng dụng trong Khoa học Máy tính — bất biến vòng lặp

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Khi học lập trình, sinh viên thường nghe cụm từ **loop invariant** (bất biến vòng lặp). Bản chất của nó rất gần với quy nạp.

Xét thuật toán tính tổng:

```text
sum := 0
for i := 1 to n do
    sum := sum + i
```

Ta muốn chứng minh rằng sau khi kết thúc vòng lặp, `sum = 1 + 2 + \cdots + n`.

### Bất biến vòng lặp

Sau khi kết thúc lần lặp thứ $k$, ta có:

$$sum = 1 + 2 + \cdots + k$$

Đây là một mệnh đề phụ thuộc vào số lần lặp. Chứng minh nó đúng thực chất là một bài quy nạp theo $k$.

**Bước cơ sở**: Sau lần lặp thứ nhất, `sum = 1`, đúng với công thức.

**Bước quy nạp**: Giả sử sau lần lặp thứ $k$, ta có

$$sum = 1 + 2 + \cdots + k$$

Ở lần lặp tiếp theo, chương trình cộng thêm $(k+1)$, nên giá trị mới là:

$$sum = 1 + 2 + \cdots + k + (k+1)$$

Đúng với bất biến tại bước $k+1$.

Vì vậy, sau lần lặp cuối cùng, ta suy ra chương trình cho kết quả đúng.

Quy nạp không nằm ngoài lập trình. Nó là xương sống của rất nhiều chứng minh về chương trình đúng.

## Ví dụ 7: Ứng dụng trong Khoa học Máy tính — số nút của cây nhị phân đầy đủ

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

**Mệnh đề.** Cây nhị phân đầy đủ có chiều cao $h$ (gốc ở mức $0$) thì có:

$$1 + 2 + 2^2 + \cdots + 2^h = 2^{h+1} - 1$$

nút.

**Chứng minh theo quy nạp trên $h$.**

**Bước cơ sở**: Với $h=0$, cây chỉ có nút gốc, nên số nút là $1 = 2^{0+1} - 1$.

**Bước quy nạp**: Giả sử cây đầy đủ chiều cao $k$ có $2^{k+1} - 1$ nút.

Xét cây đầy đủ chiều cao $k+1$. Khi thêm một mức mới, mức đó có $2^{k+1}$ nút. Vì vậy tổng số nút là:

$$ (2^{k+1} - 1) + 2^{k+1} = 2^{k+2} - 1 $$

Mệnh đề đúng với $k+1$.

Vậy công thức đúng với mọi $h \ge 0$. $\square$

Trong khoa học máy tính, cây nhị phân xuất hiện ở:

- heap,
- cây tìm kiếm nhị phân,
- cây cú pháp,
- biểu thức số học,
- duyệt theo mức và thuật toán trên cây.

Biết quy nạp trên cây hoặc trên chiều cao của cây là kỹ năng rất thực dụng.

## Ví dụ 8: Ứng dụng trong Khoa học Máy tính — tính đúng đắn của công thức truy hồi

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Xét thuật toán đệ quy tính giai thừa:

```text
factorial(n):
    if n = 0 then return 1
    else return n * factorial(n-1)
```

Ta muốn chứng minh hàm `factorial(n)` trả về đúng giá trị $n!$ với mọi $n \ge 0$.

**Bước cơ sở**: Với $n=0$, hàm trả về `1`, đúng bằng $0! = 1$.

**Bước quy nạp**: Giả sử lời gọi `factorial(k)` trả về đúng $k!$ với một $k \ge 0$.

Khi đó:

```text
factorial(k+1) = (k+1) * factorial(k)
```

Theo giả thiết quy nạp, `factorial(k) = k!`, nên:

$$factorial(k+1) = (k+1)k! = (k+1)!$$

Vậy hàm đúng với $k+1$.

Do đó, chương trình đúng với mọi $n \ge 0$. $\square$

Chứng minh chương trình đệ quy thường đi cùng quy nạp, vì bản thân lời gọi đệ quy đang dựa trên việc giải đúng những bài toán nhỏ hơn.

## Ví dụ 9: Ứng dụng trong Khoa học Máy tính — cận trên cho truy hồi

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Giả sử thuật toán chia để trị có thời gian chạy thỏa:

$$T(1) = 1, \qquad T(n) = 2T(n/2) + n \text{ với } n = 2^m$$

Ta muốn chứng minh rằng:

$$T(n) = n \log_2 n + n$$

với mọi $n$ là lũy thừa của $2$.

**Bước cơ sở**: Với $n=1$,

$$T(1) = 1 = 1 \cdot \log_2 1 + 1$$

Đúng.

**Bước quy nạp**: Giả sử công thức đúng với $n = 2^m$, tức là:

$$T(2^m) = 2^m m + 2^m$$

Cần chứng minh:

$$T(2^{m+1}) = 2^{m+1}(m+1) + 2^{m+1}$$

Ta có:

$$T(2^{m+1}) = 2T(2^m) + 2^{m+1}$$

$$= 2(2^m m + 2^m) + 2^{m+1} = 2^{m+1}m + 2^{m+1} + 2^{m+1}$$

$$= 2^{m+1}m + 2^{m+2} = 2^{m+1}(m+2)$$

Mặt khác,

$$2^{m+1}(m+1) + 2^{m+1} = 2^{m+1}(m+2)$$

Hai biểu thức bằng nhau, nên công thức đúng.

Vậy với mọi $n = 2^m$, ta có:

$$T(n) = n \log_2 n + n$$

$\square$

Đây là mô hình điển hình khi phân tích merge sort, thuật toán trên cây đoạn, hoặc nhiều bài toán chia để trị khác.

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Quy nạp xuất hiện rất thường xuyên trong khoa học máy tính, không chỉ trong môn Toán rời rạc.

### 1. Chứng minh tính đúng đắn của thuật toán

- quy nạp theo số bước lặp,
- quy nạp theo kích thước đầu vào,
- quy nạp theo độ sâu lời gọi đệ quy.

### 2. Phân tích cấu trúc dữ liệu đệ quy

- danh sách liên kết,
- cây nhị phân,
- cây tổng quát,
- biểu thức cú pháp trừu tượng.

### 3. Phân tích thời gian chạy

- giải quan hệ truy hồi,
- chứng minh cận trên/cận dưới,
- xác minh công thức thời gian của thuật toán đệ quy.

### 4. Chứng minh tính chất của chương trình

- bất biến vòng lặp,
- điều kiện trước/sau,
- số lượng thao tác sau $n$ vòng,
- tính dừng của một quá trình đơn giản.

### 5. Suy nghĩ theo cấu trúc

Một kỹ năng rất quan trọng của dân công nghệ là: "Bài toán lớn được xây từ những phần nhỏ nào?" Quy nạp buộc ta trả lời câu hỏi đó chính xác.

## Liên hệ giữa quy nạp và quan hệ truy hồi

Quan hệ truy hồi dùng để **định nghĩa** một đại lượng từ các giá trị trước đó. Quy nạp dùng để **chứng minh** một công thức hoặc tính chất liên quan đến đại lượng đó.

Ví dụ, nếu dãy số được cho bởi:

$$a_1 = 1, \qquad a_{n+1} = a_n + 2n + 1$$

ta có thể đoán rằng:

$$a_n = n^2$$

Sau đó dùng quy nạp để chứng minh dự đoán này.

### Minh họa nhanh

**Bước cơ sở**: $a_1 = 1 = 1^2$.

**Bước quy nạp**: Giả sử $a_k = k^2$. Khi đó:

$$a_{k+1} = a_k + 2k + 1 = k^2 + 2k + 1 = (k+1)^2$$

Vậy $a_n = n^2$ với mọi $n \ge 1$.

## Khi nào nên nghĩ đến quy nạp?

Bạn nên thử quy nạp khi gặp các dấu hiệu sau:

1. Mệnh đề có dạng "với mọi $n$".
2. Biểu thức ở kích thước $n+1$ có liên hệ trực tiếp với kích thước $n$.
3. Đối tượng được xây từng bước hoặc được định nghĩa đệ quy.
4. Công thức có tổng, tích, lũy thừa, hoặc số lượng nút/mức.
5. Bài toán liên quan đến thuật toán đệ quy, vòng lặp, cây, hoặc dãy.

## Checklist viết bước quy nạp

Khi làm bài, bạn có thể theo checklist sau:

1. Xác định rõ mệnh đề $P(n)$.
2. Ghi miền của $n$.
3. Chọn đúng điểm bắt đầu $n_0$.
4. Kiểm tra cơ sở thật cẩn thận.
5. Ở bước quy nạp, viết: "Giả sử $P(k)$ đúng".
6. Viết mục tiêu mới: "Cần chứng minh $P(k+1)$ đúng".
7. Bắt đầu từ biểu thức của $P(k+1)$ hoặc từ vế cần biến đổi thuận lợi hơn.
8. Chỉ dùng đúng những gì giả thiết quy nạp cho phép.
9. Kết thúc bằng câu khẳng định rõ ràng.

<div class="interactive-tool" markdown="1">
### Công cụ tương tác: Xây dựng chứng minh quy nạp

<div data-demo="induction-checker"></div>
</div>

<script src="{{ '/public/js/induction-step-checker.js' | relative_url }}"></script>

## Bài tập tự luyện

### Bài 1

Chứng minh bằng quy nạp rằng với mọi $n \ge 1$,

$$1 + 3 + 5 + \cdots + (2n-1) = n^2$$

### Bài 2

Chứng minh bằng quy nạp rằng với mọi $n \ge 1$,

$$1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

### Bài 3

Chứng minh rằng với mọi $n \ge 1$, số $5^n - 1$ chia hết cho $4$.

### Bài 4

Chứng minh rằng với mọi $n \ge 4$,

$$2^n > n^2$$

*Gợi ý:* Chọn đúng bước cơ sở là phần quan trọng của bài này.

### Bài 5

Một cây nhị phân đầy đủ có $h$ mức (tính từ mức $1$). Hãy chứng minh rằng số lá của cây là $2^{h-1}$.

### Bài 6

Xét đoạn mã sau:

```text
product := 1
for i := 1 to n do
    product := 2 * product
```

Hãy dùng ý tưởng quy nạp theo số vòng lặp để chứng minh rằng sau khi kết thúc, `product = 2^n`.

### Bài 7

Cho hàm đệ quy:

```text
power2(n):
    if n = 0 then return 1
    else return 2 * power2(n-1)
```

Hãy chứng minh bằng quy nạp rằng `power2(n)` trả về đúng giá trị $2^n$ với mọi $n \ge 0$.

### Bài 8 — sửa lỗi chứng minh

Một sinh viên muốn chứng minh rằng với mọi $n \ge 1$,

$$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$

và viết như sau:

> Giả sử công thức đúng với $n=k+1$. Khi đó
> $$1 + 2 + \cdots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$
> nên công thức đúng.

Hãy chỉ ra chỗ sai trong lập luận trên và viết lại bước quy nạp cho đúng.

### Bài 9 — bài tập có yếu tố khoa học máy tính

Giả sử một thuật toán đệ quy có số lời gọi hàm thỏa:

$$C(0) = 1, \qquad C(n+1) = C(n) + 2$$

Hãy dùng quy nạp để chứng minh rằng:

$$C(n) = 2n + 1$$

## Tổng kết

Quy nạp toán học là công cụ chứng minh cốt lõi của toán rời rạc. Điểm mạnh của nó không nằm ở việc "học thuộc hai bước", mà ở chỗ nó dạy ta một lối tư duy rất gần với lập trình và thiết kế thuật toán:

- giải quyết trường hợp nhỏ nhất,
- giả sử bài toán nhỏ hơn đã giải được,
- dùng điều đó để xây và chứng minh trường hợp lớn hơn.

Khi bạn thấy một mệnh đề phụ thuộc vào $n$, một cấu trúc đệ quy, một vòng lặp, hoặc một cây được phát triển theo từng mức, hãy tự hỏi: **Liệu đây có phải là lúc dùng quy nạp không?**

Nếu câu trả lời là có, hãy quay lại đúng khung chuẩn:

- xác định $P(n)$,
- kiểm tra bước cơ sở,
- viết giả thiết quy nạp rõ ràng,
- chứng minh trường hợp kế tiếp,
- kết luận mạch lạc.

Làm đúng đủ nhiều lần, quy nạp sẽ trở thành một phản xạ tự nhiên khi bạn chứng minh trong toán và trong khoa học máy tính.

Trong chương tiếp theo, chúng ta sẽ chuyển sang **lý thuyết tập hợp** — một trong những nền tảng quan trọng nhất của toán học rời rạc.
