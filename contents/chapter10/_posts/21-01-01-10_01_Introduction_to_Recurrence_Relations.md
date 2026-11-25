---
layout: post
title: "Giới thiệu Quan hệ Truy hồi"
categories: chapter10
date: 2021-01-01
order: 1
required: true
lang: vi
excerpt: "Làm quen với quan hệ truy hồi — công cụ mô hình hóa các dãy số, thuật toán đệ quy và quá trình biến đổi theo thời gian trong khoa học máy tính."
---

<div class="textbook-epigraph" markdown="1">

"Every recursion must have a base case and a recursive step that approaches the base case."

<span class="epigraph-attribution">— Computer science folk wisdom</span>

</div>


Khi đối mặt với một bài toán đếm phức tạp — như xếp gạch phủ hành lang $$2 \times n$$ hay tính số bước chuyển $$n$$ đĩa Tháp Hà Nội — việc tìm ngay công thức trực tiếp theo $$n$$ thường rất khó. Nhưng chỉ cần hỏi một câu nhẹ nhàng hơn: *"Nếu đã biết đáp án cho kích thước nhỏ hơn, làm sao xây tiếp bước thứ $$n$$?"* — lập tức toàn bộ bài toán hiện hình dưới dạng một **quan hệ truy hồi (recurrence relation)**.

**Mạch bài học:** Ý tưởng mô tả dãy bằng trạng thái trước đó $$\longrightarrow$$ phân loại truy hồi theo **bậc, tính tuyến tính và tính thuần nhất** $$\longrightarrow$$ mô hình hóa các bài toán kinh điển (Fibonacci, Tháp Hà Nội, lát gạch) $$\longrightarrow$$ giải truy hồi bậc nhất bằng phương pháp lặp (unrolling).

## Bản đồ kiến thức nền: Quan hệ truy hồi nghiên cứu gì trong Toán rời rạc và Khoa học Máy tính?

- **Hệ động lực rời rạc (Discrete Dynamical Systems):** Quan hệ truy hồi là phiên bản rời rạc của phương trình vi phân: thay vì đạo hàm liên tục $$y'(t)$$, ta mô tả sự tiến hóa của dãy $$(a_n)_{n \ge 0}$$ theo các bước nhảy nguyên $$n \to n+1$$ kèm **điều kiện biên (base cases)** xác định nghiệm duy nhất.
- **Phân loại cấu trúc đại số (Order, Linearity, Homogeneity):** Bậc $$k$$ cho biết bộ nhớ cần nhìn lại bao nhiêu bước; tính tuyến tính (không có $$a_{n-1}^2$$ hay $$a_{n-1}a_{n-2}$$) và tính thuần nhất (không có số hạng tự do $$f(n)$$) quyết định liệu ta có dùng được phương trình đặc trưng hay không.
- **Đệ quy và Phân tích thuật toán (Recursion & Complexity Analysis):** Mọi hàm đệ quy đều tương ứng 1–1 với một hệ thức truy hồi cho số phép tính $$T(n)$$ — việc "mở vòng lặp" (unrolling) biến mô tả đệ quy thành công thức đóng tường minh để đánh giá độ phức tạp.

Ở Chương 9, chúng ta đã làm quen với nhiều bài toán đếm và cách ước lượng tốc độ tăng trưởng của hàm số. Sang Chương 10, chúng ta sẽ tiếp cận một công cụ nền tảng để mô hình hóa các quá trình biến đổi theo từng bước: **quan hệ truy hồi** (recurrence relation). Thay vì cho ngay một công thức đóng để tính trực tiếp phần tử thứ $$n$$, quan hệ truy hồi mô tả quy tắc xác định phần tử tiếp theo dựa trên một hoặc nhiều phần tử đứng trước nó.

Cách tiếp cận này xuất hiện rất tự nhiên trong cả toán học lẫn khoa học máy tính: từ dãy Fibonacci kinh điển, các hàm đệ quy, phân tích độ phức tạp thuật toán, quy hoạch động (dynamic programming) cho đến các mô hình tăng trưởng dân số hay lan truyền thông tin. Khi nắm vững quan hệ truy hồi, ta có thể chuyển từ quy luật cục bộ giữa các bước liên tiếp sang cái nhìn toàn cục về hành vi của cả hệ thống.

Bài học này giới thiệu khái niệm quan hệ truy hồi, cách phân loại, quy trình mô hình hóa bài toán thực tế và phương pháp giải một số truy hồi bậc nhất cơ bản.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** quan hệ truy hồi và phân loại theo bậc, tính tuyến tính (tuyến tính / phi tuyến) và tính thuần nhất (thuần nhất / không thuần nhất).
- **Mô hình hóa** các bài toán đếm, bài toán đệ quy và thuật toán bằng quan hệ truy hồi kèm điều kiện ban đầu.
- **Giải** các quan hệ truy hồi bậc nhất đơn giản bằng phương pháp liệt kê, quy nạp hoặc tách nghiệm thuần nhất và nghiệm riêng.

**Từ khóa**: quan hệ truy hồi (recurrence relation), điều kiện đầu (initial conditions), dãy Fibonacci, đệ quy (recursion), quy hoạch động (dynamic programming).
</div>

## Định nghĩa và Khái niệm

### Quan hệ Truy hồi

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ truy hồi là một phương trình biểu diễn số hạng thứ $$n$$ của một dãy số theo một hoặc nhiều số hạng đứng trước nó (và có thể phụ thuộc thêm vào chỉ số $$n$$).
</div>

**Dạng tổng quát**:

<div class="textbook-equation" markdown="1">
$$a_n = f(a_{n-1}, a_{n-2}, \dots, a_{n-k}, n)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trong đó:

- $$a_n$$ là số hạng thứ $$n$$ của dãy.
- $$f$$ là hàm xác định quy luật liên hệ giữa $$a_n$$ và các số hạng trước đó.
- $$k$$ là **bậc** (order) của quan hệ truy hồi — cho biết cần dùng tối đa bao nhiêu số hạng liền trước để tính $$a_n$$.
- $$a_0, a_1, \dots, a_{k-1}$$ là $$k$$ **điều kiện đầu** (initial conditions) cần thiết để xác định duy nhất toàn bộ dãy số.

<div class="content-box insight-box textbook-block" markdown="1">
**Vì sao cần điều kiện đầu?** Quan hệ truy hồi chỉ quy định cách suy ra số hạng sau từ các số hạng trước, chứ không tự xác định được điểm xuất phát của dãy. Các điều kiện đầu $$a_0, a_1, \ldots, a_{k-1}$$ đóng vai trò "mốc khởi tạo" giúp dãy số được xác định duy nhất.
</div>

<div class="textbook-example" markdown="1">
**Một số ví dụ kinh điển**:
</div>

#### Dãy Fibonacci và bài toán đôi thỏ

**Bài toán gốc** (Fibonacci, 1202): Giả sử ta có một đôi thỏ mới sinh (gồm một thỏ đực và một thỏ cái). Khi tròn hai tháng tuổi, mỗi đôi thỏ bắt đầu sinh ra một đôi thỏ con mới vào mỗi tháng, và các đôi thỏ con cũng tuân theo đúng quy luật sinh sản đó (giả sử thỏ không chết). Hỏi sau $$n$$ tháng có tất cả bao nhiêu đôi thỏ?

**Phân tích**: Gọi $$F_n$$ là số đôi thỏ ở tháng thứ $$n$$.

- Tháng 1: có 1 đôi thỏ ban đầu $$\to F_1 = 1$$.
- Tháng 2: đôi thỏ ban đầu vẫn chưa sinh sản $$\to F_2 = 1$$.
- Tháng 3: đôi thỏ ban đầu sinh thêm 1 đôi con $$\to F_3 = 2$$.
- Tháng thứ $$n$$: tổng số đôi thỏ bằng số đôi thỏ đã có ở tháng $$n-1$$ cộng với số đôi thỏ con mới sinh. Vì chỉ những đôi thỏ đã tồn tại từ tháng $$n-2$$ mới đủ hai tháng tuổi để sinh sản, số đôi thỏ mới sinh đúng bằng $$F_{n-2}$$.

**Quan hệ truy hồi Fibonacci**:

<div class="textbook-equation" markdown="1">
$$F_n = F_{n-1} + F_{n-2}, \quad F_1 = 1,\; F_2 = 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Dãy Fibonacci là một ví dụ tiêu biểu của quan hệ truy hồi **tuyến tính thuần nhất bậc 2 có hệ số hằng**. Ở bài học tiếp theo, chúng ta sẽ dùng **phương trình đặc trưng** để tìm công thức đóng cho lớp truy hồi này.

**Các số hạng đầu của dãy**: $$1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$$

![Xoắn ốc Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

<p class="textbook-figure-caption" data-figure="10.1">Dãy Fibonacci xuất hiện trong tự nhiên — tỷ lệ vàng và đường xoắn ốc là hệ quả trực tiếp của quan hệ truy hồi $$F_n = F_{n-1} + F_{n-2}$$.</p>

<div class="content-box fun-fact-box textbook-block" markdown="1">
**Giai thoại**: Khi nêu ra bài toán đôi thỏ vào thời Trung Cổ, nhà toán học người Ý Leonardo Fibonacci hẳn không ngờ rằng dãy số mang tên ông lại xuất hiện rộng rãi đến thế — từ tỷ lệ vàng trong kiến trúc, đường xoắn ốc trên vỏ ốc, cách sắp xếp lá cây trong tự nhiên cho đến các thuật toán tìm kiếm và cấu trúc dữ liệu trong khoa học máy tính hiện đại.
</div>

#### Giai thừa

- **Quan hệ truy hồi**: $$n! = n \cdot (n-1)!$$
- **Điều kiện đầu**: $$0! = 1$$
- **Các số hạng đầu**: $$1, 1, 2, 6, 24, 120, 720, \dots$$

#### Tháp Hà Nội

Trò chơi Tháp Hà Nội (Tower of Hanoi) gồm ba cọc và $$n$$ đĩa có kích thước khác nhau, ban đầu xếp chồng lên nhau theo thứ tự nhỏ dần từ dưới lên trên. Nhiệm vụ là chuyển toàn bộ $$n$$ đĩa sang một cọc khác sao cho mỗi bước chỉ chuyển một đĩa và không bao giờ đặt đĩa lớn lên trên đĩa nhỏ.

Để chuyển $$n$$ đĩa, ta cần chuyển $$n-1$$ đĩa trên cùng sang cọc trung gian (tốn $$H_{n-1}$$ bước), chuyển đĩa lớn nhất sang cọc đích (tốn $$1$$ bước), rồi chuyển tiếp $$n-1$$ đĩa từ cọc trung gian sang cọc đích (tốn thêm $$H_{n-1}$$ bước).

- **Quan hệ truy hồi**: $$H_n = 2H_{n-1} + 1$$
- **Điều kiện đầu**: $$H_1 = 1$$
- **Các số hạng đầu**: $$1, 3, 7, 15, 31, 63, \dots$$

![Tháp Hà Nội — bài toán đệ quy kinh điển](/discrete-mathematics-for-computer-science-iuh/img/course/Tower_of_Hanoi.gif)

<p class="textbook-figure-caption" data-figure="10.2">Tháp Hà Nội — mỗi bước giải bài toán kích thước $$n$$ đều quy về bài toán kích thước $$n-1$$, tạo nên một mô hình kinh điển cho quan hệ truy hồi.</p>

<div class="interactive-tool" markdown="1">
<div data-demo="recurrence-visualizer"></div>
</div>
<script src="{{ '/public/js/recurrence-visualizer.js' | relative_url }}"></script>

## Phân loại Quan hệ Truy hồi

Việc phân loại quan hệ truy hồi giúp chúng ta nhận diện nhanh phương pháp giải phù hợp. Thông thường, quan hệ truy hồi được phân loại theo ba tiêu chí: tính tuyến tính, tính thuần nhất và tính hằng của hệ số.

### Theo Tính tuyến tính (Linear vs. Nonlinear)

Một quan hệ truy hồi được gọi là **tuyến tính** nếu vế phải là tổ hợp tuyến tính của các số hạng đứng trước (mỗi số hạng chỉ xuất hiện với bậc nhất, không có tích hay lũy thừa giữa chúng), có thể cộng thêm một hàm $$f(n)$$ chỉ phụ thuộc vào $$n$$.

| Loại | Dạng tổng quát | Ví dụ |
|:-----|:-----|:------|
| **Tuyến tính** | $$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + f(n)$$ | $$a_n = 3a_{n-1} - 2a_{n-2}$$ |
| **Phi tuyến** | Chứa tích, lũy thừa hoặc hàm phi tuyến của các $$a_{n-i}$$ | $$a_n = a_{n-1} \cdot a_{n-2}$$ hoặc $$a_n = a_{n-1}^2 + 1$$ |

**Ví dụ phân biệt nhanh**:

- $$f_n = 4f_{n-1} + f_{n-2}$$: **tuyến tính thuần nhất, hệ số hằng**, bậc 2.
- $$f_n = 3f_{n-1} + 2f_{n-2} + n$$: **tuyến tính không thuần nhất, hệ số hằng**, bậc 2 (có thêm thành phần $$f(n) = n$$).
- $$f_n = 3(f_{n-1})^2 + 2f_{n-2} + n$$: **phi tuyến** (vì chứa bình phương $$(f_{n-1})^2$$).
- $$f_n = 2f_{n-1}\cdot f_{n-2} + n$$: **phi tuyến** (vì chứa tích của hai số hạng $$f_{n-1}$$ và $$f_{n-2}$$).
- $$f_n = n \cdot f_{n-2} + n$$: **tuyến tính nhưng có hệ số biến thiên** (hệ số nhân với $$f_{n-2}$$ phụ thuộc vào $$n$$, không phải hằng số). Do không có hệ số hằng, quan hệ này không thể giải trực tiếp bằng phương trình đặc trưng.

### Theo Tính thuần nhất (Homogeneous vs. Nonhomogeneous)

| Loại | Dạng tổng quát | Ví dụ |
|:-----|:-----|:------|
| **Thuần nhất** | $$a_n = c_1 a_{n-1} + \dots + c_k a_{n-k}$$ | $$a_n = 3a_{n-1} - 2a_{n-2}$$ |
| **Không thuần nhất** | Có thêm thành phần tự do $$f(n) \neq 0$$ | $$a_n = 2a_{n-1} + n$$ |

<div class="textbook-example" markdown="1">
**Ví dụ tổng hợp**:

- $$F_n = F_{n-1} + F_{n-2}$$ là quan hệ **tuyến tính thuần nhất** bậc 2.
- $$H_n = 2H_{n-1} + 1$$ là quan hệ **tuyến tính không thuần nhất** bậc 1.
- $$a_n = a_{n-1} \cdot a_{n-2}$$ là quan hệ **phi tuyến** bậc 2.

![Dãy truy hồi tuyến tính hệ số hằng](/discrete-mathematics-for-computer-science-iuh/img/course/Constant-recursive-sequences.svg)

<p class="textbook-figure-caption" data-figure="10.3">Phân loại quan hệ truy hồi theo tính tuyến tính và tính thuần nhất giúp lựa chọn đúng phương pháp tìm nghiệm.</p>
</div>

<div class="content-box warning-box textbook-block" markdown="1">
**Sai lầm thường gặp**: Sinh viên hay nhầm lẫn giữa **bậc** và **tính tuyến tính**. Bậc cho biết ta cần nhìn ngược lại bao nhiêu số hạng trước đó để tính $$a_n$$, còn tính tuyến tính yêu cầu các số hạng không nhân với nhau hay nâng lên lũy thừa. Một quan hệ truy hồi có thể có bậc rất cao nhưng vẫn tuyến tính; ngược lại, nó có thể chỉ có bậc 1 nhưng lại phi tuyến (chẳng hạn $$a_n = a_{n-1}^2 + 1$$).
</div>

## Mô hình hóa bài toán bằng Quan hệ Truy hồi

Quan hệ truy hồi không chỉ là khái niệm lý thuyết mà còn là công cụ rất hiệu quả để mô hình hóa các bài toán có cấu trúc lặp lại. Khi xây dựng mô hình truy hồi, ta thường thực hiện theo ba bước:

1. **Xác định dãy số**: Đặt ký hiệu đại lượng cần tính (thường là $$a_n$$) và làm rõ ý nghĩa của chỉ số $$n$$.
2. **Thiết lập quan hệ**: Phân tích cấu trúc bài toán để biểu diễn $$a_n$$ theo các bài toán con nhỏ hơn ($$a_{n-1}, a_{n-2}, \dots$$).
3. **Xác định điều kiện đầu**: Tính trực tiếp giá trị của vài số hạng đầu tiên từ dữ kiện bài toán.

<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ 1: Lãi kép (Compound Interest)**

Một người gửi tiết kiệm 10 triệu đồng với lãi suất $$0{,}5\%$$ mỗi tháng, tiền lãi được nhập vào gốc sau mỗi tháng. Gọi $$a_n$$ là số tiền có trong tài khoản sau $$n$$ tháng.

Sau mỗi tháng, số dư tăng thêm $$0{,}5\%$$ so với tháng liền trước:

<div class="textbook-equation" markdown="1">
$$a_n = a_{n-1} + 0.005 \cdot a_{n-1} = 1.005 \cdot a_{n-1}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Điều kiện đầu: $$a_0 = 10\,000\,000$$ (số tiền gốc ban đầu).

Đây là quan hệ truy hồi tuyến tính thuần nhất bậc 1, có công thức đóng:

<div class="textbook-equation" markdown="1">
$$a_n = 10\,000\,000 \cdot (1.005)^n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ 2: Đếm xâu nhị phân không chứa hai bit 0 liên tiếp**

Hãy đếm số xâu nhị phân độ dài $$n$$ không có hai bit $$0$$ đứng cạnh nhau. Gọi $$a_n$$ là số xâu hợp lệ có độ dài $$n$$.

Ta phân chia các xâu hợp lệ độ dài $$n$$ theo bit cuối cùng:

- **Bit cuối là 1**: Khi đó $$n-1$$ bit đứng trước có thể là bất kỳ xâu hợp lệ nào có độ dài $$n-1$$, nên có $$a_{n-1}$$ xâu.
- **Bit cuối là 0**: Để tránh hai bit $$0$$ liên tiếp, bit kề cuối bắt buộc phải là $$1$$, còn $$n-2$$ bit đầu tiên có thể là bất kỳ xâu hợp lệ nào có độ dài $$n-2$$, nên có $$a_{n-2}$$ xâu.

Vì hai trường hợp này rời nhau và phủ hết mọi khả năng, ta thu được:

<div class="textbook-equation" markdown="1">
$$a_n = a_{n-1} + a_{n-2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Điều kiện đầu: $$a_1 = 2$$ (gồm `"0"` và `"1"`), $$a_2 = 3$$ (gồm `"01"`, `"10"`, `"11"`).
</div>

<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ 3: Số cách leo cầu thang**

Một cầu thang có $$n$$ bậc, mỗi bước bạn có thể đi lên 1 bậc hoặc 2 bậc. Gọi $$a_n$$ là số cách khác nhau để lên đến bậc thứ $$n$$.

Để đặt chân lên bậc thứ $$n$$, bước cuối cùng chỉ có thể xuất phát từ bậc $$n-1$$ (bước 1 bậc) hoặc từ bậc $$n-2$$ (bước 2 bậc). Do đó:

<div class="textbook-equation" markdown="1">
$$a_n = a_{n-1} + a_{n-2}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Điều kiện đầu: $$a_1 = 1$$ (1 cách: đi 1 bậc), $$a_2 = 2$$ (2 cách: $$1+1$$ hoặc bước thẳng 2 bậc).

Dãy số thu được là $$1, 2, 3, 5, 8, 13, \dots$$ — mang đúng quy luật truy hồi của dãy Fibonacci nhưng có điều kiện đầu dịch đi một chỉ số.
</div>

![Dãy hình học — tăng trưởng theo tỷ lệ](/discrete-mathematics-for-computer-science-iuh/img/course/Geometric_sequence.svg)

<p class="textbook-figure-caption" data-figure="10.4">Các bài toán tăng trưởng theo tỷ lệ phần trăm như lãi kép hay tăng trưởng dân số thường dẫn về cấp số nhân $$a_n = r \cdot a_{n-1}$$.</p>

## Quan hệ Truy hồi Bậc nhất

<div class="textbook-definition" id="định-nghĩa" markdown="1">
**Định nghĩa**: Quan hệ truy hồi bậc nhất có dạng tổng quát

<div class="textbook-equation" markdown="1">
$$a_n = f(a_{n-1}, n)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

trong đó $$a_n$$ chỉ phụ thuộc vào số hạng liền trước $$a_{n-1}$$ và có thể phụ thuộc thêm vào chỉ số $$n$$.
</div>

### Truy hồi tuyến tính bậc nhất thuần nhất

Dạng chuẩn:

<div class="textbook-equation" markdown="1">
$$a_n = c \cdot a_{n-1} \quad \text{với} \quad a_0 = A$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nghiệm tổng quát của phương trình này là một cấp số nhân:

<div class="textbook-equation" markdown="1">
$$a_n = A \cdot c^n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Chứng minh bằng quy nạp**:

- Với $$n = 0$$: $$a_0 = A = A \cdot c^0$$ (đúng).
- Với $$n = 1$$: $$a_1 = c \cdot a_0 = cA = A \cdot c^1$$ (đúng).
- Giả sử công thức đúng đến $$n-1$$, tức $$a_{n-1} = A \cdot c^{n-1}$$. Khi đó $$a_n = c \cdot a_{n-1} = c \cdot A \cdot c^{n-1} = A \cdot c^n$$. Công thức được chứng minh.

<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Dân số hiện tại của một thành phố là $$1{,}2$$ triệu người và tăng đều $$1{,}5\%$$ mỗi năm. Gọi $$a_n$$ là dân số sau $$n$$ năm.

Ta có quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$a_n = 1.015 \cdot a_{n-1}, \quad a_0 = 1.2 \times 10^6$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nghiệm tổng quát là $$a_n = 1.2 \times 10^6 \cdot (1.015)^n$$.

Sau 10 năm, dân số ước tính đạt $$a_{10} = 1.2 \times 10^6 \cdot (1.015)^{10} \approx 1.393 \times 10^6$$ người.
</div>
</div>

### Truy hồi tuyến tính bậc nhất không thuần nhất

Dạng chuẩn:

<div class="textbook-equation" markdown="1">
$$a_n = c \cdot a_{n-1} + f(n) \quad \text{với} \quad a_0 = A$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Quy trình giải gồm ba bước:

1. Tìm nghiệm tổng quát của phần thuần nhất liên kết: $$a_n^{(h)} = A_0 \cdot c^n$$.
2. Tìm một nghiệm riêng $$a_n^{(p)}$$ có dạng tương ứng với $$f(n)$$.
3. Cộng hai nghiệm lại để được nghiệm tổng quát $$a_n = a_n^{(h)} + a_n^{(p)}$$, rồi thay điều kiện đầu để tìm hằng số $$A_0$$.

#### Trường hợp $$f(n) = d$$ (hằng số)

Khi $$c \neq 1$$, ta thử nghiệm riêng là hằng số $$a_n^{(p)} = K$$. Thay vào quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$K = c \cdot K + d \quad\Rightarrow\quad K(1-c) = d \quad\Rightarrow\quad K = \frac{d}{1-c}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

*(Lưu ý: Nếu $$c = 1$$, hằng số đã là nghiệm thuần nhất nên cần thử nghiệm riêng dạng $$K \cdot n$$.)*

<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Giải $$a_n = 3a_{n-1} + 4$$ với điều kiện đầu $$a_0 = 1$$.

- Nghiệm thuần nhất: $$a_n^{(h)} = A \cdot 3^n$$.
- Nghiệm riêng (hằng số): $$K = \frac{4}{1-3} = -2$$.
- Nghiệm tổng quát: $$a_n = A \cdot 3^n - 2$$.
- Thay $$a_0 = 1$$: $$1 = A - 2 \Rightarrow A = 3$$.

Vậy công thức đóng là $$a_n = 3 \cdot 3^n - 2 = 3^{n+1} - 2$$.

Kiểm tra nhanh với $$n = 1$$: công thức cho $$a_1 = 3^2 - 2 = 7$$, khớp với truy hồi $$3 \cdot 1 + 4 = 7$$ ✓.
</div>
</div>

#### Trường hợp $$f(n)$$ là đa thức bậc $$m$$

Khi $$c \neq 1$$, ta thử nghiệm riêng là một đa thức cùng bậc $$m$$:

<div class="textbook-equation" markdown="1">
$$a_n^{(p)} = b_0 + b_1 n + b_2 n^2 + \cdots + b_m n^m$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Giải $$a_n = 2a_{n-1} + 3n + 1$$ với điều kiện đầu $$a_0 = 2$$.

- Nghiệm thuần nhất: $$a_n^{(h)} = A \cdot 2^n$$.
- Vì $$f(n) = 3n + 1$$ là đa thức bậc nhất và $$c = 2 \neq 1$$, ta thử nghiệm riêng dạng $$a_n^{(p)} = B_0 + B_1 n$$.
- Thay vào quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$B_0 + B_1 n = 2\bigl(B_0 + B_1(n-1)\bigr) + 3n + 1 = 2B_0 + 2B_1 n - 2B_1 + 3n + 1$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đồng nhất hệ số ở hai vế:

- Hệ số của $$n$$: $$B_1 = 2B_1 + 3 \Rightarrow B_1 = -3$$.
- Hằng số tự do: $$B_0 = 2B_0 - 2B_1 + 1 = 2B_0 + 7 \Rightarrow B_0 = -7$$.

Suy ra nghiệm tổng quát là $$a_n = A \cdot 2^n - 3n - 7$$.

Thay $$a_0 = 2$$: $$2 = A - 7 \Rightarrow A = 9$$.

Vậy công thức đóng là $$a_n = 9 \cdot 2^n - 3n - 7$$.

Kiểm tra với $$n = 1$$: công thức cho $$a_1 = 18 - 3 - 7 = 8$$, khớp với truy hồi $$2 \cdot 2 + 3 + 1 = 8$$ ✓.
</div>
</div>

<div class="content-box warning-box textbook-block" markdown="1">
**Sai lầm thường gặp**: Khi chọn dạng nghiệm riêng, người học thường quên kiểm tra xem dạng thử có bị trùng với nghiệm thuần nhất hay không. Nếu xảy ra trùng lặp (cộng hưởng), ta phải nhân thêm $$n$$ (hoặc $$n^s$$) vào dạng nghiệm thử. Trường hợp này sẽ được trình bày đầy đủ ở Bài 10.3.
</div>

## Ứng dụng trong Khoa học Máy tính

### Phân tích độ phức tạp thuật toán

Thời gian chạy của hầu hết các thuật toán đệ quy đều được mô tả tự nhiên bằng quan hệ truy hồi. Chẳng hạn:

- **Merge Sort**: $$T(n) = 2T(n/2) + n$$
- **Tìm kiếm nhị phân (Binary Search)**: $$T(n) = T(n/2) + 1$$
- **Tính Fibonacci bằng đệ quy trực tiếp**: $$T(n) = T(n-1) + T(n-2) + 1$$

![Dãy số học — tổng tích lũy](/discrete-mathematics-for-computer-science-iuh/img/course/Arithmetic_progression.svg)

<p class="textbook-figure-caption" data-figure="10.5">Quan hệ truy hồi không thuần nhất với $$f(n)$$ là đa thức thường sinh ra cấp số cộng hoặc các tổng tích lũy có công thức đóng gọn gàng.</p>

### Quy hoạch động (Dynamic Programming)

Quy hoạch động giải quyết bài toán lớn bằng cách lưu trữ và kết hợp lời giải của các bài toán con gối nhau — thực chất chính là thiết lập một công thức truy hồi chuyển trạng thái. Nhiều bài toán kinh điển như cái túi (Knapsack), xâu con chung dài nhất (LCS) hay đường đi ngắn nhất (Bellman-Ford) đều được xây dựng trực tiếp từ quan hệ truy hồi.

### Mô hình hóa hệ thống

Từ dự báo dân số, tính lãi kép ngân hàng đến mô phỏng tốc độ lan truyền mã độc trong mạng máy tính, quan hệ truy hồi giúp chúng ta mô tả quy luật tiến triển của hệ thống và dự đoán trạng thái tương lai từ lịch sử hiện có.

### Minh hoạ tương tác

Bạn có thể thử tính các số hạng, quan sát đồ thị tăng trưởng và đối chiếu trực tiếp giữa quan hệ truy hồi với công thức đóng (chẳng hạn dãy Fibonacci) qua công cụ tương tác dưới đây:

<div class="interactive-demo" markdown="1">
<div data-demo="recurrence-explainer" data-mode="linear" data-preset="fib"></div>
</div>
<script src="{{ '/public/js/explainers/recurrence-explainer.js' | relative_url }}"></script>

## Ví dụ tính tay cầm tay chỉ việc: Mở vòng lặp giải bài toán Tháp Hà Nội $$H_n = 2H_{n-1} + 1$$

Với điều kiện đầu $$H_1 = 1$$ (1 đĩa cần đúng 1 bước chuyển), hãy giải công thức đóng cho $$H_n$$ hoàn toàn bằng tay qua kỹ thuật **thay thế lặp (unrolling)**:

1. **Tính 4 giá trị đầu để lấy trực giác:**
   - $$H_1 = 1$$
   - $$H_2 = 2(1) + 1 = 3$$
   - $$H_3 = 2(3) + 1 = 7$$
   - $$H_4 = 2(7) + 1 = 15$$
   Ta thấy mẫu hình rất rõ: $$1, 3, 7, 15$$ đều kém lũy thừa của 2 đúng 1 đơn vị!
2. **Mở rộng từng bước (unrolling) từ $$H_n$$ xuống $$H_1$$:**
   $$\begin{aligned}
   H_n &= 2H_{n-1} + 1 \\
       &= 2(2H_{n-2} + 1) + 1 = 2^2 H_{n-2} + 2 + 1 \\
       &= 2^3 H_{n-3} + 2^2 + 2 + 1 \\
       &\;\;\vdots \\
       &= 2^{n-1} H_1 + \sum_{k=0}^{n-2} 2^k = 2^{n-1}(1) + (2^{n-1} - 1) = 2^n - 1.
   \end{aligned}$$
3. **Kiểm tra ngược bằng thế vào truy hồi:** $$2H_{n-1} + 1 = 2(2^{n-1} - 1) + 1 = 2^n - 2 + 1 = 2^n - 1 = H_n$$. Chính xác! Với $$n = 64$$ đĩa, $$H_{64} = 2^{64} - 1 \approx 1{,}84 \times 10^{19}$$ bước.

### Khung giải thích: Ba bước vàng để lập mô hình bằng truy hồi (nên đọc chậm)

1. **Bước 1 — Phân hoạch theo lựa chọn cuối cùng (hoặc đầu tiên):** Để đếm $$a_n$$, hãy chia toàn bộ tập cấu hình kích thước $$n$$ thành các trường hợp **rời nhau và phủ kín** dựa trên phần tử thứ $$n$$ (ví dụ: viên gạch cuối đặt dọc hay đặt ngang).
2. **Bước 2 — Ghép điều kiện đầu đủ số bậc:** Một truy hồi bậc $$k$$ cần đúng $$k$$ điều kiện đầu độc lập (ví dụ $$a_0, a_1$$ cho bậc 2). Thiếu 1 điều kiện đầu thì dãy có vô số nghiệm.
3. **Bước 3 — Kiểm tra nhỏ trước khi chứng minh tổng quát:** Luôn tính tay $$a_1, a_2, a_3, a_4$$ và đối chiếu trực tiếp bằng cách liệt kê cấu hình nhỏ — đây là cách nhanh nhất để phát hiện sai lệch hệ số hoặc thiếu trường hợp biên.

$$\text{Phân hoạch bước cuối} \;\xrightarrow{\text{hệ thức } a_n = F(a_{n-1},\dots)}\; \text{Điều kiện đầu} \;\xrightarrow{\text{unrolling / giải}}\; \text{Công thức đóng } a_n.$$

## Bài tập thực hành

### Bài tập 1: Phân loại quan hệ truy hồi

Hãy phân loại các quan hệ truy hồi sau theo tính tuyến tính (tuyến tính / phi tuyến), tính thuần nhất (thuần nhất / không thuần nhất) và xác định bậc của chúng:

a) $$a_n = 3a_{n-1} - 2a_{n-2}$$
b) $$a_n = a_{n-1}^2 + 1$$
c) $$a_n = 2a_{n-1} + n^2$$
d) $$a_n = a_{n-1} \cdot a_{n-2} + a_{n-3}$$

<details>
<summary>Đáp án</summary>

a) Tuyến tính, thuần nhất, bậc 2.
b) Phi tuyến (chứa bình phương $$a_{n-1}^2$$), bậc 1.
c) Tuyến tính, không thuần nhất (có thành phần $$f(n) = n^2$$), bậc 1.
d) Phi tuyến (chứa tích $$a_{n-1} \cdot a_{n-2}$$), bậc 3.

</details>

### Bài tập 2: Thiết lập quan hệ truy hồi

Một người gửi 50 triệu đồng vào ngân hàng với lãi suất $$0{,}7\%$$ mỗi tháng. Vào cuối mỗi tháng (sau khi cộng lãi), người đó rút ra 3 triệu đồng để chi tiêu. Hãy thiết lập quan hệ truy hồi cho số dư $$a_n$$ sau $$n$$ tháng.

<details>
<summary>Đáp án</summary>

Gọi $$a_n$$ là số dư (đơn vị: triệu đồng) sau $$n$$ tháng. Sau mỗi tháng, số dư tăng thêm $$0{,}7\%$$ (nhân với $$1{,}007$$) rồi giảm đi 3 triệu:

<div class="textbook-equation" markdown="1">
$$a_n = 1.007 \cdot a_{n-1} - 3, \quad a_0 = 50$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Kiểm tra với tháng đầu tiên: $$a_1 = 1.007 \cdot 50 - 3 = 47.35$$ (triệu đồng) ✓.
</details>

### Bài tập 3: Giải quan hệ truy hồi bậc nhất

Tìm công thức đóng cho các quan hệ truy hồi sau:

a) $$a_n = 2a_{n-1}$$ với $$a_0 = 5$$
b) $$a_n = a_{n-1} + 3$$ với $$a_0 = 4$$
c) $$a_n = -3a_{n-1}$$ với $$a_0 = 2$$

<details>
<summary>Đáp án</summary>

a) $$a_n = 5 \cdot 2^n$$ (cấp số nhân). Các số hạng đầu: $$5, 10, 20, 40, 80, \dots$$

b) $$a_n = 4 + 3n$$ (cấp số cộng). Các số hạng đầu: $$4, 7, 10, 13, 16, \dots$$

c) $$a_n = 2 \cdot (-3)^n$$. Các số hạng đầu: $$2, -6, 18, -54, 162, \dots$$
</details>

### Bài tập 4: Ứng dụng thực tế

Một công ty khởi nghiệp có 1.000 người dùng ở tháng đầu tiên. Giả sử mỗi tháng số người dùng tăng gấp đôi so với tháng trước. Hỏi đến tháng thứ 12 công ty có bao nhiêu người dùng?

<details>
<summary>Đáp án</summary>

Gọi $$u_n$$ là số người dùng ở tháng thứ $$n$$. Ta có:

<div class="textbook-equation" markdown="1">
$$u_n = 2u_{n-1}, \quad u_1 = 1000$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Công thức đóng là $$u_n = 1000 \cdot 2^{n-1}$$.

Ở tháng thứ 12: $$u_{12} = 1000 \cdot 2^{11} = 1000 \cdot 2048 = 2.048.000$$ người dùng.
</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Ôn tập về quan hệ tương đương)

## Tóm tắt

- **Quan hệ truy hồi** biểu diễn số hạng $$a_n$$ theo các số hạng đứng trước nó.
- **Bậc** của quan hệ truy hồi là số lượng số hạng liền trước cần dùng để xác định $$a_n$$.
- **Phân loại** dựa trên tính tuyến tính (tuyến tính / phi tuyến), tính thuần nhất (thuần nhất / không thuần nhất) và tính hằng của hệ số.
- **Điều kiện đầu** giúp xác định duy nhất một dãy số từ quan hệ truy hồi.
- **Quy trình mô hình hóa** gồm 3 bước: đặt dãy số, thiết lập quan hệ truy hồi và xác định điều kiện đầu.
- **Truy hồi bậc nhất thuần nhất** $$a_n = c \cdot a_{n-1}$$ có nghiệm dạng $$a_n = A \cdot c^n$$; với **truy hồi không thuần nhất**, nghiệm tổng quát bằng tổng của nghiệm thuần nhất và một nghiệm riêng.

Trong bài tiếp theo, chúng ta sẽ học cách giải quan hệ truy hồi tuyến tính thuần nhất bậc cao bằng **phương trình đặc trưng** — công cụ mạnh mẽ giúp tìm công thức tường minh cho dãy Fibonacci và nhiều lớp dãy số quan trọng khác.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eAaP4XaB8hM">RECURRENCE RELATIONS - DISCRETE MATHEMATICS</a> — TrevTutor (tiếng Anh). Giới thiệu tổng quan cách định nghĩa dãy số qua các số hạng đứng trước.
- <a href="https://www.youtube.com/watch?v=0OcUAjOXmFc">Recursive Sequences</a> — Dr. Trefor Bazett (tiếng Anh). Trình bày rõ ràng về dãy truy hồi và vai trò của điều kiện đầu.
- <a href="https://www.youtube.com/watch?v=qmm9GPhA1MY">The Miraculous Fibonacci Sequence</a> — Dr. Trefor Bazett (tiếng Anh). Khám phá dãy Fibonacci — ví dụ trọng tâm sẽ được giải tường minh ở bài sau.
