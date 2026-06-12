# CONTENTS KNOWLEDGE BASE

## OVERVIEW
Chapter source tree for course pages/posts. Vietnamese-first lesson prose, with mixed `lang: en` / `lang: vi` front matter (see CONVENTIONS). Treat Markdown/HTML here as source; `_site/contents/...` is generated and must not be edited. To author a new lesson, load the user-global `math-lesson-creator` skill (`~/.claude/skills/math-lesson-creator/SKILL.md`).

## STRUCTURE
```
contents/
├── chapter01/ ... chapter16/   # 78 lesson files across 16 populated chapters
└── chapter17/ ... chapter20/   # placeholder chapter dirs (index.html only, no _posts/ yet)
```

A populated chapter directory looks like:
```
contents/chapterNN/
├── index.html              # chapter landing page
└── _posts/
    └── YY-MM-DD-NN_MM_Lesson_Name.md   # date typically 21-01-01; NN matches chapter, MM is lesson order
```

There is NO `contents/en/` or `contents/vi/` subdirectory. The tree was flattened. The bilingual `t.en` / `t.vi` UI labels in `_config.yml` remain active for page chrome, but per-page language-switching machinery is dormant (see `../_plugins/AGENTS.md`).

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Chapter landing page | `contents/chapterNN/index.html` | All 20 chapters share the same template; copy a populated one when seeding 17-20. Uses `{% assign sorted_posts = site.categories.chapterNN \| sort: "order" %}`. |
| Lesson posts | `contents/chapterNN/_posts/` | Ordered by `order:` front matter; dated filenames affect permalink. |
| Front matter bugs | Top of each post | Check `layout`, `title`, `categories`, `date`, `order`, `required`, `lang`. |
| Math render bugs | Markdown body | Liquid parses `{{...}}` before kramdown/MathJax. |
| Chapter images | `../img/chapter_img/chapterNN/` relative to repo root | Reference with literal absolute path including baseurl, not `{{ site.baseurl }}`. |
| How to author a new lesson | `~/.claude/skills/math-lesson-creator/SKILL.md` | Front-matter template, math/Liquid pitfalls, widget catalog, content-box reference. |

## CONVENTIONS
- Keep chapter numbering aligned across path (`chapterNN`), `categories: chapterNN`, and `img/chapter_img/chapterNN/`.
- Preserve `order:` for lesson ordering within a chapter; chapter `index.html` sorts on it.
- `lang: en` is the majority convention (65 of 78 lessons) even when prose is Vietnamese. Chapter index sort does not depend on `lang:`. When adding a new lesson, match the rest of the chapter rather than choosing arbitrarily.
- Escape raw Liquid-looking math: rewrite `{...}` as `\{...\}` inside `$$ ... $$`, or wrap the whole math block in `{% raw %}` / `{% endraw %}`. Both patterns are used in production lessons.
- Use `$$ ... $$` for both inline and display math (project convention); single `$` is NOT used.
- Image markup uses the literal absolute prefix: `<img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapterNN/file.png" ...>`. Do not substitute `{{ site.baseurl }}`.

## ANTI-PATTERNS
- Do not edit `_site/contents/` for content fixes; Jekyll regenerates it on every build.
- Do not leave `{{...}}` mathematical sets unescaped in Jekyll-processed files.
- Do not rename dated post files without checking generated permalink impact.
- Do not mass-change `lang:` values across many files; the field has been inconsistent historically and bulk edits have caused regressions.
- Do not invent `{% multilang_post_url %}` cross-references; the plugin is disabled (see `../_plugins/AGENTS.md`). No production lesson uses post cross-links - write prose references to lesson titles or a hand-crafted relative URL instead.

## NOTES
- The historically failing pattern `E = {{1,2}, {2,3}}` in `chapter12/_posts/21-01-01-12_01_Introduction_to_Graphs.md` has been fixed using `$$E = [\{1,2\}, \{2,3\}]$$` (square brackets wrap the set literal to avoid the `{{` Liquid open tag). Use this file as the canonical example for graph-related set notation.
- Other canonical `{% raw %}$$...$${% endraw %}` examples live at `chapter02/_posts/21-01-01-02_03_Rules_of_Inference_for_Predicate_Logic.md:61` and `chapter10/_posts/21-01-01-10_01_Introduction_to_Recurrence_Relations.md:119`.
- Chapters 17-20 have only an `index.html` placeholder and no `_posts/` directory yet.
