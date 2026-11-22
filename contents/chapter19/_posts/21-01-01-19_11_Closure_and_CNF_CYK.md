---
layout: post
title: "Đóng CFL, CNF và CYK"
categories: chapter19
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Tính đóng của CFL dưới hợp, nối, sao; tính không đóng dưới giao và bù; dạng chuẩn Chomsky (CNF) và thuật toán quy hoạch động CYK."
---

<div class="textbook-epigraph" markdown="1">

"CFLs are closed under union, not under intersection."

<span class="epigraph-attribution">— Classic contrast with regular</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** lớp CFL đóng dưới phép hợp ($$\cup$$), nối chuỗi và bao đóng sao ($$*$$).
- **Chứng minh** lớp CFL không đóng dưới phép giao ($$\cap$$) bằng ngôn ngữ $$\{a^nb^nc^n\}$$.
- **Mô tả** dạng chuẩn Chomsky (CNF) và thuật toán CYK có độ phức tạp $$O(n^3)$$.

</div>

## Tính đóng của CFL

Lớp CFL đóng dưới các phép toán **hợp, nối và sao** (chứng minh trực tiếp bằng cách thêm ký hiệu khởi đầu mới kết nối các văn phạm thành phần), đồng thời cũng đóng dưới phép đồng cấu (*homomorphism*) và đảo chuỗi (*reverse*).

<div class="textbook-theorem" markdown="1">

**Định lý.** Lớp ngôn ngữ phi ngữ cảnh **không** đóng dưới phép giao ($$\cap$$) và phép lấy bù.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Hai ngôn ngữ $$L_1=\{a^nb^nc^m : n,m \ge 0\}$$ và $$L_2=\{a^nb^mc^m : n,m \ge 0\}$$ đều là CFL, nhưng giao của chúng là $$L_1\cap L_2=\{a^nb^nc^n : n \ge 0\}$$ không phải là CFL.  
Suy ra CFL cũng không đóng dưới phép lấy bù: nếu CFL đóng dưới cả phép bù và phép hợp thì theo định luật De Morgan, nó sẽ phải đóng dưới phép giao — mâu thuẫn.

</div>

## Dạng chuẩn Chomsky (CNF)

Một CFG ở dạng chuẩn Chomsky khi mọi luật sinh đều có một trong hai dạng $$A\to BC$$ hoặc $$A\to a$$ (với ngoại lệ $$S\to\varepsilon$$ nếu ngôn ngữ chứa chuỗi rỗng; quy trình chuyển đổi chuẩn xem trong Sipser).

## Thuật toán CYK

Với văn phạm ở dạng chuẩn CNF, thuật toán CYK dùng quy hoạch động tính bảng $$X_{i,j}$$ chứa tất cả các ký hiệu không kết thúc có thể sinh ra chuỗi con $$w_{i..i+j-1}$$. Độ phức tạp thời gian của thuật toán là $$O(n^3\lvert P\rvert)$$.

<div class="textbook-theorem" markdown="1">

**Định lý.** Thuật toán CYK quyết định đúng bài toán thành viên cho văn phạm CNF: $$S\in X_{1,n}\Leftrightarrow w\in L(G)$$.

</div>

**Ý tưởng chứng minh:** quy nạp theo độ dài $$j$$ của chuỗi con. $$\square$$

### Minh họa CYK: điền bảng phân tích

Điền bảng CYK từng ô với văn phạm dạng chuẩn Chomsky: ở mỗi bước, thuật toán thử một điểm chia và ghép ô trái với ô phải theo các luật $$A \to BC$$. Bạn có thể tùy chỉnh cả văn phạm lẫn chuỗi đầu vào:

<div class="interactive-demo" markdown="1">
<div data-demo="cyk-explainer" data-preset="classic"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Viết đầy đủ chứng minh CFL không đóng dưới phép giao.
2. Chạy tay thuật toán CYK trên một ví dụ chuỗi nhỏ độ dài 4.
3. Giải thích trực giác vì sao ngôn ngữ chính quy đóng dưới phép giao (nhờ ô-tô-mát tích) còn CFL lại không.

## Tài liệu đọc thêm

Sipser §2.3; Hopcroft (phần CYK); Grune, *Parsing Techniques*.

## Tóm tắt

Lớp CFL đóng dưới hợp, nối, sao nhưng không đóng dưới giao và bù; dạng chuẩn CNF cho phép quyết định bài toán thành viên trong thời gian đa thức bằng thuật toán CYK.

**Bài tiếp theo:** Trình biên dịch, trình phân tích cú pháp và lộ trình nghiên cứu.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Mh-UQVmAxnw">Chomsky Normal Form &amp; CFG to CNF Conversion</a> — Neso Academy, tiếng Anh. Giới thiệu dạng chuẩn Chomsky — điều kiện đầu vào của thuật toán CYK.
- <a href="https://www.youtube.com/watch?v=N8d4kkfxM-s">The CYK Algorithm: How does it work? Dynamic Programming!</a> — Easy Theory, tiếng Anh. Giải thích thuật toán quy hoạch động CYK để kiểm tra chuỗi thuộc CFG.
- <a href="https://www.youtube.com/watch?v=P_F0-kY_kKQ">Closure Properties of Context-Free Languages</a> — Easy Theory, tiếng Anh. Tổng hợp các tính chất đóng và không đóng của ngôn ngữ phi ngữ cảnh.
