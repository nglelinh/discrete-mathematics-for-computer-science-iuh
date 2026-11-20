---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Lý thuyết Số — Chia hết & Modulo

**Toán Rời Rạc**

Tiết 40 (45 phút) — Divisibility, Primes, GCD, Modulo

---

## Mục tiêu tiết học

- Hiểu tính chia hết và Định lý Chia
- Nhận biết số nguyên tố, phân tích thừa số nguyên tố
- Tính GCD bằng thuật toán Euclid
- Thực hiện phép toán modulo và đồng dư
- Liên hệ lý thuyết số với CS (hash, bảo mật)

---

## Tại sao lý thuyết số trong CS?

- **Mật mã**: RSA, Diffie-Hellman dựa trên modulo
- **Hashing**: `hash(key) % table_size`
- **Checksum**: CRC, xác thực dữ liệu
- **Random**: Sinh số nguyên tố, kiểm tra tính nguyên tố
- **Blockchain**: Số học modulo trên trường hữu hạn

**Nền tảng**: Chia hết → GCD → Modulo → Mật mã (tiết 41).

---

## Tính chia hết

Cho $$a, b \in \mathbb{Z}$$, $$b \neq 0$$:

$$b \mid a \quad \Leftrightarrow \quad \exists c \in \mathbb{Z}: a = bc$$

**Ví dụ**:
- $$3 \mid 12$$ vì $$12 = 3 \times 4$$
- $$7 \nmid 20$$
- $$1 \mid n$$ với mọi $$n$$
- $$n \mid 0$$ với mọi $$n \neq 0$$

**Tính chất**: Nếu $$b \mid a$$ và $$b \mid c$$ thì $$b \mid (a + c)$$ và $$b \mid (a - c)$$.

---

## Định lý Chia (Division Algorithm)

Cho $$a \in \mathbb{Z}$$, $$d \in \mathbb{Z}^+$$. Tồn tại **duy nhất** $$q$$ (thương) và $$r$$ (số dư):

$$a = dq + r, \quad 0 \leq r < d$$

**Ký hiệu**: $$a \textbf{ div } d = q$$, $$a \textbf{ mod } d = r$$.

**Ví dụ**: $$17 = 5 \times 3 + 2$$ → $$17 \bmod 5 = 2$$

**Cạm bẫy**: Python `-17 % 5 = 3` (đúng toán học); C/C++ có thể trả $$-2$$.

---

## Số nguyên tố

**Định nghĩa**: $$p > 1$$ là **số nguyên tố** nếu ước dương duy nhất là 1 và $$p$$.

Số $$n > 1$$ không nguyên tố → **hợp số** (composite).

- **Nguyên tố**: 2, 3, 5, 7, 11, 13, 17, 19, 23...
- **Lưu ý**: 1 **không** phải nguyên tố cũng không phải hợp số
- 2 là số nguyên tố **chẵn duy nhất**

---

## Định lý Cơ bản của Số học

Mọi $$n > 1$$ biểu diễn **duy nhất** (không kể thứ tự) dưới dạng:

$$n = p_1^{e_1} \times p_2^{e_2} \times \cdots \times p_k^{e_k}$$

**Ví dụ**:
- $$60 = 2^{2} \times 3 \times 5$$
- $$84 = 2^{2} \times 3 \times 7$$
- $$1001 = 7 \times 11 \times 13$$

**Ứng dụng**: Kiểm tra chia hết, tính GCD/LCM nhanh.

---

## Kiểm tra số nguyên tố

**Chia thử**: Kiểm tra ước từ 2 đến $$\lfloor\sqrt{n}\rfloor$$ → $$O(\sqrt{n})$$.

**Sàng Eratosthenes** — tìm mọi số nguyên tố $$\leq n$$:

```
prime[2..n] ← TRUE
FOR i ← 2 TO √n:
    IF prime[i] THEN
        FOR j ← i² TO n STEP i:
            prime[j] ← FALSE
```

**Độ phức tạp**: $$O(n \log \log n)$$ — dùng rộng rãi trong thực tế.

---

## GCD — Ước chung lớn nhất

$$\gcd(a, b)$$ = ước chung lớn nhất của $$a$$ và $$b$$.

**Tính chất**:
- $$\gcd(a, 0) = |a|$$
- $$\gcd(a, b) = \gcd(b, a \bmod b)$$

**Ví dụ**: $$\gcd(252, 198)$$
- $$252 = 198 \times 1 + 54$$
- $$198 = 54 \times 3 + 36$$
- $$54 = 36 \times 1 + 18$$
- $$36 = 18 \times 2 + 0$$ → **$$\gcd = 18$$**

---

## Thuật toán Euclid

```
EUCLID(a, b):
    WHILE b ≠ 0:
        r ← a mod b
        a ← b
        b ← r
    RETURN |a|
```

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
```

**Độ phức tạp**: $$O(\log \min(a, b))$$ — rất nhanh!

**Ứng dụng**: Rút gọn phân số, kiểm tra số nguyên tố cùng nhau.

---

## Đồng dư và Modulo

$$a \equiv b \pmod{n}$$ **iff** $$n \mid (a - b)$$

Hai số có **cùng số dư** khi chia cho $$n$$.

**Ví dụ**:
- $$17 \equiv 5 \pmod{12}$$
- $$23 \times 17 \equiv 3 \times 2 = 6 \equiv 1 \pmod{5}$$

**Phép toán**: Nếu $$a \equiv b$$ và $$c \equiv d \pmod{n}$$ thì:
- $$a + c \equiv b + d$$
- $$a \times c \equiv b \times d$$

---

## Ứng dụng Modulo trong CS

```python
# Hash table
def hash_index(key, size):
    return key % size

# Đồng hồ 24h
hour = (current_hour + 5) % 24

# Kiểm tra chẵn/lẻ
is_even = (n % 2 == 0)

# Xoay buffer vòng
next_pos = (pos + 1) % buffer_size
```

**Lũy thừa modulo** (nhanh): $$a^{e} \bmod n$$ trong $$O(\log e)$$ — nền RSA.

---

## Định lý Fermat nhỏ (preview)

Nếu $$p$$ nguyên tố và $$\gcd(a, p) = 1$$:

$$a^{p-1} \equiv 1 \pmod{p}$$

**Ví dụ**: $$2^{6} = 64 \equiv 1 \pmod{7}$$ (vì 7 nguyên tố).

**Ứng dụng**: Kiểm tra số nguyên tố (Miller-Rabin), tính nghịch đảo modulo.

**Tiết 41**: Dùng modulo cho RSA và mật mã khóa công khai.

---

## Thực hành 1

1. Tính $$252 \bmod 45$$ và $$-17 \bmod 5$$ (theo định nghĩa toán học).
2. Phân tích $$360$$ ra thừa số nguyên tố.
3. $$\gcd(1071, 462)$$ bằng Euclid (viết từng bước).

---

## Thực hành 2

1. Dùng sàng Eratosthenes, liệt kê số nguyên tố $$\leq 50$$.
2. Tính $$(17 \times 23) \bmod 7$$ bằng cách rút gọn từng số trước.
3. Chứng minh: nếu $$a \equiv b \pmod{n}$$ thì $$a^{2} \equiv b^{2} \pmod{n}$$.

---

## Thực hành 3

Một hash table có `size = 11`. Với `key = 25, 36, 47`:

1. Tính `key % 11` cho mỗi khóa
2. Có collision không?
3. Nếu `size = 10` (hợp số), vấn đề gì có thể xảy ra?

---

## Tóm tắt Tiết 40

- **Chia hết**: $$b \mid a \Leftrightarrow a = bc$$
- **Nguyên tố**: phân tích duy nhất (FTA)
- **GCD**: Euclid — $$O(\log n)$$
- **Modulo**: đồng dư, phép toán modulo
- Nền cho mật mã RSA (tiết 41)

---

## Liên hệ

**Định lý chính**: FTA — mọi số > 1 phân tích duy nhất thành nguyên tố.

**Edge case**: `mod` với số âm; `size` hash table nên là số nguyên tố.

**Liên hệ**: Đếm (tiết 16–22) ↔ Euclid $$O(\log n)$$ ↔ RSA (tiết 41).

---

## Bài tập ôn tập (1/2)

1. **Euclid**: Tính $$\gcd(1071, 462)$$ và $$\gcd(17, 13)$$.

2. **Modulo**: Tính $$3^{10} \bmod 7$$ (dùng Fermat nhỏ hoặc lũy thừa từng bước).

3. **Nguyên tố**: 97 có phải số nguyên tố? Kiểm tra bằng chia thử.

---

## Bài tập ôn tập (2/2)

4. **Phân tích**: Viết $$1260$$ dưới dạng tích lũy thừa số nguyên tố.

5. **Bài 5**: Chứng minh $$\gcd(a, b) \cdot \text{lcm}(a, b) = |a \cdot b|$$. Áp dụng với $$a=12, b=18$$.
