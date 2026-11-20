# Skill: Add trusted educational video links to Discrete Math lessons

## Purpose
Append a "Xem thêm / Video gợi ý" section (2–3 high-quality YouTube links) to the end of each lesson file, right before the `## Tóm tắt` heading. Sources must be reputable, high-view-count channels with clear explanations.

## Design rules
- **Trusted sources only** (priority order):
  1. 3Blue1Brown (Grant Sanderson) — animation + deep intuition
  2. MIT OCW (Gilbert Strang, Tom Leighton 6.042J)
  3. Khan Academy — clear basics, subtitles
  4. Numberphile — combinatorial topics
  5. Trefor Bazett / TrevTutor — full Discrete Math playlists
  6. William Fiset — algorithms + discrete math
- Always use the **watch?v=** form with timestamp if relevant.
- Exactly **2–3 links** per lesson.
- Insert **before** `## Tóm tắt`.
- Use Vietnamese label: `## Xem thêm / Video gợi ý`.
- Format:

```markdown
## Xem thêm / Video gợi ý

- [Title](https://youtube.com/watch?v=ID) — Channel (why it helps)
- [Title](https://youtube.com/watch?v=ID) — Channel
```

## When to run
- New lesson created
- Major content update
- Quarterly review pass

## Safety
- Never overwrite existing video section.
- If section already exists, skip or append only if user confirms.
- Do not change lesson structure or navigation.
