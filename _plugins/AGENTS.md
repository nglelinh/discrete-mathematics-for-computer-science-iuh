# JEKYLL PLUGINS KNOWLEDGE BASE

## OVERVIEW
Custom Ruby plugins. Only one plugin is currently active; the two multilang plugins were disabled by renaming them with a `.disabled` suffix so Jekyll no longer loads them.

## STRUCTURE
```
_plugins/
├── redirect_generator.rb              # ACTIVE - generates redirect pages during build
├── multilang.rb.disabled              # DISABLED - language-aware Jekyll behavior
└── multilang_post_url.rb.disabled     # DISABLED - {% multilang_post_url %} Liquid tag
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Redirect output | `redirect_generator.rb` | Only active plugin; generates redirect pages on build. |
| Cross-post Liquid tags | (none) | `{% multilang_post_url %}` is NOT available; the plugin is disabled. No production lesson uses post cross-links. |
| Language-aware filters | (none) | `multilang.rb` is disabled; corresponding `languages:` and `default_lang:` lines in `_config.yml` are also commented out. |

## CONVENTIONS
- Plugins run during `bundle exec jekyll build` and `bundle exec jekyll serve`.
- Keep plugin behavior compatible with Jekyll 4.3 and Liquid 4.
- Bilingual UI labels under `t.en` / `t.vi` in `_config.yml` are still active for page chrome (titles, switch links) even with the multilang plugins disabled.
- Generated artifacts should go through the Jekyll destination, not source directories.

## ANTI-PATTERNS
- Do not re-enable `multilang.rb` or `multilang_post_url.rb` in isolation: per-page language switching, the `languages:` config in `_config.yml`, and post cross-link references in lessons would all need to be re-established together.
- Do not add plugin dependencies without updating `Gemfile` and `Gemfile.lock`.
- Do not assume plugin changes are safe until `bundle exec jekyll build` passes.
- Do not write generated files into source-of-truth directories unless intentionally tracked.

## NOTES
- Liquid parsing errors in content (`{{...}}` math) happen before any generated outputs finish, so a single lesson with unescaped braces can fail the whole build.
- If `{% multilang_post_url %}` reappears in lesson source files it will trigger a Liquid error at build time because the tag is no longer defined.
