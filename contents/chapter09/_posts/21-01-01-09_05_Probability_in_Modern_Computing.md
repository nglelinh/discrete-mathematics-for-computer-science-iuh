---
layout: post
title: "Xác suất trong Khoa học Máy tính Hiện đại"
categories: chapter09
date: 2021-01-01
order: 5
required: false
lang: en
---

# Xác suất trong Khoa học Máy tính Hiện đại

Máy tính thường được xem như cỗ máy của sự chính xác tuyệt đối.
Một lệnh đúng là đúng,
một bit là 0 hoặc 1,
một chương trình chạy theo quy tắc rõ ràng.

Nhưng thế giới mà máy tính phục vụ lại đầy bất định:
người dùng hành xử khó đoán,
mạng có thể lỗi,
dữ liệu có thể nhiễu,
và nhiều thuật toán tốt nhất lại chủ động dùng ngẫu nhiên.

Vì vậy,
xác suất không phải phần bên lề của computing.
Nó là công cụ để xử lý thế giới thật.

---

## Phần 1: Từ cờ bạc đến lý thuyết xác suất hiện đại

### 1.1. Khởi đầu từ trò chơi may rủi

Giống như chương về phép đếm,
lịch sử xác suất mở đầu từ cờ bạc.
Con người cần hiểu cơ hội thắng,
chia tiền cược,
và đánh giá rủi ro.

Pascal,
Fermat,
Bernoulli,
Laplace
đều góp phần biến câu hỏi giải trí thành lĩnh vực toán học nghiêm túc.

### 1.2. Từ lý thuyết sang hạ tầng của thế giới dữ liệu

Khi khoa học hiện đại phát triển,
xác suất trở thành ngôn ngữ cho:

- thống kê,
- vật lý,
- tài chính,
- truyền thông,
- machine learning,
- reliability engineering.

Khoa học máy tính thừa hưởng toàn bộ kho công cụ này,
và biến nó thành sức mạnh thực dụng ở quy mô số.

![Lịch sử xác suất từ cờ bạc đến dữ liệu]
*Hình 1: Xác suất đi từ câu hỏi về may rủi sang ngôn ngữ nền của AI, networks, và experimentation.*

---

## Phần 2: Machine learning và mô hình xác suất

### 2.1. Nhiều bài toán AI vốn dĩ không chắc chắn

Khi mô hình phân loại email spam,
nó không thật sự “biết chắc” theo nghĩa logic tuyệt đối.
Nó ước lượng xác suất email thuộc lớp spam.

Đó là lý do tư duy xác suất đặc biệt hợp với ML.

### 2.2. Naive Bayes — mô hình đơn giản nhưng đẹp

Naive Bayes dùng Bayes’ theorem và giả định độc lập có điều kiện để phân loại.

Ví dụ,
trong spam detection,
ta ước lượng:

$$
P(Spam \mid words)
$$

Mô hình đơn giản,
nhưng lịch sử của nó rất quan trọng vì nó cho thấy:
không phải AI nào cũng bắt đầu bằng neural nets.

### 2.3. Hidden Markov Models và chuỗi ẩn

HMM từng là công cụ mạnh trong:

- speech recognition,
- NLP cổ điển,
- bioinformatics,
- temporal pattern modeling.

Ý tưởng:
có trạng thái ẩn sinh ra quan sát bề mặt,
và ta suy luận xác suất về trạng thái đó.

Đây là ví dụ đẹp cho sức mạnh của xác suất khi thế giới có phần không quan sát trực tiếp được.

---

## Phần 3: Randomized algorithms và cấu trúc dữ liệu xác suất

### 3.1. Ngẫu nhiên không phải thiếu kỷ luật

Nhiều sinh viên ban đầu thấy lạ:
tại sao lại cố tình đưa randomness vào thuật toán?

Câu trả lời là:
trong nhiều trường hợp,
ngẫu nhiên giúp thuật toán đơn giản hơn,
nhanh hơn,
hoặc chống worst-case do đối thủ dàn dựng.

### 3.2. Quick sort randomized pivot

Nếu luôn chọn pivot tệ,
quick sort có thể rơi vào trường hợp xấu.
Chọn pivot ngẫu nhiên giúp kỳ vọng hiệu năng tốt hơn trên nhiều dạng input.

### 3.3. Bloom filters và xác suất sai có kiểm soát

Bloom filter chấp nhận false positives để đổi lấy tiết kiệm bộ nhớ.

Đây là ví dụ kinh điển của engineering xác suất:
không cần trả lời hoàn hảo mọi lúc,
miễn là xác suất sai được định lượng,
kiểm soát,
và chấp nhận được với ứng dụng.

![Randomized algorithms và Bloom filters]
*Hình 2: Xác suất trong computing không chỉ để phân tích dữ liệu; nó còn là công cụ thiết kế thuật toán và cấu trúc dữ liệu.*

---

## Phần 4: Network reliability và tính toán uptime

### 4.1. Hệ thống lớn hiếm khi hoàn hảo tuyệt đối

Server hỏng,
router lỗi,
đường truyền gián đoạn,
ổ cứng chết,
nguồn điện mất.

Reliability engineering phải hỏi:
với các xác suất hỏng hóc thành phần,
hệ thống tổng thể ổn định tới đâu?

### 4.2. Redundancy là bài toán xác suất có chi phí

Thêm máy chủ dự phòng,
replication,
multi-region deployment
thường làm tăng độ tin cậy,
nhưng cũng tăng chi phí.

Kỹ sư cần dùng xác suất để cân đối:

- mức SLA mong muốn,
- ngân sách,
- expected downtime,
- rủi ro hệ thống liên đới.

### 4.3. 99.9%, 99.99%, 99.999% khác nhau rất nhiều

Chỉ nhìn số phần trăm dễ đánh giá sai.
Xác suất và kỳ vọng downtime giúp biến các con số này thành ngôn ngữ kỹ thuật rõ ràng hơn.

---

## Phần 5: A/B testing và statistical significance

### 5.1. Product decisions không nên dựa vào cảm giác

Giả sử bạn đổi màu nút đăng ký,
thay headline,
hoặc tối ưu luồng thanh toán.
Số click tăng một chút.

Liệu thay đổi đó thật sự hiệu quả,
hay chỉ là nhiễu ngẫu nhiên?

Đó là lý do A/B testing cần xác suất và thống kê.

### 5.2. Significance và hiệu ứng thực tế

Một kết quả có thể statistically significant
nhưng business impact rất nhỏ.
Ngược lại,
hiệu ứng lớn nhưng sample quá ít
có thể chưa đủ tin cậy.

Đây là nơi xác suất buộc product teams phải khiêm tốn hơn trước dữ liệu.

### 5.3. Từ startup đến big tech

A/B testing là vũ khí quen thuộc trong:

- e-commerce,
- search,
- recommendation,
- ads,
- SaaS onboarding,
- mobile apps.

Quyết định sản phẩm ở quy mô lớn
ngày càng cần suy nghĩ xác suất tốt hơn,
không phải ít hơn.

---

## Phần 6: Tương lai — xác suất trong AI và systems ngày càng sâu

Ta đang đi vào thế giới mà uncertainty có mặt ở mọi tầng:

- probabilistic AI,
- approximate query processing,
- anomaly detection,
- stochastic optimization,
- simulation-based planning,
- online experimentation.

Ai hiểu xác suất tốt
sẽ hiểu tốt hơn cách hệ thống thật vận hành dưới bất định.

---

## Kết luận

Xác suất là ngôn ngữ của sự không chắc chắn có kỷ luật.

Từ cờ bạc,
đến Naive Bayes,
randomized algorithms,
network reliability,
và A/B testing,
nó xuất hiện ở mọi nơi mà quyết định cần dựa trên hơn cả trực giác.

Trong khoa học máy tính hiện đại,
điều đó gần như là mọi nơi.

---

## Bài tập thực hành

### Bài tập 1: Xác suất có điều kiện

Một hệ thống phát hiện spam có:
- 95% email spam được phát hiện đúng
- 2% email thường bị đánh dấu nhầm là spam  
Hỏi nếu email bị đánh dấu spam thì xác suất nó thực sự là spam là bao nhiêu? (giả sử 20% email là spam)

<details>
<summary>Đáp án</summary>

Dùng Bayes: $$P(Spam|Detected) \approx 0.91$$ (91%).

</details>

### Bài tập 2: Bloom filter

Giải thích tại sao Bloom filter có thể báo false positive nhưng không bao giờ báo false negative.

<details>
<summary>Đáp án</summary>

Nếu phần tử có mặt thì mọi bit đều được set → không bao giờ miss. Nếu không có mặt thì có thể một số bit tình cờ được set bởi phần tử khác → false positive.

</details>

### Bài tập 3: A/B testing

Hai phiên bản A và B có click rate 12% và 15%. Với 1000 người dùng mỗi nhóm, kiểm tra xem sự khác biệt có ý nghĩa thống kê không (dùng z-test đơn giản).

<details>
<summary>Đáp án</summary>

Tính z-score và p-value. Nếu p < 0.05 thì kết luận khác biệt có ý nghĩa.

</details>

## Tóm tắt

Xác suất là công cụ đo lường sự không chắc chắn trong hệ thống thực tế. Từ Naive Bayes, Bloom filter, mạng tin cậy, đến A/B testing — xác suất giúp chúng ta đưa ra quyết định có cơ sở khi dữ liệu không hoàn hảo. Hiểu rõ xác suất có điều kiện và các mô hình xác suất cơ bản là chìa khóa để xây dựng hệ thống thông minh và đáng tin cậy.
