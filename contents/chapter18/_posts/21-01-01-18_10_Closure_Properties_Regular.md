---
layout: post
title: "Tính Đóng của Ngôn ngữ Chính quy"
categories: chapter18
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "Chứng minh tính đóng của lớp ngôn ngữ chính quy dưới các phép toán hợp, giao, bù, nối chuỗi, bao đóng sao, đảo chuỗi và đồng cấu."
---

> **Câu chuyện mở đầu:** Nếu bạn biết hai ngôn ngữ $$L_1, L_2$$ đều là ngôn ngữ chính quy, liệu hợp $$L_1 \cup L_2$$, giao $$L_1 \cap L_2$$, phần bù $$\overline{L_1}$$, hay đảo ngược $$L_1^R$$ có còn là ngôn ngữ chính quy không? Tin vui: **Lớp Ngôn ngữ Chính quy là lớp "bất khả xâm phạm" nhất trong Lý thuyết Tính toán** — nó đóng dưới **TẤT CẢ** các phép toán tập hợp và chuỗi cơ bản! Không chỉ giúp xây dựng ô-tô-mát phức tạp từ các mảnh nhỏ, **Tính đóng** còn là vũ khí tuyệt vời để chứng minh ngôn ngữ *không* chính quy chỉ trong 2 dòng!

<div class="textbook-epigraph" markdown="1">

"Closure proofs are constructions — and constructions are algorithms."

<span class="epigraph-attribution">— Automata as algebra</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** lớp ngôn ngữ chính quy đóng dưới các phép toán hợp, giao, bù, nối chuỗi và bao đóng sao.
- **Sử dụng** phép dựng ô-tô-mát tích (*product automaton*) để chứng minh tính đóng dưới phép giao.

</div>

## Kiến thức cần nhớ: Bảng Tính đóng & Kỹ thuật Ô-tô-mát Tích

### 1. Đóng dưới các Phép toán Biểu thức Chính quy (Hợp, Nối tiếp, Sao Kleene)
- **Bản chất:** Hiển nhiên ngay từ Định lý Kleene (hoặc ghép $$\varepsilon$$-NFA kiểu Thompson).

### 2. Đóng dưới Phần bù ($$\bar{L}$$) & Giao ($$L_1 \cap L_2$$) — Dùng DFA!
- **Phần bù (Complement):** Chỉ cần lấy **DFA đầy đủ** nhận $$L$$ rồi **đảo tập kết thúc** $$F \mapsto Q \setminus F$$! *(Cảnh báo chết người: KHÔNG ĐƯỢC đảo $$F$$ trực tiếp trên NFA vì một chuỗi có thể vừa có nhánh vào $$F$$ vừa có nhánh vào $$Q\setminus F$$!)*
- **Giao (Intersection) — Ô-tô-mát Tích (Product Construction):** Chạy đồng thời hai DFA $$M_1, M_2$$ trên cặp trạng thái $$(q_1, q_2) \in Q_1 \times Q_2$$ với $$\delta((q_1, q_2), a) = (\delta_1(q_1, a), \delta_2(q_2, a))$$ và $$F = F_1 \times F_2$$! (Đổi $$F$$ thành $$(F_1 \times Q_2) \cup (Q_1 \times F_2)$$ ra ngay phép Hợp; đổi thành $$F_1 \times (Q_2 \setminus F_2)$$ ra ngay phép Hiệu $$L_1 \setminus L_2$$!)

### 3. Đóng dưới Đảo ngược ($$L^R$$) & Đồng cấu Chuỗi (Homomorphism)
- **Đảo ngược:** Đảo chiều tất cả mũi tên của NFA, đổi trạng thái bắt đầu và kết thúc (thêm 1 trạng thái đầu mới nối $$\varepsilon$$ tới tất cả các $$F$$ cũ)!

## Ví dụ tính tay làm từng bước: Dùng Tính đóng chứng minh 2 dòng $$L = \{w : \#_0(w) = \#_1(w)\}$$ KHÔNG chính quy

Thay vì chật vật với nhiều trường hợp của Bổ đề Bơm trên $$L = \{w \in \{0, 1\}^* : \text{số bit 0 bằng số bit 1}\}$$, hãy dùng **Tính đóng dưới phép giao**:
1. Giả sử phản chứng $$L$$ là ngôn ngữ chính quy.
2. Ta biết rõ $$R = L(0^* 1^*)$$ là ngôn ngữ chính quy (mọi số `0` đứng trước mọi số `1`).
3. Vì lớp ngôn ngữ chính quy **đóng dưới phép giao**, nên giao của hai ngôn ngữ chính quy phải là ngôn ngữ chính quy:
   $$
   L \cap L(0^* 1^*) = \{0^n 1^n : n \ge 0\}.
   $$
4. Nhưng ta đã chứng minh ở bài 18.09 rằng $$\{0^n 1^n\}$$ **KHÔNG chính quy** $$\implies$$ **mâu thuẫn**! Vậy $$L$$ không phải ngôn ngữ chính quy!

### Giải thích: 4 ứng dụng thực chiến của Tính đóng & Ô-tô-mát Tích
#### Bước 1: Luôn chuyển sang DFA ĐẦY ĐỦ trước khi lấy Phần bù
Nếu bỏ sót trạng thái bẫy (dead state) rồi đảo $$F \mapsto Q\setminus F$$, kết quả sẽ sai hoàn toàn!

#### Bước 2: Dùng Ô-tô-mát Tích để giải mọi bài toán "Thỏa ĐỒNG THỜI 2 điều kiện"
Ví dụ: nhận chuỗi vừa có chẵn bit `0` (DFA 2 trạng thái) vừa chia hết cho 3 (DFA 3 trạng thái) $$\implies$$ DFA tích có đúng $$2 \times 3 = 6$$ trạng thái!

#### Bước 3: Dùng tính đóng dưới Phép Giao để kiểm tra tương đương hai DFA
Hai DFA $$M_1, M_2$$ nhận cùng ngôn ngữ $$\iff (L_1 \setminus L_2) \cup (L_2 \setminus L_1) = \emptyset$$ — kiểm tra được tự động bằng thuật toán duyệt đồ thị BFS từ trạng thái khởi đầu của DFA tích!

#### Bước 4: Đòn "Mượn dao giết người" chứng minh Không chính quy
Khi gặp ngôn ngữ khó tách $$y$$ bằng Bổ đề Bơm, hãy lấy **phần bù** hoặc **giao** với một Regex khéo chọn (như $$0^*1^*$$) để rút gọn về đúng ngôn ngữ kinh điển $$\{0^n 1^n\}$$!

$$
L_1, L_2 \text{ chính quy}
\;\Longrightarrow\;
L_1 \cup L_2,\; L_1 \cap L_2,\; \overline{L_1},\; L_1 \setminus L_2,\; L_1^R \text{ đều chính quy!}
$$

## Định lý tính đóng

<div class="textbook-theorem" markdown="1">

**Định lý.** Lớp các ngôn ngữ chính quy đóng dưới các phép toán hợp ($$\cup$$), giao ($$\cap$$), lấy bù, nối chuỗi, bao đóng Kleene ($$*$$) và đảo chuỗi (*reverse*).

</div>

Ta chứng minh bằng các phép dựng tường minh sau:

- **Phép bù:** trên DFA toàn phần nhận $$L$$, chỉ cần đổi tập trạng thái kết thúc từ $$F$$ sang $$Q \setminus F$$.
- **Phép giao:** có thể suy từ định luật De Morgan $$L_1\cap L_2=\overline{\overline{L_1}\cup\overline{L_2}}$$, hoặc dựng trực tiếp ô-tô-mát tích với $$\delta((p,q),a)=(\delta_1(p,a),\delta_2(q,a))$$ và $$F=F_1\times F_2$$.
- **Phép hợp:** dùng ô-tô-mát tích với $$F=(F_1\times Q_2)\cup(Q_1\times F_2)$$, hoặc ghép hai NFA bằng trạng thái đầu mới có cạnh ε.
- **Phép nối và bao đóng sao:** dựng trực tiếp bằng ε-NFA theo kiểu Thompson.
- **Phép đảo chuỗi (*reverse*):** đảo chiều tất cả các cạnh của NFA, biến trạng thái đầu cũ thành trạng thái kết thúc mới và thêm một trạng thái đầu mới nối cạnh ε tới mọi trạng thái thuộc $$F$$ cũ. $$\square$$

## Ô-tô-mát tích — chứng minh phép giao

Với ô-tô-mát tích của hai DFA $$M_1$$ và $$M_2$$, ta có bất biến: sau khi đọc chuỗi $$w$$, máy tích ở trạng thái $$(p,q)$$ khi và chỉ khi $$w$$ đưa $$M_1$$ đến $$p$$ và đưa $$M_2$$ đến $$q$$. Vì $$F = F_1 \times F_2$$, chuỗi $$w$$ được chấp nhận khi và chỉ khi nó được chấp nhận bởi cả hai máy. $$\square$$

## Bài tập

1. Dựng chi tiết ô-tô-mát tích cho hai DFA gồm 2 trạng thái.
2. Trình bày chứng minh đầy đủ cho tính đóng dưới phép đảo chuỗi (*reverse*).
3. Phát biểu tính đóng dưới phép đồng cấu (*homomorphism*) và nêu ý tưởng chứng minh.

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman.

## Tóm tắt

Tính đóng của ngôn ngữ chính quy được chứng minh trực tiếp bằng các phép dựng trên ô-tô-mát như lật tập trạng thái kết thúc $$F$$, dựng ô-tô-mát tích và ghép nối bằng cạnh ε.

**Bài tiếp theo:** Định lý Myhill–Nerode và tối tiểu hóa DFA.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=6aRJQNYYz4s">Operations on Regular Languages</a> — Neso Academy, tiếng Anh. Giới thiệu các phép hợp, nối và lặp sao trên ngôn ngữ chính quy.
- <a href="https://www.youtube.com/watch?v=WrzaPNj9OZ4">Regular Languages</a> — Neso Academy, tiếng Anh. Ôn lại khái niệm ngôn ngữ chính quy trước khi xét các tính chất đóng.
- <a href="https://www.youtube.com/watch?v=nX4JrcHgpZY">Equivalence of Two Finite Automata</a> — Neso Academy, tiếng Anh. Kiểm tra sự tương đương của hai ô-tô-mát hữu hạn sau khi áp dụng các phép dựng.
