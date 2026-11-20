---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hệ thức Truy hồi Không thuần nhất

**Toán Rời Rạc**

Tiết 26 (45 phút) — ch10 `10_03`

---

## Mục tiêu tiết học

- Nhận dạng HTTH **không thuần nhất** $$+f(n)$$
- Áp dụng **nguyên lý chồng chất** $$a=a^{(h)}+a^{(p)}$$
- **Hệ số bất định** cho hằng / đa thức / $$b^{n}$$
- **Cộng hưởng** (kể cả $$a_n-a_{n-1}=n^{2}$$)
- Ví dụ giáo trình: $$2x+1$$, $$+3^{n}$$ (bậc 2), $$+n^{2}$$

---

## Dạng tổng quát

**Tuyến tính không thuần nhất bậc k**:

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k} + f(n)$$

**Thuần nhất liên kết** (homogeneous):

$$a_n^{(h)}: \quad a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k}$$

**Khác biệt**: thêm tác động ngoài $$f(n)$$

---

## Nguyên lý chồng chất

**Nghiệm tổng quát**:

$$a_n = a_n^{(h)} + a_n^{(p)}$$

- $$a_n^{(h)}$$: nghiệm tổng quát phần **thuần nhất**
- $$a_n^{(p)}$$: một **nghiệm riêng** (particular solution)

---

## Chứng minh $$a = a^{(p)}+a^{(h)}$$

$$L(a)_n = a_n - c_1 a_{n-1}-\cdots-c_k a_{n-k}$$

$$L(a^{(p)})=f$$. Mọi nghiệm $$b$$: $$L(b)=f$$.

$$L(b-a^{(p)})=0$$ → $$b-a^{(p)}$$ là nghiệm **thuần nhất**.

$$\Rightarrow b = a^{(p)}+a^{(h)}$$.

---

## Bảng hệ số bất định

| $$f(n)$$ | Dạng thử $$a_n^{(p)}$$ |
|----------|------------------------|
| Hằng $$d$$ | $$A$$ |
| Đa thức bậc $$m$$ | $$B_0 + B_1 n + \cdots + B_m n^{m}$$ |
| $$b^{n}$$ | $$A b^{n}$$ |
| $$n^{m} b^{n}$$ | $$(B_0 + \cdots + B_m n^{m})\, b^{n}$$ |

**Quy tắc cộng hưởng**: nếu dạng thử trùng nghiệm thuần nhất → nhân thêm $$n$$ (hoặc $$n^{s}$$) đủ lần.

---

## Ví dụ 1: $$f(n) = d$$ (hằng)

$$a_n = 2a_{n-1} + 3, \quad a_0 = 1$$

**Thuần nhất**: $$a_n^{(h)} = C \cdot 2^{n}$$

**Nghiệm riêng**: thử $$A$$ → $$A = 2A + 3$$ → $$A = -3$$

$$a_n = C \cdot 2^{n} - 3$$. Từ $$a_0=1$$: $$C - 3 = 1$$ → $$C = 4$$.

$$a_n = 4 \cdot 2^{n} - 3$$. Kiểm tra: $$a_1 = 8 - 3 = 5 = 2(1)+3$$ ✓

---

## Ví dụ 2: $$f(n) = n$$ (đa thức)

$$a_n = a_{n-1} + n, \quad a_0 = 0$$

**Thuần nhất**: $$a_n^{(h)} = C$$ (đặc trưng $$r-1=0$$)

---

**Nghiệm riêng**: thử $$A n^{2} + B n$$ (bậc 1 → thử bậc 2 vì $$f(n)=n$$ và $$c=1$$ và $r=1$ là nghiệm của phương trình đặc trưng nên phải **nhân thêm $n$**:

$$A n^{2} + B n = A(n-1)^{2} + B(n-1) + n$$

→ $$A = \frac12$$, chọn $$B = \frac12$$ → $$a_n^{(p)} = \frac{n(n+1)}{2}$$

**Tổng Gauss**: $$1+2+\cdots+n = \frac{n(n+1)}{2}$$.

---

## Ví dụ 3: $$f(n) = 2n + 1$$

$$a_n = 2a_{n-1} + 2n + 1, \quad a_0 = 2$$

**Thuần nhất**: $$a_n^{(h)} = A \cdot 2^{n}$$

---

**Nghiệm riêng**: thử $$B_0 + B_1 n$$:

$$B_0 + B_1 n = 2(B_0 + B_1(n-1)) + 2n + 1$$

→ $$B_1 = -3$$, $$B_0 = -7$$ → $$a_n^{(p)} = -3n - 7$$

$$a_n = A \cdot 2^{n} - 3n - 7$$. Từ $$a_0=2$$: $$A = 9$$.

$$a_n = 9 \cdot 2^{n} - 3n - 7$$.

---

## Cộng hưởng (Resonance)

$$a_n = 2a_{n-1} + 2^{n}$$

**Thuần nhất**: $$a_n^{(h)} = C \cdot 2^{n}$$ (đặc trưng $$r=2$$)

---

Thử $$A \cdot 2^{n}$$ → **trùng** nghiệm thuần nhất → thử $$A \cdot n \cdot 2^{n}$$:

$$A n 2^{n} = 2 A (n-1) 2^{n-1} + 2^{n}$$

→ $$A n = A(n-1) + 1$$ → $$A = 1$$ → $$a_n^{(p)} = n \cdot 2^{n}$$.

$$a_n = (C + n) 2^{n}$$. Xác định $$C$$ từ điều kiện đầu.

---

## Tháp Hà Nội / $$x_n=2x_{n-1}+1$$

$$H_n = 2H_{n-1} + 1, \quad H_1 = 1$$

**Thuần nhất**: $$A\cdot 2^{n}$$

**Riêng hằng**: $$K=2K+1\Rightarrow K=-1$$

$$H_n=A\cdot 2^{n}-1$$, $$H_1=1\Rightarrow A=1$$

$$\boxed{H_n = 2^{n} - 1}$$
(dãy 1, 3, 7, 15, …)

---

## Ví dụ: $$a_n = 3a_{n-1} + 2$$

$$a_n^{(h)} = A \cdot 3^{n}$$, riêng $$K$$: $$K=3K+2\Rightarrow K=-1$$.

$$a_0=1\Rightarrow A=2$$ → $$a_n = 2\cdot 3^{n}-1$$.

---

## Tổng bình phương (cộng hưởng đa thức)

$$a_n = a_{n-1} + n^{2},\quad a_0=0$$

($$a_n=1^{2}+\cdots+n^{2}$$)

Thuần nhất: $$C$$ ($$r=1$$).  
$$f=n^{2}$$ → phải thử **bậc 3**: $$n(qn^{2}+sn+t)$$.

$$\boxed{a_n=\dfrac{n(n+1)(2n+1)}{6}}$$

---

## Bậc 2 + $$3^{n}$$ (giáo trình)

$$X_n=2X_{n-1}-X_{n-2}+3^{n},\quad X_0=1,X_1=3$$

**Thuần nhất**: $$(r-1)^{2}=0$$ → $$A+Bn$$

**Riêng**: $$C\cdot 3^{n}$$

$$C\cdot 3^{n}=2C\cdot 3^{n-1}-C\cdot 3^{n-2}+3^{n}$$

$$\Rightarrow 4C=9\Rightarrow C=\dfrac{9}{4}$$

---

## Bậc 2 + $$3^{n}$$ — Điều kiện đầu

$$X_n=A+Bn+\dfrac{9}{4}\,3^{n}$$

$$n=0$$: $$A+\dfrac{9}{4}=1\Rightarrow A=-\dfrac{5}{4}$$

$$n=1$$: $$A+B+\dfrac{27}{4}=3\Rightarrow B=-\dfrac{5}{2}$$

$$\boxed{X_n=-\dfrac{5}{4}-\dfrac{5}{2}n+\dfrac{9}{4}\,3^{n}}$$

Kiểm $$n=2$$: truy hồi $$14$$; công thức $$14$$ ✓

---

## Bậc 2 + $$n^{2}$$ (phác)

$$a_n=2a_{n-1}+a_{n-2}+n^{2}$$

Thuần nhất: $$r=1\pm\sqrt{2}$$

$$a_n^{(h)}=C_1(1+\sqrt{2})^{n}+C_2(1-\sqrt{2})^{n}$$

Riêng thử $$An^{2}+Bn+C$$:

$$A=-\tfrac12,\ B=-2,\ C=-\tfrac52$$

(+ $$C_1,C_2$$ từ ĐKĐ)

---

## Thực hành 1

Giải $$a_n = 2a_{n-1} + n$$, $$a_0 = 1$$.

Gợi ý: thử $$a_n^{(p)} = An + B$$.

---

## Thực hành 2

$$x_n=2x_{n-1}+1$$, $$x_1=1$$  
(viết đóng + $$x_5$$)

---

## Thực hành 3

$$a_n=a_{n-1}+n^{2}$$, $$a_0=0$$  
(công thức tổng $$k^{2}$$)

---

## Thực hành 4

$$X_n=2X_{n-1}-X_{n-2}+3^{n}$$, $$X_0=1,X_1=3$$

---

## Tóm tắt Tiết 26

- $$a_n=a_n^{(h)}+a_n^{(p)}$$ (mọi nghiệm)
- Hệ số bất định theo họ $$f(n)$$
- Cộng hưởng: nhân $$n$$ / tăng bậc đa thức
- **Hanoi**: $$2^{n}-1$$
- **$$\sum k^{2}$$**: $$\frac{n(n+1)(2n+1)}{6}$$
- Bậc 2: $$+3^{n}$$ với $$(r-1)^{2}$$

---

## Liên hệ

**Edge case**: $$c=1$$, $$f$$ hằng → riêng $$Kn$$ (không $$K$$).

- Chi phí cố định mỗi bước đệ quy
- Tổng Gauss / tổng $$k^{2}$$
- Tiết 27: Master / divide-and-conquer

---

## Bài tập ôn tập (1/2)

1. $$a_n=3a_{n-1}+2$$, $$a_0=1$$
2. $$x_n=2x_{n-1}+1$$, $$x_1=1$$
3. $$a_n=a_{n-1}+n^{2}$$, $$a_0=0$$

---

## Bài tập ôn tập (2/2)

4. $$X_n=2X_{n-1}-X_{n-2}+3^{n}$$, $$X_0=1,X_1=3$$
5. $$a_n=2a_{n-1}+a_{n-2}+n^{2}$$ (viết $$a^{(h)}$$, $$a^{(p)}$$)
6. Tài khoản: $$a_n=1.007a_{n-1}-3$$, $$a_0=50$$

---

## Gợi ý đáp án nhanh

1. $$a_n=2\cdot 3^{n}-1$$  
2. $$x_n=2^{n}-1$$  
3. $$\frac{n(n+1)(2n+1)}{6}$$  
4. $$-\frac54-\frac52 n+\frac94\cdot 3^{n}$$  
5. $$a^{(h)}$$ với $$1\pm\sqrt{2}$$; $$a^{(p)}=-\frac12 n^{2}-2n-\frac52$$  
6. Riêng hằng $$K=1.007K-3\Rightarrow K=\frac{3}{0.007}$$; rồi $$a_0$$
