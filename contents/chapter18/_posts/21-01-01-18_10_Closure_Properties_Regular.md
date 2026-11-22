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

<div class="textbook-epigraph" markdown="1">

"Closure proofs are constructions — and constructions are algorithms."

<span class="epigraph-attribution">— Automata as algebra</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** lớp ngôn ngữ chính quy đóng dưới các phép toán hợp, giao, bù, nối chuỗi và bao đóng sao.
- **Sử dụng** phép dựng ô-tô-mát tích (*product automaton*) để chứng minh tính đóng dưới phép giao.

</div>

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
