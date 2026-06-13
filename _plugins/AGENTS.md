# JEKYLL PLUGINS KNOWLEDGE BASE

## OVERVIEW
Custom Ruby plugins. Only one plugin is currently active; the two multilang plugins were disabled by renaming them with a `.disabled` suffix so Jekyll no longer loads them.

## CONVENTIONS
- Plugins run during `bundle exec jekyll build` and `bundle exec jekyll serve`.
- Keep plugin behavior compatible with Jekyll 4.3 and Liquid 4.
- Bilingual UI labels under `t.en` / `t.vi` in `_config.yml` are still active for page chrome (titles, switch links) even with the multilang plugins disabled.
- Generated artifacts should go through the Jekyll destination, not source directories.

## NOTES
- Liquid parsing errors in content (`{{...}}` math) happen before any generated outputs finish, so a single lesson with unescaped braces can fail the whole build.