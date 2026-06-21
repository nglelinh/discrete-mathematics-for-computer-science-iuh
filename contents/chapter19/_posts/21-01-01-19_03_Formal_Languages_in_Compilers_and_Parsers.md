---
layout: post
title: "Ngôn ngữ Hình thức trong Trình biên dịch và Parser"
categories: chapter19
date: 2021-01-01
order: 3
required: false
lang: en
---

Mỗi lần bạn chạy `python main.py` hay `tsc app.ts`, trình biên dịch/thông dịch đang trả lời một câu hỏi logic vị từ: **chuỗi ký tự này có thuộc ngôn ngữ cú pháp hợp lệ không?**

```python
# Mini-grammar cho biểu thức số học (BNF)
# Expr  -> Expr '+' Term | Term
# Term  -> Term '*' Factor | Factor
# Factor -> NUMBER | '(' Expr ')'

def parse_expr(tokens, pos=0):
    """Recursive descent — triển khai CFG ở trên."""
    left, pos = parse_term(tokens, pos)
    while pos < len(tokens) and tokens[pos] == "+":
        pos += 1
        right, pos = parse_term(tokens, pos)
        left = ("add", left, right)
    return left, pos
```

Pipeline `source code → tokens → parse tree → AST → bytecode` là chuỗi **nhận diện ngôn ngữ** theo phân cấp Chomsky: regex/DFA cho token, CFG + parser cho cú pháp, rồi semantic analysis.

Từ Chomsky và BNF đến lexer/parser thực tế — bài này nối Chương 19 với cách ngôn ngữ lập trình được định nghĩa và xử lý.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Đọc** grammar BNF/EBNF mô tả cú pháp ngôn ngữ lập trình.
- **Phân biệt** lexical analysis (regular) và syntax analysis (context-free).
- **Giải thích** vai trò của parse tree và AST trong compiler.
- **Viết** lexer đơn giản và parser recursive descent cho grammar nhỏ.
- **Đặt** ngôn ngữ vào phân cấp Chomsky và chọn công cụ phù hợp.

**Từ khóa**: ngôn ngữ hình thức (formal language), CFG, BNF, lexer, parser, AST, phân cấp Chomsky (Chomsky hierarchy), trình biên dịch (compiler).

---

## Phần 1: Ngôn ngữ như tập hợp chuỗi

### 1.1. $$L \subseteq \Sigma^*$$

Cho bảng chữ cái $$\Sigma$$ (ví dụ ASCII), $$\Sigma^*$$ là mọi chuỗi hữu hạn trên $$\Sigma$$. **Ngôn ngữ** $$L$$ là tập con — có thể mô tả bằng grammar, regex, hoặc automaton.

Ví dụ Python hợp lệ là tập **rất lớn** nhưng **cấu trúc**: không phải mọi chuỗi `def` + text đều compile được.

![Noam Chomsky — phân cấp ngôn ngữ hình thức](/discrete-mathematics-for-computer-science-iuh/img/course/Noam_Chomsky.jpg)

*Hình 19.11: Noam Chomsky — phân cấp bốn loại grammar; Type-3 (regex) và Type-2 (CFG) là xương sống compiler.*

### 1.2. Phân cấp Chomsky trong một bảng

| Loại | Grammar | Máy / công cụ | Ví dụ trong compiler |
|---|---|---|---|
| Type-3 Regular | $$A \to aB$$ | DFA/NFA, regex | Lexer, token |
| Type-2 CF | $$A \to \alpha$$ | PDA, parser | Cú pháp biểu thức, câu lệnh |
| Type-1 CS | phụ thuộc ngữ cảnh | LBA | Một số ràng buộc ngữ nghĩa |
| Type-0 | không hạn chế | Turing | Không dùng trực tiếp trong parser |

<div class="content-box insight-box" markdown="1">
**Nhận xét**: Tách lexer (regular) và parser (CFG) không phải ngẫu nhiên — đơn giản hóa thiết kế, tăng tốc, và báo lỗi rõ (token sai vs cú pháp sai).
</div>

![Phân cấp Chomsky — sức mạnh grammar và máy chấp nhận](/discrete-mathematics-for-computer-science-iuh/img/course/Chomsky_hierarchy.svg)

*Hình 19.12: Phân cấp Chomsky — lexer nằm ở tầng regular; parser cú pháp ở context-free.*

---

## Phần 2: Lexer — regular language

### 2.1. Token là ngôn ngữ regular

```python
import re

def lex(source: str):
    specs = [
        ("KW_DEF", r"def"),
        ("IDENT",  r"[a-zA-Z_]\w*"),
        ("NUMBER", r"\d+"),
        ("SKIP",   r"[ \t\n]+"),
    ]
    pattern = "|".join(f"(?P<{n}>{p})" for n, p in specs)
    for m in re.finditer(pattern, source):
        if m.lastgroup != "SKIP":
            yield m.lastgroup, m.group()
```

Mỗi token class là pattern hữu hạn → DFA/NFA. Lỗi lexical: ký tự không khớp bất kỳ pattern nào.

### 2.2. Từ chuỗi ký tự đến dòng token

Input: `def add(x, 1)`

Output token: `(KW_DEF, def)`, `(IDENT, add)`, `(LPAREN, ()`, ...

Parser **không** đọc byte trực tiếp — chỉ đọc dòng token (giống đọc từ vựng thay vì chữ cái).

![Lexical analysis — tách mã nguồn thành token](/discrete-mathematics-for-computer-science-iuh/img/course/lexical_analysis.svg)

*Hình 19.13: Lexical analysis — bước đầu pipeline compiler; mỗi token thuộc lớp regular language.*

---

## Phần 3: Parser — context-free grammar

### 3.1. BNF cho biểu thức

```
<expr>   ::= <expr> "+" <term> | <term>
<term>   ::= <term> "*" <factor> | <factor>
<factor> ::= NUMBER | "(" <expr> ")"
```

Đây là **CFG**: vế trái một nonterminal, vế phải chuỗi terminal/nonterminal. Đệ quy trái (`expr -> expr + term`) mô tả chuỗi cộng trái kết hợp.

### 3.2. Recursive descent

```python
def parse_factor(tokens, pos):
    if tokens[pos][0] == "NUMBER":
        return ("num", int(tokens[pos][1])), pos + 1
    if tokens[pos][1] == "(":
        pos += 1
        node, pos = parse_expr(tokens, pos)
        assert tokens[pos][1] == ")"
        return node, pos + 1
    raise SyntaxError("expected factor")

def parse_term(tokens, pos):
    left, pos = parse_factor(tokens, pos)
    while pos < len(tokens) and tokens[pos][1] == "*":
        pos += 1
        right, pos = parse_factor(tokens, pos)
        left = ("mul", left, right)
    return left, pos
```

Mỗi nonterminal → một hàm `parse_*`. Đây là cách hand-written parser phổ biến cho grammar LL(1) đơn giản.

### 3.3. Parse tree vs AST

- **Parse tree**: giữ mọi node trung gian theo grammar (verbose).
- **AST** (abstract syntax tree): bỏ node thừa (`expr`, dấu ngoặc chỉ cấu trúc), giữ ý nghĩa.

`2 + 3 * 4` → AST `add(2, mul(3, 4))` nhờ ưu tiên `*` cao hơn `+`.

![Cây cú pháp trừu tượng (AST)](/discrete-mathematics-for-computer-science-iuh/img/course/Abstract_syntax_tree_for_Euclidean_algorithm.svg)

*Hình 19.14: AST — biểu diễn cấu trúc chương trình sau parser; input cho type checker và code generator.*

![Parse tree — mọi bước suy diễn grammar](/discrete-mathematics-for-computer-science-iuh/img/course/Parse_tree.png)

*Hình 19.15: Parse tree — chi tiết hơn AST; hữu ích khi debug grammar và lỗi cú pháp.*

---

## Phần 4: Sau parser — semantics và codegen

### 4.1. Type checking là vị từ trên AST

Sau khi có AST, compiler hỏi: $$\forall node,\ Type(node)$$ nhất quán? Ví dụ không cộng `string + int` (trừ khi ngôn ngữ cho phép overload).

### 4.2. Công cụ thực tế

| Giai đoạn | Công cụ ví dụ |
|---|---|
| Lexer generator | flex, ANTLR lexer |
| Parser generator | Bison, ANTLR, yacc |
| AST + IR | LLVM, Rust `syn`, Python `ast` module |

Python `ast.parse("x + 1")` trả AST sẵn — grammar được implement trong CPython.

```python
import ast
tree = ast.parse("price * (1 + tax)")
# ast.walk(tree) để duyệt node
```

<div class="content-box warning-box" markdown="1">
**Cẩn thận**: Ambiguous grammar (nhiều parse tree cho cùng chuỗi) gây bug ngầm. Ngôn ngữ production dùng precedence/associativity declaration hoặc grammar LL/LR đã chứng minh không ambiguous.
</div>

---

## Bài tập thực hành

### Bài tập 1: Phân loại Chomsky

Xếp loại: (a) mọi chuỗi `0` và `1` có số `1` chẵn; (b) $$a^n b^n$$; (c) cú pháp JSON (đơn giản hóa).

<details>
<summary>Đáp án</summary>

(a) Type-3 — regular. (b) Type-2 CF — không regular, cần stack. (c) Type-2 CF — cấu trúc lồng `{}`, `[]` với đệ quy.

</details>

### Bài tập 2: Viết BNF

Viết grammar cho chuỗi ngoặc đơn cân: `()`, `(())`, `()()`.

<details>
<summary>Đáp án</summary>

```
<S> ::= "" | "(" <S> ")" <S>
```

Hoặc `S -> (S) | SS | ε` tùy ký hiệu rỗng.

</details>

### Bài tập 3: Lexer

Tokenize `if x > 0` với spec: `IF` → `if`, `IDENT`, `GT` → `>`, `NUMBER`.

<details>
<summary>Đáp án</summary>

`[('IF','if'), ('IDENT','x'), ('GT','>'), ('NUMBER','0')]` (cần thêm pattern `if` trước `IDENT` trong spec để không nhận `if` là IDENT).

</details>

### Bài tập 4: AST tay

Vẽ AST cho `1 + 2 * 3` với grammar ưu tiên `*` trên `+`.

<details>
<summary>Đáp án</summary>

```
    +
   / \
  1   *
     / \
    2   3
```

Root là `+`; con phải là `*` — không phải cây cân bằng `+` và `*` cùng độ sâu.

</details>

### Bài tập 5: Lỗi lexical vs syntax

Phân loại lỗi: (1) `def @foo` — (2) `if (x + )`.

<details>
<summary>Đáp án</summary>

(1) Lexical — `@` không phải token hợp lệ (trong nhiều ngôn ngữ). (2) Syntax — thiếu operand sau `+`; token stream có thể hợp lệ nhưng parser fail.

</details>

### Bài tập 6: Python `ast`

Dùng `ast.parse` in loại node gốc của `3 * (4 + 5)`.

<details>
<summary>Đáp án</summary>

```python
import ast
tree = ast.parse("3 * (4 + 5)")
print(type(tree.body[0].value))  # <class 'ast.BinOp'>
print(ast.dump(tree.body[0].value, indent=2))
```

Gốc expression là `BinOp` với `op=Mult`.

</details>

### Bài tập 7: Left recursion

Grammar `E -> E + T | T` có **left recursion**. Vì sao recursive descent naive gọi `parse_E` vô hạn?

<details>
<summary>Đáp án</summary>

`parse_E` gọi `parse_E` ngay trước khi đọc token mới — không tiến `pos`. Cần chuyển sang dạng right recursion hoặc loop (`while` đọc `+`) như Phần 3.2.

</details>

### Bài tập 8: Thiết kế pipeline

Liệt kê 5 bước từ file `.java` đến bytecode JVM, gắn mỗi bước với regular/CFG/semantic.

<details>
<summary>Đáp án</summary>

1. Đọc file (chuỗi) — raw.
2. Lexer → token stream — **regular**.
3. Parser → AST — **CFG**.
4. Type check / semantic analysis — predicate trên AST.
5. Codegen → bytecode — IR transformation.

</details>

## Tóm tắt

- **Ngôn ngữ** $$L \subseteq \Sigma^*$$ — compiler kiểm tra membership.
- **Lexer** (Type-3): regex/DFA → token.
- **Parser** (Type-2): CFG/BNF → parse tree → **AST**.
- **AST** là giao diện cho type checker, optimizer, codegen.
- **Chomsky hierarchy** chọn đúng công cụ: đừng dùng regex parse cú pháp lồng nhau.

Trong Chương 20, chúng ta hỏi câu khác: không chỉ "có parse được không", mà "parse và tối ưu trong thời gian chấp nhận được không?" — độ phức tạp và lớp P/NP.