---
layout: post
title: "Endianness và Byte Order Mark: Khi cùng một số, hai cách lưu"
categories: chapter09
date: 2021-01-01
order: 2
required: false
lang: en
excerpt: "Phân tích hai quy ước sắp xếp byte trong bộ nhớ (big-endian và little-endian), vai trò của Byte Order Mark trong UTF-16 và chuẩn network byte order trên mạng."
---

Cùng một con số 32-bit `0x12345678` nằm gọn trong 4 ô RAM liên tiếp từ địa chỉ `1000` đến `1003` — nhưng nếu bạn chạy code trên máy chủ x86/ARM thông thường rồi gửi thẳng 4 byte đó qua mạng sang một bộ định tuyến chuẩn mạng (network byte order), hai máy sẽ đọc ra **hai con số khác nhau một trời một vực**!

Hiện tượng đó gọi là **Endianness** (thứ tự byte: **Big-Endian** đặt byte có trọng số cao nhất trước, còn **Little-Endian** đặt byte thấp nhất trước). Hiểu rõ endianness giúp bạn giải mã đúng mọi gói tin TCP/IP, tệp ảnh/âm thanh nhị phân (WAV, PNG) và chuỗi UTF-16 có Byte Order Mark (BOM).

**Mạch bài học:** Bản đồ kiến thức nền (Big-Endian vs. Little-Endian, Network Byte Order RFC 1700, BOM trong UTF-16) → Vì sao cả hai quy ước cùng tồn tại & ví dụ log của Lan → Ví dụ tính tay cầm tay chỉ việc: khi quên `htons()` biến cổng HTTP `80` thành `20480`! → Khung giải thích chậm: 3 nguyên tắc vàng tránh lỗi đảo byte khi lập trình mạng & đọc tệp nhị phân → Bài tập thực hành.

## Bản đồ kiến thức nền: Thứ tự Byte (Endianness) trong Kiến trúc Máy tính và Mạng

### 1. Big-Endian vs. Little-Endian — chỉ áp dụng cho thứ tự BYTE, không đảo BIT!
Với số 32-bit `0x12345678` (gồm 4 byte `12`, `34`, `56`, `78`):
- **Big-Endian:** lưu `12 34 56 78` (giống cách con người viết từ trái sang phải; dễ đọc hex dump).
- **Little-Endian:** lưu `78 56 34 12` (chuẩn của CPU x86-64 và đa số ARM hiện đại; thuận lợi khi ép kiểu xuống số nguyên nhỏ hơn ở cùng địa chỉ gốc!).

### 2. Network Byte Order = Big-Endian
Để máy Little-Endian và Big-Endian nói chuyện được với nhau trên Internet, mọi giao thức mạng tiêu chuẩn (IP, TCP, UDP) thống nhất dùng **Big-Endian** — đó là lý do C/Python có các hàm chuyển đổi `htons()` / `htonl()` (*host-to-network*) và ký hiệu `>` trong `struct.pack(">I", ...)`.

### 3. Endianness trong văn bản UTF-16 và vai trò của BOM (`0xFEFF`)
Vì UTF-8 đọc từng byte một nên **không có vấn đề endianness**. Ngược lại, UTF-16 lưu từng đơn vị 2 byte nên có hai biến thể **UTF-16BE** và **UTF-16LE** — cần 2 byte mở đầu **BOM** (`FE FF` cho BE, `FF FE` cho LE) để báo cho trình đọc biết thứ tự byte.

Ở bài Unicode, chúng ta đã tách hai lớp: Unicode cho biết ký tự ứng với mã số nào, còn encoding cho biết ghi mã số đó thành dãy byte ra sao. Câu hỏi tương tự cũng xuất hiện với **số nguyên** như timestamp, cổng mạng hay độ dài gói tin. Khi một số cần nhiều hơn một byte để lưu trữ, máy tính phải quy ước byte nào đứng trước và byte nào đứng sau trong bộ nhớ. Hai cách sắp xếp đó gọi là **big-endian** và **little-endian**, và khái niệm chung gọi là **endianness** (thứ tự byte).

Ý cốt lõi cần giữ xuyên suốt bài này là: **cùng một giá trị số có thể được lưu trong RAM theo hai thứ tự byte khác nhau.** Nếu đọc nhầm quy ước — chẳng hạn dùng `struct.unpack(">I", ...)` cho một tệp ghi theo little-endian — một timestamp hoàn toàn hợp lệ có thể bị hiểu thành năm 2286 dù các byte trong tệp không hề thay đổi. Nắm vững quy ước này giúp tránh những lỗi khó phát hiện khi đọc tệp nhị phân, phân tích tiêu đề gói tin mạng hoặc sao chép chuỗi UTF-16 giữa các hệ thống khác nhau.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/32bit-Endianess.svg"
       alt="Số nguyên 32-bit 0x0A0B0C0D lưu trong RAM theo big-endian và little-endian"
       width="65%" height="65%">
  <figcaption style="text-align: center;">Hình 9.2a: Cùng một giá trị số nhưng có hai cách sắp xếp byte trong RAM; đọc sai quy ước đủ để timestamp nhảy sang năm 2286 như trường hợp của Lan (nguồn: <a href="https://commons.wikimedia.org/wiki/File:32bit-Endianess.svg">Aeroid / Wikimedia Commons</a>, CC BY-SA 4.0).</figcaption>
</p>
</figure>

## Vì sao một số cần nhiều byte?

Ô nhớ nhỏ nhất được địa chỉ hóa là **byte**, chỉ biểu diễn được số nguyên không dấu từ 0 đến 255. Với số lớn hơn 255, một byte không đủ chứa. Chẳng hạn, số **4660** viết trong hệ thập lục phân là **0x1234**, cần **hai byte**: một byte mang phần `12` và một byte mang phần `34`.

Trong hai byte này, `12` gọi là **byte cao** (MSB — phần có trọng số lớn hơn, tương tự chữ số hàng cao trong số thập phân) và `34` gọi là **byte thấp** (LSB — phần có trọng số nhỏ hơn). Khi viết `0x1234` trên giấy, ta luôn viết `12` trước rồi đến `34`. Nhiều người mới học thường mặc định máy tính cũng lưu trong bộ nhớ đúng theo thứ tự đó, nhưng thực tế không phải lúc nào cũng như vậy.

## Địa chỉ 1000 chứa `12` — bên trong ô nhớ có gì?

Khi tài liệu viết “ô `1000` chứa `12`”, nhiều người dễ hiểu lầm rằng trong RAM lưu hai ký tự `1` và `2`, hoặc cả số `1234` nằm trọn trong một ô nhớ. Thực tế không phải vậy.

**Địa chỉ bộ nhớ** (ví dụ `1000`, `1001`) giống như số nhà trên một dãy phố dài là RAM. Mỗi địa chỉ trỏ tới **đúng một ô**, và mỗi ô lưu **đúng một byte** — tức **8 bit** (tám vị trí mang mức điện áp cao `1` hoặc thấp `0`). Không có ô nhớ đơn lẻ nào chứa trọn số `1234`; số lớn bắt buộc phải **tách** sang nhiều ô liền kề.

Giá trị hex **`0x12`** là cách viết gọn của số **18** trong hệ thập phân. Nói ô `1000` “chứa `12`” nghĩa là **toàn bộ ô đó** đang mang giá trị 18. Ở tầng phần cứng, tám bit bên trong ô đó có trạng thái:

`0001 0010` (nhị phân)

Bit ngoài cùng bên trái có trọng số lớn nhất trong byte, còn bit ngoài cùng bên phải có trọng số nhỏ nhất. Phần cứng không lưu ký hiệu `12` như trên giấy mà lưu **mẫu điện áp** trên tám đường dây; công cụ hex dump chỉ chuyển đổi mẫu bit đó thành hai ký tự `1` và `2` để con người dễ đọc.

Ô kế tiếp tại địa chỉ `1001` chứa byte **`0x34`** (bằng 52 ở hệ thập phân), với mẫu 8 bit là `0011 0100`. Hai ô `1000` và `1001` nằm cạnh nhau trong RAM. Khi CPU cần đọc một số nguyên 16-bit bắt đầu từ địa chỉ `1000`, nó lấy giá trị tại `1000`, lấy tiếp giá trị tại `1001`, rồi **ghép** chúng lại theo quy ước endian để thu được `0x1234`.

![Một ô nhớ chứa byte 0x12](/discrete-mathematics-for-computer-science-iuh/img/course/memory_byte_12.svg)

<p class="textbook-figure-caption" data-figure="9.4">Một địa chỉ tương ứng một byte gồm 8 bit; `0x12` là cách viết hex của giá trị lưu trong ô.</p>

<div class="content-box insight-box textbook-block" markdown="1">
Có ba lớp cần phân biệt rõ: **(1)** giá trị toán học `4660` (viết gọn `0x1234`); **(2)** từng **byte** `0x12` và `0x34` nằm trong từng ô nhớ; **(3)** bên trong mỗi byte là **8 bit** nhị phân. Endianness chỉ quy định byte `0x12` và `0x34` nằm ở ô `1000` hay `1001`, chứ không đảo thứ tự bit bên trong từng byte.
</div>

---

## Big-endian — sắp xếp giống cách viết trên giấy

**Big-endian** đặt byte cao ở **địa chỉ bộ nhớ thấp hơn** (tức ô nhớ đứng trước khi đọc từ trái sang phải).

Quay lại ví dụ số `0x1234` lưu từ địa chỉ `1000`: theo big-endian, ô `1000` chứa byte `0x12` (`0001 0010`) và ô `1001` chứa byte `0x34` (`0011 0100`). Khi xem hex dump, ta thấy `12 34` — trùng khớp với thứ tự viết trên giấy. CPU đọc ô `1000` lấy phần cao, đọc ô `1001` lấy phần thấp rồi ghép thành `0x1234`.

Một số kiến trúc phần cứng và phần lớn **giao thức mạng** sử dụng big-endian. Khi hai máy tính trao đổi dữ liệu qua Internet, việc thống nhất “byte cao trước” giúp hai bên hiểu cùng một giá trị mà không phải đoán.

![Sơ đồ 16-bit big vs little](/discrete-mathematics-for-computer-science-iuh/img/course/endian_16bit_1234.svg)

*Hình 9.5a: Cùng giá trị `0x1234` nhưng được sắp xếp theo hai thứ tự byte khác nhau trong RAM.*

---

## Little-endian — byte thấp đứng trước

**Little-endian** sắp xếp ngược lại: byte **thấp** (`0x34`) nằm ở ô có địa chỉ **thấp hơn**, còn byte **cao** (`0x12`) nằm ở ô kế tiếp.

Với cùng số `0x1234` trên hai ô `1000` và `1001`, ô `1000` nay chứa `0x34` và ô `1001` chứa `0x12`. Hex dump hiển thị `34 12`. Lỗi phổ biến nhất là đọc thẳng từ trái sang phải thành `0x3412` — tương ứng **13330**, hoàn toàn sai lệch. Để đọc đúng trên máy little-endian, cần nhớ ô đứng trước là byte thấp và ô đứng sau là byte cao, rồi mới ghép thành `0x1234`.

Phần lớn máy tính cá nhân hiện nay — chạy Windows, Linux hoặc macOS trên bộ xử lý Intel x86 hay Apple Silicon — đều dùng **little-endian**. Do đó, khi kiểm tra RAM lúc lập trình trên PC, dãy byte thường trông “ngược” so với cách viết hex trên giấy; đây là quy ước phần cứng chứ không phải lỗi.

<div class="content-box warning-box textbook-block" markdown="1">
Không nên nhầm little-endian với việc “đảo ngược từng bit”. Thứ tự bit bên trong mỗi byte vẫn giữ nguyên; chỉ **thứ tự các byte** (2 byte, 4 byte, 8 byte…) khi ghép thành một số lớn mới đảo ngược. Giá trị 4660 không đổi, chỉ vị trí ô nhớ giữ `12` và `34` đổi chỗ cho nhau.
</div>

---

### Minh họa thứ tự byte: big-endian và little-endian

Nhập một số hex 32-bit để quan sát 4 byte được phân bố vào các địa chỉ bộ nhớ theo từng kiểu endian; khi đọc sai kiểu, giá trị thu được sẽ khác hẳn.

<div class="interactive-demo" markdown="1">
<div data-demo="bits-explainer" data-tab="endian"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Vì sao cả hai quy ước cùng tồn tại?

Một câu hỏi tự nhiên là: **vì sao không chọn duy nhất một kiểu cho toàn bộ hệ thống máy tính?** Lý do không nằm ở việc kiểu nào “đúng” hay “sai”. Cả hai đều là **quy ước thiết kế** mà các nhóm kỹ sư lựa chọn khi xây dựng vi xử lý và giao thức trong thập niên 1970–1980. Khi đã có hàng triệu thiết bị, định dạng tệp và phần mềm phụ thuộc vào từng quy ước, chi phí chuyển đổi toàn bộ là quá lớn nên cả hai tiếp tục song hành.

**Big-endian** trực quan khi đọc hex dump vì thứ tự byte khớp với cách viết số trên giấy (`12` trước, `34` sau). Các hệ thống mainframe, một số dòng chip MIPS/PowerPC và đặc biệt là **giao thức mạng** trên Internet chọn kiểu này để mọi máy khác hãng có thể giao tiếp thống nhất. Nhiều đặc tả RFC và định dạng tệp như PNG đều giữ quy ước “byte cao trước”.

**Little-endian** lại thuận tiện cho cách CPU thực hiện phép toán nhiều byte. Nhiều phép tính như cộng hoặc nhân xử lý tuần tự từ **byte thấp** lên **byte cao** (tương tự cách cộng từ hàng đơn vị lên hàng chục). Việc đặt byte thấp ở địa chỉ nhỏ hơn giúp dòng vi xử lý Intel x86 từ năm 1978 đọc dữ liệu thuận lợi theo chiều địa chỉ tăng dần. Các máy tính cá nhân hiện đại kế thừa kiến trúc này nên RAM trên PC chủ yếu là little-endian.

Vì không có một quy ước duy nhất trên toàn cầu, cách xử lý thực tế trong kỹ thuật phần mềm là **ghi rõ thứ tự byte trong đặc tả định dạng** (tệp dùng big hay little), **thống nhất một chuẩn chung trên đường truyền mạng** (big-endian) và sử dụng **hàm chuyển đổi** trong mã nguồn (như `htonl`, `ntohl` trong C hoặc ký hiệu `<`, `>` trong Python). Lập trình viên cần luôn kiểm tra “byte nào đứng trước” thay vì mặc định mọi hệ thống giống máy cục bộ.

<div class="content-box note-box textbook-block" markdown="1">
Có thể liên hệ với cách ghi ngày tháng giữa các quốc gia: `21/06/2026` và `06/21/2026` biểu diễn cùng một ngày, không cách nào sai về mặt toán học mà chỉ khác **quy ước ghi**. Khi trao đổi dữ liệu, hai bên buộc phải nói rõ định dạng đang dùng — endianness cũng tương tự.
</div>

---

## Cùng một số, hai dãy byte — ví dụ trong tệp log của Lan

Mở rộng sang số nguyên 32-bit (4 byte), nguyên tắc vẫn giữ nguyên. Số 4660 viết đầy đủ ở dạng 32-bit hex là `0x00001234`. Trên máy PC little-endian, bốn byte trong tệp là `34 12 00 00` — byte thấp nhất `34` đứng đầu, các byte `00` đứng sau.

Lan đọc đúng giá trị này bằng Python như sau:

```python
import struct
data = bytes.fromhex("34 12 00 00")
struct.unpack("<I", data)   # '<' nghĩa là little-endian
```

Ký hiệu `<` trong `struct` báo cho Python đọc bốn byte theo quy ước little-endian, trả về `(4660,)`.

Nếu tệp được ghi theo chuẩn mạng (big-endian), bốn byte sẽ là `00 00 12 34` và cần đọc bằng `struct.unpack(">I", ...)` với ký hiệu `>` chỉ big-endian.

Sự cố của Lan xảy ra khi dùng `>` cho một tệp thực chất được ghi theo `<`. Bốn byte vật lý trong tệp hoàn toàn chính xác, nhưng việc ghép nhầm thứ tự tạo ra một giá trị số khác hẳn — đủ khiến timestamp nhảy sang năm 2286. Không có phép tính nào sai, chỉ có **quy ước đọc bị lệch**.

![Endianness 32-bit](/discrete-mathematics-for-computer-science-iuh/img/course/32bit-Endianess.svg)

*Hình 9.5b: Với số nhiều byte hơn, nguyên lý vẫn là hai chiều sắp xếp byte trong bộ nhớ.*

---

## Endianness ảnh hưởng đến văn bản UTF-16

Nhắc lại bài Unicode: trong UTF-16, phần lớn ký tự thuộc phạm vi cơ bản chiếm **hai byte**. Ký tự `H` có mã Unicode `U+0048`, gồm hai byte hex là `00` và `48`. Lúc này câu hỏi về thứ tự byte lại xuất hiện: `00` đứng trước hay `48` đứng trước?

Theo big-endian, tệp lưu `00 48`; theo little-endian, tệp lưu `48 00`. Cả chuỗi `Hello` cũng khác nhau tương ứng (`00 48 00 65…` so với `48 00 65 00…`). Khi sao chép tệp giữa các máy mà không rõ chiều ghi, văn bản có thể hiển thị thành ô vuông, ký tự lạ hoặc không đọc được.

Vì bản thân chuỗi byte UTF-16 không tự khai báo thứ tự byte, chuẩn Unicode quy định có thể đặt thêm hai byte đặc biệt ở **đầu tệp** gọi là **BOM** (Byte Order Mark). Nếu hai byte đầu là `FE FF`, tệp dùng UTF-16 big-endian; nếu là `FF FE`, tệp dùng UTF-16 little-endian. Ví dụ, chuỗi `He` theo UTF-16 little-endian bắt đầu bằng `FF FE`, tiếp theo là `48 00` (chữ `H`) và `65 00` (chữ `e`). Nếu bỏ qua hoặc hiểu sai BOM, toàn bộ phần nội dung phía sau sẽ bị giải mã sai.

Ngược lại, UTF-8 không chịu ảnh hưởng của endianness vì mỗi ký tự được đọc tuần tự theo từng byte đơn lẻ thay vì ghép theo đơn vị 16-bit. Do đó, endianness chủ yếu cần lưu ý khi làm việc với **số nguyên nhiều byte** và **tệp UTF-16**.

---

## Trên mạng, các hệ thống thống nhất một chuẩn chung

Khi hai máy có endianness khác nhau trao đổi số cổng (như 8080) hoặc độ dài gói tin, nếu máy gửi truyền nguyên thứ tự byte trong RAM của mình và máy nhận đọc theo RAM của máy nhận, giá trị sẽ bị sai lệch. Giải pháp tiêu chuẩn được dùng từ lâu trên Internet là luôn truyền theo **big-endian**, gọi là **network byte order**.

Trên máy PC little-endian, chương trình chuyển đổi dữ liệu sang dạng mạng trước khi gửi và chuyển ngược về dạng máy cục bộ sau khi nhận. Ngôn ngữ C cung cấp sẵn các hàm `htonl` (host to network, long) và `ntohl` (network to host). Nguyên tắc rất rõ ràng: **không để các máy tự suy đoán; mọi dữ liệu trên đường truyền mạng đều tuân theo một quy ước chung.**

![Mô hình OSI](/discrete-mathematics-for-computer-science-iuh/img/course/OSI_Model_v1.svg)

<p class="textbook-figure-caption" data-figure="9.6">Trong tiêu đề gói tin mạng, mọi trường số nhiều byte đều phải được diễn giải theo cùng một thứ tự byte.</p>

---

## Làm sao biết tệp hoặc API dùng quy ước nào?

Không có “tệp nhị phân thuần” dùng chung một thứ tự byte ngầm định trên mọi máy; mỗi định dạng đều ghi rõ quy ước trong đặc tả. Ví dụ, chuẩn PNG quy định độ dài mỗi khối dữ liệu là số 4 byte **big-endian**. Lớp `ByteBuffer` trong Java cũng có thứ tự byte mặc định riêng (big-endian), nên lập trình viên cần chủ động gọi `buf.order(ByteOrder.BIG_ENDIAN)` hoặc `LITTLE_ENDIAN` theo đúng yêu cầu đặc tả.

Trong Python, ký hiệu `<` trong `struct.unpack` biểu thị little-endian, `>` biểu thị big-endian, và `I` biểu thị số nguyên không dấu 32-bit. Do đó, `struct.unpack("<I", data)` đọc 4 byte theo kiểu PC, còn `struct.unpack(">I", data)` đọc theo chuẩn mạng hoặc nhiều định dạng tệp truyền thống.

Khi đọc tệp nhị phân hoặc phân tích bộ đệm dữ liệu, luôn tra cứu tài liệu đặc tả để biết **byte nào được ghi trước**, thay vì suy đoán theo endianness của máy đang chạy.

---


## Ví dụ tính tay cầm tay chỉ việc: Khi quên `htons()` biến cổng HTTP `80` thành `20480`!

Giả sử bạn viết một chương trình socket trên máy tính x86 (**Little-Endian**) và gửi cổng HTTP **$$80$$** (kiểu 16-bit không dấu `uint16`) mà quên chuyển sang Network Byte Order (**Big-Endian**):
1. **Đổi $$80$$ sang 2 byte hex:** $$80 = 5 \times 16 + 0 = \texttt{0x0050}$$ (byte cao = `0x00`, byte thấp = `0x50`).
2. **Máy Little-Endian ghi ra RAM theo thứ tự:** `50 00`.
3. **Router / máy nhận đọc theo chuẩn mạng Big-Endian (`50` là byte cao, `00` là byte thấp):**
   $$
   \texttt{0x5000} = 5 \times 16^3 = 5 \times 4096 = \mathbf{20{,}480}!
   $$
Chỉ vì quên đúng 1 lời gọi `htons(80)` (hoặc `struct.pack(">H", 80)`), gói tin của bạn đã lao thẳng vào cổng **20480** thay vì cổng **80**!

### Khung giải thích: 3 nguyên tắc vàng để không bao giờ dính lỗi Endianness (nên đọc chậm)

#### Bước 1: Không bao giờ ép con trỏ struct C gửi thẳng ra mạng hay ghi thẳng ra đĩa
Luôn tuần tự hóa tường minh từng trường số nguyên với thứ tự byte quy định rõ (ví dụ `struct.pack(">I", ts)` cho Big-Endian hoặc `struct.pack("<I", ts)` cho Little-Endian trong Python).

#### Bước 2: Dùng phép dịch bit độc lập kiến trúc khi tự viết parser
Nếu bạn đọc 4 byte `b0, b1, b2, b3` theo chuẩn Big-Endian, công thức `(b0 << 24) | (b1 << 16) | (b2 << 8) | b3` cho kết quả **giống hệt nhau trên mọi CPU** (dù máy chạy x86 Little-Endian hay mainframe Big-Endian)!

#### Bước 3: Kiểm tra đặc tả định dạng tệp trước khi giải mã
Gói tin TCP/IP, PNG, Java bytecode dùng **Big-Endian**; tệp WAV (PCM), ELF x86, Windows BMP và bộ nhớ x86 dùng **Little-Endian**; còn văn bản web luôn ưu tiên **UTF-8** để triệt tiêu hoàn toàn bài toán endianness!

$$
\text{Số } \texttt{0x0050}\ (80)
\;\xrightarrow{\text{Little-Endian RAM}}\;
\texttt{50 00}
\;\xrightarrow{\text{Đọc nhầm Big-Endian}}\;
\texttt{0x5000}\ (20{,}480!).
$$

## Bài tập thực hành

### Bài tập 1

Trong bộ nhớ, ô `0x1000` chứa byte `34` và ô `0x1001` chứa byte `12`. Máy sử dụng little-endian. Giá trị số nguyên không dấu 16-bit là bao nhiêu?

<details>
<summary>Đáp án</summary>

Little-endian đặt byte thấp ở địa chỉ thấp hơn: ô `0x1000` là `34` (byte thấp), ô `0x1001` là `12` (byte cao). Ghép lại ta được `0x1234`, bằng **4660** trong hệ thập phân.

</details>

### Bài tập 2

Với cùng hai byte `34` và `12` ở bài trên, nếu đọc nhầm theo big-endian (ghép từ trái sang phải thành một số hex), kết quả thu được là bao nhiêu?

<details>
<summary>Đáp án</summary>

Đọc theo big-endian sẽ ghép `34` trước rồi đến `12`, tạo thành `0x3412` = **13330**. Mức sai lệch so với giá trị đúng 4660 rất lớn, đủ làm timestamp hoặc số cổng mạng nhảy sang một giá trị vô nghĩa.

</details>

### Bài tập 3

Viết một đoạn mã Python ngắn đọc bốn byte `34 12 00 00` thành số nguyên không dấu 32-bit theo kiểu little-endian.

<details>
<summary>Đáp án</summary>

```python
import struct
struct.unpack("<I", bytes.fromhex("34 12 00 00"))
```

Ký hiệu `<` chỉ little-endian và `I` chỉ số nguyên không dấu 32-bit. Kết quả trả về là `(4660,)`.

</details>

### Bài tập 4

Một tệp bắt đầu bằng dãy byte `FE FF 00 48`. Đây là UTF-16 kiểu nào? Hai byte ngay sau BOM biểu diễn ký tự gì?

<details>
<summary>Đáp án</summary>

`FE FF` là BOM của UTF-16 **big-endian**. Hai byte `00 48` ghép theo big-endian tạo thành code point `U+0048`, tương ứng với ký tự **H**.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Endianness là quy ước sắp xếp thứ tự các byte của cùng một giá trị số trong bộ nhớ. **Big-endian** đặt byte cao ở địa chỉ thấp hơn (giống cách viết hex trên giấy), còn **little-endian** đặt byte thấp ở địa chỉ thấp hơn (phổ biến trên phần lớn máy tính cá nhân hiện nay). Đọc nhầm quy ước khiến dãy byte hợp lệ bị hiểu thành một giá trị hoàn toàn sai, như sự cố timestamp năm 2286 của Lan.

Văn bản UTF-16 cũng chịu ảnh hưởng của endianness vì mỗi đơn vị mã chiếm 2 byte; do đó BOM ở đầu tệp được dùng để khai báo thứ tự byte. Trên mạng Internet, các giao thức thống nhất dùng big-endian (network byte order). Khi lập trình, cần đối chiếu đặc tả định dạng và chỉ rõ thứ tự byte (như `<` hoặc `>` trong Python `struct`).

Trong bài tiếp theo, chúng ta sẽ chuyển sang **số nguyên có dấu trong máy tính**: vì sao cộng thêm 1 giây vào timestamp 32-bit có thể kéo đồng hồ lùi về năm 1901 — cơ chế của sự cố Year 2038 và cách biểu diễn số âm bằng bù hai (two's complement).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=NcaiHcBvDR4">Endianness Explained With an Egg - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu trực quan big-endian và little-endian trên số nhiều byte.
- <a href="https://www.youtube.com/watch?v=LxvFb63OOs8">Endianness Explained</a> — Aaron Yoo, tiếng Anh. Trình bày thứ tự byte trong bộ nhớ theo hai cách sắp xếp của bài.
- <a href="https://www.youtube.com/watch?v=T1C9Kj_78ek">Lecture 22. Big Endian and Little Endian</a> — Embedded Systems and Deep Learning, tiếng Anh. So sánh hai kiểu endian qua ví dụ địa chỉ bộ nhớ cụ thể.
