---
layout: post
title: "Tính Đóng của Ngôn ngữ Chính quy"
categories: chapter18
date: 2021-01-01
order: 10
required: true
lang: en
excerpt: "Chứng minh đóng: hợp, giao, bù, ghép, star, reverse, homomorphism."
---


<div class="textbook-epigraph" markdown="1">

"Closure proofs are constructions — and constructions are algorithms."

<span class="epigraph-attribution">— Automata as algebra</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** đóng dưới ∪, ∩, bù, ·, *.
- **Dùng** product automaton cho giao.

</div>

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý.** Lớp regular đóng với ∪, ∩, bù, ghép, *, reverse.

</div>

**Bù:** DFA lật $$F$$ (total δ).  
**Giao:** $$L_1\cap L_2=\overline{\overline{L_1}\cup\overline{L_2}}$$ hoặc product:  
$$\delta((p,q),a)=(\delta_1(p,a),\delta_2(q,a))$$, $$F=F_1\times F_2$$.  
**Hợp:** product $$F=(F_1\times Q_2)\cup(Q_1\times F_2)$$ hoặc NFA ε.  
**Ghép/*:** ε-NFA Thompson-style.  
**Reverse:** đảo cạnh NFA, start↔accept (ε từ new start tới mọi old F). $$\square$$

## Product — chứng minh giao

Bất biến: sau $$w$$ ở $$(p,q)$$ ⇔ $$w$$ đưa $$M_1$$ tới $$p$$ và $$M_2$$ tới $$q$$.  
Chấp nhận ⇔ cả hai accept. $$\square$$

## Bài tập

1. Product chi tiết cho hai DFA 2 trạng thái.  
2. Chứng minh đóng reverse.  
3. Homomorphism: phát biểu + ý chứng minh.

## Đọc

Sipser; Hopcroft.

## Tóm tắt

Product · lật F · ε-ghép.

**Tiếp:** Myhill–Nerode.
