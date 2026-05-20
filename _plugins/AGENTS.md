# JEKYLL PLUGINS KNOWLEDGE BASE

## OVERVIEW
Custom Ruby plugins for generated pages, redirects, and multilingual URLs.

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Redirect output | `redirect_generator.rb` | Generates redirect pages during build. |
| Multilingual post URL | `multilang_post_url.rb` | URL helper/filter behavior. |
| Multilingual site logic | `multilang.rb` | Language-aware Jekyll behavior. |

## CONVENTIONS
- Plugins run during `bundle exec jekyll build` and `bundle exec jekyll serve`.
- Keep plugin behavior compatible with Jekyll 4.3 and Liquid 4.
- Match languages from `_config.yml`: `en`, `vi`.
- Generated artifacts should go through Jekyll destination, not source directories.

## ANTI-PATTERNS
- Do not add plugin dependencies without updating `Gemfile` and `Gemfile.lock`.
- Do not assume plugin changes are safe until `bundle exec jekyll build` passes.
- Do not write generated files into source-of-truth directories unless intentionally tracked.

## NOTES
- Liquid parsing errors in content happen before many generated outputs finish.
