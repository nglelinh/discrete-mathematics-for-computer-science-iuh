---
layout: post
title: "Ghi chú mở rộng: Biểu diễn tập hợp gọn (2022–2026)"
categories: chapter04
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---


Mỗi lần bạn gõ một địa chỉ web vào trình duyệt, hệ thống bảo mật phải kiểm tra xem đường dẫn đó có nằm trong danh sách hàng tỷ trang lừa đảo hay không—ngay trên chiếc điện thoại có bộ nhớ RAM hạn hẹp. Lưu nguyên danh sách hàng chục gigabyte là bất khả thi; giải pháp của khoa học máy tính hiện đại là nén toàn bộ tập hợp thành một **cấu trúc tập xấp xỉ gọn (compact approximate set)**, trong đó **Binary Fuse Filter (2022)** tiệm cận sát giới hạn lý thuyết thông tin nhất từ trước đến nay.

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Cấu trúc Tập hợp Xấp xỉ: Bloom Filter & HyperLogLog](/discrete-mathematics-for-computer-science-iuh/img/course/approximate_sets_hll.svg)

## Kiến thức cần nhớ: Ba trụ cột của Cấu trúc Biểu diễn Tập Xấp xỉ Gọn

1. **Hàm đặc trưng $$\mathbf{1}_S$$ & Cận dưới lý thuyết thông tin**:
   Một tập con $$S \subseteq U$$ tương đương với hàm đặc trưng $$\mathbf{1}_S : U \to \{0, 1\}$$. Nếu muốn lưu xấp xỉ $$S$$ với tỷ lệ dương tính giả không quá $$\varepsilon$$, lý thuyết thông tin chứng minh mọi cấu trúc dữ liệu đều cần ít nhất $$\log_2(1/\varepsilon)$$ bit cho mỗi phần tử.

2. **Sai số một phía do Nguyên lý Chuồng bồ câu**:
   Khi ngân sách bộ nhớ nhỏ hơn $$\log_2 \binom{\lvert U \rvert}{\lvert S \rvert}$$ bit, theo Nguyên lý Chuồng bồ câu chắc chắn có hai tập khác nhau chia sẻ cùng một trạng thái bộ nhớ—nên dương tính giả (*false positive*) là cái giá toán học bắt buộc để đổi lấy dung lượng siêu nhỏ, trong khi vẫn giữ tuyệt đối không có âm tính giả.

3. **Bước nhảy từ Bloom Filter đến Binary Fuse Filter (Graf & Lemire, 2022)**:
   Bloom filter cổ điển tốn tới $$\approx 1{,}44 \log_2(1/\varepsilon)$$ bit/phần tử (dư 44% so với cận lý thuyết). **Binary Fuse Filter** giải một hệ phương trình XOR thưa trên đồ thị phân đoạn, kéo dung lượng xuống chỉ còn **1,13x** (bản 3-wise) hoặc **1,08x** (bản 4-wise) cận dưới lý thuyết thông tin và xây dựng nhanh hơn gấp đôi Xor filter.

Một tập hữu hạn $$S \subseteq U$$ được xác định hoàn toàn bởi hàm đặc trưng $$\mathbf{1}_S : U \to \{0,1\}$$. Khi $$\vert S\vert$$ rất lớn và việc lưu trữ chính xác quá tốn kém, các hệ thống thường dùng **cấu trúc biểu diễn tập xấp xỉ gọn**: trả lời câu hỏi “$$x \in S$$?” với sai số một phía (có thể dương tính giả, không có âm tính giả).

Trong bài báo trên *ACM JEA* năm 2022, Graf và Lemire đề xuất *binary fuse filter* với dung lượng lưu trữ chỉ cách cận dưới lý thuyết thông tin khoảng **13%** (còn khoảng **8%** nếu chấp nhận truy vấn chậm hơn), đồng thời có tốc độ xây dựng thường nhanh gấp hơn hai lần so với xor filter. Nhóm tác giả cũng so sánh cấu trúc này với Bloom filter, blocked Bloom, cuckoo, ribbon và xor filter.

Dưới góc nhìn toán rời rạc: đối tượng được lưu vẫn là một cách biểu diễn của **tập hợp**; dương tính giả là hệ quả tất yếu của nguyên lý chuồng bồ câu khi số bit lưu trữ nhỏ hơn $$\log_2 \binom{\vert U\vert}{\vert S\vert}$$; và các tham số kỹ sư lựa chọn — gồm $$\vert S\vert$$, độ rộng dấu vân tay (fingerprint) và xác suất sai số — vẫn là những tham số của bài toán biểu diễn tập hợp.

Bạn nên đọc phần này sau các mục tập hợp bắt buộc để thấy một ví dụ từ năm 2022 về cách hệ thống thực tế mã hóa tập hợp khi bộ nhớ RAM bị giới hạn.

**Câu hỏi.** (1) Binary fuse filter là một tập con của $$U$$ hay là một *biểu diễn nén có mất mát* của tập con đó? (2) Phép toán tập hợp nào vẫn có chi phí thấp khi hệ thống chỉ lưu giữ bộ lọc này?

### Giải thích: Tính tay dung lượng RAM cho 10 triệu phần tử ở mức sai số $$\varepsilon \approx 0{,}39\%$$

Giả sử hệ thống cần lưu một tập tĩnh gồm $$\lvert S \rvert = 10{,}000{,}000$$ URL độc hại và yêu cầu tỷ lệ dương tính giả $$\varepsilon = 2^{-8} = \frac{1}{256} \approx 0{,}39\%$$ (tương ứng dấu vân tay dài $$f = 8$$ bit):

1. **Cận dưới lý thuyết thông tin (không thuật toán nào vượt qua được)**:
   $$\text{Số bit/khóa} = \log_2\!\left(\frac{1}{\varepsilon}\right) = \log_2(256) = \mathbf{8\text{ bit/khóa}} \implies 8 \times 10^7\text{ bit} = \mathbf{10{,}00\text{ MB}}.$$
2. **Bloom Filter chuẩn** (chi phí $$\frac{1}{\ln 2}\log_2(1/\varepsilon) \approx 1{,}4427 \times 8$$):
   $$\text{Số bit/khóa} \approx \mathbf{11{,}54\text{ bit/khóa}} \implies \mathbf{14{,}43\text{ MB}} \quad (\text{dư } 44{,}3\%).$$
3. **Binary Fuse Filter 3-wise (2022)** (chi phí $$\approx 1{,}13 \times 8$$):
   $$\text{Số bit/khóa} \approx \mathbf{9{,}04\text{ bit/khóa}} \implies \mathbf{11{,}30\text{ MB}} \quad (\text{chỉ dư } 13\%).$$
4. **Binary Fuse Filter 4-wise (2022)** (chi phí $$\approx 1{,}08 \times 8$$):
   $$\text{Số bit/khóa} \approx \mathbf{8{,}64\text{ bit/khóa}} \implies \mathbf{10{,}80\text{ MB}} \quad (\text{chỉ dư } 8\%).$$

Chỉ bằng cách đổi cấu trúc mã hóa tập hợp từ Bloom filter sang Binary Fuse Filter, hệ thống tiết kiệm được hơn **3,1–3,6 MB RAM** trên mỗi 10 triệu khóa mà không tăng thêm một phần nghìn sai số nào—lợi ích nhân lên thành hàng chục gigabyte trên hạ tầng cơ sở dữ liệu phân tán.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Giới thiệu tập xấp xỉ qua Bloom filter — trả lời câu hỏi thuộc tập với sai số một phía.
- <a href="https://www.youtube.com/watch?v=kfFacplFY4Y">What Are Bloom Filters?</a> — Spanning Tree, tiếng Anh. Giải thích cách mảng bit và hàm băm mã hóa một tập lớn trong bộ nhớ nhỏ.
- <a href="https://www.youtube.com/watch?v=mPxslXpg8wA">Advanced Data Structures: Count-Min Sketches</a> — Niema Moshiri, tiếng Anh. Giới thiệu Count-Min Sketch, thuộc cùng nhóm cấu trúc dữ liệu nén tập hợp và đa tập.
