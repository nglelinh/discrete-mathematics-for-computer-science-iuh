---
layout: post
title: "Lộ trình Nghiên cứu Automata & Computability"
categories: chapter18
date: 2021-01-01
order: 14
required: true
lang: en
excerpt: "Tổng hợp mạch kiến thức 18.1–18.13, các nhánh nghiên cứu hiện đại về ô-tô-mát, kế hoạch tự đọc 10 tuần và liên hệ với Chương 19–20."
---

<div class="textbook-epigraph" markdown="1">

"Automata theory is both a closed classical subject and an open toolbox."

<span class="epigraph-attribution">— Research perspective</span>

</div>

## Bản đồ kiến thức 18.1–18.13

Mạch lý thuyết của chương đi theo trình tự: DFA → sự tương đương NFA ≡ DFA → biểu thức chính quy và định lý Kleene → bổ đề bơm và định lý Myhill–Nerode → máy Turing → tính không quyết định được.

## Các nhánh nghiên cứu chính

| Nhánh nghiên cứu | Chủ đề tiêu biểu | Hội nghị / tài liệu chính |
|:---|:---|:---|
| Descriptional complexity | Độ phức tạp trạng thái (*state complexity*) | DCFS |
| Weighted / timed automata | Kiểm chứng hình thức (*verification*) | CONCUR, CAV |
| Learning automata | Thuật toán học $$L^*$$ của Angluin | ICML, ALT |
| Circuit vs. automata | Độ phức tạp mạch và ô-tô-mát | CCC |
| Logic và automata | Logic bậc hai đơn ngôi (MSO), ô-tô-mát Büchi | LICS |

## Kế hoạch tự đọc trong 10 tuần

- **Tuần 1–3:** Đọc Sipser Chương 1 và tự chứng minh lại xây dựng tập con, bổ đề bơm, Myhill–Nerode.
- **Tuần 4–5:** Ôn định lý Kleene và các tính chất đóng.
- **Tuần 6–7:** Máy Turing và tính không quyết định được.
- **Tuần 8:** Chọn một nhánh nghiên cứu và đọc khảo sát khoảng 10 bài báo.
- **Tuần 9–10:** Viết ghi chú tổng hợp khoảng 6 trang hoặc chuẩn bị bài trình bày ngắn.

## Danh mục bài tập cốt lõi

1. Thực hiện phép xây dựng tập con hoàn toàn bằng tay.
2. Chứng minh $$0^n1^n$$ không chính quy bằng bổ đề bơm.
3. Chứng minh một ngôn ngữ có vô hạn lớp tương đương theo Myhill–Nerode.
4. Đối chiếu khái niệm bảng cấu hình (*tableau*) của máy Turing với định lý Cook–Levin ở Chương 20.

## Tài liệu đọc cốt lõi

Sipser; Hopcroft–Ullman; Kozen; Sakarovitch, *Elements of Automata Theory* (mức nâng cao).

## Tóm tắt Chương 18

Qua 14 bài học từ DFA đến giới hạn tính toán của máy Turing, bạn đã có nền tảng để tiếp cận các công trình về ô-tô-mát và kiểm chứng hình thức, đồng thời sẵn sàng chuyển tiếp sang Chương 19 và Chương 20.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=BBuBv3P2aSs">TOC – Conclusion and Summary</a> — Neso Academy, tiếng Anh. Tổng kết bản đồ lý thuyết ô-tô-mát tương ứng với lộ trình 18.1–18.13.
- <a href="https://www.youtube.com/watch?v=58N2N7zJGrQ">Introduction to Theory of Computation</a> — Neso Academy, tiếng Anh. Điểm khởi đầu vào lý thuyết tính toán trước khi chọn nhánh nghiên cứu.
- <a href="https://www.youtube.com/watch?v=macM_MtS_w4">Turing &amp; The Halting Problem - Computerphile</a> — Computerphile, tiếng Anh. Ranh giới của tính quyết định được, nơi mở ra nhiều câu hỏi nghiên cứu.
