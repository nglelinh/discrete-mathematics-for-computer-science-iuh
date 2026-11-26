---
layout: post
title: "Ghi chú mở rộng: Cận chuồng bồ câu trong bộ lọc hiện đại (2022–2026)"
categories: chapter08
date: 2021-01-01
order: 4
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Nguyên lý Chuồng bồ câu trong Count-Min Sketch](/discrete-mathematics-for-computer-science-iuh/img/course/sketch_filters_pigeonhole.svg)

Nguyên lý Dirichlet giải thích vì sao không thể xây dựng một cấu trúc kiểm tra phần tử thuộc tập (membership) vừa **chính xác tuyệt đối** vừa siêu gọn: khi số khóa (bồ câu) lớn hơn số mẫu bit khả dĩ (chuồng), va chạm chắc chắn xảy ra. Các cấu trúc kiểm tra xấp xỉ chấp nhận một tỷ lệ dương tính giả $$\varepsilon$$, rồi đặt câu hỏi bộ nhớ cần dùng tiến gần đến cận dưới lý thuyết thông tin $$\approx n \log_2(1/\varepsilon)$$ bit (cho $$n$$ khóa) đến mức nào.

Trong công trình trên tạp chí *J. Exp. Algorithmics* (2022), Graf và Lemire báo cáo bộ lọc **binary fuse filter** chỉ lớn hơn cận dưới lý thuyết khoảng **13%** (hoặc khoảng **8%** nếu dùng bố cục chậm hơn), vượt qua xor filter về dung lượng bộ nhớ và thường nhanh hơn về thời gian xây dựng, đồng thời so sánh trực tiếp với các bộ lọc Bloom, cuckoo và ribbon.

Điểm đáng rút ra cho Chương 8 là cuộc đua tối ưu các cấu trúc dữ liệu bộ lọc thực chất là một bài toán chuồng bồ câu định lượng. Hiện tượng va chạm trong bảng băm (đã học ở phần bắt buộc) có cùng bản chất, chỉ khác cách tổ chức bộ nhớ. Binary fuse filter không phá vỡ nguyên lý Dirichlet; thay vào đó, khi đã chấp nhận một số ngăn chứa phải dùng chung, chúng sử dụng từng bit bộ nhớ một cách tiết kiệm hơn.

**Câu hỏi.** (1) Nếu yêu cầu $$\varepsilon = 0$$ với $$n > m$$ dấu vân tay (fingerprint), định lý nào của chương này được áp dụng? (2) Vì sao phát biểu “cao hơn cận dưới 13%” mang bản chất của nguyên lý chuồng bồ câu chứ không phải học máy?


### Kiến thức cần nhớ: Cận Chuồng bồ câu trong Bộ lọc Xác suất Hiện đại

1. **Tập chính xác vs. Bộ lọc xấp xỉ:** Lưu chính xác $$n$$ khóa 64-bit tốn ít nhất $$64n$$ bit. Trong RocksDB hay bộ định tuyến CDN, các bộ lọc **Bloom**, **Xor** và **Ribbon** chấp nhận tỷ lệ dương tính giả nhỏ $$\varepsilon$$ để tiết kiệm gấp nhiều lần RAM.
2. **Sàn lý thuyết từ Nguyên lý Chuồng bồ câu:** Bằng phép đếm chuồng bồ câu, *mọi* bộ lọc thành viên tĩnh có tỷ lệ dương tính giả $$\varepsilon$$ bắt buộc tốn tối thiểu **$$\log_2(1/\varepsilon)$$ bit cho mỗi khóa**!
3. **Bộ lọc tĩnh 2022–2026 (Binary Fuse & Ribbon):** Bộ lọc Binary Fuse (Graf & Lemire, 2022) tiến sát sàn lý thuyết chỉ còn dư $$8\text{–}13\%$$ — gọn hơn hẳn mức dư $$44\%$$ ($$1.44\log_2(1/\varepsilon)$$) của Bloom filter kinh điển!

### Giải thích: Tính tay số MB RAM cho 10 triệu khóa ở mức $$\varepsilon = 1/256$$
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
