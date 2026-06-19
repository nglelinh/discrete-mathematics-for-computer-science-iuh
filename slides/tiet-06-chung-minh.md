---
theme: white
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Chứng minh Trực tiếp và Phản chứng

**Toán Rời Rạc — IUH**

Tiết 6 (45 phút) — Phương pháp chứng minh

---

# Mục tiêu tiết học

- Hiểu cấu trúc chứng minh trực tiếp
- Thành thạo phương pháp chứng minh phản chứng
- Viết chứng minh rõ ràng, chặt chẽ
- Áp dụng vào chứng minh tính đúng của thuật toán và phần mềm
- Phân biệt khi nào dùng trực tiếp, khi nào dùng phản chứng

---

# Định nghĩa Chứng minh Trực tiếp

**Chứng minh trực tiếp** (Direct Proof) của mệnh đề "Nếu P thì Q" ($$P \to Q$$) là một chuỗi suy luận:

**Bắt đầu** từ việc giả sử $$P$$ đúng → dùng **định nghĩa**, **định lý đã biết** và **quy tắc suy diễn hợp lệ** → suy ra $$Q$$.

**Cấu trúc 5 bước chuẩn**:
1. Giả sử $$P$$ đúng
2. Mở định nghĩa của các khái niệm trong $$P$$
3. Biến đổi hoặc suy luận từng bước
4. Đạt được đúng dạng của $$Q$$
5. Kết luận mệnh đề đã được chứng minh (∎)

**Nguyên tắc**: Không được giả sử $$Q$$ đúng từ đầu.

---

# Ví dụ 1: Số chẵn

**Định lý**: Nếu $$n$$ là số chẵn thì $$n^2$$ cũng là số chẵn.

**Chứng minh trực tiếp**:
1. Giả sử $$n$$ là số chẵn.
2. Theo định nghĩa, tồn tại $$k \in \mathbb{Z}$$ sao cho $$n = 2k$$.
3. Khi đó:  
   $$n^2 = (2k)^2 = 4k^2 = 2(2k^2)$$
4. Vì $$2k^2 \in \mathbb{Z}$$, nên $$n^2$$ có dạng $$2m$$ với $$m \in \mathbb{Z}$$.
5. Do đó $$n^2$$ là số chẵn. ∎

---

# Định nghĩa Chứng minh Phản chứng

**Chứng minh phản chứng** (Proof by Contradiction):

Để chứng minh $$P$$ đúng:
1. Giả sử ngược lại: $$\neg P$$ đúng.
2. Từ giả sử này + các sự kiện đã biết → dẫn đến mâu thuẫn (thường là $$Q \land \neg Q$$).
3. Vì giả thiết $$\neg P$$ dẫn đến điều vô lý → $$\neg P$$ phải sai.
4. Do đó $$P$$ đúng.

**Cơ sở logic**:
$$\neg P \to (Q \land \neg Q) \quad \Rightarrow \quad P$$

---

# Khi nào nên dùng phản chứng?

- Kết luận mang tính **phủ định** ("không tồn tại...", "không thể...")
- Đường đi trực tiếp quá dài hoặc phức tạp
- Muốn chứng minh **duy nhất** hoặc **vô lý**
- Giả sử phủ định dễ dẫn đến mâu thuẫn rõ ràng

**Ví dụ kinh điển**: Chứng minh $$\sqrt{2}$$ vô tỷ.

---

# Ví dụ Phản chứng: Số vô tỷ

**Định lý**: $$\sqrt{2}$$ là số vô tỷ.

**Chứng minh**:
1. Giả sử ngược lại: $$\sqrt{2} = \frac{a}{b}$$ (với $$a, b \in \mathbb{Z}$$, $$b \neq 0$$, phân số tối giản).
2. Bình phương: $$2 = \frac{a^2}{b^2} \Rightarrow a^2 = 2b^2$$.
3. Suy ra $$a^2$$ chẵn → $$a$$ chẵn (vì nếu a lẻ thì a² lẻ).
4. Đặt $$a = 2k$$ → $$4k^2 = 2b^2 \Rightarrow b^2 = 2k^2$$.
5. Suy ra $$b^2$$ chẵn → $$b$$ chẵn.
6. Vậy cả $$a$$ và $$b$$ đều chẵn → phân số **không tối giản** → mâu thuẫn.
7. Do đó giả sử sai → $$\sqrt{2}$$ vô tỷ. ∎

---

# Ứng dụng trong Khoa học Máy tính

**Chứng minh trực tiếp**:
- Chứng minh một thuật toán luôn đúng với mọi đầu vào hợp lệ (loop invariant).
- Chứng minh hàm trả về kết quả đúng theo spec.

**Chứng minh phản chứng**:
- Chứng minh không tồn tại lỗi nào trong một trạng thái (ví dụ: không thể vừa logged in và logged out).
- Chứng minh một vấn đề là undecidable.
- Debug: giả sử không có lỗi → dẫn đến mâu thuẫn với test case.

**Ví dụ code**:
```python
# Chứng minh: nếu n chẵn thì n^2 chẵn
def is_even_square(n):
    if n % 2 == 0:           # giả sử P
        return (n * n) % 2 == 0  # suy ra Q
```

---

# Thực hành 1 (8 phút)

Chứng minh trực tiếp:
> Nếu $$n$$ là số chẵn thì $$n+2$$ cũng là số chẵn.

Viết đầy đủ 5 bước.

---

# Thực hành 2 (10 phút)

Dùng phản chứng:
> Chứng minh rằng không tồn tại số nguyên dương $$n$$ sao cho $$n^2 + 1$$ chia hết cho 4.

---

# Thực hành 3 (7 phút)

Phân tích:
> Một hệ thống không thể vừa ở trạng thái "đã xác thực" và "chưa xác thực" cùng lúc.

Viết dưới dạng chứng minh phản chứng.

---

# Tóm tắt Tiết 6

- **Chứng minh trực tiếp**: Giả sử P → dùng định nghĩa + suy luận → đạt Q
- **Chứng minh phản chứng**: Giả sử ¬P → dẫn đến mâu thuẫn → kết luận P đúng
- Cả hai đều dựa trên quy tắc suy diễn hợp lệ
- Rất quan trọng trong chứng minh tính đúng của phần mềm

---

# Chiều sâu & Liên hệ

**Chứng minh chính**:
Bước mở định nghĩa quan trọng nhất (unpack như code).

**Edge case**:
Không mở định nghĩa → không chứng minh được.

---

# Liên hệ & Ứng dụng nâng cao

**Liên hệ**:
- Trực tiếp ↔ Loop invariant.
- Phản chứng ↔ Bug proof.

**Ứng dụng nâng cao**:
- Formal verification (Coq, Dafny).
- Security protocol proof.

---

# Bài tập ôn tập (1/2)

1. **Bài 1**: Chứng minh trực tiếp: n chia 3 → n² chia 9.

2. **Bài 2**: Phản chứng: Không có n>0 với n²+n+1 chia 3.

---

# Bài tập ôn tập (2/2)

3. **Bài 3**: Viết trực tiếp: a,b lẻ → a+b chẵn.

4. **Bài 4**: Tại sao phản chứng phù hợp cho "không tồn tại thuật toán giải Halting"?

5. **Bài 5** (thách thức): Viết chứng minh cho một hàm code đơn giản.

---

# Tiết sau

**Logic vị từ**

- Mệnh đề lượng hóa
- Lượng từ ∀ và ∃
- Phủ định lượng từ
- Ứng dụng trong CSDL và lập trình

---

# Câu hỏi?

**Tiết 7**: Logic vị từ — Lượng từ ∀, ∃