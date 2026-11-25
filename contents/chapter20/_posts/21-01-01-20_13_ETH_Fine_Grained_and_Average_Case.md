---
layout: post
title: "ETH, Fine-grained và Average-case"
categories: chapter20
date: 2021-01-01
order: 13
required: true
lang: en
excerpt: "Giả thuyết thời gian mũ (ETH/SETH) và hệ quả, độ phức tạp mịn trong lớp P (3SUM, APSP), năm thế giới của Impagliazzo và sự khác biệt giữa mật mã học với NP-complete trường hợp xấu nhất."
---

<div class="textbook-epigraph" markdown="1">

"Not all hardness is NP-completeness — some is fine-grained, some is average-case."

<span class="epigraph-attribution">— Modern complexity map</span>

</div>

Bài học này giới thiệu ba hướng tiếp cận **tinh tế hơn** lý thuyết NP-complete cổ điển: giả thuyết thời gian mũ (ETH/SETH), cận dưới bên trong chính lớp $$P$$ (độ phức tạp mịn) và độ khó trường hợp trung bình gắn với mật mã học.

Giả thuyết $$P \neq NP$$ chỉ nói rằng `3SAT` không giải được trong thời gian đa thức, nhưng nó không cho biết liệu `3SAT` có giải được trong $$2^{\sqrt{n}}$$ hay không, cũng như không phân biệt được giữa thuật toán $$O(n^2)$$ và $$O(n^{1.5})$$ ngay bên trong lớp $$P$$. Bài học này mở cánh cửa vào biên giới nghiên cứu hiện đại của độ phức tạp: **ETH/SETH**, **Độ phức tạp mịn (Fine-Grained Complexity)** và **Độ khó trung bình (Average-Case Complexity)**.

## Bản đồ kiến thức nền: Ba trụ cột của Độ phức tạp Hiện đại

1. **Giả thuyết Thời gian Mũ (ETH & SETH)**:
   - **ETH:** `3SAT` không giải được trong thời gian dưới hàm mũ $$2^{o(n)}$$.
   - **SETH:** Khi $$k \to \infty$$, hằng số mũ cho `k-SAT` tiến sát $$2^n$$ (không tồn tại thuật toán $$O((2-\varepsilon)^n)$$ cho mọi $$k$$). Hai giả thuyết này mạnh hơn $$P \neq NP$$ nhưng giúp chứng minh nhiều chặn dưới sắc bén cực kỳ đẹp.
2. **Độ phức tạp Mịn (Fine-Grained Complexity ngay trong lớp $$P$$)**:
   Rút gọn từ SETH, `3SUM` hoặc `APSP` chứng minh các bài toán quen thuộc như **Khoảng cách soạn thảo (Edit Distance)** hay **Longest Common Subsequence (LCS)** khó có thể vượt qua bức tường $$O(n^{2-\varepsilon})$$ — giải thích vì sao 50 năm qua chưa ai tìm ra thuật toán $$O(n^{1.99})$$ cho Edit Distance!
3. **Trường hợp xấu nhất vs. Trung bình & Năm thế giới của Impagliazzo**:
   Mật mã học hiện đại (như RSA, mã hóa hậu lượng tử dựa trên mạng lưới LWE) không chỉ cần bài toán khó ở *trường hợp xấu nhất* mà phải khó ở **trường hợp trung bình** (sinh khóa ngẫu nhiên). Năm thế giới của Impagliazzo (`Algorithmica`, `Heuristica`, `Pessiland`, `Minicrypt`, `Cryptomania`) phân loại rõ vũ trụ toán học ta đang sống.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phát biểu** giả thuyết ETH/SETH cùng một hệ quả điển hình.
- **Mô tả** ý tưởng của độ phức tạp mịn (*fine-grained complexity*).
- **Giải thích** năm thế giới của Impagliazzo và lý do mật mã học không thể dựa trực tiếp vào tính NP-complete trường hợp xấu nhất.

</div>

## Giả thuyết thời gian mũ (ETH và SETH)

<div class="textbook-definition" markdown="1">

**Giả thuyết ETH** (*Exponential Time Hypothesis*, Impagliazzo–Paturi–Zane): bài toán 3SAT với $$n$$ biến không có thuật toán giải trong thời gian dưới hàm mũ $$2^{o(n)}$$.

</div>

**Hệ quả điển hình:** dưới giả thuyết ETH, nhiều bài toán đồ thị không có thuật toán $$2^{o(n+m)}$$ và nhiều bài toán FPT không thể đạt $$2^{o(k)}n^{O(1)}$$. Trong bài báo nghiên cứu, ETH thường dùng để chứng minh cận trên là chặt (chẳng hạn khẳng định thời gian $$2^{\Theta(k)}$$ là tối ưu dưới ETH).

**SETH** (*Strong ETH*) là phiên bản mạnh hơn xét bài toán $$k$$-SAT khi $$k\to\infty$$, làm nền tảng cho nhiều cận dưới đa thức (như khoảng cách biên tập *edit distance*).

## Độ phức tạp mịn (*Fine-grained complexity*)

Ngay bên trong lớp $$P$$, nhiều bài toán đặt ra câu hỏi về số mũ đa thức chính xác: liệu bài toán đường đi ngắn nhất mọi cặp đỉnh (APSP) có giải được trong $$O(n^{3-\varepsilon})$$ hay 3SUM có giải được trong $$O(n^{2-\varepsilon})$$ không? Các phép rút gọn **fine-grained** liên kết những bài toán này dưới các giả thuyết SETH, 3SUM hoặc APSP (xem các bài khảo sát của V. Vassilevska Williams). Đây là hướng nghiên cứu sôi nổi cho những ai quan tâm đến cận dưới có điều kiện kết hợp thiết kế thuật toán.

## Độ khó trung bình và năm thế giới của Impagliazzo

Impagliazzo (1995) phác họa năm kịch bản có thể xảy ra cho thế giới độ phức tạp:

| Thế giới | Đặc trưng |
|:---|:---|
| Algorithmica | $$P=NP$$ (hoặc mọi bài trong $$NP$$ đều giải được nhanh) |
| Heuristica | Khó ở trường hợp xấu nhất, nhưng dễ ở trường hợp trung bình |
| Pessiland | Khó ở trường hợp trung bình, nhưng không tồn tại hàm một chiều (OWF) |
| Minicrypt | Có hàm một chiều (mật mã đối xứng), nhưng chưa đủ cho mật mã khóa công khai |
| Cryptomania | Tồn tại đầy đủ mật mã khóa công khai (PKE) |

**Bài học quan trọng:** tính NP-complete ở trường hợp xấu nhất **không** tự động suy ra sự tồn tại của hàm một chiều. Mật mã học hiện đại phải dựa vào các giả thuyết riêng biệt có độ khó trung bình (như LWE, phân tích thừa số, logarit rời rạc) cùng các phép rút gọn bảo toàn phân bố trung bình (xem Goldreich).

## Tính ngẫu nhiên và bài toán đếm

Bên cạnh đó còn các nhánh lớn như lớp ngẫu nhiên **BPP** cùng khử ngẫu nhiên (*derandomization*) dưới cận dưới mạch (Arora–Barak), và lớp đếm **#P** gắn với định lý Valiant về *permanent*.

### Khung giải thích (nên đọc chậm): Phân biệt nhanh 3 bậc giả thuyết độ phức tạp trên cùng một trục

| Giả thuyết | Khẳng định cốt lõi | Hệ quả tiêu biểu |
| :--- | :--- | :--- |
| **1. $$P \neq NP$$** | `3SAT` $$\notin O(n^c)$$ với mọi hằng $$c$$ | Tách bài toán đa thức khỏi NP-complete, nhưng không cấm thuật toán $$2^{\sqrt{n}}$$ |
| **2. ETH** | `3SAT` $$\notin 2^{o(n)}$$ | `Vertex Cover` không giải được trong $$2^{o(k)} n^{O(1)}$$; `k-CLIQUE` không giải được trong $$n^{o(k)}$$ |
| **3. SETH** | `CNF-SAT` $$\notin O((2-\varepsilon)^n)$$ | **Edit Distance** và **LCS** không giải được trong $$O(n^{2-\varepsilon})$$ (chặn dưới ngay trong lớp $$P$$!) |

Mối quan hệ kéo theo chặt chẽ là: $$\text{SETH} \implies \text{ETH} \implies P \neq NP$$. Nắm được chuỗi này giúp bạn đọc hiểu ngay phần "Hardness Assumptions" trong các bài báo STOC/FOCS/SODA ngày nay.

## Bài tập

1. Viết một ghi chú ngắn (khoảng 1 trang) giải thích cách dùng ETH để chứng minh một cận trên thuật toán là chặt.
2. Lập bảng đầy đủ 5 thế giới của Impagliazzo kèm hệ quả thực tế đối với thuật toán và mật mã học.
3. Giải thích vì sao suy luận “TSP là NP-hard nên có thể dùng trực tiếp để xây dựng hệ mật mã an toàn” là chưa chính xác.

## Tài liệu đọc thêm

Impagliazzo (1995); Impagliazzo–Paturi–Zane (ETH); V. Vassilevska Williams (khảo sát fine-grained); Goldreich (*Foundations of Cryptography*).

## Tóm tắt

ETH, độ phức tạp mịn và lý thuyết độ khó trung bình mở rộng bản đồ độ phức tạp vượt ra ngoài ranh giới P/NP cổ điển, đồng thời làm rõ khoảng cách giữa tính khó xấu nhất với nền tảng của mật mã học.

**Bài tiếp theo:** 20.14 — Thực hành nghiên cứu và lộ trình đọc.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=hNesYirH8gM">Algorithms for NP-Hard Problems (Section 23.5: The Exponential Time Hypothesis)</a> — Tim Roughgarden Lectures, tiếng Anh. Giới thiệu giả thuyết thời gian mũ (ETH) đúng trọng tâm bài học.
- <a href="https://www.youtube.com/watch?v=dVQrj52JhyA">Exponential Time Hypotheses: ETH and SETH || @ CMU || Lecture 26d of CS Theory Toolkit</a> — Ryan O&#x27;Donnell, tiếng Anh. Trình bày chi tiết về ETH và SETH cho phần độ phức tạp mịn.
- <a href="https://www.youtube.com/watch?v=XV6f7XYUMg8">What Makes P vs. NP So Hard? (P ≠ EXPTIME, Time Hierarchy, Baker-Gill-Solovay)</a> — Undefined Behavior, tiếng Anh. Bối cảnh về các giả thuyết mạnh hơn $$P \neq NP$$.
