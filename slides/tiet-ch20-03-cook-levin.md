---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Cook–Levin & Rút gọn Cổ điển

**Chương 20 · Bài 20.3** · Seminar NCS

---

## Mục tiêu chứng minh

SAT NPC  
SAT ≤ₚ 3SAT  
3SAT ≤ₚ IS  
IS ≡ CLIQUE  
IS ≤ₚ VC

---

## Cook–Levin — ý

$$L\in NP$$ · verifier / TM thời gian $$T$$

Tableau $$T\times T$$ → biến Boole  
CNF local → $$\varphi_x$$

$$x\in L \Leftrightarrow \varphi_x\in\mathrm{SAT}$$

---

## Nhóm mệnh đề

G1 khởi tạo  
G2 uniqueness  
G3 chuyển $$\delta$$  
G4 chấp nhận

Số biến $$O(T^2)$$

---

## SAT → 3SAT

$$\lvert C\rvert=1,2$$: pad biến phụ  

$$\lvert C\rvert\ge 4$$: chuỗi

$$(\ell_1\lor\ell_2\lor y_1)\land(\neg y_1\lor\ell_3\lor y_2)\land\cdots$$

---

## 3SAT → IS

Đỉnh: literal trong mệnh đề  

Tam giác mỗi mệnh đề  
Cạnh mâu thuẫn $$\ell$$ — $$\neg\ell$$  

$$k=m$$

---

## IS ↔ CLIQUE

$$\overline{G}$$: bù  

IS trong $$G$$ ⇔ clique trong $$\overline{G}$$

---

## IS → VC

$$S$$ IS ⇔ $$V\setminus S$$ cover  

$$(G,k)\mapsto(G,n-k)$$

---

## HC → TSP-DEC

$$w=1$$ nếu cạnh có  
$$w=2$$ nếu không  

Tour ≤ $$n$$ ⇔ Hamilton

---

## Checklist hardness proof

1. ∈ NP (certificate)  
2. A ≤ₚ B với A đã NPC  
3. Tính đúng Yes ↔ Yes  
4. $$f$$ poly-time

---

## Đọc

Sipser · Arora–Barak §2  
Garey–Johnson  
CLRS NPC chapter
