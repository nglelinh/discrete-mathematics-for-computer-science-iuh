---
layout: post
title: "Định lý Cook–Levin (Tableau)"
categories: chapter20
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Chứng minh SAT NP-complete: biến tableau, mệnh đề G1–G4, tính đúng rút gọn L≤ₚSAT."
---

<div class="textbook-epigraph" markdown="1">

"Every efficient verification becomes a Boolean formula."

<span class="epigraph-attribution">— Cook–Levin</span>

</div>

Đây là **định lý trung tâm** mở ngành NPC: mọi $$L\in NP$$ rút gọn về **SAT**.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Chứng minh** $$\mathrm{SAT}\in NP$$.
- **Xây** tableau và các nhóm mệnh đề.
- **Chứng minh** $$L\le_p\mathrm{SAT}$$ cho $$L\in NP$$ tùy ý.

</div>

## 1. $$\mathrm{SAT}\in NP$$

Certificate = gán chân trị. Verifier đánh giá công thức: thời gian tuyến tính theo $$\lvert\varphi\rvert$$. $$\square$$

## 2. Từ verifier/TM đến CNF

Cho $$L\in NP$$, verifier/TM $$M$$ thời gian $$T=N^{O(1)}$$ trên $$z=\langle x,c\rangle$$ độ dài $$N$$. Cửa sổ băng $$[-T,T]$$.

### Biến

- $$C_{t,i,a}$$: ô $$i$$ lúc $$t$$ chứa $$a$$.  
- $$H_{t,i}$$: đầu ở $$i$$ lúc $$t$$.  
- $$Q_{t,q}$$: trạng thái $$q$$ lúc $$t$$.  

Số biến $$O(T^2)$$.

### Mệnh đề (CNF local)

**G1 Khởi tạo** $$t=0$$: băng = $$z$$, blank ngoài, đầu 0, $$q_0$$.  
**G2 Uniqueness:** đúng một trạng thái / một đầu / một ký hiệu mỗi ô.  
**G3 Transition:**  
- đầu không ở $$i$$ ⇒ ô $$i$$ không đổi;  
- đầu ở $$i$$, $$(q,a)\mapsto(q',b,D)$$ ⇒ cập nhật $$q',b$$, đầu mới.  
$$X\Rightarrow Y$$ thành $$\neg X\lor Y$$; phân phối hội trong $$X$$.  
**G4 Accept:** $$\bigvee_t Q_{t,q_A}$$.

### Tính đúng

Chạy thật $$M$$ ⇒ gán transcript thỏa $$\varphi_z$$.  
Gán thỏa ⇒ tableau = chạy hợp lệ + accept.  
$$z\mapsto\varphi_z$$ poly-time.

Vậy $$L\le_p\mathrm{SAT}$$. Kết hợp §1: **SAT NP-complete**. $$\square$$

## 3. Ghi chú viết paper

Thường viết: “by the standard tableau construction (Sipser / Arora–Barak)”.  
Seminar: phải tường minh G1–G4.

## Bài tập

1. Ước số biến nếu $$T=n^3$$, $$\lvert\Gamma\rvert=10$$.  
2. Viết CNF cho “đúng một trong $$x_1,x_2,x_3$$”.  
3. Đối chiếu cửa sổ Sipser vs Arora–Barak (1 trang).

## Đọc

**Sipser** Cook–Levin; **Arora–Barak** §2; Cook STOC 1971.

## Tóm tắt

Tableau $$O(T^2)$$ · local gates · SAT NPC.

**Tiếp:** 20.8 — SAT→3SAT.
