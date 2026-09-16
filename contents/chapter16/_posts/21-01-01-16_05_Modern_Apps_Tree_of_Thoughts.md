---
layout: post
title: "Optional note: Search trees for language models (2023–2026)"
categories: chapter16
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Tree of Thoughts (NeurIPS 2023) is BFS/DFS on a tree of partial solutions — the same objects as this chapter. Does not replace tree theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite traversals, MST, Huffman, or BST.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại duyệt cây, MST, Huffman hay BST.

</div>

## English

A rooted tree is already the model for backtracking: each node is a prefix of a solution, children are legal extensions, DFS/BFS decide the visit order. Yao, Yu, Zhao, Shafran, Griffiths, Cao, and Narasimhan, “Tree of Thoughts: Deliberate Problem Solving with Large Language Models,” *NeurIPS 2023*, [proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.html), [arXiv:2305.10601](https://arxiv.org/abs/2305.10601), apply that model to LLM inference.

A state is $$s = [x, z_{1\cdots i}]$$ (input plus thoughts so far). The paper specifies four design choices — how to cut a thought step, how to expand, how to score, which search to run — and instantiates BFS (Game of 24) and DFS with pruning (mini crosswords). Headline number: GPT-4 with chain-of-thought solved **4%** of Game of 24; ToT reached **74%**. Code: [princeton-nlp/tree-of-thought-llm](https://github.com/princeton-nlp/tree-of-thought-llm).

Optional link to this chapter: ToT is not a new tree definition. It is tree *search* (the traversals you already wrote) plus a heuristic evaluator. Huffman and BST remain about encoding and ordered keys; ToT is about exploring a state tree when the branching factor is linguistic rather than numeric.

**Citations**

1. S. Yao et al., “Tree of Thoughts: Deliberate Problem Solving with Large Language Models,” NeurIPS 2023. [arXiv](https://arxiv.org/abs/2305.10601)

**Questions.** (1) Draw the ToT state tree for one Game-of-24 instance with branching factor 3 and depth 2. (2) Which traversal matches “expand all thoughts at this depth, keep top $$b$$”?

## Tiếng Việt

Cây có gốc đã là mô hình backtracking: mỗi đỉnh là tiền tố nghiệm, con là bước hợp lệ, DFS/BFS chọn thứ tự. Yao và cộng sự (NeurIPS 2023) áp dụng mô hình đó cho suy luận LLM.

Một trạng thái là $$s = [x, z_{1\cdots i}]$$ (input cộng các thought đến nay). Bài báo nêu bốn lựa chọn thiết kế — cắt bước thought, mở rộng, chấm điểm, thuật toán tìm — và cài BFS (Game of 24) cùng DFS có cắt nhánh (mini crossword). Số headline: GPT-4 + chain-of-thought giải **4%** Game of 24; ToT đạt **74%**.

Liên hệ tùy chọn: ToT không định nghĩa cây mới. Nó là *tìm kiếm trên cây* (các phép duyệt bạn đã viết) cộng bộ đánh giá heuristic. Huffman và BST vẫn về mã hóa và khóa có thứ tự; ToT là duyệt cây trạng thái khi hệ số nhánh là ngôn ngữ chứ không phải số.

**Câu hỏi.** (1) Vẽ cây trạng thái ToT cho một instance Game of 24, nhánh 3, sâu 2. (2) Phép duyệt nào khớp “mở mọi thought ở độ sâu này, giữ top $$b$$”?
