---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## NFA & Tương đương DFA

**Toán Rời Rạc** · Chương 18 · Bài 18.3

---

## NFA

$$\delta:Q\times\Sigma\to\mathcal{P}(Q)$$

Chấp nhận: **tồn tại** đường tới $$F$$

---

## Hình

![NFA](../img/course/Automata_nfa_ends_01.svg)

---

## Subset construction

Trạng thái DFA = tập con NFA

$$\delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a)$$

$$\le 2^{|Q|}$$ trạng thái

---

## Hình

![Subset](../img/course/Automata_subset_construction.svg)

---

## Kết luận

NFA gọn khi thiết kế  
DFA chắc khi chạy  
**Cùng** lớp regular

**Sau**: regex · Kleene
