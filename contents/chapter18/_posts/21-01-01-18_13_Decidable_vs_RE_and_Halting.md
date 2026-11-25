---
layout: post
title: "Decidable, RE và Bài toán Dừng"
categories: chapter18
date: 2021-01-01
order: 13
required: true
lang: en
excerpt: "Phân biệt ngôn ngữ quyết định được (decidable) và đệ quy liệt kê (RE); bài toán A_TM và tính không quyết định được của bài toán dừng (Halting Problem)."
---

<div class="textbook-epigraph" markdown="1">

"Some problems are not merely hard — they are impossible."

<span class="epigraph-attribution">— Computability</span>

</div>

Bài học này đóng vai trò cầu nối giữa Chương 18 và Chương 20: ngoài những bài toán khó giải trong thời gian đa thức, tồn tại những bài toán hoàn toàn **không thể quyết định được** bằng bất kỳ thuật toán nào.

Mọi lập trình viên đều từng mơ về một công cụ kiểm tra mã nguồn hoàn hảo: nạp vào bất kỳ chương trình `P` và đầu vào `w` nào, công cụ lập tức báo chính xác `P(w)` có bị treo vòng lặp vô hạn hay không. Năm 1936, Alan Turing chứng minh giấc mơ đó là **bất khả thi về mặt toán học** — không phải vì máy tính còn chậm hay ta chưa đủ thông minh, mà vì chính logic tự quy chiếu đã dựng nên một bức tường không thể vượt qua.

## Kiến thức cần nhớ: Ba trụ cột của Tính quyết định được và Bài toán Dừng

1. **Ngôn ngữ Quyết định được (Decidable / Recursive) vs. Nhận dạng được (RE)**:
   Một ngôn ngữ là *decidable* nếu có máy Turing luôn dừng và trả lời Đúng/Sai cho mọi đầu vào. Ngược lại, ngôn ngữ *RE* chỉ cần dừng và chấp nhận khi $$w \in L$$, nhưng có thể chạy mãi không dừng khi $$w \notin L$$.
2. **Định lý Bù ($$L$$ và $$\overline{L}$$ đều RE $$\iff L$$ Decidable)**:
   Nếu có máy nhận dạng cho $$L$$ và máy nhận dạng cho phần bù $$\overline{L}$$, ta chỉ cần chạy song song hai máy từng bước một — chắc chắn một trong hai sẽ dừng, biến cả hai thành bộ quyết định.
3. **Phép chéo hóa Cantor (Diagonalization) & Rút gọn (Reduction)**:
   Chứng minh $$A_{\mathrm{TM}}$$ không quyết định được dùng đúng kỹ thuật chéo hóa của Cantor (tạo ra máy nghịch lý $$D$$ làm ngược lại dự đoán về chính nó); sau đó dùng phép rút gọn để chứng minh hàng loạt bài toán thực tế khác (như `HALT`, kiểm tra tương đương hai chương trình) cũng bất khả quyết định.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Phân biệt** ngôn ngữ quyết định được (*decidable*) và ngôn ngữ đệ quy liệt kê (*RE*).
- **Phác thảo** lý do bài toán $$A_{\mathrm{TM}}$$ thuộc lớp RE nhưng không quyết định được.
- **Nêu** hệ quả của tính không quyết định được đối với kiểm chứng phần mềm (*verification*).

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

- **Decidable (quyết định được / đệ quy):** tồn tại một máy Turing luôn dừng trên mọi đầu vào và chấp nhận đúng các chuỗi thuộc $$L$$.
- **RE (đệ quy liệt kê / Turing-recognizable):** tồn tại một máy Turing chấp nhận đúng các chuỗi thuộc $$L$$, nhưng có thể lặp vô hạn đối với các chuỗi không thuộc $$L$$.

</div>

Quan hệ bao hàm chặt giữa các lớp ngôn ngữ là: $$\mathrm{decidable}\subsetneq\mathrm{RE}\subsetneq$$ tập mọi ngôn ngữ.

## Bài toán $$A_{\mathrm{TM}}$$

Xét ngôn ngữ $$A_{\mathrm{TM}}=\{\langle M,w\rangle:M\text{ chấp nhận }w\}$$. Ngôn ngữ này thuộc lớp **RE** vì máy Turing phổ dụng có thể mô phỏng $$M$$ trên đầu vào $$w$$ và chấp nhận khi $$M$$ chấp nhận. Tuy nhiên, $$A_{\mathrm{TM}}$$ **không quyết định được** (chứng minh bằng lập luận đường chéo, xem Sipser §4–5).

## Bài toán Dừng (*Halting Problem*)

Bài toán dừng $$\mathrm{HALT}=\{\langle M,w\rangle:M\text{ dừng trên }w\}$$ cũng là bài toán không quyết định được (có thể chứng minh bằng phép quy giảm từ $$A_{\mathrm{TM}}$$).

### Giải thích: Theo dõi tận mắt nghịch lý tự quy chiếu của máy $$D$$

Giả sử tồn tại một bộ quyết định hoàn hảo $$H(\langle M, w \rangle)$$ luôn dừng và trả về:
- `ACCEPT` nếu máy $$M$$ chấp nhận chuỗi $$w$$;
- `REJECT` nếu máy $$M$$ từ chối hoặc chạy vô hạn trên $$w$$.

Bây giờ ta viết một chương trình ngắn $$D$$ nhận mã nguồn của một máy bất kỳ $$\langle M \rangle$$ làm đầu vào:
1. $$D$$ gọi $$H(\langle M, \langle M \rangle \rangle)$$ để hỏi: *"Nếu nạp chính mã nguồn của $$M$$ vào cho $$M$$ chạy thì sao?"*
2. $$D$$ **cố tình làm ngược lại**: nếu $$H$$ bảo `ACCEPT` thì $$D$$ trả về `REJECT`; nếu $$H$$ bảo `REJECT` thì $$D$$ trả về `ACCEPT`.

**Khoảnh khắc sụp đổ:** Điều gì xảy ra khi ta nạp **chính mã nguồn $$\langle D \rangle$$** vào cho $$D$$ chạy?

| Giả sử kết quả của $$D(\langle D \rangle)$$ | Bộ quyết định $$H(\langle D, \langle D \rangle \rangle)$$ phải báo gì? | Hành động thực tế của $$D(\langle D \rangle)$$ (làm ngược lại $$H$$) | Kết luận |
| :--- | :---: | :---: | :---: |
| Trường hợp 1: $$D(\langle D \rangle)$$ **ACCEPT** | `ACCEPT` | **REJECT** | Mâu thuẫn! |
| Trường hợp 2: $$D(\langle D \rangle)$$ **REJECT** | `REJECT` | **ACCEPT** | Mâu thuẫn! |

Cả hai nhánh đều dẫn tới mâu thuẫn tuyệt đối. Vì mọi bước xây dựng $$D$$ từ $$H$$ đều hợp lệ, thứ duy nhất sai chính là giả định ban đầu rằng bộ quyết định $$H$$ tồn tại. Do đó, $$A_{\mathrm{TM}}$$ (và theo phép rút gọn là Bài toán Dừng) là **bất khả quyết định**.

## Bài tập

1. Chứng minh mọi ngôn ngữ quyết định được đều thuộc lớp RE ($$\mathrm{decidable} \subseteq \mathrm{RE}$$).
2. Nếu giả sử $$A_{\mathrm{TM}}$$ quyết định được thì điều gì sẽ xảy ra?
3. Liên hệ tính không quyết định được của bài toán dừng với bài toán kiểm chứng chương trình tự động trong thực tế.

## Tài liệu đọc thêm

Sipser §4–5; Davis, *Computability and Unsolvability*.

## Tóm tắt

Lớp ngôn ngữ quyết định được là tập con thực sự của lớp RE, và bài toán dừng khẳng định giới hạn tuyệt đối của khả năng tính toán bằng thuật toán.

**Bài tiếp theo:** Lộ trình nghiên cứu ô-tô-mát và lý thuyết khả tính.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=macM_MtS_w4">Turing &amp; The Halting Problem - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu bài toán dừng và lý do không tồn tại thuật toán giải tổng quát.
- <a href="https://www.youtube.com/watch?v=6XZvw9W9QSc">The Halting Problem</a> — Neso Academy, tiếng Anh. Đặt bài toán dừng vào khung khái niệm decidable và undecidable.
- <a href="https://www.youtube.com/watch?v=_eM0-KfAmhQ">Undecidability of the Halting Problem</a> — Neso Academy, tiếng Anh. Chứng minh tính không quyết định được bằng kỹ thuật tự áp dụng.
