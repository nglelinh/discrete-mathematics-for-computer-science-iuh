---
layout: post
title: "Combinatorial explosion trong kiểm thử: Từ 324 xuống 15 test"
categories: chapter09
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Phân tích hiện tượng bùng nổ tổ hợp (combinatorial explosion) theo quy tắc nhân trong kiểm thử phần mềm và cách kiểm thử pairwise (2-wise) giảm 324 cấu hình xuống khoảng 15 ca kiểm thử."
---

Một yêu cầu tưởng rất hợp lý trong buổi họp sprint — *"nhớ test hết mọi tổ hợp trình duyệt, hệ điều hành, thiết bị và cổng thanh toán nhé!"* — thực ra lại là một cái bẫy toán học. Chỉ cần thêm vài tùy chọn vào giao diện, số kịch bản kiểm thử không cộng thêm vài chục ca mà nhân vọt lên hàng nghìn, vượt xa quỹ thời gian của cả đội QA.

**Mạch bài học:** **Quy tắc nhân** và hiện tượng bùng nổ tổ hợp $$N = \prod v_i$$ $$\longrightarrow$$ quan sát thực nghiệm rằng phần lớn lỗi phần mềm xuất phát từ tương tác **1 hoặc 2 tham số** $$\longrightarrow$$ **kiểm thử theo cặp (pairwise / covering arrays)** rút 324 ca xuống ~15 ca.

## Kiến thức cần nhớ: Toán tổ hợp trong kiểm thử phần mềm nghiên cứu gì?

- **Quy tắc nhân & Tích Descartes (Product Rule):** Với $$k$$ tham số độc lập mà tham số thứ $$i$$ có $$v_i$$ giá trị, không gian cấu hình đầy đủ là tích Descartes $$S_1 \times \cdots \times S_k$$ có lực lượng $$N = \prod_{i=1}^k v_i$$ — tăng theo hàm mũ theo số tham số $$k$$.
- **Mảng phủ $$t$$-chiều (Covering Arrays $$CA(N; t, k, v)$$):** Đối tượng cốt lõi của tổ hợp ứng dụng: tìm tập con nhỏ nhất gồm $$N$$ dòng cấu hình sao cho với mọi nhóm $$t$$ cột bất kỳ (thường $$t=2$$, tức *pairwise*), **mọi bộ giá trị $$t$$-chiều có thể đều xuất hiện ít nhất một lần**.
- **Đánh đổi độ phủ và chi phí (Coverage–Cost Trade-off):** Dùng chứng cứ thực nghiệm (như nghiên cứu của NIST cho thấy phần lớn lỗi thực tế bị kích hoạt bởi tương tác 1–2 tham số) để phân bổ ngân sách kiểm thử có cơ sở toán học thay vì chọn cảm tính.

Ở bài connection pool, chúng ta đã thấy tác hại của việc nhầm lẫn giữa các đại lượng đếm (DAU, RPS và kết nối bận). Mục này xét một bài toán đếm khác trong **kiểm thử phần mềm**: **bùng nổ tổ hợp** (combinatorial explosion). Khi kết hợp nhiều tham số môi trường (trình duyệt × hệ điều hành × thiết bị × …), số cấu hình kiểm thử vét cạn (exhaustive) tăng theo **tích** chứ không theo tổng. Câu hỏi “vì sao không kiểm thử hết mọi tổ hợp?” thường xuất phát từ việc chưa tính trực tiếp tích $$N = \prod v_i$$.

Hương, trưởng nhóm QA phụ trách luồng thanh toán, gặp câu hỏi đó gần như mỗi sprint. Khi lập bảng cho luồng **đăng ký / thanh toán** mới bàn giao — gồm 5 tham số là trình duyệt, hệ điều hành, loại người dùng, thiết bị và trạng thái ứng dụng — áp dụng quy tắc nhân đã cho ra **324 cấu hình** chỉ riêng cho một luồng. Nếu bổ sung thêm cổng thanh toán, ngôn ngữ (locale) hay điều kiện mạng chậm, con số lập tức lên tới **hàng nghìn**. Với mỗi cấu hình gồm 10 bước kiểm tra, một sprint hai tuần hoàn toàn không đủ thời gian để chạy hết, chưa kể các bộ kiểm thử hồi quy (regression) khác.

Hiện tượng này gọi là **combinatorial explosion**: không gian tổ hợp phình to vượt xa thời gian thực thi của con người. [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) mô tả rõ vấn đề này ở tầng kiểm thử giao diện, còn [Optivem Journal](https://journal.optivem.com/p/combinatorial-explosion) (Valentina Jemuović) phân tích thêm rằng bùng nổ tổ hợp cũng xảy ra ở unit test khi nhân các tham số đầu vào. Giải pháp thực tế không phải “kiểm thử qua loa” mà là **kiểm thử theo cặp** (**pairwise / 2-wise testing**): bảo đảm **mọi cặp** giá trị giữa hai tham số bất kỳ đều xuất hiện ít nhất một lần, thường chỉ cần **15–20** ca kiểm thử thay vì 324.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Exponential.svg"
       alt="So sánh tăng trưởng tuyến tính, lũy thừa và hàm mũ 2^x"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.6a: Quy tắc nhân tạo ra 324 cấu hình; kỹ thuật pairwise rút gọn xuống khoảng 15 ca kiểm thử bằng cách phủ mọi *cặp* tham số thay vì mọi *bộ* năm chiều (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Exponential.svg">McSush / Wikimedia Commons</a>, public domain / CC0).</figcaption>
</p>
</figure>

---

## 324 cấu hình — khi quy tắc nhân thể hiện bằng con số cụ thể

Để Product Manager thấy rõ quy mô thực tế, Hương liệt kê năm tham số vào một bảng:

| Tham số | Giá trị | Số lượng |
|:---|:---|:---:|
| Browser | Chrome, Firefox, Edge, Safari | 4 |
| OS | Windows, macOS, Linux | 3 |
| User type | Admin, Standard, Guest | 3 |
| Device | Desktop, Tablet, Mobile | 3 |
| App state | Logged In, Logged Out, Error | 3 |

Kiểm thử **vét cạn** (exhaustive) đòi hỏi chạy qua tất cả các bộ giá trị có thể. Với $$k$$ tham số, trong đó tham số thứ $$i$$ có $$v_i$$ giá trị, tổng số cấu hình là:

<div class="textbook-equation" markdown="1">
$$N = \prod_{i=1}^{5} v_i = 4 \cdot 3 \cdot 3 \cdot 3 \cdot 3 = 4 \times 3^4 = 324$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Mỗi tham số bổ sung sẽ **nhân** thêm một thừa số chứ không chỉ cộng thêm vài ca kiểm thử. Vì thế, yêu cầu tưởng như nhỏ (“thêm một tùy chọn nữa”) có thể làm khối lượng kiểm thử tăng gấp đôi hoặc gấp ba.

![Combinatorial growth — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Exponential.svg)

<p class="textbook-figure-caption" data-figure="9.13">Quy tắc nhân — mỗi tham số mới nhân thêm một hệ số vào tổng số cấu hình.</p>

Hệ quả thực tế rất rõ ràng: chạy vét cạn 324 cấu hình làm chậm tiến độ phát hành do lặp lại nhiều kiểm tra dư thừa (cùng một lỗi giao diện xuất hiện giống nhau trên cả Chrome/Windows và Chrome/macOS). Ngược lại, nếu chỉ chọn ngẫu nhiên vài tổ hợp mà không có chiến lược, các lỗi phụ thuộc vào tương tác cụ thể (như **Chrome + Linux + Guest + Mobile + Error**) dễ bị bỏ sót. Với 324 cấu hình và 5 phút cho mỗi ca kiểm thử, chỉ riêng luồng này đã tiêu tốn **27 giờ** — chưa tính toàn bộ bộ kiểm thử hồi quy của sprint.

---

## Pairwise — phủ mọi cặp tham số thay vì mọi bộ năm chiều

**Kiểm thử pairwise** (2-wise) đặt ra một tiêu chí gọn hơn kiểm thử vét cạn nhưng có cơ sở thực nghiệm vững chắc: mọi **cặp** giá trị $$(v_i, v_j)$$ thuộc **hai tham số khác nhau bất kỳ** phải xuất hiện trong **ít nhất một** ca kiểm thử. Kỹ thuật này không đảm bảo phủ toàn bộ các bộ năm chiều, mà tập trung phủ trọn mọi tương tác hai chiều — một sự đánh đổi có kiểm soát vì thực tế cho thấy đa số lỗi phát sinh từ tương tác giữa hai yếu tố (như trình duyệt × hệ điều hành, thiết bị × ngôn ngữ).

Hương lập bảng minh họa rút gọn dựa trên ví dụ từ [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) gồm 8 ca kiểm thử để giải thích nguyên lý; trên thực tế, công cụ **PICT** (Pairwise Independent Combinatorial Testing của Microsoft) thường sinh khoảng **9–15** ca kiểm thử cho bài toán 324 cấu hình này:

| TC | Browser | OS | User | Device | State |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Chrome | Win | Admin | Desktop | In |
| 2 | Firefox | Mac | Standard | Tablet | Out |
| 3 | Edge | Linux | Guest | Mobile | Error |
| 4 | Safari | Win | Standard | Mobile | In |
| 5 | Chrome | Mac | Guest | Desktop | Out |
| 6 | Firefox | Linux | Admin | Tablet | Error |
| 7 | Edge | Win | Standard | Mobile | Out |
| 8 | Safari | Linux | Admin | Desktop | Error |

Mười lăm ca kiểm thử, mỗi ca 5 phút, chỉ mất **75 phút** — tiết kiệm khoảng **95%** thời gian so với 27 giờ chạy vét cạn. Để trả lời câu hỏi “liệu như vậy có đủ không?”, Hương viện dẫn cơ sở toán học phía sau kỹ thuật pairwise.

Trong lý thuyết kiểm thử tổ hợp, bộ ca kiểm thử được mô hình hóa bằng **mảng phủ** (**covering array**): một ma trận $$A$$ kích thước $$N \times k$$ ($$N$$ hàng kiểm thử, $$k$$ cột tham số) sao cho với mọi cặp cột $$(i, j)$$, mọi cặp giá trị $$(v_i, v_j)$$ có thể đều xuất hiện ở ít nhất một hàng. Bài toán tìm giá trị $$N$$ nhỏ nhất cho một covering array 2-wise là bài toán tối ưu rời rạc thuộc lớp NP-hard trong trường hợp tổng quát. Các thuật toán heuristic trong PICT, Hexawise hay ACTS cho kết quả đủ gọn cho môi trường production; kỹ sư QA không cần giải tay nhưng cần hiểu rõ bộ kiểm thử của mình **đang phủ phần nào** và **đang bỏ qua phần nào**.

---

## Optivem Journal — bùng nổ tổ hợp không chỉ xảy ra ở trình duyệt

Khi trao đổi với lập trình viên về chiến lược kiểm thử, Hương thường gặp sự đánh đổi mà [Optivem Journal](https://journal.optivem.com/p/combinatorial-explosion) phân tích: kiểm thử **end-to-end** qua giao diện người dùng phản ánh sát hành vi thật và bền vững khi tái cấu trúc mã, nhưng rất dễ **bùng nổ tổ hợp** khi nhân trình duyệt × hệ điều hành × thiết bị × ngôn ngữ. Ngược lại, viết **unit test bám sát từng lớp** (một lớp kiểm thử cho mỗi lớp sản phẩm) ít bị bùng nổ tổ hợp hơn nhưng lại **dễ vỡ** (fragile) mỗi khi tái cấu trúc (refactor): chỉ cần đổi tên phương thức hoặc tách dịch vụ là hàng loạt test hỏng dù hành vi nghiệp vụ không thay đổi. Robert C. Martin (Uncle Bob) cũng bàn về mâu thuẫn này trong bài [TDD Harms Architecture](https://blog.cleancoder.com/uncle-bob/2017/03/03/TDD-Harms-Architecture.html).

Giải pháp mà Optivem đề xuất kết hợp tự nhiên với pairwise: chọn các **điểm vào ổn định** (như API hoặc use case nghiệp vụ) rồi áp dụng **pairwise trên tham số đầu vào**, tách khỏi cấu trúc lớp nội bộ. Nhóm của Hương áp dụng theo quy trình này cho luồng thanh toán: định nghĩa mô hình tham số, dùng PICT sinh tập cấu hình, rồi ánh xạ từng dòng thành một ca kiểm thử hướng dữ liệu (data-driven test) chạy tự động trong CI.

Quy trình thực tế với Microsoft PICT:

```bash
# File model.txt — khai báo từng tham số và giá trị:
# Browser: Chrome, Firefox, Edge, Safari
# OS: Win, Mac, Linux
# User: Admin, Standard, Guest
# Device: Desktop, Tablet, Mobile
# State: In, Out, Error
pict model.txt > tests.txt
```

Mỗi dòng trong `tests.txt` là một bộ cấu hình; `pytest.mark.parametrize`, testRigor hoặc framework tương đương đọc tệp này để chạy cùng một kịch bản với các đầu vào khác nhau. Thay vì tranh luận cảm tính, quy mô tổ hợp được lượng hóa rõ ràng: PM thấy 15 dòng thay vì 324, còn lập trình viên dễ dàng rà soát trực tiếp tệp `model.txt`.

<div class="content-box warning-box textbook-block" markdown="1">
Pairwise **không** đảm bảo phủ mọi bộ ba (3-tuple). Những lỗi chỉ xảy ra khi **Chrome + Linux + cổng thanh toán X** đồng thời xuất hiện cần kiểm thử **3-wise** hoặc ca kiểm thử nhắm mục tiêu (targeted test) cho các tổ hợp rủi ro cao. Pairwise là phương pháp **giảm tổ hợp có chủ đích**, không thay thế kiểm thử vét cạn khi quy định tuân thủ (compliance) hoặc hợp đồng bắt buộc kiểm tra 100% cấu hình.
</div>

---

## Kết quả thực tế — phê duyệt và bổ sung khi phát hiện tổ hợp thiếu

Hương gửi PM bảng 15 ca kiểm thử do PICT sinh kèm ghi chú rõ ràng: “Phủ 100% các cặp (Browser, OS), (Browser, Device), (OS, User)…, không phủ toàn bộ 324 bộ năm chiều.” PM đồng ý. Tuần tiếp theo, một lỗi phát sinh trên production với tổ hợp **Safari + iPhone + locale vi + OAuth** — tổ hợp chưa có trong mô hình cũ vì ban đầu chưa đưa cột ngôn ngữ và phương thức xác thực vào bảng. Nhóm lập tức bổ sung kiểm thử **3-wise** cho luồng xác thực và thêm ca kiểm thử nhắm trực tiếp vào tổ hợp Safari × di động × OAuth.

Bùng nổ tổ hợp là nguyên nhân thực tế gây trễ lịch phát hành hoặc sót lỗi khi số tham số tăng nhanh hơn thời gian kiểm thử. Pairwise không phải cách cắt giảm tùy tiện mà là **phương pháp đếm có hệ thống**, giúp nhóm kiểm soát rõ phạm vi bao phủ và mức rủi ro chấp nhận được.

**Đọc thêm:** [testRigor — Combinatorial Testing](https://testrigor.com/blog/what-is-combinatorial-testing/) · [Optivem — Combinatorial Explosion](https://journal.optivem.com/p/combinatorial-explosion) · [Microsoft PICT](https://github.com/microsoft/pict)

---

## Ví dụ tính tay làm từng bước: Giảm 8 cấu hình xuống 4 ca kiểm thử Pairwise hoàn hảo

Xét một mô-đun thanh toán nhỏ có **3 tham số nhị phân** (mỗi tham số 2 giá trị):
- **Trình duyệt (B):** Chrome (`C`), Safari (`S`)
- **Hệ điều hành (O):** macOS (`M`), Windows (`W`)
- **Chế độ mạng (N):** Nhanh (`F`), Chậm (`L`)

1. **Kiểm thử vét cạn (Exhaustive):** Số cấu hình là $$2 \times 2 \times 2 = 8$$ ca.
2. **Đếm tổng số cặp giá trị cần phủ cho Pairwise ($$t=2$$):**
   - Cặp (B, O): $$2 \times 2 = 4$$ cặp (`CM, CW, SM, SW`).
   - Cặp (B, N): $$2 \times 2 = 4$$ cặp (`CF, CL, SF, SL`).
   - Cặp (O, N): $$2 \times 2 = 4$$ cặp (`MF, ML, WF, WL`).
   - Tổng cộng có $$4 + 4 + 4 = 12$$ cặp cần phủ. Vì mỗi ca kiểm thử chứa $$\binom{3}{2} = 3$$ cặp, cận dưới lý thuyết tối thiểu là $$\lceil 12 / 3 \rceil = 4$$ ca.
3. **Dựng tay bộ 4 ca kiểm thử đạt đúng cận dưới (bảng trực giao $$OA(4, 3, 2, 2)$$):**

| Ca test | Trình duyệt (B) | Hệ điều hành (O) | Mạng (N) | 3 cặp được phủ |
| :--- | :--- | :--- | :--- | :--- |
| T1 | C | M | F | (C,M), (C,F), (M,F) |
| T2 | C | W | L | (C,W), (C,L), (W,L) |
| T3 | S | M | L | (S,M), (S,L), (M,L) |
| T4 | S | W | F | (S,W), (S,F), (W,F) |

4. **Kiểm tra thủ công:** Đếm cột cuối cùng — cả **12/12 cặp** đều xuất hiện đúng 1 lần, không thiếu cặp nào, trong khi số ca kiểm thử giảm một nửa (từ 8 xuống 4). Khi số tham số tăng lên 5–10 biến, tỷ lệ nén nhảy vọt từ $$324 \to 15$$ hoặc từ hàng chục nghìn xuống vài chục ca!

### Giải thích: Tại sao Pairwise đánh bại bùng nổ tổ hợp
1. **Bước 1 — Chiều sâu nhân nhanh hơn chiều rộng:** Mỗi khi thêm một tham số mới có 3 giá trị, không gian vét cạn nhân 3 ngay lập tức, còn số cặp mới cần phủ chỉ tăng tuyến tính theo số tham số hiện có.
2. **Bước 2 — Một ca kiểm thử phủ nhiều cặp cùng lúc:** Với $$k$$ tham số, một dòng cấu hình duy nhất đồng thời kiểm tra $$\binom{k}{2}$$ cặp tham số. Nhờ tính "chia sẻ dòng" này, kích thước mảng phủ pairwise tăng xấp xỉ theo $$O(\log k)$$ thay vì $$O(v^k)$$.
3. **Bước 3 — Nhắm trúng vùng mật độ lỗi cao:** Phần lớn lỗi tương thích đến từ một giá trị đơn lẻ (1-way) hoặc xung đột giữa hai thành phần (2-way, ví dụ Safari + OAuth).
4. **Bước 4 — Kết hợp rủi ro nghiệp vụ:** Pairwise là nền tảng tối ưu; với vài tổ hợp bậc 3 đặc biệt nhạy cảm (như iOS + Safari + cổng thanh toán chính), ta chủ động bổ sung thêm vài ca mục tiêu.

$$N_{\text{exhaustive}} = \prod_{i=1}^k v_i \sim v^k \quad\text{vs.}\quad N_{\text{pairwise}} \approx O(v^2 \log k).$$

## Bài tập thực hành

### Bài tập 1

Một biểu mẫu đăng ký cần kiểm thử trên 3 trình duyệt, 2 hệ điều hành, 4 loại người dùng và 2 loại thiết bị. Tính tổng số cấu hình kiểm thử vét cạn (viết dưới dạng tích và kết quả cụ thể).

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$N = 3 \times 2 \times 4 \times 2 = 48 \text{ cấu hình}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Theo quy tắc nhân, mỗi tham số nhân thêm một hệ số. Nếu thêm chỉ một giá trị cho “loại người dùng” (từ 4 lên 5), tổng số cấu hình tăng lên $$3 \times 2 \times 5 \times 2 = 60$$ — tăng thêm 12 cấu hình chứ không phải 1 ca kiểm thử.

</details>

### Bài tập 2

Với bài toán 324 cấu hình (4 trình duyệt × $$3^4$$), kiểm thử vét cạn mất 27 giờ nếu mỗi ca tốn 5 phút. Kiểm thử pairwise sinh ra 15 ca với cùng thời gian mỗi ca. Tính thời gian chạy pairwise và tỷ lệ phần trăm thời gian tiết kiệm được (làm tròn đến số nguyên).

<details>
<summary>Đáp án</summary>

Kiểm thử vét cạn: $$324 \times 5 = 1620$$ phút = **27 giờ**.

Kiểm thử pairwise: $$15 \times 5 = 75$$ phút = **1 giờ 15 phút**.

Phần trăm thời gian tiết kiệm: $$(1620 - 75) / 1620 \approx 95{,}4\%$$ — khoảng **95%**.

</details>

### Bài tập 3

Cho ba tham số: **Browser** $$\in \{\text{Chrome, Firefox}\}$$, **OS** $$\in \{\text{Win, Mac}\}$$, **Device** $$\in \{\text{Desktop, Mobile}\}$$. Tính số cấu hình vét cạn và giải thích vì sao pairwise chỉ giảm được số ca kiểm thử khi có từ **ba** tham số trở lên (không giảm được khi chỉ có **hai** tham số).

<details>
<summary>Đáp án</summary>

Số cấu hình vét cạn:

<div class="textbook-equation" markdown="1">
$$N = 2 \times 2 \times 2 = 8 \text{ cấu hình}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Pairwise yêu cầu phủ mọi cặp giá trị thuộc hai trong ba cột: (Browser, OS), (Browser, Device) và (OS, Device). Một hàng kiểm thử chứa một bộ ba nhưng đồng thời phủ được **ba** cặp cùng lúc — chẳng hạn `(Chrome, Win, Desktop)` phủ đồng thời `(Chrome, Win)`, `(Chrome, Desktop)` và `(Win, Desktop)`. Nhờ vậy, PICT có thể phủ toàn bộ các cặp chỉ với **4** ca kiểm thử thay vì 8.

Khi chỉ có **hai** tham số (ví dụ Browser × OS = $$2 \times 3 = 6$$), mỗi hàng chỉ phủ đúng **một** cặp nên kiểm thử 2-wise trùng hoàn toàn với vét cạn. Lợi thế của pairwise chỉ phát huy rõ khi $$k \geq 3$$ tham số, như ví dụ 324 cấu hình với 5 tham số ở trên.

</details>

### Bài tập 4

Theo Optivem Journal, vì sao kiểm thử end-to-end dễ bị bùng nổ tổ hợp còn kiểm thử từng lớp lại dễ vỡ khi tái cấu trúc? Kiểm thử pairwise trên đầu vào API giải quyết được phần nào của hai vấn đề này?

<details>
<summary>Đáp án</summary>

Kiểm thử **end-to-end** đi qua nhiều tầng (giao diện, mạng, cơ sở dữ liệu), mỗi tầng bổ sung thêm tham số (trình duyệt, hệ điều hành, thiết bị, ngôn ngữ…) làm tổng số tổ hợp nhân lên nhanh chóng (**bùng nổ tổ hợp**). Ngược lại, **kiểm thử bám sát từng lớp** phụ thuộc vào cấu trúc mã nội bộ nên khi đổi tên phương thức hoặc tái cấu trúc lớp, test dễ hỏng dù hành vi nghiệp vụ không đổi (**dễ vỡ**).

Áp dụng **pairwise trên đầu vào API** giảm bùng nổ tổ hợp bằng mảng phủ 2-wise thay vì vét cạn, đồng thời điểm vào API/use case ổn định hơn nhiều so với cấu trúc lớp nội bộ nên giảm nguy cơ vỡ test khi refactor. Tuy vậy, cách này không thay thế hoàn toàn kiểm thử giao diện và cũng không tự động phủ tương tác 3 chiều nếu không mở rộng lên 3-wise hoặc bổ sung ca kiểm thử mục tiêu.

</details>

---

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

Bùng nổ tổ hợp trong kiểm thử là hệ quả trực tiếp của **quy tắc nhân**: $$N = \prod v_i$$. Chỉ với 4 trình duyệt và 4 tham số khác mỗi tham số 3 giá trị, luồng thanh toán đã tạo ra $$4 \times 3^4 = 324$$ cấu hình — vượt quá quỹ thời gian chạy vét cạn của một sprint thông thường.

**Kiểm thử pairwise (2-wise)** yêu cầu mọi **cặp** giá trị từ hai tham số khác nhau xuất hiện ít nhất một lần, giúp phát hiện phần lớn lỗi tương tác hai chiều chỉ với khoảng **15–20** ca kiểm thử thay vì 324. Khái niệm toán học **covering array** mô tả ma trận phủ tối thiểu, còn công cụ như **PICT** tự động sinh bộ kiểm thử từ tệp mô hình. Phân tích của **Optivem Journal** cho thấy kết hợp pairwise với các điểm vào ổn định như API vừa giảm bùng nổ tổ hợp vừa hạn chế test dễ vỡ khi tái cấu trúc mã.

Pairwise không thay thế kiểm thử vét cạn khi có yêu cầu tuân thủ nghiêm ngặt, và những lỗi đòi hỏi tương tác **ba** tham số cùng lúc vẫn cần kiểm thử 3-wise hoặc ca kiểm thử mục tiêu.

Bài tiếp theo sẽ xét **nghịch lý sinh nhật (Birthday paradox) trong production** theo phân tích của [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/) — vì sao các định danh ngẫu nhiên 32-bit, 64-bit hay UUID có thể **va chạm** sớm hơn nhiều so với trực giác dù không gian giá trị trông rất lớn.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=jlOcUOK3gNQ">The Power of Pairwise Testing: Maximize Coverage, Minimize Effort!</a> — Testing.Business, tiếng Anh. Giới thiệu trực quan kỹ thuật pairwise: phủ mọi cặp tham số thay vì vét cạn mọi bộ cấu hình.
- <a href="https://www.youtube.com/watch?v=Kn8J4bRhghc">Using Pairwise Testing to Improve Your Test Coverage</a> — Construx Software, tiếng Anh. Trình bày cách kiểm thử pairwise mở rộng độ phủ mà không làm bùng nổ số ca kiểm thử.
- <a href="https://www.youtube.com/watch?v=8JiWWvEoaoc">RULE of SUM and RULE of PRODUCT - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Ôn lại quy tắc cộng và quy tắc nhân giải thích nguồn gốc của 324 cấu hình.
