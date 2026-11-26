---
layout: post
title: "Ghi chú mở rộng: Hàm sinh gặp bộ lọc năm 2022"
categories: chapter11
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú tùy chọn song ngữ: cận lưu trữ của binary fuse filter (JEA 2022) nhìn từ góc độ bài toán đếm, hàm sinh và nguyên lý bao hàm–loại trừ."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Tổ hợp Giải tích: Từ Hàm sinh tới Điểm cực Phức](/discrete-mathematics-for-computer-science-iuh/img/course/analytic_combinatorics_poles.svg)

Hàm sinh thông thường đóng gói một dãy đếm $$(a_n)$$ thành $$A(x) = \sum a_n x^n$$. Cận dưới về dung lượng lưu trữ cho cấu trúc biểu diễn tập xấp xỉ cũng thuộc cùng dạng bài toán đếm này: có bao nhiêu bộ lọc $$m$$ bit phân biệt nhau, và chúng cần phân tách bao nhiêu tập $$n$$ phần tử với tỷ lệ dương tính giả không vượt quá $$\varepsilon$$?

Graf và Lemire (JEA 2022) chỉ ra rằng bộ lọc binary fuse chỉ vượt cận dưới lý thuyết thông tin khoảng **13%** (hoặc **8%**). Bản thân cận dưới đó là một lập luận đếm / hàm sinh: số mẫu trạng thái “có” biểu diễn được không thể nhỏ hơn số tập hợp mà bộ lọc cần phân biệt. Nguyên lý bao hàm–loại trừ xuất hiện khi ước lượng xác suất va chạm trên nhiều vị trí băm — tương tự mối quan hệ giữa cận hợp (union bound) và phép đếm chính xác trong bài toán derangement.

Ghi chú này không xây dựng thêm đồng nhất thức hàm sinh mới, mà giới thiệu một cấu trúc dữ liệu năm 2022 trong đó con số tiêu biểu (phần trăm vượt trên cận dưới) chỉ thực sự có ý nghĩa khi được hiểu dưới góc độ lập luận đếm.

**Câu hỏi.** (1) Hàm sinh nào có thể mã hóa “số lượng bộ lọc $$m$$ bit”? (2) Nguyên lý bao hàm–loại trừ xuất hiện ở bước nào khi tính tỷ lệ dương tính giả với ba vị trí băm?

### Kiến thức cần nhớ: Phép đếm, Hàm sinh và Bao hàm – Loại trừ thiết lập cận dưới bộ lọc ra sao?

- **Cận dưới lý thuyết thông tin từ phép đếm:** Mọi cấu trúc dữ liệu biểu diễn tập con $$n$$ phần tử với tỷ lệ dương tính giả $$\le \varepsilon$$ đều cần phân tách $$\binom{\vert U \vert}{n}$$ tập bằng $$2^m$$ trạng thái bit, kéo theo cận cứng $$m \ge n\log_2(1/\varepsilon)$$ bit.
- **Hàm sinh & Ngưỡng bóc vỏ siêu đồ thị (Hypergraph Peeling):** Binary fuse filter dựng siêu đồ thị băm bậc 3 rồi "bóc" dần các đỉnh bậc 1; tổ hợp giải tích (dùng hàm sinh phân tích lõi siêu đồ thị ngẫu nhiên) dự đoán chính xác ngưỡng tải (~87%–92%) để quá trình bóc vỏ thành công.
- **Bao hàm – Loại trừ cho va chạm đa hàm băm:** Khi kiểm tra $$k$$ vị trí băm, xác suất có ít nhất một vị trí báo `0` (loại bỏ đúng phần tử ngoại lai) chính là tổng xen kẽ của Nguyên lý Bao hàm – Loại trừ.

### Giải thích: Tính tay Bao hàm – Loại trừ cho 3 vị trí băm
1. **Bước 1 — Thiết lập bài toán:** Giả sử mỗi phép tra cứu kiểm tra $$k = 3$$ vị trí băm độc lập, xác suất mỗi vị trí đang là bit `1` là $$0{,}2$$ (suy ra xác suất gặp bit `0` là $$\Pr(A_i) = 0{,}8$$).
2. **Bước 2 — Tính xác suất loại bỏ đúng (có ít nhất một bit `0`) bằng Bao hàm – Loại trừ:**
   $$\Pr(A_1 \cup A_2 \cup A_3) = 3(0{,}8) - 3(0{,}8)^2 + (0{,}8)^3 = 2{,}4 - 1{,}92 + 0{,}512 = 0{,}992.$$
3. **Bước 3 — Suy ra tỷ lệ dương tính giả & cận bit:** Phần tử chỉ lọt qua nhầm khi không có vị trí nào là `0`, nên $$\varepsilon = 1 - 0{,}992 = 0{,}008$$. Theo cận đếm, muốn đạt $$\varepsilon = 0{,}008$$ cần tối thiểu $$\log_2(1/0{,}008) = \log_2(125) \approx 6{,}97$$ bit/khóa — chính là mốc chuẩn để Binary Fuse Filter (2022) chứng minh mức dư chỉ 8%–13%!

$$m \ge n\log_2(1/\varepsilon), \qquad \Pr\!\left(\bigcup_{i=1}^3 A_i\right) = \sum \Pr(A_i) - \sum \Pr(A_i \cap A_j) + \Pr(A_1 \cap A_2 \cap A_3).$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=-drdeNMoe8w">GENERATING FUNCTIONS - Discrete Mathematics</a> — TrevTutor, tiếng Anh. Giới thiệu hàm sinh — công cụ đếm có cùng bản chất với cận lưu trữ của bộ lọc.
- <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Minh họa Bloom filter và ngân sách bit khi biểu diễn tập xấp xỉ.
- <a href="https://www.youtube.com/watch?v=eV1haPUt0NU">Hyperloglog: Facebook&#x27;s algorithm to count distinct elements</a> — Gaurav Sen, tiếng Anh. Bài toán ước lượng lực lượng tập hợp, cùng hướng tiếp cận lý thuyết thông tin với fuse filter.
