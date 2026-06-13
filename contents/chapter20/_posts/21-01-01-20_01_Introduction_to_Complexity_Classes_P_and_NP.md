---
layout: post
title: "Giới thiệu Lớp Phức tạp P và NP"
categories: chapter20
date: 2021-01-01
order: 1
required: true
lang: en
---

Sắp xếp một danh sách một triệu số là chuyện vài giây trên một laptop hiện đại. Nhưng tìm **đường đi ngắn nhất** đi qua 50 thành phố và quay về điểm xuất phát - bài toán **người du lịch** (Traveling Salesman Problem, TSP) - thì có thể khiến cả một trung tâm dữ liệu chạy hàng giờ vẫn chưa cho ra lời giải tối ưu. Sự khác biệt này không phải do lập trình viên chưa đủ giỏi; nó là một sự thật **toán học** sâu sắc về bản chất của hai loại bài toán.

Khoa học máy tính lý thuyết phân loại các bài toán quyết định theo lượng tài nguyên (thời gian, bộ nhớ) cần để giải chúng. Hai lớp quan trọng nhất là **P** - các bài toán có thể **giải** trong thời gian đa thức - và **NP** - các bài toán mà một lời giải đề xuất có thể được **kiểm tra** trong thời gian đa thức. Câu hỏi $$P \stackrel{?}{=} NP$$ - liệu mọi bài toán có lời giải dễ kiểm tra có lời giải dễ tìm hay không - là **bài toán mở nổi tiếng nhất** của khoa học máy tính, với giải thưởng một triệu USD từ Viện Clay dành cho ai chứng minh được đáp án.

<div class="content-box info-box" markdown="1">
**Trạng thái:** [Nội dung đang được biên soạn]

Đây là bài mở đầu chương 20. Nội dung chi tiết sẽ được bổ sung trong các phiên bản tiếp theo.
</div>

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên sẽ:

- Phân biệt **độ phức tạp thời gian** (time complexity) đa thức và mũ, và hiểu vì sao ranh giới này có ý nghĩa thực tế.
- Định nghĩa hình thức lớp **P** và lớp **NP** dưới dạng bài toán quyết định (decision problem).
- Hiểu **đặc trưng theo bộ kiểm tra** (verifier characterization) của NP: $$L \in NP$$ khi và chỉ khi tồn tại bộ kiểm tra đa thức.
- Nắm khái niệm **rút gọn đa thức** (polynomial-time reduction) và **NP-đầy đủ** (NP-complete).
- Phát biểu rõ câu hỏi $$P \stackrel{?}{=} NP$$ và ý nghĩa của nó đối với mật mã học, tối ưu hóa và trí tuệ nhân tạo.

## Nội dung sẽ bao gồm

1. Ôn tập ký hiệu **Big-O**, $$\Theta$$, $$\Omega$$ và các hàm tăng trưởng thường gặp.
2. Bài toán quyết định, mã hóa đầu vào và máy Turing như mô hình đo độ phức tạp.
3. Định nghĩa lớp **P** (deterministic polynomial time) với ví dụ: PATH, MATCHING, PRIMES.
4. Định nghĩa lớp **NP** (nondeterministic polynomial time) và đặc trưng theo bộ kiểm tra.
5. Bài toán **SAT** và **định lý Cook-Levin** (1971): SAT là NP-đầy đủ.
6. **Rút gọn đa thức** và cách chứng minh tính NP-đầy đủ của các bài toán cổ điển: 3-SAT, CLIQUE, VERTEX-COVER, SUBSET-SUM, HAMILTON-PATH, TSP.
7. Câu hỏi $$P \stackrel{?}{=} NP$$, hệ quả thực tế và các hướng nghiên cứu hiện đại.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.), Chương 3.3 và 13.5: Complexity of Algorithms; Turing Machines.
- Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.), Chương 7: Time Complexity.
- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.), Chương 34: NP-Completeness.
</div>
