---
layout: post
title: "Ghi chú mở rộng: Cận chuồng bồ câu trong bộ lọc hiện đại (2022–2026)"
categories: chapter08
date: 2021-01-01
order: 4
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Binary fuse filters (JEA 2022) sit a few percent above the pigeonhole / information-theoretic floor for set sketches. Does not replace Dirichlet theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite the pigeonhole principle or the existing computing applications lesson.

Ghi chú ứng dụng song ngữ (tiếng Anh, sau đó là tiếng Việt). Bài này **không** thay thế nội dung về nguyên lý Dirichlet hay bài ứng dụng trong khoa học máy tính.

</div>

## English

Dirichlet’s principle is why **perfect** compact membership is impossible: more pigeons (keys) than holes (bit patterns) forces a collision. Approximate membership structures accept a false-positive rate $$\varepsilon$$ and then ask how close they sit to the information-theoretic floor $$\approx n \log_2(1/\varepsilon)$$ bits for $$n$$ keys.

Graf and Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27, Article 1.5 (2022), [DOI 10.1145/3510449](https://doi.org/10.1145/3510449), report constructions within **13%** of that lower bound (about **8%** with a slower layout), beating xor filters on space and often on build time, and comparing Bloom, cuckoo, and ribbon filters.

The optional takeaway for Chapter 8: the 2022 data-structure race is a quantitative pigeonhole contest. Hash collisions in tables (already in the required lessons) are the same phenomenon with a different layout. Binary fuse filters do not repeal Dirichlet; they spend bits more carefully after you accept that some holes must be shared.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) If you demand $$\varepsilon = 0$$ and $$n > m$$ fingerprints, which theorem of this chapter applies? (2) Why is “13% above the lower bound” a pigeonhole statement rather than a machine-learning statement?


### Background Knowledge Map: Pigeonhole Lower Bounds in Probabilistic Data Structures

1. **Exact Sets vs. Approximate Filters:** Storing $$n$$ distinct 64-bit keys exactly requires $$\ge 64n$$ bits. When RAM is scarce (database SSTables, CDN routers), filters like **Bloom**, **Xor**, and **Ribbon filters** trade a tiny false-positive rate $$\varepsilon$$ for an order-of-magnitude memory reduction.
2. **The Information-Theoretic Pigeonhole Floor:** By a direct pigeonhole counting argument, *any* static membership filter with false-positive rate $$\varepsilon$$ MUST spend at least $$\log_2(1/\varepsilon)$$ bits per key!
3. **2022–2026 Static Filters (Binary Fuse & Ribbon):** Modern filters (Graf & Lemire, 2022) approach that pigeonhole floor within just $$8\text{–}13\%$$ overhead—far tighter than classic Bloom filters’ $$44\%$$ overhead ($$1.44\log_2(1/\varepsilon)$$ bits/key).

### Deep-Dive Explanation: Hand-Checking the Bits-per-Key Floor at $$\varepsilon = 1/256$$ (Read Slowly)

#### Step 1: Compute the theoretical pigeonhole floor
Suppose you allow a false-positive rate of $$\varepsilon = 2^{-8} \approx 0.39\%$$ (1 in 256 queries). The information-theoretic pigeonhole lower bound demands at least:
$$
\log_2(1/\varepsilon) = \log_2(256) = \mathbf{8.0\text{ bits/key}}.
$$

#### Step 2: Compare Bloom filter vs. Binary Fuse filter (2022) on 10 million keys
- **Classic Bloom filter:** needs $$1.44 \times 8.0 \approx 11.52\text{ bits/key}$$ $$\implies \approx \mathbf{14.4\text{ MB}}$$ for $$10^7$$ keys.
- **3-wise Binary Fuse filter (Graf & Lemire, 2022):** uses $$1.13 \times 8.0 \approx 9.04\text{ bits/key}$$ $$\implies \approx \mathbf{11.3\text{ MB}}$$ (saving $$21\%$$ RAM while answering queries in 3 cache lookups!).

#### Step 3: Why no future paper can beat 8.0 bits/key at $$\varepsilon = 1/256$$
Just like lossless compression cannot beat $$2^N - 1 < 2^N$$, no filter—classical or learned—can store arbitrary $$n$$-key sets below $$\log_2(1/\varepsilon)$$ bits/key without exceeding false-positive rate $$\varepsilon$$ on worst-case universes!

$$
\text{Target FP rate } \varepsilon
\;\xrightarrow{\text{Pigeonhole bound}}\;
\ge \log_2(1/\varepsilon)\text{ bits/key}
\;\xrightarrow{\text{2022 Binary Fuse}}\;
\approx 1.08\text{–}1.13\,\log_2(1/\varepsilon).
$$

## Tiếng Việt

Nguyên lý Dirichlet giải thích vì sao không thể xây dựng một cấu trúc kiểm tra phần tử thuộc tập (membership) vừa **chính xác tuyệt đối** vừa siêu gọn: khi số khóa (bồ câu) lớn hơn số mẫu bit khả dĩ (chuồng), va chạm chắc chắn xảy ra. Các cấu trúc kiểm tra xấp xỉ chấp nhận một tỷ lệ dương tính giả $$\varepsilon$$, rồi đặt câu hỏi bộ nhớ cần dùng tiến gần đến cận dưới lý thuyết thông tin $$\approx n \log_2(1/\varepsilon)$$ bit (cho $$n$$ khóa) đến mức nào.

Trong công trình trên tạp chí *J. Exp. Algorithmics* (2022), Graf và Lemire báo cáo bộ lọc **binary fuse filter** chỉ lớn hơn cận dưới lý thuyết khoảng **13%** (hoặc khoảng **8%** nếu dùng bố cục chậm hơn), vượt qua xor filter về dung lượng bộ nhớ và thường nhanh hơn về thời gian xây dựng, đồng thời so sánh trực tiếp với các bộ lọc Bloom, cuckoo và ribbon.

Điểm đáng rút ra cho Chương 8 là cuộc đua tối ưu các cấu trúc dữ liệu bộ lọc thực chất là một bài toán chuồng bồ câu định lượng. Hiện tượng va chạm trong bảng băm (đã học ở phần bắt buộc) có cùng bản chất, chỉ khác cách tổ chức bộ nhớ. Binary fuse filter không phá vỡ nguyên lý Dirichlet; thay vào đó, khi đã chấp nhận một số ngăn chứa phải dùng chung, chúng sử dụng từng bit bộ nhớ một cách tiết kiệm hơn.

**Câu hỏi.** (1) Nếu yêu cầu $$\varepsilon = 0$$ với $$n > m$$ dấu vân tay (fingerprint), định lý nào của chương này được áp dụng? (2) Vì sao phát biểu “cao hơn cận dưới 13%” mang bản chất của nguyên lý chuồng bồ câu chứ không phải học máy?


### Bản đồ kiến thức nền: Cận Chuồng bồ câu trong Bộ lọc Xác suất Hiện đại

1. **Tập chính xác vs. Bộ lọc xấp xỉ:** Lưu chính xác $$n$$ khóa 64-bit tốn ít nhất $$64n$$ bit. Trong RocksDB hay bộ định tuyến CDN, các bộ lọc **Bloom**, **Xor** và **Ribbon** chấp nhận tỷ lệ dương tính giả nhỏ $$\varepsilon$$ để tiết kiệm gấp nhiều lần RAM.
2. **Sàn lý thuyết từ Nguyên lý Chuồng bồ câu:** Bằng phép đếm chuồng bồ câu, *mọi* bộ lọc thành viên tĩnh có tỷ lệ dương tính giả $$\varepsilon$$ bắt buộc tốn tối thiểu **$$\log_2(1/\varepsilon)$$ bit cho mỗi khóa**!
3. **Bộ lọc tĩnh 2022–2026 (Binary Fuse & Ribbon):** Bộ lọc Binary Fuse (Graf & Lemire, 2022) tiến sát sàn lý thuyết chỉ còn dư $$8\text{–}13\%$$ — gọn hơn hẳn mức dư $$44\%$$ ($$1.44\log_2(1/\varepsilon)$$) của Bloom filter kinh điển!

### Khung giải thích: Tính tay số MB RAM cho 10 triệu khóa ở mức $$\varepsilon = 1/256$$ (nên đọc chậm)

#### Bước 1: Tính sàn lý thuyết chuồng bồ câu
Với tỷ lệ dương tính giả $$\varepsilon = 2^{-8} \approx 0.39\%$$, sàn lý thuyết tối thiểu là:
$$
\log_2(1/\varepsilon) = \log_2(256) = \mathbf{8.0\text{ bit/khóa}}.
$$

#### Bước 2: Đối chiếu Bloom filter với Binary Fuse filter (2022) cho $$10^7$$ khóa
- **Bloom filter cổ điển:** tốn $$1.44 \times 8.0 \approx 11.52\text{ bit/khóa} \implies \approx \mathbf{14.4\text{ MB}}$$.
- **Binary Fuse filter (Graf & Lemire, 2022):** tốn $$1.13 \times 8.0 \approx 9.04\text{ bit/khóa} \implies \approx \mathbf{11.3\text{ MB}}$$ (tiết kiệm hơn $$21\%$$ RAM!).

#### Bước 3: Hiểu giới hạn bất khả vượt
Không một bộ lọc nào có thể lưu tập khóa tùy ý dưới mức $$8.0$$ bit/khóa mà vẫn giữ $$\varepsilon \le 1/256$$ — mọi cải tiến thuật toán đều đang đua nhau tiến sát sàn chuồng bồ câu ấy!

$$
\text{Tỷ lệ } \varepsilon
\;\xrightarrow{\text{Dirichlet}}\;
\ge \log_2(1/\varepsilon)\text{ bit/khóa}
\;\xrightarrow{\text{Binary Fuse 2022}}\;
\approx 1.08\text{–}1.13\,\log_2(1/\varepsilon).
$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Giới thiệu trực quan bộ lọc Bloom và lý do bộ nhớ bị chặn dưới bởi số phần tử cần phân biệt.
- <a href="https://www.youtube.com/watch?v=eV1haPUt0NU">Hyperloglog: Facebook&#x27;s algorithm to count distinct elements</a> — Gaurav Sen, tiếng Anh. Giới thiệu HyperLogLog để đếm lực lượng gần đúng, thuộc cùng họ cấu trúc tóm tắt (sketch) với fuse filter.
- <a href="https://www.youtube.com/watch?v=B_PexYrEcEw">HyperLogLog Hit Counter - Computerphile</a> — Computerphile, tiếng Anh. Minh họa ngắn gọn về HyperLogLog, làm rõ vì sao không cần lưu riêng từng khóa.
