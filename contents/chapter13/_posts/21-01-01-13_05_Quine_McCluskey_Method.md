---
layout: post
title: "Phương pháp Quine–McCluskey"
categories: chapter13
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Thuật toán Quine–McCluskey: sinh implicant nguyên tố bằng gộp minterm, bảng phủ, implicant cốt yếu và so sánh với K-map."
---

<div class="textbook-epigraph" markdown="1">

"Tabulate, combine, cover — Quine–McCluskey is the Karnaugh map written as an algorithm."

<span class="epigraph-attribution">— Tinh thần QM</span>

</div>

Bản đồ Karnaugh (bài 13.4) phát huy khi mắt còn nhìn nổi lưới. Khi số biến tăng, ta cần một quy trình **không phụ thuộc hình vẽ** — có thể kiểm từng bước và sau này lập trình được.

**Quine–McCluskey** (phương pháp bảng, *tabulation method*) làm đúng việc mắt đã làm trên K-map, nhưng bằng bảng:

1. **Pha 1 — Sinh implicant nguyên tố:** gộp các minterm chỉ khác **một** bit cho đến khi không gộp thêm được.
2. **Pha 2 — Chọn phủ:** trên bảng phủ, chọn tập implicant tối thiểu che hết các minterm bắt buộc.

Kết quả là **SOP** (tổng các tích) hai tầng tối tiểu, hoặc một trong các cover tối ưu tương đương.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Mô tả** hai pha: sinh implicant nguyên tố và chọn cover trên bảng phủ.
- **Thực hiện** kết hợp minterm (dấu `-` tại bit khác nhau) cho hàm nhỏ.
- **Nhận** implicant cốt yếu và hoàn tất cover.
- **Xử lý** don't-care: dùng ở pha 1, không bắt buộc ở pha 2.
- **So sánh** QM với K-map và nêu khi nào nên dùng máy tính.

**Từ khóa**: Quine–McCluskey, implicant nguyên tố, bảng phủ, implicant cốt yếu, don't-care.

</div>

## 1. Vì sao cần thuật toán bảng?

K-map trực quan đến khoảng bốn biến; năm–sáu biến đã chật và dễ sót wrap-around. Quine–McCluskey không vẽ lưới:

- mỗi minterm là một chuỗi bit;
- hai chuỗi gộp được khi chỉ khác đúng **một** vị trí — đúng $$xy + xy' = x$$.

Trên lớp ta làm tay ví dụ 3–4 biến để hiểu thuật toán. Với nhiều biến hơn, cùng quy trình được máy tính thực hiện.

![Bảng Quine–McCluskey](/discrete-mathematics-for-computer-science-iuh/img/course/quine_mccluskey.svg)

<p class="textbook-figure-caption" data-figure="13.21">Tabulation: nhóm theo số bit 1; mũi tên kết hợp tạo implicant rộng hơn.</p>

![K-map — đối chiếu](/discrete-mathematics-for-computer-science-iuh/img/course/karnaugh_map.svg)

<p class="textbook-figure-caption" data-figure="13.22">Cùng mục tiêu tối thiểu SOP (tổng các tích); K-map nhìn, QM đếm và đánh dấu.</p>

## 2. Pha 1 — Sinh implicant nguyên tố

Làm lần lượt các bước sau (ghi bảng trên giấy):

1. **Liệt kê** mọi minterm (và don't-care nếu có) dưới dạng nhị phân $$n$$ bit.
2. **Xếp nhóm** theo số lượng bit **1**.
3. **So cặp** chỉ giữa hai nhóm kề (lệch đúng một bit 1):
   - nếu hai mã khác đúng **một** vị trí → tạo mã mới, đặt `-` tại vị trí khác nhau;
   - mã mới đại diện **cả hai** minterm gốc.
4. **Lặp** trên các mã đã có `-`: gộp khi `-` cùng chỗ và phần bit còn lại khác đúng một vị trí.
5. **Đánh dấu** mọi mã đã từng tham gia một phép gộp.
6. Những mã **không bao giờ bị đánh dấu** = **implicant nguyên tố** (không còn mở rộng được).

**Cơ sở toán:** mỗi lần gộp là một lần áp dụng $$xy + xy' = x$$. Chuỗi gộp dài tương ứng nhóm $$2^k$$ ô trên K-map.

![Bảng chân trị / minterm](/discrete-mathematics-for-computer-science-iuh/img/course/truth_table_grid.svg)

<p class="textbook-figure-caption" data-figure="13.23">Điểm xuất phát luôn là tập minterm (các hàng $$F = 1$$) — giống SOP (tổng các tích) chuẩn ở 13.2.</p>

## 3. Pha 2 — Bảng phủ và implicant cốt yếu

Lập bảng:

- **hàng** = implicant nguyên tố;
- **cột** = minterm **bắt buộc** (không gồm don't-care);
- đánh dấu ô nếu implicant phủ minterm.

Một implicant gọi là **cốt yếu** khi tồn tại một cột chỉ có **đúng một** dấu: minterm đó buộc chọn implicant đó.

Các bước gọn:

1. Phát hiện mọi implicant cốt yếu.
2. Xóa các cột đã được chúng phủ.
3. Xóa các hàng không còn dấu.
4. Trên phần còn lại, chọn một hệ implicant với ít hạng / ít litera nhất phủ các cột còn lại.

Mục tiêu: mọi cột bắt buộc có ít nhất một dấu được chọn. Trên K-map, đây chính là bước 3–5 của quy trình tế bào lớn.

## 4. Don't-care trong QM

- **Pha 1:** đưa don't-care vào danh sách **như thể** chúng là minterm — giúp tạo implicant lớn hơn.
- **Pha 2:** **không** mở cột cho don't-care — không bắt buộc phủ chúng.

Như vậy **X** chỉ là “chất xúc tác” sinh hạng, không phải nghĩa vụ cover.

<div class="textbook-example" markdown="1">

**Ví dụ phác.** $$F(a, b, c) = \sum m(1, 2, 5) + d(0, 7)$$.  
Pha 1 gộp cả $$0$$ và $$7$$; pha 2 chỉ cột $$1, 2, 5$$.  
Một cover tối ưu thường gặp: $$F = a'c' + b'c$$ (đối chiếu bảng 8 dòng).

</div>

## 5. Ví dụ bốn biến (luyện quy trình)

Cho

$$
F(a, b, c, d) = \sum m(0, 2, 3, 5, 7, 8, 10, 11, 13, 15).
$$

Sau khi nhóm theo số bit 1 và gộp cặp, các implicant nguyên tố điển hình gồm các dạng như $$cd$$, $$bd$$, $$b'd'$$. Trên bảng phủ, $$b'd'$$ thường cốt yếu vì phủ cụm $$0, 2, 8, 10$$; sau đó chọn thêm $$cd$$ (hoặc $$bd$$) để phủ nốt. Một kết quả tối tiểu:

$$
F = cd + b'd'.
$$

Đừng học thuộc đáp án số: hãy tập **đánh dấu đã gộp** và **cột một dấu** — hai thói quen đó chuyển được sang mọi đề.

## 6. So với K-map và khi nào cần máy tính

| Công cụ | Ưu điểm | Khi nào dùng |
|:---|:---|:---|
| **K-map** | Nhanh, trực quan | 2–4 biến trên lớp / bài tập tay |
| **Quine–McCluskey** | Hệ thống, kiểm từng bước, lập trình được | Hiểu thuật toán; $$n$$ vừa phải |
| **Phần mềm hỗ trợ** | Xử lý nhiều biến hơn làm tay | Bài toán lớn; không cần nhớ tên tool trên lớp |

Thông điệp chính: máy cũng chỉ **gộp minterm kề** rồi **chọn phủ** — cùng việc mắt làm trên K-map, chỉ khác quy mô.

<div class="interactive-demo" markdown="1">
Mô phỏng từng bước QM (nếu widget có trên site).
<div data-demo="quine-mccluskey-simplifier"></div>
</div>
<script src="{{ '/public/js/quine-mccluskey-simplifier.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Chạy QM (tay) cho $$F(a, b, c, d) = \sum m(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)$$ và nêu implicant cốt yếu bạn chọn.

<details>
<summary>Đáp án</summary>

Tham khảo mục 5: cover $$cd + b'd'$$ (hoặc tương đương tối ưu). $$b'd'$$ cốt yếu cho cụm chẵn thấp.

</details>

### Bài tập 2

$$F(a, b, c) = \sum m(1, 2, 5) + d(0, 7)$$. Hoàn tất pha 1–2.

<details>
<summary>Đáp án</summary>

$$F = a'c' + b'c$$ là một cover tối ưu thường gặp.

</details>

### Bài tập 3

$$F(x, y, z) = \sum m(0, 1, 4, 5, 6)$$. Làm bằng K-map và bằng QM; so sánh SOP (tổng các tích).

<details>
<summary>Đáp án</summary>

Cả hai phải ra cùng hàm (có thể khác cách viết hạng nhưng tương đương), ví dụ $$F = x'z' + xy' + yz'$$ — kiểm bằng bảng 8 dòng.

</details>

## Xem thêm

- Ôn K-map (13.4) trên cùng một hàm bốn biến rồi đối chiếu QM.
- Bài 13.6 — bối cảnh ứng dụng rộng hơn (khi muốn đọc thêm).

## Tóm tắt

1. Quine–McCluskey tách tối thiểu hóa thành hai pha: sinh implicant nguyên tố, rồi chọn phủ.
2. Gộp khi hai mã khác đúng một bit; mã không bị đánh dấu là implicant nguyên tố.
3. Implicant cốt yếu = cột chỉ có một dấu trên bảng phủ.
4. Don't-care chỉ vào pha 1.
5. QM là phiên bản “bảng” của K-map — cùng tư duy, khác quy mô.
