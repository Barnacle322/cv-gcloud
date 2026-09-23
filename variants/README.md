# Résumé variants

Tailored PDFs for specific applications. The public site (`/`) and `/download`
always render the base résumé from `src/resume_data.py`; variants only produce
PDFs.

```
DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib uv run --python 3.12 \
    --with weasyprint --with flask python src/render.py variants/teach.json
```

Output lands next to the JSON unless `-o` is given.

## JSON keys (all optional)

| key | meaning |
|---|---|
| `headline` | one line under the name (e.g. `Full-Stack Developer · BCIT CIT student`) |
| `summary` | short paragraph at the top of the main column |
| `location` | overrides `Vancouver, BC` |
| `skills` | full replacement list of `{category, text}` |
| `experiences` | ordered list; each item is an id string or `{id, title?, bullets?, extra_bullets?}`. Ids not listed are omitted. Ids: `rw atlabyte kasu globalify wiot cec bilimkana developstoday eso` |
| `education` | full replacement list of `{years, program, place}` |
| `show_days` | show the `(N days)` counter (default off for variants) |
| `filename` | output PDF name |

Rules: keep experiences in reverse-chronological order (ids above are listed newest first). Never invent facts — only reorder, trim, or reword what the base already
says. Keep every variant to one A4 page unless the role is senior.
