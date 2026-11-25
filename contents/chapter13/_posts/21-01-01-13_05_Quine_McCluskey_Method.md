---
layout: post
title: "Phương pháp Quine–McCluskey"
categories: chapter13
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Phương pháp bảng Quine–McCluskey tối giản hàm Boole gồm hai giai đoạn: phép dán tìm nguyên nhân nguyên tố và bảng phủ chọn nguyên tố cốt yếu, kèm xử lý don't-care và so sánh với K-map."
---

> **Câu chuyện mở đầu:** Bản đồ Karnaugh tuyệt vời cho 3–4 biến, hơi chật chội ở 5 biến, và gần như **bất khả thi với mắt người** từ 6 biến trở lên (một mạch giải mã 16 biến có tới 65.536 ô!). Năm 1952–1956, Willard Quine và Edward McCluskey đã biến trực giác ghép cặp của K-map thành một **thuật toán dạng bảng hoàn toàn cơ khí hóa được trên máy tính**, đảm bảo tìm ra biểu thức SOP tối tiểu chính xác 100% cho bất kỳ số biến $$n$$ nào!

<div class="textbook-epigraph" markdown="1">

"Tabulate, combine, cover — Quine–McCluskey is the Karnaugh map written as an algorithm."

<span class="epigraph-attribution">— Tinh thần QM</span>

</div>

Phương pháp **Quine–McCluskey** (*tabulation method*) là kỹ thuật tối thiểu hóa hàm Boole có hệ thống dưới dạng bảng. Phương pháp này đặc biệt phù hợp khi số biến vượt quá bốn, thời điểm mà bản đồ Karnaugh trở nên khó quan sát và dễ bỏ sót nhóm. Các **nguyên nhân hạng $$n$$** (minterm / từ tối tiểu) được biểu diễn bằng chuỗi bit; các cặp chỉ khác nhau đúng một bit được **dán** (gộp) lại với nhau; sau đó ta chọn một tập hạng tử gọn nhất vẫn phủ đầy đủ hàm.

Về bản chất, Quine–McCluskey thực hiện cùng phép rút gọn đại số như K-map, nhưng trình bày thành quy trình bảng rõ ràng, dễ kiểm chứng từng bước và có thể cài đặt thành thuật toán trên máy tính.

Phương pháp gồm **hai phần** chính:

1. **Phần 1 — Tìm dạng tổng chuẩn tắc thu gọn.**  
   Xác định toàn bộ các số hạng **ứng viên** cho biểu thức cực tiểu — gọi là các **nguyên nhân nguyên tố** (*prime implicant*) của $$F$$ — xuất phát từ tập nguyên nhân hạng $$n$$ của **dạng nối rời chính tắc** (SOP chuẩn).

2. **Phần 2 — Tìm dạng tổng chuẩn tắc tối thiểu.**  
   Dựa trên **bảng phủ**, chọn một tập con nguyên nhân nguyên tố gọn nhất sao cho vẫn phủ hết mọi vị trí $$F = 1$$, từ đó thu được **dạng SOP tối tiểu**.

Kết quả là một dạng SOP hai tầng tối tiểu (hoặc một trong các phủ tối ưu tương đương).

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Giải thích** lý do sử dụng Quine–McCluskey khi số biến vượt quá phạm vi thuận tiện của K-map.
- **Trình bày** hai giai đoạn của phương pháp: tìm **nguyên nhân nguyên tố** và chọn phủ trên **bảng phủ**.
- **Thực hiện** **phép dán** (gộp minterm và đánh dấu `-` tại bit khác nhau) cho hàm 3–4 biến.
- **Xác định** **nguyên nhân nguyên tố cốt yếu** và hoàn thiện phủ tối tiểu.
- **Xử lý** các trạng thái don't-care: sử dụng ở phần 1 nhưng không bắt buộc phủ ở phần 2.
- **So sánh** Quine–McCluskey với K-map về phạm vi áp dụng và cách biểu diễn.

**Từ khóa**: Quine–McCluskey, dạng nối rời chính tắc, nguyên nhân hạng $$n$$ (minterm / từ tối tiểu), phép dán, nguyên nhân nguyên tố, nguyên tố cốt yếu, dạng tổng chuẩn tắc thu gọn / tối thiểu, SOP (tổng các tích), bảng phủ, don't-care.

</div>

## Kiến thức cần nhớ: Phương pháp Quine–McCluskey (QM) là gì?

### 1. Giai đoạn 1 — Gom nhóm theo Trọng số Hamming để tìm mọi Prime Implicant (PI)
- **Bản chất:** Hai minterm chỉ ghép cặp khử được 1 biến ($$xy + x\bar{y} = x$$) nếu biểu diễn nhị phân của chúng khác nhau đúng **1 vị trí** — nghĩa là số lượng bit $$1$$ (**trọng số Hamming**) của chúng hơn kém nhau đúng **1 đơn vị**! Chia các minterm vào từng nhóm theo trọng số $$0, 1, 2, \dots, n$$ giúp chỉ cần so sánh hai nhóm kề nhau!

### 2. Giai đoạn 2 — Bảng phủ Prime Implicant (Bài toán Set Cover)
- **Bản chất:** Sau khi thu toàn bộ các PI (những cụm không thể ghép thêm được nữa), ta lập bảng hàng là PI, cột là các minterm gốc cần phủ: chọn hết các **Essential PI** (cột chỉ có đúng 1 dấu `×`), rồi rút gọn hàng/cột bị trội (hoặc dùng **phương pháp Petrick** khi gặp vòng lặp đối xứng).

### 3. Giới hạn Độ phức tạp (NP-hard) & Cầu nối sang Espresso / SAT
- **Bản chất:** Số lượng PI trong trường hợp xấu nhất tăng theo hàm mũ $$\Omega(3^n/n)$$, và bài toán Set Cover là NP-hard. Vì thế trong thiết kế chip thực tế (hàng triệu cổng), QM là chuẩn mực chính xác cho $$n$$ nhỏ còn các bộ tổng hợp công nghiệp dùng heuristic (Espresso) và SAT!

## Ví dụ tính tay làm từng bước: Chạy Quine–McCluskey cho $$f(A,B,C) = \sum m(0, 1, 2, 5, 6, 7)$$

1. **Bước 1 — Phân nhóm theo số bit $$1$$:**
   - Nhóm 0: $$m_0 = 000$$
   - Nhóm 1: $$m_1 = 001,\; m_2 = 010$$
   - Nhóm 2: $$m_5 = 101,\; m_6 = 110$$
   - Nhóm 3: $$m_7 = 111$$

2. **Bước 2 — Ghép các cặp kề khác nhau đúng 1 bit (thay bit khác bằng dấu `-`):**
   - Nhóm 0–1: $$(0,1) \to 00-\; (\bar{A}\bar{B})$$, $$(0,2) \to 0-0\; (\bar{A}\bar{C})$$
   - Nhóm 1–2: $$(1,5) \to -01\; (\bar{B}C)$$, $$(2,6) \to -10\; (B\bar{C})$$
   - Nhóm 2–3: $$(5,7) \to 1-1\; (AC)$$, $$(6,7) \to 11-\; (AB)$$
   *(Kiểm tra vòng ghép tiếp theo: không có hai cụm nào có dấu `-` ở cùng vị trí mà chỉ khác 1 bit! Nên cả **6 cụm** trên đều là Prime Implicant!)*

3. **Bước 3 — Lập bảng phủ & phát hiện Chu trình đối xứng (Cyclic Core):**
   Mỗi minterm $$0, 1, 2, 5, 6, 7$$ đều được phủ bởi đúng **2 PI** (không có EPI nào!). Ta có hai nghiệm tối tiểu đồng hạng (đều gồm đúng 3 PI):
   - Nghiệm 1: $$\bar{A}\bar{B} + B\bar{C} + AC$$ (phủ $$(0,1), (2,6), (5,7)$$).
   - Nghiệm 2: $$\bar{A}\bar{C} + \bar{B}C + AB$$ (phủ $$(0,2), (1,5), (6,7)$$).

### Giải thích: Tại sao Quine–McCluskey vừa chính xác tuyệt đối vừa dễ lập trình?
#### Bước 1: Thay trực giác thị giác bằng trọng số Hamming
Không cần vẽ bảng 2D hay 3D — máy tính chỉ cần đếm số bit $$1$$ rồi so sánh các chuỗi nhị phân ở hai nhóm kề nhau (phép XOR chỉ có đúng một bit $$1$$!).

#### Bước 2: Đánh dấu tick `✓` để lọc ra mọi Prime Implicant
Bất kỳ chuỗi nào không ghép được với ai ở vòng kế tiếp đều tự động là một Prime Implicant cực đại.

#### Bước 3: Rút gọn bảng phủ bằng EPI và Luật Trội (Dominance)
Chọn ngay mọi EPI, xóa các cột đã phủ; xóa hàng bị trội (phủ ít hơn nhưng tốn nhiều biến hơn) và cột trội (dư thừa).

#### Bước 4: Dùng phương pháp Petrick xử lý phần lõi tuần hoàn (Cyclic Core)
Khi bảng còn lại không có EPI (như ví dụ trên!), viết tích các tổng điều kiện phủ từng cột rồi khai triển để tìm tập PI ít phần tử nhất.

$$
\text{Minterm}
\;\xrightarrow{\;\text{Nhóm trọng số Hamming + XOR}\;}\;
\text{Toàn bộ Prime Implicants}
\;\xrightarrow{\;\text{Bảng phủ + EPI / Petrick}\;}\;
\text{SOP tối tiểu chính xác}.
$$

## Vì sao cần thuật toán dạng bảng?

Bản đồ Karnaugh rất trực quan với hàm từ **2 đến 4 biến**: mỗi ô ứng với một minterm, hai ô kề nhau khác nhau đúng một bit, và việc khoanh nhóm tương đương áp dụng $$xy + x\bar y = x$$ bằng trực giác hình học. Tuy nhiên, từ **5 biến trở lên**, lưới trở nên cồng kềnh, có nhiều chiều vòng mép và rất dễ bỏ sót nhóm hợp lệ.

Quine–McCluskey khắc phục hạn chế đó bằng cách không phụ thuộc vào hình vẽ:

- mỗi nguyên nhân hạng $$n$$ được viết thành một **chuỗi bit** cố định (ví dụ 4 bit cho hàm $$wxyz$$);
- hai chuỗi **dán được** với nhau khi chúng chỉ khác nhau đúng **một** vị trí bit — tương ứng đẳng thức $$xy + x\bar y = x$$;
- các nhóm lớn trên K-map tương ứng với những chuỗi được dán qua nhiều vòng trên bảng.

Khi thực hành trên lớp, ta thường làm tay trên ví dụ **3–4 biến** để nắm chắc quy trình; với số biến lớn hơn, máy tính sẽ thực hiện chính xác cùng quy trình này.

![Bảng Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.21">Phương pháp bảng: phân nhóm theo số bit 1; mũi tên minh họa phép dán tạo ra các hạng tử rộng hơn (ít litera hơn).</p>

![K-map — đối chiếu](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.22">Cùng mục tiêu tìm SOP tối tiểu: K-map thao tác trên lưới, còn Quine–McCluskey thao tác trên bảng.</p>

## Phần 1 — Tìm dạng tổng chuẩn tắc thu gọn

### Sinh các nguyên nhân nguyên tố

Mục tiêu của phần 1 là từ **dạng nối rời chính tắc** (tổng các nguyên nhân hạng $$n$$), tìm **tất cả** các tích không thể mở rộng thêm được nữa. Trong tài liệu tiếng Việt, mỗi tích như vậy gọi là một **nguyên nhân nguyên tố** của $$F$$ (tiếng Anh: *prime implicant*). Đó là các đơn thức tích không thể bỏ thêm biến nào mà vẫn chỉ phủ các điểm làm $$F = 1$$ (và các ô don't-care cho phép).

**Quy trình tìm dạng tổng chuẩn tắc thu gọn:**

**Bước 1.** Liệt kê vào **cột thứ nhất** chuỗi bit của tất cả các **nguyên nhân hạng $$n$$** của hàm $$F$$ (các minterm), chia thành từng nhóm có cùng số bit **1** và sắp xếp các nhóm theo **số bit 1 tăng dần**.

**Bước 2.** Lần lượt thực hiện mọi **phép dán** có thể giữa một chuỗi ở nhóm có $$k$$ bit 1 với một chuỗi ở nhóm có $$k+1$$ bit 1 ($$k = 0, 1, 2, \ldots$$):

- Hai chuỗi **dán được** khi chỉ khác nhau đúng **một** vị trí bit; vị trí khác nhau được thay bằng dấu `-`.
- Mọi chuỗi tham gia vào **ít nhất một** phép dán đều được đánh dấu `*` bên cạnh.
- Các chuỗi mới tạo thành được ghi vào **cột kế tiếp** (loại bỏ bản sao trùng lặp).

**Bước 3.** Lặp lại Bước 2 trên cột mới tạo cho đến khi **không** thể thực hiện thêm phép dán nào nữa. Khi đó, **toàn bộ các biểu diễn không có dấu `*`** ở tất cả các cột chính là tập hợp đầy đủ các **nguyên nhân nguyên tố** của $$F$$.

**Cơ sở toán học.** Mỗi phép dán tương ứng với một lần áp dụng hằng đẳng thức:

$$
xy + x\bar y = x.
$$

Số dấu `-` càng nhiều thì tích tương ứng càng ít litera, tương đương với nhóm kích thước $$2^k$$ trên K-map.

![Bảng chân trị / minterm](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.23">Điểm xuất phát của thuật toán là tập nguyên nhân hạng $$n$$ (các hàng có $$F = 1$$) trong dạng nối rời chính tắc.</p>

## Phần 2 — Tìm dạng tổng chuẩn tắc tối thiểu

### Bảng phủ và nguyên tố cốt yếu

Sau phần 1, ta thu được toàn bộ các **nguyên nhân nguyên tố**, nhưng thường không cần dùng hết tất cả để biểu diễn $$F$$. Phần 2 chọn ra một **phủ tối tiểu** (ưu tiên ít hạng tử nhất; nếu bằng nhau thì ưu tiên ít litera nhất).

Cách lập **bảng phủ**:

- mỗi **hàng** ứng với một nguyên nhân nguyên tố;
- mỗi **cột** ứng với một minterm **bắt buộc** (vị trí $$F = 1$$; **không** đưa các vị trí don't-care vào cột);
- đánh dấu `+` (hoặc ×) tại giao điểm nếu nguyên nhân nguyên tố ở hàng đó phủ minterm ở cột tương ứng.

Một nguyên nhân nguyên tố gọi là **cốt yếu** (*essential prime implicant*) nếu tồn tại ít nhất một cột chỉ chứa **đúng một** dấu `+` nằm trên hàng của nó — khi đó ta bắt buộc phải chọn hàng này.

**Quy trình tìm dạng tổng chuẩn tắc tối thiểu:**

**Bước 1.** Xác định toàn bộ các **nguyên nhân nguyên tố cốt yếu**.

**Bước 2.** Xóa tất cả các **cột** đã được phủ bởi những nguyên nhân nguyên tố cốt yếu này.

**Bước 3.** Trên bảng thu gọn, xóa các **dòng** không còn dấu `+`. Nếu có hai cột giống hệt nhau thì có thể bỏ bớt một cột.

**Bước 4.** Từ các hàng còn lại, chọn một tập $$S$$ gồm ít nguyên nhân nguyên tố nhất (và ít litera nhất) sao cho phủ hết các cột còn lại.

Kết quả thu được là tổng của các nguyên tố cốt yếu hợp với $$S$$ — đó là **dạng tổng chuẩn tắc tối thiểu** (SOP tối tiểu). Quy trình này hoàn toàn tương ứng với việc chọn tế bào cốt yếu rồi hoàn tất phủ trên K-map (Mục 13.4).

## Don't-care trong Quine–McCluskey

Khi đặc tả bài toán **không quan tâm** giá trị đầu ra tại một số tổ hợp đầu vào (tổ hợp không bao giờ xuất hiện), ta ký hiệu chúng là **don't-care** ($$d$$ hoặc $$X$$).

Cách xử lý don't-care trong Quine–McCluskey tách bạch rõ theo hai giai đoạn:

- **Phần 1 (tìm nguyên nhân nguyên tố):** đưa các vị trí don't-care vào bảng ngay từ đầu như các minterm thông thường để tăng cơ hội dán thành các nguyên nhân nguyên tố lớn hơn (ít litera hơn).
- **Phần 2 (bảng phủ):** **không** lập cột cho các vị trí don't-care vì ta không bắt buộc phải phủ chúng.

<div class="textbook-example" markdown="1">

**Ví dụ (3 biến có don't-care).** Cho $$F(a,b,c)$$ bằng **1** tại các hàng **1, 2, 5** và don't-care tại **0, 7**.

Ở phần 1, ta đưa cả $$0$$ và $$7$$ vào dán cùng với $$1, 2, 5$$. Sang phần 2, bảng phủ **chỉ** gồm ba cột $$1$$, $$2$$, $$5$$. Một phủ tối tiểu thu được là:

$$
F = \bar a\,\bar c + \bar b\,c.
$$

Ta có thể kiểm chứng lại trên bảng chân trị 8 dòng (bằng 1 tại 1, 2, 5 và bằng 0 tại 3, 4, 6).

</div>

## Ví dụ bốn biến

Xét hàm $$F(a,b,c,d)$$ nhận giá trị **1** tại các hàng **0, 2, 3, 5, 7, 8, 10, 11, 13, 15**.

Sau khi phân nhóm theo số bit 1 và thực hiện hai vòng phép dán, ta thu được **bốn** nguyên nhân nguyên tố (mỗi nguyên nhân phủ 4 minterm và không thể dán tiếp):

- $$N_1=\bar b\,\bar d$$ phủ $$0,2,8,10$$;
- $$N_2=\bar b\,c$$ phủ $$2,3,10,11$$;
- $$N_3=cd$$ phủ $$3,7,11,15$$;
- $$N_4=bd$$ phủ $$5,7,13,15$$.

Bảng phủ cho 10 minterm bắt buộc:

| Nguyên nhân nguyên tố | 0 | 2 | 3 | 5 | 7 | 8 | 10 | 11 | 13 | 15 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $$N_1=\bar b\,\bar d$$ | + | + |  |  |  | + | + |  |  |  |
| $$N_2=\bar b\,c$$ |  | + | + |  |  |  | + | + |  |  |
| $$N_3=cd$$ |  |  | + |  | + |  |  | + |  | + |
| $$N_4=bd$$ |  |  |  | + | + |  |  |  | + | + |

**Xác định nguyên tố cốt yếu.** Cột $$0$$ và $$8$$ chỉ có dấu `+` ở $$N_1$$; cột $$5$$ và $$13$$ chỉ có dấu `+` ở $$N_4$$. Do đó $$N_1=\bar b\,\bar d$$ và $$N_4=bd$$ là hai nguyên tố **cốt yếu**. Hai nguyên tố này phủ các cột $$0,2,8,10$$ và $$5,7,13,15$$, chỉ **còn lại** hai cột $$3$$ và $$11$$.

**Vì sao không thể bỏ $$bd$$.** Hai minterm $$5=0101$$ và $$13=1101$$ đều có $$b=1$$ và $$c=0$$, trong khi $$\bar b\,\bar d$$ đòi hỏi $$b=0$$ còn $$cd$$ đòi hỏi $$c=1$$. Chỉ có $$bd$$ phủ được $$5$$ và $$13$$, nên $$cd+\bar b\,\bar d$$ không phải là một phủ đầy đủ của $$F$$.

**Phủ nốt cột $$3$$ và $$11$$.** Cả $$N_3=cd$$ và $$N_2=\bar b\,c$$ đều phủ được cả $$3$$ lẫn $$11$$ và cùng có 2 litera, nên chọn một trong hai đều cho phủ tối tiểu (3 hạng, 6 litera):

$$
F = cd + \bar b\,\bar d + bd
$$

hoặc phương án tương đương $$F = \bar b\,c + \bar b\,\bar d + bd$$. Không thể có phủ chỉ gồm 2 hạng vì hai nguyên tố cốt yếu chưa phủ được $$3$$ và $$11$$.

Hai thao tác cần chú ý nhất khi làm bài là đánh dấu `*` đầy đủ sau mỗi phép dán (phần 1) và rà soát các cột chỉ có duy nhất một dấu `+` để không bỏ sót nguyên tố cốt yếu (phần 2).

### Video ngắn: Quine–McCluskey

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/quine-mccluskey.mp4"></video>
</div>

Video dài khoảng 3 phút 13 giây, minh họa trực tiếp ví dụ bốn biến ở trên: phân nhóm minterm theo số bit 1, dán qua hai vòng kèm đánh dấu, xác định bốn nguyên nhân nguyên tố, lập bảng phủ, chọn nguyên tố cốt yếu để thu được $$F = \bar b\,\bar d + bd + cd$$, và kết thúc với ví dụ có don't-care.

## Ví dụ đầy đủ — hàm $$F_1$$

Phần dưới đây trình bày trọn vẹn lời giải dạng bảng cho một bài toán tiêu biểu: rút gọn một biểu thức SOP 4 biến bằng Quine–McCluskey.

<div class="textbook-example" markdown="1">

**Đề bài.** Cho hàm Boole:

$$
\begin{aligned}
F_1
&=
\overline{w}\,xy\,\overline{z}
+\overline{w}\,x\,\overline{y}\,z
+\overline{w}\,xyz
+w\,\overline{x}\,\overline{y}\,z
+w\,\overline{x}\,yz
+wxyz.
\end{aligned}
$$

Hãy tối thiểu hóa $$F_1$$ bằng phương pháp Quine–McCluskey theo thứ tự biến $$wxyz$$ (từ bit cao đến bit thấp).

### Bước 0 — Chuyển từng hạng thành nguyên nhân hạng $$n$$ (minterm)

Với mỗi tích đầy đủ 4 biến:

- biến ở dạng nguyên (không gạch trên) ứng với bit **1**;
- biến ở dạng bù (có gạch trên) ứng với bit **0**;
- đổi chuỗi 4 bit sang hệ thập phân để lấy chỉ số minterm.

| Hạng trong $$F_1$$ | Mã $$wxyz$$ | Nguyên nhân hạng $$n$$ |
|:---|:---:|:---:|
| $$\overline{w}xy\overline{z}$$ | $$0110$$ | $$m_6$$ |
| $$\overline{w}x\overline{y}z$$ | $$0101$$ | $$m_5$$ |
| $$\overline{w}xyz$$ | $$0111$$ | $$m_7$$ |
| $$w\overline{x}\overline{y}z$$ | $$1001$$ | $$m_9$$ |
| $$w\overline{x}yz$$ | $$1011$$ | $$m_{11}$$ |
| $$wxyz$$ | $$1111$$ | $$m_{15}$$ |

Như vậy, $$F_1$$ bằng **1** tại 6 hàng **5, 6, 7, 9, 11, 15** (không có don't-care).

### Phần 1 — Phân nhóm theo số bit 1 (Bước 1)

| Nhóm (số bit 1) | Minterm | Mã $$wxyz$$ |
|:---:|:---:|:---:|
| 2 | 5 | $$0101$$ |
| 2 | 6 | $$0110$$ |
| 2 | 9 | $$1001$$ |
| 3 | 7 | $$0111$$ |
| 3 | 11 | $$1011$$ |
| 4 | 15 | $$1111$$ |

### Phần 1 — Phép dán lần 1 (Bước 2)

Ta so sánh từng cặp giữa **nhóm 2 và nhóm 3**, rồi giữa **nhóm 3 và nhóm 4**. Hai mã khác nhau đúng một bit được dán lại bằng cách thay bit khác nhau bằng `-`, đồng thời đánh dấu `*` cho mọi mã đã tham gia dán.

| Cặp dán | Mã mới | Phủ các minterm | Tích tương ứng |
|:---|:---:|:---:|:---|
| $$5$$ với $$7$$ | $$01{-}1$$ | $$5,7$$ | $$\overline{w}\,x\,z$$ ($$y$$ tự do) |
| $$6$$ với $$7$$ | $$011{-}$$ | $$6,7$$ | $$\overline{w}\,xy$$ ($$z$$ tự do) |
| $$9$$ với $$11$$ | $$10{-}1$$ | $$9,11$$ | $$w\,\overline{x}\,z$$ ($$y$$ tự do) |
| $$7$$ với $$15$$ | $${-}111$$ | $$7,15$$ | $$xyz$$ ($$w$$ tự do) |
| $$11$$ với $$15$$ | $$1{-}11$$ | $$11,15$$ | $$wyz$$ ($$x$$ tự do) |

Vì cả 6 minterm $$5,6,7,9,11,15$$ đều đã được dán ít nhất một lần, không còn minterm đơn lẻ nào là nguyên nhân nguyên tố.

### Phần 1 — Kiểm tra phép dán lần 2 (Bước 3)

Hai mã đã chứa dấu `-` chỉ dán tiếp được khi:

1. các dấu `-` nằm ở **cùng vị trí**, và  
2. các bit còn lại khác nhau đúng **một** vị trí.

Kiểm tra các mã vừa tạo:

- $$01{-}1$$ và $$10{-}1$$ có dấu `-` ở cùng cột, nhưng phần bit còn lại $$01$$ và $$10$$ khác nhau tới **hai** bit nên không dán được;
- các cặp còn lại đều có vị trí dấu `-` khác nhau nên cũng không dán được.

Do đó không sinh thêm được nguyên nhân nào phủ 4 minterm. Cả **năm** mã thu được ở vòng 1 đều không có dấu `*`, nên chúng là toàn bộ các **nguyên nhân nguyên tố**:

| Ký hiệu | Mã | Tích (nguyên nhân nguyên tố) | Phủ |
|:---:|:---:|:---|:---|
| $$N_1$$ | $$01{-}1$$ | $$\overline{w}\,xz$$ | $$5,7$$ |
| $$N_2$$ | $$011{-}$$ | $$\overline{w}\,xy$$ | $$6,7$$ |
| $$N_3$$ | $$10{-}1$$ | $$w\overline{x}z$$ | $$9,11$$ |
| $$N_4$$ | $${-}111$$ | $$xyz$$ | $$7,15$$ |
| $$N_5$$ | $$1{-}11$$ | $$wyz$$ | $$11,15$$ |

### Phần 2 — Bảng phủ

| Nguyên nhân nguyên tố | 5 | 6 | 7 | 9 | 11 | 15 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $$N_1=\overline{w}xz$$ | + |  | + |  |  |  |
| $$N_2=\overline{w}xy$$ |  | + | + |  |  |  |
| $$N_3=w\overline{x}z$$ |  |  |  | + | + |  |
| $$N_4=xyz$$ |  |  | + |  |  | + |
| $$N_5=wyz$$ |  |  |  |  | + | + |

### Phần 2 — Xác định nguyên tố cốt yếu (Bước 1)

| Cột minterm | Các nguyên nhân phủ | Kết luận |
|:---:|:---|:---|
| 5 | chỉ $$N_1$$ | $$N_1$$ **cốt yếu** |
| 6 | chỉ $$N_2$$ | $$N_2$$ **cốt yếu** |
| 9 | chỉ $$N_3$$ | $$N_3$$ **cốt yếu** |
| 7 | $$N_1$$, $$N_2$$, $$N_4$$ | chưa bắt buộc thêm |
| 11 | $$N_3$$, $$N_5$$ | chưa bắt buộc thêm |
| 15 | $$N_4$$, $$N_5$$ | chưa bắt buộc thêm |

Khi chọn ba nguyên tố cốt yếu $$N_1, N_2, N_3$$ và xóa các cột đã được phủ (Bước 2), ta đã phủ xong $$5, 6, 7, 9, 11$$, chỉ **còn lại** duy nhất cột $$15$$.

### Phần 2 — Phủ nốt $$m_{15}$$ (Bước 3–4)

Cột $$15$$ có thể được phủ bởi $$N_4=xyz$$ hoặc $$N_5=wyz$$ với cùng chi phí. Chọn một trong hai đều cho SOP tối tiểu gồm 4 tích:

$$
\begin{aligned}
F_1
&= \overline{w}\,xz + \overline{w}\,xy + w\overline{x}z + xyz, \\[0.4em]
F_1
&= \overline{w}\,xz + \overline{w}\,xy + w\overline{x}z + wyz.
\end{aligned}
$$

Nếu muốn viết gọn hơn ở dạng nhiều tầng, có thể đặt nhân tử chung:

$$
\begin{aligned}
F_1
&= \overline{w}\,x(y+z) + w\overline{x}z + xyz, \\[0.4em]
F_1
&= \overline{w}\,x(y+z) + wz(\overline{x}+y).
\end{aligned}
$$

Không tồn tại phủ nào ít hơn 4 hạng vì cả ba nguyên tố cốt yếu đều bắt buộc mà vẫn còn thiếu $$m_{15}$$.

### Kiểm chứng nhanh

- Biểu thức ban đầu có **6** hạng; dạng SOP tối tiểu chỉ còn **4** hạng.
- Tại $$m_{15}$$ ($$1111$$): cả hai đáp án đều bằng **1** nhờ $$xyz$$ hoặc $$wyz$$.
- Tại $$m_5$$ ($$0101$$): chỉ có hạng $$\overline{w}xz$$ bằng **1**.
- Tại $$m_0$$ ($$0000$$): mọi hạng đều bằng **0**, khớp với tập minterm ban đầu.

Nếu vẽ tập minterm **5, 6, 7, 9, 11, 15** lên K-map 4 biến, ta sẽ thấy chính xác năm nhóm tương ứng với $$N_1, \ldots, N_5$$.

</div>

## So sánh với bản đồ Karnaugh

| Phương pháp | Đặc trưng | Phạm vi phù hợp |
|:---|:---|:---|
| Bản đồ Karnaugh (K-map) | Trực quan trên lưới hai chiều | 2–4 biến |
| Quine–McCluskey | Quy trình bảng, phép dán và bảng phủ | Dễ thuật toán hóa; áp dụng cho số biến lớn hơn |
| Công cụ phần mềm EDA | Tự động hóa trên cùng khung nguyên lý | Mạch quy mô lớn |

Cốt lõi chung của cả hai phương pháp là **gộp các hạng tử kề nhau (khác nhau đúng 1 bit)** rồi **chọn một phủ đầy đủ và ngắn gọn nhất**.

<div class="interactive-demo" markdown="1">
<div data-demo="quine-mccluskey-simplifier"></div>
</div>
<script src="{{ '/public/js/quine-mccluskey-simplifier.js' | relative_url }}"></script>

### Minh họa tương tác

Chạy mô phỏng Quine–McCluskey từng bước trên các ví dụ trong bài (hàm $$F_1$$, ví dụ có don't-care và ví dụ bốn biến): phân nhóm theo số bit 1, dán cặp có dấu `-`, đánh dấu ✓, liệt kê nguyên nhân nguyên tố, lập bảng phủ với nguyên tố cốt yếu, trội hàng/cột và phương pháp Petrick. Với 2–4 biến, công cụ hiển thị kèm K-map để đối chiếu; bạn cũng có thể nhập trực tiếp minterm, don't-care hoặc biểu thức từ 2 đến 6 biến.

<div class="interactive-demo" markdown="1">
<div data-demo="qm-explainer" data-preset="f1"></div>
</div>
<script src="{{ '/public/js/explainers/qm-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Thực hiện Quine–McCluskey bằng tay cho hàm $$F(a,b,c,d)$$ nhận giá trị **1** tại các hàng **0, 2, 3, 5, 7, 8, 10, 11, 13, 15** và xác định các **nguyên nhân nguyên tố cốt yếu**.

<details>
<summary>Đáp án</summary>

Đối chiếu phần *Ví dụ bốn biến*: hàm có bốn nguyên nhân nguyên tố là $$\bar b\,\bar d$$, $$\bar b\,c$$, $$cd$$ và $$bd$$. Hai nguyên tố **cốt yếu** là $$\bar b\,\bar d$$ (duy nhất phủ $$0$$ và $$8$$) và $$bd$$ (duy nhất phủ $$5$$ và $$13$$). Để phủ nốt $$3$$ và $$11$$, chọn $$cd$$ (hoặc $$\bar b\,c$$), thu được SOP tối tiểu $$F = cd + \bar b\,\bar d + bd$$.

</details>

### Bài tập 2

Cho $$F(a,b,c)$$ bằng **1** tại các hàng **1, 2, 5** và don't-care tại **0, 7**. Hoàn thành cả phần 1 và phần 2 của phương pháp Quine–McCluskey (lưu ý: don't-care chỉ dùng để dán ở phần 1).

<details>
<summary>Đáp án</summary>

Một phủ tối tiểu là $$F = \bar a\,\bar c + \bar b\,c$$ (có thể kiểm chứng trên bảng chân trị 8 dòng).

</details>

### Bài tập 3

Cho $$F(x,y,z)$$ bằng **1** tại các hàng **0, 1, 4, 5, 6**. Tối thiểu hóa hàm bằng cả **K-map** và **Quine–McCluskey**, rồi so sánh kết quả SOP thu được.

<details>
<summary>Đáp án</summary>

Cả hai phương pháp đều cho cùng một hàm tối tiểu duy nhất: nhóm 4 minterm $$\{0, 1, 4, 5\}$$ cho $$\bar y$$ và nhóm 2 minterm $$\{4, 6\}$$ cho $$x\bar z$$, nên $$F = \bar y + x\bar z$$. (Kiểm chứng trên bảng 8 dòng: hàm bằng 1 đúng tại các hàng 0, 1, 4, 5, 6.)

</details>

### Bài tập 4 — Hàm $$F_1$$ (đối chiếu ví dụ đầy đủ ở trên)

Cho

$$
\begin{aligned}
F_1
&=
\overline{w}xy\overline{z}
+\overline{w}x\overline{y}z
+\overline{w}xyz
+w\overline{x}\overline{y}z
+w\overline{x}yz
+wxyz.
\end{aligned}
$$

1. Liệt kê các hàng có $$F_1=1$$ (dạng nối rời chính tắc) theo thứ tự bit $$wxyz$$.
2. Thực hiện **phần 1**: phân nhóm, dán cặp và liệt kê toàn bộ **nguyên nhân nguyên tố**.
3. Lập **bảng phủ**, xác định các **nguyên tố cốt yếu** và hoàn tất phủ.
4. Viết ít nhất một dạng SOP tối tiểu và nêu phủ tối tiểu thứ hai (nếu có).

<details>
<summary>Đáp án chi tiết</summary>

**1. Chuyển sang nguyên nhân hạng $$n$$ (minterm)**

| Hạng | $$wxyz$$ | $$m$$ |
|:---|:---:|:---:|
| $$\overline{w}xy\overline{z}$$ | $$0110$$ | 6 |
| $$\overline{w}x\overline{y}z$$ | $$0101$$ | 5 |
| $$\overline{w}xyz$$ | $$0111$$ | 7 |
| $$w\overline{x}\overline{y}z$$ | $$1001$$ | 9 |
| $$w\overline{x}yz$$ | $$1011$$ | 11 |
| $$wxyz$$ | $$1111$$ | 15 |

Vậy $$F_1 = 1$$ tại các hàng **5, 6, 7, 9, 11, 15**.

**2. Phần 1 — phép dán**

Phân nhóm theo số bit 1: $$\{5,6,9\}$$ (2 bit), $$\{7,11\}$$ (3 bit), $$\{15\}$$ (4 bit).

Năm **nguyên nhân nguyên tố** (không dán tiếp được thành nhóm 4 ô):

| Mã | Tích | Phủ |
|:---:|:---|:---|
| $$01{-}1$$ | $$\overline{w}xz$$ | 5, 7 |
| $$011{-}$$ | $$\overline{w}xy$$ | 6, 7 |
| $$10{-}1$$ | $$w\overline{x}z$$ | 9, 11 |
| $${-}111$$ | $$xyz$$ | 7, 15 |
| $$1{-}11$$ | $$wyz$$ | 11, 15 |

**3. Phần 2 — bảng phủ**

|  | 5 | 6 | 7 | 9 | 11 | 15 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $$\overline{w}xz$$ | + |  | + |  |  |  |
| $$\overline{w}xy$$ |  | + | + |  |  |  |
| $$w\overline{x}z$$ |  |  |  | + | + |  |
| $$xyz$$ |  |  | + |  |  | + |
| $$wyz$$ |  |  |  |  | + | + |

Các nguyên tố cốt yếu: cột 5 → $$\overline{w}xz$$; cột 6 → $$\overline{w}xy$$; cột 9 → $$w\overline{x}z$$.  
Ba nguyên tố này phủ $$5,6,7,9,11$$; còn lại cột $$15$$ nên chọn thêm **$$xyz$$** hoặc **$$wyz$$**.

**4. SOP tối tiểu** (hai phủ tương đương):

$$
F_1 = \overline{w}xz + \overline{w}xy + w\overline{x}z + xyz
$$

hoặc

$$
F_1 = \overline{w}xz + \overline{w}xy + w\overline{x}z + wyz.
$$

Có thể đặt nhân tử chung:

$$
F_1 = \overline{w}x(y+z) + w\overline{x}z + xyz
= \overline{w}x(y+z) + wz(\overline{x}+y).
$$

Xem lại mục *Ví dụ đầy đủ — hàm $$F_1$$* ở trên để đối chiếu từng bảng và bước kiểm chứng.

</details>

## Xem thêm

- Mục 13.4 — bản đồ Karnaugh (tế bào lớn tương ứng với nguyên nhân nguyên tố).  
- Mục 13.2 — dạng nối rời chính tắc (SOP chuẩn).  
- Mục 13.6 — ứng dụng trong thiết kế mạch số.

## Tóm tắt

1. Quine–McCluskey tối thiểu hóa hàm Boole bằng **bảng**, phù hợp khi số biến vượt quá phạm vi trực quan của K-map.  
2. **Phần 1** (dạng tổng chuẩn tắc thu gọn): dán các chuỗi bit khác nhau đúng một vị trí; các biểu diễn không bị đánh dấu `*` là **nguyên nhân nguyên tố**.  
3. **Phần 2** (dạng tổng chuẩn tắc tối thiểu): lập **bảng phủ**, chọn các **nguyên tố cốt yếu** rồi phủ tiếp các cột còn lại.  
4. **Don't-care** chỉ tham gia ở phần 1 để tạo hạng tử gọn hơn, không bắt buộc phủ ở phần 2.  
5. K-map và Quine–McCluskey dựa trên cùng nguyên lý “dán rồi phủ”, chỉ khác nhau về hình thức biểu diễn và quy mô áp dụng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=8YbbV42UX7Q">#006 TOÁN RỜI RẠC Tối thiểu hóa biểu thức logic mệnh đề  bằng Thuật toán Quine_McCluskey</a> — Đỗ Văn Đức - ĐH GTVT, tiếng Việt. Hướng dẫn thuật toán Quine–McCluskey bằng tiếng Việt.
- <a href="https://www.youtube.com/watch?v=l1jgq0R5EwQ">Quine-McCluskey Minimization Technique (Tabular Method)</a> — Neso Academy, tiếng Anh. Trình bày phương pháp bảng: dán minterm và chọn phủ.
- <a href="https://www.youtube.com/watch?v=wmM7Y5qQqu4">Quine-McCluskey Method: Boolean Function Minimization Explained!</a> — CodeLucky, tiếng Anh. Ví dụ ngắn gọn giúp đối chiếu các bước tối thiểu hóa.
