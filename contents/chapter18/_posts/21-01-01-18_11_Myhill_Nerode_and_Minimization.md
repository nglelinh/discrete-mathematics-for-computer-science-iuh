---
layout: post
title: "Myhill–Nerode và DFA Tối tiểu"
categories: chapter18
date: 2021-01-01
order: 11
required: true
lang: en
excerpt: "Quan hệ ~L; định lý MN; chứng minh không regular; thuật toán minimize."
---


<div class="textbook-epigraph" markdown="1">

"The number of states you need is the number of distinguishable futures."

<span class="epigraph-attribution">— Myhill–Nerode</span>

</div>

Công cụ **mạnh hơn pumping** cho lower bound số trạng thái và tính không regular.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** $$x\sim_L y$$.
- **Phát biểu** Myhill–Nerode.
- **Áp dụng** chứng minh không regular / bound DFA.

</div>

## 1. Quan hệ

<div class="textbook-definition" markdown="1">

$$x\sim_L y$$ iff $$\forall z\in\Sigma^*$$: $$xz\in L\Leftrightarrow yz\in L$$.

</div>

Tương đương; lớp $$[x]$$.

## 2. Định lý

<div class="textbook-theorem" markdown="1">

**Định lý (Myhill–Nerode).** $$L$$ regular ⇔ số lớp $$~\sim_L$$ hữu hạn.  
Khi đó DFA tối tiểu có đúng số lớp đó (mỗi lớp một trạng thái).

</div>

**Ý chứng minh.**  
⇒: trạng thái $$\hat\delta(q_0,x)$$ refine $$~\sim_L$$ (cùng trạng thái ⇒ cùng tương lai).  
⇐: DFA các lớp; $$\delta([x],a)=[xa]$$ well-defined; $$F=\{[x]:x\in L\}$$. $$\square$$

## 3. Ứng dụng

$$0^n1^n$$: $$0^i\not\sim 0^j$$ ($$z=1^i$$) ⇒ vô hạn lớp ⇒ không regular.

## 4. Minimize DFA

Table-filling / partition refinement: gộp trạng thái không phân biệt — $$O(n\log n)$$ Hopcroft.

## Bài tập

1. Chứng minh $$~\sim_L$$ tương đương.  
2. Số lớp của “chẵn số 1”.  
3. $$\{a^ib^jc^k:i=j\text{ or }j=k\}$$ — MN hay pump?

## Đọc

Sipser (optional MN); Hopcroft minimization; Kozen.

## Tóm tắt

Phân biệt tương lai · DFA tối tiểu · lower bound.

**Tiếp:** máy Turing.
