---
layout: post
title: "Biểu thức Chính quy"
categories: chapter18
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Định nghĩa đệ quy biểu thức chính quy (regex), ngôn ngữ L(r) sinh bởi ba toán tử cơ bản và các ví dụ minh họa."
---

<div class="textbook-epigraph" markdown="1">

"Regular expressions are the algebra of finite automata."

<span class="epigraph-attribution">— Kleene</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** biểu thức chính quy (*regular expression*) và ngôn ngữ tương ứng $$L(r)$$.
- **Chuyển đổi** qua lại giữa mô tả ngôn ngữ tự nhiên và biểu thức chính quy đơn giản.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Biểu thức chính quy trên bảng chữ cái $$\Sigma$$ được xây dựng đệ quy từ:

- **Các biểu thức cơ sở:** $$\emptyset$$, $$\varepsilon$$ và từng ký hiệu $$a\in\Sigma$$.
- **Ba toán tử:** $$r+s$$ (hợp), $$rs$$ (nối chuỗi) và $$r^*$$ (bao đóng Kleene / lặp không hoặc nhiều lần).

Ngôn ngữ $$L(r)$$ biểu diễn bởi biểu thức $$r$$ được xác định tương ứng:

$$L(\emptyset)=\emptyset,\quad L(\varepsilon)=\{\varepsilon\},\quad L(a)=\{a\}.$$

$$L(r+s)=L(r)\cup L(s),\quad L(rs)=L(r)L(s),\quad L(r^*)=\bigcup_{k\ge 0}L(r)^k.$$

</div>

## Ví dụ

Một số biểu thức chính quy quen thuộc trên $$\{0,1\}$$: $$(0+1)^*$$ (mọi chuỗi nhị phân), $$0^*1^*$$ (chuỗi gồm các số 0 đứng trước các số 1), $$(0+1)^*01$$ (chuỗi kết thúc bằng `01`) và $$(01)^*$$ (chuỗi lặp lại cặp `01`).

### Thử nghiệm: dựng ε-NFA Thompson

Ghép từng khối cơ bản cho ký tự, nối tiếp, hợp và lặp sao, sau đó chạy thử chuỗi đầu vào trên NFA vừa dựng:

<div class="interactive-demo" markdown="1">
<div data-demo="regex-explainer" data-tab="thompson"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Viết biểu thức chính quy cho ngôn ngữ các chuỗi trên $$\{0,1\}$$ có số bit 0 chẵn (gợi ý: bài này phức tạp hơn thoạt nhìn, nên dựng DFA trước).
2. Chứng minh đồng nhất thức $$L(r^*)=L(\varepsilon+rr^*)$$.
3. Phân biệt biểu thức chính quy lý thuyết với biểu thức chính quy thực tế như PCRE (có hỗ trợ tham chiếu ngược *backreference*).

## Tài liệu đọc thêm

Sipser §1.3.

## Tóm tắt

Biểu thức chính quy tạo nên một đại số gọn gàng cho ngôn ngữ chính quy với ba phép toán hợp, nối và bao đóng sao.

**Bài tiếp theo:** Định lý Kleene.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=upu_TeZImN0">Regular Expression</a> — Neso Academy, tiếng Anh. Giới thiệu cú pháp và ý nghĩa của biểu thức chính quy trong lý thuyết ô-tô-mát.
- <a href="https://www.youtube.com/watch?v=paOPoZyjzdg">Regular Expression - Examples</a> — Neso Academy, tiếng Anh. Các ví dụ đọc ngôn ngữ tương ứng của một biểu thức chính quy.
- <a href="https://www.youtube.com/watch?v=RxfXyvfTsgQ">Conversion of Regular Expression to Finite Automata</a> — Neso Academy, tiếng Anh. Chuyển đổi từ biểu thức chính quy sang ô-tô-mát hữu hạn.
