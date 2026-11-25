---
layout: post
title: "coNP và Hệ quả Cấu trúc"
categories: chapter20
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Định nghĩa lớp coNP, chứng minh P⊆NP∩coNP, hệ quả nếu một bài toán NP-complete thuộc coNP thì NP=coNP, và vị trí của bài toán phân tích thừa số nguyên tố."
---

<div class="textbook-epigraph" markdown="1">

"coNP is about short proofs of NO."

<span class="epigraph-attribution">— Structural complexity</span>

</div>

Nếu lớp $$NP$$ đặc trưng cho các bài toán có chứng chỉ ngắn cho câu trả lời **Có (Yes)**, thì $$\mathrm{coNP}$$ đặc trưng cho các bài toán có chứng chỉ ngắn cho câu trả lời **Không (No)**. Mối quan hệ giữa $$NP$$ và $$\mathrm{coNP}$$ mang nhiều hệ quả cấu trúc sâu sắc và gắn chặt với mật mã học.

Để chứng minh một công thức logic là *thỏa được* (`SAT`), bạn chỉ cần đưa ra **1 phép gán đúng** duy nhất. Nhưng để chứng minh công thức đó là *hằng đúng* (`TAUTOLOGY` — đúng với mọi phép gán), làm sao thuyết phục người khác chỉ bằng một chứng chỉ ngắn gọn? Câu hỏi về tính bất đối xứng giữa câu trả lời **CÓ** và câu trả lời **KHÔNG** sinh ra lớp $$\mathrm{coNP}$$ — người anh em song sinh phản chiếu của $$NP$$.

## Kiến thức cần nhớ: Ba trụ cột của $$\mathrm{coNP}$$ và Hệ quả Cấu trúc

1. **Định nghĩa $$\mathrm{coNP} = \{L \mid \overline{L} \in NP\}$$**:
   Một bài toán thuộc $$\mathrm{coNP}$$ khi các trường hợp trả lời **KHÔNG (NO-instance)** có chứng chỉ ngắn kiểm tra được trong thời gian đa thức (ví dụ: 1 phép gán làm công thức sai là chứng chỉ ngắn bác bỏ `TAUTOLOGY`).
2. **Bốn định lý cấu trúc xương sống**:
   - $$P \subseteq NP \cap \mathrm{coNP}$$ (vì $$P$$ đóng dưới phần bù).
   - Nếu $$P = NP$$ thì $$NP = \mathrm{coNP}$$ (nên chứng minh $$NP \neq \mathrm{coNP}$$ sẽ lập tức giải quyết luôn $$P \neq NP$$!).
   - Nếu tồn tại một bài toán NP-complete thuộc $$\mathrm{coNP}$$ thì toàn bộ $$NP = \mathrm{coNP}$$.
3. **Vùng giao thú vị $$NP \cap \mathrm{coNP}$$ (Trường hợp `FACTORING`)**:
   Phân tích thừa số nguyên tố (nền tảng của mã hóa RSA) nằm trong cả $$NP$$ lẫn $$\mathrm{coNP}$$ (nhờ kiểm tra nguyên tố ở $$P$$). Vì thế giới lý thuyết tin mạnh rằng $$NP \neq \mathrm{coNP}$$, `FACTORING` rất khó có khả năng là NP-complete!

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** lớp $$\mathrm{coNP}$$.
- **Chứng minh** quan hệ $$P\subseteq NP\cap\mathrm{coNP}$$.
- **Phát biểu** hệ quả khi có một bài toán NP-complete thuộc $$\mathrm{coNP}$$.
- **Thảo luận** vị trí của bài toán phân tích thừa số (factoring) trong $$NP\cap\mathrm{coNP}$$.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Lớp $$\mathrm{coNP}$$ gồm các ngôn ngữ có phần bù thuộc $$NP$$:

$$\mathrm{coNP}=\{L:\overline{L}\in NP\}.$$

Tương đương, mọi thể hiện trả lời Không (No) của $$L$$ đều có một chứng chỉ ngắn kiểm tra được trong thời gian đa thức.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét bài toán TAUTOLOGY (kiểm tra một công thức logic có luôn đúng hay không): câu trả lời “Không” tương ứng với sự tồn tại của một phép gán chân trị làm công thức sai — phép gán đó chính là chứng chỉ ngắn cho đáp án Không, nên TAUTOLOGY thuộc $$\mathrm{coNP}$$.

</div>

## Các định lý cấu trúc

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq\mathrm{coNP}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Nếu $$L\in P$$ thì phần bù $$\overline{L}\in P$$ (bằng cách đảo kết quả đầu ra của thuật toán quyết định $$L$$). Vì $$P\subseteq NP$$ nên $$\overline{L}\in NP$$, suy ra $$L\in\mathrm{coNP}$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq NP\cap\mathrm{coNP}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Suy trực tiếp từ $$P\subseteq NP$$ và định lý $$P\subseteq\mathrm{coNP}$$ ở trên.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Hệ quả cấu trúc). Nếu tồn tại một bài toán NP-complete $$L$$ sao cho $$L\in\mathrm{coNP}$$ thì $$NP=\mathrm{coNP}$$.

</div>

**Ý tưởng chứng minh.** Mọi ngôn ngữ $$A\in NP$$ đều rút gọn đa thức được về $$L$$ ($$A\le_p L$$); do lớp $$\mathrm{coNP}$$ đóng dưới phép rút gọn đa thức nên $$A\in\mathrm{coNP}$$, suy ra $$NP\subseteq\mathrm{coNP}$$ (xem Arora–Barak). Chiều ngược lại suy ra tương tự bằng cách lấy phần bù. $$\square$$

## Lưu ý về bài toán phân tích thừa số (*Factoring*)

Phiên bản quyết định chuẩn của bài toán phân tích thừa số nguyên tố (Integer Factoring) thuộc giao $$NP\cap\mathrm{coNP}$$, nhưng hiện **không** được biết (và cũng không được kỳ vọng) là NP-complete. Vì vậy, không thể nói độ an toàn của RSA dựa trên giả thiết “phân tích thừa số là NP-complete”.

### Giải thích: Kiểm chứng `FACTORING` thuộc cả $$NP$$ lẫn $$\mathrm{coNP}$$ bằng số cụ thể

Xét phiên bản quyết định của bài toán phân tích thừa số:
$$\mathrm{FACT} = \{ \langle N, k \rangle \mid N \text{ có ít nhất một ước không tầm thường } d \text{ thỏa } 1 < d \le k \}.$$

Thử trên đầu vào $$N = 91, k = 10$$:
- **Chứng chỉ cho câu trả lời CÓ ($$\mathrm{FACT} \in NP$$):** Đưa ra $$d = 7$$. Bộ kiểm chứng chỉ cần thử $$1 < 7 \le 10$$ và chia $$91 \div 7 = 13$$ dư `0` → **Xong trong $$O(\log^2 N)$$!**
- **Chứng chỉ cho câu trả lời KHÔNG ($$\mathrm{FACT} \in \mathrm{coNP}$$):** Xét đầu vào $$N = 91, k = 5$$ (câu trả lời là KHÔNG vì ước nhỏ nhất là 7). Chứng chỉ ngắn là **toàn bộ phân tích nguyên tố đầy đủ** $$c = (7, 13)$$. Bộ kiểm chứng làm 3 bước đa thức:
  1. Nhân lại: $$7 \times 13 = 91$$ (khớp $$N$$).
  2. Kiểm tra từng thừa số $$7, 13$$ đều là **số nguyên tố** (dùng thuật toán AKS trong $$P$$!).
  3. Kiểm tra mọi thừa số nguyên tố đều $$> k = 5$$ → theo tính duy nhất của phân tích nguyên tố, chắc chắn không có ước nào $$\le 5$$!

Vì cả trường hợp CÓ lẫn trường hợp KHÔNG đều có chứng chỉ đa thức, $$\mathrm{FACT} \in NP \cap \mathrm{coNP}$$.

## Bài tập

1. Viết lại chứng minh $$P\subseteq\mathrm{coNP}$$ đầy đủ từng bước.
2. Thảo luận ý nghĩa của giả thuyết $$NP=\mathrm{coNP}$$ đối với độ dài chứng minh cho các hằng đúng logic (tautology).
3. Đọc phần bàn luận về $$NP$$ và $$\mathrm{coNP}$$ trong giáo trình Arora–Barak.

## Tài liệu đọc thêm

Arora–Barak §2; Goldreich (các ghi chú khái niệm về độ phức tạp).

## Tóm tắt

Lớp $$\mathrm{coNP}$$ tập hợp các bài toán có chứng chỉ ngắn cho đáp án Không; luôn có $$P\subseteq NP\cap\mathrm{coNP}$$, và nếu một bài NP-complete rơi vào $$\mathrm{coNP}$$ thì $$NP=\mathrm{coNP}$$.

**Bài tiếp theo:** 20.5 — Phép rút gọn đa thức (*Karp reduction*).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=_pCw6h0Maj8">The Complexity Class coNP</a> — Computer Science Theory Explained, tiếng Anh. Giới thiệu lớp $$\mathrm{coNP}$$ qua góc nhìn chứng chỉ ngắn cho câu trả lời Không.
- <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Đặt $$\mathrm{coNP}$$ cạnh $$NP$$ trên bản đồ các lớp độ phức tạp.
- <a href="https://www.youtube.com/watch?v=pQsdygaYcE4">P vs NP Explained: Computer Science&#x27;s Biggest Puzzle</a> — Quanta Magazine, tiếng Anh. Bối cảnh rộng hơn về $$P$$ và $$NP$$ cho các hệ quả cấu trúc trong bài.
