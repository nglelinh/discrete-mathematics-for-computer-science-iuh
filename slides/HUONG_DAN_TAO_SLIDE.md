# Hướng dẫn Tạo Slide Bài Giảng (Obsidian)

**Quan trọng**: Tất cả slide được xây dựng theo **CHƯƠNG TRÌNH GIẢNG DẠY 2026** (xem file `slides/program_2026.md`).

Tài liệu này hướng dẫn cách tạo **slide Markdown** để trình bày trong Obsidian, phù hợp với các tiết học **45 phút** của môn **Toán Rời Rạc cho Khoa học Máy tính — IUH**.

## Yêu cầu

- **Obsidian** (phiên bản mới nhất)
- Plugin: **Advanced Slides** (khuyến nghị) hoặc **Slides**
  - Cài trong Obsidian → Community plugins → Tìm "Advanced Slides"
- Hỗ trợ **MathJax** (thường có sẵn trong Obsidian hoặc bật qua plugin)

## Cấu trúc Frontmatter (bắt buộc)

Mỗi file slide bắt đầu bằng:

**Lưu ý theme**: Đã chuyển sang `theme: white` (light, clean, phù hợp teaching slide style). Tránh dark themes như black.

```yaml
---
theme: beige
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---
```

**Giải thích:**
- `timeForPresentation: 2700` → 45 phút (45 × 60)
- `theme: white` → nền sáng, phù hợp giảng dạy
- `slideNumber`, `transition`, `enableTimeBar` → bật tính năng trình bày

## Quy ước đặt tên file

- `tiet-XX-ten-chu-de.md`
- Ví dụ:
  - `tiet-01-gioi-thieu.md`
  - `tiet-06-logic-vi-tu.md`
  - `tiet-07-chung-minh-truc-tiep.md`

Giữ thứ tự tăng dần theo tiến độ môn học.

## Cấu trúc một tiết học 45 phút (gợi ý)

| Phần                  | Thời lượng     | Số slide gợi ý | Mục đích |
|-----------------------|----------------|----------------|----------|
| Tiêu đề + Giới thiệu  | 2–3 phút       | 1–2            | Tạo context |
| Mục tiêu tiết học     | 1–2 phút       | 1              | Học viên biết cần đạt gì |
| Nội dung chính        | 18–22 phút     | 8–14           | Khái niệm + ví dụ + ứng dụng |
| Thực hành / Thảo luận | 8–12 phút      | 2–4            | Làm bài tập ngắn |
| Tóm tắt + Bài tập ôn tập | 3–4 phút    | 1–2            | Củng cố + giao bài về nhà |
| **Tổng**              | **~45 phút**   | **12–20**      | — |

**Quy tắc vàng (áp dụng cho TẤT CẢ slide):**
- Mỗi slide (giữa 2 dấu ---) **chỉ 5-7 dòng** tối đa.
- Nếu một block dài → tách ngay thành nhiều slide nhỏ.
- Ưu tiên: 1 ý chính + bảng ngắn hoặc 4-6 bullet ngắn + 1 ví dụ ngắn.
- Bổ sung "rule" (luật, quy tắc, định lý) thành slide riêng nếu cần.

## Bắt buộc: Bài tập ôn tập ở cuối mỗi slide

**Mọi slide deck phải có phần "Bài tập ôn tập" ngay trước "Tiết sau" và "Câu hỏi?".**

### Thiết kế bài tập ôn tập
- **Số lượng**: 4–6 bài (không quá nhiều)
- **Độ khó tăng dần**:
  1. Hiểu / nhớ định nghĩa, khái niệm
  2. Nhận biết, tính toán, bảng chân trị đơn giản
  3. Viết biểu thức logic / code / mô hình hóa yêu cầu
  4. Phân tích / chứng minh / mở rộng ứng dụng
- Kết hợp nhiều loại:
  - Câu hỏi lý thuyết
  - Viết công thức + giải thích
  - Chuyển từ tiếng Việt → logic hoặc code
  - Một bài hơi khó hơn để sinh viên tư duy
- Lấy cảm hứng trực tiếp từ phần **## Bài tập thực hành** trong `contents/chapter*/_posts/*.md`

### Ví dụ cấu trúc bài tập ôn tập
```markdown
# Bài tập ôn tập

1. Xác định câu nào là mệnh đề và cho giá trị chân lý.
2. Đặt biến và viết biểu thức logic cho điều kiện sau: ...
3. Lập bảng chân trị cho ...
4. Viết đoạn code Python tương đương với biểu thức ...
5. (Thách thức) Mô hình hóa yêu cầu nghiệp vụ phức tạp hơn.
```

Phần này giúp sinh viên **ôn tập ngay sau tiết học** và tạo tài liệu tự học tốt.

## Yêu cầu quan trọng: Nội dung phong phú – Đầy đủ định nghĩa và định lý

**Mỗi bài học slide phải có nội dung đầy đủ, phong phú**, không chỉ ví dụ và thực hành.

### Hướng dẫn tăng chiều sâu (Depth Guidelines) - Áp dụng cho TẤT CẢ slide

Để tăng chiều sâu cho slide (yêu cầu "lam tat ca"):

**Bắt buộc thêm các phần sau vào hầu hết các tiết:**

1. **Chứng minh / Sketch chứng minh**:
   - Ít nhất 1-2 định lý quan trọng có ý tưởng chứng minh hoặc chứng minh ngắn (bằng bảng chân trị, quy nạp, mâu thuẫn, hoặc trực tiếp).

2. **Edge Cases & Counterexamples**:
   - Thêm ít nhất 1-2 ví dụ biên hoặc phản ví dụ để làm rõ giới hạn.

3. **Deep CS Applications** (tăng chiều sâu):
   - Kết nối với thuật toán thực tế (ví dụ: RSA, Dijkstra, Merge Sort, Hash collision, Topo sort, SQL optimization).
   - Thảo luận về hệ quả: hiệu quả, bảo mật, lỗi phổ biến, hoặc trade-off.

4. **Rigorous Properties & Notation**:
   - Thêm danh sách tính chất chính thức, corollaries, hoặc định lý bổ sung.

5. **Cross-topic Connections**:
   - Thêm 1 phần "Liên hệ" với các chủ đề khác trong chương trình (Logic ↔ Chứng minh ↔ Truy hồi ↔ Đồ thị...).

6. **Historical / Foundational Context** (khi phù hợp):
   - Ngắn gọn về người phát hiện hoặc tầm quan trọng lịch sử.

7. **Bài tập ôn tập nâng cao**:
   - Có ít nhất **1 bài thách thức** yêu cầu chứng minh, phân tích sâu, hoặc mô hình hóa phức tạp.
   - Phân cấp: Cơ bản → Trung bình → Nâng cao.

**Mục tiêu cuối cùng**:
Slide giúp sinh viên không chỉ "biết" mà còn "hiểu sâu", "chứng minh được", và "áp dụng vào hệ thống thực tế".

Mỗi slide nên nhắm đến mức độ "university level + practical CS application".

Ví dụ cấu trúc sâu hơn cho một khái niệm:
- Định nghĩa hình thức
- Tính chất / Định lý (kèm chứng minh ngắn)
- Edge cases
- Ứng dụng cơ bản + Ứng dụng nâng cao (CS)
- Ví dụ code / SQL chi tiết
- Bài tập thực hành sâu

### Bắt buộc phải có
1. **Định nghĩa chính xác** (formal definition) cho mọi khái niệm quan trọng.
   - Ví dụ: Định nghĩa Mệnh đề, Mệnh đề sơ cấp, Phép kéo theo, Tương đương logic, DNF, CNF, Quy tắc suy diễn...
   - Đặt riêng một slide hoặc một phần rõ ràng, dùng **bold** + công thức.

2. **Bảng chân trị đầy đủ** khi giới thiệu phép toán.

3. **Danh sách đầy đủ các luật / định lý** liên quan đến bài học:
   - Luật logic (De Morgan, Phân phối, Bù, Hấp thụ, Giao hoán, Kết hợp, Phủ định kép, Đồng nhất...)
   - Định lý về sự tồn tại và duy nhất của DNF/CNF đầy đủ
   - Các quy tắc suy diễn (Modus Ponens, Modus Tollens, Tam đoạn luận giả định, Tam đoạn luận tuyển, Mâu thuẫn...)

4. **Ký hiệu hình thức**:
   - Sử dụng đúng ký hiệu: \(\to, \leftrightarrow, \equiv, \vdash, \therefore\)
   - Đưa ra dạng dòng suy diễn khi dạy quy tắc suy diễn.

5. **Cấu trúc slide khuyến nghị cho mỗi khái niệm lớn**:
   - Slide 1: Định nghĩa (formal)
   - Slide 2: Bảng / Tính chất
   - Slide 3: Ví dụ + Ứng dụng thực tế (code, CSDL)
   - Slide 4: Luật / Định lý liên quan

### Nguyên tắc khi tóm tắt từ nội dung
- Không bỏ bớt định nghĩa cốt lõi chỉ để "ngắn gọn".
- Giữ đầy đủ các luật quan trọng (kể cả nếu chỉ liệt kê bảng).
- Có thể rút gọn ví dụ, nhưng **không rút gọn định nghĩa hoặc định lý**.
- Ưu tiên độ chính xác và đầy đủ hơn là số lượng slide ít.

**Mục tiêu**: Sau khi xem slide, sinh viên có thể tra cứu lại định nghĩa và các luật/định lý mà không cần xem lại bài giảng gốc.

### Review Checklist (tự review trước khi dùng slide)

- [ ] Có định nghĩa hình thức rõ ràng?
- [ ] Có ít nhất 1-2 định lý + sketch chứng minh hoặc ý tưởng?
- [ ] Có edge case / counterexample?
- [ ] Có ứng dụng nâng cao (thuật toán thực tế, bảo mật, CSDL)?
- [ ] Có kết nối với chủ đề khác?
- [ ] Bài tập ôn tập có bài thách thức + yêu cầu chứng minh?
- [ ] Code / SQL ví dụ chi tiết và giải thích?

## Mẹo viết nội dung tốt

- Mỗi slide chỉ **1 ý chính** (nhưng ý chính đó phải đầy đủ)
- Dùng bảng, code, ví dụ thực tế nhiều hơn văn bản dài
- Thực hành có **thời gian rõ ràng**
- Giữ giọng điệu ngắn gọn, ứng dụng CNTT

## Quy trình tạo slide từ nội dung khóa học

1. **Nhận topic** từ giảng viên (ví dụ: "Phép toán logic", "Chứng minh quy nạp", "Nguyên lý chuồng bồ câu").
2. **Tìm nội dung nguồn** trong:
   - `contents/chapterXX/_posts/*.md`
   - `material/*.pdf` (nếu cần tài liệu gốc)
3. **Tóm tắt** thành các điểm ngắn, ưu tiên:
   - Định nghĩa chính xác
   - Ví dụ minh họa (toán + code + CSDL)
   - Ứng dụng thực tế trong CNTT
4. **Thiết kế thực hành** ngắn (5–12 phút), có câu hỏi rõ ràng.
5. **Viết slide** theo template bên dưới.
6. **Kiểm tra** bằng cách mở file trong Obsidian → Start Slideshow (Advanced Slides).

## Template Slide 45 Phút (copy-paste để bắt đầu)

Tạo file mới, dán toàn bộ khối dưới đây rồi chỉnh sửa:

```markdown
---
theme: black
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

# Tên Tiết Học

**Toán Rời Rạc — IUH**

Tiết XX (45 phút) — Chủ đề ngắn gọn

---

# Mục tiêu tiết học

- Hiểu định nghĩa / khái niệm chính
- Phân biệt A và B
- Áp dụng vào code / CSDL
- Thực hành viết biểu thức / chứng minh

---

# Khái niệm 1

**Định nghĩa ngắn gọn**

- Điểm 1
- Điểm 2

Ví dụ:

> "Nếu ... thì ..."

---

# Ví dụ thực tế

Ứng dụng trong lập trình:

```python
# ví dụ code
if p and (not q or r):
    ...
```

---

# Bảng / So sánh

| A | B | Ý nghĩa |
|:--|:--|:--|
|   |   |     |

---

# Thực hành 1 (8 phút)

Câu hỏi / bài tập:

1. ...
2. ...

Làm theo nhóm hoặc cá nhân.

---

# Tóm tắt

- Ý 1
- Ý 2
- Ý 3

---

# Tiết sau

**Chủ đề tiếp theo**

- Nội dung chính
- ...

---

# Câu hỏi?
```

## Bắt buộc: Bài tập ôn tập ở cuối slide

**Mọi file slide phải có phần "Bài tập ôn tập" ở cuối cùng** (sau Tóm tắt).

Xem chi tiết ở phần "Bắt buộc: Bài tập ôn tập ở cuối mỗi slide" bên dưới.

## Thu thập thông tin từ course content

Ví dụ topic "Phép toán logic":

- Đọc: `contents/chapter01/_posts/21-01-01-01_02_Logical_Operators.md`
- Lấy: định nghĩa, bảng chân trị, ví dụ đăng nhập, ví dụ SQL, lỗi thường gặp.
- Chuyển thành: 1-2 slide định nghĩa + bảng + 2-3 ví dụ code + 1 slide thực hành.

**Không copy nguyên văn** — tóm tắt, chuyển sang dạng slide dễ trình bày.

## Lưu ý khi chuyển sang 45 phút

- Các file `tiet-*.md` hiện tại dùng `7200` (2 giờ). Khi tạo slide mới → dùng `2700`.
- Có thể tách các tiết 2 giờ cũ thành 2–3 tiết 45 phút nếu cần.
- Giữ tính ứng dụng mạnh (code, database, bảo mật, AI).

## Bắt buộc: Bài tập ôn tập ở cuối mỗi slide

**Mọi slide deck phải kết thúc bằng phần "Bài tập ôn tập"**.

### Vị trí
- Đặt sau phần **Tóm tắt**, trước **Tiết sau** và **Câu hỏi?**

### Yêu cầu nội dung
- 4–6 bài tập (tối đa 6 để không quá tải).
- Độ khó tăng dần:
  1. Nhớ định nghĩa / khái niệm cơ bản
  2. Bài tập tính toán / nhận diện đơn giản
  3. Áp dụng vào ví dụ thực tế hoặc code
  4. Mô hình hóa yêu cầu nghiệp vụ hoặc chứng minh
  5. Bài nâng cao / thảo luận (tùy chọn)
- Nên lấy cảm hứng từ phần **Bài tập thực hành** trong các file `contents/chapterXX/_posts/`
- Viết rõ ràng, ngắn gọn, có thể làm trong 15–30 phút tổng cộng.
- Có thể thêm ghi chú: "(Về nhà)" hoặc "(Thảo luận tiết sau)".

### Ví dụ tiêu đề
```markdown
# Bài tập ôn tập

Làm các bài sau để củng cố kiến thức:

1. **Bài 1**: ...
2. ...
```

### Lợi ích
- Giúp sinh viên ôn tập ngay sau tiết học
- Tạo thói quen thực hành
- Dễ dùng để kiểm tra nhanh đầu tiết sau
```

I need to insert this in a good place in the instructions.

## Kiểm tra trước khi dạy

1. Mở file trong Obsidian.
2. Command palette → "Start Slideshow" (Advanced Slides).
3. Kiểm tra thời gian, công thức render đúng, code hiển thị đẹp.
4. Thử trình bày 1 vòng nhanh để ước lượng thời gian thực.

---

**Liên hệ**: nglelinh@gmail.com  
**Nguồn nội dung**: `contents/` + `material/`

Chúc giảng dạy hiệu quả!
```

This gives a solid instruction. Now create a clean, copyable template file.