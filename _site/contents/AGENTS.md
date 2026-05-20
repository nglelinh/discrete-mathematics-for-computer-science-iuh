# CONTENTS KNOWLEDGE BASE

## OVERVIEW
Chapter source tree for course pages/posts. Treat Markdown/HTML here as source; `_site/contents/...` is generated.

## STRUCTURE
```
contents/
├── en/chapter*/             # chapter posts/pages, often Vietnamese prose
└── vi/                      # Vietnamese language output/source area
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Chapter page text | `contents/*/chapter*/index.html` | Page-level chapter landing content. |
| Lesson posts | `contents/*/chapter*/_posts/` | Ordered by front matter and dated filenames. |
| Front matter bugs | Top of each post/page | Check `layout`, `categories`, `order`, `required`, `lang`. |
| Math render bugs | Markdown body | Liquid parses `{{...}}` before Markdown/MathJax. |
| Chapter images | `../img/chapter_img/chapterNN/` | Keep image filenames stable. |

## CONVENTIONS
- Keep chapter numbering in path, category, and linked image folder aligned.
- Keep `categories: chapterNN` matching parent chapter directory.
- Preserve `order:` for lesson ordering.
- Use `lang:` from desired output language, not from visible prose alone.
- Escape raw Liquid-looking math with `{% raw %}` blocks or rewrite notation.

## ANTI-PATTERNS
- Do not edit `_site/contents` for content fixes.
- Do not leave `{{...}}` mathematical sets unescaped in Jekyll-processed files.
- Do not rename dated post files without checking generated permalink impact.
- Do not mass-change `lang:`; `fix_language_tags.sh` exists because prior language tags were inconsistent.

## NOTES
- Known failing file while serving: `contents/en/chapter12/_posts/21-01-01-12_01_Introduction_to_Graphs.md`.
- Exact failing pattern: `E = {{1,2}, {2,3}}`.
