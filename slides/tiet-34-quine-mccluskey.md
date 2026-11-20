---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Quine–McCluskey

**Toán Rời Rạc** · Chương 13 · Bài 13.5

Tiết 34 (45 phút)

---

## Mục tiêu tiết học

- Hai phần Quine–McCluskey (thu gọn + tối thiểu)
- **Phép dán** → **nguyên nhân nguyên tố**
- Bảng phủ → **nguyên tố cốt yếu**
- Don't-care trong QM
- So với K-map

---

## Khi nào dùng QM?

| | K-map | QM |
|:---|:---|:---|
| Biến | 2–4 | Hệ thống hơn |
| Dạng | Lưới | **Bảng** |
| Lập trình | Khó | Dễ |

Cùng mục tiêu: **SOP (tổng các tích)** tối tiểu

---

## Hình: tabulation

![QM](../img/course/quine_mccluskey.svg)

Nhóm theo số bit 1 → dán → nguyên nhân nguyên tố

---

## Hai pha (tổng quan)

**Phần 1** — Dạng tổng chuẩn tắc **thu gọn** (nguyên nhân nguyên tố)

**Phần 2** — Dạng tổng chuẩn tắc **tối thiểu** (bảng phủ)

---

## Phần 1 — ý tưởng (phép dán)

- Nhóm minterm theo **số bit 1**
- **Dán** cặp khác **đúng 1 bit** → đặt `-`; gắn dấu `*`
- Lặp đến khi không dán thêm
- Mã **không** có `*` = **nguyên nhân nguyên tố**

---

## Phần 2 — ý tưởng (bảng phủ)

- Bảng: nguyên nhân nguyên tố × minterm **bắt buộc**
- Chọn **nguyên tố cốt yếu** trước
- Cover phần còn lại (ít hạng nhất)

---

## Quy tắc phép dán

Hai mã **dán được** khi:

- khác **đúng 1 bit**
- bit khác → thay bằng `-`

**Cơ sở**: $$xy+xy'=x$$

---

## Ví dụ dán một cặp

$$m_{1}=0001$$  
$$m_{5}=0101$$

→ $$0{-}01$$  
(phủ minterm 1 và 5)

---

## Phần 1 — các bước giấy

1. Liệt kê minterm (và $$d$$) dạng bit  
2. Xếp nhóm theo số bit 1  
3. **Dán** cặp nhóm kề; gắn `*`  
4. Lặp trên mã có `-`  
5. Biểu diễn đã dán → dấu `*`  
6. **Không** `*` = nguyên nhân nguyên tố  

---

## Ví dụ 4 biến — đề

$$F$$ bằng **1** tại các hàng **0, 2, 3, 5, 7, 8, 10, 11, 13, 15**

(Giáo trình 13.5 — luyện quy trình)

---

## Phần 1 — nhóm (phác)

| # bit 1 | Minterm |
|:---:|:---|
| 0 | 0 |
| 1 | 2, 8 |
| 2 | 3, 5, 10, … |
| 3 | 7, 11, 13, … |
| 4 | 15 |

*(Trên lớp: viết đủ nhị phân)*

---

## Phần 1 — kết quả điển hình

Nguyên nhân nguyên tố thường gặp:

- $$b'd'$$ (cụm $$0,2,8,10$$)
- $$cd$$, $$bd$$, …

**Đừng học thuộc số**  
→ tập **đánh dấu `*` sau phép dán**

---

## Phần 2 — cấu trúc bảng phủ

|  | Ý nghĩa |
|:---|:---|
| **Hàng** | mỗi nguyên nhân nguyên tố |
| **Cột** | mỗi minterm bắt buộc |
| **Dấu `+`** | hàng phủ cột |

**Không** mở cột cho don't-care

---

## Nguyên tố cốt yếu

Cột chỉ có **đúng một** dấu  
→ nguyên nhân đó **buộc** chọn

= tế bào **cốt yếu** trên K-map

---

## Quy trình phủ (phần 2)

1. Chọn mọi **nguyên tố cốt yếu**
2. Xóa cột đã phủ
3. Xóa hàng trống
4. Cover phần còn lại (thử tay / nhánh)

---

## Kết quả ví dụ 4 biến

Một cover tối tiểu:

$$
F=cd+b'd'
$$

$$b'd'$$ thường cốt yếu  
→ thêm $$cd$$ (hoặc tương đương) phủ nốt

---

## Kiểm kết quả

- So K-map cùng hàm
- Hoặc thử vài vector $$F=1$$ / $$F=0$$

Cùng bảng chân trị → đúng

---

## Don't-care trong QM

**Phần 1**: đưa $$d$$ **như** minterm  
→ nguyên nhân nguyên tố lớn hơn

**Phần 2**: **không** bắt buộc phủ $$d$$

$$X$$ = chất xúc tác, không phải nghĩa vụ

---

## Ví dụ don't-care

$$F$$ bằng **1** tại các hàng **1, 2, 5**, don't-care tại **0, 7**

Phần 1: dán cả 0, 7  
Phần 2: chỉ cột 1, 2, 5  

---

## Cover don't-care

Một kết quả thường gặp:

$$
F=a'c'+b'c
$$

Đối chiếu bảng 8 dòng

---

## So sánh K-map vs QM

| | K-map | QM |
|:---|:---|:---|
| Ưu | Nhanh, trực quan | Hệ thống |
| Nhược | $$n$$ lớn chật | Bảng dài tay |
| Máy | Khó | Dễ lập trình |

---

## Thông điệp chính

Máy cũng chỉ:

1. **Dán** minterm kề  
2. **Chọn** phủ  

= việc mắt làm trên K-map, khác quy mô

---

## Thực hành 1

$$F$$ bằng **1** tại các hàng **0, 1, 2, 6** (3 biến)

QM tay → so K-map

---

## Thực hành 2

$$F$$ bằng **1** tại các hàng **1, 2, 5**, don't-care tại **0, 7**

Phần 1–2 đầy đủ

---

## Tóm tắt Tiết 34

- Phần 1: dán → nguyên nhân nguyên tố
- Phần 2: bảng phủ → cốt yếu → cover
- Cơ sở: $$xy+xy'=x$$
- Don't-care: pha 1 có, pha 2 không buộc
- QM = K-map dạng bảng

---

## Liên hệ lộ trình

13.1 đại số → 13.2 SOP/POS  
→ 13.3 cổng → 13.4 K-map  
→ **13.5 QM** → 13.6–13.7 ứng dụng

---

## Bài tập ôn (1)

1. Nêu hai pha QM  
2. Dán $$000$$ và $$010$$  
3. Nguyên tố cốt yếu là gì?  

---

## Bài tập ôn (2)

4. QM ví dụ 4 biến giáo trình  
5. Hàng **0, 1, 4, 5, 6**: K-map **và** QM  
6. Khi nào ưu tiên K-map / QM / máy?  
