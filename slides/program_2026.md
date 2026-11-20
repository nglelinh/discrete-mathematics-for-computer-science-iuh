# CHƯƠNG TRÌNH GIẢNG DẠY 2026
**Toán Rời Rạc cho Khoa học Máy tính**

**Tổng số tiết**: ~39 tiết × 45 phút *(tiết học có nội dung)*  
**Phiên bản**: 2026.5 (rút gọn sau Boolean; bỏ tiết 36–44 cũ)  
**Giảng viên**: Nguyễn Lê Linh

---

## Căn cứ đối chiếu

| Nguồn | Vai trò |
|-------|---------|
| [`README.md`](../README.md) | Khung chương trình tổng |
| [`contents/chapterNN/_posts/`](../contents/) | Bài học Jekyll (ưu tiên ch01–ch11, ch13) |

**Nguyên tắc v2026.5**:
- Giữ Phần I–IV (Logic → Quan hệ/Hàm → Đếm → Truy hồi) như v2026.4.
- **Phần V = Boolean đầy đủ** (tiết 30–38): lý thuyết + luyện tập + mạch.
- **Bỏ** block cũ tiết 36–44 (đồ thị, Big-O, số học, CSDL, SAT, cây) khỏi lộ trình bắt buộc — file đã archive.
- Tiết cuối = **tổng kết** (tiết 39).

**Kiểm tra**:
- **Tiết 10** — Kiểm tra 1: Logic + Chứng minh + Tập hợp
- **Tiết 23** — Kiểm tra giữa kỳ: Quan hệ + Hàm + Đếm
- **Thi cuối kỳ** — Lịch nhà trường (không chiếm tiết tổng kết)

---

## Thay đổi v2026.5 (so với v2026.4)

| V2026.4 | V2026.5 |
|---------|---------|
| Tiết 36–37 Đồ thị | **Bỏ** (archive) |
| Tiết 38–39 Big-O / độ phức tạp | **Bỏ** (archive) |
| Tiết 40–41 Số học / RSA | **Bỏ** (archive) |
| Tiết 42–43 CSDL / SAT | **Bỏ** (archive) |
| Tiết 44 Cây | **Bỏ** (archive) |
| Tiết 45 Tổng kết | → **Tiết 39** Tổng kết |
| — | **Tiết 36** Bài tập hàm Boole |
| — | **Tiết 37** Phương pháp đơn giản hóa hàm Boole |
| — | **Tiết 38** Mạch logic tổ hợp |

**Archive**: `slides/archive/obsolete-v2026.5-post36-44/`

---

## Cấu trúc tổng thể

| Phần | Tiết | Nội dung |
|------|------|----------|
| **I** | 1–10 | Logic, chứng minh, tập hợp → **KT1** |
| **II** | 11–15 | Quan hệ, hàm |
| **III** | 16–23 | Đếm → **KT giữa kỳ** |
| **IV** | 24–29 | Truy hồi + ôn số phức / ôn HTTH (tiết 28–29) |
| **V** | 30–38 | **Boolean**: đại số → hàm → cổng → K-map/QM → luyện → mạch |
| **VI** | 39 | **Tổng kết** + feedback |

---

## Bảng tiết — map `contents/` (rút gọn)

| Tiết | Chủ đề | Tham chiếu | Slide |
|------|--------|------------|-------|
| 1–29 | *(giữ như v2026.4 — xem git history / README)* | ch01–ch11 | `tiet-01` … |
| 30 | Đại số Boolean | ch13 `13_01` | `tiet-30-dai-so-boole.md` |
| 31 | Hàm Boolean | ch13 `13_02` | `tiet-31-ham-boole.md` |
| 32 | Cổng logic & tối thiểu hóa | ch13 `13_03` | `tiet-32-cong-logic.md` |
| 33 | Bản đồ Karnaugh | ch13 `13_04` | `tiet-33-karnaugh.md` |
| 34 | Quine–McCluskey | ch13 `13_05` | `tiet-34-quine-mccluskey.md` |
| 35 | Boolean — ứng dụng | ch13 `13_06` | `tiet-35-boole-ung-dung.md` |
| 35b | Mạch cộng, nhân | ch13 `13_07` | `tiet-35b-mach-cong-nhan.md` |
| **36** | **Bài tập hàm số Boole** | ch13 `13_02` | `tiet-36-bai-tap-ham-boole.md` **mới** |
| **37** | **Phương pháp đơn giản hóa hàm Boole** | ch13 `13_03`–`13_05` | `tiet-37-don-gian-hoa-ham-boole.md` **mới** |
| **38** | **Mạch logic tổ hợp** | ch13 `13_03`, `13_07` | `tiet-38-mach-logic.md` **mới** |
| **39** | **Tổng kết khóa học** | — | `tiet-39-tong-ket.md` |

### Chi tiết block Boolean (30–38)

| Tiết | Mục tiêu giảng |
|------|----------------|
| 30 | Tiên đề, hằng đẳng thức, De Morgan |
| 31 | Bảng, minterm/maxterm, SOP/POS |
| 32 | Cổng, mạch hai tầng, rút đại số |
| 33 | K-map 2–4 biến |
| 34 | Quine–McCluskey |
| 35–35b | Bối cảnh + half/full adder, MUX… |
| **36** | **Luyện thuần**: SOP/POS, chuyển đổi, majority, code→hàm |
| **37** | **Tổng hợp 3 phương pháp** rút gọn + chọn tool |
| **38** | **Mạch**: 5 bước thiết kế, đếm cổng/tầng, half adder, MUX |

---

## Đánh giá

| Hạng mục | Tỷ lệ | Gắn với tiết |
|----------|-------|--------------|
| Kiểm tra TX + Bài tập | 20% | KT1 (10), bài `contents/` |
| Giữa kỳ | 30% | Tiết 23 |
| Cuối kỳ | 50% | Lịch thi riêng — **không** dùng tiết 39 |

---

## Ghi chú giảng viên

1. Mỗi tiết 45′: mục tiêu → nội dung → thực hành → **bài tập ôn tập** cuối slide.
2. **Không** có tiết ôn thi riêng; ôn qua bài tập cuối slide + website.
3. Tiết **36–38** là **luyện + hệ thống hóa** Boolean — ưu tiên làm bài trên lớp.
4. Nội dung đã archive (đồ thị, Big-O, RSA, CSDL, SAT, cây): có thể giao **tự học** hoặc mở lại ở kỳ sau.
5. `css: slides/center-content.css` bắt buộc trên mọi slide mới.

---

## Việc cần làm tiếp

- [x] Archive `tiet-36`…`tiet-44` (v2026.4) → `obsolete-v2026.5-post36-44/`
- [x] Thêm `tiet-36` bài tập hàm Boole, `tiet-37` đơn giản hóa, `tiet-38` mạch
- [x] Tổng kết → `tiet-39-tong-ket.md`
- [ ] (Tuỳ chọn) Cập nhật `tiet-01` nếu vẫn nói “45 tiết”
- [ ] (Tuỳ chọn) Khôi phục đồ thị/cây thành module tự học

---

**Cập nhật lần cuối**: 2026-07-19 (v2026.5)  
**Nguồn**: `contents/chapter13/`, Rosen, Nguyễn Hữu Anh.
