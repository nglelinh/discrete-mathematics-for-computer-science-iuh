---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Unicode và Encoding

**Toán Rời Rạc · Chương 9**

Bài `09_01` — Không có văn bản thuần (45 phút)

---

## Mục tiêu tiết học

- Phân biệt **ASCII**, **Unicode** (code point) và **encoding** (byte)
- Giải thích mối quan hệ: Ký tự → Unicode → Encoding → Bytes
- So sánh UTF-8 / UTF-16 / UTF-32 trên cùng code point
- Giải thích mojibake và trace pipeline DB → API → browser
- Áp dụng quy tắc khai báo charset trong code thực tế

**Bài blog:** `contents/chapter09/.../09_01_No_Such_Thing_As_Plain_Text.md`

---

## Ba khái niệm — mối quan hệ

```
Ký tự (ế)
   ↓
Unicode (U+1EBF)
   ↓
Encoding (UTF-8)
   ↓
Bytes trong file (E1 BA BF)
```

**ASCII** ⊂ **Unicode** · **UTF-8** = một cách **mã hóa** Unicode.

---

## 1. ASCII là gì?

**ASCII** — bảng mã cũ, **128 ký tự** (7 bit):

- Chữ `A`–`Z`, `a`–`z` · số `0`–`9`
- Ký hiệu `! @ # $ %` · điều khiển Enter, Tab, …

| Ký tự | Mã ASCII |
|:---:|:---:|
| A | 65 |
| B | 66 |
| a | 97 |
| 0 | 48 |

`ă`, `ế`, `中` **không có** trong ASCII.

![Bảng ASCII](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2003/10/ascii.png?resize=360%2C190)

---

## 2. Unicode là gì?

Cần Việt, Trung, Nhật, Hàn, emoji → ASCII không đủ.

**Unicode** gán **code point** `U+xxxx` duy nhất cho mọi ký tự:

| Ký tự | Unicode |
|:---:|:---:|
| A | U+0041 |
| á | U+00E1 |
| ế | U+1EBF |
| 中 | U+4E2D |
| 😀 | U+1F600 |

Unicode chỉ trả lời: **“Ký tự này có số hiệu bao nhiêu?”**

Chưa nói: **“Lưu file bằng byte nào?”**

![Unicode Consortium](https://commons.wikimedia.org/wiki/Special:FilePath/Unicode_logo.svg?width=260)

---

## Unicode — ví dụ `Nguyễn` & normalization

`Nguyễn` → `U+004E` · `U+0067` · `U+0075` · `U+0079` · `U+1EC5` · `U+006E`

---

## 3. Encoding là gì?

**Encoding** = cách biến code point Unicode thành **dãy byte** (lưu file, gửi mạng).

Phổ biến: **UTF-8** · **UTF-16** · **UTF-32**

Cùng một code point — **encoding khác → byte khác**.

Hai đầu pipeline phải dùng **cùng** encoding.

---

## So sánh byte — ký tự `A`

Unicode: **U+0041**

| Encoding | Byte (hex) |
|:---|:---|
| UTF-8 | `41` |
| UTF-16 | `00 41` |
| UTF-32 | `00 00 00 41` |

---

## So sánh byte — ký tự `ế`

Unicode: **U+1EBF**

| Encoding | Byte (hex) |
|:---|:---|
| UTF-8 | `E1 BA BF` |
| UTF-16 | `1E BF` |
| UTF-32 | `00 00 1E BF` |

Cùng ký tự trên màn hình — **file nhị phân khác** nếu đổi encoding.

---

## UTF-8 — quy tắc & vì sao phổ biến

| Phạm vi code point | Số byte |
|:---|:---:|
| `U+0000`–`U+007F` | 1 |
| `U+0080`–`U+07FF` | 2 |
| `U+0800`–`U+FFFF` | 3 |
| trên `U+FFFF` | 4 |

**128 ký tự đầu Unicode = ASCII** trong UTF-8:

| Ký tự | ASCII | UTF-8 |
|:---:|:---:|:---:|
| A | `41` | `41` |
| B | `42` | `42` |
| 0 | `30` | `30` |

→ Tương thích ngược ASCII · tiết kiệm cho tiếng Anh · mặc định web/Linux/macOS.

![UTF-8 diagram](https://i0.wp.com/www.joelonsoftware.com/wp-content/uploads/2003/10/utf8.png?resize=460%2C72)

---

## UTF-16, UTF-32 & Java `String`

UTF-16: BMP thường **2 byte**/code point; > `U+FFFF` → surrogate pair.

UTF-32: **4 byte** cố định / code point (đơn giản, tốn chỗ).

JVM `String` nội bộ = UTF-16 → Unicode trong RAM **≠** UTF-8 trên dây.

JDBC decode sai charset → tên tiếng Việt hỏng dù DB đúng.

---

## ASCII mở rộng — code page (lịch sử)

Byte 8 bit → 256 giá trị; ASCII chỉ chuẩn 0–127.

Vùng 128–255: **mỗi locale một bảng** (Windows-1252, ISO-8859-1…).

Cùng byte `0xE9` → `é` hoặc chữ Hebrew — không có metadata.

Unicode + UTF-8 thay thế hỗn loạn này.

---

## Toán rời rạc — encoding là hàm

Encoding là hàm $$f$$: chuỗi code point → dãy byte.

Hiển thị đúng ⟺ cả pipeline dùng **cùng** $$f$$.

Decode bằng $$f' \neq f$$ → mojibake; dữ liệu gốc trong DB có thể vẫn đúng.

---

## Mojibake — decode sai bảng mã

**Mojibake** (文字化け): byte UTF-8 bị đọc như Latin-1.

`E1 BB 85` (`ễ`) → `á` + `»` + `…` = `Nguyá»…n`

Không mất byte — **bảng tra sai**.

**Double encoding**: decode nhầm → encode lại → **hỏng trong DB** (phải migrate).

---

## Demo Python

```python
name = "Nguyễn"
b = name.encode("utf-8")
print(b.hex())              # 4e677579e1bb856e
print(b.decode("utf-8"))    # Nguyễn
print(b.decode("latin-1"))  # Nguyá»…n
```

**Quy ước code:**
- `str` / `String` trong RAM → đã decode
- byte vào → `decode(charset)`; byte ra → `encode("utf-8")`

---

## Pipeline TaskFlow

| Hop | Encoding |
|:---|:---|
| PostgreSQL | UTF-8 trên disk |
| JDBC | **phải** `characterEncoding=UTF-8` |
| JSON body | UTF-8 (RFC) |
| Browser | UTF-8 nếu header đúng |

Lỗi Minh: JDBC mặc định Latin-1 — `String` JVM sai trước khi serialize JSON.

---

## Khai báo charset — checklist ngắn

- HTTP: `Content-Type: application/json; charset=utf-8`
- HTML: `<meta charset="UTF-8">`
- Email: `charset` trên **từng** MIME part
- MySQL: `utf8mb4` (không dùng `utf8` cũ 3-byte)
- PostgreSQL: `UTF8` + client encoding khớp

Bug encoding **im lặng** — xem hex dump, không đoán bằng mắt.

---

## Thực hành 1

1. Viết code point từng ký tự trong tên bạn (có dấu).
2. `encode("utf-8")` rồi in `.hex()` — đếm byte của ký tự có dấu.
3. `decode("latin-1")` cùng byte — mô tả mojibake nhận được.

---

## Thực hành 2

Pipeline giả định: Postgres UTF-8, API thiếu `charset` trong header.

1. Vẽ 4 hop và ghi encoding mỗi hop.
2. Chỉ ra hop dễ lỗi nhất và cách sửa.
3. Phân biệt: bug **hiển thị** vs **double encoding** trong DB.

---

## Tóm tắt

| Khái niệm | Một câu |
|:---|:---|
| **ASCII** | 128 ký tự đầu (7 bit) — tập con Unicode |
| **Unicode** | Mã số `U+xxxx` cho mọi ký tự trên thế giới |
| **Encoding** | Cách chuyển Unicode → byte (UTF-8, UTF-16, UTF-32) |

**UTF-8** mã hóa Unicode, tương thích ASCII. Không có văn bản thuần — chỉ byte + quy ước.

---

## Liên hệ

- **Định lý / mô hình**: encoding là hàm $$f$$; decode sai = $$f' \neq f$$
- **Edge case**: NFC vs NFD; `utf8` vs `utf8mb4`; `?` vs `U+FFFD`
- **Tiếp theo** (`09_02`): endianness, BOM — UTF-16 và binary

**Đọc thêm:** [Joel on Software (2003)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

---

## Bài tập ôn tập (1/2)

1. **Phân biệt**: ASCII vs Unicode vs Encoding — mỗi thứ trả lời câu hỏi gì?

2. **Tính toán**: `ế` (`U+1EBF`) — ghi byte UTF-8, UTF-16, UTF-32 (hex).

3. **Nhận diện**: Vì sao `SELECT` trong psql đúng mà JSON browser sai?

---

## Bài tập ôn tập (2/2)

4. **Code**: Viết Python đọc file text, thử `utf-8` và `latin-1`, so sánh khi file thật sự UTF-8.

5. **Phân tích**: Mô tả double encoding — tại sao sửa HTTP header không cứu được dữ liệu đã lưu sai?

6. **Mở rộng**: Tìm trong project Java/Spring chỗ khai báo JDBC charset và `Content-Type` JSON.

---

## Tiết sau

**Endianness & BOM** (`09_02`) — cùng code point `U+0048`, byte `00 48` hay `48 00`?

Vì sao copy file UTF-16 Windows ↔ Mac có thể hỏng chữ?

**Câu hỏi?**
