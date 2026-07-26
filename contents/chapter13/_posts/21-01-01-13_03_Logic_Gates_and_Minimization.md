---
layout: post
title: "Mạng các Cổng Logic và Tối thiểu hóa Hàm Boole"
categories: chapter13
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Cổng logic (AND, OR, NOT, NAND, NOR, XOR, XNOR), mạng công tắc, đọc/vẽ mạch, SOP/POS hai tầng, tối thiểu hóa đại số, NAND/NOR-only, và năm bước thiết kế."
---

<div class="textbook-epigraph" markdown="1">

"Switching circuits are a practical embodiment of Boolean algebra."

<span class="epigraph-attribution">— Claude Shannon (ý tưởng, 1937)</span>

</div>

Biểu thức Boole trên giấy chưa phải là mạch. Ở bài này chúng ta nối **hàm Boole** (bài 13.2) với **cổng logic** — khối thực hiện các phép AND, OR, NOT và các phép dẫn xuất — rồi học cách **rút gọn biểu thức bằng đại số** để mạch dùng **ít cổng hơn**.

Vì sao cần ít cổng? Trên bài tập, bạn đếm và vẽ sơ đồ nhanh hơn. Về sau, khi làm việc với phần cứng hoặc mô phỏng mạch, ít cổng cũng thường nghĩa là mạch đơn giản hơn và dễ kiểm tra hơn. Công cụ rút gọn là các hằng đẳng thức đã học ở 13.1 (hấp thụ, De Morgan, phân phối, lũy đẳng), áp dụng có chiến lược, rồi **kiểm lại bằng bảng chân trị**.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Liên hệ** mạng công tắc (nối tiếp / song song) với AND / OR và viết hàm Boole của mạch công tắc.
- **Nhận biết** cổng AND, OR, NOT, NAND, NOR, XOR, XNOR và đọc đúng bảng chân trị của từng cổng.
- **Đọc** biểu thức từ sơ đồ cổng và **vẽ** mạch từ biểu thức (hai chiều).
- **Chuyển** biểu thức SOP (tổng các tích) / POS (tích các tổng) thành mạch hai tầng và ước lượng số cổng.
- **Áp dụng** tối thiểu hóa đại số cơ bản: đồng nhất, hấp thụ, gom nhân tử, De Morgan — và thấy vì sao rút gọn giảm số cổng.
- **Map** NOT/AND/OR sang mạng **chỉ NAND** hoặc **chỉ NOR**.
- **Thiết kế** mạch tổ hợp từ mô tả bằng lời theo **năm bước** (ví dụ công tắc–đèn).
- **Ước lượng** độ phức tạp mạch: số cổng và số tầng (độ sâu).

**Từ khóa**: cổng logic (logic gate), mạng công tắc, mạch hai tầng, SOP (tổng các tích), POS (tích các tổng), tối thiểu hóa đại số, NAND/NOR, XNOR, độ sâu mạch.

</div>

## 1. Từ mạch điện đến cổng logic

### 1.1. Mạch điện, công tắc và biến Boole

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Trong ngữ cảnh logic số sơ cấp:

- **Mạch điện** (ở đây) gồm các **công tắc** và dây dẫn; ta quan tâm có/không có dòng từ nguồn sang tải.
- Mỗi **công tắc** tương ứng một **biến Boole**: quy ước **đóng = 1**, **hở = 0** (hoặc ngược lại — nhưng **nhất quán** trong cả bài).
- **Cổng logic** (logic gate) là khối nhận **một hoặc nhiều** tín hiệu **0**/**1** và phát ra **một** tín hiệu ra theo **bảng chân trị cố định**.

</div>

- Bit **1** thường tương ứng mức điện áp “cao” (hoặc công tắc đóng).
- Bit **0** thường tương ứng mức “thấp” (hoặc công tắc hở).
- **Hành vi** của cổng chỉ phụ thuộc bảng chân trị, không phụ thuộc bạn vẽ ký hiệu thế nào.

Claude Shannon (1937) chỉ ra rằng mạng rơ-le đóng/mở tuân **cùng luật** OR / AND / NOT với đại số Boole. Ngày nay tín hiệu số thường là mức điện áp “cao/thấp” thay cho tiếp điểm, nhưng **bảng chân trị không đổi**. Vì vậy mỗi lần bạn rút gọn biểu thức, số cổng cần vẽ (và sau này số linh kiện thật) cũng giảm theo.

### 1.2. Nối tiếp và song song — trực giác AND / OR

Trước khi học ký hiệu ANSI của cổng, hãy nhìn hai cấu trúc công tắc cổ điển:

| Cấu trúc công tắc | Có dòng khi… | Hàm Boole |
|:---|:---|:---|
| **Nối tiếp** (series) | **cả hai** công tắc đóng | $$t(a,b) = ab$$ (**AND**) |
| **Song song** (parallel) | **ít nhất một** công tắc đóng | $$t(a,b) = a + b$$ (**OR**) |

![Nối tiếp và song song](/discrete-mathematics-for-computer-science-iuh/img/course/Switch_series_parallel.svg)

<p class="textbook-figure-caption" data-figure="13.10a">Nối tiếp = AND; song song = OR. Ghép hai kiểu này thành mạng phức tạp → một biểu thức Boole.</p>

<div class="textbook-example" markdown="1">

**Ví dụ (mạng hỗn hợp).**  
Giả sử từ nguồn đến tải: nhánh trên là $$x$$ nối tiếp với $$(y$$ song song $$z)$$; nhánh dưới là $$\bar z$$ nối tiếp $$\bar x$$; hai nhánh song song nhau, rồi nối tiếp công tắc $$t$$. Hàm “có dòng” là

$$
f(x,y,z,t) = \bigl[x(y + z) + \bar z\,\bar x\bigr] t = xyt + xzt + \bar x\,\bar z\, t.
$$

Đây chính là **dạng đa thức / SOP (tổng các tích)** của mạng công tắc — cùng kiểu biểu thức bạn sẽ vẽ bằng cổng AND–OR–NOT ở các mục sau.

</div>

### 1.3. Phép Boole ↔ cổng (bảng 0/1)

| Phép đại số Boole | Cổng | Bảng tóm tắt trên $$\{0,1\}$$ |
|:---|:---|:---|
| Cộng $$+$$ | **OR** | $$0+0=0$$, $$0+1=1$$, $$1+0=1$$, $$1+1=1$$ |
| Nhân $$\cdot$$ | **AND** | $$0\cdot0=0$$, $$0\cdot1=0$$, $$1\cdot0=0$$, $$1\cdot1=1$$ |
| Phủ định $$'$$ / $$\bar{\phantom{x}}$$ | **NOT** | $$\bar 0 = 1$$, $$\bar 1 = 0$$ |

## 2. Bảy cổng cơ bản — đọc bảng trước, nhớ ký hiệu sau

Dưới đây mỗi cổng được mô tả bằng **một câu tiếng Việt + bảng chân trị + một hình riêng**. Bạn nên thuộc bảng trước khi vẽ schematic.

### 2.1. Cổng NOT (đảo, inverter)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cổng **NOT** có **một** ngõ vào $$A$$ và một ngõ ra $$Y = A'$$ (cũng viết $$\bar A$$ hoặc $$\lnot A$$).

- Nếu vào là **0** thì ra là **1**.
- Nếu vào là **1** thì ra là **0**.

</div>

| $$A$$ | $$Y = A'$$ |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

![Cổng NOT](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.11">Cổng NOT (inverter) — ký hiệu ANSI.</p>

### 2.2. Cổng AND (và)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cổng **AND** với các ngõ vào $$A, B, \ldots$$ cho ra **1** **chỉ khi mọi** ngõ vào đều bằng **1**. Nếu có **ít nhất một** ngõ bằng **0** thì ra **0**.

Với hai ngõ: $$Y = AB = A \land B$$.

</div>

| $$A$$ | $$B$$ | $$Y = AB$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

![Cổng AND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_AND.svg)

<p class="textbook-figure-caption" data-figure="13.12">Cổng AND — ký hiệu ANSI.</p>

### 2.3. Cổng OR (hoặc)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cổng **OR** cho ra **1** khi **ít nhất một** ngõ vào bằng **1**. Ra **0** chỉ khi **mọi** ngõ đều bằng **0**.

Với hai ngõ: $$Y = A + B = A \lor B$$.

</div>

| $$A$$ | $$B$$ | $$Y = A+B$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

![Cổng OR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_OR.svg)

<p class="textbook-figure-caption" data-figure="13.13">Cổng OR — ký hiệu ANSI.</p>

### 2.4. Cổng NAND và NOR

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

- **NAND** = NOT sau AND: $$Y = (AB)'$$. Ra **0** chỉ khi cả hai vào đều **1**; các trường hợp còn lại ra **1**.
- **NOR** = NOT sau OR: $$Y = (A+B)'$$. Ra **1** chỉ khi cả hai vào đều **0**; các trường hợp còn lại ra **0**.

</div>

| $$A$$ | $$B$$ | NAND $$(AB)'$$ | NOR $$(A+B)'$$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | **0** | 0 |

![Cổng NAND](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NAND.svg)

<p class="textbook-figure-caption" data-figure="13.14">Cổng NAND — NOT sau AND.</p>

![Cổng NOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOR.svg)

<p class="textbook-figure-caption" data-figure="13.15">Cổng NOR — NOT sau OR.</p>

**Vì sao NAND/NOR quan trọng?** Một mình NAND đã **đầy đủ chức năng** (*functionally complete*): từ NAND ta dựng được NOT, AND, OR — do đó dựng được **mọi** hàm Boole. NOR cũng đầy đủ (đối ngẫu). Nhiều bài tập (và thiết kế phần cứng sau này) yêu cầu “chỉ dùng NAND” hoặc “chỉ dùng NOR” chính vì lý do này.

### 2.5. Cổng XOR (loại trừ / exclusive OR)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cổng **XOR** hai ngõ cho ra **1** khi hai ngõ **khác nhau**, ra **0** khi hai ngõ **giống nhau**.

$$
Y = A \oplus B = A'B + AB'.
$$

</div>

| $$A$$ | $$B$$ | $$Y = A\oplus B$$ |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | 0 |

![Cổng XOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XOR.svg)

<p class="textbook-figure-caption" data-figure="13.16">Cổng XOR — ra 1 khi hai ngõ khác nhau.</p>

**Liên hệ half adder.** Bit **tổng** (sum) của half adder chính là XOR; bit **nhớ** (carry) là AND. Xem hình half adder bên dưới và chi tiết ở bài 13.7.

![Half adder](/discrete-mathematics-for-computer-science-iuh/img/course/Half_Adder.svg)

<p class="textbook-figure-caption" data-figure="13.17">Half adder: Sum = XOR, Carry = AND — một hàm đơn giản thành ít cổng.</p>

### 2.6. Cổng XNOR (tương đương / exclusive NOR)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cổng **XNOR** (còn gọi *equivalence*) hai ngõ cho ra **1** khi hai ngõ **giống nhau**, ra **0** khi hai ngõ **khác nhau**.

$$
Y = A \odot B = AB + \bar A\,\bar B = (A \oplus B)'.
$$

</div>

| $$A$$ | $$B$$ | $$Y = A\odot B$$ |
|:---:|:---:|:---:|
| 0 | 0 | **1** |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

![Cổng XNOR](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_XNOR.svg)

<p class="textbook-figure-caption" data-figure="13.17b">Cổng XNOR — ra 1 khi hai ngõ giống nhau (đối ngẫu XOR).</p>

**Ghi nhớ nhanh.** XOR = “khác nhau?”; XNOR = “bằng nhau?”. Trong ví dụ ba công tắc–đèn (mục 7), sau khi gom nhân tử bạn sẽ gặp đúng $$A \odot B$$.

### 2.7. Tên gọi logic cổ điển (tham chiếu)

Trên một số giáo trình / slide cũ, bốn phép còn được gọi:

| Tên | Ký hiệu | Nghĩa |
|:---|:---|:---|
| XOR (tổng modulo 2) | $$P \oplus Q$$ | exclusive OR |
| **Webb** / Peirce | $$P \downarrow Q$$ | NOR |
| **Sheffer** | $$P \mid Q$$ hoặc $$P \uparrow Q$$ | NAND |
| XNOR | $$P \odot Q$$ | exclusive NOR / tương đương |

Công thức mở rộng (cùng bảng chân trị):

$$
\begin{aligned}
P \oplus Q &= (P \land \lnot Q) \lor (\lnot P \land Q), \\
P \odot Q &= (P \land Q) \lor (\lnot P \land \lnot Q).
\end{aligned}
$$

### 2.8. Tóm tắt nhanh bảy cổng

| Cổng | Ra **1** khi… | Công thức (2 ngõ) |
|:---|:---|:---|
| NOT | vào bằng **0** | $$A'$$ |
| AND | **mọi** vào = **1** | $$AB$$ |
| OR | **ít nhất một** vào = **1** | $$A+B$$ |
| NAND | **không** phải cả hai = **1** | $$(AB)'$$ |
| NOR | **mọi** vào = **0** | $$(A+B)'$$ |
| XOR | hai vào **khác nhau** | $$A\oplus B$$ |
| XNOR | hai vào **giống nhau** | $$A\odot B$$ |

## 3. Từ biểu thức đến mạch hai tầng

### 3.1. SOP (tổng các tích) → mạch AND–OR

<div class="textbook-definition" markdown="1">

**Định nghĩa (hiện thực hai tầng).** Biểu thức **SOP** (tổng các tích / *Sum of Products*)

$$
F = t_1 + t_2 + \cdots + t_r
$$

trong đó mỗi $$t_i$$ là **tích** các litera (ví dụ $$x'y z$$), được vẽ thành:

1. **Tầng 1:** các cổng **AND** (mỗi tích một cổng; NOT ở đầu vào nếu có litera phủ định).
2. **Tầng 2:** một cổng **OR** gom mọi tích.

</div>

Dạng **POS** (tích các tổng / *Product of Sums*) đối ngẫu: tầng OR rồi tầng AND.

Độ trễ lý tưởng tỉ lệ với **hai tầng** cổng — đó là lý do SOP (tổng các tích) / POS (tích các tổng) được ưa trong tổng hợp hai cấp.

<div class="textbook-example" markdown="1">

**Ví dụ (XOR hai tầng).**  
$$F = A'B + AB'$$.

- Đảo $$A$$ và $$B$$ (hai NOT).
- AND cặp $$(A', B)$$ và $$(A, B')$$.
- OR hai kết quả.

Cùng hàm có thể chỉ cần **một** cổng XOR nếu đề cho phép dùng XOR có sẵn — cùng hành vi, khác số khối vẽ.

</div>

![Mạch hai tầng SOP](/discrete-mathematics-for-computer-science-iuh/img/course/Two_level_SOP.svg)

<p class="textbook-figure-caption" data-figure="13.18">SOP $$A'B + AB'$$ thành mạch AND–OR hai tầng (tương đương XOR).</p>

<div class="textbook-example" markdown="1">

**Ví dụ (majority ba biến).**  
$$F = AB + AC + BC$$: ba AND hai ngõ và một OR ba ngõ.  
Đây cũng là biểu thức $$C_{out}$$ của full adder khi ba ngõ là $$A$$, $$B$$, $$C_{in}$$.

</div>

![Mạch majority](/discrete-mathematics-for-computer-science-iuh/img/course/Majority_circuit.svg)

<p class="textbook-figure-caption" data-figure="13.19">Majority $$AB+AC+BC$$ — ba AND và một OR; nền tảng carry của full adder.</p>

### 3.2. Đếm cổng trước khi rút gọn

Xét SOP (tổng các tích)

$$
F = x'y'z + x'yz' + xy'z' + xyz.
$$

Thô: **4 AND** (tối đa 3 ngõ), **1 OR** 4 ngõ, vài **NOT**.  
Nếu sau tối thiểu hóa còn **hai** hạng, số AND giảm khoảng một nửa — đó là động lực của phần còn lại bài này.

### 3.3. Hai chiều: đọc mạch ↔ viết biểu thức

Trên bài tập (và đề thi), bạn cần **cả hai hướng**:

1. **Đọc mạch → biểu thức:** đi từ ngõ vào sang ngõ ra, ghi nhãn từng dây (NOT trước, rồi AND/OR).
2. **Biểu thức → vẽ mạch:** mỗi phép $$+$$ / $$\cdot$$ / $$'$$ thành một cổng (hoặc tái dùng tín hiệu đã có).

<div class="textbook-example" markdown="1">

**Ví dụ (đọc mạch).**  
Sơ đồ: NOT($$A$$); OR($$\bar A, B$$); OR($$A, B, C$$); NOT($$C$$); AND ba ngõ ra $$Y$$.

$$
Y = (\bar A + B)\,(A + B + C)\,\bar C.
$$

</div>

![Đọc mạch ra biểu thức](/discrete-mathematics-for-computer-science-iuh/img/course/Circuit_to_expression.svg)

<p class="textbook-figure-caption" data-figure="13.19b">Ghi nhãn từng lớp cổng: $$Y = (\bar A+B)(A+B+C)\bar C$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ (vẽ từ biểu thức).**  

- (a) $$F = (x + y)\bar x$$: một OR($$x,y$$), một NOT($$x$$), một AND hai ngõ.  
  (Có thể rút gọn: $$F = x\bar x + y\bar x = y\bar x$$ — còn OR biến mất.)
- (b) $$G = (x + y + z)(\bar x\,\bar y\,\bar z)$$: một OR 3 ngõ, một AND 3 ngõ trên các litera phủ định, rồi AND hai ngõ (tích hai khối).

Luôn **đọc lại** sơ đồ vừa vẽ bằng cách ghi nhãn dây — nếu không khớp biểu thức, sơ đồ sai.

</div>

## 4. Tối thiểu hóa đại số cơ bản

### 4.1. Mục tiêu

Hai biểu thức **tương đương** nếu cùng bảng chân trị. Trong lớp biểu thức tương đương, ta ưa dạng có:

- ít **hạng** (số tích trong SOP),
- ít **litera**,
- ít **tầng** (khi có thể).

Tối thiểu hóa đại số = chuỗi biến đổi hợp lệ (tiên đề và hằng đẳng thức bài 13.1) cho đến khi không còn cắt gọn “rõ ràng” bằng tay.

Không có một thuật toán máy móc duy nhất “luôn làm A rồi B”; có **các kỹ thuật** hay dùng. Dưới đây là bộ kỹ thuật cơ bản — đủ cho hầu hết bài tập tay trước K-map (13.4) và Quine–McCluskey (13.5).

### 4.2. Kỹ thuật 1 — Đồng nhất và lũy đẳng

Dùng:

$$
x+x'=1,\quad xx'=0,\quad x+x=x,\quad xx=x,
$$
$$
x+0=x,\quad x\cdot 1=x,\quad x+1=1,\quad x\cdot 0=0.
$$

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = xy + x\bar y$$.  
$$F = x(y+\bar y) = x\cdot 1 = x$$.  
Ba litera ban đầu còn một tín hiệu — không cần cổng.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ (hai cách vẽ — vì sao phải rút gọn).**  
Đề: mạch ra **1** khi và chỉ khi $$x = y = z = 1$$ **hoặc** $$x = z = 1$$ và $$y = 0$$.

SOP (tổng các tích) chuẩn:

$$
F = xyz + x\bar y z.
$$

- **Cách 1 (vẽ thô):** hai AND 3-ngõ + một OR + một NOT — khoảng **4 cổng**.  
- **Cách 2 (rút rồi vẽ):**

$$
F = xyz + x\bar y z = xz(y + \bar y) = xz.
$$

Chỉ còn **một** AND hai ngõ. Cùng bảng chân trị; số cổng giảm mạnh.

</div>

![Hai cách hiện thực sau rút gọn](/discrete-mathematics-for-computer-science-iuh/img/course/Minimize_two_ways.svg)

<p class="textbook-figure-caption" data-figure="13.19c">$$xyz + x\bar y z = xz$$ — SOP thô so với một AND.</p>

### 4.3. Kỹ thuật 2 — Hấp thụ

$$
x + xy = x, \qquad x(x+y) = x.
$$

Hạng “nhỏ” bị hạng lớn nuốt. Dạng mở rộng hay gặp:

$$
x + \bar x\, y = x + y
$$

(chứng minh: $$x + \bar x y = (x+\bar x)(x+y) = x+y$$).

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = a + ab + ac$$.  
$$F = a(1+b+c) = a$$.  
Toàn bộ nhánh $$ab$$, $$ac$$ biến mất.

</div>

### 4.4. Kỹ thuật 3 — Phân phối và gom nhân tử chung

Kéo nhân tử chung ra ngoài (factoring) hoặc nhân vào để tạo cặp $$y+\bar y$$.  
Chiều $$x+(yz)=(x+y)(x+z)$$ đôi khi biến SOP (tổng các tích) thành dạng khác — chỉ dùng khi có lợi cho số cổng hoặc khi đề yêu cầu POS (tích các tổng).

<div class="textbook-example" markdown="1">

**Ví dụ (gom rồi đồng nhất).**  
$$F = xy + x\bar y + \bar x y$$.  

$$
F = x(y+\bar y) + \bar x y = x + \bar x y.
$$

Áp dụng $$x + \bar x y = x + y$$: $$F = x + y$$.  
So với ba AND + OR rộng, còn **một** OR hai ngõ.

</div>

### 4.5. Kỹ thuật 4 — De Morgan đẩy phủ định

$$
(x+y)' = x'y', \qquad (xy)' = x' + y'.
$$

Đưa NOT “ra ngoài biểu thức phức” thành NOT trên litera đơn, hoặc ngược lại khi cần NAND/NOR.

<div class="textbook-example" markdown="1">

**Ví dụ.** $$F = (x'+y)' + xy$$.  
$$F = xy' + xy = x(y'+y) = x$$.

</div>

### 4.6. Kỹ thuật 5 — Thêm hạng phụ (đôi khi)

Đôi khi **viết thêm** một hạng đã có (vì $$t+t=t$$) để tạo cặp gộp với hạng khác.  
Ví dụ $$xy + x\bar y + \bar x y$$: thêm một $$xy$$ rồi nhóm

$$
(xy + x\bar y) + (\bar x y + xy) = x + y.
$$

Cùng kết quả kỹ thuật 3, nhưng tư duy “tạo cặp $$y$$ / $$\bar y$$” rõ hơn trên giấy.

### 4.7. Chiến lược gợi ý khi làm bài

1. **Ưu tiên** hấp thụ và lũy đẳng trước (cắt nhanh).
2. Tìm cặp chỉ khác **một** litera bù để gom thành $$x$$ hoặc $$x+y$$.
3. De Morgan khi có ngoặc phủ định.
4. Phân phối khi thấy nhân tử chung.
5. **Dừng** khi mỗi bước tiếp không giảm litera/hạng một cách rõ ràng — và luôn **kiểm**.

### 4.8. Kiểm chứng sau khi rút gọn

Hai cách chắc chắn:

1. Lập bảng chân trị hai biểu thức (khi $$n$$ nhỏ, $$2^n$$ hàng).
2. Khi $$n$$ lớn hơn: thử mọi tổ hợp trên máy, hoặc ít nhất mọi hàng nơi dạng cũ bằng **1** và vài hàng bằng **0**.

Nếu tại một bộ giá trị hai vế lệch, phép biến đổi đã sai — thường do áp dụng De Morgan thiếu “đảo phép”.

![NOT trong chuỗi tối ưu](/discrete-mathematics-for-computer-science-iuh/img/course/Gate_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.15">Mỗi lớp NOT/AND/OR trên đường dài nhất làm tín hiệu “đi xa hơn”; biểu thức gọn thường (không phải luôn) giảm cả số cổng lẫn số tầng.</p>

<div class="textbook-example" markdown="1">

**Ví dụ tổng hợp.**  
$$F = ab' + ac + a'b + bc$$.  
Gom $$ab' + a'b$$ (XOR) và $$c(a+b)$$:

$$
F = (ab' + a'b) + c(a + b).
$$

Dạng này chưa hẳn “ít ký hiệu nhất” theo mọi metric, nhưng **rõ nghĩa**: bit $$a \oplus b$$, cộng thêm $$c$$ khi $$a$$ hoặc $$b$$ bật.

Kiểm nhanh:

| $$(a,b,c)$$ | Gốc | Dạng mới |
|:---:|:---:|:---:|
| $$(1,1,1)$$ | 1 | 1 |
| $$(1,0,0)$$ | 1 | 1 |
| $$(0,0,1)$$ | 0 | 0 |

Khi làm bài: mỗi bước ghi *đẳng thức nào*, rồi đối một vài vector — đừng nhảy cóc.

</div>

## 5. Độ phức tạp mạch (cách so sánh trên lớp)

Khi hai biểu thức **cùng bảng chân trị**, ta so “cái nào tốt hơn” bằng hai đại lượng đơn giản (đếm trên sơ đồ / bài tập):

| Đại lượng | Cách đếm trên bài tập | Ý nghĩa trực quan |
|:---|:---|:---|
| **Số cổng** | Đếm thô số AND, OR, NOT (hoặc quy hết về NAND nếu đề yêu cầu) | Mạch **phức tạp / gọn** đến đâu |
| **Số tầng** (độ sâu) | Đếm số lớp cổng trên đường dài nhất từ ngõ vào → ngõ ra | Tín hiệu phải “đi qua” bao nhiêu lớp trước khi ổn định |

Mạch hai tầng SOP (tổng các tích) thường **nông** (ít tầng) nhưng có thể **rộng** (nhiều cổng AND song song). Đôi khi chấp nhận thêm một tầng để tái dùng tín hiệu trung gian và giảm tổng số cổng.

<div class="textbook-example" markdown="1">

**Ví dụ đếm.**  
SOP dài $$F = x'y'z + x'yz' + xy'z' + xyz$$: khoảng 4 AND + 1 OR + NOT.  
Sau rút (ví dụ) $$F = x'z' + xz$$: 2 AND + 1 OR — số cổng giảm rõ; depth hai tầng giữ nguyên nếu vẫn SOP (tổng các tích).

</div>

## 6. NAND-only và NOR-only

Vì NAND đầy đủ, mọi SOP (tổng các tích) đều chuyển được sang mạng NAND bằng cách “đẩy” NOT (De Morgan) và thay AND–OR bằng cấu trúc NAND tương đương. **Tối thiểu hóa trước** khi map NAND thường rẻ hơn map xong mới rút.

| Phép | Chỉ NAND (Sheffer $$\mid$$) | Chỉ NOR (Peirce $$\downarrow$$) |
|:---|:---|:---|
| NOT | $$x' = (x \mid x)$$ | $$x' = (x \downarrow x)$$ |
| AND | $$xy = ((x \mid y) \mid (x \mid y))$$ | qua De Morgan + NOR |
| OR | $$x+y = (x' \mid y')$$ | $$x+y = ((x \downarrow y) \downarrow (x \downarrow y))$$ |

![NOT từ NAND](/discrete-mathematics-for-computer-science-iuh/img/course/NAND_to_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.20">NOT = NAND với hai ngõ nối chung: $$A' = A \mid A$$.</p>

![AND từ NAND](/discrete-mathematics-for-computer-science-iuh/img/course/NAND_to_AND.svg)

<p class="textbook-figure-caption" data-figure="13.21">AND = NAND rồi đảo bằng NAND: $$AB = (A\mid B)\mid(A\mid B)$$.</p>

![OR từ NAND](/discrete-mathematics-for-computer-science-iuh/img/course/NAND_to_OR.svg)

<p class="textbook-figure-caption" data-figure="13.22">OR theo De Morgan: $$A+B = A' \mid B'$$.</p>

### 6.1. Chỉ NOR (đối ngẫu NAND)

| Phép | Mạng chỉ NOR | Công thức |
|:---|:---|:---|
| NOT | 1 NOR, hai ngõ nối chung | $$A' = A \downarrow A$$ |
| OR | NOR rồi đảo bằng NOR | $$A+B = (A\downarrow B)\downarrow(A\downarrow B)$$ |
| AND | đảo từng ngõ rồi NOR (De Morgan) | $$AB = A' \downarrow B'$$ |

![NOT từ NOR](/discrete-mathematics-for-computer-science-iuh/img/course/NOR_to_NOT.svg)

<p class="textbook-figure-caption" data-figure="13.22a">NOT = NOR với hai ngõ nối chung: $$A' = A \downarrow A$$.</p>

![OR từ NOR](/discrete-mathematics-for-computer-science-iuh/img/course/NOR_to_OR.svg)

<p class="textbook-figure-caption" data-figure="13.22b">OR = NOR rồi đảo bằng NOR.</p>

![AND từ NOR](/discrete-mathematics-for-computer-science-iuh/img/course/NOR_to_AND.svg)

<p class="textbook-figure-caption" data-figure="13.22c">AND theo De Morgan: $$AB = A' \downarrow B'$$.</p>

Trên schematic, “bubble” NOT trên ngõ vào/ra của NAND/NOR là mẹo vẽ nhanh khi chuyển từ AND–OR. **Rút gọn biểu thức trước**, rồi mới map sang NAND-only / NOR-only — map xong mới rút thường tốn cổng hơn.

## 7. Năm bước thiết kế mạch tổ hợp từ yêu cầu

Nhiều đề bài không cho sẵn bảng chân trị mà cho **mô tả bằng lời** (công tắc, cảm biến, điều kiện bật đèn). Quy trình chuẩn — **mỗi bước một hình**:

![Bước 1 — Đặt biến](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_1.svg)

<p class="textbook-figure-caption" data-figure="13.23">Bước 1: đặt biến vào/ra và quy ước 0–1.</p>

![Bước 2 — Bảng chân trị](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_2.svg)

<p class="textbook-figure-caption" data-figure="13.24">Bước 2: lập bảng chân trị đầy đủ.</p>

![Bước 3 — Biểu thức](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_3.svg)

<p class="textbook-figure-caption" data-figure="13.25">Bước 3: viết SOP/POS chuẩn.</p>

![Bước 4 — Rút gọn](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_4.svg)

<p class="textbook-figure-caption" data-figure="13.26">Bước 4: rút gọn (đại số, K-map, QM).</p>

![Bước 5 — Vẽ mạch](/discrete-mathematics-for-computer-science-iuh/img/course/Design_step_5.svg)

<p class="textbook-figure-caption" data-figure="13.27">Bước 5: vẽ mạch AND–OR–NOT hoặc map NAND.</p>

1. **Đặt biến** ngõ vào và ngõ ra (quy ước: **1** = đóng/sáng, **0** = hở/tắt — hoặc ngược lại, nhưng **nhất quán**).
2. **Lập bảng chân trị** theo yêu cầu (liệt kê mọi tổ hợp vào).
3. **Viết** biểu thức logic: SOP (tổng các tích) từ các dòng $$Y = 1$$, hoặc POS (tích các tổng) từ các dòng $$Y = 0$$.
4. **Rút gọn** (đại số, K-map, hoặc QM) để giảm cổng.
5. **Vẽ mạch** từ biểu thức đã rút (AND–OR–NOT, hoặc map NAND/NOR nếu đề yêu cầu).

<div class="textbook-example" markdown="1">

**Ví dụ — ba công tắc và bóng đèn.**  
Một ngôi nhà có ba công tắc $$A$$, $$B$$, $$C$$. Đèn $$Y$$ sáng khi:

- cả ba công tắc đều **hở**, hoặc  
- công tắc 1 và 2 **đóng**, công tắc 3 **hở**.

Thiết kế mạch với số cổng càng ít càng tốt.

**Bước 1.** Đóng = **1**, hở = **0**; đèn sáng = **1**.

**Bước 2–3.** Chỉ hai dòng cho $$Y = 1$$: $$(A,B,C) = (0,0,0)$$ và $$(1,1,0)$$. SOP (tổng các tích) chuẩn:

$$
Y = \bar A\,\bar B\,\bar C + AB\,\bar C.
$$

**Bước 4.** Nhân tử chung $$\bar C$$:

$$
Y = \bar C\,(\bar A\,\bar B + AB) = \bar C\,(A \odot B),
$$

với $$A \odot B = AB + \bar A\,\bar B$$ (**XNOR**, không phải XOR).  
Lưu ý: một số slide cũ ghi nhầm “XOR” ở bước này — công thức và bảng chân trị xác nhận là **XNOR** (hai ngõ giống nhau).

Cũng có thể giữ $$Y = \bar C(\bar A\bar B + AB)$$ và vẽ bằng AND/OR/NOT (không cần cổng XNOR có sẵn).

**Bước 5.**

| Phương án | Mạch gợi ý | Ước lượng |
|:---|:---|:---|
| SOP thô | 2 AND 3-ngõ + 1 OR + 3 NOT | nhiều cổng hơn |
| Factor $$\bar C$$ | 2 AND 2-ngõ + 1 OR + 3 NOT | trung bình |
| Có XNOR | 1 XNOR + 1 NOT + 1 AND | ít khối nhất nếu được dùng XNOR |

</div>

![Bảng chân trị công tắc–đèn](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_truth_table.svg)

<p class="textbook-figure-caption" data-figure="13.28">Bảng chân trị ví dụ ba công tắc (chỉ hai dòng $$Y=1$$).</p>

![Mạch ba công tắc và đèn](/discrete-mathematics-for-computer-science-iuh/img/course/Three_switch_lamp.svg)

<p class="textbook-figure-caption" data-figure="13.29">Mạch rút gọn $$Y=\bar C(A\odot B)$$ — XNOR rồi AND với $$\bar C$$.</p>

**Gợi ý.** Bài “công tắc – đèn” và “cảm biến – còi” trong đề thi thường chỉ khác bảng chân trị; **năm bước** giữ nguyên. Rút gọn ở bước 4 chính là chỗ K-map / QM (bài 13.4–13.5) phát huy.

## 8. Gợi mở mạch cộng

Từ bảng cộng hai bit: $$S = A \oplus B$$ và $$C = AB$$ tạo half adder — đã tối giản.  
Full adder: $$S = A \oplus B \oplus C_{in}$$, $$C_{out} = AB + AC_{in} + BC_{in}$$ (majority).  

Bài 13.7 ghép chúng thành bộ cộng $$n$$-bit. Ở đây chỉ cần thấy: chúng là hàm Boole đã rút gọn + cổng — đúng quy trình năm bước ở mục 7.

## Bài tập

### Bài tập 1

Vẽ (mô tả tầng) mạch hai tầng cho $$F = x'y'z + xy$$. Đếm AND, OR, NOT (AND tối đa 3 ngõ).

<details>
<summary>Đáp án</summary>

Hai AND (3 ngõ và 2 ngõ), một OR 2 ngõ, hai NOT ($$x'$$, $$y'$$).

</details>

### Bài tập 2

Rút gọn bằng đại số (ghi rõ đẳng thức dùng):

(a) $$ab + ab' + a'b$$  
(b) $$xy + x'z + yz$$  
(c) $$(x'+y)' + x$$

<details>
<summary>Đáp án</summary>

(a) $$ab + ab' + a'b = a(b+b') + a'b = a + a'b = a + b$$ (đồng nhất, rồi $$a + a'b = a + b$$).

(b) $$xy + x'z + yz = xy + x'z + yz(x+x') = xy + x'z + xyz + x'yz$$.  
Gom $$xy + xyz = xy$$, $$x'z + x'yz = x'z$$ → $$F = xy + x'z$$.  
(Hoặc kiểm 8 dòng bảng chân trị.)

(c) $$(x'+y)' + x = xy' + x = x$$ (De Morgan rồi hấp thụ $$x + xy' = x$$).

</details>

### Bài tập 3

Giải thích vì sao NAND một mình đủ xây NOT, AND, OR (viết công thức). Làm tương tự với NOR cho NOT và OR.

<details>
<summary>Đáp án</summary>

NAND: $$x' = (x \mid x)$$; $$xy = ((x \mid y) \mid (x \mid y))$$; $$x + y = (x' \mid y')$$ với $$x'$$, $$y'$$ cũng bằng NAND.  
NOR: $$x' = (x \downarrow x)$$; $$x + y = ((x \downarrow y) \downarrow (x \downarrow y))$$; AND qua De Morgan.

</details>

### Bài tập 3b — Công tắc và đèn

Lặp lại ví dụ ba công tắc: viết bảng chân trị đầy đủ 8 dòng, SOP (tổng các tích) chuẩn, dạng rút gọn, và mô tả mạch. So sánh số AND+OR+NOT của SOP (tổng các tích) chuẩn với dạng có $$\bar C$$ và XNOR (đếm XNOR như 1 cổng phức).

<details>
<summary>Đáp án</summary>

Chỉ $$Y(0,0,0) = Y(1,1,0) = 1$$; $$Y = \bar A\bar B\bar C + AB\bar C = \bar C(\bar A\bar B + AB)$$.  
SOP (tổng các tích) chuẩn: 2 AND 3-ngõ + 1 OR + 3 NOT (có thể chia sẻ).  
Dạng XNOR: 1 XNOR + 1 NOT + 1 AND — thường ít khối hơn nếu được dùng cổng XNOR có sẵn.

</details>

### Bài tập 4

$$F = (ab)(cd)$$: so **số tầng** nếu có AND 4 ngõ (1 tầng) với cây hai AND 2 ngõ rồi AND (2 tầng). Khi quan tâm “tín hiệu ra chậm vì phải đi qua nhiều lớp cổng”, đại lượng nào quan trọng hơn?

<details>
<summary>Đáp án</summary>

Số tầng: 1 so với 2. Nếu đề hỏi về **độ trễ / đường dài nhất**, ưu tiên số tầng nhỏ. Nếu đề hỏi về **độ phức tạp / số linh kiện**, ưu tiên số cổng (và loại cổng).

</details>

### Bài tập 5

Cho $$F = ab'c + abc' + a'bc + abc$$.  
Rút gọn từng bước đến $$ab + bc + ca$$ (majority). Kiểm tại $$(a,b,c) = (1,1,0)$$ và $$(1,0,0)$$.

<details>
<summary>Đáp án</summary>

{% raw %}
$$
\begin{aligned}
F
&= ab'c + abc' + a'bc + abc \\
&= ab'c + abc' + bc(a'+a) \\
&= ab'c + abc' + bc.
\end{aligned}
$$
{% endraw %}

Tiếp tục gom về $$ab + bc + ca$$ (đối bảng: $$F = 1$$ đúng khi **ít nhất hai** trong ba biến bằng **1**).

Tại $$110$$: gốc và majority đều **1**.  
Tại $$100$$: cả hai **0**.

</details>

### Bài tập 6 — Đọc mạch

Cho mạch: NOT($$A$$); OR($$\bar A, B$$); OR($$A, B, C$$); NOT($$C$$); AND ba ngõ → $$Y$$.  
Viết biểu thức $$Y$$. (Không cần rút gọn.)

<details>
<summary>Đáp án</summary>

$$Y = (\bar A + B)(A + B + C)\bar C$$.

</details>

### Bài tập 7 — Rút gọn rồi đếm cổng

Hàm ra **1** khi $$(x,y,z) = (1,1,1)$$ hoặc $$(1,0,1)$$.

1. Viết SOP (tổng các tích) chuẩn.  
2. Rút gọn.  
3. So sánh số cổng AND/OR/NOT của SOP thô với dạng rút (không dùng XOR/XNOR).

<details>
<summary>Đáp án</summary>

1. $$F = xyz + x\bar y z$$.  
2. $$F = xz(y + \bar y) = xz$$.  
3. Thô ≈ 2 AND 3-ngõ + 1 OR + 1 NOT; rút ≈ **1 AND** 2-ngõ (0 NOT nếu lấy thẳng $$x,z$$).

</details>

### Bài tập 8 — Chỉ NOR

Viết mạng chỉ NOR cho NOT, OR, AND (công thức). Vẽ (mô tả) NOT và OR bằng NOR.

<details>
<summary>Đáp án</summary>

$$A' = A\downarrow A$$;  
$$A+B = (A\downarrow B)\downarrow(A\downarrow B)$$;  
$$AB = A'\downarrow B'$$ (mỗi $$A'$$, $$B'$$ cũng là NOR).  
Xem hình NOR_to_NOT / NOR_to_OR / NOR_to_AND trong mục 6.1.

</details>

## Xem thêm

- Bài 13.1 — ôn hấp thụ, De Morgan, phân phối; Sheffer / Peirce.
- Bài 13.2 — minterm, SOP (tổng các tích) / POS (tích các tổng) chuẩn.
- Bài 13.4 — khi muốn **nhìn** minterm kề trên lưới (K-map).
- Bài 13.7 — half/full adder, MUX từ cổng; ripple-carry (kể cả mẫu 3-bit HA+FA+FA).

## Tóm tắt

1. **Công tắc nối tiếp / song song** là trực giác AND / OR; mạng công tắc → biểu thức Boole.
2. **Cổng** hiện thực phép Boole theo bảng chân trị: NOT, AND, OR, NAND, NOR, XOR (khác nhau), XNOR (giống nhau).
3. **Hai chiều:** đọc mạch → biểu thức; biểu thức → vẽ mạch; SOP (tổng các tích) → AND–OR hai tầng; POS (tích các tổng) → OR–AND.
4. Tối thiểu hóa **đại số** (đồng nhất, hấp thụ, gom nhân tử, De Morgan) **trước** khi vẽ — ví dụ $$xyz + x\bar y z = xz$$.
5. **NAND/NOR** đầy đủ chức năng; map NOT/AND/OR sau khi đã rút; **năm bước** đưa yêu cầu lời → bảng → biểu thức → rút gọn → mạch.
6. Số cổng và số tầng đo chi phí sau khi rút. K-map, QM và mạch cộng ở các bài sau.
