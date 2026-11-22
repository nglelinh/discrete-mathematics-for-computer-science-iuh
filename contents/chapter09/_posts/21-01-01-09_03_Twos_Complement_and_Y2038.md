---
layout: post
title: "Two's complement và Year 2038: Khi +1 giây phá vỡ thời gian"
categories: chapter09
date: 2021-01-01
order: 3
required: false
lang: en
excerpt: "Tìm hiểu cách máy tính biểu diễn số nguyên có dấu bằng bù hai (two's complement), phân biệt giới hạn 32-bit signed/unsigned và cơ chế tràn số gây ra sự cố Year 2038."
---

Ở bài endianness, chúng ta đã thấy cùng một dãy byte có thể cho ra những giá trị khác nhau tùy theo quy ước sắp xếp thứ tự byte. Mục này xét một vấn đề tương tự đối với **số nguyên có dấu**: trên cùng một dãy bit trong bộ nhớ, máy tính áp dụng quy tắc **bù hai** (two's complement) để phân biệt số dương và số âm. Nhiều hệ thống không lưu “ngày giờ” theo định dạng hiển thị trên đồng hồ mà lưu **một số nguyên** đếm số giây trôi qua kể từ mốc epoch Unix (01/01/1970). Mỗi giây, số này tăng thêm 1; khi biến đếm chỉ rộng **32 bit có dấu** (signed), giá trị cực đại là $$2^{31}-1$$, tương ứng **03:14:07 UTC ngày 19/01/2038**. Cộng thêm 1 giây nữa sẽ gây **tràn số** (overflow) và đẩy timestamp quay ngược về khoảng năm **1901**.

Khác với sự cố **Y2K** (do lưu năm bằng hai chữ số dẫn đến nhầm lẫn giữa 1900 và 2000), **Y2038** bắt nguồn từ việc **ô nhớ đầy**: không thể khắc phục chỉ bằng cách “thêm chữ số”, mà phải mở rộng độ rộng biểu diễn (`int64_t`, `time_t` 64-bit) hoặc thay thế thiết bị cũ. Điểm cần nhớ: **thời gian trong máy tính là một số nguyên có giới hạn biên; cộng thêm 1 tại biên có thể làm lệch cả một thế kỷ.** Trong thực tế, các firmware PLC, camera IP và định dạng tệp lưu trữ dùng timestamp `int32` vẫn chạy bình thường vào năm 2026 nhưng có nguy cơ gặp sự cố sau năm 2038 nếu không được kiểm tra và nâng cấp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Binary_clock.svg"
       alt="Đồng hồ nhị phân — thời gian hiển thị được ghi bằng pattern bit"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.3a: Đồng hồ trên giao diện chỉ là lớp hiển thị; bên dưới là số nguyên có giới hạn biên — cộng 1 tại giá trị cực đại 32-bit có dấu sẽ nhảy sang vùng âm, tương ứng năm 1901 (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Binary_clock.svg">Alexander Jones &amp; Eric Pierce / Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

---

## Unix time — đếm giây từ một mốc quy ước

Phần lớn hệ điều hành họ Unix và nhiều hệ thống nhúng dùng **Unix time**: số giây đã trôi qua kể từ **00:00:00 UTC ngày 1 tháng 1 năm 1970**, gọi là mốc **epoch**. Đây đơn thuần là một quy ước chọn mốc 0 rồi đếm tăng dần theo từng giây. Giá trị `0` ứng với 1970-01-01 00:00:00 UTC, còn giá trị `1_000_000_000` ứng với khoảng ngày 09/09/2001 — mốc “một tỷ giây” thường được nhắc đến trong các tài liệu kỹ thuật.

Khi Unix time được lưu trong biến **số nguyên 32-bit có dấu**, tập giá trị biểu diễn được là **hữu hạn**, gồm đúng $$2^{32}$$ giá trị khác nhau từ cận dưới âm đến cận trên dương theo quy tắc bù hai. Mọi thời điểm nằm ngoài dải này đều không thể biểu diễn trực tiếp hoặc sẽ bị quay vòng (wrap) theo cơ chế phần cứng — hệ quả của việc **chọn kiểu dữ liệu quá hẹp**, không phải do bản thân chuẩn thời gian UTC gặp lỗi.

![Unix time timeline — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Unix_timeline.en.svg)

<p class="textbook-figure-caption" data-figure="9.11">Unix time tăng đều mỗi giây cho đến khi chạm giới hạn bit của biến 32-bit có dấu (nguồn: Wikimedia Commons).</p>

Nhìn vào trục thời gian này, Lan thấy rõ điểm mà Planet Mainframe nhấn mạnh: nhiều thiết bị công nghiệp **vận hành đúng thiết kế** suốt hai thập kỷ nhưng rất khó được nâng cấp trước năm 2038 vì chi phí tái kiểm định (recertification) — cập nhật firmware PLC có thể đòi hỏi dừng dây chuyền nhà máy, kiểm định an toàn lại và xin cấp phép vận hành mới. Lỗi không nằm ở logic điều khiển thiết bị mà nằm ngay ở **ô nhớ đếm giây**.

**Y2K** và **Y2038** cùng là sự cố liên quan đến mốc thời gian, nhưng bản chất hoàn toàn khác nhau:

| | Y2K (2000) | Y2038 |
|:---|:---|:---|
| Nguyên nhân | Lưu năm bằng 2 chữ số | **Tràn số** 32-bit có dấu |
| Bản chất | Quy ước lưu trữ văn bản/trường năm | **Giới hạn biểu diễn nhị phân** |
| Hệ thống ảnh hưởng | Ứng dụng nghiệp vụ | **Hệ nhúng**, firmware, PLC, hệ thống cũ |

Y2K được khắc phục bằng cách mở rộng trường năm trong cơ sở dữ liệu thêm hai chữ số. Với Y2038, nếu biến vẫn chỉ rộng 32 bit và đọc theo bù hai có dấu thì không thể vá cục bộ — bắt buộc phải **mở rộng kiểu biểu diễn** hoặc **thay thế phần cứng/firmware** cũ.

## Giới hạn 32-bit — có dấu hay không dấu?

Một câu hỏi thường gặp trước khi đi sâu vào Year 2038 là: **32 bit biểu diễn được đến giá trị nào?** Câu trả lời không chỉ phụ thuộc vào số bit mà còn phụ thuộc vào **quy ước đọc** dãy bit đó.

Với 32 bit, mỗi bit nhận giá trị 0 hoặc 1, tổng cộng có đúng $$2^{32} = 4\,294\,967\,296$$ **tổ hợp bit khác nhau**. Tuy nhiên, giá trị nhỏ nhất và lớn nhất lại phụ thuộc vào kiểu dữ liệu:

| Kiểu dữ liệu | Nhỏ nhất | Lớn nhất | Hệ quả với Unix time |
|:---|:---|:---|:---|
| **Có dấu** (`int32_t`, bù hai) | $$-2^{31} = -2\,147\,483\,648$$ | $$2^{31} - 1 = 2\,147\,483\,647$$ | Tràn năm **2038** → nhảy về **1901** |
| **Không dấu** (`uint32_t`) | $$0$$ | $$2^{32} - 1 = 4\,294\,967\,295$$ | Tràn khoảng năm **2106** → quay về **1970** |

Kiểu **có dấu** chia không gian $$2^{32}$$ tổ hợp thành một nửa cho số âm và một nửa cho số không âm; dải giá trị **không đối xứng** (biểu diễn được $$+2^{31}-1$$ nhưng không có $$+2^{31}$$, vì tổ hợp bit tương ứng dành cho số âm nhỏ nhất). Kiểu **không dấu** dùng toàn bộ không gian cho số không âm nên giá trị cực đại gần gấp đôi kiểu có dấu.

Vì Unix timestamp trên các hệ thống cũ thường dùng **32-bit có dấu**, giới hạn quyết định sự cố Year 2038 là **2,147,483,647**, chứ không phải 4,294,967,295.

<div class="content-box insight-box textbook-block" markdown="1">
**Ghi nhớ nhanh**: Cực đại có dấu = **2,147,483,647** (03:14:07 UTC, 19/01/2038); cực tiểu có dấu = **−2,147,483,648** (~1901 sau tràn số); cực đại không dấu = **4,294,967,295** (tràn khoảng năm 2106). Cùng 32 bit nhưng khác kiểu đọc sẽ cho ra mốc tràn khác nhau.
</div>

---

## Bù hai (two's complement) — khi +1 biến cực đại thành cực tiểu âm

Máy tính hiện đại hầu như luôn biểu diễn số nguyên có dấu bằng **bù hai** (two's complement). Trong 32 bit, **bit cao nhất** đóng vai trò **bit dấu** (0 là không âm, 1 là âm), còn **31 bit** còn lại kết hợp theo trọng số của quy tắc bù hai — không phải dạng “1 bit dấu tách rời và 31 bit trị tuyệt đối” như nhiều người dễ nhầm.

Giá trị dương **lớn nhất** mà số 32-bit có dấu biểu diễn được có mẫu bit `0111…111` (một bit 0 đứng trước 31 bit 1):

<div class="textbook-equation" markdown="1">
$$2^{31} - 1 = 2\,147\,483\,647$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đó chính là mốc **03:14:07 UTC ngày 19/01/2038** — giây Unix cuối cùng trước khi tràn trên biến `int32_t`. Đây không phải một mốc thời gian ngẫu nhiên mà là **cận trên toán học** của kiểu dữ liệu 32-bit có dấu.

Khi cộng thêm 1 vào giá trị cực đại bằng phép cộng nhị phân thông thường (trên cùng mạch ALU như số không dấu):

```
  0111...111
+ 0000...001
-----------
  1000...000   ← sign bit = 1, các bit khác = 0
```

Trong hệ bù hai, mẫu bit `1000…000` không phải là một số dương lớn hơn mà biểu diễn **−2³¹ = −2,147,483,648** — giá trị **âm nhỏ nhất** của 32-bit có dấu. Đếm lùi 2,147,483,648 giây tính từ mốc epoch 1970 sẽ cho ra **1901-12-13 20:45:52 UTC**, đúng như [Planet Mainframe](https://planetmainframe.com/2026/01/inside-the-math-that-will-break-time-the-y2k38-problem/) và [Wikipedia — Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem) ghi nhận. Khi sự cố xảy ra, màn hình HMI có thể báo năm 1901, nhật ký kiểm toán ghi mốc thời gian lùi hơn một thế kỷ, và các tác vụ lập lịch cho “03:15” có thể không bao giờ chạy vì bộ lập lịch tưởng thời điểm đó đã trôi qua từ hơn trăm năm trước.

<div class="content-box warning-box textbook-block" markdown="1">
Trong ngôn ngữ C, tràn số trên kiểu có dấu như `time_t` là **hành vi không xác định** (undefined behavior) về mặt tiêu chuẩn ngôn ngữ, nên lập trình viên không được giả định kết quả. Dù trên thực tế hầu hết kiến trúc phần cứng đều quay vòng theo bù hai, ứng dụng vẫn nhận sai thời gian dù mạch cộng hoạt động đúng. “Quay vòng có quy luật” hoàn toàn không đồng nghĩa với “ứng dụng an toàn”.
</div>

Công thức tổng quát của biểu diễn bù hai cho từ máy $$w$$ bit với các bit $$b_{w-1} \ldots b_0$$ (trong đó $$b_{w-1}$$ là bit dấu):

<div class="textbook-equation" markdown="1">
$$
\text{value} = -b_{w-1} \cdot 2^{w-1} + \sum_{i=0}^{w-2} b_i \cdot 2^i
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Với $$w = 32$$, cực đại dương là $$2^{31}-1$$ và cực tiểu âm là $$-2^{31}$$. Dải biểu diễn không đối xứng vì tổ hợp bit tương ứng với $$2^{31}$$ đã được dùng cho $$-2^{31}$$.

Để giải thích trực quan cho thực tập sinh mới vào nhà máy, Lan thường lấy mô hình **8-bit**: cực đại dương là $$2^7 - 1 = 127$$ (`01111111`); cộng thêm 1 cho ra `10000000`, đọc theo bù hai là **−128** chứ không phải 128. Cùng một mạch cộng và cùng một dãy bit, sự khác biệt chỉ nằm ở **cách CPU diễn giải bit dấu**. Year 2038 trên 32-bit có cơ chế giống hệt, chỉ mở rộng từ 127 lên hơn hai tỷ.

<div class="content-box insight-box textbook-block" markdown="1">
Tương tự bài endianness, cần tách hai lớp: **(1)** dãy bit vật lý trong thanh ghi sau phép cộng; **(2)** kiểu dữ liệu (`uint32_t` hay `int32_t`) quyết định cách đọc giá trị của dãy bit đó. Mẫu `1000…000` là $$-2^{31}$$ nếu đọc có dấu, nhưng là $$2^{31}$$ nếu đọc không dấu.
</div>

---

### Minh họa bù hai, cộng có nhớ và Y2038

Nhấn vào từng bit để xem giá trị bù hai (bit đầu có trọng số âm), cách lấy số đối bằng “đảo bit + 1”, phép cộng từng cột gây tràn số, và kéo thanh trượt qua ngưỡng $$2^{31}-1$$ của Unix time.

<div class="interactive-demo" markdown="1">
<div data-demo="bits-explainer" data-tab="twos"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## ALU và tràn số — cùng mạch cộng, khác cách đọc

Trong bộ số học logic (ALU) thực tế, phép cộng bù hai sử dụng **chính mạch cộng số không dấu** trên từng bit kèm chuỗi nhớ (carry chain) — không cần một mạch cộng riêng cho số âm. CPU chỉ bổ sung **lớp diễn giải** ở tầng tập lệnh (ISA): bit dấu, cờ tràn số (overflow flag) và quy tắc mở rộng dấu khi nạp/lưu dữ liệu. Loạt video của Ben Eater minh họa phép cộng không dấu trên breadboard, còn CPU thực tế đặt thêm cờ tràn để phần mềm phát hiện khi phép cộng có dấu vượt khỏi dải biểu diễn.

**Tràn số có dấu** (signed overflow) xảy ra khi cộng hai số cùng dấu nhưng kết quả lại mang dấu ngược lại — tức hai số dương cộng ra âm, hoặc hai số âm cộng ra dương. Year 2038 là ví dụ kinh điển cho trường hợp **dương + dương → âm**, xảy ra đồng loạt trên hàng triệu thiết bị tại cùng một giây lịch thực mà không cần bất kỳ tác động bên ngoài nào.

Lan không cần mở sơ đồ mạch của PLC để kiểm chứng nguy cơ này: chỉ cần biết firmware lưu epoch bằng `int32_t` có dấu rồi tự cộng 1 vào 2,147,483,647 trên giấy là đủ thấy mẫu bit nhảy sang cực tiểu âm và timestamp lùi về năm 1901.

---

## Hệ thống nào còn rủi ro và giải pháp thực tế

Phần lớn máy chủ Linux/macOS 64-bit và ứng dụng Java (dùng kiểu `long` cho epoch tính theo mili giây) đã vượt qua giới hạn 32-bit, vì `time_t` trên đa số hệ điều hành hiện đại đã là 64-bit. Điện thoại và máy tính cá nhân thông thường khó gặp lỗi này ở tầng hệ điều hành.

Rủi ro thực sự tập trung ở các hệ thống **ít được cập nhật**: firmware router cũ, camera IP, PLC công nghiệp hoạt động ổn định nhiều năm nên ít đơn vị muốn dừng hệ thống để nạp lại firmware. Ngoài ra, các định dạng tệp hoặc bản sao lưu ghi timestamp bằng `int32` vẫn đọc bình thường đến năm 2037, nhưng sang năm 2039 có thể hiển thị thời gian nhảy về 1901. Mã C nhúng trên vi điều khiển 32-bit giữ nguyên ABI cũ cũng vẫn mang `time_t` 32-bit trong thư viện chuẩn.

Giải pháp bền vững không phải là chuyển sang `unsigned` 32-bit mà là nâng `time_t` lên **64-bit** (Linux từ phiên bản 5.6 trở đi đã hỗ trợ rộng rãi hướng này trên nhiều kiến trúc). Trong môi trường nhà máy, một mô hình thực tế khác là đặt **máy chủ chuẩn thời gian** (time authority) 64-bit tập trung; thiết bị nhúng chỉ đồng bộ độ lệch hoặc nhận thời gian đã xử lý thay vì tự lưu epoch 32-bit lâu dài. Trong mã nguồn mới, cần dùng kiểu 64-bit ngay từ đầu cho dữ liệu lưu trữ dài hạn:

```c
#include <stdint.h>
#include <time.h>

// An toàn hơn cho lưu trữ dài hạn
int64_t t = (int64_t)time(NULL);
```

Nếu chuyển `time_t` sang **không dấu** 32-bit, thời điểm tràn chỉ bị đẩy lùi sang khoảng năm **2106** (và quay về 0 tức năm 1970, đồng thời không biểu diễn được thời điểm trước năm 1970) — đây chỉ là giải pháp trì hoãn chứ không giải quyết triệt để. Trong sổ quản lý rủi ro nhà máy, Lan ghi ngắn gọn: “PLC dây chuyền 3 — firmware 2012, giả định `time_t` 32-bit có dấu, cần kiểm thử tràn số trên môi trường staging trước Q4/2037.”

Tính từ năm 2026, mốc Y2038 chỉ còn khoảng **12 năm**. Khác với Y2K, vấn đề này không thể vá bằng cách thêm chữ số hiển thị mà đòi hỏi **mở rộng độ rộng biểu diễn**, **thay thế thiết bị** hoặc chấp nhận chi phí dừng máy và kiểm định lại.

**Đọc thêm**: [Planet Mainframe — Y2K38 (2026)](https://planetmainframe.com/2026/01/inside-the-math-that-will-break-time-the-y2k38-problem/) · [Wikipedia — Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem)

---

## Bài tập thực hành

### Bài tập 1

Với số nguyên 8-bit có dấu theo bù hai, giá trị lớn nhất là bao nhiêu? Khi cộng thêm 1 vào giá trị đó, mẫu bit và giá trị thập phân thu được là gì?

<details>
<summary>Đáp án</summary>

Giá trị lớn nhất là $$2^7 - 1 = 127$$, mẫu bit `01111111`. Cộng thêm 1 cho ra `10000000`, biểu diễn **−128** (giá trị âm nhỏ nhất), không phải 128.

</details>

### Bài tập 2

Unix time lưu trong `int32_t` có dấu đạt giá trị $$2\,147\,483\,647$$ tại 03:14:07 UTC ngày 19/01/2038. Ngay giây kế tiếp, biến chứa giá trị nào theo bù hai và tương ứng với khoảng thời gian nào?

<details>
<summary>Đáp án</summary>

Giá trị biến trở thành $$-2\,147\,483\,648 = -2^{31}$$. Đếm lùi từ mốc epoch 1970 cho ra khoảng ngày **13/12/1901** (UTC). Đây là cơ chế tràn số học của sự cố Year 2038, không phải lỗi hỏng đồng hồ ngẫu nhiên.

</details>

### Bài tập 3

Áp dụng công thức bù hai với $$w = 4$$, tính giá trị thập phân của mẫu bit `1010`.

<details>
<summary>Đáp án</summary>

Với bit dấu $$b_3 = 1$$: $$\text{value} = -1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = -8 + 2 = -6$$.

</details>

### Bài tập 4

Hệ thống A dùng `time_t` 32-bit có dấu; hệ thống B dùng `time_t` 32-bit không dấu. Khi cả hai đều bị tràn quay vòng qua giới hạn 32-bit, nêu ngắn gọn sự khác nhau về năm hiển thị sau khi tràn.

<details>
<summary>Đáp án</summary>

- **Có dấu**: sau khi vượt cực đại (năm 2038), giá trị nhảy sang cực tiểu âm, hiển thị khoảng năm **1901**.
- **Không dấu**: sau khi vượt cực đại (khoảng năm 2106), giá trị quay về **0**, hiển thị năm **1970**.

Cả hai trường hợp đều gây lỗi ứng dụng nếu không chuyển đổi kiểu dữ liệu, nhưng biểu hiện thời gian sau tràn là khác nhau.

</details>

### Bài tập 5: Giới hạn 32-bit

(a) Liệt kê giá trị nhỏ nhất, lớn nhất và tổng số giá trị biểu diễn được của kiểu 32-bit có dấu theo bù hai. (b) Thực hiện tương tự với kiểu 32-bit không dấu. (c) Vì sao sự cố Year 2038 xảy ra ở mốc **2,147,483,647** chứ không phải **4,294,967,295**?

<details>
<summary>Đáp án</summary>

(a) Kiểu có dấu: nhỏ nhất $$-2^{31} = -2\,147\,483\,648$$, lớn nhất $$2^{31}-1 = 2\,147\,483\,647$$, tổng cộng $$2^{32} = 4\,294\,967\,296$$ giá trị.

(b) Kiểu không dấu: nhỏ nhất $$0$$, lớn nhất $$2^{32}-1 = 4\,294\,967\,295$$, cũng gồm $$2^{32}$$ giá trị.

(c) Unix time trên các hệ thống cũ dùng kiểu `int32_t` **có dấu**, nên giây cuối cùng trước khi tràn là cực đại của kiểu có dấu, không phải cực đại của kiểu không dấu.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Với 32 bit luôn có $$2^{32}$$ tổ hợp bit khác nhau: kiểu có dấu có dải từ **−2,147,483,648** đến **2,147,483,647**, còn kiểu không dấu có cực đại **4,294,967,295**. Cùng 32 bit nhưng khác kiểu đọc (`int32_t` so với `uint32_t`) sẽ dẫn đến thời điểm tràn số khác nhau.

Unix time đếm số giây từ mốc epoch 1970 và vẫn bị ràng buộc bởi biên của kiểu dữ liệu. Với 32-bit có dấu theo bù hai, giây hợp lệ cuối cùng là 2,147,483,647 (03:14:07 UTC ngày 19/01/2038). Cộng thêm 1 làm lật bit dấu sang $$-2^{31}$$, kéo thời gian về khoảng năm 1901. Khác với Y2K, Year 2038 là hiện tượng **tràn số học** trong biểu diễn nhị phân.

Phép cộng bù hai dùng chung mạch cộng với số không dấu; sự khác biệt nằm ở cách diễn giải bit dấu và phát hiện tràn số. Dù máy chủ 64-bit và `int64_t` đã giải quyết phần lớn ứng dụng web, các thiết bị PLC, firmware và tệp lưu trữ cũ vẫn cần được rà soát để mở rộng biểu diễn, đồng bộ thời gian tập trung hoặc thay thế phần cứng trước năm 2038.

Trong bài tiếp theo, loạt dự án của Ben Eater sẽ giúp ta quan sát trực tiếp **bit trên breadboard** — từ transistor đến cổng NAND và chính mạch cộng ALU thực hiện phép cộng bù hai vừa học.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=lKTsv6iVxV4">Binary: Plusses &amp; Minuses (Why We Use Two&#x27;s Complement) - Computerphile</a> — Computerphile, tiếng Anh. Giải thích quy tắc bù hai và lý do phép cộng nhị phân cơ học hoạt động tự nhiên với số âm.
- <a href="https://www.youtube.com/watch?v=4qH4unVtJkE">Twos complement: Negative numbers in binary</a> — Ben Eater, tiếng Anh. Minh họa cách dựng số âm bù hai trên mạch phần cứng, gắn với phần ALU của bài.
- <a href="https://www.youtube.com/watch?v=BeK3LHegUr8">The Year 2038 Problem, Explained</a> — Code Blame, tiếng Anh. Trình bày sự cố tràn bộ đếm giây Unix 32-bit tại mốc năm 2038.
