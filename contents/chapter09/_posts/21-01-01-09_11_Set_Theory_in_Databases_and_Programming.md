---
layout: post
title: "Tập hợp trong CSDL và lập trình: Từ Russell đến Bloom filter"
categories: chapter09
date: 2021-01-01
order: 11
required: false
lang: en
excerpt: "Kết nối lý thuyết tập hợp (Chương 4) với thực hành SQL (UNION, INTERSECT, EXCEPT, JOIN), Python set, Bloom filter, chỉ mục cơ sở dữ liệu và hệ thống kiểu (type system)."
---

Một lỗi gửi email quảng cáo hai lần cho cùng một khách hàng thường bị đổ cho "nhầm câu SQL". Nhưng gốc rễ của nó lại nằm ở sự phân biệt tinh tế của lý thuyết tập hợp: **tập hợp (set)** không chứa phần tử lặp, còn **đa tập (multiset / bag)** thì có. Khi Edgar F. Codd đặt nền móng cho cơ sở dữ liệu quan hệ năm 1970, toàn bộ SQL, bảng băm, hệ thống kiểu dữ liệu và Bloom filter đều lớn lên từ các phép toán tập hợp cơ bản này.

**Mạch bài học:** Từ lý thuyết tập hợp Cantor–Codd $$\longrightarrow$$ khác biệt giữa **Set (`UNION`)** và **Bag (`UNION ALL`)** trong SQL $$\longrightarrow$$ phép hợp–giao–hiệu $$O(1)$$ trên `set` Python & bảng băm $$\longrightarrow$$ tập hợp xấp xỉ **Bloom filter** và kiểu dữ liệu như tập giá trị.

## Bản đồ kiến thức nền: Lý thuyết tập hợp vận hành bên trong phần mềm như thế nào?

- **Đại số quan hệ & Phân biệt Set vs. Bag (Relational Algebra):** Mô hình quan hệ chuẩn coi mỗi bảng là một **tập hợp** các bộ (tuples), nơi các phép chọn ($$\sigma$$), chiếu ($$\pi$$), hợp ($$\cup$$), giao ($$\cap$$), hiệu ($$\setminus$$) loại bỏ trùng lặp. SQL thực tế mặc định dùng **đa tập (bag)** để tiết kiệm chi phí khử trùng lặp, nên lập trình viên phải chủ động phân biệt `UNION` và `UNION ALL`.
- **Cấu trúc dữ liệu kiểm tra phần tử thuộc tập (Membership Data Structures):** Câu hỏi $$x \in S$$ quyết định hiệu năng của hầu hết chương trình: danh sách tốn $$O(n)$$, cây cân bằng tốn $$O(\log n)$$, bảng băm (`set`/`dict`) đạt trung bình $$O(1)$$, còn **Bloom filter** đánh đổi một xác suất dương tính giả nhỏ để nén bộ nhớ xuống vài bit mỗi phần tử.
- **Lý thuyết kiểu như lý thuyết tập hợp (Types as Sets):** Trong TypeScript, Rust hay Python typing, mỗi kiểu dữ liệu ứng với một tập giá trị; kiểu hợp `A | B` là $$A \cup B$$, kiểu giao `A & B` là $$A \cap B$$, còn kiểu `never` tương ứng tập rỗng $$\emptyset$$.

Ở các mục trước, chúng ta đã thấy lực lượng tập hợp (**cardinality**) quyết định khả năng nén dữ liệu và tính ổn định của hệ thống giám sát. Mục này quay lại **lý thuyết tập hợp** (Chương 4) trong môi trường kỹ thuật thực tế — từ PostgreSQL, Redis, Python, TypeScript đến Bloom filter. Mọi tầng đều xoay quanh cùng những câu hỏi nền tảng: phần tử có thuộc tập hay không, và các phép hợp–giao–hiệu hoạt động như thế nào? Một lỗi thực tế rất phổ biến: chiến dịch email gửi **hai lần** cho cùng một khách hàng chỉ vì câu lệnh SQL dùng `UNION ALL` (nối đa tập/bag, giữ bản sao) thay vì `UNION` (hợp tập, loại trùng).

Linh, kỹ sư dữ liệu tại một công ty thương mại điện tử, kiểm tra câu truy vấn do thực tập sinh viết:

```sql
SELECT email FROM newsletter_subscribers
UNION ALL
SELECT email FROM loyalty_vip;
```

CRM chỉ có 48.000 địa chỉ email duy nhất, nhưng SendGrid báo đã gửi tới **61.000** người nhận. Đây không phải lỗi của dịch vụ gửi thư mà là lỗi **phép toán tập hợp**: `UNION ALL` giữ lại **mọi bản sao**, còn `UNION` mới thực hiện phép **hợp** có loại trùng.

Bài này nối kết những bài học trước trong Chương 9 về lại nền tảng lý thuyết tập hợp của Chương 4 — từ công trình của Cantor và nghịch lý Russell đến mô hình quan hệ của Codd, `set` trong Python, Bloom filter và kiểu hợp (union type) trong TypeScript.

Nhiều người học Chương 4 thường cảm thấy lý thuyết tập hợp thiên về trừu tượng, nhưng trên thực tế nó nằm ngay dưới các thao tác quen thuộc như truy vấn SQL, kiểm tra `if user_id in cache` hay khai báo kiểu dữ liệu. Để xử lý sự cố gửi trùng email, Linh chỉ cần áp dụng đúng ngữ nghĩa phép hợp tập của `UNION`.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg"
       alt="Biểu đồ Venn ba tập — hợp, giao, hiệu trên tập hợp"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.11a: Lý thuyết tập hợp hiện diện trực tiếp trong bảng SQL, kiểu `set` của Python và Bloom filter — tất cả đều xoay quanh câu hỏi phần tử có thuộc tập hay không (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Venn3.svg">Wikimedia Commons</a>, public domain).</figcaption>
</p>
</figure>

---

## Từ Cantor, Russell đến mô hình quan hệ của Codd

Georg Cantor đã xây dựng lý thuyết tập hợp thành ngôn ngữ chung cho số học, hàm số và quan hệ — nền tảng mà khoa học máy tính trực tiếp kế thừa. Khi viết `SELECT DISTINCT`, ta yêu cầu hệ quản trị loại bỏ phần tử trùng trong một tập bộ (tuple); khi khai báo `type ID = string | number`, ta định nghĩa hợp của hai tập giá trị hợp lệ.

![Georg Cantor](/discrete-mathematics-for-computer-science-iuh/img/course/Georg_Cantor_1894.jpg)

<p class="textbook-figure-caption" data-figure="9.18">Georg Cantor (1845–1918) — người đặt nền móng cho lý thuyết tập hợp hiện đại.</p>

Không lâu sau đó, Bertrand Russell chỉ ra một nghịch lý nổi tiếng: xét tập hợp chứa tất cả các tập hợp **không** chứa chính nó. Tập này có chứa chính nó không? Nếu có thì trái định nghĩa; nếu không thì theo định nghĩa nó lại phải chứa chính nó. Mâu thuẫn này buộc toán học phải xây dựng lý thuyết tập hợp chặt chẽ hơn.

![Bertrand Russell](/discrete-mathematics-for-computer-science-iuh/img/course/Bertrand_Russell_photo.jpg)

<p class="textbook-figure-caption" data-figure="9.19">Bertrand Russell — người chỉ ra nguy cơ mâu thuẫn từ tự tham chiếu không kiểm soát trong định nghĩa tập hợp.</p>

Bài học từ nghịch lý Russell cũng có ý nghĩa trực tiếp trong kỹ thuật dữ liệu: một lược đồ cho phép tự tham chiếu tùy tiện dễ dẫn đến mâu thuẫn hoặc vòng lặp vô hạn (như JSON tham chiếu vòng hay khóa ngoại vòng `A → B → A`). Năm 1970, E. F. Codd đặt nền móng cho **mô hình cơ sở dữ liệu quan hệ** dựa trên tập hợp có cấu trúc chặt chẽ: mỗi bảng là tập các bộ (tuple) xác định theo lược đồ, và mỗi cột chỉ nhận giá trị thuộc một miền (domain) cụ thể.

---

## SQL hằng ngày — `SELECT` là phép chọn tập con

![Cơ sở dữ liệu quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="9.20">Mỗi bảng là tập hợp các bộ (tuple); truy vấn là phép chọn lọc và biến đổi tập hợp.</p>

Trong mô hình quan hệ, một bảng tương ứng với tập các tuple, còn mệnh đề `WHERE` thực hiện phép **chọn** (**selection**) để lấy tập con thỏa mãn vị từ:

```sql
SELECT *
FROM Employees
WHERE department = 'IT';
```

Về mặt đại số quan hệ, kết quả là một tập hợp (hoặc đa tập/bag trong SQL thực tế khi không dùng `DISTINCT` và cho phép dòng trùng). Linh sửa câu truy vấn chiến dịch email thành:

```sql
SELECT email FROM newsletter_subscribers
UNION          -- không phải UNION ALL
SELECT email FROM loyalty_vip;
```

Ba phép toán tập hợp quen thuộc từ Chương 4 ánh xạ trực tiếp sang SQL: `UNION` là phép **hợp** (tự động loại trùng), `INTERSECT` là phép **giao**, và `EXCEPT` là phép **hiệu** (lấy phần tử thuộc tập bên trái nhưng không thuộc tập bên phải).

Ví dụ tìm sinh viên học cả hai môn DM và DB nhưng không học môn AI:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

Bộ tối ưu truy vấn (query optimizer) của PostgreSQL thường biến đổi các truy vấn lồng nhau dựa trên các đẳng thức tương đương của đại số tập hợp; hiểu rõ ngữ nghĩa tập hợp giúp lập trình viên đọc kế hoạch thực thi (`EXPLAIN`) chính xác hơn.

Trong sự cố gửi trùng email, lỗi phát sinh do `UNION ALL` giữ lại toàn bộ bản sao từ hai nhánh; chỉ cần đổi sang `UNION` là dữ liệu được loại trùng đúng bản chất phép hợp.

### `JOIN` — tích Descartes có điều kiện lọc

Mỗi bảng là một tập bộ, và phép `JOIN` kết hợp các bộ từ hai bảng dựa trên điều kiện khớp khóa.

![Phép JOIN trong SQL](/discrete-mathematics-for-computer-science-iuh/img/course/Square_join.png)

<p class="textbook-figure-caption" data-figure="9.21">JOIN — ghép các bộ từ hai bảng theo điều kiện khóa tương ứng.</p>

```sql
SELECT s.name, c.title
FROM Students s
JOIN Enrollments e ON s.id = e.student_id
JOIN Courses c ON e.course_id = c.id;
```

Về bản chất toán học, câu truy vấn trên tương đương với việc lấy **tích Descartes** `Students × Enrollments × Courses` rồi **lọc** các bộ thỏa `s.id = e.student_id` và `e.course_id = c.id`. Nếu sự cố email là lỗi phép hợp (`UNION ALL`), thì sự cố truy vấn chậm mà Linh gặp tuần trước lại là lỗi tích Descartes: quên mệnh đề `ON` trong `JOIN` khiến kết quả trung gian phình lên hàng triệu dòng trước khi `WHERE` lọc lại.

<div class="content-box warning-box textbook-block" markdown="1">
`INNER JOIN` giữ phần giao khớp khóa giữa hai bảng, còn `LEFT JOIN` giữ toàn bộ bản ghi bên trái kể cả khi không khớp bên phải. Nhầm giữa hai phép này dẫn đến mất dòng hoặc nhân bản dòng — không phải lỗi cú pháp mà là lỗi ngữ nghĩa tập hợp.
</div>

---

## Kiểu `set` trong Python — hợp, giao, hiệu trong ETL

Trong tác vụ ETL chạy hằng đêm, Linh dùng `set` để loại trùng `user_id` trước khi đồng bộ sang kho dữ liệu:

```python
newsletter = {"u1", "u2", "u3"}
vip = {"u2", "u4"}

all_reach = newsletter | vip      # union
both = newsletter & vip           # intersection
only_newsletter = newsletter - vip  # difference

if "u2" in vip:
    ...
```

Các toán tử `|`, `&`, `-` và `in` tương ứng trực tiếp với hợp, giao, hiệu và kiểm tra thuộc tập (membership) của Chương 4. Với kiểu `dict`, kiểm tra `if user_id in cache` cũng chính là bài toán kiểm tra thuộc tập trên tập khóa, được thực hiện nhanh nhờ bảng băm.

Dùng `set` trong RAM nhanh hơn `SELECT DISTINCT` trên bảng trung gian khi dữ liệu vừa phải. Tuy nhiên, khi số lượng `user_id` tăng lên hàng chục triệu và vượt quá dung lượng RAM, cần chuyển sang dùng `UNION` trong kho dữ liệu hoặc cấu trúc xấp xỉ như Bloom filter.

---

## Bloom filter — tập hợp xấp xỉ khi cần tiết kiệm bộ nhớ

Tầng Redis đặt trước PostgreSQL trong hệ thống của Linh dùng **Bloom filter** để trả lời nhanh câu hỏi: “`user_id` này đã từng đặt hàng chưa?” Câu hỏi này lặp lại hàng triệu lần mỗi đêm, nên nếu truy vấn thẳng bảng `Orders` sẽ tiêu tốn nhiều I/O và chi phí cơ sở dữ liệu.

Bloom filter không lưu trực tiếp từng phần tử mà lưu dấu vết bit thông qua $$k$$ hàm băm độc lập vào một mảng $$m$$ bit. Nhờ vậy, thao tác kiểm tra thuộc tập rất nhanh và tốn rất ít RAM. Sự đánh đổi có chủ đích ở đây là: có thể xảy ra **dương tính giả** (**false positive** — bộ lọc báo “có thể đã mua”, dẫn đến một lần truy vấn DB kiểm tra lại), nhưng **không bao giờ xảy ra âm tính giả** (**false negative** — nếu bộ lọc báo “chưa có”, phần tử chắc chắn chưa từng được thêm vào).

![Bloom filter](/discrete-mathematics-for-computer-science-iuh/img/course/Bloom_filter.svg)

<p class="textbook-figure-caption" data-figure="9.22">Bloom filter — cấu trúc kiểm tra thuộc tập xác suất, chấp nhận dương tính giả để tiết kiệm đáng kể bộ nhớ.</p>

Liên hệ với bài `09_07`–`09_09`: Bloom filter dựa trên cùng nền tảng hàm băm và xác suất va chạm, tương đồng về triết lý với HyperLogLog (chấp nhận sai số có kiểm soát để đổi lấy bộ nhớ nhỏ). Bloom filter được dùng rộng rãi cho bộ đệm tránh truy vấn rỗng (negative cache), cơ sở dữ liệu phân tán, trình thu thập web (kiểm tra URL đã duyệt chưa) và các công cụ lưu trữ (storage engine).

---

## Bảng băm và chỉ mục — tổ chức tập hợp để tra cứu nhanh

Bảng băm (hash table) quản lý một tập khóa bằng cách ánh xạ khóa vào các bucket và xử lý va chạm khi nhiều khóa rơi vào cùng một bucket; đây là nền tảng của `dict`, `set` và bộ nhớ đệm trong RAM.

![Hash table](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="9.23">Bảng băm — hỗ trợ kiểm tra thuộc tập với thời gian trung bình $$O(1)$$.</p>

Trong PostgreSQL, đánh **chỉ mục (index)** trên cột `customer_id` giúp câu truy vấn:

```sql
SELECT * FROM Orders WHERE customer_id = 42;
```

trích xuất nhanh **tập con nhỏ** thay vì phải quét toàn bộ bảng `Orders`. Dù chỉ mục là cấu trúc dữ liệu (như B-tree) chứ không phải tập hợp thuần túy, trực giác tập hợp vẫn giữ nguyên: cả bảng là tập vũ trụ, mệnh đề `WHERE` định nghĩa tập con cần lấy, và chỉ mục giúp tránh phải duyệt toàn bộ tập vũ trụ.

---

## Hệ thống kiểu (type system) — mỗi kiểu dữ liệu là một tập giá trị

Trong TypeScript:

```ts
type ID = string | number;
```

Biểu thức `string | number` chính là **hợp** của hai tập giá trị hợp lệ. Tương tự, `boolean` là tập $$\{\text{true}, \text{false}\}$$, còn `Option<T>` trong Rust hay `Maybe` trong Haskell tương ứng với $$\{\text{None}\} \cup T$$ (bổ sung trạng thái không có giá trị vào miền kiểu).

![Union of sets](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="9.24">Union type — phép hợp các tập giá trị trong hệ thống kiểu.</p>

Bộ kiểm tra kiểu (type checker) về bản chất trả lời câu hỏi: giá trị truyền vào có **thuộc** tập giá trị mà kiểu cho phép không? Với hàm `function process(id: string | number)`, trình biên dịch sẽ báo lỗi ngay nếu gọi `process(true)` vì `true` không thuộc hợp `string ∪ number`.

Kiểu hợp phân biệt (discriminated union) như `type Result = { ok: true, data: T } | { ok: false, error: string }` còn biểu diễn một **phân hoạch tập hợp** (set partition từ Chương 4): hai nhánh rời nhau hoàn toàn và hợp của chúng phủ kín toàn bộ không gian kết quả.

---

## Kết thúc tình huống

Linh đổi `UNION ALL` sang `UNION` và chạy lại chiến dịch — tổng số người nhận còn 48.012, khớp với dữ liệu CRM. Ghi chú sau sự cố tóm gọn bài học: *“SQL vận hành trên đại số tập hợp, không phải thao tác nối danh sách.”*

Nếu case study TaskFlow (`09_10`) tập hợp các lỗi đếm ở tầng hạ tầng và giám sát, thì bài này hoàn thiện bức tranh bằng lớp **lý thuyết tập hợp** bên dưới SQL, bộ đệm và hệ thống kiểu: `UNION` là hợp, `JOIN` là tích Descartes có lọc, Bloom filter là kiểm tra thuộc tập xấp xỉ, và union type là hợp các miền giá trị.

**Đọc thêm**: [PostgreSQL — UNION, INTERSECT, EXCEPT](https://www.postgresql.org/docs/current/queries-union.html) · [Use The Index, Luke — Anatomy of an Index](https://use-the-index-luke.com/sql/anatomy) · [Wikipedia — Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)

---

## Ví dụ tính tay cầm tay chỉ việc: So sánh `UNION` vs. `UNION ALL` và tính tay Bloom Filter

**Phần A — Hai tập khách hàng trong ETL:**
Giả sử tập khách hàng mở app hôm nay là $$A = \{101, 102, 103\}$$ và tập khách hàng có đơn hàng là $$B = \{102, 103, 104\}$$.
- `A UNION B` (hợp tập $$A \cup B$$): $$\{101, 102, 103, 104\}$$ — lực lượng **4** (khách 102, 103 chỉ nhận **1** email).
- `A UNION ALL B` (hợp đa tập $$A \uplus B$$): $$\{101, 102, 102, 103, 103, 104\}$$ — lực lượng **6** (khách 102, 103 bị spam **2** lần!).
- `A EXCEPT B` (hiệu tập $$A \setminus B$$): $$\{101\}$$ — khách mở app nhưng chưa mua hàng.

**Phần B — Chạy tay Bloom Filter nhỏ có $$m = 8$$ bit (đánh số 0..7) và $$k = 2$$ hàm băm:**
Ban đầu mảng bit là `0 0 0 0 0 0 0 0`.
1. **Chèn `"an"`** với $$h_1(\text{"an"}) = 1, h_2(\text{"an"}) = 5$$ $$\Rightarrow$$ bật bit 1 và 5: `0 1 0 0 0 1 0 0`.
2. **Chèn `"binh"`** với $$h_1(\text{"binh"}) = 3, h_2(\text{"binh"}) = 5$$ $$\Rightarrow$$ bật bit 3 và 5: `0 1 0 1 0 1 0 0`.
3. **Truy vấn `"chi"`** có $$h_1(\text{"chi"}) = 1, h_2(\text{"chi"}) = 6$$: bit 1 là `1`, nhưng bit 6 là `0` $$\Rightarrow$$ **chắc chắn 100% `"chi"` KHÔNG thuộc tập** (zero false negative).
4. **Truy vấn `"dung"`** có $$h_1(\text{"dung"}) = 1, h_2(\text{"dung"}) = 3$$: cả bit 1 lẫn bit 3 đều đang là `1` (do `"an"` và `"binh"` vô tình bật sẵn) $$\Rightarrow$$ bộ lọc báo "có thể thuộc tập" dù `"dung"` chưa từng được chèn (**false positive**!).

### Khung giải thích: Một lý thuyết tập hợp — bốn tầng trừu tượng của phần mềm (nên đọc chậm)

1. **Bước 1 — Ý nghĩa nghiệp vụ quyết định Set hay Bag:** Trước khi viết SQL hay ETL, luôn hỏi: bản sao có mang nghĩa không? Đếm tổng doanh thu cần đa tập (`UNION ALL`), còn gửi thông báo cho người dùng duy nhất bắt buộc phải là tập hợp (`UNION` / `DISTINCT`).
2. **Bước 2 — Chi phí của phép toán $$x \in S$$:** Khử trùng lặp không miễn phí — SQL `UNION` phải sắp xếp hoặc băm toàn bộ tập kết quả tốn $$O(n \log n)$$ hoặc $$O(n)$$ RAM.
3. **Bước 3 — Khi RAM là giới hạn cứng, chấp nhận sai số một chiều:** Bloom filter không bao giờ bỏ sót phần tử thật (no false negative), nên nó đóng vai "người gác cổng" siêu rẻ trước ổ đĩa hoặc CSDL để loại bỏ nhanh phần lớn truy vấn không tồn tại.
4. **Bước 4 — Hệ thống kiểu bảo vệ tập giá trị từ lúc biên dịch:** Khi khai báo `type Status = "idle" | "loading" | "done"`, trình biên dịch đang kiểm tra quan hệ tập con $$x \in S$$ ngay trước khi chương trình chạy.

$$\text{Tập hợp } (A \cup B,\, x \in S) \;\Longrightarrow\; \text{SQL (Set/Bag)} \;+\; \text{Hash Set } O(1) \;+\; \text{Bloom Filter} \;+\; \text{Type System.}$$

## Bài tập thực hành

### Bài tập 1

Bảng `newsletter_subscribers` có 30.000 email phân biệt, bảng `loyalty_vip` có 22.000 email phân biệt, và phần giao giữa hai tập có **4.000** email trùng. Hỏi `UNION ALL` và `UNION` mỗi phép trả về bao nhiêu dòng? Liên hệ ngắn gọn với con số 61.000 trong sự cố của Linh.

<details>
<summary>Đáp án</summary>

`UNION ALL` giữ toàn bộ bản sao:

<div class="textbook-equation" markdown="1">
$$30{,}000 + 22{,}000 = 52{,}000 \text{ dòng}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

`UNION` thực hiện phép hợp tập (loại trùng):

<div class="textbook-equation" markdown="1">
$$30{,}000 + 22{,}000 - 4{,}000 = 48{,}000 \text{ email phân biệt}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Chênh lệch là:

<div class="textbook-equation" markdown="1">
$$52{,}000 - 48{,}000 = 4{,}000$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

— đúng bằng số phần tử thuộc giao hai tập bị đếm hai lần. Con số 61.000 người nhận so với 48.000 email duy nhất trong sự cố của Linh cho thấy dữ liệu thực tế còn có độ trùng lặp lớn hơn (từ nhiều nguồn hoặc bảng trung gian), nhưng cơ chế hoàn toàn giống nhau: đa tập (bag) phình to hơn tập hợp (set) do không loại trùng.

</details>

### Bài tập 2

Cho ba tập sinh viên (theo `student_id`):

- $$A$$: đăng ký môn DM — $$\vert A\vert = 120$$
- $$B$$: đăng ký môn DB — $$\vert B\vert = 95$$
- $$C$$: đăng ký môn AI — $$\vert C\vert = 40$$
- $$\vert A \cap B\vert = 50$$, $$\vert A \cap C\vert = 10$$, $$\vert B \cap C\vert = 8$$, $$\vert A \cap B \cap C\vert = 5$$

Tính $$\vert (A \cap B) \setminus C\vert $$ (số sinh viên học cả DM và DB nhưng không học AI) và viết câu lệnh SQL tương đương dùng `INTERSECT` và `EXCEPT`.

<details>
<summary>Đáp án</summary>

Số sinh viên học cả DM và DB là $$\vert A \cap B\vert = 50$$. Trong nhóm này có $$\vert A \cap B \cap C\vert = 5$$ người cũng học AI, nên:

<div class="textbook-equation" markdown="1">
$$\vert (A \cap B) \setminus C\vert = 50 - 5 = 45$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Câu lệnh SQL tương đương:

```sql
(SELECT student_id FROM enrollments WHERE course = 'DM')
INTERSECT
(SELECT student_id FROM enrollments WHERE course = 'DB')
EXCEPT
(SELECT student_id FROM enrollments WHERE course = 'AI');
```

Trong đó `INTERSECT` ứng với phép giao và `EXCEPT` ứng với phép hiệu $$(A \cap B) \setminus C$$.

</details>

### Bài tập 3

Một Bloom filter có $$m = 10{,}000$$ bit và $$k = 3$$ hàm băm. Ước lượng tỷ lệ dương tính giả (false positive rate) khi đã chèn $$n = 1{,}000$$ phần tử bằng công thức xấp xỉ $$p \approx (1 - e^{-kn/m})^k$$. Nếu chỉ chấp nhận tối đa 1% dương tính giả khi $$n$$ tăng lên 5.000, nên tăng $$m$$, tăng $$k$$ hay bỏ bộ lọc để truy vấn DB trực tiếp?

<details>
<summary>Đáp án</summary>

Với $$n = 1{,}000$$:

<div class="textbook-equation" markdown="1">
$$\frac{kn}{m} = \frac{3 \times 1{,}000}{10{,}000} = 0{,}3$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$p \approx (1 - e^{-0.3})^3 \approx (1 - 0{,}741)^3 \approx 0{,}0174$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

— tức khoảng **1,7%** dương tính giả.

Khi $$n = 5{,}000$$, tỷ số $$\frac{kn}{m} = 1{,}5$$ khiến $$p \approx (1 - e^{-1.5})^3 \approx 46{,}9\%$$, quá cao so với mức 1%. Để giữ tỷ lệ dương tính giả quanh 1%:

- **Tăng $$m$$** (mở rộng số bit) là giải pháp chuẩn. Với số hàm băm tối ưu $$k = \frac{m}{n}\ln 2$$, kích thước mảng bit cần thiết được ước lượng theo công thức $$m \approx -\frac{n \ln p}{(\ln 2)^2}$$ (hoặc với $$k$$ cố định là $$m \approx -\frac{kn}{\ln(1 - p^{1/k})}$$).
- **Tăng $$k$$** đơn thuần không giải quyết được khi mảng bit đã quá chật, vì quá nhiều hàm băm sẽ làm đầy mảng bit nhanh hơn và tăng cả tỷ lệ dương tính giả lẫn chi phí tính toán.
- **Bỏ bộ lọc để truy vấn DB mọi lần** vẫn đảm bảo tính đúng đắn nhưng làm tăng mạnh chi phí I/O và độ trễ, không phù hợp khi mở rộng.

Lưu ý rằng Bloom filter không bao giờ tạo âm tính giả cho phần tử đã chèn; khi tỷ lệ dương tính giả tăng quá cao, hệ thống không sai kết quả nhưng mất dần lợi ích giảm tải DB.

</details>

### Bài tập 4

Xét đoạn mã TypeScript:

```ts
type PaymentId = string;
type LegacyId = number;
type OrderRef = PaymentId | LegacyId;

function charge(ref: OrderRef): void { ... }
```

và hai tập hợp trong Python:

```python
newsletter = {"u1", "u2"}
vip = {"u2", "u3"}
```

(a) Trong hai lời gọi `charge(42)` và `charge("pay_abc")`, lời gọi nào hợp lệ? (b) `newsletter | vip` và `newsletter & vip` trả về tập nào? (c) Điểm chung giữa SQL `IN`, Python `in` và kiểm tra kiểu trong TypeScript là gì?

<details>
<summary>Đáp án</summary>

(a) Vì `OrderRef = string ∪ number`, cả `charge(42)` ($$42 \in \text{number}$$) lẫn `charge("pay_abc")` ($$\text{"pay\_abc"} \in \text{string}$$) đều **hợp lệ**. Ngược lại, `charge(true)` sẽ bị từ chối vì `boolean` không thuộc hợp này.

(b) `newsletter | vip` = $$\{\text{u1}, \text{u2}, \text{u3}\}$$ (hợp); `newsletter & vip` = $$\{\text{u2}\}$$ (giao).

(c) Cả ba đều thực hiện phép **kiểm tra thuộc tập (membership)**: SQL `WHERE id IN (...)` kiểm tra phần tử có thuộc tập kết quả truy vấn con hay không; Python `"u2" in vip` kiểm tra lúc chạy (runtime); còn TypeScript kiểm tra tĩnh lúc biên dịch (compile time) xem giá trị có thuộc tập giá trị hợp lệ của kiểu hay không.

</details>

---

## Xem thêm / Video gợi ý

- [Set Theory — Cardinality and Infinity](https://www.youtube.com/watch?v=5jZ5n8k0p0Q) — Numberphile (Hilbert's Hotel)
- [Introduction to Sets](https://www.youtube.com/watch?v=4l7L9v0p0Q) — Khan Academy (Basics + notation)

## Tóm tắt

Lý thuyết tập hợp từ Cantor và Russell hiện diện trực tiếp dưới tầng cơ sở dữ liệu, bộ đệm và hệ thống kiểu: **Cantor** định hình ngôn ngữ phần tử thuộc tập, **Russell** cảnh báo rủi ro tự tham chiếu không kiểm soát (tương ứng JSON vòng hay khóa ngoại vòng), và **Codd** xây dựng CSDL quan hệ trên tập bộ có cấu trúc.

Trong SQL, `WHERE` chọn tập con; `UNION` là phép hợp có loại trùng còn `UNION ALL` giữ bản sao; `INTERSECT` và `EXCEPT` là phép giao và hiệu; `JOIN` là tích Descartes có điều kiện lọc khóa. Trong Python, `set` cung cấp trực tiếp `|`, `&`, `-`, `in`. **Bloom filter** cung cấp phép kiểm tra thuộc tập xấp xỉ tiết kiệm RAM (không có âm tính giả, chấp nhận dương tính giả có kiểm soát). **Bảng băm** và **chỉ mục** tổ chức tập để tối ưu tra cứu, còn **union type** trong TypeScript biến kiểm tra kiểu thành phép kiểm tra thuộc tập ngay ở thời điểm biên dịch.

Từ nền tảng tập hợp và đếm của Chương 9, **Chương 10: Quan hệ truy hồi** sẽ mở rộng sang mô hình hóa sự tăng trưởng theo thời gian.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=tyDKR4FG3Yw">INTRODUCTION to SET THEORY - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu nền tảng lý thuyết tập hợp đứng sau `SELECT`, `set` trong Python và hệ thống kiểu.
- <a href="https://www.youtube.com/watch?v=4TlCToZZ5gA">SET OPERATIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Trình bày các phép hợp, giao, hiệu tương ứng trực tiếp với các thao tác ETL và SQL trong bài.
- <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Giải thích Bloom filter như cấu trúc tập xấp xỉ tiết kiệm bộ nhớ khi kiểm tra thuộc tập.
