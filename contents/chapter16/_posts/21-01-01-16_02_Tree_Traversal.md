---
layout: post
title: "Duyệt Cây"
categories: chapter16
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Các thứ tự duyệt preorder, inorder, postorder trên cây nhị phân; duyệt theo tầng level-order (BFS); độ phức tạp O(n) và ứng dụng trong tuần tự hóa, BST, giải phóng cây."
---

<div class="textbook-epigraph" markdown="1">

"The order in which we visit the nodes is not cosmetic — it is the algorithm."

<span class="epigraph-attribution">— Tinh thần duyệt cây</span>

</div>

**Duyệt cây** là thao tác thăm mọi đỉnh của cây **đúng một lần** theo một quy tắc xác định. Thứ tự duyệt quyết định trực tiếp ngữ nghĩa của thuật toán: tuần tự hóa (serialize) cấu trúc cây, in khóa của cây BST theo thứ tự tăng dần, giải phóng bộ nhớ từ dưới lên (bottom-up) hoặc duyệt DOM theo từng tầng. Bài học này so sánh bốn cách duyệt cơ bản: preorder, inorder, postorder và level-order.

![Duyệt cây nhị phân](/discrete-mathematics-for-computer-science-iuh/img/course/Tree_binary_traversal.svg)

<p class="textbook-figure-caption" data-figure="16.3">Cùng một cây nhị phân nhưng ba thứ tự DFS khác nhau ở thời điểm thăm nút gốc so với hai cây con.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** các phép duyệt preorder, inorder và postorder trên cây nhị phân.
- **Thực hiện** phép duyệt theo tầng (level-order / BFS) trên cây có gốc.
- **Giải thích** ứng dụng của từng thứ tự: tuần tự hóa, duyệt tăng dần trên BST và xóa cây.
- **Phân tích** độ phức tạp thời gian $$O(n)$$ và bộ nhớ phụ của các thuật toán duyệt.

**Từ khóa**: preorder, inorder, postorder, level-order, DFS trên cây, BFS trên cây.

</div>

### Video ngắn: Duyệt cây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/tree-traversal.mp4"></video>
</div>

Video dài khoảng 2 phút 13 giây: minh họa cách đi quanh cây để đọc đồng thời preorder $$ABDECF$$, inorder $$DBEACF$$ và postorder $$DEBFCA$$; xét cây biểu thức $$(3+4)\times(5-2)$$ với ba dạng tiền tố, trung tố, hậu tố và cách tính biểu thức hậu tố bằng ngăn xếp; trình bày inorder trên BST cho dãy tăng dần và level-order dùng hàng đợi.

## Ba thứ tự DFS trên cây nhị phân

Xét một nút có cây con trái và cây con phải (có thể rỗng):

| Thứ tự | Quy tắc thăm | Ứng dụng điển hình |
|:---|:---|:---|
| **Preorder** (NLR) | Gốc → Trái → Phải | Sao chép cây, tuần tự hóa dạng tiền tố |
| **Inorder** (LNR) | Trái → Gốc → Phải | In khóa của BST theo thứ tự tăng dần |
| **Postorder** (LRN) | Trái → Phải → Gốc | Giải phóng bộ nhớ cây, tính giá trị biểu thức từ lá lên |

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Xét cây nhị phân:

```text
        A
       / \
      B   C
     / \   \
    D   E   F
```

- Preorder: **A, B, D, E, C, F**
- Inorder: **D, B, E, A, C, F**
- Postorder: **D, E, B, F, C, A**

</div>

```python
def preorder(node):
    if node is None:
        return
    visit(node)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    visit(node)
    inorder(node.right)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    visit(node)
```

Trên cây **tổng quát** (một nút có thể có nhiều hơn hai con), preorder thăm gốc trước rồi lần lượt các con, còn postorder thăm hết các con rồi mới thăm gốc; riêng thứ tự “inorder” chỉ có định nghĩa chuẩn tự nhiên trên cây nhị phân.

## Duyệt theo tầng: Level-order (BFS)

Phép duyệt theo từng **tầng** từ gốc xuống sử dụng cấu trúc **hàng đợi** (*queue*):

```python
from collections import deque

def level_order(root):
    if root is None:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        visit(node)
        for child in getattr(node, "children",
                             [c for c in (node.left, node.right) if c]):
            q.append(child)
```

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Với cùng cây ở Ví dụ 1, thứ tự duyệt level-order là **A, B, C, D, E, F**.

</div>

## Độ phức tạp và liên hệ Chương 12

<div class="textbook-theorem" markdown="1">

**Định lý.** Trên một cây gồm $$n$$ đỉnh, cả bốn thứ tự duyệt (DFS và BFS) đều chạy trong thời gian $$O(n)$$. Bộ nhớ phụ là $$O(h)$$ cho ngăn xếp đệ quy của DFS (với $$h$$ là chiều cao cây) và $$O(w)$$ cho hàng đợi của BFS (với $$w$$ là độ rộng lớn nhất của một tầng).

</div>

Trên **đồ thị** tổng quát, DFS và BFS cần tập `visited` để tránh thăm lặp đỉnh do chu trình. Ngược lại, trên **cây có gốc** (chỉ đi từ cha xuống con), mỗi đỉnh chỉ được truy cập đúng một lần nên không cần đánh dấu chu trình.

| Thuật toán trên đồ thị | Tương ứng trên cây |
|:---|:---|
| DFS “thăm khi vào nút” | Preorder |
| DFS “thăm giữa hai con” (cây nhị phân) | Inorder |
| DFS “thăm khi rời nút” | Postorder |
| BFS | Level-order |

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="tree-traversal-visualizer"></div>
</div>
<script src="{{ '/public/js/tree-traversal-visualizer.js' | relative_url }}"></script>

### Minh họa tương tác

Minh họa duyệt tiền thứ tự, trung thứ tự, hậu thứ tự và duyệt theo mức từng nút một:

<div class="interactive-demo" markdown="1">
<div data-demo="tree-explainer" data-mode="traversal"></div>
</div>
<script src="{{ '/public/js/explainers/tree-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Với cây trong Ví dụ 1, hãy viết lại thứ tự duyệt preorder và postorder.

<details>
<summary>Đáp án</summary>

Preorder: A, B, D, E, C, F.  
Postorder: D, E, B, F, C, A.

</details>

### Bài tập 2

Vì sao duyệt **inorder** trên cây tìm kiếm nhị phân (BST) luôn cho ra dãy khóa tăng dần?

<details>
<summary>Đáp án</summary>

Theo định nghĩa BST, mọi khóa ở cây con trái đều nhỏ hơn khóa ở gốc, và khóa ở gốc nhỏ hơn mọi khóa ở cây con phải. Vì inorder thăm theo thứ tự trái → gốc → phải, nó ghép ba phần đã có thứ tự thành dãy tăng dần toàn cục (có thể chứng minh chặt chẽ bằng quy nạp theo chiều cao cây).

</details>

### Bài tập 3

Vì sao duyệt **postorder** phù hợp cho thao tác `delete(node)` khi cần giải phóng các nút con trước nút cha?

<details>
<summary>Đáp án</summary>

Postorder luôn xử lý hai cây con trước khi thăm nút gốc. Khi thao tác đến `node`, toàn bộ các cây con bên dưới đã được giải phóng, tránh phát sinh tham chiếu treo từ nút cha tới vùng nhớ đã giải phóng.

</details>

### Bài tập 4

Một cây nhị phân đầy đủ (mọi tầng đều kín nút) có chiều cao $$h$$ (gốc ở độ sâu 0) chứa bao nhiêu nút? Nút cuối cùng được thăm trong duyệt level-order nằm ở vị trí nào?

<details>
<summary>Đáp án</summary>

Số nút của cây là $$n = 2^{h+1}-1$$. Vì level-order duyệt lần lượt từng tầng từ trái sang phải, nút được thăm cuối cùng là nút lá ngoài cùng bên phải ở tầng $$h$$.

</details>

## Tóm tắt

1. **Preorder, inorder, postorder** đều thuộc họ DFS, chỉ khác nhau ở thời điểm thực hiện thao tác `visit`.
2. **Level-order** là duyệt theo chiều rộng (BFS) từng tầng từ gốc xuống.
3. Cả bốn cách duyệt đều có độ phức tạp $$O(n)$$; inorder cho dãy tăng trên BST, còn postorder xử lý từ dưới lên.
4. Khi duyệt cây có gốc từ cha xuống con, ta không cần tập `visited` như trên đồ thị có chu trình.

Trong bài tiếp theo, ta sẽ tìm hiểu về **cây khung** và bài toán **cây khung nhỏ nhất (MST)** với thuật toán Kruskal và Prim.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=z_OwSnFY_5s">[Discrete Mathematics] Tree Directories and Traversals</a> — TrevTutor, tiếng Anh. Giới thiệu duyệt cây và mô hình cây thư mục.
- <a href="https://www.youtube.com/watch?v=HZ5YTanv5QE">Breadth-first search in 4 minutes</a> — Michael Sambol, tiếng Anh. Trình bày ngắn gọn về BFS, cơ sở của duyệt theo mức.
- <a href="https://www.youtube.com/watch?v=Urx87-NMm6c">Depth-first search in 4 minutes</a> — Michael Sambol, tiếng Anh. Trình bày ngắn gọn về DFS, cơ sở của các thứ tự duyệt sâu trên cây.
