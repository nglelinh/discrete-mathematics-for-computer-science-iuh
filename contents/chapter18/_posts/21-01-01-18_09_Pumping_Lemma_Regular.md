---
layout: post
title: "Bổ đề Bơm cho Ngôn ngữ Chính quy"
categories: chapter18
date: 2021-01-01
order: 9
required: true
lang: en
excerpt: "Phát biểu và chứng minh bổ đề bơm từ DFA, ứng dụng chứng minh {0ⁿ1ⁿ} không chính quy và quy trình phản chứng."
---

> **Câu chuyện mở đầu:** Nếu DFA chỉ có đúng $$p$$ trạng thái (bộ nhớ hữu hạn!) mà bạn cho nó đọc một chuỗi dài từ $$p$$ ký tự trở lên, chuyện gì chắc chắn phải xảy ra? Theo **Nguyên lý Chuồng bồ câu**, máy **bắt buộc phải ghé lại ít nhất một trạng thái hai lần** — tạo thành một **vòng lặp**! Và hễ đã có vòng lặp, bạn có thể chạy qua vòng đó **0 lần, 2 lần, hay 100 lần** mà máy vẫn chấp nhận! Đó chính là **Bổ đề Bơm (Pumping Lemma)** — con dao sắc bén nhất để chứng minh một ngôn ngữ **KHÔNG phải ngôn ngữ chính quy**!

<div class="textbook-epigraph" markdown="1">

"If it is regular, long enough strings pump — use that to kill candidates."

<span class="epigraph-attribution">— Pumping lemma</span>

</div>

## Mục tiêu

![Bổ đề Bơm cho Ngôn ngữ Chính quy (Chu trình trên DFA)](/discrete-mathematics-for-computer-science-iuh/img/course/pumping_lemma_regular.svg)

<div class="textbook-objectives" markdown="1">

- **Phát biểu** và **chứng minh** bổ đề bơm (*pumping lemma*) cho ngôn ngữ chính quy.
- **Chứng minh** ngôn ngữ $$\{0^n1^n\}$$ không chính quy.
- **Áp dụng** quy trình phản chứng chuẩn để bác bỏ tính chính quy của một ngôn ngữ.

</div>

## Kiến thức cần nhớ: Bổ đề Bơm & Giới hạn của Bộ nhớ Hữu hạn

### 1. Bản chất Hình học của Bổ đề Bơm (Nguyên lý Chuồng bồ câu)
- **Phát biểu:** Nếu $$L$$ chính quy, tồn tại hằng số bơm $$p \ge 1$$ (chính là số trạng thái của một DFA nhận $$L$$!) sao cho mọi chuỗi $$s \in L$$ dài $$\lvert s\rvert \ge p$$ đều tách được thành $$s = xyz$$ thỏa đủ 3 điều kiện:
  1. $$\lvert xy\rvert \le p$$ (vòng lặp đầu tiên phải xuất hiện ngay trong $$p$$ ký tự đầu!).
  2. $$\lvert y\rvert \ge 1$$ (vòng lặp không rỗng!).
  3. $$x y^i z \in L$$ với **mọi** $$i \ge 0$$ (bơm lên $$i=2,3,\dots$$ hoặc rút xuống $$i=0$$ đều vẫn thuộc $$L$$!).

### 2. Cấu trúc Logic "Trò chơi Đối kháng" (Phản chứng!)
- **Cảnh báo sinh viên hay sai nhất:** Bổ đề Bơm là **điều kiện CẦN, KHÔNG phải điều kiện ĐỦ** (chỉ dùng để chứng minh **KHÔNG** chính quy, không bao giờ dùng để chứng minh *có* chính quy!).
- Trong chứng minh phản chứng, **đối thủ** chọn $$p$$ và cách tách $$xyz$$; **bạn** được quyền chọn chuỗi $$s \in L$$ (theo $$p$$) và chọn số lần bơm $$i$$ để đánh bại **mọi** cách tách hợp lệ của đối thủ!

## Ví dụ tính tay làm từng bước: Chứng minh trọn vẹn $$L = \{0^n 1^n : n \ge 0\}$$ KHÔNG chính quy

Giả sử phản chứng $$L$$ là ngôn ngữ chính quy, gọi $$p \ge 1$$ là hằng số bơm của Bổ đề Bơm:
1. **Bạn chọn chuỗi thử:** Lấy **$$s = 0^p 1^p$$**. Kiểm tra: $$s \in L$$ và $$\lvert s\rvert = 2p \ge p$$. ✓
2. **Đối thủ tách $$s = xyz$$** thỏa $$\lvert xy\rvert \le p$$ và $$\lvert y\rvert \ge 1$$:
   - Vì $$p$$ ký tự đầu tiên của $$s = 0^p 1^p$$ **toàn là số `0`**, điều kiện $$\lvert xy\rvert \le p$$ ép cả $$x$$ lẫn $$y$$ chỉ gồm toàn số `0`!
   - Do $$\lvert y\rvert \ge 1$$, ta viết $$y = 0^k$$ với **$$k \ge 1$$**.
3. **Bạn chọn số lần bơm $$i = 2$$** (bơm thêm 1 vòng lặp):
   $$
   x y^2 z = 0^{p + k} 1^p.
   $$
4. **Mâu thuẫn:** Vì $$k \ge 1$$ nên $$p + k > p \implies 0^{p+k} 1^p \notin L$$! Trái với Bổ đề Bơm $$\implies$$ **$$L = \{0^n 1^n\}$$ KHÔNG phải ngôn ngữ chính quy**! (Hệ quả thực tế: không thể dùng Regex thuần để kiểm tra dấu ngoặc lồng nhau tùy ý `((()))` hay cú pháp HTML!)

### Giải thích: 4 bước áp dụng Bổ đề Bơm chuẩn không bị đối thủ "lách luật"
#### Bước 1: Không bao giờ chọn hằng số $$p$$ cụ thể!
$$p$$ là ẩn số bất kỳ do đối thủ đưa ra — chuỗi $$s$$ bạn chọn phải được viết **theo biến $$p$$** (như $$0^p 1^p$$, $$a^p b^{p+1}$$, $$0^{p^2}$$).

#### Bước 2: Lợi dụng tối đa điều kiện $$\lvert xy\rvert \le p$$ để "khóa chặt" nội dung của $$y$$
Hãy thiết kế $$p$$ ký tự đầu của $$s$$ thật đồng nhất (ví dụ toàn `0`) để bất chấp đối thủ tách thế nào, $$y$$ cũng chỉ có đúng một loại ký tự!

#### Bước 3: Thử cả bơm lên ($$i = 2$$) lẫn bơm xuống ($$i = 0$$)
Đôi khi $$i = 2$$ vẫn nằm trong $$L$$ (ví dụ $$L = \{0^m 1^n : m < n\}$$ nếu chọn $$s = 0^p 1^{p+1}$$ thì bơm lên $$i=2$$ ra $$0^{p+k}1^{p+1} \notin L$$ ngay, còn với $$m > n$$ chọn $$s = 0^{p+1}1^p$$ thì bơm xuống $$i = 0$$ ra $$0^{p+1-k}1^p \notin L$$!).

#### Bước 4: Kết hợp với Tính đóng (bài 18.10) để tiết kiệm nửa trang giấy!
Nếu ngôn ngữ có cấu trúc phức tạp (như "số `0` bằng số `1`"), hãy giao với $$0^*1^*$$ trước để rút về $$0^n 1^n$$ rồi mới dùng Bổ đề Bơm!

$$
\text{Giả sử }L\text{ chính quy}
\;\xrightarrow{\;\text{Chọn }s(p) \in L\;}\;
\lvert xy\rvert \le p \;(\text{khóa }y)
\;\xrightarrow{\;\text{Bơm }i = 0 \text{ hoặc } 2\;}\;
xy^i z \notin L \;(\text{Mâu thuẫn!}).
$$

## Phát biểu và chứng minh

<div class="textbook-theorem" markdown="1">

**Bổ đề bơm (cho ngôn ngữ chính quy).** Nếu $$L$$ là ngôn ngữ chính quy thì tồn tại hằng số bơm $$p\ge 1$$ sao cho mọi chuỗi $$w\in L$$ có độ dài $$\lvert w\rvert\ge p$$ đều phân tích được thành $$w=xyz$$ thỏa mãn đồng thời ba điều kiện:  
(1) $$xy^kz\in L$$ với mọi $$k\ge 0$$;  
(2) $$\lvert y\rvert\ge 1$$;  
(3) $$\lvert xy\rvert\le p$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử $$L$$ được chấp nhận bởi một DFA có $$p=\lvert Q\rvert$$ trạng thái. Xét chuỗi $$w=a_1\ldots a_n \in L$$ với $$n\ge p$$. Dãy $$p+1$$ trạng thái đầu tiên khi đọc tiền tố độ dài $$p$$ chắc chắn có ít nhất một trạng thái lặp lại theo nguyên lý Dirichlet: $$q_i=q_j$$ với $$0\le i<j\le p$$. Đặt $$x$$ là phần chuỗi đến $$q_i$$, $$y$$ là phần từ $$q_i$$ đến $$q_j$$ (tạo thành một vòng lặp khác rỗng) và $$z$$ là phần còn lại. Việc lặp vòng $$y$$ với số lần $$k \ge 0$$ bất kỳ đều giữ nguyên trạng thái kết thúc, nên $$xy^kz \in L$$.

</div>

### Thử nghiệm: trò chơi bổ đề bơm (ngôn ngữ chính quy)

Chọn hằng số $$p$$ và duyệt mọi cách phân tích $$w = xyz$$; nếu với mọi cách chia hợp lệ đều tồn tại giá trị $$k$$ phá vỡ điều kiện thuộc $$L$$ thì $$L$$ không chính quy:

<div class="interactive-demo" markdown="1">
<div data-demo="pumping-explainer" data-kind="regular" data-lang="anbn"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Ứng dụng

<div class="textbook-theorem" markdown="1">

**Định lý.** Ngôn ngữ $$L=\{0^n1^n:n\ge 0\}$$ không phải là ngôn ngữ chính quy.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Giả sử phản chứng rằng $$L$$ chính quy với hằng số bơm $$p$$. Chọn chuỗi $$w=0^p1^p \in L$$ (có $$\lvert w\rvert = 2p \ge p$$). Với mọi phân tích $$w=xyz$$ thỏa mãn $$\lvert xy\rvert\le p$$ và $$\lvert y\rvert\ge 1$$, phần $$y$$ chỉ chứa ký tự $$0$$, tức $$y=0^{t}$$ với $$t\ge 1$$. Khi chọn $$k=2$$, ta được $$xy^2z = 0^{p+t}1^p\notin L$$ — mâu thuẫn. Vậy $$L$$ không chính quy.

</div>

## Quy trình phản chứng chuẩn

1. Giả sử $$L$$ chính quy và tồn tại hằng số bơm $$p$$.
2. Chọn một chuỗi $$w \in L$$ phụ thuộc vào $$p$$ sao cho $$\lvert w\rvert \ge p$$.
3. Xét **mọi** phân tích $$w=xyz$$ thỏa mãn $$\lvert xy\rvert \le p$$ và $$\lvert y\rvert \ge 1$$.
4. Chỉ ra ít nhất một giá trị $$k \ge 0$$ khiến $$xy^kz \notin L$$ để rút ra mâu thuẫn.

## Bài tập

1. Chứng minh ngôn ngữ $$\{ww\}$$ không chính quy.
2. Xét ngôn ngữ $$\{0^{n!}\}$$ — hãy thử áp dụng bổ đề bơm và so sánh với cách dùng định lý Myhill–Nerode.
3. Thảo luận vì sao bổ đề bơm chỉ là điều kiện **cần** chứ không phải điều kiện đủ để một ngôn ngữ là chính quy (tham khảo Sipser).

## Tài liệu đọc thêm

Sipser §1.4; Hopcroft–Ullman.

## Tóm tắt

Bổ đề bơm xuất phát từ sự tồn tại của chu trình trạng thái trong DFA và cung cấp khuôn mẫu phản chứng chuẩn để bác bỏ tính chính quy của ngôn ngữ.

**Bài tiếp theo:** Tính đóng của ngôn ngữ chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=dikEDuepOtI">Pumping Lemma (For Regular Languages)</a> — Neso Academy, tiếng Anh. Giới thiệu bổ đề bơm cho ngôn ngữ chính quy.
- <a href="https://www.youtube.com/watch?v=Ty9tpikilAo">Pumping Lemma (For Regular Languages) | Example 1</a> — Neso Academy, tiếng Anh. Ví dụ chứng minh một ngôn ngữ không chính quy bằng bổ đề bơm.
- <a href="https://www.youtube.com/watch?v=kZzH8E-s-9o">Pumping Lemma (For Regular Languages) | Example 2</a> — Neso Academy, tiếng Anh. Ví dụ thứ hai giúp luyện cách chọn chuỗi và xét mọi phân tích $$xyz$$.
