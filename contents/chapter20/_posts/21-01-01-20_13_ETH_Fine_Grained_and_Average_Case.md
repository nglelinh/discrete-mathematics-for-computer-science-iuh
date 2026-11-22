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
