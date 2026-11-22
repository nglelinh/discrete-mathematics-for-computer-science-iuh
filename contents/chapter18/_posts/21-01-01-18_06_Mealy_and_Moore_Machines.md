---
layout: post
title: "Máy Mealy và Moore"
categories: chapter18
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Bộ biến đổi hữu hạn trạng thái (transducer), so sánh hàm đầu ra λ(q) và ω(q,a), độ dài chuỗi ra và sự tương đương giữa máy Moore và máy Mealy."
---

<div class="textbook-epigraph" markdown="1">

"Moore outputs on states; Mealy on edges."

<span class="epigraph-attribution">— Sequential machine theory</span>

</div>

![Mealy Moore](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_mealy_moore.svg)

<p class="textbook-figure-caption" data-figure="18.4">Hai kiểu bộ biến đổi (transducer) hữu hạn trạng thái: máy Moore gắn đầu ra ở trạng thái, còn máy Mealy gắn đầu ra ở cạnh chuyển.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** máy Moore và máy Mealy.
- **Tính** chuỗi đầu ra tương ứng với một chuỗi đầu vào cho trước.
- **Phác thảo** cách chuyển đổi qua lại giữa máy Moore và máy Mealy.

</div>

## Máy Moore

Máy Moore được định nghĩa là bộ sáu $$M=(Q,\Sigma,\Delta,\delta,\lambda,q_0)$$, trong đó hàm đầu ra $$\lambda:Q\to\Delta$$ chỉ phụ thuộc vào trạng thái hiện tại. Với chuỗi đầu vào $$a_1\ldots a_n$$, máy sinh ra chuỗi đầu ra $$\lambda(q_0)\lambda(q_1)\ldots\lambda(q_n)$$ có độ dài $$n+1$$.

## Máy Mealy

Trong máy Mealy, hàm đầu ra $$\omega:Q\times\Sigma\to\Delta$$ phụ thuộc vào cả trạng thái hiện tại lẫn ký hiệu đầu vào. Với chuỗi đầu vào $$a_1\ldots a_n$$, máy sinh ra chuỗi đầu ra $$\omega(q_0,a_1)\ldots\omega(q_{n-1},a_n)$$ có độ dài $$n$$.

## Tính tương đương giữa hai mô hình

<div class="textbook-theorem" markdown="1">

**Định lý** (Ý chính). Mọi máy Mealy đều có một máy Moore tương đương (với độ trễ đầu ra bằng 1, xét theo ký tự đầu ra khởi tạo) và ngược lại, bằng cách mở rộng không gian trạng thái để lưu thông tin đầu ra.

</div>

**Ý tưởng chuyển đổi:**  
Từ Mealy sang Moore: tách mỗi trạng thái $$q$$ thành các cặp $$(q,\mathrm{last\_out})$$ sao cho mọi cạnh đi vào đều mang cùng một giá trị đầu ra, rồi gán $$\lambda$$ theo giá trị đó.  
Từ Moore sang Mealy: định nghĩa trực tiếp $$\omega(q,a)=\lambda(\delta(q,a))$$ (bỏ qua giá trị khởi tạo $$\lambda(q_0)$$ nếu chuẩn hóa cùng độ dài $$n$$).

### Thử nghiệm: máy Mealy và Moore

Chạy máy có đầu ra theo từng ký tự để quan sát dãy đầu ra được sinh ra:

<div class="interactive-demo" markdown="1">
<div data-demo="mealy-explainer" data-preset="m11"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Xây dựng máy Mealy đảo bit và chứng minh chuỗi đầu ra là phần bù từng bit của chuỗi đầu vào.
2. So sánh độ trễ (*latency*) giữa máy Moore và máy Mealy khi triển khai trên mạch số phần cứng.
3. Thiết kế máy Mealy hoặc máy Moore phát hiện chuỗi con `aab`.

## Tài liệu đọc thêm

Kohavi, *Switching and Finite Automata Theory*; Hopcroft–Ullman (phần ứng dụng).

## Tóm tắt

Máy Moore và máy Mealy là hai dạng bộ biến đổi hữu hạn trạng thái khác nhau ở cách gắn đầu ra và độ dài chuỗi ra, nhưng có thể mô phỏng lẫn nhau.

**Bài tiếp theo:** Biểu thức chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0_OZKWdCixw">Mealy and Moore State Machines (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu máy Mealy và Moore với đầu ra gắn theo bước chuyển hoặc trạng thái.
- <a href="https://www.youtube.com/watch?v=LioitkXDfmA">Construction of Mealy Machine</a> — Neso Academy, tiếng Anh. Cách dựng máy Mealy từ đặc tả đầu ra.
- <a href="https://www.youtube.com/watch?v=MFnRF07SoFo">Construction of Moore Machine</a> — Neso Academy, tiếng Anh. Cách dựng máy Moore để đối chiếu cùng một hành vi đầu vào–đầu ra.
