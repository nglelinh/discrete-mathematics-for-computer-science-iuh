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

Khi làm việc với quan hệ trong hệ thống thực, ta không chỉ quan sát một quan hệ có sẵn. Ta thường phải đảo chiều liên kết, ghép hai quan hệ thành một đường suy diễn mới, hoặc thêm vào những cặp còn thiếu để quan hệ đạt một tính chất mong muốn.


Khi đọc phần này, hãy nghĩ đến các liên kết giữa đối tượng trong cơ sở dữ liệu, đồ thị và hệ thống phân quyền, vì quan hệ chính là cách ta mô tả những liên kết đó.
Đó là lúc các **phép toán trên quan hệ** và khái niệm **bao đóng** trở nên quan trọng. Chúng giúp ta chuyển từ mô tả tĩnh sang thao tác chủ động trên cấu trúc liên hệ, rất giống cách ta biến dữ liệu thô thành dữ liệu có thể dùng được.

Ví dụ, từ quan hệ phụ thuộc trực tiếp giữa các module, ta muốn suy ra phụ thuộc gián tiếp. Từ quan hệ kết nối trong mạng, ta muốn biết cặp node nào cuối cùng vẫn liên thông với nhau. Những câu hỏi như vậy dẫn thẳng đến bao đóng bắc cầu.

Trong bài học này, chúng ta sẽ học cách đảo, hợp thành và mở rộng quan hệ để khai thác được nhiều thông tin hơn từ cùng một mô hình ban đầu.

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

Ở phần này, đừng chỉ nhớ các bước. Hãy chú ý điều kiện áp dụng, thông tin được duy trì sau mỗi bước và lý do thuật toán cho kết quả đúng.

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

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div class="interactive-demo" data-demo="relation-closure-warshall">
  <p><strong>Demo đề xuất:</strong> nhập ma trận quan hệ, công cụ tô sáng từng bước Warshall và hiển thị các cặp được thêm vào bao đóng bắc cầu.</p>
</div>

<script src="{{ '/public/js/warshall-visualizer.js' | relative_url }}"></script>


## 9. Ứng dụng trong Khoa học Máy tính

- **Đồ thị**: bao đóng bắc cầu trả lời truy vấn reachability.
- **Cơ sở dữ liệu**: truy vấn đệ quy như "tất cả cấp dưới của một quản lý" dùng transitive closure.
- **Compiler**: phân tích call graph để biết hàm nào có thể gọi gián tiếp hàm nào.
- **Bảo mật**: quan hệ quyền truy cập kế thừa cần bao đóng theo cây vai trò.

## Bài tập thực hành

### Bài tập 1: Tính quan hệ hợp thành

Cho $$R = \{(1,2),(2,3)\}$$ và $$S = \{(2,4),(3,5)\}$$. Tính $$R \circ S$$ và $$S \circ R$$.

<details>
<summary>Đáp án</summary>

- $$R \circ S = \{(2,4),(3,5)\}$$ (không có cặp nào thỏa)
- $$S \circ R = \{(1,4),(2,5)\}$$

</details>

### Bài tập 2: Bao đóng

Tìm bao đóng phản xạ và bắc cầu nhỏ nhất của quan hệ $$R = \{(1,2),(2,3)\}$$ trên $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

Bao đóng phản xạ + bắc cầu: $$\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}$$

</details>

### Bài tập 3: Ma trận Warshall

Cho ma trận quan hệ 3×3, áp dụng thuật toán Warshall một bước.

<details>
<summary>Đáp án</summary>

Thực hiện $$W = W \lor (W[:,k] \land W[k,:])$$ với mỗi k.

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Quan hệ ngược đảo chiều cặp; hợp thành ghép hai bước thành một bước; lũy thừa quan hệ mô tả đường đi nhiều bước. Bao đóng phản xạ, đối xứng và bắc cầu thêm tối thiểu các cặp để quan hệ có tính chất mong muốn. Warshall là thuật toán cổ điển để tính bao đóng bắc cầu trên tập hữu hạn.
