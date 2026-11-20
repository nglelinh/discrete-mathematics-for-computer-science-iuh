---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 16200
enableTimeBar: true
---

## Chương 9 — Toán rời rạc trong CNTT thực chiến

**Toán Rời Rạc**

Tiết ch09-10 — Tổng hợp 13 bài (`09_00`–`09_12`)

*Slide dài — có thể chia 4–6 buổi (~45 phút/buổi)*

---

## Mục tiêu tổng hợp

- Nắm **hai trục** Chương 9: dữ liệu nhị phân (bit → silicon) và **đếm** ở quy mô production
- Phân biệt **diễn giải** vs **byte thô**; Unicode vs encoding; endianness; two's complement
- Áp dụng Little's Law, combinatorial explosion, birthday paradox, Matt Might, cardinality
- Đọc **case study TaskFlow** — 5 incident trong một buổi sáng login
- Liên hệ tập hợp (SQL/Python) và backtracking (Knight's tour / Hamilton)

**Nguồn:** `contents/chapter09/_posts/21-01-01-09_*.md`

---

## Bản đồ chương — 13 bài

| Order | Bài | Hook chính |
|:---:|:---|:---|
| 0 | Bit & byte | Debugger: `42` → `2A 00 00 00` |
| 1 | Unicode | TaskFlow: `Nguyễn` → mojibake |
| 2 | Endianness | Timestamp nhảy năm **2286** |
| 3 | Y2038 | PLC +1 giây → năm **1901** |
| 4 | Transistor | Ben Eater: `a+b` = cổng logic |
| 5 | Pool | 10k user ≠ 10k connection |
| 6 | Pairwise | 324 cấu hình → ~15 test |
| 7 | Birthday | 2 user, cùng `session_id` INT32 |
| 8 | Matt Might | Trial: bao nhiêu nurse review? |
| 9 | Cardinality | Cloudflare 1M DNS query/s |
| 10 | Case study | TaskFlow 1M DAU, login sập |
| 11 | Set theory | `UNION ALL` → email gửi 2 lần |
| 12 | Knight's tour | LeetCode treo ở $8 \times 8$ |

---

## Trục 1 — Từ bit đến silicon

```
Bit (0/1) → Byte (8 bit) → Word (16/32/64 bit)
    → Encoding (UTF-8) / Endianness
    → Signed integer (two's complement)
    → Transistor → NAND → ALU → CPU
```

**Ý then chốt:** Máy không lưu “chữ” hay “ngày giờ” — chỉ lưu **mẫu bit** + quy ước đọc.

![Bit và byte](https://commons.wikimedia.org/wiki/Special:FilePath/Bits_and_Bytes.svg?width=520)

---

## 09_00 — Bit và byte

**Bit:** $$b \in \{0, 1\}$$ — đơn vị nhỏ nhất.

**Byte:** 8 bit → unsigned $0 \ldots 255$ ($2^{8}$ giá trị).

**Nhị phân:**
$$N = \sum_{i=0}^{k-1} b_i \cdot 2^{i}$$

**Hex:** 1 ký tự hex = 4 bit; `0x2A` = 42 thập phân.

---

## 09_00 — RAM và hai lớp dữ liệu

- **Địa chỉ** = số nhà; mỗi ô = **1 byte** (không phải cả số `1234`)
- Số lớn = nhiều byte **liền kề**; thứ tự byte → endianness

| Lớp | Ví dụ |
|:---|:---|
| Vật lý | bit trong transistor, byte trong RAM |
| Quy ước | `int`, `float`, UTF-8, PNG |

```python
int.from_bytes(bytes.fromhex("2a000000"), "little")  # 42
```

---

## 09_00 — Bảng kiểu & hex dump

| Tên | Bit | Byte | Kiểu C |
|:---|:---:|:---:|:---|
| byte | 8 | 1 | `uint8_t` |
| word | 32 | 4 | `int`, `float` |
| double word | 64 | 8 | `int64_t` |

**$n$ bit unsigned:** $$2^{n}$$ giá trị khác nhau.

Cùng byte `0x41`: ASCII → `A`; `uint8_t` → 65; trong JPEG → header.

---

## 09_01 — Không có “plain text”

**Joel Spolsky (2003):** *There Ain't No Such Thing As Plain Text.*

Ba tầng:
1. **Repertoire** — bộ ký tự
2. **Encoding** — code point → byte
3. **Decoding** — byte → code point (phải cùng quy ước)

**Unicode** = “ký tự là số nào?” (`U+0103` = ă)

**Encoding** = “ghi số đó thành byte nào?”

![UTF-8 scheme](https://commons.wikimedia.org/wiki/Special:FilePath/UTF-8_Encoding_Scheme.png?width=400)

---

## 09_01 — UTF-8 và mojibake

**UTF-8:** 1–4 byte/code point; ASCII-compatible (`A` = `41`).

`Nguyễn` UTF-8: `4E 67 75 79 E1 BB 85 6E`

**Mojibake:** decode UTF-8 bằng Latin-1 → `Nguyá»…n`

```python
b = "Nguyễn".encode("utf-8")
b.decode("latin-1")  # sai
```

**Normalization:** NFC vs NFD — quan trọng cho index DB.

---

## 09_01 — Pipeline TaskFlow (5 lớp)

1. PostgreSQL `UTF8`
2. JDBC `?characterEncoding=UTF-8`
3. Jackson: `String` UTF-16 → JSON UTF-8
4. Browser: `Content-Type; charset=utf-8`
5. Email MIME: `charset=UTF-8`

**Double encoding:** sửa header không cứu DB đã lưu sai.

---

## 09_02 — Endianness

**Cùng số, hai cách xếp byte trong RAM:**

- **Big-endian:** byte cao (MSB) ở địa chỉ thấp → dump `12 34` cho `0x1234`
- **Little-endian:** byte thấp (LSB) trước → dump `34 12`

**Lỗi kinh điển:** đọc `34 12` như big → `0x3412` = 13330 (sai).

![32-bit endian](https://commons.wikimedia.org/wiki/Special:FilePath/32bit-Endianess.svg?width=560)

---

## 09_02 — Code & spec thực tế

```python
import struct
struct.unpack("<I", bytes.fromhex("34 12 00 00"))  # LE → 4660
struct.unpack(">I", data)  # BE
```

| Định dạng | Endian |
|:---|:---|
| PNG, mạng (TCP/IP) | big-endian |
| PC RAM (x86/ARM) | little-endian |
| UTF-8 | không phụ thuộc endian |

**UTF-16 BOM:** `FE FF` (BE) · `FF FE` (LE)

---

## 09_03 — Unix time & Y2038

**Unix time:** số giây từ 1970-01-01 00:00:00 UTC.

**32-bit signed max:** $$2^{31}-1 = 2\,147\,483\,647$$
→ **03:14:07 UTC, 19/01/2038**

**+1 giây:** bit pattern nhảy sang vùng âm (two's complement) → ~**1901**.

| | Y2K | Y2038 |
|:---|:---|:---|
| Nguyên nhân | Năm 2 chữ số | Tràn 32-bit signed |
| Sửa | Thêm chữ số | `int64_t` / thay HW |

---

## 09_03 — Two's complement

$$\text{value} = -b_{w-1} \cdot 2^{w-1} + \sum_{i=0}^{w-2} b_i \cdot 2^{i}$$

**8-bit ví dụ:** max 127 (`01111111`); +1 → −128 (`10000000`).

**ALU:** cùng mạch cộng unsigned; khác **cách đọc** sign bit.

```c
int64_t t = (int64_t)time(NULL);  // mitigation
```

![Binary clock](https://commons.wikimedia.org/wiki/Special:FilePath/Binary_clock.svg?width=420)

---

## 09_03 — Bảng giới hạn 32-bit

| Kiểu | Min | Max | Unix overflow |
|:---|:---|:---|:---|
| `int32_t` signed | $-2^{31}$ | $2^{31}-1$ | **2038** → ~1901 |
| `uint32_t` | $0$ | $2^{32}-1$ | **~2106** → wrap 1970 |

**Tổng pattern:** luôn $2^{32}$ — khác kiểu → khác min/max đọc được.

---

## 09_04 — Transistor → NAND → ALU

**Transistor:** công tắc 2 trạng thái → bit.

**NAND (Sheffer):** $$y = (xz)'$$ — **functional completeness** (chỉ NAND → mọi cổng).

**Half-adder:**
$$\text{Sum} = a \oplus b,\quad \text{Carry} = a \cdot b$$

**Full-adder × 8** → cộng 8-bit → **ALU** → `a + b` trong C.

![Transistor](https://commons.wikimedia.org/wiki/Special:FilePath/Transistor.svg?width=280)

---

## 09_04 — Y2038 trên silicon

`01111111` (127) + 1 → `10000000`

- Unsigned đọc: **128**
- Two's complement: **−128**

**Không có mạch “số âm” riêng** — cộng + ISA đọc sign bit.

Opcode 4-bit → $$2^{4} = 16$$ lệnh máy khả dĩ.

![Logic gates](https://commons.wikimedia.org/wiki/Special:FilePath/Logic_Gates.svg?width=480)

---

## Trục 2 — Đếm ở quy mô production

```
Concurrent users ≠ DB connections  (Little's Law)
Exhaustive test = ∏ v_i            (combinatorial)
Collision risk ∝ n²               (birthday)
E[matches] ≠ P(collision)         (Matt Might)
|distinct values| → aggregate?     (cardinality)
```

**Case study:** TaskFlow — một cửa login, năm incident.

---

## 09_05 — Little's Law & connection pool

**Little's Law (steady state):**
$$L = \lambda \times W$$

- $L$ = connection **busy** trung bình
- $\lambda$ = throughput (query/s)
- $W$ = thời gian query trong hệ (giây)

**Pool:** $$N \geq \lceil L \rceil + \text{buffer}$$

**HikariCP (OLTP):** $$\text{connections} = \text{cores} \times 2 + \text{spindles}$$

---

## 09_05 — Ví dụ Dũng & PgBouncer

Peak: 500 req/s × 2 query → $\lambda = 1000$ query/s

$W = 5$ ms → $L = 1000 \times 0{,}005 = 5$

→ pool **10–15**/pod, **không** 200.

DB 8 core + 1 SSD: $8 \times 2 + 1 = 17$ connection backend.

**PgBouncer:** multiplex nhiều client → ít backend Postgres.

![Client-server](https://commons.wikimedia.org/wiki/Special:FilePath/Client-server-model.svg?width=480)

---

## 09_05 — Ba con số hay nhầm

| Đại lượng | Đếm gì |
|:---|:---|
| DAU | Người khác nhau / ngày |
| Concurrent users | Online cùng lúc |
| $\lambda$ | Query hoàn thành/giây |
| Pool $N$ | Connection sẵn sàng |

**Pool quá lớn** → context switch, lock → DB **chậm hơn**.

---

## 09_06 — Combinatorial explosion

**Quy tắc nhân:**
$$N = \prod_{i=1}^{k} v_i$$

Ví dụ 5 tham số: $4 \times 3^{4} = 324$ cấu hình.

× 10 bước test → 3.240 bước — sprint 2 tuần không đủ.

**Pairwise (2-wise):** cover mọi **cặp** tham số → ~**15–20** test (~95% tiết kiệm).

![Exponential growth](https://commons.wikimedia.org/wiki/Special:FilePath/Exponential.svg?width=480)

---

## 09_06 — Pairwise vs exhaustive

| Chiến lược | Cover | Test (ví dụ) |
|:---|:---|:---:|
| Exhaustive | mọi bộ 5 chiều | 324 |
| Pairwise | mọi cặp 2 chiều | ~15 |

**Cảnh báo:** pairwise **không** cover 3-tuple — bug cần 3 chiều → test targeted.

```bash
pict model.txt > tests.txt
```

---

## 09_07 — Birthday paradox

**Trực giác sai:** “còn nhiều slot trống” ≠ an toàn.

Va chạm do **số cặp** so sánh:
$$\binom{n}{2} = \frac{n(n-1)}{2} \propto n^{2}$$

**Xác suất va chạm (xấp xỉ):**
$$P \approx 1 - e^{-\frac{n(n-1)}{2d}}$$

**Ngưỡng 50%:** $$n_{0.5} \approx 1.177\sqrt{d}$$

![Birthday match](https://commons.wikimedia.org/wiki/Special:FilePath/Birthdaymatch.svg?width=480)

---

## 09_07 — Ngưỡng production

| Không gian $d$ | ~50% tại $n$ |
|:---|:---:|
| 32-bit ($2^{32}$) | ~77.000 |
| 64-bit | ~$5 \times 10^{9}$ |
| UUID v4 ($2^{122}$) | ~$2.7 \times 10^{18}$ |

**Cổ điển:** $d=365$, $n=23$ → $P \approx 51\%$.

**SessionHub:** ~45k session INT32 → $P \approx 21\%$ — không còn “hiếm”.

```python
import math
1 - math.exp(-(n*(n-1))/(2*d))
```

---

## 09_08 — Hai câu hỏi khác nhau (Matt Might)

| Câu hỏi | Đại lượng |
|:---|:---|
| Có ≥1 cặp trùng? | $P(\text{collision})$ |
| Trung bình bao nhiêu lần “người mới trùng”? | $E[\text{matches}]$ |

**Công thức Might:**
$$E[\text{matches}] = n - D + D\left(\frac{D-1}{D}\right)^{n}$$

**Khi $n \ll \sqrt{D}$:** $$E \approx \binom{n}{2}/D$$

![Hash table](https://commons.wikimedia.org/wiki/Special:FilePath/Hash_table_simple_999.svg?width=480)

---

## 09_08 — Ví dụ số Might

| Bối cảnh | $D$ | $n$ | $E$ |
|:---|:---:|:---:|:---:|
| Sinh nhật | 365 | 23 | ~5 |
| Patient matching | 500 | 1000 | ~568 |
| Hash bucket | 1024 | 100 | ~2.7 |
| Hash bucket | 1024 | 500 | ~159 |

**23 người:** $P(\geq1) \approx 50\%$ nhưng $E \approx 5$ lần match — **không nhầm hai số**.

---

## 09_09 — Cardinality analytics

**Cardinality** $|V_C|$ = số giá trị **distinct** trên cột $C$.

**Aggregate reduction:**
$$R' \leq \min\left(R,\; \prod_{i=1}^{k} c_i'\right)$$

| Chiều DNS | $|V|$ | Reduction (1M query/phút) |
|:---|:---:|:---:|
| `response_code` | ~12 | ~83.000× |
| `query_name` | có thể ~1M | 0–60× |

![HyperLogLog](https://commons.wikimedia.org/wiki/Special:FilePath/Hyperloglog.svg?width=420)

---

## 09_09 — HyperLogLog & hai lớp dữ liệu

**HLL:** ước lượng $|V|$ ~1–2% sai số, bộ nhớ cố định (20–100 B/sketch).

**Pattern incident:**
- **Aggregate zone-level** → trend/SLA (rẻ)
- **Sampled raw + `qname`** → root cause (đắt)

Label Prometheus `user_id` → cardinality ≈ DAU → **OOM**.

---

## 09_10 — Case study TaskFlow

**Thứ Hai 7:45** — 1M DAU, confetti + `#incidents` đỏ.

```
Browser ──HTTPS──► LB ──► 6 pod (K8s)
                              └── HikariCP ──► PgBouncer ──► PG 8-core
```

**5 incident** — mỗi incident = một bài Chương 9.

![OSI layers](https://commons.wikimedia.org/wiki/Special:FilePath/OSI_Model_v1.svg?width=420)

---

## 09_10 — Incident 1: Connection pool

**Triệu chứng:** P99 login 8s; `active_connections` = 200 (trần).

**Toán:** peak 3000 req/s × 4 query → $\lambda = 12000$ query/s

$W = 8$ ms → $L = 96$ → pool ~25/pod + PgBouncer 20.

**Bài:** 09_05 — Little's Law.

---

## 09_10 — Incident 2: Pairwise QA

**Triệu chứng:** Safari + iPhone + tiếng Việt + OAuth — chỉ Chrome Windows pass.

**Toán:** $4 \times 3 \times 3 \times 2 \times 2 = 144$ cấu hình × 10 bước.

**Fix:** ~15 pairwise + 5 test targeted Safari/vi/OAuth.

**Bài:** 09_06.

---

## 09_10 — Incident 3 & 4

**Incident 3 — INT32 session collision**
- `DuplicateKeyException`; ~45k session active
- $n_{0.5} \approx 77k$ cho 32-bit
- Fix: **UUID v4**; `expires_at` **BIGINT** ms (tránh Y2038)
- Bài: 09_07, 09_03

**Incident 4 — Email Nhật `????`**
- Thiếu `charset=UTF-8` trên MIME
- Joel: không plain text
- Bài: 09_01

---

## 09_10 — Incident 5: Metric cardinality

**Triệu chứng:** Prometheus OOM; label `user_id` trên metric login.

**Toán:** label cardinality ≈ số user distinct → triệu time series.

**Fix:** label `status`, `method`, `region` — **không** `user_id`/`email`.

**Bài:** 09_09.

---

## 09_10 — Design doc (tóm tắt)

| Hạng mục | Quyết định đếm được |
|:---|:---|
| Pool | $L \approx 96$; 25/pod; PgBouncer 20 |
| QA | 15 pairwise + 5 targeted |
| Session | UUID v4; BIGINT `expires_at` |
| Encoding | UTF-8 mọi lớp pipeline |
| Metrics | Low-cardinality labels only |

**Một triệu DAU** = vài phép nhân bị bỏ qua — không phải “scale tự nhiên”.

---

## 09_11 — Tập hợp trong CSDL

**Russell:** tập “mọi tập không chứa chính nó” → mâu thuẫn → cảnh báo tự tham chiếu.

**SQL = đại số tập:**

| SQL | Tập hợp |
|:---|:---|
| `UNION` | Hợp (dedup) |
| `UNION ALL` | Bag (giữ trùng) |
| `INTERSECT` | Giao |
| `INNER JOIN` | Giao có điều kiện |

![Venn 3 tập](https://commons.wikimedia.org/wiki/Special:FilePath/Venn3.svg?width=420)

---

## 09_11 — Incident email & công thức

**Linh:** `UNION ALL` newsletter + VIP → gửi **2 lần**.

$$|A \cup B| = |A| + |B| - |A \cap B|$$

- `UNION ALL`: $30{,}000 + 22{,}000 = 52{,}000$
- `UNION`: $48{,}000$ (overlap 4.000)

```python
all_reach = newsletter | vip   # union
both = newsletter & vip        # intersection
```

---

## 09_11 — Bloom filter & membership

**Bloom filter:** membership xấp xỉ — **không** false negative; **có** false positive.

$$p \approx \left(1 - e^{-kn/m}\right)^{k}$$

Ứng dụng: cache negative lookup, crawler, Redis trước PostgreSQL.

**Cùng câu hỏi mọi tầng:** phần tử có thuộc tập không?
- SQL `IN`, Python `in`, type check, Bloom, hash table

---

## 09_12 — Knight's Tour

**Bài toán:** quân mã đi qua mọi ô $n \times n$ **đúng một lần**.

- **Open tour** ⟺ đường **Hamilton**
- **Closed tour** ⟺ chu trình **Hamilton**

**Khác Euler:** duyệt **cạnh** (bậc chẵn) vs duyệt **đỉnh** (NP-hard).

![Knight's tour](https://commons.wikimedia.org/wiki/Special:FilePath/Knight%27s_tour.svg?width=360)

---

## 09_12 — Backtracking & Warnsdorf

**Brute force:** cây độ sâu $n^{2}$; $8 \times 8$ → không khả thi laptop.

**Warnsdorf (1823):** chọn ô tiếp theo có **ít láng giềng mã chưa thăm nhất**.

$$W(v) = |\{u : u \text{ láng giềng hợp lệ}, u \text{ chưa thăm}\}|$$

**$8 \times 8$ closed tour (có hướng):** $26\,534\,728\,821\,064$.

Song song QA: không test hết combination — **cấu trúc + cắt nhánh**.

---

## 09_12 — Bảng bàn nhỏ

| $n$ | Closed tour? |
|:---:|:---:|
| 3 | Không |
| 4 | Không (open có) |
| 5+ | Có (ngoại lệ nhỏ) |

**$3 \times 3$:** không tour 9 ô — ô góc bậc 2.

**Liên hệ SAT solver (tiết 43):** cùng backtracking, khác predicate hợp lệ.

---

## Bản đồ công thức — Chương 9

| Chủ đề | Công thức |
|:---|:---|
| Nhị phân | $N = \sum b_i 2^{i}$; $2^{n}$ giá trị |
| Two's complement | $-b_{w-1}2^{w-1} + \sum_{i<w-1} b_i 2^{i}$ |
| Little's Law | $L = \lambda W$ |
| HikariCP | $\text{cores} \times 2 + \text{spindles}$ |
| Combinatorial | $N = \prod v_i$ |
| Birthday $P$ | $1 - e^{-n(n-1)/(2d)}$ |
| Birthday $n_{0.5}$ | $\approx 1.177\sqrt{d}$ |
| Might $E$ | $n - D + D((D-1)/D)^{n}$ |
| Set union | $\|A \cup B\| = \|A\|+\|B\|-\|A \cap B\|$ |

---

## Nhân vật xuyên chương

| Nhân vật | Bối cảnh | Bài |
|:---|:---|:---|
| Hùng | Debugger C | 09_00 |
| Minh | TaskFlow backend | 09_01, 10, 12 |
| Lan | Log binary / SCADA | 09_02–04 |
| Dũng | DevOps fintech | 09_05 |
| Hương | QA checkout | 09_06, 10 |
| Huy | SRE SessionHub | 09_07 |
| Dr. Phương | Trial lâm sàng | 09_08 |
| Khoa | DNS analytics | 09_09 |
| Linh | Data engineer | 09_11 |

**TaskFlow** = thread kết nối toàn chương.

---

## Thực hành 1 — Bit & encoding

1. Chuyển 42 sang nhị phân 8-bit và hex.
2. Hex dump `2A 00 00 00` → `uint32` little-endian.
3. Python: encode `Nguyễn` UTF-8, decode Latin-1 — quan sát mojibake.
4. Vẽ 5 hop pipeline charset TaskFlow; chỉ hop dễ lỗi.

---

## Thực hành 2 — Endian & thời gian

1. LE: ô `1000`=`34`, `1001`=`12` → ghép `0x1234`.
2. `struct.unpack("<I", ...)` vs `">I"`.
3. Unix signed 32-bit max → ngày 2038-01-19 03:14:07 UTC.
4. +1 → pattern âm → năm ~1901; giải thích two's complement.

---

## Thực hành 3 — Đếm hệ thống

1. $\lambda=800$ query/s, $W=6$ ms → tính $L$ và pool gợi ý.
2. 4×3×3×2 tham số → $N$ exhaustive; ước pairwise.
3. INT32 $d=2^{32}$, $n=50{,}000$ → $P(\text{collision})$ xấp xỉ.
4. $D=500$, $n=1000$ patient → $E[\text{matches}]$ (Might).

---

## Thực hành 4 — Case study & tập hợp

1. FlowBoard 2500 login/s, 5 query, 10 ms → $L$; 8 pod — pool hợp lý?
2. `UNION ALL` vs `UNION` — 30k + 22k, overlap 4k → số recipient.
3. Metric label: tại sao `user_id` gây OOM Prometheus?
4. Knight $5 \times 5$: mô tả backtracking + một bước Warnsdorf.

---

## Bài tập ôn tập (1/3)

1. **Bit:** $n=16$ bit unsigned — bao nhiêu giá trị? So với INT16 signed max?

2. **Unicode:** `ế` (`U+1EBF`) — ghi byte UTF-8 (hex).

3. **Endian:** File LE `34 12 00 00` — đọc BE nhầm ra số gì?

4. **Y2038:** Liệt kê min/max `int32` và `uint32`; vì sao signed overflow → 1901?

---

## Bài tập ôn tập (2/3)

5. **Pool:** 16 core, 2 SSD — HikariCP gợi ý? 4 pod × pool 20 vs backend?

6. **Pairwise:** 324 cấu hình, 5 phút/test — exhaustive mất bao lâu? Pairwise 15 test?

7. **Birthday:** $n_{0.5}$ cho UUID v4? Cho INT32?

8. **Might:** $D=365$, $n=23$ — $E$ và $P$ — tại sao khác nhau?

---

## Bài tập ôn tập (3/3)

9. **Cardinality:** 900k log/phút; `response_code` $|V|=12$ vs `qname` unique — reduction?

10. **Set:** Python `newsletter | vip` vs SQL `UNION` — khi nào dùng `UNION ALL`?

11. **Knight:** $4 \times 4$ — open tour có? closed? Giải thích bậc đỉnh góc.

12. **Tổng hợp:** Viết 5 dòng design doc login cho startup 500k DAU (pool, session, encoding, QA, metrics).

---

## Tóm tắt Chương 9

**Tầng dữ liệu:** bit → byte → encoding/endian/signed → transistor → ALU.

**Tầng quy mô:** Little's Law → combinatorial → birthday → Might → cardinality → sets.

**Một câu:** Máy tính **đếm và lưu có giới hạn** — hiểu công thức trước khi scale.

**Case study TaskFlow:** login = cửa nguy hiểm nhất — năm incident, một buổi sáng.

**Đọc thêm:** 13 bài `contents/chapter09/_posts/`

---

## Liên hệ chương khác

| Chương 9 | Liên hệ |
|:---|:---|
| Bit, two's complement | Ch13 Boolean / ALU |
| Combinatorial, birthday | Ch07–08 đếm, chuồng bồ câu |
| Set theory SQL | Ch04 tập hợp, tiết 42 CSDL |
| Knight's tour / Hamilton | Tiết 36–37 đồ thị |
| Big-O backtracking | Tiết 38–39 độ phức tạp |
| RSA, hash | Tiết 40–41 lý thuyết số |

**Tiếp theo:** Chương 10 — quan hệ truy hồi, mô hình tăng trưởng theo thời gian.

---

## Gợi ý chia buổi (4–6 × 45 phút)

| Buổi | Nội dung |
|:---|:---|
| 1 | 09_00–01: bit, Unicode, UTF-8 |
| 2 | 09_02–04: endian, Y2038, transistor |
| 3 | 09_05–06: pool, pairwise |
| 4 | 09_07–09: birthday, Might, cardinality |
| 5 | 09_10–11: TaskFlow, set theory |
| 6 | 09_12 + ôn tập + bài tập |

**Slide chi tiết từng bài:** `tiet-ch09-01-unicode-encoding.md` (mở rộng thêm tương tự).

**Câu hỏi?**
