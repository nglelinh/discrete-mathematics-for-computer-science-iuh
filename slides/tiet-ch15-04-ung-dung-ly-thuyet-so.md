---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Ứng dụng Lý thuyết Số

**Toán Rời Rạc** · Chương 15 · Bài 15.4

Hash · LCG · CRT-RSA · ECC · PQC

---

## Mục tiêu tiết học

- Yêu cầu hash mật mã
- LCG vs CSPRNG
- CRT tăng tốc RSA
- RSA vs ECC (bảng)
- Shor & post-quantum

**Bài học**: `…15_04_Applications…`

---

## Hash mật mã

$$H:\{0,1\}^*\to\{0,1\}^k$$

1. Tất định  
2. Preimage resistance  
3. Collision resistance  
4. Avalanche

SHA-256: Git, TLS, Bitcoin, …

---

## Hash ≠ bucket modulo

```python
index = hash(key) % table_size
```

Hữu ích cấu trúc dữ liệu  
**Không** đủ cho mật mã

Đừng nhầm SHA-256 với `% m`

---

## Avalanche

`"Hello"` vs `"hello"`  
→ digest **hoàn toàn** khác

Một bit plaintext  
→ khoảng nửa bit digest lật (kỳ vọng)

---

## LCG

$$x_{n+1}=(a x_n + c)\bmod m$$

- Dễ cài, chu kỳ ≤ $$m$$
- **Không** dùng cho khóa/nonce
- Dùng **CSPRNG** (`secrets`, `/dev/urandom`)

---

## CRT + RSA

Tính $$M^d\bmod n$$ qua

$$S_p \bmod p,\quad S_q \bmod q$$

rồi ghép CRT

→ nhanh hơn ~3–4× trong thực tế

---

## ECC

Cùng mức ước lượng bảo mật:

| Bits | RSA | ECC |
|:---:|:---:|:---:|
| 128 | ~3072 | ~256 |
| 256 | ~15360 | ~512 |

TLS, ECDSA, di động, …

---

## Lượng tử & PQC

**Shor**: phá RSA / DLP (lượng tử)

**PQC**: lattice, code, hash-based, …

NIST: Kyber, Dilithium, …

*Harvest now, decrypt later*

---

## Nguyên tắc vàng

**Không** tự phát minh cipher

Dùng thư viện / chuẩn đã review

Tránh MD5 / SHA-1 cho bảo mật mới

---

## Thực hành

1. Avalanche: đổi 1 ký tự, so hash
2. LCG $$a=7,c=3,m=10,x_0=2$$ — chu kỳ?
3. Vì sao cần PQC dù RSA-2048 còn dùng?
4. So sánh gọn RSA / ECC / Kyber

---

## Tóm tắt Chương 15

| Mục | Nội dung |
|:---|:---|
| 15.1 | Chia hết, prime, Euclid |
| 15.2 | Đồng dư, CRT, ModExp |
| 15.3 | RSA, DH, chữ ký |
| 15.4 | Hash, LCG, ECC, PQC |

**Tiếp**: Chương 16 — Cây

---

## Bài tập ôn tập (1/2)

1. Bốn yêu cầu hash mật mã
2. LCG dùng cho session key được không? Vì sao?
3. CRT giúp RSA ở bước nào?

---

## Bài tập ôn tập (2/2)

4. ECC ngắn hơn RSA nghĩa là gì?
5. Shor đe dọa hệ nào trong chương?

---

## Câu hỏi?
