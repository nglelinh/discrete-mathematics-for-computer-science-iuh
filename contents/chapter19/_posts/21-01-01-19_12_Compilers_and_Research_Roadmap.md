---
layout: post
title: "Compiler, Parser và Lộ trình Nghiên cứu"
categories: chapter19
date: 2021-01-01
order: 12
required: true
lang: en
excerpt: "Lexer vs parser; LL/LR ý; checklist DSL; lộ trình 12 tuần NCS; thư mục."
---


<div class="textbook-epigraph" markdown="1">

"Lex with regular languages; parse with context-free structure."

<span class="epigraph-attribution">— Compiler construction</span>

</div>

![Phases](/discrete-mathematics-for-computer-science-iuh/img/course/compiler_phases.svg)

<p class="textbook-figure-caption" data-figure="19.4">Lexer regular · parser CFG.</p>

## Bản đồ Ch.19

Σ* → grammar → Chomsky → CFG/PDA → pump → CNF/CYK → compiler.

## Compiler

| Tầng | Lớp | Công cụ |
|:---|:---|:---|
| Lexer | Regular | Flex, regex |
| Parser | CFL (thường LALR/LL) | yacc, ANTLR, hand RD |

**DCFL** ⊂ CFL: deterministic PDA — liên hệ parsing thực tế.

## Nhánh nghiên cứu

| Nhánh | Chủ đề |
|:---|:---|
| Parsing theory | GLL, GLR, earley, PEG |
| Grammar inference | learning CFGs |
| Tree automata | XML, compilers |
| Weighted/SCFG | NLP |
| Verification | pushdown systems |

## Lộ trình 12 tuần

1–2: 19.1–19.5 + Ch.18 regular bridge  
3–5: CFG PDA pump  
6–7: CNF CYK implement  
8: Dragon book parsing chapters  
9–10: chọn nhánh + papers  
11–12: mini parser / note hardness CFL

## Portfolio

1. Chứng minh $$a^nb^n$$ CFG + không regular  
2. $$a^nb^nc^n$$ không CFL  
3. CYK code + test  
4. Grammar không mơ hồ cho expr

## Thư mục

Sipser; Hopcroft; Aho et al. *Compilers*; Grune *Parsing Techniques*; Sakarovitch; Kozen.

## Tóm tắt Chương 19

12 bài: từ chuỗi đến CFL/PDA/CYK và cửa ngõ nghiên cứu ngôn ngữ/biên dịch — nối Ch.18 (regular/TM) và Ch.20 (complexity của parsing ∈ P cho CNF, nhưng nhiều bài grammar hard).
