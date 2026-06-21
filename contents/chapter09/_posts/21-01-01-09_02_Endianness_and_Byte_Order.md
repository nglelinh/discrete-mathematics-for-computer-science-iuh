---
layout: post
title: "Endianness và Byte Order Mark: Khi cùng một số, hai cách lưu"
categories: chapter09
date: 2021-01-01
order: 2
required: false
lang: en
---

Tuần thực tập, Lan mở file log mà team backend gửi từ server khác. Trong file có một dãy byte ghi thời điểm sự kiện xảy ra. Lan viết vài dòng Python để đọc, chạy thử — kết quả nhảy tới năm 2286. Cô sửa code, đổi một ký tự trong lệnh `unpack`, chạy lại — ra đúng ngày giờ. Không ai ghi sai số vào file. Chỉ có điều: Lan lần đầu **đọc byte theo thứ tự mà máy cô không dùng**.

Bài trước (09_01) nói về chữ: Unicode cho biết ký tự là số nào, encoding cho biết ghi số đó thành byte thế nào. Bài này gặp câu hỏi tương tự, nhưng với **số nguyên** — timestamp, cổng mạng, độ dài gói tin. Khi một số cần nhiều hơn một byte, máy tính phải quyết định: byte nào đứng trước, byte nào đứng sau trong bộ nhớ? Hai cách xếp đó gọi là **big-endian** và **little-endian**. Cả lớp quy ước này gọi chung là **endianness** (thứ tự byte).

Nếu bạn mới học năm 1 hoặc năm 2, hãy đọc bài theo một ý chính: **cùng một giá trị số, nhưng có thể được cất trong RAM theo hai kiểu xếp byte khác nhau.** Hiểu được điều đó là đủ để tránh hàng loạt lỗi khó thấy khi đọc file binary, làm mạng, hoặc copy chữ UTF-16 giữa hai máy.

---

## Vì sao một số cần nhiều byte?

Một ô nhớ nhỏ nhất gọi là **byte**, lưu được số từ 0 đến 255. Số lớn hơn 255 thì một byte không đủ. Ví dụ số **4660** viết trong hệ hexadecimal là **0x1234** — tức là cần **hai byte**: một byte mang phần `12`, một byte mang phần `34`.

Trong hai byte đó, người ta gọi `12` là **byte cao** (MSB — phần “nặng” hơn, giống chữ số hàng chục trong số thập phân) và `34` là **byte thấp** (LSB — phần “nhẹ” hơn, giống hàng đơn vị). Khi bạn viết `0x1234` lên giấy, bạn luôn viết `12` trước rồi mới đến `34`. Nhiều sinh viên mới học cũng mặc định máy tính sẽ cất trong bộ nhớ y hệt như vậy. Thực tế không phải lúc nào cũng thế — và đó chính là chỗ gây nhầm.

---

## Địa chỉ 1000 chứa `12` — bên trong ô nhớ là gì?

Khi bài học viết “ô `1000` chứa `12`”, nhiều bạn hình dung sai: tưởng trong RAM có chữ `1` và chữ `2`, hoặc tưởng số `1234` nằm trọn trong một ô. Không phải vậy.

**Địa chỉ** (ví dụ `1000`, `1001`) giống **số nhà** trên một con phố dài gọi là RAM. Mỗi số nhà trỏ tới **đúng một ô**, và mỗi ô lưu **đúng một byte** — tức **8 bit** (tám chỗ chỉ được điện cao `1` hoặc thấp `0`). Không có ô nào lưu cả số `1234` một lần; số lớn phải **chia** ra nhiều ô liền kề.

Giá trị hex **`0x12`** là cách viết gọn của số **18** trong hệ thập phân. Khi nói ô `1000` “chứa `12`”, ý là **cả ô đó** đang mang giá trị 18. Bên trong phần cứng, tám bit của ô đó ở trạng thái:

`0001 0010` (nhị phân)

Bit bên trái là bit “nặng” nhất của byte, bit bên phải là bit “nhẹ” nhất. Máy không lưu ký hiệu `12` như trong sách; nó lưu **mẫu điện** trên tám đường dây. Khi bạn xem hex dump, công cụ chỉ **dịch** mẫu đó ra hai ký tự `1` và `2` cho dễ đọc.

Ô kế tiếp, địa chỉ `1001`, chứa byte **`0x34`** (tức 52 thập phân), với tám bit khác: `0011 0100`. Hai ô `1000` và `1001` **đứng cạnh nhau** trên con phố RAM. Khi CPU cần đọc một số 16-bit bắt đầu tại `1000`, nó lấy nội dung ô `1000`, lấy nội dung ô `1001`, rồi **ghép** theo quy tắc endian — đó mới thành `0x1234`.

![Một ô nhớ chứa byte 0x12](/discrete-mathematics-for-computer-science-iuh/img/course/memory_byte_12.svg)

*Hình 9.4: Một địa chỉ = một byte = 8 bit. `0x12` là cách viết hex của giá trị lưu trong ô.*

<div class="content-box insight-box" markdown="1">
Tóm lại ba tầng dễ lẫn: **(1)** số toán học `4660` hay `0x1234`; **(2)** từng **byte** `0x12`, `0x34` trong từng ô nhớ; **(3)** bên trong mỗi byte là **8 bit** nhị phân. Endianness chỉ nói byte `0x12` và `0x34` nằm ở ô `1000` hay `1001` — không đổi bit bên trong từng byte.
</div>

---

## Big-endian — xếp giống cách viết trên giấy

**Big-endian** nghĩa là: byte cao được đặt ở **địa chỉ bộ nhớ thấp hơn** (ô nhớ đứng trước khi bạn đọc từ trái sang phải).

Quay lại ví dụ trên: số `0x1234` được cất bắt đầu từ ô `1000`. Với big-endian, ô `1000` chứa byte `0x12` (tám bit `0001 0010`), ô `1001` chứa byte `0x34` (tám bit `0011 0100`). Hex dump hiện `12 34` — đúng thứ tự viết trên giấy. CPU đọc ô `1000` trước, lấy phần cao; đọc ô `1001` sau, lấy phần thấp; ghép lại được `0x1234`.

Một số hệ thống và nhiều **chuẩn trên mạng** dùng big-endian. Khi hai máy trao đổi dữ liệu qua Internet, người ta thường thống nhất kiểu “byte cao trước” để không ai phải đoán.

![Sơ đồ 16-bit big vs little](/discrete-mathematics-for-computer-science-iuh/img/course/endian_16bit_1234.svg)

*Hình 9.5a: Cùng số 0x1234, nhưng hai cách xếp trong RAM.*

---

## Little-endian — byte thấp đứng trước

**Little-endian** làm ngược lại: byte **thấp** (`0x34`) nằm ở ô có địa chỉ **thấp hơn**, byte **cao** (`0x12`) nằm ở ô kế tiếp.

Cùng số `0x1234`, cùng hai ô `1000` và `1001`, nhưng lần này ô `1000` chứa `0x34`, ô `1001` chứa `0x12`. Hex dump hiện `34 12`. Sinh viên mới hay mắc lỗi ở đây: nhìn `34 12` mà vẫn ghép trái sang phải thành `0x3412` — ra số **13330**, hoàn toàn sai. Muốn đọc đúng trên máy little-endian, bạn phải biết quy tắc: ô trước là byte thấp, ô sau là byte cao, rồi mới ghép thành `0x1234`.

Phần lớn máy tính cá nhân hôm nay — Windows, Linux, Mac trên chip Intel hoặc Apple Silicon — dùng **little-endian**. Vì vậy khi bạn học lập trình trên PC, dãy byte trong RAM thường “trông ngược” so với cách viết hex trên giấy. Đó không phải bug; đó là quy ước phần cứng.

<div class="content-box warning-box" markdown="1">
Đừng nhầm little-endian với “đảo ngược từng bit”. Bên trong mỗi byte, bit vẫn xếp bình thường. Chỉ có **thứ tự hai byte** (hoặc bốn byte, tám byte…) khi ghép thành một số lớn là đổi chỗ. Số 4660 vẫn là 4660; thay đổi duy nhất là ô nhớ nào giữ `12`, ô nào giữ `34`.
</div>

---

## Tại sao lại tồn tại cả hai cách?

Câu hỏi tự nhiên sau khi biết big và little: **sao không chọn một kiểu cho cả thế giới?** Lý do không phải vì một kiểu “sai” và kiể kia “đúng”. Cả hai đều là **quy ước** — cách các nhóm kỹ sư khác nhau quyết định xếp byte khi thiết kế chip và giao thức, từ những thập niên 1970–1980. Khi đã có hàng triệu máy, file, và chương trình chạy theo một quy ước, đổi toàn bộ rất tốn kém — nên hai kiểu cùng tồn tại đến hôm nay.

**Big-endian** được nhiều người thấy “tự nhiên” vì hex dump đọc giống cách viết số trên giấy: `12` trước, `34` sau. Các máy mainframe, một số chip MIPS/PowerPC, và đặc biệt **giao thức mạng** (Internet) chọn kiểu này để hai máy khác hãng nói chuyện mà không phải đoán. Khi bạn đọc tài liệu RFC hay spec file PNG, thường gặp quy ước “byte cao trước” — đó là di sản của lựa chọn này.

**Little-endian** xuất phát từ cách CPU làm việc với số nhiều byte. Nhiều phép tính (cộng, nhân từng bước) xử lý từ **bit/byte thấp** lên **byte cao** — giống bạn cộng số từ hàng đơn vị lên hàng chục. Đặt byte thấp ở địa chỉ nhỏ hơn giúp vi xử lý Intel (x86) từ thập niên 1978 tiện khi đọc tuần tự địa chỉ tăng dần. PC phổ biến ngày nay kế thừa dòng quy ước đó, nên RAM máy bạn thường là little-endian.

Hai hãng, hai thời điểm, hai ưu tiên thiết kế — không có cuộc họp toàn cầu bắt buộc thống nhất. Kết quả: thế giới thật **lẫn cả hai**. Giải pháp thực tế không phải “chọn một kiểu và xóa kiểu kia”, mà là **ghi rõ trong spec** (file này big hay little), **quy ước chung trên dây mạng** (luôn big-endian), và **hàm chuyển đổi** trong code (`htonl`, `ntohl`, dấu `<` / `>` trong Python). Lập trình viên học cách hỏi “byte nào trước?” thay vì giả định mọi nơi giống máy mình.

<div class="content-box note-box" markdown="1">
Có thể hình dung như hai quốc gia viết ngày-tháng: `21/06/2026` hay `06/21/2026`. Cùng một ngày, không ai sai toán — chỉ khác **thói quen ghi**. Khi trao đổi, phải nói rõ đang dùng format nào; endianness cũng vậy.
</div>

---

## Cùng một số, hai dãy byte — ví dụ Lan gặp trong file log

Mở rộng sang số 32-bit (bốn byte), nguyên tắc không đổi. Số 4660 đầy đủ viết là `0x00001234`. Trên PC little-endian, bốn byte trong file có thể là `34 12 00 00` — byte thấp nhất `34` đứng đầu, các byte `00` đứng sau.

Lan đọc đúng bằng Python như sau:

```python
import struct
data = bytes.fromhex("34 12 00 00")
struct.unpack("<I", data)   # '<' nghĩa là little-endian
```

Dấu `<` trong `struct` là cách Python nói: “hãy đọc bốn byte theo kiểu little-endian”. Kết quả là `(4660,)`.

Nếu file được ghi theo chuẩn mạng (big-endian), bốn byte sẽ là `00 00 12 34` — trông giống cách viết trên giấy hơn. Đọc đúng bằng `struct.unpack(">I", ...)` với dấu `>` nghĩa là big-endian.

Vấn đề của Lan là dùng `>` trên file mà thực tế được ghi kiểu `<`. Cùng bốn byte vật lý trong file, nhưng hiểu nhầm thứ tự → ra số khác hoàn toàn, có thể thành timestamp năm 2286. Không có phép tính sai; chỉ có **đọc sai quy ước**.

![Endianness 32-bit](/discrete-mathematics-for-computer-science-iuh/img/course/32bit-Endianess.svg)

*Hình 9.5b: Khi số dài hơn, vẫn chỉ là chuyện xếp nhiều byte theo hai chiều.*

---

## Endianness cũng ảnh hưởng tới chữ (UTF-16)

Bài 09_01 giới thiệu UTF-16: mỗi ký tự (trong phạm vi cơ bản) thường chiếm **hai byte**. Chữ `H` có mã Unicode `U+0048`, tức hai byte hex là `00` và `48`. Câu hỏi endian lại xuất hiện: byte `00` đứng trước hay byte `48` đứng trước?

Với big-endian, file chứa `00 48`. Với little-endian, file chứa `48 00`. Cùng một chữ `H`, nhưng nhìn hex dump đã khác. Cả chuỗi `Hello` cũng vậy — một máy có thể ghi `00 48 00 65…`, máy kia ghi `48 00 65 00…`. Copy file qua USB mà không biết máy ghi theo kiểu nào, chữ có thể thành ô vuông, ký tự lạ, hoặc mất hẳn.

Vì UTF-16 không tự giải thích “tôi là kiểu nào”, chuẩn Unicode khuyên ghi thêm vài byte đặc biệt ở **đầu file** gọi là **BOM** (Byte Order Mark). Nếu hai byte đầu là `FE FF`, file là UTF-16 big-endian. Nếu là `FF FE`, file là UTF-16 little-endian. Ví dụ chuỗi “He” kiểu little-endian bắt đầu bằng `FF FE`, rồi đến `48 00` cho chữ H và `65 00` cho chữ e. Đọc nhầm endian sau BOM thì toàn bộ phần còn lại của file sẽ sai.

UTF-8 ít dính chuyện endian hơn vì mỗi ký tự là dãy byte đọc tuần tự từ trái sang, không chia thành “cặp byte 16-bit” như UTF-16. Endian chủ yếu làm phiền khi làm việc với **số nguyên nhiều byte** và **file UTF-16**.

---

## Trên mạng, mọi người thống nhất một kiểu

Hai máy khác endian gửi cho nhau số cổng 8080 hoặc độ dài gói tin. Nếu máy A gửi byte theo RAM của A, máy B đọc theo RAM của B, kết quả lệch ngay. Giải pháp lâu đời: trên dây mạng luôn dùng **big-endian**, gọi là **network byte order**.

Trên PC little-endian, trước khi gửi đi bạn chuyển sang dạng mạng, sau khi nhận về bạn chuyển lại dạng máy mình. Trong C có sẵn hàm `htonl` (host to network, long) và `ntohl` (network to host). Tên hàm nghe khó, nhưng ý rất đơn giản: **đừng để mỗi máy tự đoán; trên dây luôn dùng một quy ước chung.**

![Mô hình OSI](/discrete-mathematics-for-computer-science-iuh/img/course/OSI_Model_v1.svg)

*Hình 9.6: Trong header gói tin, các trường số nhiều byte phải hiểu cùng một thứ tự.*

---

## Làm sao biết file hoặc API dùng kiểu nào?

Không có “file binary thuần” theo nghĩa mọi byte đều giống nhau trên mọi máy. Mỗi định dạng ghi rõ trong tài liệu. File PNG quy định độ dài mỗi khối là bốn byte **big-endian**. Java `ByteBuffer` mặc định có thể khác với RAM PC; bạn phải gọi `buf.order(ByteOrder.BIG_ENDIAN)` nếu spec yêu cầu.

Trong Python, dấu `<` sau lệnh unpack nghĩa là little-endian, dấu `>` là big-endian. Chữ `I` nghĩa là số nguyên không dấu 32 bit. Vì vậy `struct.unpack("<I", data)` đọc bốn byte theo kiểu PC; `struct.unpack(">I", data)` đọc theo kiểu mạng hoặc nhiều file chuẩn cũ.

Thói quen tốt khi mới học: mỗi lần mở file binary hoặc parse buffer, hãy hỏi **“tài liệu nói byte nào trước?”** — không đoán theo máy mình.

---

## Bài tập thực hành

### Bài tập 1

Trong bộ nhớ, ô `0x1000` chứa byte `34`, ô `0x1001` chứa byte `12`. Máy dùng little-endian. Số 16-bit là bao nhiêu?

<details>
<summary>Đáp án</summary>

Little-endian đặt byte thấp ở địa chỉ thấp hơn. Ô `1000` là `34` (byte thấp), ô `1001` là `12` (byte cao). Ghép lại được `0x1234`, tức **4660** trong hệ thập phân.

</details>

### Bài tập 2

Cùng hai byte `34` và `12`, nhưng bạn vô tình đọc như big-endian (ghép trái sang phải thành một số hex). Kết quả là gì?

<details>
<summary>Đáp án</summary>

Đọc big-endian nghĩa là ghép `34` rồi `12` thành `0x3412`, tức **13330**. So với đáp án đúng 4660, sai lệch rất lớn — đủ để làm timestamp hoặc mã cổng “nhảy” sang giá trị vô lý.

</details>

### Bài tập 3

Viết một dòng Python đọc bốn byte `34 12 00 00` thành số 32-bit trên PC little-endian.

<details>
<summary>Đáp án</summary>

```python
import struct
struct.unpack("<I", bytes.fromhex("34 12 00 00"))
```

Dấu `<` báo little-endian, chữ `I` là unsigned 32-bit. Kết quả là `(4660,)`.

</details>

### Bài tập 4

File bắt đầu bằng `FE FF 00 48`. Đây là UTF-16 kiểu nào? Ba byte sau BOM có thể là chữ gì?

<details>
<summary>Đáp án</summary>

`FE FF` là BOM của UTF-16 **big-endian**. Hai byte `00 48` ghép theo big-endian là mã `U+0048`, tức chữ **H**.

</details>

---

## Tóm tắt

Endianness là câu chuyện **cùng một số, nhưng xếp byte khác nhau trong RAM**. Big-endian giống cách viết hex trên giấy — byte cao trước. Little-endian đặt byte thấp trước — đây là kiểu phổ biến trên PC bạn đang dùng. Nhầm kiểu đọc thì hex dump vẫn “có vẻ hợp lý” nhưng số ra sai, như Lan thấy với timestamp năm 2286.

Chữ UTF-16 cũng chịu ảnh hưởng vì mỗi ký tự là hai byte; BOM ở đầu file giúp máy biết đọc theo chiều nào. Trên mạng, mọi người thống nhất big-endian để khỏi đoán. Khi code, hãy đọc spec hoặc dùng đúng dấu `<` / `>` trong Python — đó là cách bạn nói với máy: “hãy đọc byte theo thứ tự này”.

Bài sau chúng ta bỏ endian, đi vào **số có dấu trong máy**: cộng một giây vào timestamp 32-bit có thể đưa đồng hồ về năm 1901 — hiện tượng Year 2038 và cách máy lưu số âm bằng two's complement.