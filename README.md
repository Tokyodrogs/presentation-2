# Fresko — Philippine Startup Challenge XI Concept Note

A 15-slide, **3D auto-advancing** concept-note presentation for the Philippine Startup
Challenge XI, built as a working example (the sample venture "Fresko" can be swapped for
your own idea).

> **Fresko** — *Farm-side cooling, shared.* Solar-powered 2-tonne cold rooms plus a
> freshness-AI app, shared by ~40 smallholder vegetable farms per hub. Priority SDG:
> **SDG 12** (Responsible Consumption & Production, Target 12.3), with SDGs 2, 8, 9, 13.

## What's in here

| File | What it is |
|---|---|
| `index.html` | The live deck — real CSS 3D page-turn (rotating carousel), autoplay, presenter notes, overview grid, parallax camera. Self-contained, no build step. |
| `Fresko-PSC-XI-Concept-Note.pptx` | The PowerPoint version of the same 15 slides, with a **Cube (3D) transition on every slide** and **auto-advance timings** — press F5 (Slide Show) and it turns and moves by itself. |
| `tools/build_pptx.py` | Rebuilds the `.pptx` from scratch (`python3 tools/build_pptx.py`). Edit content here, not by hand. |
| `CONCEPT-NOTE.md` | The full written concept note (Sections I–X) with sources, assumptions and unit economics — submission-ready text. |
| `assets/` | Brand logo, hero photo and cold-room photo used by both decks. |

### About the PowerPoint version

- **3D page turn:** every slide carries PowerPoint's *Cube* transition (`p14:cube dir="l"`), with a `push` fallback for older readers.
- **Auto-advance:** each slide has its own `advTm` (13–18 s), and `useTimings` is on by default — so the show runs itself in Slide Show mode. Adjust the numbers in `tools/build_pptx.py` (the `slide(13000)` calls).
- Speaker notes are attached to all 15 slides.
- Fonts: Calibri; colours match the HTML deck.

## Run the deck

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Or just open `index.html` directly in a browser.

### Controls

| Key | Action |
|---|---|
| `→` / `Space` | Next slide (3D turn) |
| `←` | Previous slide |
| `P` | Play / pause autoplay |
| `O` | Overview grid (click any slide to jump) |
| `N` | Presenter notes for the current slide |
| `F` | Fullscreen |
| `Home` / `End` | First / last slide |

Autoplay is **on by default**: each slide advances on its own after its own duration
(13–18s), and every element animates in on a stagger. Click the right/left half of the
screen to advance or go back; swipe on touch.

## The deck

1. Cover
2. The 30-second pitch
3. I. Summary
4. II. Background of the problem
5. III. Proposed startup solution (SDG alignment)
6. IV. Objectives (SMART, Month-12 targets)
7. V. Target market / beneficiaries
8. VI. Value proposition (vs. status quo, own cold room, reefer 3PL)
9. VII. Business model (4 revenue lines + unit economics)
10. VIII. Market analysis (TAM / SAM / SOM + positioning map)
11. IX. Operations plan (phased rollout + SOPs + risks)
12. X. Financial requirement (₱2.4M use of funds + 3-year projection)
13. Impact & SDG alignment
14. Closing & asks
15. Appendix — sources & assumptions

## Customise it

- **Team name / startup name:** search `index.html` for `[TEAM NAME]` and `[Member 1]`.
- **Colours:** the whole theme is CSS variables at the top of `index.html` (`--forest`,
  `--mint`, `--amber`, …).
- **Timing:** each `<article class="slide">` has `data-dur="15000"` (milliseconds).
- **Notes:** each slide's `data-notes="…"` is the presenter script.

## Sources used in the content

PSA RSSO-CAR (Benguet 2024) · UN-CSAM / Mopera (2016) · PCAARRD (2025) · SEARCA/ADB (2022) ·
UN Food Systems Philippines Pathway · industry cold-chain capacity estimates · OECD
agricultural policy review. Full list in `CONCEPT-NOTE.md`.
