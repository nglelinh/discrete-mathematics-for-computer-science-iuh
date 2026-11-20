---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Ôn tập — Hệ thức truy hồi
---

## Mục tiêu tiết học

- **Phân loại** HTTH: bậc, tuyến tính, thuần nhất / không thuần nhất
- **Giải** thuần nhất hệ số hằng (nghiệm đơn / kép / phức)
- **Giải** không thuần nhất: $$a^{(h)}+a^{(p)}$$

---

## Phân loại hệ thức truy hồi

| Thuật ngữ            | Ý nghĩa                             |     |
| :------------------- | :---------------------------------- | --- |
| **Bậc $$k$$**        | Cần $$k$$ điều kiện đầu             |     |
| **Tuyến tính**       | $$a_n$$ tuyến tính theo $$a_{n-i}$$ |     |
| **Thuần nhất**       | Không có $$f(n)$$ ngoài             |     |
| **Không thuần nhất** | Có $$+f(n)$$                        |     |
| **Hệ số hằng**       | $$c_i$$ không phụ thuộc $$n$$       |     |

---

## Nghiệm thuần nhất

Giả sử $$a_n = r^{n}$$ → **phương trình đặc trưng**.

| Nghiệm                 | Dạng $$a_n$$                              |
| :--------------------- | :---------------------------------------- |
| $$r_1\neq r_2$$ thực   | $$\alpha r_1^{n}+\beta r_2^{n}$$          |
| Nghiệm kép $$r$$       | $$(\alpha+\beta n)r^{n}$$                 |
| $$r=\alpha\pm i\beta$$ | $$\rho^{n}(A\cos n\theta+B\sin n\theta)$$ |

$$\rho=\sqrt{\alpha^{2}+\beta^{2}}$$, $$\theta=\operatorname{arg}(r)$$.

---

## Không thuần nhất

$$a_n = a_n^{(h)} + a_n^{(p)}$$

| $$f(n)$$ | Thử $$a_n^{(p)}$$ |
|:---|:---|
| Hằng $$d$$ | $$A$$ |
| Đa thức bậc $$m$$ | $$B_0+\cdots+B_m n^{m}$$ |
| $$b^{n}$$ | $$A b^{n}$$ |

**Cộng hưởng**: dạng thử trùng nghiệm thuần nhất → nhân $$n$$ (hoặc $$n^{s}$$).

---

## Nhận dạng

Với mỗi dãy: nêu **bậc**, **tuyến tính?**, **thuần nhất?**, **hệ số hằng?**

1. $$a_n = 3a_{n-1}+2$$
2. $$a_n = a_{n-1}^{2}+n$$
3. $$a_n = 2a_{n-1}-a_{n-2}$$

---

## Thuần nhất

Giải:

1. $$a_n = 7a_{n-1}-12a_{n-2}$$
2. $$a_n = 6a_{n-1}-9a_{n-2}$$
3. $$a_n = 2a_{n-1}-5a_{n-2}$$

Viết **phương trình đặc trưng** + dạng nghiệm tổng quát.

---

## Đáp án nhanh — B

1. $$r^{2}-7r+12=0$$ → $$(r-3)(r-4)=0$$  
   $$a_n=\alpha\,3^{n}+\beta\,4^{n}$$

2. $$r^{2}-6r+9=(r-3)^{2}$$ → $$a_n=(\alpha+\beta n)3^{n}$$

3. $$r^{2}-2r+5=0$$ → $$r=1\pm 2i$$  
   $$\rho=\sqrt{5}$$, $$\theta=\arctan 2$$  
   $$a_n=(\sqrt{5})^{n}\bigl(A\cos(n\theta)+B\sin(n\theta)\bigr)$$

---

## Gắn điều kiện đầu

$$a_n=7a_{n-1}-12a_{n-2}$$, $$a_0=2$$, $$a_1=5$$

Tìm $$\alpha,\beta$$ trong $$a_n=\alpha 3^{n}+\beta 4^{n}$$.

---

## Đáp án — điều kiện đầu

$$
\begin{cases}
\alpha+\beta=2\\
3\alpha+4\beta=5
\end{cases}
\Rightarrow \alpha=3,\ \beta=-1
$$

$$a_n=3\cdot 3^{n}-4^{n}=3^{n+1}-4^{n}$$  
(kiểm $$n=0$$: $$3-1=2$$; $$n=1$$: $$9-4=5$$).

---

## Không thuần nhất

$$a_n = a_n^{(h)}+a_n^{(p)}$$

| Bài | Phương trình           | Gợi ý $$a^{(p)}$$             |
| :-: | :--------------------- | :---------------------------- |
|  1  | $$a_n=2a_{n-1}+3$$     | hằng $$A$$                    |
|  2  | $$a_n=3a_{n-1}+2^{n}$$ | $$A\cdot 2^{n}$$ + cộng hưởng |
|  3  | $$a_n=a_{n-1}+n$$      | đa thức; $$r=1$$ + cộng hưởng |

---

## Đáp án nhanh

1. Thuần nhất: $$a_n^{(h)}=C\cdot 2^{n}$$  
   Riêng: $$A=2A+3\Rightarrow A=-3$$  
   $$a_n=C\cdot 2^{n}-3$$  
   (gắn $$a_0$$ nếu có)

---

## Đáp án nhanh 

2. $$a_n-3a_{n-1}=2^{n}$$  
   $$r=3$$; $$2\neq 3$$ → thử $$A\cdot 2^{n}$$:  
   $$A\cdot 2^{n}-3A\cdot 2^{n-1}=2^{n}$$  
   $$A-\frac{3A}{2}=1\Rightarrow A=-2$$  
   $$a_n^{(p)}=-2\cdot 2^{n}=-2^{n+1}$$

---

## Đáp án nhanh 

3. $$a_n-a_{n-1}=n$$; $$r=1$$ là nghiệm → thử $$A n^{2}+B n$$  
   (hoặc $$An^{2}$$ đủ nếu chỉ cần một riêng).  
   Thay vào tìm $$A,B$$;  
   $$a_n^{(h)}=C$$;  
   $$a_n=C+An^{2}+Bn$$.

---

## Cộng hưởng 

**Nếu $$f(n)$$ “giống” một hạng đã có trong $$a^{(h)}$$**  
→ nhân thêm $$n^{s}$$ ($$s$$ = bội nghiệm).

Ví dụ: $$f(n)=3^{n}$$ và $$r=3$$ là nghiệm đơn → thử $$A n\, 3^{n}$$.

---

## Lỗi hay gặp

- Quên kiểm tra **cộng hưởng**
- Sai bậc phương trình đặc trưng
- Gắn điều kiện đầu nhầm chỉ số $$n=0$$ vs $$n=1$$
- Phức: quên $$\rho^{n}$$ hoặc sai $$\theta$$

---

## Checklist giải HTTH

1. Phân loại (bậc / thuần nhất?)  
2. Phương trình đặc trưng → $$a^{(h)}$$  
3. Nếu có $$f(n)$$: thử $$a^{(p)}$$ (+ cộng hưởng)  
4. $$a=a^{(h)}+a^{(p)}$$  
5. Điều kiện đầu → hằng số

---

## Tóm tắt tiết 29

- Phân loại trước khi giải
- Thuần nhất = đặc trưng + dạng nghiệm
- Không thuần nhất = chồng chất + hệ số bất định
- Cộng hưởng = nhân $$n^{s}$$
- Phức → ôn tiết 28

---

## Bài tập về nhà (1/2)

1. $$a_n=6a_{n-1}-9a_{n-2}$$, $$a_0=1$$, $$a_1=6$$ — giải đầy đủ.
2. $$a_n=2a_{n-1}+n$$, $$a_0=0$$ — có cộng hưởng không? Giải.
3. $$a_n=a_{n-1}+2a_{n-2}+3^{n}$$ — viết $$a^{(h)}$$ và dạng thử $$a^{(p)}$$ (chưa bắt buộc gắn ĐKĐ).

---

## Bài tập về nhà (2/2)

4. Nghiệm $$r=-\frac12\pm i\frac{\sqrt3}{2}$$: tính $$\rho,\theta$$ và dạng $$a_n$$ thực.
5. (Tuỳ chọn) Merge sort: vì sao $$T(n)=2T(n/2)+n$$ cho $$\Theta(n\log n)$$? (lời giải phác)

---

## Ôn xong chùm truy hồi

| Tiết | Nội dung |
|:---:|:---|
| 24 | Mô hình hóa HTTH |
| 25 | Thuần nhất + số phức |
| 26 | Không thuần nhất |
| 27 | Ứng dụng thuật toán |
| **28** | Ôn số phức |
| **29** | Ôn HTTH |

---

## Câu hỏi?
