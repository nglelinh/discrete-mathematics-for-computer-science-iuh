---
layout: post
title: "Lý thuyết Số: Từ Euclid đến Blockchain"
categories: chapter15
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Bài khảo sát tổng hợp Chương 15: từ Euclid và Gauss đến RSA, HTTPS, hàm băm, mã Reed–Solomon, chứng minh không tiết lộ thông tin (zero-knowledge), blockchain và hậu lượng tử."
---

> **Câu chuyện mở đầu:** Ít có câu chuyện nào trong lịch sử khoa học kịch tính như cú lật kèo của Lý thuyết Số: năm 1940, nhà toán học lừng danh G. H. Hardy từng viết đầy tự hào rằng *"chưa ai từng tìm ra ứng dụng thực tế nào cho lý thuyết số"*. Chỉ 37 năm sau, RSA ra đời; và đến thế kỷ XXI, chính các đường cong elliptic, bài toán logarit rời rạc và cây băm Merkle đã trở thành **xương sống niềm tin của toàn bộ Internet, thương mại điện tử và Blockchain**!

<div class="textbook-epigraph" markdown="1">

"Number theory is the purest mathematics — and now the quiet machinery of the Internet."

<span class="epigraph-attribution">— Tinh thần bài khảo sát 15.5</span>

</div>

Các bài trước trong Chương 15 đã lần lượt trình bày tính chia hết, đồng dư, RSA/Diffie–Hellman và các ứng dụng hệ thống. Bài bổ sung này **tổng hợp tiến trình phát triển** từ Euclid và Gauss đến hạ tầng HTTPS, hàm băm, mã sửa lỗi, chứng minh không tiết lộ thông tin (*zero-knowledge*) và blockchain, nhằm làm rõ mối liên hệ giữa các khái niệm thay vì lặp lại chi tiết kỹ thuật của các mục 15.1–15.4.

![Blockchain](/discrete-mathematics-for-computer-science-iuh/img/course/Blockchain.svg)

<p class="textbook-figure-caption" data-figure="15.8">Blockchain kết hợp hàm băm, chữ ký số và cơ chế đồng thuận — điểm giao nhau giữa lý thuyết số và hệ phân tán.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** mạch phát triển từ Euclid đến Gauss và tới RSA/Diffie–Hellman.
- **Giải thích** vai trò của hàm băm và chữ ký số trong blockchain ở mức khái niệm.
- **Mô tả** chính xác khái niệm *zero-knowledge proof* trong một câu.
- **Đặt** thách thức máy tính lượng tử và mật mã hậu lượng tử (PQC) vào bức tranh chung của chương.

**Từ khóa**: Euclid, Gauss, RSA, HTTPS, blockchain, ECDSA, zero-knowledge, post-quantum.

</div>

## Bản đồ kiến thức nền: Dòng chảy 2.300 năm từ Euclid đến Blockchain

### 1. Từ Euclid (300 TCN) đến Gauss (1801)
- **Euclid:** Chứng minh vô hạn số nguyên tố và thuật toán GCD.
- **Fermat, Euler, Gauss:** Xây dựng hệ thống đồng dư $$\mathbb{Z}_m$$, định lý Fermat–Euler và luật thuận nghịch bậc hai — đặt sẵn toàn bộ vũ khí đại số trước khi máy tính ra đời gần 200 năm!

### 2. Hai bài toán Khó tạo nên An ninh Internet
- **Phân tích thừa số nguyên tố (RSA):** Dễ nhân $$p\cdot q$$, khó tách $$n$$.
- **Logarit rời rạc (Diffie–Hellman, ECC/ECDSA):** Dễ tính $$g^a \bmod p$$, cực kỳ khó tìm lại $$a$$ từ $$g^a \bmod p$$!

### 3. Blockchain: Chuỗi Băm + Chữ ký Đường cong Elliptic (ECDSA)
- **Bản chất:** Mỗi khối trong Blockchain chứa **mã băm của khối trước đó** (tạo chuỗi bất biến: sửa 1 bit quá khứ làm hỏng toàn bộ chuỗi sau!), và mỗi giao dịch được ký bằng **chữ ký số đường cong elliptic** (như `secp256k1` trong Bitcoin/Ethereum) giúp mọi nút mạng xác minh mà không cần ngân hàng trung ương!

## Ví dụ tính tay cầm tay chỉ việc: Trao đổi khóa Diffie–Hellman trên $$p = 23,\; g = 5$$

Công bố công khai số nguyên tố $$p = 23$$ và phần tử sinh $$g = 5$$ (kẻ nghe lén Eve biết rõ cả $$23$$ và $$5$$!):
1. **Alice** chọn bí mật $$a = 6$$, tính và gửi công khai:
   $$
   A = 5^6 \bmod 23 = (5^3)^2 \bmod 23 = 125^2 \bmod 23 \equiv 10^2 = 100 \equiv 8 \pmod{23}.
   $$
2. **Bob** chọn bí mật $$b = 15$$, tính và gửi công khai:
   $$
   B = 5^{15} \bmod 23 = (5^6)^2 \cdot 5^3 \equiv 8^2 \cdot 10 = 640 = 27\cdot 23 + 19 \equiv 19 \pmod{23}.
   $$
3. **Tính khóa bí mật chung (không hề truyền qua mạng!):**
   - **Alice** tính từ $$B = 19$$: $$K_A = 19^6 \bmod 23 \equiv (-4)^6 = 4096 = 178\cdot 23 + 2 \equiv 2 \pmod{23}$$!
   - **Bob** tính từ $$A = 8$$: $$K_B = 8^{15} \bmod 23 = (8^3)^5 \equiv 512^5 \equiv 6^5 = 7776 = 338\cdot 23 + 2 \equiv 2 \pmod{23}$$!

Cả hai cùng thu được **khóa chung $$K = 2$$** ngay trước mắt kẻ nghe lén Eve (chỉ thấy $$23, 5, 8, 19$$)!

### Khung giải thích: 4 cột mốc biến Lý thuyết Số thành hạ tầng niềm tin số (nên đọc chậm)

#### Bước 1: Sự ra đời của Hàm một chiều (1976)
Diffie–Hellman chứng minh hai người lạ hoàn toàn có thể thiết lập bí mật chung trên kênh công khai nhờ độ khó của logarit rời rạc.

#### Bước 2: RSA & Cơ sở hạ tầng Khóa Công khai PKI (1977–1990s)
Kết hợp mã hóa khóa công khai và chữ ký số mở đường cho TLS/HTTPS và thương mại điện tử toàn cầu.

#### Bước 3: Đường cong Elliptic ECC — Cùng độ an toàn, khóa ngắn gấp 10 lần
Khóa ECC 256-bit có độ bảo mật tương đương khóa RSA 3072-bit — tối ưu hoàn hảo cho thiết bị di động, IoT và giao dịch Blockchain.

#### Bước 4: Chuẩn bị cho kỷ nguyên Lượng tử
Lịch sử tiếp tục lặp lại: khi máy tính lượng tử đe dọa RSA/ECC, các nhà toán học lại tìm thấy pháo đài mới trong **Lý thuyết Mạng tinh thể (Lattice)** ở bài 15.06!

$$
\text{Euclid / Gauss}
\;\xrightarrow{\;\text{Hàm một chiều}\;}\;
\text{Diffie–Hellman \& RSA}
\;\xrightarrow{\;\text{ECC + SHA-256}\;}\;
\text{HTTPS \& Blockchain}.
$$

## Từ Euclid đến Gauss

Euclid (~300 TCN) để lại thuật toán tìm ước chung lớn nhất và chứng minh có vô hạn số nguyên tố — hai kết quả cốt lõi ở Mục 15.1. Ý nghĩa sâu xa không chỉ nằm ở việc có vô hạn số nguyên tố, mà ở chỗ xác lập số nguyên tố là **đơn vị cấu tạo cơ bản** của số học.

Gauss (1777–1855), thông qua tác phẩm *Disquisitiones Arithmeticae* (1801), đã đưa **quan hệ đồng dư** trở thành ngôn ngữ chuẩn mực của lý thuyết số. Hầu hết các giao thức ở Mục 15.2–15.3 đều được diễn đạt bằng chính ngôn ngữ này: $$a\equiv b\pmod n$$, các lớp thặng dư và hàm phi Euler $$\varphi$$.

## RSA và an ninh Internet

RSA khai thác sự **bất đối xứng về độ khó tính toán**: nhân hai số nguyên tố lớn rất dễ, nhưng phân tích tích $$n=pq$$ thành hai thừa số ban đầu lại rất khó trên máy tính cổ điển. Mật mã khóa công khai từ đó cho phép:

- công bố khóa mã hóa rộng rãi,
- giữ riêng khóa giải mã,
- xây dựng chữ ký số và hạ tầng khóa công khai (PKI).

Giao thức HTTPS/TLS, ký số phần mềm và bảo mật email đều dựa trên mô hình này, dù các triển khai hiện đại thường kết hợp thêm ECDHE, AES và nhiều thành phần khác. Người dùng cuối không cần trực tiếp thấy các phép tính modulo, nhưng hạ tầng mạng không thể vận hành an toàn nếu thiếu chúng.

## Hàm băm và phép modulo trong thực hành

Biểu thức quen thuộc trong lập trình:

```python
index = hash(key) % table_size
```

là ứng dụng trực tiếp của số học modulo trong kỹ thuật phần mềm hằng ngày. Dù hàm băm mật mã (như SHA-256) phức tạp hơn nhiều, trực giác về **lớp thặng dư**, hiện tượng quay vòng (*wrap-around*) và phân bố bucket vẫn rất hữu ích. Do máy tính biểu diễn số bằng các từ có độ dài bit hữu hạn, nhiều phép toán số học phần cứng vốn đã hoạt động theo modulo $$2^w$$.

## Mã sửa lỗi và Reed–Solomon

Khi truyền tải hoặc lưu trữ, dữ liệu luôn có nguy cơ gặp nhiễu. **Mã Reed–Solomon** và các họ mã sửa lỗi liên quan sử dụng đại số trên **trường hữu hạn** (một cấu trúc số học mở rộng) để phát hiện và sửa lỗi trên đĩa CD/DVD, mã QR, hệ thống lưu trữ phân tán và thông tin vệ tinh. Như vậy, lý thuyết số và đại số hữu hạn không chỉ phục vụ bảo mật như RSA mà còn đảm bảo **độ tin cậy** của dữ liệu.

## Zero-knowledge và blockchain

**Chứng minh không tiết lộ thông tin (*zero-knowledge proof*)** cho phép một bên chứng minh rằng một mệnh đề là đúng (hoặc mình nắm giữ một bí mật) mà **không tiết lộ** bất kỳ thông tin nào về bản thân bí mật đó. Các biến thể như zk-SNARK và zk-STARK đã đưa ý tưởng này vào nhiều hệ thống phi tập trung.

Ở mức tổng quan, **blockchain** là chuỗi các khối được liên kết bằng hàm băm; các giao dịch được **ký số** (theo cơ chế ECDSA hoặc tương tự RSA), còn cơ chế đồng thuận quyết định chuỗi hợp lệ. Số nguyên tố, phép toán modulo và đường cong elliptic xuất hiện trong chữ ký số, trong khi hàm băm đảm bảo tính toàn vẹn của liên kết giữa các khối. Mục này không thay thế một giáo trình chuyên sâu về blockchain, mà chỉ chỉ rõ những điểm lý thuyết số gắn trực tiếp vào kiến trúc hệ thống.

## Lượng tử và hậu lượng tử

Thuật toán Shor đe dọa RSA cũng như nhiều hệ dựa trên DLP và ECC cổ điển. Hướng giải quyết không phải là từ bỏ lý thuyết số, mà là **chuyển sang những bài toán nền tảng mới** (mạng tinh thể, mã sửa lỗi, hàm băm, …) như đã nêu ở Mục 15.4. Bảo mật dài hạn về bản chất vẫn là một bài toán toán học.

## Kết luận chương

| Mốc | Ý tưởng chính | Vị trí trong khóa học |
|:---|:---|:---|
| Euclid | GCD, vô hạn số nguyên tố | 15.1 |
| Gauss | Quan hệ đồng dư | 15.2 |
| RSA / DH | Mật mã khóa công khai | 15.3 |
| Hash, LCG, CRT, ECC, PQC | Ứng dụng hệ thống | 15.4 |
| Blockchain / ZK | Hệ phân tán và quyền riêng tư | 15.5 (khảo sát) |

Tiến trình từ Euclid đến blockchain minh họa một quy luật phổ biến của khoa học cơ bản: những kết quả toán học thuần túy có thể trở thành nền tảng hạ tầng kỹ thuật sau nhiều thế kỷ.

## Bài tập

### Bài tập 1

Tính $$\gcd(48,18)$$ bằng thuật toán Euclid.

<details>
<summary>Đáp án</summary>

$$48=2\cdot 18+12$$, $$18=1\cdot 12+6$$, $$12=2\cdot 6+0$$, suy ra $$\gcd(48,18)=6$$.

</details>

### Bài tập 2

Cho $$p=5$$, $$q=11$$, $$e=3$$. Tính $$n$$ và một giá trị $$d$$ hợp lệ.

<details>
<summary>Đáp án</summary>

Ta có $$n=55$$, $$\varphi(n)=40$$ và $$d=27$$ vì $$3\cdot 27=81\equiv 1\pmod{40}$$.

</details>

### Bài tập 3

Nêu ngắn gọn trong một câu vai trò của phép modulo hoặc số nguyên tố trong chữ ký số trên blockchain.

<details>
<summary>Đáp án</summary>

Chữ ký số (ECDSA hoặc tương tự RSA) sử dụng phép lũy thừa hoặc phép toán nhóm trên trường hữu hạn/đường cong elliptic, trong đó nghịch đảo modulo cùng độ khó của DLP hoặc phân tích thừa số giúp bảo vệ khóa riêng, còn hàm băm dùng để liên kết các khối và băm thông điệp trước khi ký.

</details>

## Tóm tắt

Lý thuyết số — từ tính chia hết và đồng dư đến RSA, hàm băm, mã sửa lỗi và chữ ký số — đóng vai trò nền tảng cho bảo mật và nhiều hệ phân tán hiện đại. Chương 15 khép lại bằng cái nhìn tổng hợp này; Chương 16 sẽ tiếp tục với **cây**, một cấu trúc dữ liệu và toán rời rạc quan trọng khác.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=cOwyHTiW4KE">EUCLIDEAN ALGORITHM - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Ôn lại thuật toán Euclid, điểm khởi đầu của tiến trình lịch sử trong bài.
- <a href="https://www.youtube.com/watch?v=JD72Ry60eP4">Prime Numbers &amp; RSA Encryption Algorithm - Computerphile</a> — Computerphile, tiếng Anh. Hệ mật RSA, chặng phát triển của mật mã khóa công khai trước hạ tầng mạng hiện đại.
- <a href="https://www.youtube.com/watch?v=bBC-nXj3Ng4">But how does bitcoin actually work?</a> — 3Blue1Brown, tiếng Anh. Giải thích cách Bitcoin sử dụng hàm băm và chữ ký số, tương ứng với phần blockchain ở cuối bài.
