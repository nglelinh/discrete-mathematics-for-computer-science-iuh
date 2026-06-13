---
layout: post
title: "Định lý Bayes và Ứng dụng"
categories: chapter09
date: 2021-01-01
order: 3
required: true
lang: en
---

Một email bị bộ lọc đánh dấu spam không có nghĩa nó chắc chắn là spam. Một kết quả xét nghiệm dương tính không có nghĩa bệnh chắc chắn hiện diện. Trong rất nhiều hệ thống, ta phải cập nhật niềm tin của mình sau khi quan sát thêm dữ liệu mới.


Xác suất giúp ta chuyển từ trực giác mơ hồ sang đánh giá định lượng, điều rất quan trọng khi phân tích thuật toán ngẫu nhiên, dữ liệu nhiễu và rủi ro hệ thống.
**Định lý Bayes** là công cụ làm đúng việc đó. Nó cho phép đảo chiều điều kiện, từ xác suất quan sát khi giả thuyết đúng sang xác suất giả thuyết đúng khi đã có quan sát. Đây là nền tảng của chẩn đoán, phân loại, học máy và nhiều hệ thống ra quyết định dưới bất định.

Điều khiến Bayes vừa mạnh vừa dễ bị hiểu sai là con người thường bỏ qua xác suất nền. Một tín hiệu có vẻ rất mạnh vẫn có thể dẫn đến kết luận yếu nếu trường hợp gốc vốn rất hiếm.

Trong bài này, chúng ta sẽ học phát biểu của định lý Bayes, cách tính từng thành phần, và cách dùng nó để đọc đúng những tình huống mà trực giác thường đánh lừa.

## 1. Phát biểu định lý Bayes

Với hai biến cố $A,B$ và $P(B)>0$,

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
$$

**Chứng minh**: Từ định nghĩa xác suất có điều kiện,

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},
$$

và

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}.
$$

Suy ra $P(A\cap B)=P(B\mid A)P(A)$, thay vào công thức đầu được định lý Bayes.

## 2. Ngôn ngữ Bayes

Trong công thức

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)},
$$

- $P(A)$ là **xác suất tiên nghiệm** (prior): niềm tin trước khi quan sát bằng chứng.
- $P(B\mid A)$ là **likelihood**: xác suất thấy bằng chứng nếu giả thuyết đúng.
- $P(B)$ là **evidence**: xác suất tổng thể của bằng chứng.
- $P(A\mid B)$ là **xác suất hậu nghiệm** (posterior): niềm tin sau khi cập nhật.

Có thể nhớ ngắn gọn:

$$
\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.
$$


## 3. Dạng phân hoạch

Nếu $A_1,A_2,\ldots,A_n$ là một phân hoạch của không gian mẫu và $P(B)>0$, thì

$$
P(A_k\mid B)=\frac{P(B\mid A_k)P(A_k)}{\sum_{i=1}^{n}P(B\mid A_i)P(A_i)}.
$$

Mẫu số là công thức xác suất toàn phần:

$$
P(B)=\sum_{i=1}^{n}P(B\mid A_i)P(A_i).
$$

## 4. Ví dụ chẩn đoán y khoa

Đây là chỗ nên đi chậm và kiểm tra từng bước. Nếu hiểu vì sao ví dụ hoạt động, bạn sẽ dễ chuyển sang bài tập mới hơn nhiều.

Một bệnh có tỉ lệ trong dân số là $0.1\%$. Xét nghiệm có độ nhạy $99\%$ và tỉ lệ dương tính giả $1\%$. Nếu một người xét nghiệm dương tính, xác suất người đó thật sự có bệnh là bao nhiêu?

Gọi $D$ là biến cố có bệnh, $+$ là xét nghiệm dương tính.

$$
P(D)=0.001,\quad P(+\mid D)=0.99,\quad P(+\mid \overline D)=0.01.
$$

Theo Bayes,

$$
P(D\mid +)=\frac{0.99\cdot0.001}{0.99\cdot0.001+0.01\cdot0.999}
\approx 0.0902.
$$

Nghĩa là chỉ khoảng $9.02\%$, dù xét nghiệm có vẻ “chính xác 99%”. Lý do là bệnh rất hiếm nên số dương tính giả trong nhóm khỏe mạnh có thể lớn.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Thanh kéo điều chỉnh tỉ lệ bệnh, độ nhạy và tỉ lệ dương tính giả. Công cụ hiển thị cây xác suất trên 10.000 người và tính posterior.

<div data-demo="bayes-calculator"></div>
</div>
<script src="{{ '/public/js/bayes-calculator.js' | relative_url }}"></script>

## 5. Naive Bayes trong phân loại văn bản

Trong phân loại thư rác, ta muốn tính

$$
P(\text{Spam}\mid w_1,w_2,\ldots,w_m).
$$

Theo Bayes,

$$
P(\text{Spam}\mid \text{words})\propto P(\text{Spam})P(\text{words}\mid \text{Spam}).
$$

Giả định “naive” cho rằng các từ độc lập có điều kiện theo lớp:

$$
P(\text{words}\mid \text{Spam})\approx \prod_{i=1}^{m}P(w_i\mid \text{Spam}).
$$

Giả định này không hoàn toàn đúng trong ngôn ngữ tự nhiên, nhưng thường đủ tốt để tạo bộ phân loại nhanh, dễ cài đặt và hiệu quả.



## 7. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Bayes là nền tảng của nhiều hệ thống suy luận trong AI: lọc spam, phân loại văn bản, nhận dạng bệnh từ triệu chứng, cập nhật niềm tin trong robot, và mô hình chủ đề. Trong an ninh mạng, Bayes giúp đánh giá khả năng một cảnh báo thật sự là tấn công khi biết tỉ lệ cảnh báo giả. Trong A/B testing, tư duy Bayes giúp cập nhật niềm tin về hiệu quả của phiên bản mới khi dữ liệu đến liên tục.

```python
def bayes(prior, likelihood, false_positive):
    return likelihood * prior / (likelihood * prior + false_positive * (1 - prior))

print(bayes(0.001, 0.99, 0.01))
```

## Bài tập thực hành

### Bài tập 1

Một bộ lọc spam phát hiện đúng 95% email spam và báo nhầm 2% email thường là spam. Nếu 10% email là spam, xác suất một email thật sự là spam khi bị báo spam là bao nhiêu?

<details>
<summary>Đáp án</summary>

$$
P(S\mid +)=\frac{0.95\cdot0.10}{0.95\cdot0.10+0.02\cdot0.90}=\frac{0.095}{0.113}\approx0.8407.
$$

</details>

### Bài tập 2

Một lỗi phần mềm xuất hiện ở 3% phiên bản build. Công cụ kiểm tra phát hiện lỗi với xác suất 90% nếu lỗi có tồn tại, và báo lỗi giả 5% nếu lỗi không tồn tại. Tính xác suất build thật sự lỗi khi công cụ báo lỗi.

<details>
<summary>Đáp án</summary>

$$
\frac{0.90\cdot0.03}{0.90\cdot0.03+0.05\cdot0.97}
=\frac{0.027}{0.0755}\approx0.3576.
$$

</details>

## Tóm tắt

- Định lý Bayes đảo chiều điều kiện từ $P(B\mid A)$ sang $P(A\mid B)$.
- Posterior tỉ lệ với likelihood nhân prior.
- Mẫu số được tính bằng xác suất toàn phần.
- Prior rất quan trọng khi biến cố hiếm.
- Bayes có ứng dụng sâu rộng trong ML, bảo mật, chẩn đoán và suy luận dưới bất định.
