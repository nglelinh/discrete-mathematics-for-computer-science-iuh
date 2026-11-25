---
layout: post
title: "Phân cấp Chomsky"
categories: chapter19
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Bốn lớp văn phạm Chomsky (Type 0 đến Type 3), dạng luật sinh, mô hình máy nhận dạng tương ứng và quan hệ bao hàm chặt."
---

<div class="textbook-epigraph" markdown="1">

"Four types of rules, four kinds of machines."

<span class="epigraph-attribution">— Chomsky hierarchy</span>

</div>

![Chomsky](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_chomsky_nested.svg)

<p class="textbook-figure-caption" data-figure="19.2">Quan hệ lồng nhau giữa bốn lớp ngôn ngữ: Type-3 ⊂ Type-2 ⊂ Type-1 ⊂ Type-0.</p>

Khi Noam Chomsky phân loại các văn phạm hình thức thành bốn tầng lồng nhau (Loại 3 $$\subset$$ Loại 2 $$\subset$$ Loại 1 $$\subset$$ Loại 0), ông không chỉ tạo ra một bảng phân loại ngữ pháp học mà còn vẽ ra **chiếc thang quyền lực tính toán** quan trọng bậc nhất của Khoa học Máy tính. Mỗi lần nới lỏng một ràng buộc nhỏ trên quy tắc sinh, bộ nhớ của chiếc máy tương ứng nhảy lên một nấc mới: từ bộ nhớ hữu hạn, sang ngăn xếp, sang băng giới hạn tuyến tính, và cuối cùng là băng vô hạn của máy Turing.

## Bản đồ kiến thức nền: Bốn nấc thang của Phân cấp Chomsky

1. **Loại 3 — Ngôn ngữ Chính quy (Regular) $$\leftrightarrow$$ DFA / NFA**:
   Quy tắc tuyến tính một phía ($$A \to aB \mid a$$). Đủ cho phân tích từ vựng (lexer) và biểu thức chính quy, nhưng không đếm được cặp ngoặc lồng nhau sâu tùy ý.
2. **Loại 2 — Ngôn ngữ Phi ngữ cảnh (CFG) $$\leftrightarrow$$ PDA**:
   Vế trái đúng 1 biến ($$A \to \alpha$$). Xương sống của cú pháp ngôn ngữ lập trình (HTML, JSON, C, Python) nhờ ngăn xếp xử lý được cấu trúc lồng nhau.
3. **Loại 1 — Ngôn ngữ Cảm ngữ cảnh (CSG) $$\leftrightarrow$$ LBA (Linear Bounded Automaton)**:
   Quy tắc không thu hẹp độ dài ($$\vert \alpha \vert \le \vert \beta \vert$$). Đủ mạnh để nhận $$a^n b^n c^n$$ và luôn **quyết định được**, nhưng bài toán thành viên đã là PSPACE-complete.
4. **Loại 0 — Văn phạm Tổng quát $$\leftrightarrow$$ Máy Turing (RE)**:
   Không giới hạn quy tắc; bao trùm mọi ngôn ngữ nhận dạng được bởi thuật toán, đồng thời chạm vào ranh giới bất khả quyết định.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân loại** luật sinh theo bốn cấp của phân cấp Chomsky.
- **Nêu** mô hình máy nhận dạng tương ứng với từng cấp văn phạm.
- **Phát biểu** quan hệ bao hàm chặt giữa các lớp ngôn ngữ.

</div>

## Bảng phân loại Chomsky

| Loại | Tên lớp ngôn ngữ | Dạng luật sinh (ý chính) | Mô hình máy tương ứng |
|:---:|:---|:---|:---|
| 3 | Chính quy (Regular) | $$A\to aB$$ hoặc $$A\to a$$ | DFA / NFA |
| 2 | Phi ngữ cảnh (Context-Free) | $$A\to\alpha$$ | Ô-tô-mát đẩy xuống (PDA) |
| 1 | Cảm ngữ cảnh (Context-Sensitive) | $$\lvert\alpha\rvert\le\lvert\beta\rvert$$ | Ô-tô-mát giới hạn tuyến tính (LBA) |
| 0 | Đệ quy liệt kê (RE) | Tự do | Máy Turing (TM) |

<div class="textbook-theorem" markdown="1">

**Định lý** (Quan hệ bao hàm cổ điển). Các lớp ngôn ngữ trong phân cấp Chomsky lồng chặt vào nhau:

$$\mathcal{L}_3\subset\mathcal{L}_2\subset\mathcal{L}_1\subset\mathcal{L}_0$$

(với quy ước xử lý chuẩn cho luật sinh chuỗi rỗng $$\varepsilon$$).

</div>

### Khung giải thích (nên đọc chậm): Phân loại nhanh 4 chuỗi mẫu kinh điển lên đúng tầng Chomsky

| Ngôn ngữ mẫu | Tầng Chomsky thấp nhất chứa nó | Vì sao không nằm ở tầng thấp hơn? |
| :--- | :---: | :--- |
| $$L_1 = \{a^n b^m \mid n, m \ge 0\}$$ | **Loại 3 (Chính quy)** | Không cần đếm khớp $$n$$ với $$m$$; chỉ cần DFA 2 trạng thái kiểm tra không có `a` sau `b` |
| $$L_2 = \{a^n b^n \mid n \ge 0\}$$ | **Loại 2 (Phi ngữ cảnh)** | Cần 1 ngăn xếp để đẩy `a` rồi khớp với `b` (vượt ngoài khả năng đếm hữu hạn của DFA) |
| $$L_3 = \{a^n b^n c^n \mid n \ge 0\}$$ | **Loại 1 (Cảm ngữ cảnh)** | 1 ngăn xếp xóa hết `a` khi khớp `b` nên không còn nhớ số lượng để khớp tiếp `c` |
| $$L_4 = A_{\mathrm{TM}}$$ | **Loại 0 (RE, không decidable)** | Mọi ngôn ngữ Loại 1 đều decidable, nên ngôn ngữ bất khả quyết định chỉ có thể nằm ở Loại 0 |

Nắm chắc 4 ví dụ mốc $$a^n b^m \subset a^n b^n \subset a^n b^n c^n \subset A_{\mathrm{TM}}$$ giúp bạn phân loại tức thì hầu hết bài toán trong đề thi và thực tế thiết kế ngôn ngữ.

## Bài tập

1. Xác định cấp Chomsky của văn phạm $$S\to aS\mid b$$.
2. Thảo luận trực giác vì sao ngôn ngữ $$a^nb^nc^n$$ không thuộc loại 2 (chuẩn bị cho bổ đề bơm CFL ở bài sau).
3. Liên hệ lớp ngôn ngữ loại 3 với các kết quả về ngôn ngữ chính quy ở Chương 18.

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman; các công trình lịch sử của Chomsky (1956, 1959).

## Tóm tắt

Phân cấp Chomsky chia văn phạm thành bốn loại lồng nhau, mỗi loại tương ứng trực tiếp với một mô hình bộ nhớ và máy nhận dạng riêng biệt.

**Bài tiếp theo:** Văn phạm chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu bốn bậc phân cấp Chomsky và mô hình bộ nhớ tương ứng.
- <a href="https://www.youtube.com/watch?v=VygeACNATI4">The Chomsky Hierarchy: Every Grammar Buys a Different Memory</a> — DataMListic, tiếng Anh. Giải thích trực quan mối liên hệ giữa từng lớp văn phạm và loại bộ nhớ máy.
- <a href="https://www.youtube.com/watch?v=9idnQ2C6HfA">Chomsky Hierarchy - Explained in Detail with examples</a> — Advanced CS IT for GATE, tiếng Anh. Bảng phân cấp chi tiết kèm các ví dụ ngôn ngữ cụ thể.
