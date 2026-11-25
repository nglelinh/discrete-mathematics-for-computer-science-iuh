---
layout: post
title: "Văn phạm Chính quy ≡ Ngôn ngữ Chính quy"
categories: chapter19
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Văn phạm tuyến tính phải (right-linear grammar), chứng minh sự tương đương với NFA và kết nối trực tiếp với Chương 18."
---

<div class="textbook-epigraph" markdown="1">

"Right-linear rules are finite automata in disguise."

<span class="epigraph-attribution">— Grammar–automaton bridge</span>

</div>

Một trong những vẻ đẹp đối xứng đầu tiên của lý thuyết ngôn ngữ hình thức là: cùng một lớp ngôn ngữ chính quy có thể được mô tả bằng ba góc nhìn hoàn toàn khác nhau — biểu thức chính quy (đại số), máy trạng thái hữu hạn DFA/NFA (máy nhận dạng), và văn phạm chính quy (bộ sinh chuỗi). Bài học này nối chặt mắt xích thứ ba: cách chuyển đổi qua lại trực tiếp giữa văn phạm tuyến tính phải và NFA.

## Bản đồ kiến thức nền: Ba trụ cột của Văn phạm Chính quy

1. **Văn phạm Tuyến tính phải (Right-linear) & Tuyến tính trái (Left-linear)**:
   Trong văn phạm tuyến tính phải, mỗi quy tắc có dạng $$A \to wB$$ hoặc $$A \to w$$ (biến chỉ xuất hiện ở *cuối* vế phải). Quan trọng: không được trộn lẫn tuyến tính phải và tuyến tính trái trong cùng một văn phạm nếu muốn giữ nguyên lớp chính quy!
2. **Song ánh cấu trúc giữa Biến văn phạm và Trạng thái NFA**:
   Mỗi biến $$A \in V$$ tương ứng đúng với một trạng thái của NFA; quy tắc $$A \to aB$$ chính là cung chuyển $$\delta(A, a) \ni B$$, còn quy tắc $$A \to a$$ dẫn tới một trạng thái kết thúc mới $$q_f$$.
3. **Bẫy trộn tuyến tính hai phía**:
   Chỉ cần cho phép đồng thời mở rộng hai bên như $$S \to aSb \mid \varepsilon$$ là ta đã nhảy vọt ra khỏi lớp chính quy sang lớp phi ngữ cảnh $$a^n b^n$$.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** văn phạm tuyến tính phải (*right-linear*) và tuyến tính trái (*left-linear*).
- **Trình bày** khung chứng minh sự tương đương giữa văn phạm chính quy và NFA.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Một văn phạm được gọi là **tuyến tính phải** (*right-linear*) nếu mọi luật sinh đều có dạng $$A\to wB$$ hoặc $$A\to w$$ với $$w\in\Sigma^*$$ (sau khi chuẩn hóa, ta thường đưa $$w$$ về một ký hiệu đơn hoặc chuỗi rỗng).

</div>

## Định lý tương đương

<div class="textbook-theorem" markdown="1">

**Định lý.** Ngôn ngữ $$L$$ là ngôn ngữ chính quy khi và chỉ khi tồn tại một văn phạm tuyến tính phải $$G$$ sao cho $$L=L(G)$$.

</div>

**Ý tưởng chứng minh.**  
Chiều từ văn phạm sang NFA: xem mỗi ký hiệu không kết thúc là một trạng thái; luật sinh $$A\to aB$$ tương ứng với cạnh chuyển từ $$A$$ sang $$B$$ mang nhãn $$a$$, còn luật $$A\to a$$ đi tới trạng thái kết thúc mới.  
Chiều từ NFA sang văn phạm: thực hiện phép biến đổi ngược lại từ tập trạng thái và cạnh chuyển sang tập luật sinh. $$\square$$

### Khung giải thích (nên đọc chậm): Chuyển đổi trực tiếp bằng tay một văn phạm tuyến tính phải sang NFA

Cho văn phạm tuyến tính phải sinh các chuỗi nhị phân kết thúc bằng `01`:
$$S \to 0S \mid 1S \mid 0A, \qquad A \to 1B, \qquad B \to \varepsilon.$$

Ánh xạ trực tiếp từng quy tắc sang cung chuyển của NFA (trạng thái đầu $$S$$, trạng thái chấp nhận $$B$$ vì có $$B \to \varepsilon$$):
- Từ $$S \to 0S \mid 1S$$: vẽ vòng khuyên tự quay lại $$S$$ với nhãn `0` và `1`.
- Từ $$S \to 0A$$: vẽ cung $$S \xrightarrow{0} A$$.
- Từ $$A \to 1B$$: vẽ cung $$A \xrightarrow{1} B$$.

**Kiểm tra ngược với chuỗi `101`:**
- Theo văn phạm: $$S \Rightarrow 1S \Rightarrow 10A \Rightarrow 101B \Rightarrow 101$$.
- Theo NFA: $$S \xrightarrow{1} S \xrightarrow{0} A \xrightarrow{1} B \in F$$ (Chấp nhận!).

Từng bước dẫn xuất của văn phạm khớp **1–1** với từng bước nhảy trạng thái của NFA!

## Bài tập

1. Xây dựng văn phạm tuyến tính phải tương ứng với DFA kiểm tra tính chẵn lẻ số bit 1.
2. Viết chứng minh chi tiết cho một trong hai chiều của định lý trên.
3. Giải thích vì sao văn phạm tuyến tính trái (*left-linear*) cũng sinh ra đúng lớp ngôn ngữ chính quy.

## Tài liệu đọc thêm

Hopcroft–Ullman; Sipser (phần bài tập).

## Tóm tắt

Văn phạm loại 3 (tuyến tính phải hoặc tuyến tính trái) tương đương hoàn toàn với lớp ngôn ngữ chính quy ở Chương 18.

**Bài tiếp theo:** Văn phạm phi ngữ cảnh (CFG).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=WgEsPTAL55Q">Regular Grammar</a> — Neso Academy, tiếng Anh. Giới thiệu văn phạm chính quy và cấu trúc các luật sinh.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Cách thực hiện dẫn xuất chuỗi từ văn phạm.
- <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Biểu thức chính quy — một cách biểu diễn khác cho cùng lớp ngôn ngữ chính quy.
