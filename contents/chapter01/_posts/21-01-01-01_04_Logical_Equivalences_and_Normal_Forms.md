---
layout: post
title: "Tương đương Logic và Các Dạng Chuẩn tắc"
categories: chapter01
date: 2021-01-01
order: 4
required: true
lang: en
---

# Tương đương Logic và Các Dạng Chuẩn tắc

Cùng một ý logic có thể được viết theo rất nhiều cách khác nhau. Một lập trình viên thích điều kiện ngắn gọn, một database engine lại muốn biểu thức dễ tối ưu, còn SAT solver hay công cụ kiểm chứng hình thức lại cần công thức ở một dạng chuẩn để xử lý hàng triệu biến. Nhìn bề ngoài, các biểu thức này có thể khác nhau hoàn toàn — nhưng câu hỏi quan trọng là: **chúng có thật sự nói cùng một điều không?**

Đây không chỉ là câu hỏi của toán học thuần túy. Trong khoa học máy tính, khả năng biến đổi biểu thức logic một cách an toàn có ảnh hưởng rất lớn đến thực tế:

- giúp rút gọn điều kiện để code dễ đọc hơn,
- giúp tối ưu truy vấn và luật lọc trong hệ thống,
- giúp chuẩn hóa công thức cho bộ giải SAT,
- giúp thiết kế mạch logic,
- và giúp các công cụ kiểm chứng phần mềm xử lý bài toán hiệu quả hơn.

Một phép biến đổi nhỏ trên biểu thức có thể làm chương trình dễ hiểu hơn, mạch logic gọn hơn, hoặc bộ giải chạy nhanh hơn rất nhiều. Nhưng điều đó chỉ đúng khi ta biến đổi **đúng luật**. Nếu suy luận cảm tính, chỉ cần đổi sai một bước là toàn bộ ý nghĩa logic của biểu thức có thể bị phá vỡ.

Chính vì vậy, bài học này giới thiệu hai ý tưởng cực kỳ quan trọng:

- **Tương đương logic**: hai biểu thức khác hình thức nhưng giống nhau về ý nghĩa trong mọi trường hợp.
- **Dạng chuẩn tắc**: những cách viết chuẩn hóa giúp biểu thức trở nên dễ xử lý hơn đối với con người lẫn máy tính.

Trong bài này, chúng ta sẽ học cách nhận ra khi nào hai công thức thực sự tương đương, cách áp dụng các luật biến đổi cơ bản, và cách đưa biểu thức về các dạng chuẩn quen thuộc như DNF và CNF — những dạng xuất hiện rất nhiều trong logic toán, trí tuệ nhân tạo và kiểm chứng hệ thống.

## Mục tiêu học tập

Sau bài này, sinh viên có thể:

- Phát biểu chính xác khái niệm tương đương logic.
- Sử dụng các luật tương đương để rút gọn biểu thức mệnh đề.
- Chuyển đổi giữa biểu thức logic, bảng chân trị, DNF và CNF.
- Nhận ra lỗi thường gặp khi áp dụng De Morgan, kéo theo và phân phối.
- Giải thích vai trò của CNF trong SAT solver và kiểm chứng phần mềm.

## 1. Tương đương logic

**Định nghĩa**: Hai mệnh đề phức hợp $$P$$ và $$Q$$ được gọi là **tương đương logic** nếu chúng có cùng giá trị chân trị trong mọi phép gán giá trị cho các biến mệnh đề. Khi đó ta viết:

$$P \equiv Q$$

Tương đương với việc $$P \leftrightarrow Q$$ là một hằng đúng.

**Ký hiệu**:

- $$\equiv$$: tương đương logic, dùng cho quan hệ giữa hai công thức.
- $$\leftrightarrow$$: phép nối hai chiều, là một toán tử nằm trong công thức.
- $$T$$ và $$F$$: hằng đúng và hằng sai.

**Ví dụ**: Chứng minh $$p \to q \equiv \neg p \lor q$$.

| $$p$$ | $$q$$ | $$p \to q$$ | $$\neg p \lor q$$ |
|:---:|:---:|:---:|:---:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

Hai cột cuối giống nhau ở mọi hàng, do đó $$p \to q \equiv \neg p \lor q$$.

<div class="content-box insight-box" markdown="1">
**Ghi nhớ**: Tương đương logic là quan hệ "thay thế an toàn". Nếu $$P \equiv Q$$, ta có thể thay $$P$$ bằng $$Q$$ trong bất kỳ biểu thức lớn hơn nào mà không đổi bảng chân trị của toàn bộ biểu thức.
</div>

## 2. Các luật tương đương cơ bản

| Tên luật | Công thức tiêu biểu |
|---|---|
| Đồng nhất | $$p \land T \equiv p$$, $$p \lor F \equiv p$$ |
| Nuốt | $$p \lor T \equiv T$$, $$p \land F \equiv F$$ |
| Lũy đẳng | $$p \lor p \equiv p$$, $$p \land p \equiv p$$ |
| Phủ định kép | $$\neg\neg p \equiv p$$ |
| Giao hoán | $$p \lor q \equiv q \lor p$$, $$p \land q \equiv q \land p$$ |
| Kết hợp | $$(p \lor q) \lor r \equiv p \lor (q \lor r)$$ |
| Phân phối | $$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$ |
| De Morgan | $$\neg(p \land q) \equiv \neg p \lor \neg q$$ |
| Hấp thụ | $$p \lor (p \land q) \equiv p$$ |
| Bù | $$p \lor \neg p \equiv T$$, $$p \land \neg p \equiv F$$ |

### Khối chứng minh: Luật De Morgan

Ta chứng minh $$\neg(p \land q) \equiv \neg p \lor \neg q$$ bằng bảng chân trị.

| $$p$$ | $$q$$ | $$p \land q$$ | $$\neg(p \land q)$$ | $$\neg p$$ | $$\neg q$$ | $$\neg p \lor \neg q$$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

Hai cột $$\neg(p \land q)$$ và $$\neg p \lor \neg q$$ giống nhau. Vậy luật đúng.

## 3. Biến đổi biểu thức logic

**Ví dụ**: Rút gọn biểu thức $$\neg(p \lor \neg q) \land (r \lor \neg r)$$.

$$\begin{aligned}
\neg(p \lor \neg q) \land (r \lor \neg r)
&\equiv (\neg p \land \neg\neg q) \land T && \text{De Morgan và luật bù}\\
&\equiv (\neg p \land q) \land T && \text{phủ định kép}\\
&\equiv \neg p \land q && \text{đồng nhất.}
\end{aligned}$$

**Nhận xét**: Mỗi dòng biến đổi phải nêu rõ luật được dùng. Trong chứng minh toán học và kiểm chứng chương trình, việc ghi luật giúp phát hiện sai sót sớm.

## 4. Dạng chuẩn tắc tuyển DNF

**Định nghĩa**: **Dạng chuẩn tắc tuyển** (Disjunctive Normal Form, DNF) là biểu thức có dạng tuyển của các hội, trong đó mỗi thành phần nhỏ là một literal hoặc phủ định của literal:

$$(l_{11} \land l_{12} \land \cdots) \lor (l_{21} \land l_{22} \land \cdots) \lor \cdots$$

**Ví dụ**: $$(p \land q) \lor (\neg p \land r)$$ là DNF.

### Tạo DNF từ bảng chân trị

Với mỗi hàng làm công thức đúng, tạo một hội mô tả đúng hàng đó; sau đó lấy tuyển của các hội.

**Ví dụ**: Với $$p \to q$$, các hàng đúng là $$(T,T), (F,T), (F,F)$$. Do đó DNF đầy đủ là:

$$(p \land q) \lor (\neg p \land q) \lor (\neg p \land \neg q).$$

Biểu thức này có thể rút gọn thành $$\neg p \lor q$$.

## 5. Dạng chuẩn tắc hội CNF

**Định nghĩa**: **Dạng chuẩn tắc hội** (Conjunctive Normal Form, CNF) là biểu thức có dạng hội của các tuyển:

$$(l_{11} \lor l_{12} \lor \cdots) \land (l_{21} \lor l_{22} \lor \cdots) \land \cdots$$

**Ví dụ**: $$(p \lor q) \land (\neg p \lor r) \land (q \lor \neg r)$$ là CNF.

**Ký hiệu**: Mỗi ngoặc trong CNF thường được gọi là một **mệnh đề con** (clause). CNF là dạng chuẩn mà nhiều SAT solver nhận vào.

## 6. Công cụ tương tác

<div class="interactive-tool" data-tool="truth-table-normal-form">
  <p><strong>Demo đề xuất:</strong> nhập một biểu thức như <code>(p -> q) and (q -> r)</code>, công cụ sinh bảng chân trị, DNF và CNF tương ứng.</p>
</div>

## 7. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Nghĩ rằng $$\neg(p \land q)$$ bằng $$\neg p \land \neg q$$. Thực ra phải đổi phép toán: $$\neg(p \land q) \equiv \neg p \lor \neg q$$.

**Nhầm lẫn 2**: Lẫn lộn $$\equiv$$ và $$\leftrightarrow$$. Ký hiệu $$\leftrightarrow$$ tạo ra một mệnh đề mới; ký hiệu $$\equiv$$ nói rằng hai mệnh đề có cùng bảng chân trị.

**Nhầm lẫn 3**: Cho rằng CNF và DNF là duy nhất. Dạng chuẩn đầy đủ có thể duy nhất theo bảng chân trị, nhưng sau rút gọn có nhiều biểu thức tương đương khác nhau.
</div>

## 8. Ứng dụng trong Khoa học Máy tính

- **Tối ưu điều kiện trong chương trình**: Compiler có thể thay `not (a and b)` bằng `(not a) or (not b)` để đơn giản hóa nhánh.
- **Mạch số**: Cổng AND, OR, NOT tương ứng trực tiếp với hội, tuyển, phủ định.
- **SAT solver**: Nhiều bài toán lập lịch, kiểm chứng phần mềm, giải Sudoku và phân tích phụ thuộc được mã hóa thành CNF.
- **Cơ sở dữ liệu**: Tối ưu truy vấn SQL dùng các luật tương đương để đẩy điều kiện lọc xuống sớm hơn.

```python
# De Morgan trong kiểm tra điều kiện
if not (is_admin and is_active):
    deny_access()

# Tương đương với
if (not is_admin) or (not is_active):
    deny_access()
```

## Tóm tắt

Tương đương logic cho phép ta biến đổi biểu thức mà không đổi ý nghĩa. Các luật như De Morgan, phân phối, hấp thụ và kéo theo là công cụ đại số của logic mệnh đề. DNF mô tả các trường hợp làm công thức đúng, còn CNF mô tả ràng buộc dạng clause, đặc biệt quan trọng trong SAT và kiểm chứng chương trình.
