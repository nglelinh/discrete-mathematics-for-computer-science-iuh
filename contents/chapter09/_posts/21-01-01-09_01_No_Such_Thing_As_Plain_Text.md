---
layout: post
title: "Unicode và encoding"
categories: chapter09
date: 2021-01-01
order: 1
required: false
lang: en
excerpt: "Phân tách hai lớp Unicode (ký tự ứng với mã số nào) và encoding (mã số đó được ghi thành dãy byte nào), giải thích nguyên nhân lỗi mojibake trong hệ thống thực tế."
---

Một buổi chiều thứ Sáu yên bình ở team backend, bài test vừa xanh hết thì Product Owner chụp màn hình gửi lên Slack: tên khách hàng `Nguyễn Thị Lan` bỗng biến hình thành `Nguyá»…n Thá»‹ Lan`! Lỗi hiển thị chữ quái dị ấy (**mojibake**) không phải do "phông chữ bị lỗi" hay "cơ sở dữ liệu hỏng" — nó bắt nguồn từ định lý vàng của Joel Spolsky năm 2003: **không hề tồn tại thứ gọi là "văn bản thuần" (plain text) nếu bạn không nói rõ bảng mã (encoding)!**

**Mạch bài học:** Kiến thức cần nhớ (tách bạch 2 lớp: Unicode Code Point vs. Byte Encoding, thiết kế tự đồng bộ của UTF-8) → Câu chuyện TaskFlow & lịch sử ASCII/UTF-8/UTF-16 → Ví dụ tính tay làm từng bước: tự tay mã hóa chữ `'ễ'` (`U+1EC5`) ra đúng 3 byte UTF-8 `E1 BB 85` và tái hiện lỗi `Nguyá»…n`! → Giải thích: 3 bước dập tắt mojibake tận gốc trong đường ống Web/DB → Tóm tắt & Video.

## Kiến thức cần nhớ: Unicode và Encoding giải quyết bài toán gì?

### 1. Lớp 1 — Unicode (Bảng ánh xạ Ký tự $$\to$$ Số nguyên Code Point)
**Unicode** KHÔNG quy định cách lưu byte trên đĩa! Nó chỉ là một cuốn danh bạ toàn cầu gán cho mỗi ký tự trên thế giới một mã số duy nhất gọi là **code point** `U+XXXX`: ví dụ `'A'` là `U+0041` (65), `'ễ'` là `U+1EC5`, emoji `'😀'` là `U+1F600`.

### 2. Lớp 2 — Encoding (Quy tắc đóng gói Code Point thành dãy Byte)
**Encoding** (như **UTF-8**, **UTF-16**, **Windows-1252**) mới là thuật toán biến con số `U+XXXX` thành 1, 2, 3 hoặc 4 byte cụ thể! Cùng một chữ `'ễ'` nhưng UTF-8 ghi thành 3 byte (`E1 BB 85`), còn UTF-16LE ghi thành 2 byte (`C5 1E`).

### 3. Thiết kế thiên tài của UTF-8 (Ken Thompson & Rob Pike, 1992)
UTF-8 thống trị hơn 98% trang web toàn cầu nhờ ba tính chất toán học: (1) tương thích ngược 100% với ASCII 7-bit (`0xxxxxxx`), (2) **tự đồng bộ** (byte đầu luôn bắt đầu bằng `110`, `1110`, `11110`, còn byte tiếp nối luôn là `10xxxxxx` — nên nhìn vào giữa luồng byte vẫn tìm lại được ranh giới ký tự!), và (3) không bị ảnh hưởng bởi endianness!

Ở mục trước, chúng ta đã thấy mọi dữ liệu trong RAM cuối cùng đều là **bit** và **byte**; chương trình mới là bên quyết định đọc chúng thành số, ảnh hay chữ. Mục này đi sâu vào trường hợp **văn bản**: không có dãy byte nào tự mang nhãn “tôi là ký tự Unicode”. Chúng ta cần phân tách rõ hai lớp — **Unicode** (ký tự ứng với mã số nào) và **encoding** (mã số đó được ghi thành dãy byte nào) — vì sự nhầm lẫn giữa hai lớp này là nguyên nhân phổ biến gây ra lỗi hiển thị chữ (**mojibake**) trong các hệ thống thực tế.

Trong tuần đầu tiên làm backend cho **TaskFlow**, Minh triển khai tính năng hiển thị tên khách hàng lên trang quản trị staging. API trả về JSON đúng lược đồ, bài kiểm thử vượt qua, QA xác nhận ổn. Nhưng chiều thứ Sáu, Product Owner gửi một ảnh chụp màn hình vào Slack:

> Sao `Nguyễn Thị Lan` lại hiển thị thành `Nguyá»…n Thá»‹ Lan`?

Không ai chỉnh sửa cơ sở dữ liệu và cũng không có sự cố xâm nhập nào. Minh mở `psql` và chạy `SELECT name FROM customers WHERE id = 42` — kết quả vẫn là `Nguyễn Thị Lan`. Lỗi không nằm trong bảng dữ liệu mà nằm trên đường truyền giữa PostgreSQL, driver JDBC, bộ tuần tự hóa JSON và trình duyệt. Tuần trước, Minh từng nghĩ đoạn này đơn giản là “chỉ trả chuỗi ra frontend”.

Để khắc phục triệt để, kỹ sư cần tách bạch hai khái niệm thường bị gộp chung: **Unicode** (mỗi ký tự ứng với mã số nào) và **encoding** (mã số đó được mã hóa thành những byte nào). Mục này tập trung vào hai khái niệm đó để làm rõ vì sao lỗi encoding thường xảy ra âm thầm và vì sao một email tiếng Nhật có thể biến thành hàng loạt dấu `????` khi thiếu khai báo `charset`.

Toàn bộ đường đi từ văn bản con người đọc được xuống dãy byte trên đĩa — và chiều ngược lại khi giải mã — được tóm gọn trong sơ đồ sau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/UTF-8_Encoding_Scheme.png"
       alt="Sơ đồ UTF-8 — code point được mã hóa thành 1–4 byte theo quy tắc prefix bit"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.1a: Unicode xác định “ký tự ứng với mã số nào”, còn UTF-8 xác định “ghi mã số đó thành những byte nào”; giải mã cùng một dãy byte bằng sai bảng mã sẽ tạo ra mojibake (nguồn: <a href="https://commons.wikimedia.org/wiki/File:UTF-8_Encoding_Scheme.png">Callidus / Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

Cần ghi nhớ ba lớp xử lý: **bộ ký tự** (character repertoire) gán mã số cho từng ký tự; **encoding** chuyển mã số đó thành dãy byte; **decoding** chuyển ngược dãy byte thành ký tự — và chỉ cho kết quả đúng khi cả hai đầu cùng thống nhất một bảng mã. Minh sẽ áp dụng đúng sơ đồ này để truy vết JDBC và trình duyệt ở cuối bài.

---

## Joel Spolsky và nhận định về “văn bản thuần”

Năm 2003, Joel Spolsky xử lý một lỗi hiển thị email tiếng Nhật trong **FogBUGZ**. Thư viện phân tích email khi đó bỏ qua tiêu đề `charset`, chuyển thẳng từ dãy byte sang ký tự hiển thị mà không chọn đúng bảng mã, khiến toàn bộ chữ Kanji biến thành `????`. Nhà cung cấp thư viện không sửa lỗi này. Từ sự cố đó, Joel viết [bài blog kinh điển](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) mà các lập trình viên vẫn thường dẫn lại mỗi khi gặp lỗi hiển thị chữ.

Thông điệp cốt lõi của bài viết là: **There Ain't No Such Thing As Plain Text** — trên máy tính không tồn tại “văn bản thuần”. Dù mở tệp `.txt`, gõ vào ô trò chuyện hay nhận JSON từ API, lớp bên dưới vẫn chỉ là **dãy byte**. Một tệp “văn bản” thực chất chỉ là thỏa thuận ngầm giữa bên ghi và bên đọc rằng “đây là UTF-8” hoặc “đây là Windows-1252”. Nếu thỏa thuận này không được khai báo rõ, máy tính buộc phải đoán; khi đoán sai, kết quả sẽ là mojibake (`Nguyá»…n`), ký tự thay thế `U+FFFD`, hoặc dấu `?` khi phông chữ hay bộ mã hóa không biểu diễn được ký tự.

Đọc bài viết của Joel vào nửa đêm, Minh hiểu ngay nguyên nhân: `SELECT` trong `psql` vẫn hiển thị đúng nhưng JSON trên trình duyệt lại lỗi vì hai đầu đường ống đang áp dụng **hai quy ước giải mã khác nhau** cho cùng một dãy byte.

---

## Unicode: bảng mã số, không phải định dạng tệp

**Unicode** là tiêu chuẩn gán một **code point** (mã số định danh) cho hầu hết ký tự dùng trong văn bản trên thế giới: chữ Latin, Cyrillic, Kanji, ký hiệu toán học, emoji… Ký hiệu `U+` biểu thị mã số viết ở hệ thập lục phân: chữ `H` là `U+0048`, `ă` là `U+0103`, chữ Kanji `字` là `U+5B57`, còn emoji 🎉 là `U+1F389`.

Unicode chỉ trả lời một câu hỏi duy nhất: **“Ký tự này có mã số bao nhiêu?”** Nó **không** quy định mã số đó chiếm bao nhiêu byte trên đĩa, thứ tự byte ra sao, hay dữ liệu JSON trên đường truyền trông như thế nào. Phần việc đó thuộc về **encoding** (như UTF-8, UTF-16…).

Nhiều người vẫn lầm tưởng rằng Unicode luôn chiếm 2 byte cho mỗi ký tự. Thực tế, Unicode **không** quy định độ dài byte cố định. Chuỗi `Hello` trong Unicode đơn thuần là dãy năm code point: `U+0048`, `U+0065`, `U+006C`, `U+006C`, `U+006F`. Đây mới là lớp trừu tượng, chưa phải tệp tin trên đĩa hay gói tin HTTP.

Với tên `Nguyễn`, Minh tách ra từng code point như sau:

`U+004E` (N) · `U+0067` (g) · `U+0075` (u) · `U+0079` (y) · `U+1EC5` (ễ) · `U+006E` (n)

Ở đây, chữ `ễ` là **một** code point ở dạng **dựng sẵn** (precomposed). Unicode còn cho phép biểu diễn theo cách khác: ghép `U+0065` (e) + `U+0302` (dấu mũ) + `U+0303` (dấu ngã). Hai cách biểu diễn hiển thị giống hệt nhau trên màn hình nhưng có **dãy code point khác nhau**, kéo theo dãy byte sau khi mã hóa cũng khác nhau. Các chuỗi trông giống nhau với mắt người như vậy được gọi là cùng **grapheme**, dù khác **biểu diễn Unicode**. Chuẩn **chuẩn hóa chuỗi** (normalization — NFC, NFD) quy định thống nhất dạng biểu diễn khi so sánh, lưu cơ sở dữ liệu hoặc lập chỉ mục tìm kiếm; nếu bỏ qua bước này, `Nguyễn` (dựng sẵn) và `Nguyẽ̂n` (tổ hợp dấu) có thể không khớp nhau dù người dùng nhìn thấy cùng một tên.

Unicode cũng chia không gian code point thành các **mặt phẳng** (plane): Plane 0 (BMP, từ `U+0000` đến `U+FFFF`) chứa hầu hết ký tự thông dụng hằng ngày, còn các mặt phẳng bổ sung chứa emoji và chữ viết cổ. Các code point vượt quá `U+FFFF` (như `U+1F389`) không thể biểu diễn gọn trong một đơn vị 16-bit, điều này tác động trực tiếp đến **UTF-16** (sẽ bàn kỹ hơn về cặp thay thế surrogate pair và endianness ở bài sau).

<div class="content-box insight-box textbook-block" markdown="1">
Theo góc nhìn toán rời rạc, tập hợp các code point Unicode là miền xác định (domain), còn **encoding** là hàm $$f$$ ánh xạ một chuỗi code point sang dãy byte. Hiển thị đúng văn bản đồng nghĩa với việc cả hai đầu hệ thống đều dùng cùng một hàm $$f$$ và hàm ngược $$f^{-1}$$, chứ không phải “đọc chữ có sẵn trong byte”.
</div>

---

## Encoding: cách ghi mã số thành byte

Nếu Unicode là một cuốn danh bạ gán số cho từng ký tự, thì **encoding** là quy tắc ghi các con số trong danh bạ đó thành dãy byte để lưu xuống tệp, truyền qua socket hoặc trao đổi với driver cơ sở dữ liệu.

### ASCII và thời kỳ “mỗi vùng một bảng mã”

Vào thập niên 1970, **ASCII** chuẩn hóa 128 ký tự đầu tiên (giá trị 0–127), gồm chữ Latin không dấu, chữ số và các dấu câu cơ bản (ví dụ `A` = 65, khoảng trắng = 32).

![Bảng ASCII — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_ascii.png)

<p class="textbook-figure-caption" data-figure="9.1">ASCII — bảng mã cho ký tự tiếng Anh không dấu trong phạm vi 0–127 (Joel on Software).</p>

Các ký tự tiếng Việt như `ă`, `ê`, `ố` **không tồn tại** trong ASCII. Một byte 8 bit có 256 giá trị, nhưng ASCII chỉ dùng nửa đầu (0–127). Với nửa sau (128–255), **mỗi khu vực lại tự định nghĩa một bảng mã riêng** (code page, OEM, Windows-1252, ISO-8859-1…). Joel kể về từ **résumé** trong email: byte `0xE9` hiển thị là `é` trên máy tại Mỹ, nhưng trên máy tại Israel lại có thể hiển thị thành chữ cái Hebrew — **cùng một byte, khác ký tự** vì thiếu siêu dữ liệu chỉ rõ bảng mã.

![OEM character set — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_oem.png)

<p class="textbook-figure-caption" data-figure="9.2">Vùng byte 128–255 — mỗi khu vực dùng một bảng mã khác nhau (Joel on Software).</p>

Unicode ra đời nhằm tạo ra **một** danh bạ thống nhất cho mọi ngôn ngữ. Tuy nhiên, có chung danh bạ vẫn chưa giải quyết xong khâu lưu trữ: hệ thống vẫn cần thống nhất **cách ghi mã `U+xxxx` thành byte**, dẫn đến sự xuất hiện của các chuẩn mã hóa như UTF-8, UTF-16 hay Latin-1.

### UTF-8: độ dài biến đổi và tương thích ASCII

**UTF-8** là bảng mã **độ dài biến đổi**, sử dụng từ 1 đến 4 byte cho mỗi code point.

Quy tắc cốt lõi đủ để đọc hex dump và gỡ lỗi:

- `U+0000`–`U+007F` (trùng hoàn toàn với ASCII): **1 byte**, bit cao nhất là `0` (ví dụ `A` vẫn là `41`).
- `U+0080`–`U+07FF`: **2 byte**, mẫu bit `110xxxxx 10xxxxxx`.
- `U+0800`–`U+FFFF`: **3 byte**, mẫu bit `1110xxxx 10xxxxxx 10xxxxxx`.
- Trên `U+FFFF`: **4 byte**, mẫu bit `11110xxx` theo sau là ba byte có dạng `10xxxxxx`.

Ví dụ, ký tự `é` (`U+00E9`) trong UTF-8 được mã hóa thành `C3 A9` (2 byte), còn trong **Latin-1** (ISO-8859-1) chỉ là `E9` (1 byte). Hai tệp hiển thị cùng một ký tự nhưng có **nội dung nhị phân khác nhau**; khi chạy `diff`, công cụ sẽ báo khác biệt dù mắt người thấy giống nhau.

Với tên `Nguyễn`, code point `U+1EC5` (ễ) được UTF-8 mã hóa thành ba byte `E1 BB 85`. Toàn bộ chuỗi trở thành:

```text
4E 67 75 79 E1 BB 85 6E   ← UTF-8 của "Nguyễn"
```

Phần lớn nền tảng web, API, JSON, Git, Linux và PostgreSQL hiện đại mặc định dùng UTF-8 vì ba lý do: văn bản tiếng Anh vẫn giữ nguyên độ gọn 1 byte như ASCII; tiếng Việt, tiếng Nhật và emoji đều biểu diễn được mà không cần chọn code page theo quốc gia; và UTF-8 không phụ thuộc vào thứ tự byte (endianness) như UTF-16.

![Cách UTF-8 hoạt động — Joel on Software](/discrete-mathematics-for-computer-science-iuh/img/course/joel_utf8.png)

<p class="textbook-figure-caption" data-figure="9.4">UTF-8 — ký tự ASCII chiếm 1 byte, các ký tự quốc tế chiếm nhiều byte hơn (Joel on Software).</p>

### UTF-16 và kiểu `String` trong Java

**UTF-16** mã hóa phần lớn ký tự thuộc BMP bằng **2 byte** mỗi code point (ví dụ `H` → `00 48`) và dùng **surrogate pair** (4 byte) cho các code point ngoài BMP. Bên trong JVM, kiểu `String` sử dụng biểu diễn UTF-16; vì thế, dữ liệu “đã là Unicode trong RAM” ở Java **không** đồng nghĩa với “đã là UTF-8 trên đường truyền”. Khi JDBC đọc cột `VARCHAR` từ PostgreSQL, driver phải **giải mã byte từ giao thức mạng** sang UTF-16 trong bộ nhớ heap; chỉ cần cấu hình sai `charset` ở bước này là tên tiếng Việt đã bị hỏng dù cơ sở dữ liệu lưu hoàn toàn đúng.

---

## Mojibake: hậu quả của việc giải mã sai bảng mã

Tiếng Nhật gọi hiện tượng này là **mojibake** (文字化け): dãy byte được **giải mã bằng một encoding khác** với encoding đã dùng khi mã hóa, khiến chữ hiển thị biến dạng dù dữ liệu byte gốc chưa hề mất.

Minh tái hiện lỗi trực tiếp trên Python REPL:

```python
name = "Nguyễn"
utf8_bytes = name.encode("utf-8")       # b'Nguy\xe1\xbb\x85n'
print(utf8_bytes.hex())                 # 4e677579e1bb856e

# Đúng
print(utf8_bytes.decode("utf-8"))       # Nguyễn

# Sai: coi byte UTF-8 như Latin-1 (mỗi byte = một code point)
print(utf8_bytes.decode("latin-1"))     # Nguyá»…n
```

Ba byte `E1 BB 85` của chữ `ễ` bị hiểu nhầm thành ba ký tự Latin-1 rời nhau: `á`, `»`, `…` — khớp chính xác với ảnh chụp màn hình trên staging. Không có byte nào bị mất, chỉ có **bảng tra bị chọn sai**.

Một biến thể nghiêm trọng hơn là **mã hóa kép** (double encoding): chuỗi UTF-8 bị giải mã nhầm thành Latin-1 rồi lại bị mã hóa sang UTF-8 lần nữa trước khi ghi vào cơ sở dữ liệu. Khi đó dữ liệu trong bảng **đã bị hỏng thực sự**, không thể sửa chỉ bằng cách chỉnh tiêu đề HTTP mà phải chạy kịch bản chuyển đổi dữ liệu (migration). May mắn cho Minh là `psql` vẫn hiển thị đúng, chứng tỏ dãy byte trong PostgreSQL còn nguyên vẹn và lỗi chỉ xảy ra khi driver đọc dữ liệu sang Java.

Lỗi encoding hiếm khi ném ra ngoại lệ rõ ràng; biểu hiện thường thấy chỉ là các ký tự lạ trên giao diện — giống sự cố email tiếng Nhật của Joel hay tên khách hàng Việt trên TaskFlow.

<div class="content-box warning-box textbook-block" markdown="1">
Ký tự thay thế `U+FFFD` xuất hiện khi bộ giải mã UTF-8 gặp một dãy byte **không hợp lệ** — thường do tệp bị cắt ngang hoặc byte Latin-1 bị ép giải mã bằng UTF-8. Trong khi đó, dấu `?` có thể xuất phát từ việc phông chữ thiếu glyph hoặc bộ mã hóa thay thế các ký tự không ánh xạ được. Khi gỡ lỗi, hãy kiểm tra hex dump thay vì đoán bằng mắt.
</div>

---

## Đường ống TaskFlow: những điểm phải thống nhất encoding

Sáng hôm sau, Minh kiểm tra lần lượt từng chặng trong hệ thống:

1. **PostgreSQL** — cơ sở dữ liệu dùng encoding `UTF8`; dãy byte lưu trên đĩa là UTF-8.
2. **JDBC** — đọc văn bản từ máy chủ DB; nếu chuỗi kết nối không chỉ rõ `characterEncoding=UTF-8`, một số cấu hình có thể rơi về Latin-1 hoặc encoding mặc định của hệ điều hành.
3. **Jackson / Spring** — tuần tự hóa `String` Java (UTF-16 nội bộ) thành JSON; theo chuẩn RFC, nội dung JSON phải là UTF-8.
4. **Trình duyệt** — phân tích JSON theo UTF-8 khi tiêu đề `Content-Type` có `charset=utf-8`.

PostgreSQL và trình duyệt đều thống nhất UTF-8, nhưng JDBC lại lệch bảng mã — đủ để chuỗi `String` trong JVM bị sai ngay trước khi đưa sang bộ tạo JSON.

Minh bổ sung `?characterEncoding=UTF-8` vào JDBC URL rồi triển khai lại. Tên khách hàng hiển thị chính xác trở lại và Product Owner xác nhận đã hết lỗi.

Như Joel Spolsky đã lưu ý từ năm 2003, máy tính không thể tự đoán đúng `charset` nếu lập trình viên không khai báo rõ. Trong thực tế, mỗi tầng đều có vị trí khai báo riêng và chỉ cần bỏ sót một tầng là lỗi có thể xảy ra:

Phản hồi HTTP cần có tiêu đề `Content-Type: application/json; charset=utf-8`. Trang HTML cần thẻ `<meta charset="UTF-8">`. Email nhiều phần (multipart) cần khai báo `Content-Type: text/plain; charset="UTF-8"` trên từng phần — đúng vị trí mà thư viện trong FogBUGZ từng bỏ qua. Với MySQL, cần dùng `utf8mb4` (vì kiểu `utf8` cũ của MySQL chỉ hỗ trợ tối đa 3 byte/ký tự, làm mất emoji và một số ký tự CJK). Với PostgreSQL, cần đảm bảo cả cluster lẫn client encoding đều thống nhất là `UTF8`.

Trong mã nguồn, nguyên tắc an toàn gồm ba bước: **byte đi vào** → `decode` bằng bảng mã đã biết chắc (từ tiêu đề, siêu dữ liệu tệp hoặc đặc tả API); **văn bản trong RAM** (kiểu `str` trong Python 3, `String` trong Java) → xử lý dưới dạng chuỗi đơn vị mã Unicode; **byte đi ra** → `encode("utf-8")`, trừ khi định dạng đích bắt buộc bảng mã khác (như UTF-16 ở một số API Windows cũ). Tránh gọi `str(bytes)` hay `new String(bytes)` mà không chỉ định encoding rõ ràng.

Minh ghi lại ba dòng tóm tắt vào sổ tay:

**Unicode** — ký tự ứng với mã số nào (`U+xxxx`). **UTF-8** — mã số đó được ghi thành dãy byte nào trên đường truyền. **Charset trong header / JDBC / DB** — bảo đảm hai đầu hệ thống cùng dùng một quy tắc.

Không có văn bản thuần — chỉ có byte và quy ước.

**Đọc thêm:** [Joel on Software — Unicode (2003)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) · [Unicode Standard — Character Encoding Forms](https://www.unicode.org/versions/Unicode15.0.0/ch03.pdf) · [Lịch sử UTF-8 — Ken Thompson](http://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt)

---


## Ví dụ tính tay làm từng bước: Mã hóa chữ `'ễ'` (`U+1EC5`) sang UTF-8 và tái hiện lỗi `Nguyá»…n`!

Hãy tự tay thực hiện quy tắc UTF-8 cho chữ **`'ễ'`** trong tên `Nguyễn`:
1. **Lấy mã Unicode:** `'ễ'` = `U+1EC5`. Vì `U+0800 <= U+1EC5 <= U+FFFF`, UTF-8 dùng mẫu **3 byte**: `1110xxxx 10xxxxxx 10xxxxxx` (chứa đúng $$4 + 6 + 6 = 16$$ bit).
2. **Đổi `0x1EC5` sang 16 bit nhị phân:**
   $$
   \texttt{1} = \texttt{0001},\quad \texttt{E} = \texttt{1110},\quad \texttt{C} = \texttt{1100},\quad \texttt{5} = \texttt{0101}
   \;\Longrightarrow\;
   \underbrace{\texttt{0001}}_{4\text{ bit}}\;\underbrace{\texttt{111011}}_{6\text{ bit}}\;\underbrace{\texttt{000101}}_{6\text{ bit}}.
   $$
3. **Điền vào mẫu 3 byte UTF-8:**
   - Byte 1: `1110` + `0001` = `11100001` = **`0xE1`**
   - Byte 2: `10` + `111011` = `10111011` = **`0xBB`**
   - Byte 3: `10` + `000101` = `10000101` = **`0x85`**
4. **Giải mã hiện trường vụ án mojibake:** Nếu trình duyệt hoặc DB đọc nhầm 3 byte `E1 BB 85` theo bảng mã **Windows-1252** (1 byte = 1 ký tự): `0xE1` là **`á`**, `0xBB` là **`»`**, `0x85` là **`…`** $$\implies$$ **`Nguyễn` lập tức biến thành `Nguyá»…n`!!**

### Giải thích: 3 bước truy tìm và khóa chặt Mojibake trong hệ thống thực tế
#### Bước 1: Không bao giờ đoán — kiểm tra dãy byte thô bằng hex!
Thấy chữ Việt 1 ký tự bị bung thành 3 ký tự lạ (`á»…`, `Ã¡`)? Đó là dấu vân tay 100% của **UTF-8 bị giải mã nhầm thành Latin-1 / Windows-1252**! Còn nếu hiện `????` thì ký tự đã bị *phá hủy mất dữ liệu* do cột DB dùng `latin1` hoặc `utf8` 3-byte cũ (MySQL cần `utf8mb4` để lưu emoji 4-byte!).

#### Bước 2: Khóa chuẩn UTF-8 tại mọi đường biên giao tiếp
Đảm bảo đồng bộ ở cả 4 điểm chạm: kết nối DB (`charset=utf8mb4`), HTTP header (`Content-Type: application/json; charset=utf-8`), đọc/ghi tệp (`encoding="utf-8"`), và thẻ `<meta charset="utf-8">` trên HTML.

#### Bước 3: Phân biệt `len(s)` theo code point, UTF-16 code unit và số byte UTF-8
Trong Python, `len("😀") == 1` (1 code point), trong JavaScript/Java `"😀".length == 2` (2 đơn vị UTF-16 surrogate pair), còn `len("😀".encode("utf-8")) == 4` (4 byte)! Không hiểu sự khác biệt này là nguồn gốc của hàng loạt lỗi cắt chuỗi gây hỏng JSON!

$$
\text{Ký tự } \texttt{'ễ'}
\;\xrightarrow{\text{Unicode}}\;
\texttt{U+1EC5}
\;\xrightarrow{\text{UTF-8}}\;
\texttt{E1 BB 85}
\;\xrightarrow{\text{Đọc nhầm Win-1252}}\;
\texttt{á»…}\ (\text{Mojibake!}).
$$

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)

## Tóm tắt

- Trên máy tính không có “văn bản thuần” — chỉ có **byte** và **quy ước** encoding.
- **Unicode** gán **code point** ($$U+xxxx$$) cho từng ký tự; **UTF-8** mã hóa code point thành 1–4 byte trên đường truyền.
- **Mojibake** xảy ra khi giải mã bằng bảng mã khác với bảng mã lúc mã hóa; dữ liệu gốc trong cơ sở dữ liệu thường vẫn còn nguyên.
- Toàn bộ đường ống xử lý phải thống nhất `charset`: tiêu đề HTTP, JDBC, PostgreSQL và MIME email.
- **Chuẩn hóa chuỗi** (NFC/NFD) cần thiết khi so sánh và lập chỉ mục chuỗi Unicode.

Trong bài tiếp theo, chúng ta sẽ xét **endianness** — trường hợp hai máy tính lưu cùng một code point `U+0048` hoặc cùng một số nguyên theo thứ tự byte ngược nhau, cùng vai trò của BOM và lý do log nhị phân có thể đọc sai năm của timestamp.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=MijmeoH9LT4">Characters, Symbols and the Unicode Miracle - Computerphile</a> — Computerphile, tiếng Anh. Giải thích Unicode là bảng gán mã số cho ký tự chứ không phải một định dạng tệp.
- <a href="https://www.youtube.com/watch?v=ut74oHojxqo">Unicode, in friendly terms: ASCII, UTF-8, code points, character encodings, and more</a> — Studying With Alex, tiếng Anh. Trình bày rõ ASCII, code point và cách UTF-8 mã hóa thành byte.
- <a href="https://www.youtube.com/watch?v=0j74jcxSunY">Internationalis(z)ing Code - Computerphile</a> — Computerphile, tiếng Anh. Phân tích lỗi lệch bảng mã khi phần mềm vượt ra ngoài phạm vi ASCII, liên quan trực tiếp đến hiện tượng mojibake.
