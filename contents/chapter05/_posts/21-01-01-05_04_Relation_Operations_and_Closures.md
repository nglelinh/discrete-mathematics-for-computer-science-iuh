---
layout: post
title: "Phép toán Quan hệ và Bao đóng"
categories: chapter05
date: 2021-01-01
order: 4
required: true
lang: en
---

# Phép toán Quan hệ và Bao đóng

Trong dữ liệu thực tế, quan hệ ban đầu hiếm khi đủ dùng. Ta có thể biết A liên hệ với B và B liên hệ với C, nhưng hệ thống lại cần suy ra A liên hệ với C; ta có thể có quan hệ “đi được một bước”, nhưng ứng dụng cần biết “đi được bao nhiêu bước cũng được”. Khi đó, ta không chỉ đọc quan hệ — ta phải **xử lý** nó.

Các phép toán trên quan hệ và khái niệm **closure** cho phép mở rộng quan hệ đến mức đáp ứng đúng nhu cầu suy luận. Đây là phần rất gần với database, reachability trong đồ thị, phân tích dependency và thiết kế thuật toán. Nói ngắn gọn: từ dữ liệu liên kết thô, ta xây thành tri thức có thể dùng được.

## 1. Quan hệ ngược

**Định nghĩa**: Với quan hệ $$R\subseteq A\times B$$, quan hệ ngược của $$R$$ là:

$$R^{-1}=\{(b,a)\in B\times A\mid (a,b)\in R\}.$$

**Ví dụ**: Nếu $$R=\{(An,Toan),(Binh,Ly),(Chi,Toan)\}$$ biểu diễn "sinh viên học môn", thì $$R^{-1}$$ biểu diễn "môn có sinh viên":

$$R^{-1}=\{(Toan,An),(Ly,Binh),(Toan,Chi)\}.$$

**Tính chất**:

$$(R^{-1})^{-1}=R.$$

Nếu $$R$$ đối xứng thì $$R^{-1}=R$$.

## 2. Hợp thành quan hệ

**Định nghĩa**: Cho $$R\subseteq A\times B$$ và $$S\subseteq B\times C$$. Hợp thành $$S\circ R$$ là quan hệ từ $$A$$ đến $$C$$:

$$S\circ R=\{(a,c)\mid \exists b\in B,\ (a,b)\in R\land (b,c)\in S\}.$$

**Ký hiệu**: $$S\circ R$$ đọc là "$$S$$ sau $$R$$"; thực hiện $$R$$ trước rồi $$S$$.

**Ví dụ**: $$R=\{(1,2),(2,3)\}$$, $$S=\{(2,1),(3,3)\}$$. Khi đó:

- $$(1,2)\in R$$ và $$(2,1)\in S$$ nên $$(1,1)\in S\circ R$$.
- $$(2,3)\in R$$ và $$(3,3)\in S$$ nên $$(2,3)\in S\circ R$$.

Vậy $$S\circ R=\{(1,1),(2,3)\}$$.

## 3. Ma trận quan hệ và tích Boolean

Nếu $$R$$ và $$S$$ được biểu diễn bằng ma trận 0-1, thì ma trận của $$S\circ R$$ được tính bằng tích Boolean:

$$M_{S\circ R}[i,j]=\bigvee_k(M_R[i,k]\land M_S[k,j]).$$

Ở đây phép nhân thường được thay bằng AND, phép cộng thường được thay bằng OR.

## 4. Lũy thừa quan hệ

**Định nghĩa**: Với quan hệ $$R$$ trên $$A$$:

- $$R^1=R$$.
- $$R^{n+1}=R^n\circ R$$.

**Ý nghĩa**: $$(a,b)\in R^k$$ nếu tồn tại đường đi độ dài $$k$$ từ $$a$$ đến $$b$$ trong đồ thị của $$R$$.

## 5. Bao đóng

**Định nghĩa**: Bao đóng của quan hệ $$R$$ theo một tính chất là quan hệ nhỏ nhất chứa $$R$$ và có tính chất đó.

### Bao đóng phản xạ

Thêm mọi cặp $$(a,a)$$ còn thiếu:

$$R_{ref}=R\cup\{(a,a)\mid a\in A\}.$$

### Bao đóng đối xứng

Thêm chiều ngược cho mọi cặp:

$$R_{sym}=R\cup R^{-1}.$$

### Bao đóng bắc cầu

Thêm các cặp biểu diễn đường đi gián tiếp. Với tập hữu hạn $$A$$ có $$n$$ phần tử:

$$R^+=R\cup R^2\cup\cdots\cup R^n.$$

Bao đóng phản xạ-bắc cầu là:

$$R^*=I_A\cup R^+,$$

trong đó $$I_A=\{(a,a)\mid a\in A\}$$.

## 6. Thuật toán Warshall

**Ý tưởng**: Warshall tính bao đóng bắc cầu từ ma trận kề. Cho phép từng đỉnh $$k$$ làm đỉnh trung gian, cập nhật:

$$M[i,j]=M[i,j]\lor(M[i,k]\land M[k,j]).$$

```python
def warshall(M):
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = M[i][j] or (M[i][k] and M[k][j])
    return M
```

## 7. Công cụ tương tác

<div class="interactive-demo" data-demo="relation-closure-warshall">
  <p><strong>Demo đề xuất:</strong> nhập ma trận quan hệ, công cụ tô sáng từng bước Warshall và hiển thị các cặp được thêm vào bao đóng bắc cầu.</p>
</div>

## 8. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Đảo thứ tự hợp thành. $$S\circ R$$ nghĩa là đi theo $$R$$ trước, không phải $$S$$ trước.

**Nhầm lẫn 2**: Bao đóng không phải thêm tùy ý. Nó là quan hệ nhỏ nhất thỏa tính chất cần có.

**Nhầm lẫn 3**: Bao đóng đối xứng khác quan hệ ngược. Bao đóng đối xứng là $$R\cup R^{-1}$$.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

- **Đồ thị**: bao đóng bắc cầu trả lời truy vấn reachability.
- **Cơ sở dữ liệu**: truy vấn đệ quy như "tất cả cấp dưới của một quản lý" dùng transitive closure.
- **Compiler**: phân tích call graph để biết hàm nào có thể gọi gián tiếp hàm nào.
- **Bảo mật**: quan hệ quyền truy cập kế thừa cần bao đóng theo cây vai trò.

## Tóm tắt

Quan hệ ngược đảo chiều cặp; hợp thành ghép hai bước thành một bước; lũy thừa quan hệ mô tả đường đi nhiều bước. Bao đóng phản xạ, đối xứng và bắc cầu thêm tối thiểu các cặp để quan hệ có tính chất mong muốn. Warshall là thuật toán cổ điển để tính bao đóng bắc cầu trên tập hữu hạn.
