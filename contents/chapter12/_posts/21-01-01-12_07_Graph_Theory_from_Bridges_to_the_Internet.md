---
layout: post
title: "Lý thuyết Đồ thị: Từ những cây cầu đến Internet"
categories: chapter12
date: 2021-01-01
order: 7
required: false
lang: en
---

# Lý thuyết Đồ thị: Từ những cây cầu đến Internet

Có lẽ không nhiều lĩnh vực trong toán rời rạc có câu chuyện mở đầu đẹp như graph theory.
Một bài toán đi dạo qua các cây cầu của thành phố Königsberg
đã khai sinh cả một ngành.

Nhưng vẻ đẹp của đồ thị không chỉ nằm ở lịch sử.
Ngày nay,
đồ thị ở khắp nơi:
Internet routing,
social networks,
dependency scheduling,
circuit design,
search ranking,
transport systems.

Khi thế giới số ngày càng kết nối,
graph theory ngày càng giống bản đồ của chính thực tại tính toán.

---

## Phần 1: Euler và bảy cây cầu Königsberg năm 1736

### 1.1. Bài toán tưởng là trò giải trí

Người dân Königsberg từng hỏi:
có thể đi bộ qua tất cả bảy cây cầu đúng một lần hay không?

Nghe như câu đố du lịch.
Nhưng Leonhard Euler đã làm điều thiên tài:
ông bỏ qua chi tiết địa lý cụ thể,
giữ lại cấu trúc kết nối trừu tượng.

Đó là khoảnh khắc đồ thị ra đời.

### 1.2. Từ bản đồ thật sang mô hình trừu tượng

Euler xem mỗi vùng đất là đỉnh,
mỗi cây cầu là cạnh.
Thế là bài toán địa lý biến thành bài toán cấu trúc.

Chính nước đi trí tuệ này
định nghĩa tinh thần của graph theory:
giữ lại quan hệ kết nối,
loại bỏ chi tiết không cần thiết.

![Bảy cây cầu Königsberg]
*Hình 1: Bài toán cầu Königsberg là khoảnh khắc lịch sử khi kết nối được trừu tượng hóa thành đỉnh và cạnh.*

---

## Phần 2: Internet routing và shortest paths

### 2.1. Internet là một đồ thị khổng lồ

Router,
autonomous systems,
links,
latency,
bandwidth,
failover.

Tất cả đều có thể nhìn như đồ thị.

Khi một gói tin đi từ nơi này đến nơi khác,
ta đang giải bài toán chọn đường trên graph.

### 2.2. Dijkstra và shortest path thinking

Dijkstra’s algorithm là ví dụ nổi tiếng về sức mạnh của graph algorithms.
Nó trả lời:
đường đi có tổng trọng số nhỏ nhất từ nguồn tới các đỉnh khác là gì?

Trong đời thực,
“ngắn nhất” có thể nghĩa là:

- ít độ trễ nhất,
- ít chi phí nhất,
- ít rủi ro nhất,
- ít hops nhất,
- hoặc cân bằng nhiều tiêu chí.

### 2.3. BGP và thực tế không chỉ là shortest path thuần túy

Internet routing ngoài đời còn phức tạp hơn vì có chính sách,
kinh tế,
và quyền tự trị của các mạng con.

BGP không chỉ hỏi “đường nào ngắn nhất”.
Nó hỏi “đường nào hợp lệ và chấp nhận được theo policy”.

Đây là ví dụ hay cho sinh viên:
toán cho ta lõi mô hình,
còn hệ thống thật thêm ràng buộc đời thực vào đó.

---

## Phần 3: Social network analysis và centrality

### 3.1. Xã hội số có thể được vẽ thành đồ thị

Người dùng là đỉnh.
Quan hệ theo dõi,
kết bạn,
nhắn tin,
tương tác
là cạnh.

Một mạng xã hội lớn là một đồ thị cực lớn,
và câu hỏi sản phẩm lẫn kinh doanh đều trở thành câu hỏi graph analytics.

### 3.2. PageRank và tầm quan trọng theo liên kết

Một trong những ví dụ nổi tiếng nhất là PageRank.
Ý tưởng cốt lõi:
trang quan trọng là trang được nhiều trang quan trọng khác trỏ tới.

Đây là ví dụ kinh điển của việc
biến khái niệm “uy tín” thành bài toán trên đồ thị có thể tính được.

### 3.3. Centrality trong phân tích ảnh hưởng

Không phải mọi nút có nhiều cạnh đều giống nhau.
Một nút có thể đóng vai trò cầu nối,
trung gian,
hoặc hạt nhân cộng đồng.

Các thước đo như degree centrality,
betweenness,
closeness
giúp mô tả những vai trò đó.

![Social graph and PageRank]
*Hình 2: Phân tích mạng xã hội biến các mối quan hệ giữa con người thành bài toán đo cấu trúc và ảnh hưởng.*

---

## Phần 4: Compiler design và dependency graphs

### 4.1. Build systems là đồ thị phụ thuộc

Khi bạn chạy build,
hệ thống phải biết file nào phụ thuộc file nào,
module nào cần biên dịch trước,
task nào có thể chạy song song.

Đó là dependency graph.

### 4.2. Topological ordering và scheduling

Nếu phụ thuộc không có chu trình,
ta có DAG.
Khi đó,
topological sort cho ta thứ tự thực thi hợp lệ.

Điều này xuất hiện trong:

- compilers,
- package managers,
- workflow orchestration,
- CI/CD pipelines,
- data processing DAGs.

### 4.3. Cycle detection là chức năng sống còn

Nếu phụ thuộc tạo chu trình,
hệ thống có thể mắc kẹt.
Phát hiện cycle sớm
là ví dụ tuyệt vời của graph algorithms giúp hệ thống tránh trạng thái vô nghĩa.

---

## Phần 5: Circuit design và planar graphs

### 5.1. Mạch điện cũng là mạng kết nối

Trong VLSI,
PCB layout,
và circuit abstraction,
đồ thị giúp mô tả các thành phần và kết nối giữa chúng.

### 5.2. Planarity không chỉ là bài toán đẹp

Nếu một đồ thị có thể vẽ trên mặt phẳng mà không cắt cạnh,
ta gọi nó planar.
Ý tưởng này có hệ quả thực tế cho thiết kế mạch,
bố trí đường dây,
và một số bài toán layout.

### 5.3. Khi geometry gặp graph theory

Circuit design là ví dụ hay nơi cấu trúc graph và ràng buộc hình học gặp nhau.
Nó cho thấy đồ thị không chỉ là abstraction sạch trên giấy,
mà còn có hậu quả vật lý thật.

---

## Phần 6: Tương lai — graph everywhere

Graph thinking ngày càng quan trọng trong:

- recommendation,
- fraud detection,
- logistics,
- protein interaction networks,
- knowledge graphs,
- code analysis,
- AI agent planning.

Khi thế giới ngày càng liên kết,
đồ thị ngày càng trở thành mô hình mặc định cho những gì “quan hệ” và “phụ thuộc”.

---

## Kết luận

Từ Euler và cây cầu Königsberg,
đến Internet routing,
PageRank,
dependency graphs,
và circuit layout,
graph theory đã đi từ một câu đố thành phố
đến ngôn ngữ nền của thế giới kết nối.

Nếu chương 12 là một chương đặc biệt của toán rời rạc,
thì đó là vì nó chạm trực tiếp vào hình dạng của rất nhiều hệ thống hiện đại.

---

## Bài tập thực hành

### Bài tập 1: Mô hình hóa mạng

Vẽ đồ thị cho mạng sau: 4 router A,B,C,D; A kết nối B và C, B kết nối D, C kết nối D.

<details>
<summary>Đáp án</summary>

Đồ thị vô hướng với các cạnh: A-B, A-C, B-D, C-D.

</details>

### Bài tập 2: Đường đi ngắn nhất

Trong đồ thị trên, tìm đường ngắn nhất từ A đến D (theo số cạnh).

<details>
<summary>Đáp án</summary>

A → B → D hoặc A → C → D (độ dài 2).

</details>

### Bài tập 3: Ứng dụng Internet

Giải thích tại sao mô hình đồ thị giúp thiết kế giao thức định tuyến (routing).

<details>
<summary>Đáp án</summary>

Mỗi router chỉ cần biết hàng xóm (adjacency list). Thuật toán như Dijkstra hoặc Bellman-Ford tìm đường dựa trên đồ thị toàn cục hoặc cục bộ.

</details>

## Tóm tắt

Lý thuyết đồ thị là ngôn ngữ chung để mô tả kết nối — từ cầu Königsberg đến Internet, mạng xã hội, dependency graph và mạch điện. Hiểu các khái niệm cơ bản (đỉnh, cạnh, đường đi, chu trình) và các thuật toán kinh điển giúp chúng ta phân tích, thiết kế và tối ưu hóa mọi hệ thống có cấu trúc mạng. Đây là một trong những công cụ mạnh mẽ nhất của khoa học máy tính.
