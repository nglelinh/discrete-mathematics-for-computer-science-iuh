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

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=crPe69NeTdk">NIST&#x27;s Post-Quantum Cryptography Standardization Explained</a> — SandboxAQ, tiếng Anh. Giới thiệu tổng quan quá trình chuẩn hóa mật mã hậu lượng tử của NIST.
- <a href="https://www.youtube.com/watch?v=_MoRcYLN-7U">Post Quantum Cryptography - Computerphile</a> — Computerphile, tiếng Anh. Giải thích lý do máy tính lượng tử tác động đến bài toán phân tích thừa số và logarit rời rạc.
- <a href="https://www.youtube.com/watch?v=3e-2Q0rFmd0">NIST&#x27;s Post-Quantum Cryptography Standardized: Lattice, Code, &amp; Isogeny Algorithms Explained</a> — ieeereview, tiếng Anh. Trình bày các hướng tiếp cận mạng tinh thể, mã sửa lỗi và isogeny trong các chuẩn NIST.
