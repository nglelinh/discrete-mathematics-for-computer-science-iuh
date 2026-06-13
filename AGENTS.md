# PROJECT KNOWLEDGE BASE

**Updated:** 2026-06-06
**Branch:** main

## OVERVIEW
Jekyll 4.3 static course site for "Discrete Mathematics for Computer Science" at IUH. Vietnamese-first lesson prose; site chrome remains bilingual via `_config.yml` `t.en` / `t.vi` translations. Chapter source lives in a flat `contents/chapterNN/` tree (no `en/` or `vi/` subdirectories).

## STRUCTURE
```
./
├── _config.yml              # Jekyll config, bilingual UI labels, baseurl/imgurl
├── _plugins/                # custom Jekyll plugins; see _plugins/AGENTS.md for active/disabled state
├── contents/                # chapter pages/posts, main course body; see contents/AGENTS.md
├── contribution/            # contributor docs as Jekyll posts
├── home/                    # home-page posts
├── img/chapter_img/         # source images, grouped chapter_img/chapterNN/
├── public/css/              # site styles, course widgets, content boxes
├── public/js/               # multilingual UI, exercise system, ~50 interactive demos
├── reference/               # reference page/posts
├── src/                     # helper scripts (currently just change_issue_title.py)
└── _site/                   # generated Jekyll output; do not edit
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Site config, base URL, languages | `_config.yml` | `baseurl` must stay `/discrete-mathematics-for-computer-science-iuh` for GitHub Pages. Multilang `languages:` is commented out. |
| Main course chapters | `contents/chapterNN/` for NN in 01-20 | 16 populated, 4 are placeholders. See `contents/AGENTS.md`. |
| Chapter images | `img/chapter_img/chapterNN/` | `_site/img/...` is the generated copy; do not edit. |
| Styling | `public/css/` | `_site/public/css/` is the generated mirror. |
| Browser behavior | `public/js/` | Multilingual UI, exercise system, ~50 interactive widgets. |
| Active plugin logic | `_plugins/redirect_generator.rb` | Multilang plugins are `.disabled`; see `_plugins/AGENTS.md`. |
| Serve / build | `Gemfile`, `Gemfile.lock`, `docker-compose.yml` | Prefer the Bundler command below. |
| Writing a new lesson | `~/.claude/skills/math-lesson-creator/SKILL.md` | User-global skill: front-matter template, math/Liquid escapes, widget catalog, content-box reference. |

## CODE MAP
| Symbol/File | Type | Location | Role |
|-------------|------|----------|------|
| `_config.yml` | config | root | Jekyll config, bilingual UI labels, plugins, author metadata. |
| `redirect_generator.rb` | plugin | `_plugins/` | Only active plugin; emits redirect pages on build. |
| `multilang.rb.disabled` | disabled plugin | `_plugins/` | Multilingual filtering; not loaded. |
| `multilang_post_url.rb.disabled` | disabled plugin | `_plugins/` | `{% raw %}{% multilang_post_url %}{% endraw %}` Liquid tag; not loaded. |
| `mathjax-config.js` | JS config | root | MathJax 3 setup; custom macros (`\N \Z \floor \ceil \deg \O \Theta` etc). |
| `discrete-math.css` | CSS | `public/css/` | Course-specific math/UI styling, plus legacy `.math-*` callout classes. |
| `content-boxes.css` | CSS | `public/css/` | Modern callouts: `insight-box`, `exercise-box`, `summary-box`, `warning-box`, `info-box`, `note-box`, `example-box`, `question-box`. |
| `exercise-system.js` | JS | `public/js/` | `ExerciseSystem` class with localStorage progress tracking; globally loaded. |

## CONVENTIONS
- Use Jekyll posts/pages with YAML front matter: `layout`, `title`, `categories`, `date`, `order`, `required`, `lang`.
- Use `bundle exec jekyll serve` or `bundle exec jekyll build`.
- Source-of-truth assets live outside `_site`; generated mirrors under `_site` must be ignored for edits.
- Mathematical set notation like `{{1,2}}` conflicts with Liquid; escape `{...}` as `\{...\}` inside `$$ ... $$`, or wrap the math block with `{% raw %}` / `{% endraw %}`.
- Use `$$ ... $$` for both inline and display math (project convention); single `$` is NOT used.
- Keep bilingual UI labels in `_config.yml` synchronized across `t.en` and `t.vi`.

## ANTI-PATTERNS (THIS PROJECT)
- Do not edit `_site/`; Jekyll overwrites it on every build.
- Do not fix generated HTML when source Markdown/post caused build error - fix the source.
- Do not put raw `{{...}}` math in processed Markdown unless wrapped with `{% raw %}` / `{% endraw %}` or rewritten.
- Do not change `baseurl` casually; deployed paths and image `src` attributes depend on it.
- Do not assume directory name implies content language; chapter directories are flat (`chapterNN/`) and `lang:` front matter is the source of truth.
- Do not invent `{% multilang_post_url %}` cross-references in lessons; the plugin is disabled.

## UNIQUE STYLES
- Vietnamese-first lesson prose, with English/Vietnamese site chrome via `_config.yml` `t.en` / `t.vi`.
- Chapter images grouped by `img/chapter_img/chapterNN/` and referenced with literal baseurl-prefixed absolute paths.
- Interactive demos use `<div data-demo="widget-id"></div>`; the `public/js/` script is auto-discovered, no per-page `<script>` tag needed.
- Content boxes use named classes from `public/css/content-boxes.css` plus `markdown="1"` so inner Markdown renders.

## COMMANDS
```bash
bundle install
bundle exec jekyll serve
bundle exec jekyll build
docker compose up
```

## NOTES
- The historically failing pattern `E = {{1,2}, {2,3}}` in `contents/chapter12/_posts/21-01-01-12_01_Introduction_to_Graphs.md` has been fixed using `$$E = [\{1,2\}, \{2,3\}]$$`. Use this file as the canonical example for graph-related set notation.
- `Gemfile` pins Jekyll `~> 4.3.0`; `Gemfile.lock` currently resolves Jekyll 4.3.4.
- `docker-compose.yml` uses `jekyll/jekyll:4.2.0` and installs Bundler 1.17.2; local Bundler path may behave differently.
