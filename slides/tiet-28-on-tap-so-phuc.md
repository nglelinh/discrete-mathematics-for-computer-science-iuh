---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Ôn tập — Số phức

**Toán Rời Rạc**

Tiết 28 (45 phút) — Ôn số phức (phục vụ HTTH)

---

## Mục tiêu tiết học

- Ôn **dạng đại số** $$z=a+bi$$, liên hợp, modulus
- Tính **argument** đúng (kể cả góc **không** bội của $$\pi$$)
- Chuyển **cực / mũ**; **De Moivre**
- Giải **PT bậc 2** có nghiệm phức
- **Cầu nối** HTTH: $$r^{n}\to\rho^{n}(A\cos n\theta+B\sin n\theta)$$

---

## Vì sao số phức?

Khi phương trình đặc trưng có nghiệm $$r=\alpha\pm i\beta$$:

$$
r^{n}=\rho^{n}(\cos n\theta+i\sin n\theta)
$$

→ dãy thực: $$\rho^{n}(A\cos n\theta+B\sin n\theta)$$.

Thường $$\theta=\arctan(\beta/\alpha)$$ **không** rút gọn thành bội đẹp của $$\pi$$.

---

## Số phức — công thức cốt lõi

| Khái niệm | Công thức |
|:---|:---|
| Đại số | $$z = a + bi$$, $$i^{2}=-1$$ |
| Liên hợp | $$\bar z = a - bi$$ |
| Modulus | $$\rho=\lvert z\rvert=\sqrt{a^{2}+b^{2}}$$ |
| Argument | $$\theta=\arg(z)\in(-\pi,\pi]$$ |

---

## Dạng cực, mũ và De Moivre

| Dạng | Công thức |
|:---|:---|
| Cực | $$z=\rho(\cos\theta+i\sin\theta)$$ |
| Mũ | $$z=\rho e^{i\theta}$$ |
| De Moivre | $$z^{n}=\rho^{n}(\cos n\theta+i\sin n\theta)$$ |
| Nhân / chia | $$\rho_1\rho_2$$, $$\theta_1\pm\theta_2$$ |


---

## Đại số

1. $$z=4-3i$$: $$\bar z$$, $$\rho$$, $$\theta$$ (arctan?)

2. $$z_1=2+i$$, $$z_2=1-3i$$: $$z_1+z_2$$, $$z_1 z_2$$

3. $$z=-3-i$$: xác định góc phần tư + công thức $$\theta$$

---

## Đáp án nhanh — đại số

1. $$4+3i$$, $$\rho=5$$, $$\theta=-\arctan\frac{3}{4}$$
2. Tổng $$3-2i$$; tích $$2-6i+i-3i^{2}=5-5i$$
3. Phần tư III: $$\theta=-\pi+\arctan\frac{1}{3}$$  
   

---


## Góc không bội của $$\pi$$

Nhiều số phức **không** có $$\theta=k\pi/n$$ đẹp.

**Cách làm:**

1. Tính $$\rho=\sqrt{a^{2}+b^{2}}$$ (có thể để căn)
2. $$\theta=\arg(a+bi)$$ bằng **arctan + góc phần tư**
3. Giữ $$\theta=\arctan(\ldots)$$ hoặc viết gần đúng nếu cần

**Ví dụ khung:** $$z=3+2i$$  
$$\rho=\sqrt{13}$$, $$\theta=\arctan(2/3)$$ (góc phần tư I)  


---

## Ví dụ — góc không bội $$\pi$$ (1)

Cho $$z=3+2i$$.

1. $$\bar z$$, $$\rho$$, $$\theta$$ (để arctan)
2. Dạng cực: $$\sqrt{13}\bigl(\cos\theta+i\sin\theta\bigr)$$, $$\theta=\arctan\frac{2}{3}$$
3. $$z^{2}$$ bằng đại số: $$(3+2i)^{2}=5+12i$$

---

## So sánh 2 cách nhân và mũ

Cho $$z=1+i$$: $$\rho=\sqrt{2}$$, $$\theta=\dfrac{\pi}{4}$$.

| Cách | Tính $$z^{2}$$ |
|:---|:---|
| **Đại số** | $$(1+i)^{2}=1+2i+i^{2}=2i$$ |
| **Cực / De Moivre** | $$\rho^{2}=2$$, $$2\theta=\dfrac{\pi}{2}$$ → $$2\bigl(\cos\frac{\pi}{2}+i\sin\frac{\pi}{2}\bigr)=2i$$ |

Hai cách **trùng** $$2i$$. Góc đẹp: bội của $$\pi$$.

---

## Ví dụ — góc không bội $$\pi$$ (2)

$$z=-2+5i$$ (góc phần tư **II**).

1. $$\rho=\sqrt{4+25}=\sqrt{29}$$
2. $$\theta=\pi-\arctan\frac{5}{2}$$  
   (hoặc $$\operatorname{atan2}(5,-2)$$)
3. Viết dạng mũ: $$\sqrt{29}\, e^{i\theta}$$

---

## Đáp án — $$-2+5i$$

- $$\rho=\sqrt{29}$$
- $$\theta=\pi-\arctan\frac{5}{2}\in(\pi/2,\pi)$$
- $$z=\sqrt{29}\bigl(\cos\theta+i\sin\theta\bigr)=\sqrt{29}\, e^{i\theta}$$

Kiểm: $$\operatorname{Re}<0$$, $$\operatorname{Im}>0$$ → đúng phần tư II.

---

## Ví dụ — góc không bội $$\pi$$ (3)

$$z=1-4i$$ (phần tư **IV**).

1. $$\rho=\sqrt{1+16}=\sqrt{17}$$
2. $$\theta=-\arctan 4$$ (âm)
3. Tính $$z\cdot\bar z$$ và $$1/z$$

---

## Đáp án — $$1-4i$$

1. $$\rho=\sqrt{17}$$, $$\theta=-\arctan 4$$
2. $$z\bar z=\rho^{2}=17$$
3. $$\displaystyle\frac{1}{z}=\frac{\bar z}{\lvert z\rvert^{2}}=\frac{1+4i}{17}$$

---

## Cực & De Moivre — luyện

(a) Viết cực/mũ: $$3+2i$$, $$-2+5i$$  
(b) $$(3+2i)^{2}$$ bằng De Moivre (đã có)  
(c) $$z_1=\sqrt{13}\, e^{i\arctan(2/3)}$$, $$z_2=2 e^{i\pi/6}$$: $$z_1 z_2$$ (để $$\theta$$ dạng tổng)

---

## Đáp án — cực / De Moivre

(a) Như các slide ví dụ  
(b) $$5+12i$$  
(c) $$\rho=2\sqrt{13}$$,  
$$\theta=\arctan\frac{2}{3}+\frac{\pi}{6}$$  
(không rút gọn thêm — **đúng** khi không “đẹp”)

---

## PT bậc 2 — nghiệm phức

$$az^{2}+bz+c=0\quad (a\neq 0)$$

$$\Delta=b^{2}-4ac$$

| $$\Delta$$ | Nghiệm |
|:---|:---|
| $$>0$$ | hai nghiệm thực phân biệt |
| $$=0$$ | nghiệm kép thực |
| $$<0$$ | hai nghiệm **phức liên hợp** |

$$
z=\frac{-b\pm\sqrt{\Delta}}{2a}
$$

Khi $$\Delta<0$$: $$\sqrt{\Delta}=i\sqrt{\lvert\Delta\rvert}$$.

---

## PT bậc 2 — công thức phức

$$\Delta<0$$: đặt $$D=\lvert\Delta\rvert=-\Delta$$

$$
z=\frac{-b}{2a}\pm i\,\frac{\sqrt{D}}{2a}
$$

Cặp $$z$$, $$\bar z$$ nếu $$a,b,c\in\mathbb{R}$$.

**Liên hệ HTTH:** phương trình đặc trưng bậc 2 thường cho đúng cặp này.

---

## Ví dụ PT — $$\Delta<0$$ (1)

$$z^{2}-2z+5=0$$

1. $$\Delta=4-20=-16$$
2. $$z=\dfrac{2\pm 4i}{2}=1\pm 2i$$
3. Với $$r=1+2i$$: $$\rho=\sqrt{5}$$, $$\theta=\arctan 2$$  
   (**không** phải $$\pi/3$$!)

---

## Đáp án — $$z^{2}-2z+5=0$$

- Nghiệm: $$1+2i$$, $$1-2i$$
- $$\rho=\sqrt{1+4}=\sqrt{5}$$
- $$\theta=\pm\arctan 2$$
- Dạng HTTH (nếu là nghiệm đặc trưng):

$$
a_n=(\sqrt{5})^{n}\bigl(A\cos(n\theta)+B\sin(n\theta)\bigr),\quad \theta=\arctan 2
$$

---

## Ví dụ PT — $$\Delta<0$$ (2)

$$z^{2}+2z+2=0$$

$$\Delta=4-8=-4$$

$$
z=\frac{-2\pm 2i}{2}=-1\pm i
$$

$$\rho=\sqrt{2}$$, $$\theta=\pm\frac{3\pi}{4}$$ (góc “đẹp” — so sánh với ví dụ 1).

---

## Ví dụ PT — hệ số “xấu” (3)

$$2z^{2}-2z+1=0$$

$$\Delta=4-8=-4$$

$$
z=\frac{2\pm 2i}{4}=\frac{1}{2}\pm\frac{1}{2}i
$$

$$\rho=\sqrt{\frac{1}{4}+\frac{1}{4}}=\frac{\sqrt{2}}{2}$$,  
$$\theta=\pm\arctan 1=\pm\frac{\pi}{4}$$.

---

## Ví dụ PT — arctan không bội đẹp (4)

$$z^{2}-4z+13=0$$

$$\Delta=16-52=-36$$

$$
z=\frac{4\pm 6i}{2}=2\pm 3i
$$

$$\rho=\sqrt{4+9}=\sqrt{13}$$,  
$$\theta=\pm\arctan\frac{3}{2}$$  
— **không** chia hết / không bội đơn giản của $$\pi$$.

---

## Đáp án — $$2\pm 3i$$ → HTTH

Nếu đặc trưng cho $$r=2+3i$$:

$$
a_n=(\sqrt{13})^{n}\Bigl(A\cos\bigl(n\arctan\tfrac{3}{2}\bigr)+B\sin\bigl(n\arctan\tfrac{3}{2}\bigr)\Bigr)
$$

Hoặc giữ $$\theta=\arctan\frac{3}{2}$$ và viết $$n\theta$$.

---

## Làm tại lớp — PT bậc 2

Giải và viết $$\rho$$, $$\theta$$ (arctan nếu cần):

1. $$z^{2}+4=0$$
2. $$z^{2}-2z+2=0$$
3. $$z^{2}+z+1=0$$ (gợi ý: căn đơn vị bậc 3)
4. $$z^{2}-6z+13=0$$

---

## Đáp án — PT tại lớp

1. $$z=\pm 2i$$; $$\rho=2$$, $$\theta=\pm\pi/2$$
2. $$1\pm i$$; $$\rho=\sqrt{2}$$, $$\theta=\pm\pi/4$$
3. $$z=\dfrac{-1\pm i\sqrt{3}}{2}$$; $$\rho=1$$, $$\theta=\pm\frac{2\pi}{3}$$
4. $$3\pm 2i$$; $$\rho=\sqrt{13}$$, $$\theta=\pm\arctan\frac{2}{3}$$

---

## Cầu nối HTTH

Cho nghiệm đặc trưng $$r=2+3i$$ (và liên hợp).

1. $$\rho$$, $$\theta$$ (arctan!)
2. $$r^{n}$$ dạng sin–cos
3. Dạng dãy thực $$a_n$$

---

## Đáp án — cầu nối

1. $$\rho=\sqrt{13}$$, $$\theta=\arctan\frac{3}{2}$$
2. $$r^{n}=(\sqrt{13})^{n}\bigl(\cos n\theta+i\sin n\theta\bigr)$$
3. $$a_n=(\sqrt{13})^{n}(A\cos n\theta+B\sin n\theta)$$
---

## Checklist

1. $$a+bi$$  
2. $$\rho$$, $$\theta$$ (arctan + phần tư)  
3. Cực / mũ / De Moivre  
4. PT bậc 2: $$\Delta$$ → nghiệm  
5. HTTH: $$\rho^{n}(A\cos n\theta+B\sin n\theta)$$

---

## Bài tập về nhà (1/2)

1. $$z=-3+5i$$: $$\rho$$, $$\theta$$ (công thức arctan + phần tư).
2. $$(2+i)^{3}$$ — khai triển đại số **và** De Moivre ($$\theta=\arctan\frac12$$).
3. Giải $$z^{2}-2z+10=0$$; viết $$\rho$$, $$\theta$$ của nghiệm.

---

## Bài tập về nhà (2/2)

4. $$z^{2}+4z+13=0$$ → nghiệm; dạng $$a_n$$ nếu đây là đặc trưng.
5. Giải thích vì sao $$\arctan 2\neq \pi/3$$ (so sánh $$\tan(\pi/3)=\sqrt{3}\approx 1{,}73$$).
6. (Tuỳ chọn) Căn bậc 2 của $$3+4i$$ (dạng đại số hoặc cực).

---

## Tiết sau

**Tiết 29** — Ôn tập hệ thức truy hồi  
(phân loại → thuần nhất → không thuần nhất → cộng hưởng)

---

## Câu hỏi?
