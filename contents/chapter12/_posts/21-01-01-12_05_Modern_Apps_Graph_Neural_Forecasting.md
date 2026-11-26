---
layout: post
title: "Ghi chú mở rộng: Đồ thị dự báo thời tiết (2022–2026)"
categories: chapter12
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Dự báo Chuỗi thời gian trên Đồ thị Không–Thời gian](/discrete-mathematics-for-computer-science-iuh/img/course/graph_neural_forecasting.svg)

GraphCast (Lam và cộng sự, *Science* 2023) là một mạng nơ-ron đồ thị (GNN) hoạt động theo kiến trúc encode–process–decode:

- **Grid2Mesh**: đồ thị hai phía ánh xạ từ lưới kinh–vĩ độ sang lưới đa phân giải (**multi-mesh**) dạng khối hai mươi mặt (icosahedral);
- **Mesh**: thực hiện truyền thông điệp (message passing) trên các đỉnh và cạnh của lưới;
- **Mesh2Grid**: đồ thị hai phía ánh xạ kết quả trở lại lưới kinh–vĩ độ.

Theo công bố, hệ thống có thể dự báo hàng trăm biến khí tượng trong 10 ngày ở độ phân giải toàn cầu $$0.25^\circ$$ trong vòng dưới một phút, đồng thời đạt độ chính xác cao hơn mô hình tất định chuẩn vận hành trên **90% trong tổng số 1380** chỉ tiêu kiểm chứng, bao gồm dự báo xoáy thuận, sông khí quyển và các hiện tượng thời tiết cực đoan.

Chương 12 đã giới thiệu cấu trúc $$G = (V,E)$$, quan hệ kề và đường đi. GraphCast cho thấy các khái niệm này có thể mở rộng lên quy mô toàn cầu: $$V$$ là tập đỉnh trên lưới phủ bề mặt Trái Đất, $$E$$ mã hóa các láng giềng cục bộ và đa tỷ lệ, còn quá trình tính toán gồm một số bước tổng hợp thông tin từ láng giềng cố định. Ngay cả khi không chuyên về khí tượng học, ta vẫn dễ nhận ra cơ chế lan truyền thông tin trên đồ thị tương tự cách mở rộng theo tầng của BFS.

**Câu hỏi.** (1) Grid2Mesh là đồ thị vô hướng đơn, đồ thị hai phía hay đa đồ thị — giải thích vì sao? (2) Bạn sẽ chọn cách biểu diễn nào trong Chương 12 để lưu trữ một lưới icosahedral tĩnh?

### Kiến thức cần nhớ: Lý thuyết đồ thị vận hành mô hình dự báo thời tiết GraphCast ra sao?

- **Đồ thị hai phía (`Grid2Mesh` & `Mesh2Grid`):** Lưới kinh–vĩ độ $$0{,}25^\circ$$ bị dồn dày bất thường ở hai cực Trái Đất; GraphCast dùng đồ thị hai phía để chuyển dữ liệu sang một lưới khối hai mươi mặt (icosahedral mesh) phủ đều toàn cầu.
- **Đa lưới thưa & Biểu diễn CSR:** Chồng nhiều cấp độ lưới thô–mịn trên cùng tập đỉnh tạo ra đồ thị thưa ($$\vert E \vert = O(\vert V \vert)$$) có cả cạnh ngắn cục bộ lẫn "đường cao tốc" xuyên lục địa, phù hợp lưu bằng danh sách cạnh / CSR thay vì ma trận kề.
- **Truyền thông điệp như BFS khả vi:** Mỗi lớp GNN cập nhật trạng thái đỉnh từ láng giềng cách 1 bước; xếp chồng $$K$$ lớp cho phép thông tin khí tượng lan xa đúng bán kính $$K$$ bước trên đồ thị — phiên bản khả vi của duyệt BFS $$K$$ tầng!

### Giải thích: Tính tay quy mô đỉnh và lợi ích nén bộ nhớ của lưới GraphCast
1. **Bước 1 — Đếm số đỉnh lưới kinh–vĩ độ ở độ phân giải $$0{,}25^\circ$$:** Kinh độ $$360^\circ / 0{,}25^\circ = 1\,440$$ điểm, vĩ độ $$180^\circ / 0{,}25^\circ + 1 = 721$$ điểm $$\Rightarrow \vert V_{\text{grid}} \vert = 1\,440 \times 721 = 1\,038\,240$$ đỉnh!
2. **Bước 2 — So sánh ma trận kề vs. danh sách kề trên lưới 40.962 đỉnh:** Ma trận kề dày đặc cần $$40\,962^2 \approx 1{,}68$$ tỷ ô (~6,7 GB), trong khi danh sách cạnh / CSR với bậc trung bình ~12 chỉ tốn ~490.000 cạnh (~4 MB) — **nhỏ hơn hơn 1.600 lần**!
3. **Bước 3 — Sức mạnh của cạnh đa tỷ lệ:** Nhờ các cạnh dài từ lưới thô rút ngắn đường kính đồ thị, chỉ **16 bước truyền thông điệp** đã đủ kết nối luồng khí quyển tầm xa và chạy dự báo 10 ngày dưới 1 phút.

$$\vert V_{\text{grid}} \vert \approx 1{,}04 \times 10^6 \;\xrightarrow{\text{Grid2Mesh (Hai phía)}}\; \vert V_{\text{mesh}} \vert = 40\,962 \;\xrightarrow{16\text{ tầng GNN (CSR)}}\; \text{Dự báo 10 ngày } < 1\text{ phút.}$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích những kết quả thực tế của GraphCast khi chạy truyền thông điệp trên đồ thị đa lưới.
- <a href="https://www.youtube.com/watch?v=1DmNdMUbDkg">Message Passing: How Graph Neural Networks Actually Work</a> — The Synthetic Mind, tiếng Anh. Giải thích cơ chế truyền thông điệp (message passing) trong mạng nơ-ron đồ thị.
