---
layout: post
title: "Unicode và encoding: Không có văn bản thuần"
categories: chapter09
date: 2021-01-01
order: 1
required: false
lang: en
---

Tuần đầu tiên Minh làm backend cho **TaskFlow**, anh deploy feature hiển thị tên khách hàng lên dashboard staging. API trả JSON đúng schema, test pass, QA gật đầu. Chiều thứ Sáu, product owner gửi screenshot vào Slack:

> Sao `Nguyễn Thị Lan` thành `Nguyá»…n Thá»‹ Lan`?

Không ai sửa database. Không ai hack. Minh mở `psql`, `SELECT name FROM customers WHERE id = 42` — vẫn `Nguyễn Thị Lan`. Bug không nằm trong bảng; nó nằm giữa Postgres, driver JDBC, serializer JSON, và trình duyệt — đoạn pipeline mà tuần trước anh gọi là “chỉ trả string ra frontend thôi mà”.

Để sửa, anh phải tách hai khái niệm mà người mới hay gộp chung: **Unicode** (chữ là số nào) và **encoding** (số đó ghi thành byte nào). Bài này đi sâu vào hai khái niệm đó — không phải để thi lịch sử OEM, mà để hiểu vì sao bug im lặng, và vì sao sáu tháng sau channel `#incidents` của TaskFlow lại nhận thêm ticket email tiếng Nhật toàn dấu `????`.

---

## Joel và câu hỏi “plain text”

Năm 2003, Joel Spolsky sửa bug email tiếng Nhật trong **FogBUGZ**. Thư viện parse email bỏ qua header `charset`, nhảy thẳng từ byte lên “chữ hiển thị” mà không qua bước chọn bảng mã. Kanji thành `????`. Vendor không sửa. Joel viết [bài blog](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) mà người ta vẫn paste vào Slack khi hỏi “sao chữ bị lỗi?” — kết bài bằng **There Ain't No Such Thing As Plain Text.** Trên máy tính **không có “văn bản thuần”**. Mở file `.txt`, gõ vào ô chat, nhận JSON từ API — bên dưới đều là **byte**. File “text” chỉ là thỏa thuận ngầm: “cùng hiểu đây là UTF-8” hoặc “cùng hiểu đây là Windows-1252”. Thỏa thuận không được ghi ra thì máy **đoán** — và đoán sai cho ra mojibake (`Nguyá»…n`), ký tự thay thế `U+FFFD`, hoặc dấu `?` khi font/codec không render được.

Minh đọc bài Joel lúc nửa đêm và hiểu vì sao `SELECT` trong psql đẹp mà JSON trên browser hỏng: hai đầu pipeline đang dùng **hai quy ước decode khác nhau** trên cùng một dãy byte.

---

## Unicode: danh bạ số, không phải file

**Unicode** là chuẩn gán **code point** — số ID — cho hầu hết ký tự dùng trong văn bản: chữ Latin, Cyrillic, kanji, ký hiệu toán, emoji. Ký hiệu `U+` là quy ước viết số ở hệ hexadecimal: chữ `H` là `U+0048`, `ă` là `U+0103`, kanji `字` là `U+5B57`, emoji 🎉 là `U+1F389`.

Unicode trả lời một câu hỏi duy nhất: **“Ký tự này là số bao nhiêu?”** Nó **không** nói số đó chiếm mấy byte trên disk, thứ tự byte ra sao, hay file JSON trên dây mạng trông thế nào. Đó là việc của **encoding** (UTF-8, UTF-16, …).

Nhiều người vẫn tưởng Unicode = 2 byte mỗi chữ. Unicode **không** cố định độ dài byte. Chuỗi `Hello` trong Unicode là năm code point: `U+0048`, `U+0065`, `U+006C`, `U+006C`, `U+006F`. Đó mới là lớp trừu tượng — chưa phải file, chưa phải payload HTTP.

Với tên `Nguyễn`, Minh ghi ra từng code point:

`U+004E` (N) · `U+0067` (g) · `U+0075` (u) · `U+0079` (y) · `U+1EC5` (ễ) · `U+006E` (n)

Chữ `ễ` ở đây là **một** code point dạng **tổ hợp sẵn** (precomposed). Unicode còn cho phép cách khác: tách thành `U+0065` (e) + `U+0302` (dấu mũ) + `U+0303` (dấu ngã) — nhìn giống nhau trên màn hình, nhưng **dãy code point khác**, và khi encode ra byte cũng khác. Hai chuỗi “giống mắt” như vậy gọi là cùng **grapheme** (ký tự người đọc thấy), nhưng có thể khác **biểu diễn Unicode**. Chuẩn **normalization** (NFC, NFD) quy định dùng dạng nào khi so sánh, lưu DB, hoặc build index tìm kiếm — bỏ qua bước này, `Nguyễn` và `Nguyẽ̂n` (e + combining marks) có thể không match dù người dùng gõ cùng một tên.

Unicode còn tổ chức code point theo **plane**: Plane 0 (BMP, `U+0000`–`U+FFFF`) chứa hầu hết chữ dùng hàng ngày; plane bổ sung chứa emoji và chữ cổ. Code point trên `U+FFFF` (ví dụ `U+1F389`) không nằm gọn trong một “ô” 16-bit — điều này ảnh hưởng trực tiếp tới **UTF-16** (bài sau nói thêm về surrogate pair và endianness).

<div class="content-box insight-box" markdown="1">
Trong toán rời rạc, tập code point Unicode (lý tưởng hóa) là domain; **encoding** là hàm $$f$$ ánh xạ chuỗi code point sang dãy byte. Hiển thị đúng là tìm được $$f$$ mà cả hai đầu pipeline cùng dùng — encode rồi decode là hàm ngược, không phải “đọc chữ có sẵn trong byte”.
</div>

---

## Encoding: byte trên dây, không phải chữ trong đầu

Nếu Unicode là danh bạ, **encoding** là cách **ghi sổ** danh bạ đó thành byte để lưu file, gửi socket, hoặc đưa vào driver database.

### ASCII và thời “mỗi nước một bảng”

Thập niên 1970, **ASCII** chuẩn hóa 128 ký tự đầu (giá trị 0–127): Latin không dấu, số, dấu câu cơ bản. `A` = 65, space = 32.

![Bảng ASCII — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_ascii.png)

*Hình 9.1: ASCII — ký tự tiếng Anh không dấu, một byte 0–127 (Joel on Software).*

Chữ `ă`, `ê`, `ố` **không có** trong ASCII. Byte 8 bit có 256 giá trị; ASCII chỉ “cắm cờ” 0–127. Vùng 128–255: **mỗi locale một bảng** (code page, OEM, Windows-1252, ISO-8859-1…). Joel kể email **résumé**: byte `0xE9` trên máy Mỹ là `é`, trên máy Israel có thể đọc thành chữ Hebrew — **cùng byte, khác chữ**, vì không có metadata nói đang dùng bảng nào.

![OEM character set — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_oem.png)

*Hình 9.2: Byte 128–255 — mỗi locale một bảng (Joel on Software).*

Unicode ra đời để **một** danh bạ cho mọi ngôn ngữ. Nhưng danh bạ thống nhất chưa giải quyết xong chuyện lưu trữ: vẫn cần chọn **cách ghi số `U+xxxx` thành byte** — và đó là lúc UTF-8, UTF-16, Latin-1 cạnh tranh.

### UTF-8: biến độ dài, ASCII-compatible

**UTF-8** là encoding **biến độ dài**: mỗi code point tốn 1–4 byte.

Quy tắc cốt lõi (đủ để đọc hex dump và debug):

- Code point `U+0000`–`U+007F` (trùng ASCII): **1 byte**, bit cao `0` — `A` vẫn là `41`.
- `U+0080`–`U+07FF`: **2 byte**, pattern `110xxxxx 10xxxxxx`.
- `U+0800`–`U+FFFF`: **3 byte**, pattern `1110xxxx 10xxxxxx 10xxxxxx`.
- Trên `U+FFFF`: **4 byte**, pattern `11110xxx` + ba byte tiếp theo dạng `10xxxxxx`.

Ví dụ chữ `é` (`U+00E9`): UTF-8 là `C3 A9` (2 byte). Trong **Latin-1** (ISO-8859-1), cùng code point chỉ là `E9` (1 byte). Cùng một chữ trên màn hình, **file nhị phân khác nhau** — so `diff` hai file sẽ thấy lệch dù “nội dung” người đọc giống nhau.

Với `Nguyễn`, UTF-8 cho code point `U+1EC5` (ễ) là ba byte `E1 BB 85`. Cả tên:

```text
4E 67 75 79 E1 BB 85 6E   ← UTF-8 của "Nguyễn"
```

Phần lớn web, API, JSON, Git, Linux, PostgreSQL hiện đại mặc định UTF-8 vì: tiếng Anh vẫn gọn một byte như ASCII cũ; chữ Việt, Nhật, emoji nhét được mà không cần chọn code page theo quốc gia; và không phụ thuộc endianness như UTF-16 (chủ đề bài sau).

![Cách UTF-8 hoạt động — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_utf8.png)

*Hình 9.4: UTF-8 — ASCII gọn, ký tự quốc tế dài hơn (Joel on Software).*

### UTF-16 và Java `String`

**UTF-16** encode phần lớn BMP bằng **2 byte** mỗi code point (`H` → `00 48`), và dùng **surrogate pair** (4 byte) cho code point ngoài BMP. Trong JVM, kiểu `String` nội bộ là UTF-16 — đó là lý do “đã là Unicode trong RAM” ở Java **không** có nghĩa “đã là UTF-8 trên dây”. Khi JDBC đọc `VARCHAR` từ Postgres, driver phải **decode byte từ wire protocol** sang UTF-16 trong heap; khai báo charset sai ở đây là đủ phá tên tiếng Việt dù cột DB lưu đúng.

---

## Mojibake: decode bằng bảng mã sai

Tiếng Nhật gọi **mojibake** (文字化け) khi byte được **giải mã bằng encoding khác** encoding đã dùng để mã hóa — chữ trên màn hình biến dạng, không mất dữ liệu gốc.

Minh tái hiện trên REPL:

```python
name = "Nguyễn"
utf8_bytes = name.encode("utf-8")       # b'Nguy\xe1\xbb\x85n'
print(utf8_bytes.hex())                 # 4e677579e1bb856e

# Đúng
print(utf8_bytes.decode("utf-8"))       # Nguyễn

# Sai: coi byte UTF-8 như Latin-1 (mỗi byte = một code point)
print(utf8_bytes.decode("latin-1"))     # Nguyá»…n
```

Ba byte `E1 BB 85` của `ễ` bị đọc lần lượt thành ba ký tự Latin-1: `á`, `»`, `…` — đúng pattern trên screenshot staging. Không có byte nào “mất”; chỉ có **bảng tra sai**.

Một biến thể khác hay gặp: **double encoding** — chuỗi UTF-8 bị decode nhầm thành Latin-1, rồi encode UTF-8 lần nữa trước khi lưu DB. Lúc đó dữ liệu trong bảng **đã hỏng**; sửa header HTTP không cứu được, phải migrate dữ liệu. May cho Minh, `psql` vẫn hiển thị đúng nên byte trong Postgres còn nguyên — lỗi nằm ở driver đọc sang Java.

Bug encoding hiếm khi ném exception có ý nghĩa. Thường chỉ thấy chữ lạ trên UI — giống Joel với email Nhật, giống TaskFlow với tên khách Việt.

<div class="content-box warning-box" markdown="1">
Ký tự thay thế `U+FFFD` xuất hiện khi decoder UTF-8 gặp byte sequence **không hợp lệ** — thường là file bị cắt giữa chừng, hoặc byte Latin-1 bị ép qua UTF-8. Dấu `?` đôi khi là font thiếu glyph, đôi khi là codec thay ký tự không map được — cần xem hex dump, không đoán bằng mắt.
</div>

---

## Pipeline TaskFlow: chỗ nào phải thống nhất encoding

Sáng hôm sau Minh trace từng hop:

1. **PostgreSQL** — database encoding `UTF8`; byte trên disk là UTF-8.
2. **JDBC** — đọc text từ server; nếu connection string không ép `characterEncoding=UTF-8`, một số stack mặc định Latin-1 hoặc platform encoding.
3. **Jackson / Spring** — serialize `String` Java (UTF-16 nội bộ) ra JSON; body JSON **theo chuẩn RFC là UTF-8**.
4. **Browser** — parse JSON dưới giả định UTF-8 khi `Content-Type` có `charset=utf-8`.

Postgres và browser đồng ý UTF-8. JDBC là đoạn lệch — đủ để `String` trong JVM đã sai trước khi tới JSON.

Anh thêm `?characterEncoding=UTF-8` vào JDBC URL, redeploy. Tên hiển thị lại đúng. Product owner gửi emoji thumbs-up.

Joel nhắc từ 2003: máy không đoán charset nếu bạn không nói. Trên thực tế, mỗi lớp có chỗ khai báo riêng — thiếu một lớp là đủ:

HTTP response nên có `Content-Type: application/json; charset=utf-8`. HTML cần `<meta charset="UTF-8">`. Email multipart cần `Content-Type: text/plain; charset="UTF-8"` trên từng part — Joel sửa FogBUGZ vì thư viện bỏ qua đúng chỗ này. MySQL dùng `utf8mb4` (không phải `utf8` cũ chỉ 3 byte/chữ — đủ cắt emoji và một số ký tự CJK). PostgreSQL: `UTF8` trên cluster và client encoding khớp nhau.

Trong code, quy ước an toàn: **byte vào** → `decode` với charset biết chắc (từ header, metadata file, hoặc hợp đồng API); **text trong RAM** (Python 3 `str`, Java `String`) → đã là Unicode code unit sequence; **byte ra** → `encode("utf-8")` trừ khi format bắt buộc khác (UTF-16 cho một số API Windows cũ). Không `str(bytes)` hay `new String(bytes)` khi chưa chỉ encoding — đó là cách tái hiện mojibake có chủ ý trong demo, và vô tình trong production.

Minh ghi vào notebook ba câu ngắn:

**Unicode** — chữ là số (`U+xxxx`). **UTF-8** — số đó ghi thành byte nào trên dây. **Charset trong header / JDBC / DB** — hai đầu cùng biết đang dùng quy tắc nào.

Không có văn bản thuần. Chỉ có byte và quy ước.

**Đọc thêm:** [Joel on Software — Unicode (2003)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) · [Unicode Standard — Character Encoding Forms](https://www.unicode.org/versions/Unicode15.0.0/ch03.pdf) · [Lịch sử UTF-8 — Ken Thompson](http://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt)

Bài sau: cùng code point `U+0048`, hai máy lưu byte **ngược thứ tự** — endianness, BOM, và vì sao log binary đọc timestamp sai năm.