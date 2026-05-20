# PUBLIC ASSETS KNOWLEDGE BASE

## OVERVIEW
Editable CSS/JS/image assets for Jekyll site. Generated copies live under `_site/public/`.

## STRUCTURE
```
public/
├── css/                     # layout, theme, math, content boxes
├── js/                      # multilingual UI, exercises, demos
├── logo.png
└── convex-logo-144x144.png
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Course-specific styling | `css/discrete-math.css` | Math UI and course visual rules. |
| Content boxes | `css/content-boxes.css` | Note/theorem/example/warning classes. |
| Layout theme | `css/poole.css`, `css/lanyon.css` | Base theme styles. |
| Multilingual UI | `css/multilang.css`, `js/multilang.js` | Language switch behavior. |
| Exercises | `js/exercise-system.js` | Interactive exercise logic. |

## CONVENTIONS
- Edit only `public/...`; Jekyll copies to `_site/public/...`.
- Keep class names used by chapter HTML stable, especially `interactive-tool` and content-box classes.
- Prefer additive CSS changes when content already depends on existing classes.
- Verify mobile layout after CSS changes; many chapter pages include wide math/tables.

## ANTI-PATTERNS
- Do not patch `_site/public` directly.
- Do not rename CSS/JS files without checking layouts/includes that reference them.
- Do not remove content-box classes; Markdown/HTML embeds rely on them.
