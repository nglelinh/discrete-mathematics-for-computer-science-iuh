---
layout: post
title: "Ghi chú mở rộng: Đếm không gian tìm kiếm trong bộ giải hiện đại (2022–2026)"
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

Ghi chú ứng dụng song ngữ (tiếng Anh, sau đó là tiếng Việt). Bài này **không** thay thế nội dung về quy tắc cộng/nhân, hệ số nhị thức hay bài phép đếm từ cờ bạc đến an ninh mạng.

</div>

## English

The multiplication rule says why brute force dies. A CNF on $$n$$ variables has $$2^n$$ assignments; a straight-line assembly program of $$L$$ instructions from an ISA of size $$A$$ has up to $$A^L$$ candidates. Two 2023–2024 results are interesting *because* those counts stay enormous, yet search still finds structure.

- **SAT Competition 2024.** Kissat 4.0 won the main-track gold medals (SAT, UNSAT, SAT+UNSAT). The solver does not enumerate $$2^n$$; it prunes with CDCL. The counting lesson is why pruning is mandatory: see Biere et al. in *SAT Competition 2024*, Univ. Helsinki Report B-2024-1, pp. 8–10, and the [medal page](https://cca.informatik.uni-freiburg.de/sat24medals/).
- **AlphaDev.** Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618:257–263 (2023), [DOI 10.1038/s41586-023-06004-9](https://doi.org/10.1038/s41586-023-06004-9), treat assembly search as a single-player game and discover shorter `sort3`/`sort4`/`sort5` routines now in LLVM libc++. The combinatorial object is a program, not a password — the same $$a^n$$ growth you used for key spaces.

Pairwise test design (already in Chapter 9) is the dual: you *refuse* to count the full Cartesian product and cover only 2-wise tuples. This optional note only updates the 2023–2024 evidence that counting still decides which searches are thinkable.

**Citations**

1. A. Biere et al., SAT Competition 2024 solver description, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
2. D. J. Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618 (2023). [DOI](https://doi.org/10.1038/s41586-023-06004-9)

**Questions.** (1) Write $$\vert \text{assignments}\vert $$ and $$\vert \text{assembly programs of length } L\vert $$ with the multiplication rule. (2) What quantity does CDCL *avoid enumerating*?

## Tiếng Việt

Quy tắc nhân giải thích vì sao cách tiếp cận vét cạn nhanh chóng trở nên bất khả thi. Một công thức CNF gồm $$n$$ biến có $$2^n$$ phép gán chân trị; một chương trình hợp ngữ (assembly) tuyến tính dài $$L$$ lệnh trên tập lệnh (ISA) kích thước $$A$$ có tối đa $$A^L$$ chương trình ứng viên. Hai kết quả giai đoạn 2023–2024 dưới đây đáng chú ý chính *vì* không gian tìm kiếm vẫn khổng lồ như vậy, nhưng các kỹ thuật tìm kiếm vẫn khai thác được cấu trúc bên trong:

- **SAT Competition 2024.** Bộ giải Kissat 4.0 giành cả ba huy chương vàng ở hạng mục chính (SAT, UNSAT và SAT+UNSAT). Thay vì liệt kê toàn bộ $$2^n$$ phép gán, bộ giải cắt tỉa không gian tìm kiếm bằng thuật toán CDCL. Bài học từ phép đếm rất rõ: cắt nhánh là yêu cầu bắt buộc.
- **AlphaDev** (*Nature* 2023) mô hình hóa việc tìm kiếm chương trình hợp ngữ như một trò chơi một người và phát hiện các đoạn mã sắp xếp `sort3`/`sort4`/`sort5` ngắn hơn, hiện đã được đưa vào thư viện LLVM libc++. Đối tượng tổ hợp ở đây là chương trình thay vì mật khẩu, nhưng vẫn tuân theo tốc độ tăng trưởng $$a^n$$ giống không gian khóa.

Kiểm thử từng cặp (pairwise testing, ở Chương 9) thể hiện hướng tiếp cận đối lập: thay vì duyệt hết tích Descartes, ta chỉ bao phủ các cặp giá trị 2 chiều. Ghi chú này cập nhật bằng chứng từ giai đoạn 2023–2024 cho thấy phép đếm vẫn quyết định những bài toán tìm kiếm nào là khả thi trên thực tế.

**Câu hỏi.** (1) Hãy viết biểu thức cho $$\vert \text{phép gán}\vert $$ và $$\vert \text{chương trình hợp ngữ độ dài } L\vert $$ bằng quy tắc nhân. (2) Thuật toán CDCL *tránh phải liệt kê* đại lượng nào?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=uAdVzz1hKYY">Boolean Satisfiability Problem - Intro to Theoretical Computer Science</a> — Udacity, tiếng Anh. Giới thiệu không gian $$2^n$$ phép gán của bài toán SAT, minh họa trực tiếp quy tắc nhân trong bài.
- <a href="https://www.youtube.com/watch?v=Gnx6EgpW6kY">AlphaDev | Daniel Mankowitz and Andrea Michi</a> — ICARL, tiếng Anh. Nhóm tác giả trình bày cách AlphaDev tìm kiếm chương trình sắp xếp trong không gian lệnh khổng lồ.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giải thích cách CDCL cắt tỉa không gian tìm kiếm thay vì duyệt hết mọi phép gán.
