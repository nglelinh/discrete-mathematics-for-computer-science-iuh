---
layout: post
title: "Định lý Kleene"
categories: chapter18
date: 2021-01-01
order: 8
required: true
lang: en
excerpt: "Sự tương đương giữa biểu thức chính quy, ε-NFA, NFA và DFA; phép dựng Thompson và phương pháp loại bỏ trạng thái."
---

> **Câu chuyện mở đầu:** Bên tay trái ta có **DFA/NFA** — những cỗ máy trạng thái cơ khí chạy bằng sơ đồ mũi tên. Bên tay phải ta có **Biểu thức Chính quy** — những công thức đại số thuần túy chỉ dùng `+`, `·`, `*`. Năm 1956, Stephen Kleene chứng minh một định lý hợp nhất kinh điển: **hai thế giới tưởng chừng khác hẳn nhau đó định nghĩa CHÍNH XÁC CÙNG MỘT LỚP NGÔN NGỮ**! Và hai thuật toán chuyển đổi hai chiều — **Thompson** (Regex $$\to \varepsilon$$-NFA) và **Khử trạng thái** (DFA $$\to$$ Regex) — chính là trái tim của mọi bộ máy Regex hiện đại!

<div class="textbook-epigraph" markdown="1">

"Three notations, one class: regular languages."

<span class="epigraph-attribution">— Kleene’s theorem</span>

</div>

![Kleene](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_kleene_triangle.svg)

<p class="textbook-figure-caption" data-figure="18.5">Ba biểu diễn tương đương nhau của lớp ngôn ngữ chính quy.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** định lý Kleene.
- **Mô tả** phép dựng Thompson và phương pháp loại bỏ trạng thái (*state elimination*).
- **Trình bày** khung chứng minh tương đương theo hai chiều.

</div>

## Bản đồ kiến thức nền: Định lý Kleene và Hai Chiều Chuyển đổi

### 1. Chiều thuận — Thuật toán Thompson (Regex $$\to \varepsilon$$-NFA)
- **Bản chất:** Xây dựng quy nạp từ dưới lên theo cây cú pháp của Regex! Mỗi khối con đều có **đúng 1 trạng thái vào** và **đúng 1 trạng thái ra** (không có cung đi ngược vào đầu vào hay đi ra từ đầu ra). Nhờ cấu trúc sạch sẽ đó, mỗi phép `+`, `·`, `*` chỉ cần thêm tối đa **2 trạng thái và 4 cung $$\varepsilon$$** — tổng số trạng thái tuyến tính $$O(\lvert R\rvert)$$!

### 2. Chiều ngược — Phương pháp Khử Trạng thái (DFA $$\to$$ GNFA $$\to$$ Regex)
- **Bản chất:** Biến DFA thành **GNFA** (mỗi cạnh có thể gắn nhãn cả một **Regex**!) có đúng 1 trạng thái bắt đầu mới $$q_{\text{start}}$$ và 1 trạng thái kết thúc mới $$q_{\text{accept}}$$. Lần lượt "xóa" từng trạng thái trung gian $$k$$ bằng cách cập nhật mọi đường đi $$i \to k \to j$$ thành đường tắt:
  $$
  R_{ij}^{\text{mới}} = R_{ij} + R_{ik}\,(R_{kk})^*\,R_{kj}!
  $$
  Khi xóa sạch mọi trạng thái giữa, nhãn duy nhất còn lại trên mũi tên $$q_{\text{start}} \to q_{\text{accept}}$$ chính là Regex cần tìm!

## Ví dụ tính tay cầm tay chỉ việc: Áp dụng Công thức Khử trạng thái cho DFA 2 trạng thái "Số bit `1` chẵn"

Xét DFA 2 trạng thái $$q_0$$ (bắt đầu & kết thúc) và $$q_1$$: tự vòng `0` ở cả hai, và hai mũi tên `1` nối qua lại $$q_0 \leftrightarrow q_1$$.
1. Thêm $$q_{\text{start}} \xrightarrow{\varepsilon} q_0$$ và $$q_0 \xrightarrow{\varepsilon} q_{\text{accept}}$$.
2. **Khử trạng thái $$q_1$$:** Đường đi qua $$q_1$$ duy nhất là $$q_0 \xrightarrow{1} q_1 \xrightarrow{0^*} q_1 \xrightarrow{1} q_0$$!
   Cập nhật tự vòng trên $$q_0$$:
   $$
   R_{00}^{\text{mới}} = 0 + 1\,0^*\,1!
   $$
3. **Khử nốt trạng thái $$q_0$$:** Đường từ $$q_{\text{start}}$$ qua $$q_0$$ tới $$q_{\text{accept}}$$ có nhãn:
   $$
   R = \varepsilon\,(0 + 10^*1)^*\,\varepsilon = (0 + 10^*1)^*!
   $$
   Kiểm tra bằng mắt: lặp tùy ý giữa từng số `0` đơn lẻ hoặc từng **cặp số `1`** kẹp giữa bởi bao nhiêu `0` cũng được — chuẩn xác 100% ngôn ngữ "chẵn bit `1`"! ✓

### Khung giải thích: Vòng tròn khép kín 4 đỉnh của Ngôn ngữ Chính quy (nên đọc chậm)

#### Bước 1: Regex $$\xrightarrow{\text{Thompson}}$$ $$\varepsilon$$-NFA
Lắp ráp như xếp Lego từ các lá (ký tự đơn) lên gốc cây biểu thức.

#### Bước 2: $$\varepsilon$$-NFA $$\xrightarrow{\text{ECLOSE + Subset Construction}}$$ DFA
Loại bỏ hoàn toàn cung $$\varepsilon$$ và tính không tất định để chạy trong $$O(\lvert w\rvert)$$.

#### Bước 3: DFA $$\xrightarrow{\text{State Elimination}}$$ Regex
Gom mọi trạng thái trung gian qua công thức đường tắt $$R_{ij} + R_{ik} R_{kk}^* R_{kj}$$ (lưu ý: chọn thứ tự khử các trạng thái ít mũi tên trước sẽ cho Regex gọn hơn rất nhiều!).

#### Bước 4: Tận dụng sự tương đương trong chứng minh lý thuyết
Từ đây, muốn chứng minh ngôn ngữ $$L$$ là chính quy, bạn được tự do chọn **bất kỳ** công cụ nào tiện tay nhất: viết Regex, vẽ NFA, hay vẽ DFA!

$$
\text{Regex}
\;\xrightarrow{\;\text{Thompson}\;}\;
\varepsilon\text{-NFA}
\;\xrightarrow{\;\text{Subset}\;}\;
\text{DFA}
\;\xrightarrow{\;\text{State Elimination}\;}\;
\text{Regex}.
$$

## Định lý Kleene

<div class="textbook-theorem" markdown="1">

**Định lý (Kleene).** Ba lớp ngôn ngữ sau trùng nhau hoàn toàn:  
(1) các ngôn ngữ $$L(r)$$ biểu diễn bởi biểu thức chính quy $$r$$;  
(2) các ngôn ngữ $$L(N)$$ chấp nhận bởi ε-NFA hoặc NFA;  
(3) các ngôn ngữ $$L(M)$$ chấp nhận bởi DFA.

</div>

## Chiều biểu thức chính quy → ε-NFA (Thompson)

Phép dựng Thompson thực hiện theo quy nạp cấu trúc của biểu thức $$r$$: xây dựng các mẫu ε-NFA cơ sở cho $$\emptyset, \varepsilon, a$$, sau đó ghép nối chúng cho các phép toán hợp, nối và sao bằng các cạnh chuyển ε. Số trạng thái sinh ra thuộc $$O(\lvert r\rvert)$$.

**Tính đúng đắn:** chứng minh bằng quy nạp cấu trúc rằng $$L(N_r)=L(r)$$.

### Thử nghiệm: Thompson từng khối

Quan sát quá trình dựng ε-NFA theo từng khối từ biểu thức chính quy:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="thompson"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Chiều NFA → DFA

Thực hiện bằng phép xây dựng tập con (*subset construction*) đã trình bày ở Bài 18.5.

## Chiều DFA → biểu thức chính quy

Ta sử dụng phương pháp loại bỏ trạng thái (*state elimination*) hoặc giải hệ phương trình ngôn ngữ bằng bổ đề Arden: phương trình $$X=A X+B$$ có nghiệm $$X=A^*B$$ (khi $$\varepsilon\notin L(A)$$, hoặc cần xử lý cẩn thận trường hợp chứa $$\varepsilon$$).

### Thử nghiệm: loại trạng thái để thu biểu thức chính quy

Thêm trạng thái đầu $$S$$ và trạng thái cuối $$F$$ mới rồi loại dần từng trạng thái trung gian; bạn có thể thử hai thứ tự loại khác nhau để thấy biểu thức chính quy thu được khác dạng nhưng vẫn tương đương về ngôn ngữ:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="eliminate" data-preset="dfa01"></div>
</div>

## Bài tập

1. Áp dụng phép dựng Thompson cho biểu thức $$(0+1)^*01$$.
2. Chọn một DFA gồm 2 trạng thái và chuyển sang biểu thức chính quy bằng phương pháp loại bỏ trạng thái.
3. Đọc và đối chiếu phát biểu chính thức của bổ đề Arden.

## Tài liệu đọc thêm

Sipser; Kozen; Hopcroft–Ullman.

## Tóm tắt

Định lý Kleene khép kín vòng tròn tương đương giữa biểu thức chính quy, NFA và DFA thông qua phép dựng Thompson, xây dựng tập con và loại bỏ trạng thái.

**Bài tiếp theo:** Bổ đề bơm (*pumping lemma*) cho ngôn ngữ chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=OKFrju0HB7k">NFA to Regular Expression Conversion</a> — Neso Academy, tiếng Anh. Minh họa một chiều của định lý Kleene: chuyển NFA sang biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=SmT1DXLl3f4">DFA to Regular Expression Conversion</a> — Neso Academy, tiếng Anh. Chuyển đổi từ DFA sang biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=RxfXyvfTsgQ">Conversion of Regular Expression to Finite Automata</a> — Neso Academy, tiếng Anh. Chiều ngược lại: chuyển biểu thức chính quy sang ô-tô-mát hữu hạn.
