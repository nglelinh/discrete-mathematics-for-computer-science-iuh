---

layout: post
title: "Phép đếm: Từ Cờ bạc đến An ninh mạng"
categories: chapter07
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Bài đọc mở rộng về ứng dụng của phép đếm: từ bài toán chia tiền cược của Pascal và Fermat đến bảo mật mật khẩu, phân tích Big-O, nghịch lý sinh nhật và kiểm thử tổ hợp."
---

Mùa hè năm 1654, một quý tộc mê bài bạc người Pháp tên Chevalier de Méré gửi thư hỏi Blaise Pascal một thắc mắc tưởng như vụn vặt: *nếu ván bài bị gián đoạn giữa chừng, nên chia tiền cược thế nào cho công bằng?* Cuộc trao đổi thư từ giữa Pascal và Pierre de Fermat đã khai sinh ra lý thuyết xác suất — và gần 400 năm sau, chính tư duy đếm không gian khả năng ấy lại là bức tường phòng thủ đầu tiên bảo vệ mật khẩu ngân hàng, mã phiên đăng nhập (`session_id`) và thuật toán Big-O của chúng ta!

**Mạch bài học:** Kiến thức cần nhớ (không gian mẫu rời rạc, entropy mật khẩu theo bit, phân tích chi phí thuật toán) → Pascal–Fermat 1654 → An ninh mạng (mật khẩu, PIN, Session ID, CSRF) & Big-O → Ví dụ tính tay làm từng bước: tính entropy (bit) và thời gian brute-force của mật khẩu 8 ký tự thường vs. passphrase 4 từ → Giải thích: 3 bước chuyển bài toán an ninh thành phép đếm không gian khóa → Bài tập.

## Kiến thức cần nhớ: Phép đếm kết nối Xác suất, Mật mã học và Thuật toán như thế nào?

### 1. Không gian khả năng & Xác suất cổ điển
Khi mọi kết quả sơ cấp đồng khả năng, xác suất là tỷ số của hai phép đếm: $$P(E) = \vert E\vert / \vert\Omega\vert$$. Trực giác con người rất dễ đánh giá sai tích lũy xác suất — chỉ có phép đếm chính xác mới trả lời đúng.

### 2. Entropy mật khẩu — đo độ mạnh bằng số bit $$H = \log_2(\vert\mathcal{K}\vert)$$
Nếu không gian khóa có $$\vert\mathcal{K}\vert = N^L$$ chuỗi đều nhau (bảng chữ cái cỡ $$N$$, độ dài $$L$$), thì **entropy** bằng $$H = L \log_2 N$$ bit. Mỗi khi tăng thêm **1 bit entropy**, thời gian dò vét cạn (brute-force) của kẻ tấn công **tăng gấp đôi**!

### 3. Đếm số bước cơ bản $$\to$$ Độ phức tạp thuật toán Big-O
Đếm số lần lặp lồng nhau của thuật toán sắp xếp hay tìm kiếm giúp dự báo chính xác chương trình có "chết đứng" hay không khi dữ liệu phình từ $$n = 10^3$$ lên $$n = 10^6$$.

Ở các mục trước, chúng ta đã xây dựng bộ công cụ tổ hợp cơ bản. Mục bổ sung này trình bày ứng dụng của phép đếm từ nguồn gốc lịch sử đến an ninh mạng, kiểm thử phần mềm và phân tích độ phức tạp thuật toán.

Động lực ban đầu của lý thuyết xác suất và phép đếm xuất phát từ các bài toán cờ bạc thế kỷ XVII. Từ nền tảng đó, tư duy đếm khả năng đã trở thành công cụ thiết yếu để đánh giá độ mạnh mật khẩu, ước lượng xác suất va chạm mã định danh và thiết kế bộ ca kiểm thử hiệu quả. Phép đếm không chỉ trả lời câu hỏi "có bao nhiêu cách", mà còn giúp định lượng quy mô thực sự của một bài toán.

## Phần 1: Pascal, Fermat và bài toán cờ bạc năm 1654

### Một tranh chấp nhỏ mở ra lĩnh vực lớn

Năm 1654, Blaise Pascal và Pierre de Fermat trao đổi thư từ để giải quyết một bài toán cờ bạc nổi tiếng: làm thế nào chia tiền cược công bằng khi ván chơi buộc phải dừng giữa chừng. Đây không chỉ là một câu đố giải trí, mà buộc họ phải đếm một cách có hệ thống tất cả các diễn biến có thể xảy ra trong tương lai. Từ cuộc trao đổi này, tổ hợp học và lý thuyết xác suất hiện đại bắt đầu định hình.

### Phép đếm như công cụ khắc phục trực giác sai

Trực giác của con người thường đánh giá rất kém những tình huống mà số trường hợp tăng nhanh theo hàm mũ hoặc giai thừa. Pascal và Fermat cho thấy rằng để đánh giá rủi ro một cách nghiêm túc, ta phải đếm chính xác thay vì phỏng đoán — tinh thần mà khoa học máy tính sau này kế thừa trực tiếp.

![Blaise Pascal — nhà toán học Pháp](/discrete-mathematics-for-computer-science-iuh/img/course/Blaise_Pascal_Versailles.JPG)

<p class="textbook-figure-caption" data-figure="7.25">Blaise Pascal — từ một bài toán chia tiền cược, ông đặt nền tảng cho lý thuyết đếm dùng trong khoa học dữ liệu và an ninh hiện đại.</p>
![Pierre de Fermat — đồng sáng lập xác suất](/discrete-mathematics-for-computer-science-iuh/img/course/Pierre_de_Fermat.jpg)

<p class="textbook-figure-caption" data-figure="7.26">Pierre de Fermat — cùng Pascal trao đổi thư về bài toán chia tiền cược, mở ra xác suất và tổ hợp hiện đại.</p>
---

## Phần 2: Bảo mật mật khẩu — đếm không gian khóa

### Độ mạnh mật khẩu trước hết là bài toán đếm

Một mật khẩu dài $$n$$ ký tự, trong đó mỗi vị trí được chọn độc lập từ bảng $$a$$ ký tự (theo quy tắc nhân ở bài `07_01`), tạo ra không gian mật khẩu có kích thước:

<div class="textbook-equation" markdown="1">
$$
\lvert \text{Passwords} \rvert = a^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ mật khẩu dài 8 ký tự** với hai chính sách phổ biến trong ứng dụng web:

| Chính sách | $$a$$ | Kích thước không gian | Entropy $$\approx n\log_2 a$$ |
|:---|:---:|:---|:---|
| Chữ thường + chữ số | 36 | $$36^8 \approx 2.8 \times 10^{12}$$ | $$\approx 41.4$$ bit |
| Chữ hoa + thường + số + ký hiệu | 77 | $$77^8 \approx 1.2 \times 10^{15}$$ | $$\approx 50.1$$ bit |

Nếu chỉ dùng chữ thường, không gian chỉ còn $$26^8 \approx 2.1 \times 10^{11}$$ ($$\approx 37.6$$ bit). Như vậy, phép đếm định lượng trực tiếp **chi phí tấn công vét cạn (brute-force)** theo số lần thử tối đa và trung bình.

### Không gian lớn chưa chắc đã đủ an toàn

Con số $$26^8$$ nghe có vẻ rất lớn, nhưng với năng lực tính toán của GPU hiện đại và các kỹ thuật bẻ khóa tối ưu, không gian đó vẫn có thể bị duyệt qua trong nhiều bối cảnh thực tế. Vì thế, kích thước không gian khóa luôn phải được đánh giá cùng tốc độ thử của kẻ tấn công, cơ chế giới hạn tốc độ (rate limiting), thuật toán băm mật khẩu và chính sách xác thực.

### Entropy và tư duy tổ hợp

**Entropy** (tính theo bit) đo logarit cơ số 2 của kích thước không gian khả năng:

<div class="textbook-equation" markdown="1">
$$
H \approx \log_2(a^n) = n \log_2 a.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mật khẩu được sinh ngẫu nhiên đều trên toàn bộ không gian mới đạt đúng $$H$$ bit entropy. Ngược lại, mật khẩu dựa trên từ điển hoặc khuôn mẫu quen thuộc (`123456`, `password`) làm thu hẹp không gian tìm kiếm **thực tế** xuống nhỏ hơn rất nhiều.

<div class="content-box warning-box textbook-block" markdown="1">
**Lưu ý**: Chính sách yêu cầu “ít nhất 2 trong 4 loại ký tự” **không** có kích thước $$77^8$$ mà phải tính bằng nguyên lý bù trừ (bài `07_03`). Các ràng buộc phức tạp không thể quy giản thành phép nhân $$a^n$$ đơn thuần.
</div>

![Không gian mật khẩu: L vị trí, mỗi vị trí N ký tự, tổng cộng N^L chuỗi](/discrete-mathematics-for-computer-science-iuh/img/course/password_entropy.svg)

<p class="textbook-figure-caption" data-figure="7.27">Với bảng chữ cái cỡ $N$ và mật khẩu dài $L$ ký tự, có đúng $N^L$ chuỗi. Entropy $H = L \cdot \log_2 N$ bit đo độ lớn không gian mà kẻ tấn công phải duyệt khi vét cạn.</p>
### Ước lượng thời gian brute-force

Giả sử kẻ tấn công thử được $$R$$ mật khẩu mỗi giây (tấn công ngoại tuyến khi hàm băm yếu bị lộ). Thời gian trung bình để duyệt qua một nửa không gian là:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{a^n / 2}{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ**: Với không gian $$36^8$$ và tốc độ $$R = 10^9$$ lần thử/giây:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{1.4 \times 10^{12}}{10^9} \approx 1{,}400\ \text{s} \approx 23\ \text{phút}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Khi kết hợp bcrypt/Argon2, muối (salt) và giới hạn tốc độ trên máy chủ, giá trị $$R$$ thực tế thấp hơn nhiều; ước lượng trên đóng vai trò là **trường hợp xấu nhất** khi cơ sở dữ liệu băm bị rò rỉ.

```python
import math
a, n = 36, 8
space = a ** n
entropy_bits = n * math.log2(a)
print(space, entropy_bits)  # ~2.8e12, ~41.4
```

### Mã PIN và mã xác nhận email

Nhiều cơ chế xác thực hằng ngày cũng có mô hình $$a^n$$ nhưng với độ dài $$n$$ nhỏ hơn mật khẩu thông thường.

| Loại mã | Ngữ cảnh | $$a$$ | $$n$$ | Kích thước không gian | Entropy $$\approx$$ |
|:---|:---|:---:|:---:|:---|:---:|
| PIN 6 số | ATM, OTP SMS | 10 | 6 | $$10^6$$ | $$\approx 20$$ bit |
| Mã email base36 | Xác nhận đăng ký, đặt lại mật khẩu | 36 | 6 | $$36^6 \approx 2.2 \times 10^9$$ | $$\approx 31$$ bit |

**PIN 6 số** ($$10^6 = 1{,}000{,}000$$) có entropy thấp, chỉ khoảng $$6 \log_2 10 \approx 19.9$$ bit. Nếu hệ thống **không khóa** sau vài lần nhập sai và không giới hạn tốc độ truy vấn, kẻ tấn công có thể vét cạn trực tuyến trong thời gian:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{10^6 / 2}{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với $$R \approx 3.3 \times 10^3$$ lần thử/giây (khi API không giới hạn tốc độ), việc duyệt một nửa không gian chỉ mất **khoảng 2,5 phút** (và duyệt toàn bộ $$10^6$$ khả năng mất khoảng 5 phút). Do đó, ATM và OTP SMS luôn **khóa sau 3–5 lần sai** hoặc giới hạn theo địa chỉ IP để bù đắp cho không gian khóa nhỏ.

**Mã xác nhận email 6 ký tự base36** (chữ thường và chữ số `0-9a-z`):

<div class="textbook-equation" markdown="1">
$$
36^6 = 2{,}176{,}782{,}336 \approx 2.2 \times 10^9,
\qquad
H \approx 6 \log_2 36 \approx 31\ \text{bit}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Không gian này lớn hơn PIN 6 số khoảng $$36^6 / 10^6 \approx 2{,}177$$ lần, nhưng vẫn **nhỏ hơn nhiều** so với mật khẩu 8 ký tự ($$36^8$$). Vì vậy mã email thường được thiết lập **hết hạn ngắn** (5–15 phút) và chỉ **dùng một lần**; rủi ro chính nằm ở việc tài khoản email bị chiếm quyền hoặc API xác thực thiếu cơ chế giới hạn tốc độ.

<div class="content-box insight-box textbook-block" markdown="1">
**So sánh nhanh**: Mã PIN có không gian $$10^6$$ nên dễ bị vét cạn nếu không khóa sau vài lần sai. Mã email base36 có không gian $$36^6 \approx 2.2 \times 10^9$$ (lớn hơn khoảng 2.200 lần), nhưng vẫn cần thời hạn hiệu lực (TTL) và giới hạn tốc độ.
</div>

### Session ID và rủi ro va chạm

**Session ID** là giá trị ngẫu nhiên ánh xạ người dùng với trạng thái phiên trên máy chủ (lưu ở cookie `sessionid`, Redis hoặc cơ sở dữ liệu). Mỗi mã phiên được chọn từ không gian $$N = 2^b$$ (hoặc $$a^n$$ nếu mã hóa theo chuỗi ký tự).

| Cách sinh mã | Không gian $$N$$ | Ghi chú |
|:---|:---|:---|
| `crypto.randomBytes(16)` (128 bit) | $$2^{128}$$ | Chuẩn cho môi trường vận hành |
| UUID v4 (122 bit ngẫu nhiên) | $$\approx 2^{122}$$ | Phổ biến |
| 32-bit `rand()` / dấu thời gian | $$2^{32}$$ | **Không dùng** cho phiên đăng nhập |

**Hai góc nhìn đếm** (xem thêm bài `08_01`, `08_03`):

- **Nguyên lý chuồng bồ câu**: khi có hơn $$N$$ phiên hoạt động đồng thời, **chắc chắn** có ít nhất hai phiên trùng ID.
- **Nghịch lý sinh nhật (Birthday paradox)**: chỉ cần khoảng $$\sqrt{N}$$ phiên đồng thời là xác suất xuất hiện một **cặp** trùng nhau đã tiến gần 50%.

Chẳng hạn, với ID 64-bit, ngưỡng sinh nhật chỉ khoảng $$2^{32} \approx 4 \times 10^9$$; còn với ID 128-bit, ngưỡng này là $$2^{64}$$, đủ an toàn cho các ứng dụng web thông thường.

**Hệ quả lập trình**: nếu hai người dùng nhận cùng một khóa phiên, dữ liệu phiên sẽ bị ghi đè và dẫn đến **chiếm quyền tài khoản (account hijack)**. Không bao giờ dùng `Math.random()`, bộ đếm tăng dần hay `userId` làm session ID.

```python
# Python — đủ entropy
import secrets
session_id = secrets.token_hex(16)  # 128 bit
```

### CSRF token và rủi ro va chạm

**CSRF token** được gắn vào biểu mẫu hoặc yêu cầu HTTP để máy chủ xác minh yêu cầu xuất phát từ trang hợp lệ thay vì từ trang giả mạo khác. Giá trị này cũng được sinh từ không gian $$N$$ và thường lưu trong phiên hoặc ký bằng HMAC.

| Cách triển khai | Mức độ rủi ro |
|:---|:---|
| `secrets.token_hex(16)` cho mỗi form | $$N = 2^{128}$$, rủi ro va chạm không đáng kể |
| Token 6 chữ số `rand() % 10^6` | $$N = 10^6$$ — vài trăm form đồng thời đã có rủi ro va chạm sinh nhật |
| Dùng lại một token cho cả phiên | Phạm vi bảo vệ hẹp hơn, dễ bị lộ qua các tab cũ |

Xác suất xuất hiện ít nhất một cặp trùng nhau trong $$k$$ biểu mẫu đồng thời với token 128-bit được xấp xỉ bởi:

<div class="textbook-equation" markdown="1">
$$
P(\text{collision}) \approx \frac{\binom{k}{2}}{2^{128}} \approx \frac{k^2}{2^{129}}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với $$k = 10^6$$ yêu cầu, xác suất này vẫn cực nhỏ. Ngược lại, với token 6 chữ số ($$N = 10^6$$), chỉ cần $$k \approx \sqrt{10^6} = 1000$$ là nguy cơ trùng lặp đã rất đáng kể.

<div class="content-box insight-box textbook-block" markdown="1">
**So sánh nhanh**: Với mật khẩu, tấn công vét cạn phải duyệt không gian $$a^n$$. Với Session ID hay CSRF token, kẻ tấn công chỉ cần đoán trúng một giá trị đang hoạt động, nên rủi ro lớn nhất là **va chạm (collision)** hoặc **entropy thấp**, chứ không chỉ là kích thước duyệt toàn bộ không gian.
</div>

---

## Phần 3: Đếm phép toán và ký hiệu Big-O

### Đánh giá tốc độ thuật toán bắt đầu từ phép đếm

Trước khi sử dụng ký hiệu tiệm cận Big-O, ta luôn bắt đầu bằng một câu hỏi cụ thể: thuật toán thực hiện bao nhiêu phép toán cơ bản khi dữ liệu đầu vào có kích thước `n`?

Ví dụ:

```python
for i in range(n):
    for j in range(n):
        total += 1
```

Trong đoạn mã trên, số lần tăng biến `total` là $$n^2$$. Nếu không đếm chính xác các bước cơ bản, ta khó hình dung đúng mức độ tăng trưởng của chi phí tính toán.

### Từ phép đếm chi tiết đến tư duy tiệm cận

Khi kích thước đầu vào rất lớn, các hằng số nhân nhỏ trở nên ít quan trọng hơn so với bậc tăng trưởng chính của hàm số. Ký hiệu Big-O không xuất hiện một cách tùy tiện mà được xây dựng trực tiếp từ việc đếm số thao tác cơ bản.

### Tầm quan trọng trong kỹ thuật phần mềm

Sự chênh lệch giữa độ phức tạp $$n \log n$$ và $$n^2$$ trong thực tế có thể quyết định:

- một truy vấn hoàn thành trong vài mili giây hay kéo dài nhiều phút,
- hệ thống mở rộng ổn định hay quá tải khi lưu lượng tăng,
- chi phí hạ tầng đám mây ở mức hợp lý hay tăng đột biến.

Vì vậy, phép đếm chính là điểm khởi đầu của kỹ thuật tối ưu hiệu năng (performance engineering).

![So sánh các lớp độ phức tạp](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="7.28">Đếm số thao tác là bước đầu giúp thấy rõ vì sao tốc độ của hai thuật toán có thể chênh lệch hoàn toàn khi dữ liệu lớn lên.</p>
![Các lớp độ phức tạp tính toán](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_classes.svg)

<p class="textbook-figure-caption" data-figure="7.29">Big-O phản ánh hàm tăng trưởng chính — sự khác biệt giữa $n \log n$ và $n^2$ quyết định khả năng mở rộng của hệ thống.</p>
---

## Phần 4: Va chạm hàm băm và nghịch lý sinh nhật

### Trực giác con người dễ ước lượng sai về va chạm

Nhiều người bất ngờ khi biết rằng chỉ trong một nhóm 23 người, xác suất có ít nhất hai người trùng ngày sinh đã vượt 50%. Hiện tượng này gọi là **nghịch lý sinh nhật (birthday paradox)** và có liên hệ trực tiếp với kỹ thuật băm dữ liệu.

### Va chạm là hệ quả tất yếu của phép đếm

Khi ánh xạ dữ liệu vào một số hữu hạn ngăn chứa (bucket), va chạm chắc chắn sẽ xảy ra nếu số lượng phần tử đủ lớn. Câu hỏi kỹ thuật quan trọng không phải là “có va chạm hay không”, mà là:

- va chạm xuất hiện sớm đến mức nào,
- xác suất va chạm là bao nhiêu,
- hệ thống có cơ chế xử lý và chịu tải đến đâu.

### Ứng dụng trong bảo mật

Trong mật mã học, **tấn công sinh nhật (birthday attack)** khai thác chính quy luật này để tìm hai đầu vào có cùng giá trị băm với chi phí thấp hơn nhiều so với tìm kiếm vét cạn thông thường. Điều đó cho thấy phép đếm không chỉ phục vụ tối ưu hiệu năng mà còn giúp đánh giá bề mặt tấn công của hệ thống bảo mật.

![Birthday paradox — va chạm sớm hơn trực giác](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="7.30">Nghịch lý sinh nhật giải thích vì sao va chạm băm xảy ra sớm hơn trực giác — chỉ cần khoảng $\sqrt{N}$ phần tử trong không gian $N$ ngăn chứa.</p>
---

## Phần 5: Kiểm thử tổ hợp và covering arrays

### Không thể kiểm thử mọi tổ hợp cấu hình

Một hệ thống phần mềm thực tế thường có rất nhiều tham số cấu hình kết hợp với nhau:

- nhiều trình duyệt,
- nhiều hệ điều hành,
- nhiều loại tài khoản người dùng,
- nhiều cờ bật/tắt tính năng,
- nhiều vùng dữ liệu khác nhau.

Nếu kiểm thử toàn bộ tích Descartes của các cấu hình này, số ca kiểm thử sẽ bùng nổ rất nhanh.

### Covering array là giải pháp cân bằng

Kiểm thử tổ hợp (combinatorial testing) dựa trên ý tưởng: thay vì kiểm thử mọi tổ hợp bậc cao, ta chọn một tập ca kiểm thử nhỏ hơn nhưng đảm bảo mọi tương tác từng cặp (2 chiều), bộ ba (3 chiều) hoặc bậc $$t$$ cho trước đều được bao phủ ít nhất một lần. Cấu trúc toán học đáp ứng yêu cầu đó gọi là **covering array**.

### Vì sao phương pháp này hiệu quả

Trong thực tế phát triển phần mềm, phần lớn lỗi phát sinh từ sự tương tác giữa một vài tham số (thường là 2 hoặc 3 yếu tố), hiếm khi đòi hỏi mọi tham số cùng nhận một tổ hợp đặc biệt. Nhờ tổ hợp học, ta có thể rút gọn đáng kể bộ ca kiểm thử trong khi vẫn duy trì khả năng phát hiện lỗi cao.

---

## Phần 6: Phép đếm trong các hệ thống quy mô lớn

Khi quy mô hệ thống ngày càng mở rộng, vai trò của phép đếm càng trở nên rõ nét trong nhiều bài toán:

- không gian tìm kiếm trong trí tuệ nhân tạo,
- không gian khóa trong bảo mật,
- không gian trạng thái trong kiểm chứng hình thức,
- không gian cấu hình trong hệ thống phân tán,
- không gian mẫu trong thực nghiệm và thống kê.

Không phải lúc nào ta cũng cần hoặc có thể tính ra con số chính xác tuyệt đối; nhiều khi chỉ cần một ước lượng tổ hợp đúng bậc độ lớn cũng đủ tránh được những quyết định thiết kế sai lầm.

---

## Kết luận

Từ bài toán chia tiền cược của Pascal và Fermat đến bẻ khóa mật khẩu, phân tích Big-O, nghịch lý sinh nhật và kiểm thử tổ hợp, phép đếm luôn xuất hiện ở những nơi cần định lượng quy mô của khả năng. Một hệ thống không chỉ gặp sự cố vì lỗi logic, mà nhiều khi còn thất bại vì không ai tính trước có bao nhiêu trường hợp có thể xảy ra.

---


## Ví dụ tính tay làm từng bước: So sánh mật khẩu 8 chữ thường vs. Passphrase 4 từ (XKCD)

Giả sử kẻ tấn công dùng dàn GPU thử được $$10^{10}$$ mật khẩu mỗi giây (10 tỷ lần/giây):
1. **Mật khẩu ngẫu nhiên 8 chữ cái thường** ($$N = 26,\; L = 8$$):
   - Kích thước không gian khóa: $$26^8 \approx 2.09 \times 10^{11}$$ tổ hợp.
   - Entropy: $$H = 8 \log_2(26) \approx 8 \times 4.70 = \mathbf{37.6\text{ bit}}$$.
   - Thời gian thử hết trung bình (50% không gian): $$\frac{2.09 \times 10^{11}}{2 \times 10^{10}} \approx \mathbf{10.4\text{ giây}}$$!
2. **Passphrase chọn ngẫu nhiên 4 từ tiếng Anh** từ từ điển $$N = 2048 = 2^{11}$$ từ ($$L = 4$$):
   - Kích thước không gian khóa: $$(2^{11})^4 = 2^{44} \approx 1.76 \times 10^{13}$$ tổ hợp.
   - Entropy: $$H = 4 \times 11 = \mathbf{44\text{ bit}}$$ (tăng lên 5 từ đạt $$55\text{ bit}$$, tức hơn **57 ngày** ở tốc độ 10 tỷ/giây — và nếu băm chậm bằng Argon2 ở $$10^4$$ lần/giây thì mất tới **57 triệu năm**!).

### Giải thích: 3 bước kiểm định độ an toàn của một mã bí mật bằng phép đếm
#### Bước 1: Tính không gian khóa THỰC TẾ, không phải lý thuyết
Một mật khẩu 8 ký tự có chữ hoa/thường/số/ký tự đặc biệt có không gian lý thuyết $$94^8 \approx 6\times 10^{15}$$, nhưng nếu người dùng chọn theo mẫu `Ten + NamSinh + !`, không gian thực tế tụt xuống chỉ còn vài triệu — kẻ tấn công dùng từ điển phá trong chưa đầy 1 giây!

#### Bước 2: Quy đổi sang bit entropy và chia cho tốc độ thử thực tế
Lấy $$H = \log_2(\vert\mathcal{K}_{\text{thực}}\vert)$$. So sánh tốc độ thử của hàm băm nhanh (MD5/SHA-256: $$10^{10}$$ lần/s trên GPU) với hàm băm chậm chuyên dụng (bcrypt/Argon2: $$10^3\text{–}10^4$$ lần/s) và giới hạn rate-limit mạng (ví dụ 5 lần/phút cho OTP 6 số).

#### Bước 3: Kiểm tra rủi ro va chạm sinh nhật cho ID không bí mật
Với `session_id` hay `CSRF token` $$b$$-bit, va chạm xảy ra sớm ở ngưỡng $$\approx 2^{b/2}$$ chứ không phải $$2^b$$ — nên chuẩn hiện đại luôn đòi hỏi ít nhất **128 bit ngẫu nhiên** (ngưỡng sinh nhật $$2^{64} \approx 1.8 \times 10^{19}$$)!

$$
\text{Không gian thực } \vert\mathcal{K}\vert
\;\xrightarrow{H = \log_2 \vert\mathcal{K}\vert}\;
\text{Bit entropy}
\;\xrightarrow{\div \text{Tốc độ thử}}\;
\text{Thời gian phá thực tế}.
$$

## Bài tập thực hành

### Bài tập 1: Mật khẩu

Một mật khẩu dài 8 ký tự, mỗi ký tự là chữ cái thường hoặc chữ số (36 khả năng). Hỏi có bao nhiêu mật khẩu khác nhau?

<details>
<summary>Đáp án</summary>

$36^8 \approx 2.8 \times 10^{12}$ mật khẩu.

</details>

### Bài tập 2: Birthday paradox

Với 23 người, xác suất có ít nhất 2 người cùng sinh nhật vào khoảng 50%. Hãy giải thích ngắn gọn vì sao con số này nhỏ hơn trực giác thông thường.

<details>
<summary>Đáp án</summary>

Vì số cặp người cần so sánh tăng theo $\binom{n}{2} = \frac{n(n-1)}{2}$ chứ không tăng tuyến tính theo $n$. Dùng công thức xấp xỉ $1 - e^{-n^2/(2d)}$ với $d=365$ và $n=23$, ta thu được xác suất xấp xỉ $0.5$.

</details>

### Bài tập 3: Kiểm thử tổ hợp

Có 5 tính năng, mỗi tính năng có 2 lựa chọn (bật/tắt). Có bao nhiêu cặp tổ hợp giá trị của 2 tính năng cần được kiểm tra?

<details>
<summary>Đáp án</summary>

Số cặp tính năng là $\binom{5}{2} = 10$. Mỗi cặp có $2 \times 2 = 4$ tổ hợp giá trị, nên tổng cộng có $10 \times 4 = 40$ cặp tổ hợp cần bao phủ (nếu kiểm thử riêng lẻ từng cặp cần 40 ca; còn khi dùng covering array, một ca kiểm thử phủ được nhiều cặp cùng lúc nên số ca thực tế nhỏ hơn nhiều).

</details>

### Bài tập 4: Entropy mật khẩu

So sánh entropy (tính theo bit) của mật khẩu dài 8 ký tự trong hai trường hợp: (a) $$a=36$$ và (b) $$a=77$$.

<details>
<summary>Đáp án</summary>

(a) $8 \log_2 36 \approx 41.4$ bit. (b) $8 \log_2 77 \approx 50.1$ bit. Chênh lệch khoảng $8.8$ bit, tương đương không gian khóa lớn hơn khoảng $2^{8.8} \approx 438$ lần ($(77/36)^8 \approx 438$).

</details>

### Bài tập 5: Session ID

Một hệ thống dùng Session ID ngẫu nhiên dài 64-bit. Khoảng bao nhiêu phiên hoạt động đồng thời thì xác suất xảy ra va chạm sinh nhật đạt mức đáng kể (~50%)?

<details>
<summary>Đáp án</summary>

Ngưỡng sinh nhật xấp xỉ $\sqrt{2^{64}} = 2^{32} \approx 4 \times 10^9$ phiên.

</details>

### Bài tập 6: CSRF token yếu

Một CSRF token gồm 6 chữ số ($$N = 10^6$$). Khi có 500 biểu mẫu hoạt động đồng thời, hãy xấp xỉ xác suất có ít nhất hai token trùng nhau.

<details>
<summary>Đáp án</summary>

$P \approx \binom{500}{2} / 10^6 = 124{,}750 / 10^6 \approx 0.12$ (12%) — mức rủi ro quá cao đối với hệ thống vận hành thực tế.

</details>

### Bài tập 7: PIN ATM

Mã PIN gồm 6 chữ số ($$10^6$$ khả năng). Nếu không khóa tài khoản và kẻ tấn công thử được $$R = 3.3 \times 10^3$$ lần/giây, hãy ước lượng thời gian brute-force trung bình (duyệt một nửa không gian).

<details>
<summary>Đáp án</summary>

$T \approx \dfrac{10^6/2}{3.3 \times 10^3} \approx 150$ giây $\approx$ **2,5 phút** cho một nửa không gian (và khoảng **5 phút** để duyệt toàn bộ $10^6$ khả năng). Trong thực tế, ATM khóa thẻ sau vài lần nhập sai.

</details>

### Bài tập 8: Mã email base36

Một mã xác nhận email gồm 6 ký tự base36. Tính kích thước không gian và entropy (bit). So với mã PIN 6 số, không gian này lớn hơn bao nhiêu lần?

<details>
<summary>Đáp án</summary>

$36^6 = 2{,}176{,}782{,}336 \approx 2.2 \times 10^9$; $H \approx 6 \log_2 36 \approx 31$ bit. Tỷ lệ $36^6 / 10^6 \approx 2{,}177$ — lớn hơn mã PIN 6 số gần **2.200 lần**.

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

- **Mật khẩu, PIN và mã OTP**: không gian $$a^n$$, entropy $$\approx n\log_2 a$$; PIN 6 số ($$10^6$$) yếu nếu không khóa sau vài lần sai, còn mã email base36 đạt $$36^6 \approx 2.2 \times 10^9$$.
- **Session ID và CSRF token**: không gian $$2^b$$; va chạm chắc chắn xảy ra theo nguyên lý Dirichlet hoặc xuất hiện sớm theo nghịch lý sinh nhật ($$\sim\sqrt{N}$$), nên cần dùng bộ sinh số ngẫu nhiên mật mã (CSPRNG) đủ bit.
- Tổ hợp và xác suất là công cụ định lượng rủi ro xuyên suốt từ mật khẩu, token web, kiểm thử phần mềm đến Big-O và va chạm hàm băm.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=XMriWTvPXHI">The mathematical secrets of Pascal’s triangle - Wajdi Mohamed Ratemi</a> — TED-Ed, tiếng Anh. Giới thiệu tổ hợp qua tam giác Pascal, gắn với bối cảnh lịch sử thế kỷ XVII trong bài.
- <a href="https://www.youtube.com/watch?v=jsraR-el8_o">Hash Collisions &amp; The Birthday Paradox - Computerphile</a> — Computerphile, tiếng Anh. Va chạm hàm băm và nghịch lý sinh nhật, khớp với phần an ninh mạng của bài.
- <a href="https://www.youtube.com/watch?v=a2ey9a70yY0">23 and Football Birthdays - Numberphile</a> — Numberphile, tiếng Anh. Minh họa ngắn gọn về nghịch lý sinh nhật cùng mô hình đếm va chạm.
