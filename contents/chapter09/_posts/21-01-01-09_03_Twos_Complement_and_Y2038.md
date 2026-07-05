---

layout: post
title: "Two's complement và Year 2038: Khi +1 giây phá vỡ thời gian"
categories: chapter09
date: 2021-01-01
order: 3
required: false
lang: en
excerpt: "Ở mục endianness, chúng ta đã thấy cùng một dãy byte có thể đọc ra số khác nhau tùy quy ước thứ tự. Mục này xét biến thể tương tự với số có dấu: cùng các bit…"
---

Ở mục endianness, chúng ta đã thấy cùng một dãy byte có thể đọc ra số khác nhau tùy quy ước thứ tự. Mục này xét biến thể tương tự với **số có dấu**: cùng các bit trong bộ nhớ, máy đọc theo quy tắc **two's complement** (bù hai) để biết số đó dương hay âm. Nhiều hệ thống không lưu “ngày giờ” như hiển thị trên đồng hồ mà lưu **một số nguyên** đếm giây từ epoch Unix (1/1/1970). Mỗi giây trôi qua, số đó tăng thêm 1; khi biến chỉ có **32 bit signed**, giá trị max là $$2^{31}-1$$ tương ứng **19/1/2038, 03:14:07 UTC** — cộng thêm 1 giây sẽ **tràn** và timestamp có thể nhảy về khoảng năm **1901**.

Khác **Y2K** (lưu năm hai chữ số rồi nhầm 1900/2000), **Y2038** là chuyện **ô nhớ đầy**: không sửa bằng “thêm chữ số”, mà phải mở rộng biểu diễn (`int64_t`, `time_t` 64-bit) hoặc thay thiết bị cũ. Ghi nhớ: **thời gian trong máy = số nguyên có biên; +1 ở biên có thể đổi cả thế kỷ.** Minh họa thực tế: firmware PLC, camera IP, và file archive lưu timestamp `int32` vẫn “chạy đúng” năm 2026 nhưng có thể gặp sự cố sau 2038 nếu không được kiểm tra.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Binary_clock.svg"
       alt="Đồng hồ nhị phân — thời gian hiển thị được ghi bằng pattern bit"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.3a: Đồng hồ trên UI là lớp trên cùng; bên dưới là số nguyên có biên — cộng 1 ở max 32-bit signed nhảy sang vùng âm, tức năm 1901 (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Binary_clock.svg">Alexander Jones &amp; Eric Pierce / Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

---

## Unix time — đếm giây từ một ngày bất kỳ

Hầu hết hệ điều hành Unix và nhiều hệ nhúng dùng **Unix time**: số giây đã trôi qua kể từ **00:00:00 UTC ngày 1 tháng 1 năm 1970**, gọi là **epoch**. Không có phép màu ở đây — chỉ là quy ước chọn một mốc 0 rồi đếm tăng dần mỗi giây. Giá trị `0` tương ứng 1970-01-01 00:00:00 UTC. Giá trị `1_000_000_000` tương ứng khoảng 2001-09-09 — mốc “tỷ giây” mà nhiều blog kỹ thuật từng ghi nhận.

Khi biến lưu Unix time là **signed 32-bit integer**, nó chỉ chứa được một **tập số nguyên hữu hạn**. Không phải đồng hồ “sai”; tập đó có đúng $$2^{32}$$ giá trị khác nhau, từ min âm đến max dương theo quy tắc two's complement. Mọi timestamp nằm ngoài dải đó — hoặc không biểu diễn được, hoặc bị wrap theo quy tắc phần cứng — đều là hệ quả của việc **chọn kiểu biến quá nhỏ**, không phải vì UTC bản thân nó hỏng.

![Unix time timeline — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Unix_timeline.en.svg)

<p class="textbook-figure-caption" data-figure="9.11">Unix time tăng đều theo giây — cho đến khi hết bit trong biến 32-bit signed (nguồn: Wikimedia Commons).</p>
Lan nhìn đường thời gian trên hình và thấy điều Planet Mainframe nhấn mạnh: nhiều thiết bị công nghiệp **hoạt động đúng thiết kế** suốt hai thập kỷ nhưng không được nâng cấp trước 2038 vì chi phí recertification — thay firmware PLC có thể cần downtime nhà máy, kiểm định an toàn, và giấy phép vận hành mới. Bug không nằm trong logic điều khiển van; nó nằm trong **ô nhớ đếm giây**.

**Y2K** và **Y2038** nghe giống nhau — cả hai đều là “năm máy tính bị lỗi” — nhưng bản chất khác hẳn:

| | Y2K (2000) | Y2038 |
|:---|:---|:---|
| Nguyên nhân | Lưu năm 2 chữ số | **Tràn** 32-bit signed |
| Bản chất | Quy ước lưu trữ | **Giới hạn toán** |
| Hệ ảnh hưởng | Business apps | **Nhúng**, firmware, PLC, legacy |

Y2K sửa bằng cách thêm hai chữ số vào field năm trong database. Y2038 không có “thêm chữ số” nào cứu được nếu biến vẫn chỉ rộng 32 bit và vẫn đọc theo signed two's complement — chúng ta phải **mở rộng biểu diễn** hoặc **thay phần cứng** đã chạy đúng spec cũ.

## Giới hạn 32-bit — signed hay unsigned?

Một câu hỏi hay gặp trước khi nói tới Year 2038: **32 bit thì số đó giới hạn là bao nhiêu?** Câu trả lời phụ thuộc vào **cách máy đọc** các bit — không chỉ vào số bit.

32 bit, mỗi bit là 0 hoặc 1, nên tổng cộng có đúng $$2^{32} = 4\,294\,967\,296$$ **tổ hợp bit khác nhau**. Nhưng **giá trị số** min/max phụ thuộc kiểu dữ liệu:

| Kiểu | Nhỏ nhất | Lớn nhất | Ý nghĩa với Unix time |
|:---|:---|:---|:---|
| **Signed** (`int32_t`, two's complement) | $$-2^{31} = -2\,147\,483\,648$$ | $$2^{31} - 1 = 2\,147\,483\,647$$ | Overflow **2038** → nhảy **1901** |
| **Unsigned** (`uint32_t`) | $$0$$ | $$2^{32} - 1 = 4\,294\,967\,295$$ | Overflow **~2106** → wrap về **1970** |

**Signed** chia không gian $$2^{32}$$ thành nửa âm và nửa không âm; dải **không đối xứng** — có thể biểu diễn $$+2^{31}-1$$ nhưng không có $$+2^{31}$$, vì pattern tương ứng đã dành cho số âm. **Unsigned** dùng toàn bộ không gian cho số không âm, nên max gần gấp đôi signed max.

Unix timestamp trên hệ cũ thường lưu trong **signed 32-bit**, nên giới hạn quyết định Year 2038 là **2,147,483,647** — không phải 4,294,967,295.

<div class="content-box insight-box textbook-block" markdown="1">
**Ghi nhớ nhanh**: Signed max = **2,147,483,647** (03:14:07 UTC, 19/01/2038); signed min = **−2,147,483,648** (~1901 sau overflow); unsigned max = **4,294,967,295** (overflow ~2106). Cùng 32 bit — khác kiểu đọc, khác ngày “vỡ”.
</div>

---

## Two's complement — khi +1 biến max thành min âm

Số nguyên có dấu trong máy tính hiện đại hầu như luôn dùng **two's complement** (bù hai). Với 32 bit, **một bit** đứng vai trò **sign** (0 = không âm, 1 = âm), **31 bit** còn lại tham gia vào giá trị magnitude theo công thức đặc biệt — không phải “bit dấu riêng, 31 bit giá trị tuyệt đối” như người mới hay tưởng.

Giá trị **lớn nhất** mà 32-bit signed biểu diễn được có bit pattern `0111…111` (31 chữ số 1 sau một số 0):

<div class="textbook-equation" markdown="1">
$$2^{31} - 1 = 2\,147\,483\,647$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đó chính là **03:14:07 UTC ngày 19/01/2038** — giây Unix cuối cùng trước overflow trên biến signed 32-bit. Lan ghi con số này lên bảng trắng trong phòng họp: không phải ngày “ma quái” do ai chọn bừa, mà là **đỉnh của dải số** mà kiểu `int32_t` cho phép.

Cộng thêm 1 vào max — phép cộng nhị phân bình thường, cùng mạch ALU như cộng số không dấu:

```
  0111...111
+ 0000...001
-----------
  1000...000   ← sign bit = 1, các bit khác = 0
```

Pattern `1000…000` trong two's complement không phải “số dương lớn hơn max”. Theo quy tắc đọc, nó là **−2³¹ = −2,147,483,648** — giá trị **âm nhỏ nhất** (magnitude lớn nhất về phía âm) mà 32-bit signed chứa được. Đếm **lùi** 2,147,483,648 giây từ epoch 1970 → ra **1901-12-13 20:45:52 UTC** — con số mà [Planet Mainframe](https://planetmainframe.com/2026/01/inside-the-math-that-will-break-time-the-y2k38-problem/) và [Wikipedia — Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem) đồng thuận. HMI có thể hiển thị năm 1901; log audit ghi timestamp lùi một thế kỷ; job “chạy lúc 03:15” có thể không bao giờ fire vì scheduler nghĩ “thời điểm đó đã qua từ 124 năm trước”.

<div class="content-box warning-box textbook-block" markdown="1">
Trong C, `time_t` overflow trên kiểu signed là **undefined behavior** nếu compiler không đảm bảo wrap — về mặt chuẩn ngôn ngữ, chúng ta không được giả định kết quả. Thực tế hầu hết nền tảng hiện đại wrap theo two's complement, nhưng ứng dụng vẫn thấy thời gian sai dù “phần cứng cộng đúng”. Đừng nhầm “wrap có quy luật” với “ứng dụng vẫn an toàn”.
</div>

Công thức tổng quát cho word $$w$$ bit, với các bit $$b_{w-1} \ldots b_0$$ (bit $$b_{w-1}$$ là sign):

<div class="textbook-equation" markdown="1">
$$
\text{value} = -b_{w-1} \cdot 2^{w-1} + \sum_{i=0}^{w-2} b_i \cdot 2^i
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với $$w=32$$: max dương = $$2^{31}-1$$, min âm = $$-2^{31}$$. Dải **không đối xứng** — có thể biểu diễn $$+2^{31}-1$$ nhưng không có $$+2^{31}$$, vì pattern dương tương ứng đã bị dành cho số âm.

Lan hay dùng mô hình **8-bit** để giải thích cho thực tập sinh mới vào nhà máy: max dương = $$2^7 - 1 = 127$$, pattern `01111111`. Cộng 1 → `10000000` = **−128**, không phải 128. Cùng mạch cộng, cùng dãy bit — chỉ khác **cách CPU diễn giải sign bit**. Year 2038 trên 32-bit là cùng câu chuyện, chỉ scale lên từ 127 sang hơn hai tỷ.

<div class="content-box insight-box textbook-block" markdown="1">
Hai lớp dễ lẫn — giống chuyện endianness: **(1)** dãy bit vật lý trong register sau phép cộng; **(2)** kiểu dữ liệu trong ngôn ngữ (`uint32_t` vs `int32_t`) quyết định **đọc** dãy đó là bao nhiêu. `1000…000` là −2³¹ nếu signed, là 2³¹ nếu unsigned — cùng bit, hai số.
</div>

---

## ALU và overflow — cùng mạch cộng, khác cách đọc

Trong ALU thật, cộng two's complement dùng **cùng mạch cộng không dấu** trên từng bit, kèm carry chain — không có “mạch cộng riêng cho số âm”. CPU chỉ thêm **lớp diễn giải** ở tầng ISA: sign bit, overflow flag, và quy tắc mở rộng dấu khi load/store. Ben Eater trên kênh YouTube thường minh họa phép cộng với số **không dấu** trên breadboard; CPU thật thêm overflow flag để phần mềm (hoặc người debug) biết khi nào phép cộng signed “vượt” dải biểu diễn.

**Overflow** signed (tràn có dấu) xảy ra khi cộng hai số cùng dấu mà kết quả mang dấu ngược — ví dụ hai số dương mà tổng bị đọc thành âm, hoặc hai số âm mà tổng bị đọc thành dương. Year 2038 là case **dương + dương → âm** kinh điển trong sách giáo khoa kiến trúc máy tính — và nó xảy ra đồng loạt trên hàng triệu thiết bị cùng **một giây** thực lịch, không cần hacker, không cần cập nhật mã độc.

Lan không cần mở schematic PLC để tin điều này. Cô chỉ cần biết firmware lưu epoch trong `int32_t` signed, rồi tự tay cộng 1 vào 2,147,483,647 trên giấy — bit pattern nhảy sang min âm, timestamp nhảy sang 1901. Đó là lý do bài này nằm trong chương “máy tính lưu gì trong bit”, không nằm trong chương “quản lý dự án IT”.

---

## Ai còn rủi ro, ai đã qua — và làm gì thực tế

Phần lớn server Linux/macOS 64-bit và ứng dụng Java dùng `long` cho epoch millis đã **qua** nguy cơ Y2038 trên kiểu 32-bit — `time_t` trên nhiều bản phân phối hiện đại là 64-bit. Điện thoại và laptop chúng ta đang dùng có thể không bao giờ gặp bug này trên OS layer.

Rủi ro tập trung ở chỗ **ít ai ngó tới**: firmware router cũ, camera IP treo trần, PLC công nghiệp như tủ Lan mở — thiết bị chạy ổn định, không ai muốn downtime để flash firmware. File format hoặc backup archive ghi timestamp kiểu `int32` vẫn “đúng” năm 2037; mở lại năm 2039 có thể thấy mọi mốc thời gian nhảy về 1901. Embedded C trên vi điều khiển 32-bit mà không đổi ABI vẫn mang `time_t` 32-bit trong thư viện chuẩn cũ.

Giảm thiểu thực tế không phải meme “đổi sang unsigned là xong”. Nâng `time_t` lên 64-bit (Linux 5.6+ trên nhiều kiến trúc đã đi hướng này) là hướng chuẩn. Một mô hình Lan hay gặp trong nhà máy: **time authority** tập trung trên server 64-bit; thiết bị nhúng chỉ sync offset hoặc nhận giờ đã parse, không tự giữ epoch 32-bit làm nguồn sự thật lâu dài. Trong code mới, lưu trữ dài hạn nên dùng kiểu rộng hơn ngay từ đầu:

```c
#include <stdint.h>
#include <time.h>

// An toàn hơn cho lưu trữ dài hạn
int64_t t = (int64_t)time(NULL);
```

Nếu ai đó chọn `time_t` **unsigned** 32-bit, overflow xảy ra **muộn hơn** — max tương ứng khoảng năm **2106**, wrap về 0 (1970), không nhảy 1901. Đó là trade-off khác (mất khoảng thời gian trước 1970), không phải “an toàn vĩnh viễn”. Lan ghi vào risk register nhà máy một dòng khô khan: “PLC line 3 — firmware 2012, giả định `time_t` 32-bit signed, cần test overflow trên staging trước Q4/2037.” Không drama. Chỉ **đếm bit** và **cộng 1** trước khi giây thứ 2,147,483,648 đến.

Y2038 không phải meme xa vời — tính từ 2026 còn khoảng **12 năm**. Khác Y2K: không sửa bằng patch “thêm hai chữ số năm”; sửa bằng **rộng biểu diễn**, **thay thiết bị**, hoặc chấp nhận downtime và chi phí kiểm định mà thiết bị công nghiệp đã né suốt hai thập kỷ.

**Đọc thêm**: [Planet Mainframe — Y2K38 (2026)](https://planetmainframe.com/2026/01/inside-the-math-that-will-break-time-the-y2k38-problem/) · [Wikipedia — Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)

---

## Bài tập thực hành

### Bài tập 1

Với 8-bit signed two's complement, giá trị lớn nhất là bao nhiêu? Cộng 1 vào giá trị đó cho bit pattern nào và số thập phân bao nhiêu?

<details>
<summary>Đáp án</summary>

Max = $$2^7 - 1 = 127$$, pattern `01111111`. Cộng 1 → `10000000` = **−128** (min âm), không phải 128.

</details>

### Bài tập 2

Unix time lưu trong `int32_t` signed đạt giá trị $$2\,147\,483\,647$$ tại 03:14:07 UTC 19/01/2038. Ngay giây sau, biến chứa bao nhiêu (theo two's complement)? Timestamp lịch tương ứng khoảng năm nào?

<details>
<summary>Đáp án</summary>

Giá trị = $$-2\,147\,483\,648 = -2^{31}$$. Đếm lùi từ epoch → khoảng **13/12/1901** (UTC). Đây là cơ chế Year 2038, không phải đồng hồ hỏng ngẫu nhiên.

</details>

### Bài tập 3

Dùng công thức two's complement với $$w=4$$, tính giá trị thập phân của pattern `1010`.

<details>
<summary>Đáp án</summary>

Bit sign $$b_3 = 1$$: $$\text{value} = -1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = -8 + 2 = -6$$.

</details>

### Bài tập 4

Hệ thống A dùng `time_t` signed 32-bit; hệ thống B dùng `time_t` unsigned 32-bit. Cùng overflow “vòng” một vòng quanh giới hạn 32-bit, mô tả ngắn sự khác biệt về năm hiển thị sau overflow.

<details>
<summary>Đáp án</summary>

**Signed**: sau max → nhảy sang min âm → timestamp ~**1901**. **Unsigned**: sau max (~2106) → wrap về **0** → hiển thị ~**1970**. Cả hai đều hỏng ứng dụng nếu không migrate, nhưng **triệu chứng** khác nhau.

</details>

### Bài tập 5: Giới hạn 32-bit

(a) Liệt kê min, max và tổng số giá trị biểu diễn được của signed 32-bit two's complement. (b) Làm tương tự với unsigned 32-bit. (c) Vì sao Year 2038 xảy ra ở **2,147,483,647** chứ không ở **4,294,967,295**?

<details>
<summary>Đáp án</summary>

(a) Signed: min = $$-2^{31} = -2\,147\,483\,648$$, max = $$2^{31}-1 = 2\,147\,483\,647$$, tổng cộng $$2^{32} = 4\,294\,967\,296$$ giá trị. (b) Unsigned: min = $$0$$, max = $$2^{32}-1 = 4\,294\,967\,295$$, cũng $$2^{32}$$ giá trị. (c) Unix time trên hệ cũ dùng **signed** `int32_t`; giây cuối trước overflow là max signed, không phải max unsigned.

</details>

---


## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

**Giới hạn 32-bit**: luôn có $$2^{32}$$ tổ hợp bit; signed max = **2,147,483,647**, min = **−2,147,483,648**; unsigned max = **4,294,967,295**. Cùng 32 bit — khác kiểu đọc (`int32_t` vs `uint32_t`), khác ngày overflow.

Unix time là số giây từ epoch 1970 — đơn giản đến mức dễ quên rằng nó vẫn phải nằm trong **biên của kiểu biến**. Khi biến là signed 32-bit two's complement, giây cuối cùng “hợp lệ” là 2,147,483,647 (19/01/2038 03:14:07 UTC). Cộng thêm 1 không tạo ra số dương lớn hơn; nó lật sign bit và biến thành −2³¹, kéo timestamp về khoảng năm 1901. Đó là Year 2038 — không phải quy ước lưu năm hai chữ số như Y2K, mà là **tràn số học** có thể minh họa bằng phép cộng nhị phân trên giấy.

Two's complement dùng cùng mạch cộng với số không dấu; khác biệt nằm ở cách đọc bit và ở overflow signed khi tổng “vượt” dải. Server 64-bit và `int64_t` đã giải quyết phần lớn web app, nhưng PLC, firmware, và file archive cũ vẫn là mảnh đất của Lan — nơi “chạy ổn” không đồng nghĩa “qua 2038”. Giải pháp thực tế là mở rộng biểu diễn, tập trung time authority, hoặc thay thiết bị — không có phép màu đổi endian hay đổi charset.

Bài tiếp theo, Ben Eater cho ta **nhìn** bit trên breadboard — từ transistor đến NAND, rồi tới cùng mạch cộng mà ALU dùng để thực hiện phép cộng two's complement vừa học. Sau khi biết “+1 tại max” là gì trên giấy, ta sẽ thấy nó xảy ra ở đâu trong silicon.