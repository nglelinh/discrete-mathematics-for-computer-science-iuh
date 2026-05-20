# PROJECT KNOWLEDGE BASE

**Generated:** 2026-05-12
**Commit:** c60968b
**Branch:** main

## OVERVIEW
Jekyll 4.3 static course site for "Discrete Mathematics for Computer Science" at IUH. Content is bilingual (`en`, `vi`) but much chapter source currently lives under `contents/en` with Vietnamese text/front matter.

## STRUCTURE
```
./
├── _config.yml              # Jekyll config, multilingual labels, baseurl/imgurl
├── _plugins/                # custom Jekyll generators/tags
├── contents/                # chapter pages/posts, main course body
├── contribution/            # contributor docs as Jekyll posts
├── home/                    # home-page posts
├── img/chapter_img/         # source images used by chapters
├── public/css/              # site styles and course widgets
├── public/js/               # language, exercise, interactive scripts
├── reference/               # reference page/posts
├── src/                     # helper scripts, not site runtime
└── _site/                   # generated Jekyll output; do not edit
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Site config, base URL, languages | `_config.yml` | `baseurl` must stay `/discrete-mathematics-for-computer-science-iuh` for GitHub Pages. |
| Main course chapters | `contents/en/chapter*/`, `contents/vi/` | Post/page front matter drives navigation and output. |
| Chapter images | `img/chapter_img/chapter*/` | `_site/img/...` is generated copy. |
| Styling | `public/css/` | `_site/public/css/` mirrors generated output. |
| Browser behavior | `public/js/` | Multilingual UI, exercises, demos. |
| Redirect/localization logic | `_plugins/redirect_generator.rb`, `_plugins/multilang*.rb` | Keep URL semantics aligned with `_config.yml`. |
| Serve/build | `Gemfile`, `Gemfile.lock`, `docker-compose.yml` | Prefer Bundler command below. |

## CODE MAP
| Symbol/File | Type | Location | Role |
|-------------|------|----------|------|
| `_config.yml` | config | root | Jekyll, multilingual labels, plugins, author metadata. |
| `multilang.rb` | plugin | `_plugins/` | Multilingual filtering/navigation support. |
| `redirect_generator.rb` | plugin | `_plugins/` | Redirect output generation. |
| `discrete-math.css` | CSS | `public/css/` | Course-specific math/UI styling. |
| `content-boxes.css` | CSS | `public/css/` | Styled note/theorem/example boxes. |
| `exercise-system.js` | JS | `public/js/` | Exercise interactions. |

## CONVENTIONS
- Use Jekyll posts/pages with YAML front matter: `layout`, `title`, `categories`, `date`, `order`, `required`, `lang`.
- Use `bundle exec jekyll serve` or `bundle exec jekyll build`.
- Source-of-truth assets live outside `_site`; generated mirrors under `_site` must be ignored for edits.
- Mathematical set notation like `{{1,2}}` conflicts with Liquid; escape or wrap affected math in raw tags.
- Keep bilingual labels in `_config.yml` synchronized across `t.en` and `t.vi`.

## ANTI-PATTERNS (THIS PROJECT)
- Do not edit `_site/`; Jekyll overwrites it.
- Do not fix generated HTML when source Markdown/post caused build error.
- Do not put raw `{{...}}` math in processed Markdown unless wrapped with `{% raw %}` / `{% endraw %}` or rewritten.
- Do not change `baseurl` casually; deployed paths depend on it.
- Do not assume directory name language equals content language; verify `lang:` front matter.

## UNIQUE STYLES
- Vietnamese-first course prose, with English site/course metadata still present.
- Chapter images grouped by `img/chapter_img/chapterNN` and referenced from chapter content.
- Interactive demos use `<div class="interactive-tool">` plus CSS/JS from `public/`.
- Content boxes use named classes from `public/css/content-boxes.css`.

## COMMANDS
```bash
bundle install
bundle exec jekyll serve
bundle exec jekyll build
docker compose up
```

## NOTES
- Current known build failure: `contents/en/chapter12/_posts/21-01-01-12_01_Introduction_to_Graphs.md` line with `E = {{1,2}, {2,3}}` is parsed as Liquid.
- `Gemfile` pins Jekyll `~> 4.3.0`; `Gemfile.lock` currently resolves Jekyll 4.3.4.
- `docker-compose.yml` uses `jekyll/jekyll:4.2.0` and installs Bundler 1.17.2; local Bundler path may behave differently.
