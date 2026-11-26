---
layout: post
title: "Biểu thức Chính quy"
categories: chapter18
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Định nghĩa đệ quy biểu thức chính quy (regex), ngôn ngữ L(r) sinh bởi ba toán tử cơ bản và các ví dụ minh họa."
---

> **Câu chuyện mở đầu:** Mỗi khi bạn kiểm tra định dạng email hợp lệ trên biểu mẫu web, tìm kiếm toàn bộ tệp `*.py` trong thư mục, hay dùng `grep` lọc log máy chủ hàng gigabyte, bạn đang gõ chính **Biểu thức Chính quy (Regular Expression — Regex)** do nhà toán học Stephen Kleene phát minh từ năm 1951! Chỉ bằng đúng **3 phép toán đại số** — Hợp (`+`), Nối tiếp (`·`), và Lặp vô hạn (`*` — Sao Kleene) — Regex mô tả trọn vẹn toàn bộ thế giới ngôn ngữ chính quy!

<div class="textbook-epigraph" markdown="1">

"Regular expressions are the algebra of finite automata."

<span class="epigraph-attribution">— Kleene</span>

</div>

## Mục tiêu

![Chuyển đổi Biểu thức Chính quy sang ε-NFA (Thompson)](/discrete-mathematics-for-computer-science-iuh/img/course/regex_to_nfa_flow.svg)

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** biểu thức chính quy (*regular expression*) và ngôn ngữ tương ứng $$L(r)$$.
- **Chuyển đổi** qua lại giữa mô tả ngôn ngữ tự nhiên và biểu thức chính quy đơn giản.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Biểu thức chính quy trên bảng chữ cái $$\Sigma$$ được xây dựng đệ quy từ:

- **Các biểu thức cơ sở:** $$\emptyset$$, $$\varepsilon$$ và từng ký hiệu $$a\in\Sigma$$.
- **Ba toán tử:** $$r+s$$ (hợp), $$rs$$ (nối chuỗi) và $$r^*$$ (bao đóng Kleene / lặp không hoặc nhiều lần).

Ngôn ngữ $$L(r)$$ biểu diễn bởi biểu thức $$r$$ được xác định tương ứng:

$$L(\emptyset)=\emptyset,\quad L(\varepsilon)=\{\varepsilon\},\quad L(a)=\{a\}.$$

$$L(r+s)=L(r)\cup L(s),\quad L(rs)=L(r)L(s),\quad L(r^*)=\bigcup_{k\ge 0}L(r)^k.$$

</div>

## Kiến thức cần nhớ: Đại số Biểu thức Chính quy (Regex)

### 1. Định nghĩa Quy nạp với 3 Phép toán Cơ bản
- **Nguyên tử cơ sở:** $$\emptyset$$ (ngôn ngữ rỗng — không chứa chuỗi nào), $$\varepsilon$$ (chứa đúng chuỗi rỗng), và từng ký tự $$a \in \Sigma$$.
- **Ba phép ghép:** Hợp $$R_1 + R_2$$ (chọn 1 trong 2), Nối tiếp $$R_1 R_2$$ (nối đuôi nhau), và **Sao Kleene $$R^*$$** (lặp $$0, 1, 2, \dots$$ lần!).
- **Thứ tự ưu tiên chuẩn:** Ngoặc `()` $$>$$ Sao `*` $$>$$ Nối tiếp $$>$$ Hợp `+`.

### 2. Phân biệt hai "Con số 0 và 1" hay bị nhầm nhất: $$\emptyset$$ vs. $$\varepsilon$$
- $$\emptyset$$ là tập rỗng ($$\{\}$$): $$R \cdot \emptyset = \emptyset$$, nhưng **$$\emptyset^* = \{\varepsilon\}$$** (lặp 0 lần luôn cho chuỗi rỗng $$\varepsilon$$!).
- $$\varepsilon$$ là tập $$\{\varepsilon\}$$: $$R \cdot \varepsilon = R$$ (phần tử đơn vị của phép nối tiếp!).

### 3. Mối quan hệ với Ô-tô-mát
- **Bản chất:** Biểu thức chính quy là **cách mô tả khai báo (declarative)** cho con người đọc và viết, còn DFA/NFA là **cỗ máy thực thi (operational)** cho máy tính chạy — và Định lý Kleene ở bài sau chứng minh cả hai có sức mạnh **tương đương 100%**!

## Ví dụ tính tay làm từng bước: Giải mã & Kiểm thử 2 Biểu thức Chính quy kinh điển

1. **Ngôn ngữ $$L_1$$: Chuỗi nhị phân chứa ít nhất một cụm `00`:**
   $$
   R_1 = (0 + 1)^*\,00\,(0 + 1)^*.
   $$
   - Kiểm tra `1001`: tách thành `1` $$\in (0+1)^*$$ + `00` + `1` $$\in (0+1)^*$$ $$\implies$$ khớp! ✓
   - Kiểm tra `10101`: không có hai số `0` đứng cạnh nhau $$\implies$$ không khớp! ✓

2. **Ngôn ngữ $$L_2$$: Chuỗi nhị phân KHÔNG chứa hai số `0` liên tiếp:**
   Ý tưởng thiết kế bằng tay: cứ mỗi khi xuất hiện một số `0` (trừ trường hợp nằm ở tận cùng cuối chuỗi), ngay sau nó **bắt buộc** phải có ít nhất một số `1` — nên mọi khối bên trong chỉ có thể là `1` hoặc `01`, cộng thêm tùy chọn kết thúc bằng một số `0` lẻ loi ở cuối:
   $$
   R_2 = (1 + 01)^*\,(0 + \varepsilon).
   $$
   - Kiểm tra `011010`: tách thành `(01)(1)(01) + (0)` $$\implies$$ khớp! ✓
   - Kiểm tra `1001`: sau `0` đầu tiên không phải `1` mà lại là `0` $$\implies$$ không thể tách được! ✓

### Giải thích: 4 mẹo viết Biểu thức Chính quy gọn và không sót biên
#### Bước 1: Dùng $$(0 + 1)^*$$ làm "ký tự đại diện tùy ý"
Gặp yêu cầu "bắt đầu bằng...", "kết thúc bằng...", "chứa..." hãy dùng $$(0+1)^*$$ bọc vào các vị trí tự do.

#### Bước 2: Dùng kỹ thuật "Gắn khóa sau ký tự cấm" cho bài toán KHÔNG chứa chuỗi con
Như ví dụ `không chứa 00`: gom mỗi `0` đi kèm ngay với `1` thành khối `(01)`, rồi xử lý riêng trường hợp `0` đứng cuối chuỗi bằng `(0 + ε)`!

#### Bước 3: Luôn thử chuỗi rỗng $$\varepsilon$$ và chuỗi 1 ký tự
Kiểm tra xem $$\varepsilon$$ có nên nằm trong ngôn ngữ không (ví dụ: dùng $$R^*$$ cho $$\ge 0$$ lần, còn $$R^+ = RR^*$$ cho $$\ge 1$$ lần!).

#### Bước 4: Rút gọn bằng các đẳng thức Đại số Regex
Ghi nhớ các luật bỏ túi: $$(R^*)^* = R^*$$, $$\varepsilon + R R^* = R^*$$, $$(a^* b^*)^* = (a + b)^*$$!

$$
\text{Mô tả ngôn ngữ}
\;\xrightarrow{\;\text{Hợp }(+),\text{ Nối},\text{ Sao }(*)\;}\;
\text{Biểu thức chính quy }R
\;\xrightarrow{\;\text{Định lý Kleene}\;}\;
\varepsilon\text{-NFA} \to \text{DFA}.
$$

## Ví dụ

Một số biểu thức chính quy quen thuộc trên $$\{0,1\}$$: $$(0+1)^*$$ (mọi chuỗi nhị phân), $$0^*1^*$$ (chuỗi gồm các số 0 đứng trước các số 1), $$(0+1)^*01$$ (chuỗi kết thúc bằng `01`) và $$(01)^*$$ (chuỗi lặp lại cặp `01`).

### Thử nghiệm: dựng ε-NFA Thompson

Ghép từng khối cơ bản cho ký tự, nối tiếp, hợp và lặp sao, sau đó chạy thử chuỗi đầu vào trên NFA vừa dựng:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="thompson"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Viết biểu thức chính quy cho ngôn ngữ các chuỗi trên $$\{0,1\}$$ có số bit 0 chẵn (gợi ý: bài này phức tạp hơn thoạt nhìn, nên dựng DFA trước).
2. Chứng minh đồng nhất thức $$L(r^*)=L(\varepsilon+rr^*)$$.
3. Phân biệt biểu thức chính quy lý thuyết với biểu thức chính quy thực tế như PCRE (có hỗ trợ tham chiếu ngược *backreference*).

## Tài liệu đọc thêm

Sipser §1.3.

## Tóm tắt

Biểu thức chính quy tạo nên một đại số gọn gàng cho ngôn ngữ chính quy với ba phép toán hợp, nối và bao đóng sao.

**Bài tiếp theo:** Định lý Kleene.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Giới thiệu cú pháp và ý nghĩa của biểu thức chính quy trong lý thuyết ô-tô-mát.
- <a href="https://www.youtube.com/watch?v=paOPoZyjzdg">Regular Expression - Examples</a> — Neso Academy, tiếng Anh. Các ví dụ đọc ngôn ngữ tương ứng của một biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=RxfXyvfTsgQ">Conversion of Regular Expression to Finite Automata</a> — Neso Academy, tiếng Anh. Chuyển đổi từ biểu thức chính quy sang ô-tô-mát hữu hạn.
