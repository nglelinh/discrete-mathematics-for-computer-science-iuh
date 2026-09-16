---
layout: post
title: "Optional note: Counting search spaces in modern solvers (2022–2026)"
categories: chapter07
date: 2021-01-01
order: 7
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. SAT 2024 and AlphaDev (Nature 2023) are counting-and-search stories: 2^n assignments and huge assembly programs. Does not replace counting theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite addition/multiplication rules, binomial identities, or the existing cybersecurity counting lesson.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại quy tắc cộng/nhân, hệ số nhị thức, hay bài đếm từ cờ bạc đến an ninh mạng.

</div>

## English

The multiplication rule says why brute force dies. A CNF on $$n$$ variables has $$2^n$$ assignments; a straight-line assembly program of $$L$$ instructions from an ISA of size $$A$$ has up to $$A^L$$ candidates. Two 2023–2024 results are interesting *because* those counts stay enormous, yet search still finds structure.

- **SAT Competition 2024.** Kissat 4.0 won the main-track gold medals (SAT, UNSAT, SAT+UNSAT). The solver does not enumerate $$2^n$$; it prunes with CDCL. The counting lesson is why pruning is mandatory: see Biere et al. in *SAT Competition 2024*, Univ. Helsinki Report B-2024-1, pp. 8–10, and the [medal page](https://cca.informatik.uni-freiburg.de/sat24medals/).
- **AlphaDev.** Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618:257–263 (2023), [DOI 10.1038/s41586-023-06004-9](https://doi.org/10.1038/s41586-023-06004-9), treat assembly search as a single-player game and discover shorter `sort3`/`sort4`/`sort5` routines now in LLVM libc++. The combinatorial object is a program, not a password — the same $$a^n$$ growth you used for key spaces.

Pairwise test design (already in Chapter 9) is the dual: you *refuse* to count the full Cartesian product and cover only 2-wise tuples. This optional note only updates the 2023–2024 evidence that counting still decides which searches are thinkable.

**Citations**

1. A. Biere et al., SAT Competition 2024 solver description, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
2. D. J. Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618 (2023). [DOI](https://doi.org/10.1038/s41586-023-06004-9)

**Questions.** (1) Write $$|\text{assignments}|$$ and $$|\text{assembly programs of length } L|$$ with the multiplication rule. (2) What quantity does CDCL *avoid enumerating*?

## Tiếng Việt

Quy tắc nhân giải thích vì sao vét cạn chết. CNF $$n$$ biến có $$2^n$$ phép gán; chương trình assembly độ dài $$L$$ trên ISA cỡ $$A$$ có tới $$A^L$$ ứng viên. Hai kết quả 2023–2024 đáng đọc *vì* các con số đó vẫn khổng lồ, nhưng tìm kiếm vẫn khai thác cấu trúc.

- **SAT Competition 2024.** Kissat 4.0 thắng ba huy chương vàng track chính. Bộ giải không liệt kê $$2^n$$; nó cắt nhánh bằng CDCL. Bài học đếm: cắt nhánh là bắt buộc.
- **AlphaDev** (*Nature* 2023) coi tìm assembly như trò chơi một người và ra routine `sort3`/`sort4`/`sort5` ngắn hơn, đã vào LLVM libc++. Đối tượng tổ hợp là chương trình — cùng tăng trưởng $$a^n$$ như không gian khóa.

Pairwise testing (Chương 9) là mặt đối: *từ chối* đếm hết tích Descartes, chỉ phủ bộ đôi. Ghi chú này chỉ cập nhật bằng chứng 2023–2024: phép đếm vẫn quyết định tìm kiếm nào còn nghĩ được.

**Câu hỏi.** (1) Viết $$|\text{phép gán}|$$ và $$|\text{chương trình độ dài } L|$$ bằng quy tắc nhân. (2) CDCL *tránh liệt kê* đại lượng nào?
