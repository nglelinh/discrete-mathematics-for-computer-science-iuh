---
layout: post
title: "Ghi chú mở rộng: Chuẩn hậu lượng tử của NIST (2024)"
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

Bài ghi chú ứng dụng song ngữ. Bài này **không** thay thế các nội dung về tính chia hết, RSA hay bài khảo sát từ Euclid đến blockchain.

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

### Background Knowledge Map: Why Quantum Computers Break RSA & How Lattices Save Us
- **Shor’s Algorithm Threat:** A large fault-tolerant quantum computer solves integer factorization (RSA) and discrete logarithms (ECC) in polynomial time, motivating NIST’s **2024 Post-Quantum Cryptography (PQC) standards**: **ML-KEM (FIPS 203, Kyber)** for key encapsulation and **ML-DSA (FIPS 204, Dilithium)** for signatures.
- **Learning With Errors (LWE):** Solving a clean modular linear system $$A\mathbf{s} \equiv \mathbf{b} \pmod q$$ is trivial via Gaussian elimination. Adding a tiny random error vector $$\mathbf{e}$$ ($$\mathbf{b} \equiv A\mathbf{s} + \mathbf{e} \pmod q$$) turns it into a hard **high-dimensional lattice problem** believed resistant even to quantum computers!

### Deep-Dive Explanation: A Tiny Hand-Checkable LWE Example Modulo $$q = 17$$ (Read Slowly)
1. **Step 1 (Secret):** Pick a secret vector $$\mathbf{s} = (3, 5)^\top \pmod{17}$$.
2. **Step 2 (Noiseless vs. Noisy Equations):** Take $$a_1 = (2, 1) \implies a_1\cdot s = 11$$; add tiny noise $$e_1 = +1 \implies b_1 = 12$$. Take $$a_2 = (4, 3) \implies a_2\cdot s = 27 \equiv 10$$; add noise $$e_2 = -1 \implies b_2 = 9$$.
3. **Step 3 (Why Gaussian Elimination Collapses):** In high dimension ($$n \approx 512..1024$$), combining equations amplifies the tiny errors $$e_i$$ linearly until the noise completely swamps the signal modulo $$q$$!
4. **Step 4 (Migration Strategy):** Today’s browsers and TLS 1.3 deploy **hybrid mode** (X25519 + ML-KEM-768) to defend against "harvest now, decrypt later" attacks!

## Tiếng Việt

RSA và Diffie–Hellman trong chương này dựa trên bài toán phân tích thừa số nguyên tố và logarit rời rạc. Ngày **13/08/2024**, NIST đã ban hành ba chuẩn FIPS cho các thuật toán khóa công khai hướng tới khả năng chống chịu trước máy tính lượng tử quy mô lớn:

| Chuẩn | Tên | Nguồn gốc | Vai trò |
|:---|:---|:---|:---|
| FIPS 203 | ML-KEM | CRYSTALS-Kyber | Cơ chế đóng gói khóa (KEM) |
| FIPS 204 | ML-DSA | CRYSTALS-Dilithium | Chữ ký số dựa trên mạng tinh thể (*lattice*) |
| FIPS 205 | SLH-DSA | SPHINCS+ | Chữ ký số dựa trên hàm băm không trạng thái |

FIPS 203 quy định các bộ tham số ML-KEM-512, ML-KEM-768 và ML-KEM-1024. Độ an toàn của chuẩn này gắn với bài toán **Module Learning With Errors** (một bài toán mạng tinh thể có cấu trúc), thay vì bài toán phân tích $$n = pq$$. Các bộ tham số thể hiện sự đánh đổi giữa mức độ bảo mật và tốc độ thực thi. Khi triển khai thực tế, mã nguồn phải tuân thủ đúng văn bản chuẩn FIPS vì ML-KEM không tương thích từng byte với phiên bản “Kyber Round 3”.

Điểm đáng lưu ý thêm cho khóa học: số học modulo và hàm băm không hề biến mất, mà được chuyển *vào bên trong* vành đa thức và họ hàm băm SHAKE; giả thuyết độ khó mới chỉ đổi sang một đối tượng lý thuyết số khác. Bạn nên đọc kỹ phần RSA trước, rồi mới xem bản cập nhật chuẩn năm 2024 này.

**Câu hỏi.** (1) Cơ chế KEM *thay thế* cho thành phần mật mã nào của Chương 15 trong quá trình bắt tay kiểu TLS? (2) Vì sao việc đã triển khai “Kyber Round 3” không đồng nghĩa với việc tuân thủ chuẩn “FIPS 203”?

### Kiến thức cần nhớ: Chuẩn Mật mã Hậu lượng tử NIST (2024) và Bài toán Mạng tinh thể (LWE)
- **Nguy cơ từ Thuật toán Shor:** Máy tính lượng tử đủ lớn có thể giải phân tích thừa số (RSA) và logarit rời rạc (ECC) trong thời gian đa thức. Tháng 8/2024, NIST chính thức ban hành các chuẩn hậu lượng tử đầu tiên: **ML-KEM (FIPS 203 — Kyber)** cho trao đổi khóa và **ML-DSA (FIPS 204 — Dilithium)**, **SLH-DSA (FIPS 205)** cho chữ ký số.
- **Bài toán Học có Nhiễu (LWE — Learning With Errors):** Giải hệ tuyến tính $$A\mathbf{s} \equiv \mathbf{b} \pmod q$$ bằng khử Gauss cực dễ, nhưng chỉ cần cộng thêm một vectơ **nhiễu nhỏ $$\mathbf{e}$$** ($$\mathbf{b} \equiv A\mathbf{s} + \mathbf{e} \pmod q$$), bài toán trở nên khó tương đương tìm vectơ ngắn nhất trên mạng tinh thể nhiều chiều — chống chịu được cả máy tính lượng tử!

### Ví dụ tính tay làm từng bước: Quan sát Nhiễu LWE làm hỏng Khử Gauss modulo $$q = 17$$
Giả sử khóa bí mật là $$\mathbf{s} = (3, 5)^\top \in \mathbb{Z}_{17}^2$$:
- Phương trình 1: $$a_1 = (2, 1) \implies 2(3) + 1(5) = 11$$. Cộng nhiễu nhỏ $$e_1 = +1 \implies b_1 = 12$$.
- Phương trình 2: $$a_2 = (4, 3) \implies 4(3) + 3(5) = 27 \equiv 10 \pmod{17}$$. Cộng nhiễu nhỏ $$e_2 = -1 \implies b_2 = 9$$.
Nếu kẻ tấn công thử khử Gauss trực tiếp trên hệ $$(2s_1 + s_2 = 12,\; 4s_1 + 3s_2 = 9) \pmod{17}$$: lấy PT2 trừ $$2\times$$PT1 được $$s_2 \equiv 9 - 24 = -15 \equiv 2 \pmod{17}$$ — **sai hoàn toàn so với đáp án thật $$s_2 = 5$$**! Ở kích thước thực tế $$n = 512..1024$$, tổ hợp tuyến tính làm nhiễu khuếch đại che phủ hoàn toàn khóa bí mật!

### Giải thích: 4 bước chuyển đổi Internet sang Kỷ nguyên Hậu lượng tử
#### Bước 1: Phòng thủ sớm trước tấn công "Thu thập hôm nay, giải mã tương lai"
Dữ liệu mã hóa bằng RSA/ECC truyền hôm nay có thể bị lưu lại chờ máy tính lượng tử giải mã sau 10–15 năm.
#### Bước 2: Chuyển nền tảng toán học từ Số học Nhân sang Đại số Tuyến tính có Nhiễu (LWE/Module-LWE)
ML-KEM dùng đại số đa thức modulo $$X^{256}+1$$ kết hợp biến đổi số học NTT (tương tự FFT) để vừa an toàn lượng tử vừa chạy nhanh ngang ECC!
#### Bước 3: Triển khai Chế độ Lai (Hybrid Mode: X25519 + ML-KEM)
Chrome, Cloudflare và Apple iMessage kết hợp song song khóa cổ điển và khóa hậu lượng tử để bảo đảm an toàn kép.
#### Bước 4: Cập nhật hạ tầng chữ ký và chứng chỉ số
Khóa và chữ ký PQC lớn hơn ECC vài lần, đòi hỏi tối ưu hóa giao thức mạng và phần cứng bảo mật (HSM).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=crPe69NeTdk">NIST&#x27;s Post-Quantum Cryptography Standardization Explained</a> — SandboxAQ, tiếng Anh. Giới thiệu tổng quan quá trình chuẩn hóa mật mã hậu lượng tử của NIST.
- <a href="https://www.youtube.com/watch?v=_MoRcYLN-7U">Post Quantum Cryptography - Computerphile</a> — Computerphile, tiếng Anh. Giải thích lý do máy tính lượng tử tác động đến bài toán phân tích thừa số và logarit rời rạc.
- <a href="https://www.youtube.com/watch?v=3e-2Q0rFmd0">NIST&#x27;s Post-Quantum Cryptography Standardized: Lattice, Code, &amp; Isogeny Algorithms Explained</a> — ieeereview, tiếng Anh. Trình bày các hướng tiếp cận mạng tinh thể, mã sửa lỗi và isogeny trong các chuẩn NIST.
