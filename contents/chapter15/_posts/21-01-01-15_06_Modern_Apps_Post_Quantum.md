---
layout: post
title: "Optional note: NIST post-quantum standards (2024)"
categories: chapter15
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. FIPS 203/204/205 (13 August 2024) standardise ML-KEM, ML-DSA, and SLH-DSA — lattice and hash number theory for a quantum-safe public key. Does not replace Euclid/RSA lessons."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite divisibility, RSA, or the Euclid-to-blockchain survey (which already mentions post-quantum at a high level).

Bài ghi chú ứng dụng song ngữ. **Không** viết lại chia hết, RSA, hay bài từ Euclid đến blockchain.

</div>

## English

RSA and Diffie–Hellman in this chapter rest on integer factorisation and discrete logs. On **13 August 2024** NIST issued three FIPS standards for public-key algorithms intended to remain secure against large quantum computers ([NIST announcement](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips)):

| Standard | Name | Derived from | Role |
|:---|:---|:---|:---|
| [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) | ML-KEM | CRYSTALS-Kyber | Key encapsulation (KEM) |
| FIPS 204 | ML-DSA | CRYSTALS-Dilithium | Lattice signatures |
| FIPS 205 | SLH-DSA | SPHINCS+ | Stateless hash signatures |

FIPS 203 ([DOI 10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203)) specifies ML-KEM-512/768/1024. Security is tied to **Module Learning With Errors** (a structured lattice problem), not to factoring $$n = pq$$. Parameter sets trade security strength against speed. Implementations must follow the FIPS text: ML-KEM is not byte-for-byte “Kyber Round 3.”

Optional point for the course: modular arithmetic and hashes do not disappear — they move *inside* polynomial rings and SHAKE. The new hardness assumption is a different number-theoretic object. Read RSA first, then this 2024 standards snapshot.

**Citations**

1. NIST, *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*, 13 Aug 2024. [CSRC](https://csrc.nist.gov/pubs/fips/203/final)
2. NIST, approval notice for FIPS 203, 204, 205, 13 Aug 2024. [News](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips)

**Questions.** (1) Which Chapter 15 primitive does a KEM *replace* in a TLS-style handshake? (2) Why is “we shipped Kyber Round 3” not the same as “we are FIPS 203 compliant”?

## Tiếng Việt

RSA và Diffie–Hellman trong chương này dựa trên phân tích số nguyên và log rời rạc. Ngày **13/08/2024** NIST ban hành ba chuẩn FIPS cho khóa công khai nhằm chống máy lượng tử lớn:

| Chuẩn | Tên | Nguồn | Vai trò |
|:---|:---|:---|:---|
| FIPS 203 | ML-KEM | CRYSTALS-Kyber | Đóng gói khóa (KEM) |
| FIPS 204 | ML-DSA | CRYSTALS-Dilithium | Chữ ký lattice |
| FIPS 205 | SLH-DSA | SPHINCS+ | Chữ ký hash không trạng thái |

FIPS 203 quy định ML-KEM-512/768/1024. An toàn gắn với **Module Learning With Errors** (bài toán lattice có cấu trúc), không phải phân tích $$n = pq$$. Bộ tham số đánh đổi độ mạnh và tốc độ. Cài đặt phải theo văn bản FIPS: ML-KEM không khớp từng byte với “Kyber Round 3.”

Điểm tùy chọn: số học modulo và hash không biến mất — chúng chuyển *vào* vành đa thức và SHAKE. Giả thiết cứng mới là đối tượng lý thuyết số khác. Đọc RSA trước, rồi ảnh chụp chuẩn 2024 này.

**Câu hỏi.** (1) KEM *thay* primitive Chương 15 nào trong handshake kiểu TLS? (2) Vì sao “đã ship Kyber Round 3” không đồng nghĩa “tuân FIPS 203”?
