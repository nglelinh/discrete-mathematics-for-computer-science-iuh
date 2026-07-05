---

layout: post
title: "Dữ liệu nhị phân trong máy tính: Từ bit đến bộ nhớ"
categories: chapter09
date: 2021-01-01
order: 0
required: true
lang: en
excerpt: "Trong chương này chúng ta khảo sát cách máy tính lưu trữ và diễn giải dữ liệu ở mức nhị phân — nền tảng cho mọi lớp phần mềm phía trên. Ở Chương 1, logic mệnh…"
---

<div class="textbook-epigraph" markdown="1">

"There is no such thing as plain text."

<span class="epigraph-attribution">— Joel Spolsky</span>

</div>

Trong chương này chúng ta khảo sát cách máy tính **lưu trữ và diễn giải** dữ liệu ở mức nhị phân — nền tảng cho mọi lớp phần mềm phía trên. Ở Chương 1, logic mệnh đề đã cho ta biến Boole với hai giá trị $$0$$ và $$1$$; mục này trả lời câu hỏi kế tiếp: **bit đó nằm ở đâu, được gom thành khối thế nào, và vì sao cùng một byte có thể vừa là chữ `A` vừa là số 65?** Câu trả lời bắt đầu từ đơn vị nhỏ nhất — **bit** — rồi mở rộng sang byte, hệ nhị phân, hexadecimal, và cách chương trình gán ý nghĩa cho dãy byte thô trong RAM.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Bits_and_Bytes.svg"
       alt="Quan hệ bit và byte — 8 bit ghép thành 1 byte, các đơn vị lưu trữ lớn hơn gom từ byte"
       width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 9.0a: 8 bit = 1 byte; các đơn vị KB, MB, GB… gom từ byte. Bit không tự biết nó là chữ hay số — chương trình quyết định cách đọc (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Bits_and_Bytes.svg">Fcarmody / Wikimedia Commons</a>, CC BY-SA 4.0).</figcaption>
</p>
</figure>

## Bit — đơn vị nhỏ nhất

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Bit** (binary digit) là đơn vị thông tin nhỏ nhất trong máy tính kỹ thuật số. Mỗi bit chỉ có **hai trạng thái**: $$0$$ hoặc $$1$$.
</div>


Trong phần cứng, hai trạng thái đó thường tương ứng với điện áp thấp/cao, từ trường hướng/nghịch, hoặc lỗ hổng đóng/mở trên đĩa quang — nhưng ở tầng lập trình, chúng ta có thể coi bit là biến Boole $$x \in \{0,1\}$$ như Chương 1 đã giới thiệu.

**Ký hiệu**: Một bit viết là $$b \in \{0,1\}$$. Chuỗi $$n$$ bit: $$b_{n-1} b_{n-2} \ldots b_1 b_0$$ (bit $$b_{n-1}$$ là **bit cao nhất**, MSB; $$b_0$$ là **bit thấp nhất**, LSB).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- Công tắc đèn: tắt = 0, bật = 1.
- `bool logged_in` trong C++: `false` thường lưu thành byte toàn 0, `true` thành 1 — nhưng vẫn chỉ cần **một bit** thông tin; ngôn ngữ thường cấp phát cả byte vì RAM đọc theo byte.
</div>


<div class="content-box insight-box textbook-block" markdown="1">
Máy tính **không** lưu chữ “42” hay “A” trực tiếp. Nó lưu **mẫu bit**. Chữ và số là cách **con người và chương trình diễn giải** mẫu đó — giống nốt nhạc trên khuông: cùng vạch, khác nhạc cụ đọc khác âm thanh.
</div>

## Byte — tám bit gom một nhóm

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Byte** là nhóm **8 bit** liền nhau, là đơn vị địa chỉ hóa phổ biến nhất của bộ nhớ máy tính hiện đại.
</div>


**Ký hiệu**: Một byte lưu giá trị nguyên từ $$0$$ đến $$2^8 - 1 = 255$$ khi đọc theo **không dấu** (unsigned). Ví dụ byte `01000001` (nhị phân) = $$64 + 1 = 65$$ (thập phân) = `0x41` (hex).

<div class="textbook-example" markdown="1">
**Ví dụ**:
- Chữ `A` trong ASCII/UTF-8: một byte `0x41`.
- Màu đỏ trong ảnh RGB thường là ba byte liên tiếp: `FF 00 00`.
- `int` 32-bit trên hầu hết máy tính để bàn: **4 byte** liền kề trong RAM.
</div>


**Tính chất**: Với 8 bit, số tổ hợp khác nhau là $$2^8 = 256$$. Đó là lý do một byte “vừa đủ” cho ký tự Latin cơ bản trong ASCII (128 ký tự đầu nằm trong 0–127), và là nền mà UTF-8, ảnh bitmap, gói tin mạng đều xây trên byte.

![Một ô nhớ chứa byte 0x12](/discrete-mathematics-for-computer-science-iuh/img/course/memory_byte_12.svg)

<p class="textbook-figure-caption" data-figure="9.0">Một địa chỉ bộ nhớ = một byte = 8 bit. Hex `0x12` chỉ là cách viết gọn của mẫu bit bên trong.</p>
## Hệ nhị phân — đếm bằng hai chữ số

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hệ nhị phân** (binary) là hệ cơ số với cơ số 2. Mỗi vị trí bit nhân với lũy thừa của 2.
</div>


**Ký hiệu**: Giá trị của chuỗi bit $$b_{k-1} \ldots b_0$$:

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
Bảng đếm 4 bit đầu:

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

**Chuyển thập phân → nhị phân**: chia liên tiếp cho 2, ghi **số dư** từ dưới lên. Ví dụ $$42$$:

<div class="textbook-equation" markdown="1">
$$
42 = 21 \times 2 + 0,\quad 21 = 10 \times 2 + 1,\quad 10 = 5 \times 2 + 0,\quad 5 = 2 \times 2 + 1,\quad 2 = 1 \times 2 + 0,\quad 1 = 0 \times 2 + 1
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đọc dư từ cuối: **`00101010`** = `0x2A`.

<div class="content-box example-box textbook-block" markdown="1">
**Ví dụ nhanh**: Số `255` = `11111111` (8 bit toàn 1). Cộng 1 nữa (nếu chỉ có 8 bit) → `00000000` với **carry** bị bỏ — hiện tượng **tràn** (overflow) mà mục Year 2038 sẽ gặp lại ở quy mô 32 bit.
</div>

## Hexadecimal — viết tắt cho bit

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hexadecimal** (hex, cơ số 16) dùng chữ số `0–9` và `A–F` (10–15). Mỗi chữ số hex tương ứng **đúng 4 bit** — gọi là **nibble**.
</div>


**Ký hiệu**: Tiền tố `0x` (ví dụ `0x2A`). Hai chữ số hex = một byte: `0x41` = `01000001`.

<div class="textbook-example" markdown="1">
**Ví dụ**:
- `0xFF` = `11111111` = 255.
- Chuỗi UTF-8 của `Hi`: `48 69` (hex) = `H` + `i` trong ASCII.

Hex dump trong debugger hoặc Wireshark hiển thị **byte**, không hiển thị từng bit — vì 8 bit một nhóm vừa đủ để đọc bằng mắt, và mỗi cặp hex digit khớp một byte.
</div>


## Bộ nhớ: địa chỉ và dãy byte

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **RAM** (bộ nhớ chính) có thể hình dung như một **con phố dài**: mỗi **địa chỉ** (ví dụ `1000`, `1001`, `1002`, …) trỏ tới **một ô** chứa **đúng một byte**.
</div>


CPU không “đọc số 42” trong một ô trừu tượng. Nó đọc byte tại địa chỉ, rồi — nếu biến là `int` — đọc thêm 3 byte kế tiếp và **ghép** theo quy tắc kiến trúc (endianness, mục tiếp theo).

![RAM — dãy byte và cách diễn giải](/discrete-mathematics-for-computer-science-iuh/img/course/binary_ram_layout.svg)

*Hình 9.0.1: Cùng vùng RAM có thể là chuỗi ký tự, số nguyên, hoặc phần file nhị phân — tùy chương trình đọc.*

**Ví dụ** — biến C `int x = 42` trên máy 32-bit little-endian (phổ biến):

| Địa chỉ | Byte (hex) | Bit pattern (rút gọn) |
|:---:|:---:|:---:|
| `0x1000` | `0x2A` | `00101010` |
| `0x1001` | `0x00` | `00000000` |
| `0x1002` | `0x00` | `00000000` |
| `0x1003` | `0x00` | `00000000` |

Giá trị toán học là 42, nhưng **vật lý trong RAM** là bốn byte; byte đầu không “trông như 42” khi in hex.

## Dữ liệu thô và cách diễn giải

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Dữ liệu thô** (raw data) là dãy byte không kèm “nhãn” kiểu. **Kiểu dữ liệu** (data type) hoặc **encoding** là quy ước nói cho chương trình biết đọc byte **như thế nào**.
</div>


**Ví dụ** — cùng byte `0x41`:

| Cách đọc | Kết quả |
|:---|:---|
| `char` / ASCII | Chữ `A` |
| `uint8_t` | Số 65 |
| Phần đầu file JPEG | Byte header định dạng, không phải chữ |

Hai lớp hay bị gộp nhầm:

1. **Lớp vật lý**: bit trong transistor, byte trong RAM, sector trên SSD.
2. **Lớp quy ước**: `int`, `float`, UTF-8, PNG — cách **ánh xạ** byte sang ý nghĩa.

<div class="content-box warning-box textbook-block" markdown="1">
**Cẩn thận**: In `char*` ra màn hình và cast sang `int*` đọc cùng địa chỉ là hai **diễn giải** khác nhau trên cùng bit — hành vi undefined trong C nếu vi phạm strict aliasing, nhưng minh họa rõ: **bit không đổi, ý nghĩa đổi**.
</div>

## Word — khi một số cần nhiều byte

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Word** (từ máy) là số bit mà CPU xử lý “tự nhiên” trong một lần trên kiến trúc đó — thường là bội số của 8.
</div>


| Tên | Số bit | Số byte | Ví dụ kiểu C |
|:---|:---:|:---:|:---|
| byte | 8 | 1 | `uint8_t` |
| half-word | 16 | 2 | `uint16_t` |
| word (32-bit) | 32 | 4 | `int`, `float` |
| double word | 64 | 8 | `int64_t`, `double` |

Số lớn hơn 255 cần **nhiều byte**. Số $$4660 = 0x1234$$ cần hai byte: `0x12` và `0x34`. Thứ tự hai byte trong RAM là chủ đề **endianness** (mục tiếp theo sau Unicode).

## Công cụ tương tác

<div data-demo="logic-operator-widgets"></div>

Widget trên ôn lại biến Boole $$0/1$$ — cùng hai giá trị mà mọi bit trong RAM đều dùng, dù sau này ta gom chúng thành byte, số, hoặc chữ.

## Ứng dụng trong Khoa học Máy tính

Mọi tầng stack đều dựa trên bit. Ở tầng lập trình, `sizeof(int)` trả về số **byte**, không phải số bit; struct padding thêm byte rỗng để căn chỉnh địa chỉ. Trên mạng, TCP header ghi độ dài bằng byte; Wireshark là hex dump có chú thích protocol. Trong cơ sở dữ liệu, `BLOB` lưu byte thô; `VARCHAR` vẫn là byte trong file page, kèm charset khi hiển thị. Trong bảo mật, hash SHA-256 trả về 32 byte; so sánh bit-by-bit tránh timing attack trong code cẩn thận.

```python
# Đọc 4 byte thô từ file — chưa biết là số hay chữ
raw = open("payload.bin", "rb").read(4)
print(raw.hex())           # ví dụ: 2a000000
print(list(raw))           # [42, 0, 0, 0] — từng BYTE, không phải bit
print(int.from_bytes(raw, "little"))  # diễn giải: uint32 little-endian → 42
```

Dòng cuối mới **gán ý nghĩa**: cùng `2a000000`, đổi `"big"` hoặc đọc như UTF-8 sẽ ra kết quả khác.

## Bài tập thực hành

### Bài tập 1: Chuyển đổi nhị phân

Chuyển các số thập phân sau sang nhị phân (8 bit, thêm số 0 đầu nếu cần): $$13$$, $$42$$, $$200$$.

<details>
<summary>Đáp án</summary>

- $$13$$: $$13 = 8+4+1$$ → **`00001101`**
- $$42$$: như trên → **`00101010`**
- $$200$$: $$200 = 128+64+8$$ → **`11001000`**

</details>

### Bài tập 2: Hex và byte

(a) Byte `0xC3` là bao nhiêu ở thập phân? (b) Viết bit pattern 8 bit của nó.

<details>
<summary>Đáp án</summary>

(a) `0xC3` = $$12 \times 16 + 3 = 195$$.

(b) $$195 = 128 + 64 + 2 + 1$$ → **`11000011`**.

</details>

### Bài tập 3: Đọc hex dump

Một vùng RAM 4 byte (little-endian) hiển thị: `2A 00 00 00`. Nếu đọc là `uint32_t` không dấu, giá trị là bao nhiêu? Nếu chỉ đọc byte đầu như ASCII, ký tự là gì?

<details>
<summary>Đáp án</summary>

- `uint32_t` little-endian: byte thấp trước → $$0 \times 2^{24} + 0 \times 2^{16} + 0 \times 2^8 + 0x2A = 42$$.
- Byte đầu `0x2A` = 42 thập phân; **không** nằm trong bảng ASCII in được (ASCII in được thường 32–126). Nếu ép đọc `char`, có thể là ký tự điều khiển hoặc không in được — minh họa vì sao cần biết **đang đọc kiểu gì**.

</details>

### Bài tập 4: Đếm tổ hợp

Một biến lưu bằng $$n$$ bit (không dấu). Có bao nhiêu giá trị khác nhau? Áp dụng với $$n = 8$$, $$n = 32$$.

<details>
<summary>Đáp án</summary>

Số giá trị = $$2^n$$.

- $$n = 8$$: $$2^8 = 256$$ giá trị (0–255).
- $$n = 32$$: $$2^{32} = 4\,294\,967\,296$$ giá trị — đủ lớn để chứa Unix timestamp 32-bit unsigned, nhưng signed 32-bit và quy tắc two's complement sẽ giới hạn dải khác (mục sau).

</details>

### Bài tập 5: Bit và bộ nhớ ảnh

Ảnh grayscale $$4 \times 4$$ pixel, mỗi pixel 1 byte (0–255). Hỏi: (a) Tổng số byte lưu ảnh? (b) Tổng số bit?

<details>
<summary>Đáp án</summary>

(a) $$4 \times 4 = 16$$ pixel × 1 byte = **16 byte**.

(b) $$16 \times 8 = 128$$ **bit**.

File trên disk còn có header (metadata) — thêm byte nữa; câu hỏi chỉ tính **dữ liệu pixel thô**.

</details>


## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Bit**: đơn vị nhỏ nhất, chỉ 0 hoặc 1 — nền của logic Boole và phần cứng số.
- **Byte**: 8 bit; RAM địa chỉ hóa theo byte; hex dump đọc theo byte.
- **Hệ nhị phân / hex**: hai cách viết cùng một mẫu bit; hex gọn hơn khi debug.
- **Diễn giải**: cùng byte có thể là chữ, số, hoặc opcode — kiểu dữ liệu và encoding quyết định ý nghĩa.
- **Word**: số lớn cần nhiều byte liền kề; thứ tự byte là chủ đề endianness.

Trong bài tiếp theo, chúng ta sẽ học cách **byte đó được hiểu thành chữ** — Unicode, encoding UTF-8, và vì sao Joel nói không có “văn bản thuần” trên máy tính.