---
layout: post
title: "Từ Königsberg đến Mạng xã hội: Lịch sử và Ứng dụng"
categories: chapter17
date: 2021-01-01
order: 5
required: true
lang: en
---

# Từ Königsberg đến Mạng xã hội: Lịch sử và Ứng dụng

Lý thuyết đồ thị bắt đầu từ một câu đố ở thành phố Königsberg vào thế kỷ 18 - một bài toán nhỏ về việc đi qua bảy cây cầu - và đã trở thành nền tảng toán học của Internet, mạng xã hội, sinh học, kinh tế và trí tuệ nhân tạo hiện đại. Hành trình $$300$$ năm này là minh chứng đẹp cho việc một câu hỏi tưởng chừng "vô dụng" cuối cùng có thể định hình toàn bộ một nền văn minh số.

Bài này không giới thiệu khái niệm mới - thay vào đó, ta kể lại câu chuyện của những ý tưởng đã học trong chương: bài toán Königsberg, cây và mạng điện, định lý bốn màu, "sáu độ phân tách", mạng nhỏ thế giới (small-world), mạng scale-free, PageRank, và mạng xã hội hiện đại. Mục đích: thấy được **mạch chảy lịch sử** kết nối toán học cổ điển với khoa học mạng đương đại.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Kể** câu chuyện bài toán Königsberg và đóng góp của Euler năm 1736.
- **Liên kết** các định lý cổ điển (bốn màu, Hall, Max-Flow Min-Cut) với bối cảnh ra đời.
- **Mô tả** ba mô hình mạng phức tạp: random graph Erdős-Rényi, small-world Watts-Strogatz, scale-free Barabási-Albert.
- **Nhận diện** ứng dụng đồ thị trong các sản phẩm số họ đang dùng hằng ngày.
- **Suy nghĩ** về các bài toán mở trong khoa học mạng đương đại.

## 1. 1736 - Königsberg và sự ra đời của Lý thuyết Đồ thị

Thành phố Königsberg (nay là Kaliningrad, Nga) có sông Pregel chảy qua, tạo thành hai đảo nhỏ nối với hai bờ bằng **bảy cây cầu**. Người dân thành phố từng đặt câu hỏi: có thể đi dạo qua **tất cả bảy cầu, mỗi cầu đúng một lần**, rồi quay về điểm xuất phát hay không?

Năm 1736, **Leonhard Euler** ($$1707-1783$$) đưa ra lời giải - và lời giải đó khai sinh lý thuyết đồ thị. Ý tưởng đột phá của Euler:

1. **Trừu tượng hóa**: các đảo và bờ trở thành **đỉnh**, các cầu trở thành **cạnh**. Hình dạng không quan trọng.
2. **Định lý**: để có chu trình đi qua mọi cạnh đúng một lần, mọi đỉnh phải có bậc chẵn.
3. **Áp dụng**: trong Königsberg, mọi đỉnh có bậc lẻ - nên không tồn tại chu trình Euler.

Bài báo của Euler, *Solutio problematis ad geometriam situs pertinentis* ($$1736$$), được coi là bài báo đầu tiên của **topology** và **graph theory**.

## 2. Thế kỷ 19 - Cây, Mạng điện và Bản đồ

**Cây** (tree) như một cấu trúc toán học được Arthur **Cayley** ($$1857$$) định danh khi nghiên cứu **đồng phân hóa học**: mỗi phân tử hidrocacbon ankan có một "cây carbon" duy nhất. Định lý Cayley: số cây có $$n$$ đỉnh đánh số là $$n^{n-2}$$.

**Gustav Kirchhoff** ($$1847$$) phát triển lý thuyết **mạch điện** dựa trên đồ thị - mỗi nút mạch là đỉnh, mỗi đoạn dây là cạnh. Định luật Kirchhoff về dòng và điện áp dẫn đến **Matrix Tree Theorem**: số cây bao trùm có thể tính bằng định thức của ma trận Laplace.

**Định lý bốn màu** được Francis Guthrie đặt ra năm $$1852$$: có thể tô màu mọi bản đồ với chỉ $$4$$ màu sao cho hai vùng kề nhau khác màu. Bài toán này mở suốt $$124$$ năm cho đến khi **Kenneth Appel** và **Wolfgang Haken** chứng minh năm $$1976$$ - **chứng minh đầu tiên trong lịch sử toán học cần sự hỗ trợ của máy tính**, kiểm tra $$1936$$ cấu hình bằng $$1200$$ giờ máy.

## 3. 1930s-1950s - Các Định lý Cấu trúc

**Định lý König** ($$1931$$): trong đồ thị hai phần, kích thước matching cực đại bằng kích thước vertex cover cực tiểu. Đây là một trong những **định lý đối ngẫu** đầu tiên trong tối ưu tổ hợp.

**Định lý Hall** ($$1935$$): điều kiện cần và đủ cho marriage problem - $$|N(S)| \geq |S|$$ cho mọi $$S \subseteq X$$.

**Định lý Max-Flow Min-Cut** (**Ford** & **Fulkerson**, $$1956$$): bắt nguồn từ một bài toán quân sự thời Chiến tranh Lạnh - lập kế hoạch vận chuyển hàng qua mạng đường sắt Liên Xô. Bài toán này khởi đầu cho cả **lý thuyết tối ưu tổ hợp** và **lập trình tuyến tính ứng dụng**.

## 4. 1959-1960 - Mô hình Đồ thị Ngẫu nhiên

**Paul Erdős** và **Alfréd Rényi** giới thiệu mô hình **đồ thị ngẫu nhiên** $$G(n, p)$$: có $$n$$ đỉnh, mỗi cặp đỉnh có cạnh với xác suất $$p$$ độc lập.

Định lý nổi tiếng: tồn tại **ngưỡng** $$p^* \approx \ln n / n$$ sao cho:

- Nếu $$p < p^*$$: hầu như chắc chắn đồ thị **không** liên thông.
- Nếu $$p > p^*$$: hầu như chắc chắn đồ thị **liên thông**.

Hiện tượng **chuyển pha** này (như nước hóa hơi ở $$100^\circ$$C) trở thành chủ đề nghiên cứu sâu trong **xác suất tổ hợp**.

## 5. 1967 - Sáu Độ Phân tách

**Stanley Milgram** ($$1933-1984$$), nhà tâm lý xã hội tại Harvard, thực hiện thí nghiệm: gửi $$296$$ lá thư cho người ở Nebraska, yêu cầu chuyển đến một nhà môi giới chứng khoán ở Boston, chỉ qua các quen biết cá nhân (mỗi lần một bước). Kết quả trung bình: thư đến đích sau khoảng **$$5.5$$ bước**.

Phát hiện này - "sáu độ phân tách" (six degrees of separation) - cho thấy mạng quen biết người với người có **đường kính rất nhỏ** dù có hàng tỷ nút. Sau này, Facebook đo được khoảng cách trung bình giữa hai người dùng bất kỳ chỉ $$3.57$$ bước ($$2016$$).

## 6. 1998 - Small-World Networks

**Duncan Watts** và **Steven Strogatz** đăng bài *Collective dynamics of small-world networks* trên *Nature* ($$1998$$). Họ chỉ ra rằng nhiều mạng thực (neural network của *C. elegans*, lưới điện Tây Mỹ, mạng diễn viên Hollywood) có hai tính chất đồng thời:

1. **Đường kính nhỏ**: khoảng cách trung bình giữa hai nút ngắn (vài bước).
2. **Hệ số clustering cao**: bạn của bạn cũng là bạn (cụm dày đặc).

Mô hình Watts-Strogatz: bắt đầu từ lưới đều (clustering cao, đường kính lớn), với xác suất $$p$$ ngẫu nhiên hóa từng cạnh (rewire). Chỉ cần $$p$$ nhỏ ($$\sim 0.01$$) là đường kính giảm mạnh trong khi clustering vẫn cao - **small world**.

## 7. 1999 - Scale-Free Networks

**Albert-László Barabási** và **Réka Albert** ($$1999$$) phát hiện rằng phân phối bậc của World Wide Web và nhiều mạng thực **không phải Gaussian** (như Erdős-Rényi) mà là **luật lũy thừa**:

$$P(\deg = k) \sim k^{-\gamma}, \quad \gamma \in [2, 3].$$

Một số ít "**hub**" có bậc cực kỳ lớn (Google, Facebook), trong khi đa số trang có rất ít liên kết. Đây gọi là **scale-free network**.

Mô hình Barabási-Albert giải thích: mạng phát triển bằng cách **gắn ưu tiên** (preferential attachment) - "người giàu càng giàu thêm" - nút mới ưu tiên kết nối với nút có nhiều cạnh sẵn có.

## 8. 1998-2000 - PageRank và sự ra đời của Google

**Larry Page** và **Sergey Brin** ($$1998$$, tại Stanford) áp dụng random walk trên đồ thị web với damping factor - thuật toán PageRank. Google ra đời năm $$1998$$, IPO năm $$2004$$ với giá trị thị trường ban đầu $$\$23$$ tỷ USD, hiện vượt $$\$2$$ nghìn tỷ.

Câu chuyện PageRank minh họa một bài học sâu sắc: **một thuật toán đồ thị đơn giản dựa trên đại số tuyến tính cơ bản có thể tạo ra ngành công nghiệp trị giá nghìn tỷ đô-la**.

## 9. 2000s-2020s - Mạng Xã hội và Khoa học Mạng

**Facebook** ($$2004$$): đồ thị bạn bè, hơn $$3$$ tỷ người dùng.

**Twitter/X** ($$2006$$): đồ thị có hướng follower-followee.

**LinkedIn**: đồ thị nghề nghiệp toàn cầu.

**TikTok** ($$2016$$): đồ thị "for you" với thuật toán đề xuất dựa trên random walk biến tướng.

Khoa học mạng (**network science**) trở thành ngành học chính thức tại Harvard, Stanford, MIT, Đại học Oxford. Tạp chí *Network Science* (Cambridge) ra đời $$2013$$.

## 10. Bài toán Mở Đương đại

Lý thuyết đồ thị còn nhiều câu hỏi chưa có lời giải đẹp:

- **Bài toán Người du lịch (TSP)**: tìm đường ngắn nhất đi qua mọi đỉnh - NP-khó (sẽ học chương 20).
- **Đoán Erdős-Ko-Rado tổng quát**: cấu trúc của các họ tập giao đôi.
- **Đoán Hadwiger**: nếu $$\chi(G) \geq k$$ thì $$G$$ chứa $$K_k$$-minor.
- **Tính chất mạng động**: làm sao mô hình hóa mạng thay đổi theo thời gian?
- **Lan truyền thông tin/dịch bệnh**: dự đoán superspreader, kiểm soát viral marketing.
- **Mạng đối抗tướng** (adversarial): bảo vệ mạng điện, mạng máy tính khỏi tấn công có chủ đích.

## 11. Ứng dụng Bạn dùng Hằng ngày

Mỗi lần bạn:

- Tìm Google → PageRank.
- Lướt Facebook News Feed → graph ranking, PageRank cải tiến.
- Xem gợi ý phim Netflix → bipartite graph (user, movie), collaborative filtering.
- Dùng GPS Google Maps → shortest path (Dijkstra, A*).
- Xem feed TikTok → random walk trên đồ thị video-user.
- Kết nối Wi-Fi → spanning tree protocol.
- Gửi tin nhắn → định tuyến gói tin qua mạng máy tính (graph routing).
- Đăng nhập tài khoản ngân hàng → phát hiện gian lận bằng đồ thị giao dịch.

Lý thuyết đồ thị không phải là toán học "đẹp nhưng vô dụng" - nó là **kết cấu xương sống** của thế giới số.

## Tổng kết

- $$1736$$: Euler giải Königsberg, khai sinh graph theory.
- $$1847$$-$$1976$$: Kirchhoff, Cayley, Hall, König, Ford-Fulkerson xây dựng các định lý cấu trúc.
- $$1959$$-$$1967$$: Erdős-Rényi (đồ thị ngẫu nhiên), Milgram (sáu độ phân tách).
- $$1998$$-$$1999$$: Watts-Strogatz (small-world), Barabási-Albert (scale-free), Page-Brin (PageRank).
- $$2000s$$+: bùng nổ network science, mạng xã hội, ứng dụng đại trà.
- Đồ thị là **mô hình toán học chung** cho mọi hệ thống có **quan hệ** giữa các thực thể.

## Bài tập

1. Tìm thông tin về một mạng thực có quy mô lớn (Facebook social graph, mạng trích dẫn arXiv, mạng tương tác protein). Liệt kê: số đỉnh, số cạnh, đường kính, phân phối bậc.
2. Tự thiết kế một mô hình đồ thị nhỏ ($$\sim 20$$ đỉnh) cho mạng bạn bè trong lớp. Tính đường kính, hệ số clustering, các hub.
3. Viết một bài luận ngắn ($$300-500$$ chữ) về việc một thuật toán đồ thị nào đó đã ảnh hưởng đến cuộc sống của bạn.
4. So sánh ba mô hình mạng (Erdős-Rényi, Watts-Strogatz, Barabási-Albert) về tính chất nào (đường kính, clustering, phân phối bậc) phù hợp với mạng thực nào.
5. Tìm hiểu một bài toán mở của lý thuyết đồ thị (TSP, P vs NP, Hadwiger) và viết tóm tắt $$200$$ chữ về hiện trạng nghiên cứu.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Euler, L. (1736). *Solutio problematis ad geometriam situs pertinentis*. Commentarii Academiae Scientiarum Petropolitanae.
- Watts, D. J., Strogatz, S. H. (1998). *Collective dynamics of 'small-world' networks*. Nature 393, 440-442.
- Barabási, A.-L., Albert, R. (1999). *Emergence of scaling in random networks*. Science 286, 509-512.
- Page, L., Brin, S. (1998). *The PageRank Citation Ranking*. Stanford InfoLab.
- Newman, M. (2018). *Networks* (2nd ed.). Oxford University Press.
- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press. (Có bản online miễn phí.)
</div>
