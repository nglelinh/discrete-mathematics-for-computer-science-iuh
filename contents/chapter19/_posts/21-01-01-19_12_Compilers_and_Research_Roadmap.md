---
layout: post
title: "Compiler, Parser và Lộ trình Nghiên cứu"
categories: chapter19
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "Phân tách tầng từ vựng (lexer) và phân tích cú pháp (parser), tổng quan LL/LR, các nhánh nghiên cứu ngôn ngữ hình thức và lộ trình tự học 12 tuần."
---

<div class="textbook-epigraph" markdown="1">

"Lex with regular languages; parse with context-free structure."

<span class="epigraph-attribution">— Compiler construction</span>

</div>

![Phases](/discrete-mathematics-for-computer-science-iuh/img/course/compiler_phases.svg)

<p class="textbook-figure-caption" data-figure="19.4">Phân tách kinh điển trong trình biên dịch: bộ phân tích từ vựng dùng ngôn ngữ chính quy, còn bộ phân tích cú pháp dùng văn phạm phi ngữ cảnh.</p>

Mỗi khi bạn bấm "Run" trên một đoạn mã Python, Rust hay TypeScript, toàn bộ lý thuyết Chương 19 lập tức hoạt động chỉ trong vài mili-giây: bộ phân tích từ vựng (Lexer) dùng DFA cắt văn bản thành chuỗi token, rồi bộ phân tích cú pháp (Parser) dùng CFG/DPDA dựng cây cú pháp trừu tượng (AST) để kiểm tra lỗi cú pháp trước khi sinh mã máy. Bài tổng kết này nối liền lý thuyết ngôn ngữ hình thức với kiến trúc trình biên dịch thực tế và các hướng nghiên cứu hiện đại.

## Kiến thức cần nhớ: Ba cầu nối từ Chương 19 sang Trình biên dịch & Nghiên cứu

1. **Đường ống Frontend của Trình biên dịch (Lexer → Parser → Semantic Check)**:
   Tách biệt rạch ròi tầng Chính quy (DFA cho từ khóa, định danh, số) khỏi tầng Phi ngữ cảnh (LL/LR parser cho biểu thức, vòng lặp, hàm), rồi giao các ràng buộc cảm ngữ cảnh (kiểm tra khai báo biến, kiểu dữ liệu) cho tầng ngữ nghĩa.
2. **Phân tích cú pháp tuyến tính $$O(n)$$ (LL(k), LR(1), LALR)**:
   CYK tổng quát chạy $$O(n^3)$$ là quá chậm cho tệp mã nguồn hàng chục nghìn dòng. Trình biên dịch thực tế chọn các lớp con đơn định của CFG (LL cho parser viết tay như Rust/Go, LR/LALR cho Bison/Yacc) để phân tích trong đúng một lượt $$O(n)$$.
3. **Hướng mở rộng hiện đại (PEG, Tree-sitter, Program Synthesis)**:
   Các công cụ IDE hiện đại dùng phân tích cú pháp gia tăng (*incremental parsing* như Tree-sitter, GLR) để cập nhật cây AST ngay khi lập trình viên gõ từng phím mà không cần parse lại cả tệp.

## Bản đồ Chương 19

Mạch nội dung của chương đi từ $$\Sigma^*$$ và phép toán ngôn ngữ → văn phạm và phân cấp Chomsky → CFG, PDA và sự tương đương → bổ đề bơm → CNF và CYK → ứng dụng trong trình biên dịch.

## Ứng dụng trong trình biên dịch

![Giai đoạn phân tích từ vựng trong trình biên dịch](/discrete-mathematics-for-computer-science-iuh/img/course/lexical_analysis.svg)

| Giai đoạn | Lớp ngôn ngữ | Công cụ điển hình |
|:---|:---|:---|
| Bộ phân tích từ vựng (Lexer) | Chính quy (Regular) | Flex, biểu thức chính quy |
| Bộ phân tích cú pháp (Parser) | Phi ngữ cảnh (thường là LALR / LL) | yacc, ANTLR, bộ phân tích đệ quy viết tay |

Trong thực hành phân tích cú pháp, lớp ngôn ngữ phi ngữ cảnh đơn định (**DCFL** $$\subset$$ CFL, nhận bởi PDA đơn định) đóng vai trò đặc biệt quan trọng vì cho phép phân tích nhanh trong thời gian tuyến tính.

## Các nhánh nghiên cứu liên quan

| Nhánh nghiên cứu | Chủ đề tiêu biểu |
|:---|:---|
| Lý thuyết phân tích cú pháp (*Parsing theory*) | GLL, GLR, Earley, PEG |
| Suy diễn văn phạm (*Grammar inference*) | Học văn phạm CFG từ dữ liệu |
| Ô-tô-mát cây (*Tree automata*) | Xử lý XML, tối ưu hóa trình biên dịch |
| Văn phạm có trọng số / xác suất (SCFG) | Xử lý ngôn ngữ tự nhiên (NLP) |
| Kiểm chứng hình thức (*Verification*) | Hệ thống đẩy xuống (*pushdown systems*) |

## Lộ trình tự đọc trong 12 tuần

- **Tuần 1–2:** Ôn mục 19.1–19.5 và nối lại với ngôn ngữ chính quy ở Chương 18.
- **Tuần 3–5:** Làm chắc CFG, PDA và bổ đề bơm CFL.
- **Tuần 6–7:** Chuyển đổi CNF và tự cài đặt thuật toán CYK.
- **Tuần 8:** Đọc các chương về phân tích cú pháp trong sách *Dragon Book*.
- **Tuần 9–10:** Chọn một nhánh nghiên cứu và đọc các bài báo nền tảng.
- **Tuần 11–12:** Xây dựng một trình phân tích cú pháp nhỏ hoặc viết ghi chú về độ khó tính toán của các bài toán văn phạm.

### Giải thích: Theo dõi một dòng lệnh `if (x > 0) y = 1;` đi qua 3 tầng của Trình biên dịch

| Tầng xử lý | Mô hình lý thuyết Chương 19 | Đầu ra cụ thể | Lỗi nào bị bắt ở tầng này? |
| :--- | :---: | :--- | :--- |
| **1. Lexer (Từ vựng)** | **DFA / Biểu thức chính quy** | `[IF, LPAREN, ID(x), GT, NUM(0), RPAREN, ID(y), EQ, NUM(1), SEMI]` | Ký tự lạ không hợp lệ như `if (x @ 0)` |
| **2. Parser (Cú pháp)** | **CFG / DPDA (LL hoặc LR)** | Cây AST: `IfStmt(cond=BinOp(>, x, 0), body=Assign(y, 1))` | Thiếu dấu ngoặc `if (x > 0 y = 1;` |
| **3. Semantic (Ngữ nghĩa)** | **Vượt ngoài CFG (cảm ngữ cảnh)** | Bảng ký hiệu xác nhận `x, y` đã khai báo và khớp kiểu | Dùng biến chưa khai báo `z = 1;` hoặc cộng chuỗi với số nguyên |

Nhờ bảng 3 tầng này, bạn thấy rõ lý do trình biên dịch không nhồi nhét kiểm tra kiểu dữ liệu vào CFG: mỗi tầng chỉ giải đúng bài toán nằm trong sức mạnh tối ưu của mô hình toán học tương ứng!

## Danh mục bài tập cốt lõi

1. Chứng minh $$\{a^nb^n\}$$ là CFL nhưng không phải ngôn ngữ chính quy.
2. Chứng minh $$\{a^nb^nc^n\}$$ không phải là CFL.
3. Cài đặt và kiểm thử thuật toán CYK.
4. Viết một văn phạm không mơ hồ cho biểu thức số học.

## Tài liệu tham khảo chính

Sipser; Hopcroft–Ullman; Aho et al., *Compilers*; Grune, *Parsing Techniques*; Sakarovitch; Kozen.

## Tóm tắt Chương 19

Qua 12 bài học từ khái niệm chuỗi cơ bản đến CFL, PDA và thuật toán CYK, chương này kết nối chặt chẽ giữa Chương 18 (ô-tô-mát chính quy và máy Turing) với Chương 20 (độ phức tạp tính toán: bài toán thành viên cho CNF thuộc lớp P, nhưng nhiều bài toán khác trên văn phạm lại khó).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=bxpc9Pp5pZM">Parsing Explained - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu trực quan quá trình phân tích cú pháp gồm lexer và parser trên văn phạm.
- <a href="https://www.youtube.com/watch?v=OIKL6wFjFOo">Introduction to Parsers</a> — Neso Academy, tiếng Anh. Vai trò của bộ phân tích cú pháp trong thiết kế trình biên dịch.
- <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Ôn lại biểu thức chính quy dùng cho tầng phân tích từ vựng.
