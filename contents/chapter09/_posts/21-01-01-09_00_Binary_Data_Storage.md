---
layout: post
title: "Dữ liệu nhị phân trong máy tính: Từ bit đến bộ nhớ"
categories: chapter09
date: 2021-01-01
order: 0
required: true
lang: en
excerpt: "Khảo sát cách máy tính lưu trữ và diễn giải dữ liệu ở mức nhị phân — từ bit, byte, hệ nhị phân, hexadecimal đến cách chương trình gán ý nghĩa cho dãy byte trong RAM."
---

<div class="textbook-epigraph" markdown="1">

"There is no such thing as plain text."

<span class="epigraph-attribution">— Joel Spolsky</span>

</div>


Mở một bức ảnh PNG, một bài hát MP3 và một tệp văn bản trong trình soạn thảo hex (hex editor), bạn sẽ thấy một sự thật làm thay đổi cách nhìn về máy tính: **bên trong RAM, không hề tồn tại "chữ cái", "màu sắc" hay "âm thanh"** — tất cả chỉ là một dãy vô tận các công tắc điện 0 và 1 được gom thành từng ô **8 bit (1 byte)** gắn địa chỉ!

Chính chương trình đọc bộ nhớ mới là kẻ "phiên dịch" xem cùng một byte `01000001` (`0x41`) là số nguyên `65`, chữ cái `'A'`, một sắc độ màu xám, hay một lệnh CPU. Bài học mở màn Chương 9 này bắt đầu từ bit, byte, hệ nhị phân–thập lục phân (hex) cho tới word 32/64-bit.

**Mạch bài học:** Kiến thức cần nhớ (biểu diễn vị trí cơ số 2 & 16, đơn vị byte & địa chỉ RAM, tính đa nghĩa của dữ liệu thô) → Bit, Byte, Nhị phân, Hex & Word → Ví dụ tính tay làm từng bước: đổi `0xCA` giữa Nhị phân–Thập phân–Hex và kiểm tra 3 cách diễn giải `0x41` → Giải thích: 3 bước đọc bất kỳ chuỗi hex dump nào trong 10 giây → Công cụ tương tác & Bài tập.

## Kiến thức cần nhớ: Biểu diễn Dữ liệu Nhị phân trong Hệ thống Máy tính

### 1. Hệ đếm vị trí cơ số 2 và cơ số 16 (Hex)
Mỗi bit $$b_i \in \{0, 1\}$$ đóng góp giá trị $$b_i \cdot 2^i$$. Vì $$16 = 2^4$$, **mỗi chữ số thập lục phân (0–9, A–F) tương ứng chính xác 1–1 với đúng 4 bit (1 nibble)** — giúp 1 byte 8 bit luôn viết gọn thành đúng 2 ký tự hex (từ `0x00` đến `0xFF`)!

### 2. RAM là một mảng byte đánh địa chỉ (Byte-Addressable Memory)
Bộ nhớ máy tính không định địa chỉ từng bit lẻ mà định địa chỉ từng **byte** (8 bit, chứa $$2^8 = 256$$ trạng thái từ $$0$$ đến $$255$$). Một kiểu dữ liệu lớn hơn (như `int32` = 4 byte, `double` = 8 byte) đơn giản là 4 hoặc 8 ô byte liên tiếp nhau trong RAM.

### 3. Dữ liệu thô + Kiểu dữ liệu (Type) = Ý nghĩa
Cùng một chuỗi 4 byte trong RAM có thể là một số nguyên 32-bit, một số thực dấu phẩy động IEEE 754, 4 ký tự ASCII, hay 1 pixel màu RGBA! Hiểu nguyên lý này là chìa khóa cho mọi bài học tiếp theo trong Chương 9 (Unicode, Endianness, Two's complement).

Trong chương này, chúng ta khảo sát cách máy tính **lưu trữ và diễn giải** dữ liệu ở mức nhị phân — nền tảng cho mọi lớp phần mềm phía trên. Ở Chương 1, logic mệnh đề đã giới thiệu biến Boole với hai giá trị $$0$$ và $$1$$; mục này trả lời câu hỏi kế tiếp: **bit đó nằm ở đâu, được gom thành khối như thế nào, và vì sao cùng một byte có thể vừa là chữ `A` vừa là số 65?** Câu trả lời bắt đầu từ đơn vị nhỏ nhất là **bit**, rồi mở rộng sang byte, hệ nhị phân, hệ thập lục phân (hexadecimal) và cách chương trình gán ý nghĩa cho dãy byte thô trong RAM.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Bits_and_Bytes.svg"
       alt="Quan hệ bit và byte — 8 bit ghép thành 1 byte, các đơn vị lưu trữ lớn hơn gom từ byte"
       width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 9.0a: 8 bit = 1 byte; các đơn vị KB, MB, GB… được gom từ byte. Bit không tự biết mình là chữ hay số — chương trình mới quyết định cách đọc (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Bits_and_Bytes.svg">Fcarmody / Wikimedia Commons</a>, CC BY-SA 4.0).</figcaption>
</p>
</figure>

## Bit — đơn vị nhỏ nhất

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Bit** (binary digit) là đơn vị thông tin nhỏ nhất trong máy tính kỹ thuật số. Mỗi bit chỉ nhận **hai trạng thái**: $$0$$ hoặc $$1$$.
</div>

Trong phần cứng, hai trạng thái này thường tương ứng với điện áp thấp/cao, hai chiều từ trường, hoặc rãnh đóng/mở trên đĩa quang. Ở tầng lập trình, ta có thể xem mỗi bit như một biến Boole $$x \in \{0,1\}$$ như đã giới thiệu ở Chương 1.

**Ký hiệu**: Một bit được viết là $$b \in \{0,1\}$$. Một chuỗi $$n$$ bit được viết là $$b_{n-1} b_{n-2} \ldots b_1 b_0$$, trong đó $$b_{n-1}$$ là **bit cao nhất** (MSB) và $$b_0$$ là **bit thấp nhất** (LSB).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- Công tắc đèn: tắt = 0, bật = 1.
- Biến `bool logged_in` trong C++: `false` thường được lưu dưới dạng byte toàn 0, `true` là 1. Dù chỉ cần **một bit** thông tin, ngôn ngữ lập trình vẫn thường cấp phát cả một byte vì RAM được địa chỉ hóa theo byte.
</div>

<div class="content-box insight-box textbook-block" markdown="1">
Máy tính **không** trực tiếp lưu chữ “42” hay ký tự “A”, mà lưu **mẫu bit**. Chữ và số là cách **con người và chương trình diễn giải** mẫu bit đó — tương tự nốt nhạc trên khuông: cùng một ký hiệu, nhưng các nhạc cụ khác nhau tạo ra âm thanh khác nhau.
</div>

## Byte — nhóm tám bit

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Byte** là một nhóm gồm **8 bit** liền kề, đồng thời là đơn vị địa chỉ hóa phổ biến nhất của bộ nhớ máy tính hiện đại.
</div>

**Ký hiệu**: Khi đọc dưới dạng số nguyên **không dấu** (unsigned), một byte biểu diễn được các giá trị từ $$0$$ đến $$2^8 - 1 = 255$$. Chẳng hạn, byte `01000001` (nhị phân) bằng $$64 + 1 = 65$$ (thập phân) và viết gọn là `0x41` (hex).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- Chữ `A` trong ASCII/UTF-8 chiếm một byte `0x41`.
- Màu đỏ trong ảnh RGB thường được lưu bằng ba byte liên tiếp: `FF 00 00`.
- Kiểu `int` 32-bit trên hầu hết máy tính để bàn chiếm **4 byte** liền kề trong RAM.
</div>

**Tính chất**: Với 8 bit, tổng số tổ hợp khác nhau là $$2^8 = 256$$. Nhờ vậy, một byte đủ chứa toàn bộ ký tự Latin cơ bản trong bảng ASCII (128 ký tự đầu từ 0 đến 127), đồng thời trở thành đơn vị cơ sở cho UTF-8, ảnh bitmap và gói tin mạng.

![Một ô nhớ chứa byte 0x12](/discrete-mathematics-for-computer-science-iuh/img/course/memory_byte_12.svg)

<p class="textbook-figure-caption" data-figure="9.0">Một địa chỉ bộ nhớ tương ứng với một byte gồm 8 bit. Ký hiệu hex `0x12` chỉ là cách viết gọn cho mẫu bit bên trong.</p>

## Hệ nhị phân — đếm bằng hai chữ số

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hệ nhị phân** (binary) là hệ đếm cơ số 2, trong đó mỗi vị trí bit có trọng số là một lũy thừa của 2.
</div>

**Ký hiệu**: Giá trị thập phân của chuỗi bit $$b_{k-1} \ldots b_0$$ là:

<div class="textbook-equation" markdown="1">
$$
N = \sum_{i=0}^{k-1} b_i \cdot 2^i
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

**Ví dụ** — chuyển `1101` (nhị phân) sang thập phân:

<div class="textbook-equation" markdown="1">
$$
1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 8 + 4 + 0 + 1 = 13
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Bảng đếm 4 bit đầu tiên:

| Thập phân | Nhị phân |
|:---:|:---:|
| 0 | `0000` |
| 1 | `0001` |
| 2 | `0010` |
| 3 | `0011` |
| 4 | `0100` |
| 5 | `0101` |
| … | … |
| 15 | `1111` |

**Chuyển từ thập phân sang nhị phân**: Chia liên tiếp cho 2 rồi đọc các **số dư** theo thứ tự ngược từ dưới lên. Với số $$42$$:

<div class="textbook-equation" markdown="1">
$$
42 = 21 \times 2 + 0,\quad 21 = 10 \times 2 + 1,\quad 10 = 5 \times 2 + 0,\quad 5 = 2 \times 2 + 1,\quad 2 = 1 \times 2 + 0,\quad 1 = 0 \times 2 + 1
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đọc số dư từ cuối lên ta được **`00101010`** = `0x2A`.

<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ nhanh**: Số `255` biểu diễn trên 8 bit là `11111111` (toàn bit 1). Nếu cộng thêm 1 trong phạm vi 8 bit, kết quả quay về `00000000` và bit nhớ (**carry**) bị loại bỏ — đây là hiện tượng **tràn số** (overflow) mà ta sẽ gặp lại ở quy mô 32 bit trong bài Year 2038.
</div>

## Hexadecimal — cách viết gọn cho bit

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hexadecimal** (hệ thập lục phân, cơ số 16) sử dụng các chữ số `0–9` và chữ cái `A–F` (biểu diễn 10–15). Mỗi chữ số hex tương ứng với **đúng 4 bit**, gọi là một **nibble**.
</div>

**Ký hiệu**: Thường dùng tiền tố `0x` (chẳng hạn `0x2A`). Hai chữ số hex ghép thành đúng một byte: `0x41` = `01000001`.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- `0xFF` = `11111111` = 255.
- Chuỗi UTF-8 của `Hi` là `48 69` (hex), tương ứng với hai ký tự `H` và `i` trong ASCII.

Các công cụ hex dump trong trình gỡ lỗi (debugger) hoặc Wireshark hiển thị dữ liệu theo từng **byte** thay vì từng bit riêng lẻ, vì mỗi cặp chữ số hex khớp chính xác với một byte và dễ quan sát hơn nhiều bằng mắt thường.
</div>

## Bộ nhớ: địa chỉ và dãy byte

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Có thể hình dung **RAM** (bộ nhớ chính) như một dãy ô nhớ liên tiếp: mỗi **địa chỉ** (ví dụ `1000`, `1001`, `1002`, …) trỏ tới **một ô** chứa **đúng một byte**.
</div>

CPU không đọc “số 42” từ một ô trừu tượng duy nhất. Nó đọc byte tại địa chỉ đã cho; nếu biến có kiểu `int` 32-bit, CPU đọc thêm 3 byte liền kề rồi **ghép** chúng lại theo quy ước của kiến trúc máy (endianness, sẽ trình bày ở bài sau).

![RAM — dãy byte và cách diễn giải](/discrete-mathematics-for-computer-science-iuh/img/course/binary_ram_layout.svg)

*Hình 9.0.1: Cùng một vùng RAM có thể được đọc thành chuỗi ký tự, số nguyên hoặc một phần tệp nhị phân, tùy vào chương trình diễn giải.*

**Ví dụ** — biến C `int x = 42` trên máy 32-bit little-endian (phổ biến hiện nay):

| Địa chỉ | Byte (hex) | Mẫu bit |
|:---:|:---:|:---:|
| `0x1000` | `0x2A` | `00101010` |
| `0x1001` | `0x00` | `00000000` |
| `0x1002` | `0x00` | `00000000` |
| `0x1003` | `0x00` | `00000000` |

Giá trị toán học là 42, nhưng **ở mức vật lý trong RAM**, đó là bốn byte; khi in dạng hex, byte đầu tiên hiển thị là `0x2A` chứ không phải “42”.

## Dữ liệu thô và cách diễn giải

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Dữ liệu thô** (raw data) là dãy byte không mang sẵn nhãn kiểu. **Kiểu dữ liệu** (data type) hoặc **bảng mã** (encoding) là quy ước cho chương trình biết cần đọc dãy byte đó **như thế nào**.
</div>

**Ví dụ** — cùng một byte `0x41`:

| Cách đọc | Kết quả |
|:---|:---|
| `char` / ASCII | Chữ `A` |
| `uint8_t` | Số 65 |
| Phần đầu tệp JPEG | Byte tiêu đề định dạng, không phải ký tự |

Hai lớp sau rất dễ bị gộp nhầm:

1. **Lớp vật lý**: bit trong transistor, byte trong RAM, sector trên SSD.
2. **Lớp quy ước**: `int`, `float`, UTF-8, PNG — tức cách **ánh xạ** dãy byte sang ý nghĩa cụ thể.

<div class="content-box warning-box textbook-block" markdown="1">
**Lưu ý**: Đọc cùng một địa chỉ bộ nhớ bằng `char*` rồi ép kiểu sang `int*` là hai **cách diễn giải** khác nhau trên cùng một dãy bit. Trong C, thao tác này có thể gây hành vi không xác định (undefined behavior) nếu vi phạm quy tắc strict aliasing, nhưng nó minh họa rõ một nguyên lý: **bit không đổi, chỉ cách diễn giải thay đổi**.
</div>

## Word — khi một số cần nhiều byte

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Word** (từ máy) là độ rộng bit mà CPU xử lý tự nhiên trong một thao tác trên một kiến trúc cụ thể, thường là bội số của 8.
</div>

| Tên gọi | Số bit | Số byte | Ví dụ kiểu trong C |
|:---|:---:|:---:|:---|
| byte | 8 | 1 | `uint8_t` |
| half-word | 16 | 2 | `uint16_t` |
| word (32-bit) | 32 | 4 | `int`, `float` |
| double word | 64 | 8 | `int64_t`, `double` |

Mọi số nguyên không dấu lớn hơn 255 đều cần **nhiều byte** để lưu trữ. Ví dụ, số $$4660 = 0x1234$$ cần hai byte là `0x12` và `0x34`. Thứ tự sắp xếp hai byte này trong RAM chính là chủ đề **endianness** ở bài sau (ngay sau bài Unicode).

## Công cụ tương tác

<div data-demo="logic-operator-widgets"></div>

<script src="{{ '/public/js/logic-operator-widgets.js' | relative_url }}"></script>

Widget trên giúp ôn lại biến Boole $$0/1$$ — đúng hai trạng thái mà mọi bit trong RAM sử dụng, trước khi chúng được gom thành byte, số hay ký tự.

## Ứng dụng trong Khoa học Máy tính

Mọi tầng của hệ thống phần mềm đều xây dựng trên bit và byte. Ở tầng lập trình, `sizeof(int)` trả về số **byte** chứ không phải số bit, còn struct padding chèn thêm byte đệm để căn chỉnh địa chỉ bộ nhớ. Trong mạng máy tính, tiêu đề TCP ghi độ dài bằng byte, và Wireshark thực chất là một công cụ xem hex dump kèm chú thích giao thức. Trong cơ sở dữ liệu, `BLOB` lưu dãy byte thô, còn `VARCHAR` vẫn lưu bằng byte trong trang dữ liệu và cần bảng mã (charset) khi hiển thị. Trong bảo mật, hàm băm SHA-256 trả về đúng 32 byte, và mã nguồn an toàn thường so sánh theo thời gian hằng để tránh tấn công kênh bên (timing attack).

```python
# Đọc 4 byte thô từ file — chưa biết là số hay chữ
raw = open("payload.bin", "rb").read(4)
print(raw.hex())           # ví dụ: 2a000000
print(list(raw))           # [42, 0, 0, 0] — từng BYTE, không phải bit
print(int.from_bytes(raw, "little"))  # diễn giải: uint32 little-endian → 42
```

Chỉ đến dòng cuối cùng, chương trình mới **gán ý nghĩa** cho dữ liệu: với cùng dãy `2a000000`, nếu đổi sang `"big"` hoặc giải mã theo UTF-8, kết quả sẽ hoàn toàn khác.


## Ví dụ tính tay làm từng bước: Chuyển đổi `0xCA` và giải mã 1 byte theo 3 góc nhìn

1. **Chuyển đổi nhanh `0xCA` (hex) $$\leftrightarrow$$ nhị phân $$\leftrightarrow$$ thập phân:**
   - Tách từng chữ số hex thành đúng 4 bit: `C` = $$12 = 8 + 4 = \texttt{1100}_2$$; `A` = $$10 = 8 + 2 = \texttt{1010}_2$$.
   - Ghép lại: `0xCA` = $$\texttt{11001010}_2$$!
   - Đổi sang thập phân: $$12 \times 16^1 + 10 \times 16^0 = 192 + 10 = \mathbf{202}$$ (kiểm tra lại bằng nhị phân: $$128 + 64 + 8 + 2 = 202$$!).
2. **Cùng byte `0x41` (`01000001`):**
   - Đọc kiểu `uint8` (số nguyên không dấu): **$$65$$**.
   - Đọc kiểu ký tự ASCII / UTF-8: chữ hoa **`'A'`**.
   - Đọc kiểu kênh màu đỏ trong RGB (0–255): sắc đỏ đậm khoảng **$$25.5\%$$** độ sáng!

### Giải thích: 3 bước đọc thuộc lòng bất kỳ chuỗi Hex Dump nào
#### Bước 1: Chia chuỗi hex thành từng cặp 2 ký tự = 1 byte
Nhìn thấy `48 69 21`, lập tức biết đây là đúng **3 byte** liên tiếp trong bộ nhớ (độ dài $$3 \times 8 = 24$$ bit).

#### Bước 2: Dùng bảng 4-bit để đổi nhẩm giữa Hex và Nhị phân không cần chia 2
Nhớ 4 mốc vàng: `8 = 1000`, `A = 1010`, `C = 1100`, `F = 1111`. Mọi chữ số hex khác chỉ cách các mốc này $$\pm 1$$!

#### Bước 3: Luôn hỏi "Kiểu diễn giải (Schema / Type) là gì?"
Trước khi kết luận `48 69 21` là chữ `"Hi!"` (ASCII: 72, 105, 33) hay số nguyên 24-bit $$4{,}745{,}505$$, luôn kiểm tra định dạng tệp, giao thức mạng hoặc kiểu dữ liệu khai báo trong code!

$$
\text{Dãy bit } (0/1)
\;\xrightarrow{\text{Gom 4 bit}}\;
\text{Hex (2 ký tự = 1 byte)}
\;\xrightarrow{+ \text{Kiểu dữ liệu}}\;
\text{Số / Chữ / Ảnh / Lệnh CPU}.
$$

## Bài tập thực hành

### Bài tập 1: Chuyển đổi nhị phân

Chuyển các số thập phân sau sang dạng nhị phân 8 bit (thêm các số 0 ở đầu nếu cần): $$13$$, $$42$$, $$200$$.

<details>
<summary>Đáp án</summary>

- $$13 = 8 + 4 + 1$$ → **`00001101`**
- $$42 = 32 + 8 + 2$$ → **`00101010`**
- $$200 = 128 + 64 + 8$$ → **`11001000`**

</details>

### Bài tập 2: Hex và byte

(a) Byte `0xC3` có giá trị thập phân là bao nhiêu? (b) Viết mẫu bit 8 bit của byte đó.

<details>
<summary>Đáp án</summary>

(a) `0xC3` = $$12 \times 16 + 3 = 195$$.

(b) $$195 = 128 + 64 + 2 + 1$$ → **`11000011`**.

</details>

### Bài tập 3: Đọc hex dump

Một vùng RAM 4 byte (little-endian) hiển thị: `2A 00 00 00`. Nếu đọc như `uint32_t` không dấu, giá trị là bao nhiêu? Nếu chỉ đọc byte đầu như ký tự ASCII, kết quả là ký tự gì?

<details>
<summary>Đáp án</summary>

- Đọc theo `uint32_t` little-endian (byte thấp đứng trước): $$0 \times 2^{24} + 0 \times 2^{16} + 0 \times 2^8 + 0x2A = 42$$.
- Byte đầu `0x2A` bằng 42 trong hệ thập phân; giá trị này nằm trong vùng ký tự ASCII in được (32–126) và tương ứng với ký tự dấu sao **`*`**. Cùng một byte `0x2A` nhưng đọc theo kiểu số nguyên ra `42`, còn đọc theo ASCII lại ra ký tự `*` — minh họa rõ vì sao chương trình phải biết **kiểu dữ liệu đang diễn giải**.

</details>

### Bài tập 4: Đếm tổ hợp

Một biến không dấu được lưu bằng $$n$$ bit. Biến này biểu diễn được bao nhiêu giá trị khác nhau? Áp dụng với $$n = 8$$ và $$n = 32$$.

<details>
<summary>Đáp án</summary>

Số giá trị khác nhau là $$2^n$$.

- Với $$n = 8$$: $$2^8 = 256$$ giá trị (từ 0 đến 255).
- Với $$n = 32$$: $$2^{32} = 4\,294\,967\,296$$ giá trị — đủ để biểu diễn Unix timestamp 32-bit không dấu, nhưng với số nguyên 32-bit có dấu theo quy tắc bù hai (two's complement), dải biểu diễn sẽ bị giới hạn khác đi (xem bài sau).

</details>

### Bài tập 5: Bit và bộ nhớ ảnh

Một ảnh mức xám (grayscale) kích thước $$4 \times 4$$ pixel, mỗi pixel chiếm 1 byte (giá trị 0–255). Hỏi: (a) Tổng số byte lưu dữ liệu pixel? (b) Tổng số bit?

<details>
<summary>Đáp án</summary>

(a) $$4 \times 4 = 16$$ pixel × 1 byte = **16 byte**.

(b) $$16 \times 8 = 128$$ **bit**.

Lưu ý rằng tệp ảnh thực tế trên đĩa còn có thêm phần tiêu đề (header/metadata) chiếm thêm byte; phép tính trên chỉ xét **dữ liệu pixel thô**.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Bit**: Đơn vị thông tin nhỏ nhất, chỉ nhận giá trị 0 hoặc 1 — nền tảng của đại số Boole và phần cứng số.
- **Byte**: Gồm 8 bit; RAM được địa chỉ hóa theo byte và công cụ hex dump hiển thị theo byte.
- **Hệ nhị phân và hệ hex**: Hai cách biểu diễn cùng một mẫu bit; hệ hex ngắn gọn và thuận tiện hơn khi gỡ lỗi.
- **Diễn giải dữ liệu**: Cùng một byte có thể là ký tự, số nguyên hoặc mã lệnh; kiểu dữ liệu và bảng mã quyết định ý nghĩa của nó.
- **Word**: Số lớn cần nhiều byte liền kề; thứ tự sắp xếp các byte trong bộ nhớ là chủ đề của endianness.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu cách **dãy byte được diễn giải thành văn bản** thông qua Unicode và UTF-8, cũng như lý do Joel Spolsky khẳng định không có “văn bản thuần” trên máy tính.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=thrx3SBEpL8">Why Use Binary? - Computerphile</a> — Computerphile, tiếng Anh. Giải thích vì sao máy tính lưu trữ bằng hai mức trạng thái, mở đầu trực tiếp cho khái niệm bit và byte.
- <a href="https://www.youtube.com/watch?v=ZL-LhaaMTTE">Understanding Binary, Hexadecimal, Decimal (Base-10), and more</a> — Corey Schafer, tiếng Anh. Hướng dẫn chuyển đổi giữa hệ nhị phân, thập phân và thập lục phân.
- <a href="https://www.youtube.com/watch?v=a8eKbrcBYPM">Binary &amp; Hexadecimal Demystified</a> — NesHacker, tiếng Anh. Cách đọc byte ở dạng hex, tương ứng với phần địa chỉ bộ nhớ và dữ liệu thô.
