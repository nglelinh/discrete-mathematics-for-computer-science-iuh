---
layout: post
title: "Combinatorial explosion trong kiểm thử: Từ 324 xuống 15 test"
categories: chapter09
date: 2021-01-01
order: 6
required: false
lang: en
---

Release thứ Tư, 16 giờ. PM hỏi trong standup: *“Sao không test hết combination?”*

Hương, QA lead của team checkout, không giận — cô đã nghe câu đó ở mỗi sprint. Cô mở spreadsheet luồng **đăng ký / checkout** mà dev vừa ship: trình duyệt, hệ điều hành, loại user, thiết bị, trạng thái đăng nhập — năm tham số, mỗi tham số vài giá trị. Nhân lại theo quy tắc tích từ chương đếm, chỉ riêng **một flow** đã là **324 cấu hình**. Thêm payment gateway, locale, mạng chậm — con số nhảy lên **hàng nghìn**. Mỗi cấu hình mười bước kiểm tra thì sprint hai tuần không đủ cho cả regression suite khác.

Đây là **combinatorial explosion** — không phải QA lười, mà **tổ hợp** lớn hơn thời gian con người. [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) mô tả hiện tượng này trong kiểm thử phần mềm; [Optivem Journal](https://journal.optivem.com/p/combinatorial-explosion) (Valentina Jemuović) phân tích sâu hơn: explosion không chỉ ở UI mà còn ở unit test khi nhân tham số đầu vào. Giải pháp không phải “test ít đi” mà **pairwise (2-wise) testing** — đảm bảo **mọi cặp** giá trị từ hai tham số đều xuất hiện ít nhất một lần, thường chỉ cần **15–20** test thay vì 324.

---

## 324 cấu hình — khi quy tắc nhân khiến PM im lặng

Hương ghi lại năm tham số vào bảng để PM nhìn thấy con số, không chỉ nghe chữ “nhiều”:

| Tham số | Giá trị | Số lượng |
|:---|:---|:---:|
| Browser | Chrome, Firefox, Edge, Safari | 4 |
| OS | Windows, macOS, Linux | 3 |
| User type | Admin, Standard, Guest | 3 |
| Device | Desktop, Tablet, Mobile | 3 |
| App state | Logged In, Logged Out, Error | 3 |

Kiểm thử **exhaustive** (thử hết mọi bộ) phải chạy qua mọi tổ hợp. Với $$k$$ tham số, tham số thứ $$i$$ có $$v_i$$ giá trị, tổng số cấu hình là tích:

$$N = \prod_{i=1}^{5} v_i = 4 \cdot 3 \cdot 3 \cdot 3 \cdot 3 = 4 \times 3^4 = 324$$

Bốn trình duyệt nhân với bốn lần “ba” — OS, user type, device, app state — không phải cộng. Mỗi tham số mới **nhân** thêm hệ số, không cộng thêm vài test. Đó là lý do PM tưởng “thêm một option nữa thôi mà” nhưng backlog QA phình gấp đôi, gấp ba.

![Combinatorial growth — Wikimedia](/discrete-mathematics-for-computer-science-iuh/img/course/Exponential.svg)

*Hình 9.13: Quy tắc nhân — mỗi tham số mới nhân thêm hệ số, không cộng.*

Hương đã thấy hệ quả thực tế của 324 cấu hình: release chậm vì team chạy test redundant — cùng một bug được tìm lại ở Chrome/Windows và Chrome/macOS mà không tìm thêm gì mới. Ngược lại, bug chỉ khi **Chrome + Linux + Guest + Mobile + Error** xảy ra **cùng lúc** dễ bị bỏ sót nếu test ngẫu nhiên không có chiến lược. 324 test, mỗi test năm phút, đã là **27 giờ** — chưa kể suite regression khác đang chờ cùng sprint.

---

## Pairwise — cover mọi cặp, không mọi bộ năm

**Pairwise testing** (2-wise) đặt một yêu cầu yếu hơn exhaustive nhưng có cơ sở thực nghiệm: mọi **cặp** giá trị $$(v_i, v_j)$$ từ **hai tham số khác nhau** phải xuất hiện trong **ít nhất một** test case. Không đảm bảo mọi **bộ năm** đồng thời — đảm bảo mọi **cặp** — trade-off có kiểm soát. Quan sát trong ngành: phần lớn bug do **tương tác hai chiều** (browser × OS, device × locale), không cần cả năm chiều cùng lúc mới lộ lỗi.

Hương dựng bảng demo rút gọn từ [testRigor](https://testrigor.com/blog/what-is-combinatorial-testing/) — tám test minh họa ý tưởng; công cụ **PICT** (Pairwise Independent Combinatorial Testing, Microsoft) thường sinh **khoảng 9–15** test cho bài toán 324 cấu hình:

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

Mười lăm test, mỗi test năm phút, là **75 phút** — tiết kiệm khoảng **95%** thời gian so với exhaustive 324 test. PM vẫn hỏi “có đủ không?”; Hương trả lời bằng định nghĩa toán học phía sau pairwise.

Trong lý thuyết combinatorial testing, bộ test được mô hình hóa bằng **covering array**: ma trận $$A$$ kích thước $$N \times k$$ ($$N$$ hàng test, $$k$$ cột tham số) sao cho với mọi cặp cột $$(i, j)$$, mọi cặp giá trị $$(v_i, v_j)$$ từ cột $$i$$ và $$j$$ xuất hiện ít nhất một hàng. Bài toán tìm **$$N$$ nhỏ nhất** cho một covering array 2-wise là tối ưu rời rạp — NP-hard trong tổng quát. Heuristic của PICT, Hexawise, hay ACTS đủ tốt cho production; QA không cần giải tay, nhưng cần hiểu mình đang **cover cái gì** và **không cover cái gì**.

---

## Optivem Journal — explosion không chỉ ở trình duyệt

Khi tranh luận với dev về “test đủ chưa”, Hương thường gặp nghịch lý mà [Optivem Journal](https://journal.optivem.com/p/combinatorial-explosion) nêu rõ. Test **hành vi end-to-end** qua UI — robust, gần user thật, nhưng **explosion** số test khi nhân browser × OS × device × locale. Test **từng class** (một test class cho một production class) — ít explosion hơn, nhưng **fragile** khi refactor: đổi tên method, tách service, toàn bộ test class vỡ dù hành vi user không đổi. Uncle Bob viết [TDD Harms Architecture](https://blog.cleancoder.com/uncle-bob/2017/03/03/TDD-Harms-Architecture.html) về mối căng này giữa test gắn diagram class và kiến trúc bền vững.

Hướng thoát Optivem gợi ý trùng với pairwise: chọn **entry point** ổn định (API, use case) và chạy **pairwise trên input** — không phụ thuộc sơ đồ class. Hương áp dụng cho checkout: thay vì mở năm trình duyệt thủ công, team định nghĩa model tham số, để PICT sinh tập test, rồi map mỗi dòng thành một data-driven test trong CI.

Workflow thực tế với Microsoft PICT:

```bash
# File model.txt — khai báo từng tham số và giá trị:
# Browser: Chrome, Firefox, Edge, Safari
# OS: Win, Mac, Linux
# User: Admin, Standard, Guest
# Device: Desktop, Tablet, Mobile
# State: In, Out, Error
pict model.txt > tests.txt
```

Mỗi dòng trong `tests.txt` là một bộ cấu hình; pytest `parametrize`, testRigor, hoặc framework tương đương đọc file đó và chạy cùng một kịch bản với input khác nhau. Explosion bị **đếm** trước khi chạy — PM thấy 15 dòng thay vì 324, dev thấy model.txt dễ review hơn spreadsheet.

<div class="content-box warning-box" markdown="1">
Pairwise **không** cover mọi 3-tuple. Bug chỉ khi **Chrome + Linux + cổng thanh toán X** cùng lúc cần **3-wise** (hoặc test targeted cho combo biết trước là rủi ro). Pairwise là công cụ **giảm tổ hợp có chủ đích**, không thay exhaustive khi compliance hoặc hợp đồng bắt buộc test 100% cấu hình.
</div>

---

## Epilogue — approve, rồi bổ sung khi thiếu cặp

Hương gửi PM bảng 15 test PICT kèm ghi chú: “Cover 100% cặp (Browser, OS), (Browser, Device), (OS, User), … — không cover 324 bộ năm.” PM approve. Tuần sau bug lên production trên **Safari + iPhone + locale vi + OAuth** — đúng tổ hợp mà bảng cũ chưa cover vì thiếu cột locale và payment; team bổ sung **3-wise** cho auth flow và thêm test targeted cho combo Safari × mobile × OAuth.

Combinatorial explosion không phải lý thuyết trên slide — là lý do release trễ và bug production khi người ta nhân tham số mà không nhân thời gian. Pairwise không phải “test ít cho vui”; là **công cụ đếm** để biết mình đang bỏ gì và chấp nhận rủi ro gì. Covering array nói rõ điều đó bằng ngôn ngữ toán; PICT và Optivem đưa nó vào pipeline thật.

**Đọc thêm:** [testRigor — Combinatorial Testing](https://testrigor.com/blog/what-is-combinatorial-testing/) · [Optivem — Combinatorial Explosion](https://journal.optivem.com/p/combinatorial-explosion) · [Microsoft PICT](https://github.com/microsoft/pict)

---

## Bài tập thực hành

### Bài tập 1

Một form đăng ký có 3 trình duyệt, 2 hệ điều hành, 4 loại user, 2 thiết bị. Tính số cấu hình exhaustive. Viết dưới dạng tích và ra số thập phân.

<details>
<summary>Đáp án</summary>

$$N = 3 \times 2 \times 4 \times 2 = 48 \text{ cấu hình}$$

Quy tắc nhân: mỗi tham số nhân thêm hệ số. Thêm một giá trị cho “loại user” (4 → 5) sẽ thành $$3 \times 2 \times 5 \times 2 = 60$$ — tăng 12 cấu hình, không chỉ thêm 1 test.

</details>

### Bài tập 2

Với bài toán 324 cấu hình (4 browser × $$3^4$$), exhaustive mất 27 giờ nếu mỗi test 5 phút. Pairwise sinh 15 test cùng thời gian mỗi test. Tính thời gian pairwise và phần trăm tiết kiệm (làm tròn số nguyên).

<details>
<summary>Đáp án</summary>

Exhaustive: $$324 \times 5 = 1620$$ phút = **27 giờ**.

Pairwise: $$15 \times 5 = 75$$ phút = **1 giờ 15 phút**.

Tiết kiệm: $$(1620 - 75) / 1620 \approx 95{,}4\%$$ — khoảng **95%** thời gian.

</details>

### Bài tập 3

Cho ba tham số: **Browser** $\in \{\text{Chrome, Firefox}\}$, **OS** $\in \{\text{Win, Mac}\}$, **Device** $\in \{\text{Desktop, Mobile}\}$. Tính số cấu hình exhaustive. Giải thích vì sao pairwise với **ba** tham số mới giảm được so với exhaustive (không giảm khi chỉ có **hai** tham số).

<details>
<summary>Đáp án</summary>

Exhaustive:

$$N = 2 \times 2 \times 2 = 8 \text{ cấu hình}$$

Pairwise phải cover mọi cặp giá trị giữa hai trong ba cột: (Browser, OS), (Browser, Device), (OS, Device). Một hàng test chứa **một** bộ (browser, OS, device) nhưng đồng thời “phục vụ” **ba** cặp — ví dụ hàng `(Chrome, Win, Desktop)` cover (Chrome, Win), (Chrome, Desktop), (Win, Desktop). Nhờ đó PICT có thể sinh **4** test cho model này thay vì 8.

Với **chỉ hai** tham số (ví dụ Browser × OS = $$2 \times 3 = 6$$), mỗi hàng chỉ cover đúng **một** cặp — 2-wise trùng exhaustive, không tiết kiệm. Lợi ích pairwise rõ khi $$k \geq 3$$ tham số, như bài 324 cấu hình với năm tham số.

</details>

### Bài tập 4

Theo Optivem Journal, vì sao test end-to-end dễ explosion còn test từng class dễ fragile? Pairwise trên API input giải quyết phần nào của hai vấn đề đó?

<details>
<summary>Đáp án</summary>

**End-to-end** đi qua nhiều tầng (UI, network, DB) — mỗi tầng thêm tham số (browser, OS, device, locale…) → nhân số tổ hợp → **explosion**. **Test từng class** bám sát cấu trúc code — refactor đổi class/method làm test vỡ dù hành vi nghiệp vụ không đổi → **fragile**.

**Pairwise trên API input** giảm explosion bằng covering array 2-wise thay vì nhân hết mọi input. Entry point API/use case ổn định hơn tên class — giảm fragile vì test không phụ thuộc diagram class. Không thay hoàn toàn e2e (vẫn cần vài test UI) và không cover 3-tuple trừ khi nâng lên 3-wise hoặc test targeted.

</details>

---

## Tóm tắt

Combinatorial explosion trong kiểm thử là hệ quả của **quy tắc nhân**: $$N = \prod v_i$$. Bài toán checkout với 4 trình duyệt và bốn tham số còn lại mỗi tham số 3 giá trị cho $$4 \times 3^4 = 324$$ cấu hình — một flow đã vượt khả năng exhaustive trong sprint thông thường.

**Pairwise (2-wise) testing** yêu cầu mọi **cặp** giá trị từ hai tham số xuất hiện ít nhất một lần — thường đủ bắt bug tương tác hai chiều, với khoảng **15–20** test thay vì 324. Khái niệm toán **covering array** mô tả ma trận test tối thiểu; công cụ **PICT** sinh bộ test từ file model. **Optivem Journal** nhắc explosion không chỉ ở browser matrix mà còn ở chiến lược test class vs e2e — pairwise trên entry point ổn định là hướng giảm tổ hợp mà vẫn kiểm soát được rủi ro.

Pairwise không thay exhaustive khi compliance bắt buộc; bug cần **ba** tham số cùng lúc cần 3-wise hoặc test nhắm combo cụ thể. Đó là trade-off có chủ đích — đếm được, giải thích được cho PM, và bổ sung được khi production chỉ ra cặp hoặc bộ còn thiếu.

Bài sau: **Birthday paradox trong production** — [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/) và khi nào UUID, ID 32-bit hay 64-bit **va chạm** lúc 2 giờ sáng, dù “không gian” ID trông vô cùng lớn.