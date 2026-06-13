---
name: illustration-fetcher
description: >
  Download educational illustrations from multiple verified sources.
  Validates image content before saving. Supports Wikimedia Commons,
  Unsplash, Pixabay, and placeholder services.
---

Use this skill whenever generating or editing Jekyll lessons.

## Workflow

1. Read the Markdown lesson.
2. Identify concepts that benefit from illustrations.
3. Try multiple sources in order:
   - Wikimedia Commons (verified URLs)
   - Unsplash (high-quality photos)
   - Pixabay (free illustrations)
   - Placeholder.co (as fallback)
4. **VALIDATE** each download:
   - Check HTTP status (must be 200)
   - Verify file is actually an image (not HTML error page)
   - Check file size (> 1KB)
5. Save to: `assets/img/<lesson-slug>/<filename>.{svg|png|jpg}`
6. Use lowercase kebab-case filenames.
7. Insert Markdown references with Vietnamese captions.
8. Skip if no valid image found (don't insert broken references).

## Image Validation Rules

Before saving any image:
- File must start with valid image magic bytes:
  - SVG: `<?xml` or `<svg`
  - PNG: `\x89PNG`
  - JPEG: `\xFF\xD8`
  - GIF: `GIF8`
- File size must be > 1024 bytes
- Content-Type must be image/* (if available)

## Sources Priority

1. **Wikimedia Commons** - Educational diagrams, public domain
   - Base: `https://commons.wikimedia.org/wiki/Special:FilePath/`
   - Format: `?width=800`

2. **Unsplash** - High-quality photos
   - Source: `https://source.unsplash.com/800x600/?{query}`

3. **Pixabay** - Free illustrations
   - Requires API key (optional)

4. **Placeholder** - Fallback only
   - `https://via.placeholder.com/800x600?text={query}`

## Usage

```bash
# The skill provides these functions:
# - search_wikimedia(query) -> url or None
# - search_unsplash(query) -> url or None
# - validate_and_download(url, output_path) -> bool
```
