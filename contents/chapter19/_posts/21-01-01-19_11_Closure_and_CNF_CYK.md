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

Cho một văn phạm phi ngữ cảnh $$G$$ và một chuỗi $$w$$ dài $$n$$ ký tự, làm sao máy tính kiểm tra xem $$w \in L(G)$$ hay không mà không rơi vào vòng lặp vô hạn kiểu $$A \Rightarrow B \Rightarrow A$$ hay thử nổ tổ hợp? Câu trả lời là một bộ đôi kinh điển: trước hết chuẩn hóa văn phạm về **Dạng chuẩn Chomsky (CNF)** để mọi cây phân tích đều là cây nhị phân chặt, rồi dùng quy hoạch động **thuật toán CYK** giải quyết bài toán thành viên trong đúng $$O(n^3 \cdot \vert G \vert)$$.

## Kiến thức cần nhớ: Ba trụ cột của Tính đóng, CNF và CYK

1. **Tính đóng bất đối xứng của CFL**:
   CFL đóng dưới hợp, nối và bao đóng Kleene (nhưng **không đóng** dưới giao và phần bù!). Bù lại, CFL đóng dưới **giao với ngôn ngữ chính quy** ($$L \cap R$$ vẫn là CFL) — công cụ cực mạnh để chứng minh một ngôn ngữ không phải CFL mà không cần Bổ đề Bơm dài dòng.
2. **Dạng chuẩn Chomsky (CNF)**:
   Chỉ cho phép hai loại quy tắc: $$A \to BC$$ (tách đôi) và $$A \to a$$ (sinh lá), cộng thêm $$S \to \varepsilon$$ nếu cần. Mọi chuỗi dài $$n \ge 1$$ luôn có đúng $$2n - 1$$ bước dẫn xuất!
3. **Thuật toán CYK (Quy hoạch động trên đoạn con $$[i, j]$$)**:
   Bảng tam giác $$T[i, j]$$ lưu tập tất cả biến $$A$$ sinh được chuỗi con $$w_i \dots w_j$$. Ô dài $$l$$ được điền bằng cách thử mọi điểm cắt $$k \in [i, j-1]$$ ghép hai ô con đã tính sẵn.

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

### Giải thích: Điền tay bảng tam giác CYK cho chuỗi `aabb`

Xét văn phạm CNF sinh $$a^n b^n$$ ($$n \ge 1$$):
$$S \to AB \mid AX, \quad X \to SB, \quad A \to a, \quad B \to b.$$

Kiểm tra chuỗi $$w = a_1 a_2 b_3 b_4$$ (độ dài $$n = 4$$):
- **Hàng độ dài 1** (từng ký tự đơn):
  $$T[1,1] = \{A\}, \quad T[2,2] = \{A\}, \quad T[3,3] = \{B\}, \quad T[4,4] = \{B\}.$$
- **Hàng độ dài 2** (ghép 1 + 1):
  - $$T[1,2]$$ từ $$T[1,1] \times T[2,2] = \{AA\} \implies \emptyset$$.
  - $$T[2,3]$$ từ $$T[2,2] \times T[3,3] = \{AB\} \implies \mathbf{\{S\}}$$ (vì $$S \to AB$$).
  - $$T[3,4]$$ từ $$T[3,3] \times T[4,4] = \{BB\} \implies \emptyset$$.
- **Hàng độ dài 3** (thử 2 cách cắt):
  - $$T[1,3]$$: cắt `(1|2..3)` cho $$AS$$ (không có luật), cắt `(1..2|3)` cho $$\emptyset \implies \emptyset$$.
  - $$T[2,4]$$: cắt `(2|3..4)` cho $$\emptyset$$, cắt `(2..3|4)` cho $$SB \implies \mathbf{\{X\}}$$ (vì $$X \to SB$$).
- **Ô đỉnh độ dài 4 ($$T[1,4]$$)**:
  - Cắt `(1|2..4)` cho $$T[1,1] \times T[2,4] = \{AX\} \implies \mathbf{\{S\}}$$ (vì $$S \to AX$$)!

Vì $$S \in T[1,4]$$, thuật toán CYK kết luận **`aabb` thuộc $$L(G)$$** chỉ sau vài phép tra bảng mà hoàn toàn không cần quay lui!

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
