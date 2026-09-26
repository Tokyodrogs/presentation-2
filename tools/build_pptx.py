#!/usr/bin/env python3
"""
Build the Fresko · Philippine Startup Challenge XI PowerPoint deck.

Mirrors the HTML deck (index.html) but as a real .pptx:
  * 16:9 slides, dark brand theme
  * PowerPoint "Cube" (3D) transition on EVERY slide  -> pages physically turn
  * advTm auto-advance timings on every slide          -> deck advances by itself
  * speaker notes on every slide

Run:  python3 tools/build_pptx.py
Out:  Fresko-PSC-XI-Concept-Note.pptx
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.oxml.ns import qn
from lxml import etree
import copy, os

# ----------------------------------------------------------------- brand ----
DEEP   = RGBColor(0x04, 0x12, 0x0C)
BG     = RGBColor(0x07, 0x21, 0x1A)
PANEL  = RGBColor(0x0C, 0x2E, 0x22)
PANEL2 = RGBColor(0x10, 0x3A, 0x2C)
LINE   = RGBColor(0x1E, 0x45, 0x36)
MINT   = RGBColor(0x7F, 0xD1, 0xAE)
LEAF   = RGBColor(0x2E, 0x7D, 0x5B)
AMBER  = RGBColor(0xF2, 0xA3, 0x3C)
AMBER2 = RGBColor(0xFF, 0xD9, 0xA2)
CORAL  = RGBColor(0xE4, 0x57, 0x2E)
SKY    = RGBColor(0x8F, 0xD4, 0xE8)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
TEXT   = RGBColor(0xEA, 0xF4, 0xEE)
BODY   = RGBColor(0xCB, 0xE2, 0xD7)
MUTED  = RGBColor(0x9F, 0xBB, 0xAE)
DIM    = RGBColor(0x7E, 0x9D, 0x8F)
CREAM  = RGBColor(0xF7, 0xF5, 0xEF)
CREAM2 = RGBColor(0xED, 0xE9, 0xDE)
INK    = RGBColor(0x0A, 0x1F, 0x17)
INK2   = RGBColor(0x3A, 0x53, 0x48)
INK3   = RGBColor(0x20, 0x56, 0x3D)

FONT = "Calibri"
W, H = 13.333, 7.5
M = 0.62                      # side margin
CW = W - 2 * M                # content width  (12.09")

P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
MC  = "http://schemas.openxmlformats.org/markup-compatibility/2006"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(W), Inches(H)
BLANK = prs.slide_layouts[6]

# --------------------------------------------------------------- helpers ----
def slide(auto_ms=12000, cube=True):
    s = prs.slides.add_slide(BLANK)
    if cube:
        _add_cube_transition(s, auto_ms)
    return s

def _add_cube_transition(s, auto_ms):
    """Insert a PowerPoint p14 Cube (3D) transition + auto-advance timing."""
    xml = (
        f'<mc:AlternateContent xmlns:mc="{MC}">'
        f'  <mc:Choice xmlns:p14="{P14}" Requires="p14">'
        f'    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
        f'                  xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
        f'                  advTm="{auto_ms}" p14:dur="1100">'
        f'      <p14:cube dir="l"/>'
        f'    </p:transition>'
        f'  </mc:Choice>'
        f'  <mc:Fallback>'
        f'    <p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
        f'                  xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"'
        f'                  spd="slow" advTm="{auto_ms}">'
        f'      <p:push dir="l"/>'
        f'    </p:transition>'
        f'  </mc:Fallback>'
        f'</mc:AlternateContent>'
    )
    node = etree.fromstring(xml)
    clr = s._element.find(qn('p:clrMapOvr'))
    clr.addnext(node)                      # cSld, clrMapOvr, transition

def notes(s, text):
    s.notes_slide.notes_text_frame.text = text

def rect(s, x, y, w, h, fill=None, line=None, lw=0.75, radius=0.05,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE and radius is not None:
        try:
            sh.adjustments[0] = radius
        except Exception:
            pass
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(lw)
    sh.shadow.inherit = False
    sh.text_frame.word_wrap = True
    return sh

def tb(s, x, y, w, h, text, size=10, color=BODY, bold=False, align=PP_ALIGN.LEFT,
       spacing=1.0, space_after=0, font=FONT, anchor=MSO_ANCHOR.TOP, italic=False):
    box = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    lines = text if isinstance(text, list) else [text]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        p.space_after = Pt(space_after)
        if isinstance(ln, str):
            ln = [(ln, {})]
        for t, st in ln:
            r = p.add_run(); r.text = t
            f = r.font
            f.name = st.get('font', font)
            f.size = Pt(st.get('size', size))
            f.bold = st.get('bold', bold)
            f.italic = st.get('italic', italic)
            f.color.rgb = st.get('color', color)
    return box

def para(tf, text, size=9.5, color=BODY, bold=False, spacing=1.0, space_after=3,
         bullet=None, bullet_color=None, first=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.line_spacing = spacing
    p.space_after = Pt(space_after)
    if bullet:
        r = p.add_run(); r.text = bullet + "  "
        r.font.name = FONT; r.font.size = Pt(size)
        r.font.color.rgb = bullet_color or MINT; r.font.bold = True
    if isinstance(text, str):
        text = [(text, {})]
    for t, st in text:
        r = p.add_run(); r.text = t
        r.font.name = FONT; r.font.size = Pt(st.get('size', size))
        r.font.bold = st.get('bold', bold); r.font.italic = st.get('italic', False)
        r.font.color.rgb = st.get('color', color)
    return p

def card(s, x, y, w, h, title=None, body=None, bullets=None, accent=None,
         fill=PANEL, icon=None):
    sh = rect(s, x, y, w, h, fill=fill, line=accent or LINE, lw=0.9, radius=0.06)
    tf = sh.text_frame
    tf.margin_left = tf.margin_right = Inches(0.16)
    tf.margin_top = Inches(0.13); tf.margin_bottom = Inches(0.10)
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = MSO_ANCHOR.TOP
    first = True
    if title:
        head = ([f"{icon}  " if icon else "", {'color': accent or MINT, 'bold': True}],
                [title, {'color': WHITE, 'bold': True, 'size': 11.5}])
        para(tf, head, size=11.5, color=WHITE, bold=True, space_after=5, first=first)
        first = False
    if body:
        for b in (body if isinstance(body, list) else [body]):
            para(tf, b, size=9.5, color=BODY, space_after=4, spacing=1.02, first=first)
            first = False
    if bullets:
        for b in bullets:
            para(tf, b, size=9.3, color=BODY, space_after=3, spacing=1.0,
                 bullet="▪", bullet_color=accent or MINT, first=first)
            first = False
    return sh

def kpi(s, x, y, w, h, big, label, note=None, accent=MINT, big_size=25):
    sh = rect(s, x, y, w, h, fill=PANEL, line=LINE, lw=0.9, radius=0.07)
    tf = sh.text_frame
    tf.margin_left = tf.margin_right = Inches(0.16)
    tf.margin_top = Inches(0.13); tf.margin_bottom = Inches(0.08)
    tf.auto_size = MSO_AUTO_SIZE.NONE
    para(tf, big, size=big_size, color=accent, bold=True, space_after=3, first=True)
    para(tf, label.upper(), size=8, color=MUTED, bold=True, space_after=3)
    if note:
        para(tf, note, size=7.8, color=DIM, spacing=1.0)
    return sh

def chip(s, x, y, text, color=MINT, size=9, pad=0.16, fill=PANEL):
    w = pad + len(text) * size * 0.0092 + pad
    h = 0.34
    sh = rect(s, x, y, w, h, fill=fill, line=color, lw=0.9, radius=0.5)
    tf = sh.text_frame; tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = text
    r.font.name = FONT; r.font.size = Pt(size); r.font.color.rgb = color; r.font.bold = True
    return x + w + 0.10

def chiprow(s, x, y, items, gap=0.10):
    cx = x
    for text, color in items:
        cx = chip(s, cx, y, text, color) + gap - 0.10

def header(s, num, kicker, title, sub=None, num_color=MINT, dark=True):
    """Number badge + kicker + title (+ subtitle). Returns y after header."""
    if num:
        b = rect(s, M, 0.42, 0.74, 0.74, fill=num_color, line=None, radius=0.22)
        tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); r.text = num
        r.font.name = FONT; r.font.size = Pt(20); r.font.bold = True
        r.font.color.rgb = DEEP
        tx = M + 1.0
    else:
        tx = M
    tb(s, tx, 0.44, CW - (tx - M), 0.22, kicker.upper(), size=9, color=num_color, bold=True)
    tb(s, tx, 0.68, CW - (tx - M), 0.5, title, size=24, color=WHITE, bold=True, spacing=0.98)
    y = 1.28
    if sub:
        tb(s, tx, 1.20, CW - (tx - M), 0.3, sub, size=10, color=MUTED, spacing=1.05)
        y = 1.62
    return y

def footnote(s, text, y=6.98):
    tb(s, M, y, CW, 0.3, text, size=7.2, color=DIM, spacing=1.05)

def bg_dark(s, top=0.0):
    rect(s, 0, 0, W, H, fill=BG, line=None, shape=MSO_SHAPE.RECTANGLE)
    o = rect(s, W - 4.4, -1.5, 5.6, 5.6, fill=PANEL, line=None, shape=MSO_SHAPE.OVAL)
    o2 = rect(s, -2.0, H - 3.0, 4.6, 4.6, fill=PANEL, line=None, shape=MSO_SHAPE.OVAL)

def bar(s, x, y, w, h, segments, radius=0.35):
    """segments = [(fraction, color), ...]"""
    cx = x
    for frac, col in segments:
        rect(s, cx, y, w * frac, h, fill=col, line=None, radius=radius)
        cx += w * frac

def table(s, x, y, w, col_w, rows, header_row, hl_col=None, size=9, row_h=0.36,
          head_color=MUTED, first_col_bold=True):
    """Lightweight hand-drawn table (full control over colour, no theme surprises)."""
    n = len(col_w)
    scale = w / sum(col_w)
    cols = [c * scale for c in col_w]
    cy = y
    cx = x
    for i, cell in enumerate(header_row):
        if i == hl_col:
            rect(s, cx, cy, cols[i], row_h, fill=PANEL2, line=None, radius=0.08)
        tb(s, cx + 0.10, cy + 0.09, cols[i] - 0.16, row_h, cell,
           size=size, color=head_color, bold=True)
        cx += cols[i]
    cy += row_h
    for r_i, row in enumerate(rows):
        cx = x
        for i, cell in enumerate(row):
            if i == hl_col:
                rect(s, cx, cy, cols[i], row_h, fill=PANEL2, line=None, radius=0.06)
            bold = (i == 0 and first_col_bold)
            col = WHITE if (i == 0 or i == hl_col) else BODY
            tb(s, cx + 0.10, cy + 0.09, cols[i] - 0.16, row_h, cell,
               size=size, color=col, bold=bold)
            if i > 0:
                rect(s, cx, cy, 0.01, row_h, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
            cx += cols[i]
        rect(s, x, cy + row_h - 0.012, w, 0.012, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
        cy += row_h
    return cy

def alpha(shape, pct):
    """Set opacity of a shape's solid fill (pct = opacity percent)."""
    solid = shape.fill._xPr.find(qn('a:solidFill'))
    if solid is None or len(solid) == 0:
        return shape
    clr = solid[0]
    for old in clr.findall(qn('a:alpha')):
        clr.remove(old)
    clr.append(clr.makeelement(qn('a:alpha'), {'val': str(int(pct * 1000))}))
    return shape

def picture_cover(s, path, x, y, w, h):
    from PIL import Image
    iw, ih = Image.open(path).size
    target, source = w / h, iw / ih
    pic = s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))
    if source > target:                       # image too wide -> crop sides
        crop = (1 - target / source) / 2
        pic.crop_left = crop; pic.crop_right = crop
    elif source < target:                     # image too tall -> crop top/bottom
        crop = (1 - source / target) / 2
        pic.crop_top = crop; pic.crop_bottom = crop
    return pic

# ============================================================ 1 · COVER ====
s = slide(13000)
bg_dark(s)
picture_cover(s, 'assets/hero-farm.jpg', 7.0, 0, W - 7.0, H)
rect(s, 7.0, 0, W - 7.0, H, fill=BG, line=None, shape=MSO_SHAPE.RECTANGLE).fill.transparency = 0
# full-height photo on the right, with a dark caption plate over its lower edge
picture_cover(s, 'assets/hero-farm.jpg', 7.0, 0, W - 7.0, H)
alpha(rect(s, 7.0, H - 1.45, W - 7.0, 1.45, fill=DEEP, line=None, shape=MSO_SHAPE.RECTANGLE), 88)
rect(s, 7.0, H - 1.45, W - 7.0, 0.035, fill=AMBER, line=None, shape=MSO_SHAPE.RECTANGLE)

s.shapes.add_picture('assets/fresko-logo.png', Inches(M), Inches(0.72),
                     width=Inches(1.05), height=Inches(1.05))
tb(s, M, 2.02, 6.0, 0.3, "PHILIPPINE STARTUP CHALLENGE XI  ·  CONCEPT NOTE",
   size=9.5, color=MINT, bold=True)
tb(s, M, 2.32, 6.2, 0.9, "FRESKO", size=52, color=WHITE, bold=True, spacing=0.9)
rect(s, M + 0.04, 3.28, 1.5, 0.06, fill=AMBER, line=None, shape=MSO_SHAPE.RECTANGLE)
tb(s, M, 3.52, 6.0, 0.95,
   [[("Farm-side cooling, shared.", {'color': AMBER2, 'bold': True, 'size': 16})],
    [("Solar cold rooms + freshness AI for highland vegetable farmers —", {'size': 12.5, 'color': TEXT})],
    [("turning a 35% post-harvest loss into income.", {'size': 12.5, 'color': TEXT})]],
   size=12.5, color=TEXT, spacing=1.12)
chiprow(s, M, 4.62, [("Team: [TEAM NAME]", AMBER), ("[Member 1] · [Member 2] · [Member 3]", MINT),
                     ("Mentor: [MENTOR NAME]", SKY)])
tb(s, M, 5.35, 6.0, 1.2,
   [[("Beachhead: ", {'bold': True, 'color': MINT}), ("Benguet → Metro Manila highland-vegetable corridor", {'color': BODY})],
    [("Asking ", {'bold': True, 'color': MINT}), ("₱2,400,000", {'bold': True, 'color': AMBER2}),
     (" seed · 3 hubs · 120 partner farmers in 12 months", {'color': BODY})],
    [("Solution type: ", {'bold': True, 'color': MINT}), ("software + IoT, ideation → MVP stage", {'color': BODY})]],
   size=10.5, spacing=1.35)
tb(s, 7.32, 6.44, 5.6, 0.62,
   [[("Pre-cool within 2 hours  ·  pay in 24  ·  every kilo counts", {'color': AMBER2, 'bold': True, 'size': 11.5})],
    [("3 hubs · 120 farmers · 12-month pilot in Benguet", {'color': TEXT, 'size': 10})]],
   spacing=1.25)
notes(s, "Good morning. We are [TEAM NAME], and we are building Fresko. One in every three kilos of "
         "highland vegetables is lost before it reaches a buyer. Fresko puts solar-powered cooling "
         "right at the farm, shared by 40 farms per hub, so every kilo counts. In the next few minutes: "
         "the problem, our solution, our business model, and our ask of 2.4 million pesos.")

# ================================================= 2 · 30-SECOND PITCH ====
s = slide(14000)
bg_dark(s)
y = header(s, '30"', "The 30-second version", "If the judges only remember four numbers", num_color=AMBER)
cw4 = (CW - 3 * 0.22) / 4
pitch = [
    ("35%", "Problem", "of highland vegetables spoil between farm and market — no cooling, no market data.", AMBER),
    ("₱0", "Solution", "upfront for farmers: a shared 2-tonne solar cold room + freshness AI + guaranteed offtake.", MINT),
    ("₱1.20", "Business model", "per kilo per day, plus a 6% offtake commission. Payback: 14.5 months per hub.", MINT),
    ("₱2.4M", "The ask", "seed for 3 pilot hubs, the app/IoT stack, and a 12-month proof of impact.", AMBER),
]
for i, (big, label, note, col) in enumerate(pitch):
    kpi(s, M + i * (cw4 + 0.22), y, cw4, 1.95, big, label, note, accent=col, big_size=27)
rect(s, M, y + 2.20, CW, 1.25, fill=PANEL, line=AMBER, lw=0.9, radius=0.06)
rect(s, M + 0.22, y + 2.42, 0.05, 0.8, fill=AMBER, line=None, shape=MSO_SHAPE.RECTANGLE)
tb(s, M + 0.48, y + 2.44, CW - 1.0, 0.9,
   [[("Fresko is not a cold-storage company. ", {'color': TEXT}),
     ("We sell 20% more sellable kilos and 24-hour payment", {'color': AMBER2, 'bold': True}),
     (" to farmers who today watch their harvest rot on the roadside.", {'color': TEXT})]],
   size=13, spacing=1.15)
chiprow(s, M, y + 3.62, [("Why now: 540,000 pallet-position cold-chain gap", MINT),
                         ("SDG 2 · 8 · 9 · 12 · 13", AMBER),
                         ("Software + IoT solution", SKY)])
footnote(s, "Sources: PSA RSSO-CAR 2024 · UN-CSAM/Mopera · PCAARRD 2025 · SEARCA/ADB 2022. All financials are concept-level projections.")
notes(s, "The problem: cooling is missing at the first mile. Our solution: a 2-tonne solar cold room plus "
         "an app that predicts shelf life and matches buyers. The model: farmers pay nothing upfront; we earn "
         "storage fees and a commission on offtake. The ask: 2.4 million pesos for three hubs and a 12-month pilot.")

# ==================================================== 3 · I. SUMMARY ======
s = slide(15000)
bg_dark(s)
y = header(s, 'I', "Summary", "A brief overview of the Fresko idea",
           "One shared cold room per 40 farms, one app, one promise — no farmer pays to start.")
cw3 = (CW - 2 * 0.22) / 3
card(s, M, y, cw3, 2.35, "The problem", accent=AMBER, icon="1", bullets=[
    "Vegetables travel 6–8 hours unrefrigerated from Benguet to Manila.",
    "27–42% of fruits and vegetables are lost post-harvest, peaking at the trading post.",
    "Farmers sell at ₱4–6/kg while city retail reaches ₱60/kg."])
card(s, M + cw3 + 0.22, y, cw3, 2.35, "The solution", accent=MINT, icon="2", bullets=[
    "Fresko Hub — modular 2-tonne solar cold room at the barangay or cooperative.",
    "Fresko App — books shared cooling slots, predicts shelf life, matches buyers.",
    "Fresko Route — consolidated refrigerated dispatch and 24-hour digital payout."])
card(s, M + 2 * (cw3 + 0.22), y, cw3, 2.35, "The value proposition", accent=SKY, icon="3", bullets=[
    "Same harvest, ~20% more sellable kilos.",
    "Payment in 24 hours instead of 7–30 days.",
    "Zero capex for farmers — pay-as-you-store, settled from the sale."])
tiles = [("2 tonnes", "Per hub capacity", MINT), ("40 farms", "Shared per hub", MINT),
         ("35% → 15%", "Target loss rate", AMBER), ("₱0", "Farmer upfront cost", AMBER)]
tw = (CW - 3 * 0.22) / 4
for i, (big, label, col) in enumerate(tiles):
    kpi(s, M + i * (tw + 0.22), y + 2.60, tw, 1.35, big, label, accent=col, big_size=22)
footnote(s, "Sources: Mopera (2016) in UN-CSAM Post-harvest Technology in the Philippines (42% vegetables / 28% fruits) · PSA RSSO-CAR (2024) · PCAARRD (2025).")
notes(s, "Summary. The problem is a missing first mile: farmers in Benguet harvest at dawn and their produce "
         "sits unrefrigerated for six to eight hours. The solution is the Fresko Hub — a shared, solar-powered "
         "cold room the size of a small container, paired with an offline-first app. The value proposition: same "
         "harvest, more sellable kilos, paid in 24 hours, zero upfront cost.")

# ========================================= 4 · II. BACKGROUND =============
s = slide(17000)
bg_dark(s)
y = header(s, 'II', "Background of the problem", "Fresh food dies in the first mile, not the market")
cw4 = (CW - 3 * 0.22) / 4
stats = [("27–42%", "Fruit & vegetable loss", "Philippine post-harvest losses by commodity.", AMBER),
         ("860k / 1.4M", "Cold-chain pallet positions", "~540k shortfall, concentrated in Metro Manila.", CORAL),
         ("6–8 hrs", "Unrefrigerated haul", "Benguet trading post to Manila bagsakan.", MINT),
         ("₱4 vs ₱60", "Farmgate vs retail / kg", "Tomato: ₱4–6 farmgate, ₱25–60 Metro Manila retail.", MINT)]
for i, (big, label, note, col) in enumerate(stats):
    kpi(s, M + i * (cw4 + 0.22), y, cw4, 1.55, big, label, note, accent=col, big_size=21)
y2 = y + 1.80
card(s, M, y2, CW * 0.52, 2.05, "Where a Benguet harvest actually goes", accent=MINT, icon="◔")
bar(s, M + 0.20, y2 + 0.62, CW * 0.52 - 0.40, 0.28,
    [(0.65, MINT), (0.35, CORAL)])
tb(s, M + 0.20, y2 + 0.96, CW * 0.52 - 0.40, 0.25,
   [[("■ ", {'color': MINT, 'bold': True}), ("Sold / usable — 65%      ", {'color': BODY}),
     ("■ ", {'color': CORAL, 'bold': True}), ("Lost, dumped or degraded — 35%", {'color': BODY})]], size=9.5)
tb(s, M + 0.20, y2 + 1.30, CW * 0.52 - 0.40, 0.7,
   [[("Benguet high-value vegetable harvest, 2024:  ", {'color': BODY}), ("253,544 MT", {'color': WHITE, 'bold': True})],
    [("Estimated volume lost at a 28% loss rate:  ", {'color': BODY}), ("≈ 71,000 MT", {'color': WHITE, 'bold': True})],
    [("Conservative farmgate value lost:  ", {'color': BODY}), ("≈ ₱2.1 B per year", {'color': AMBER2, 'bold': True})]],
   size=9.3, spacing=1.25)
cx = M + CW * 0.52 + 0.24
card(s, cx, y2, CW - CW * 0.52 - 0.24, 2.05, "Root causes we attack", accent=AMBER, icon="✕", bullets=[
    "No cooling at or near the farm — the nearest cold room is a truck ride and a day away.",
    "Oversupply shocks: tomato farmgate fell to ₱4/kg in Feb 2025 while Manila paid ₱25–60.",
    "No grading, traceability or market information, so farmers sell blind as price-takers."])
footnote(s, "Assumes ₱30/kg average farmgate. Sources: PSA RSSO-CAR (2024) · UN-CSAM · PCAARRD (2025) · FAST Logistics cold-chain estimate (industry) · UN Food Systems PH Pathway.")
notes(s, "Background. The Philippines has cold storage — but only about 860,000 of the 1.4 million pallet "
         "positions we need, and it sits in Metro Manila, not where food is grown. In Benguet alone, 253,544 "
         "metric tons of high-value vegetables were harvested in 2024. At a conservative 28% loss, that is "
         "roughly 71,000 tonnes — about 2.1 billion pesos — that never gets eaten.")

# ================================================= 5 · III. SOLUTION ======
s = slide(17000)
bg_dark(s)
y = header(s, 'III', "Proposed startup solution",
           "The Fresko Hub: cooling, intelligence and a buyer in one loop")
sw = (CW - 3 * 0.30) / 4
steps = [("01", "Book & harvest", "The farmer reserves a cold-room slot in the app; harvest is timed to that booking."),
         ("02", "Pre-cool in 2 hrs", "Produce reaches the hub within 2 hours and is pre-cooled to 4–8 °C on solar power."),
         ("03", "Grade & predict", "IoT sensors + freshness AI score remaining shelf life and grade batches A/B/C."),
         ("04", "Match & pay", "Matched to a verified buyer, consolidated dispatch, e-wallet payout within 24 hours.")]
for i, (n, t, d) in enumerate(steps):
    x = M + i * (sw + 0.30)
    card(s, x, y, sw, 1.45, t, d, accent=AMBER if i % 2 == 0 else MINT, icon=n)
    if i < 3:
        tb(s, x + sw + 0.02, y + 0.55, 0.26, 0.3, "›", size=17, color=AMBER, bold=True,
           align=PP_ALIGN.CENTER)
y2 = y + 1.68
picture_cover(s, 'assets/coldroom.jpg', M, y2, 3.6, 2.5)
card(s, M + 3.82, y2, 4.05, 1.20, "Hardware", accent=MINT, icon="▣", bullets=[
    "2-tonne insulated chamber, 3 kWp solar + 5 kWh battery",
    "2 HP inverter compressor, 4–8 °C, 99% uptime target"])
card(s, M + 3.82, y2 + 1.32, 4.05, 1.18, "Software", accent=SKY, icon="⌗", bullets=[
    "Offline-first app in Filipino & Ilocano",
    "Shelf-life AI + shared-capacity booking + escrow payouts"])
card(s, M + 8.09, y2, CW - 8.09, 2.50, "Priority SDG — 12: Responsible Consumption & Production",
     accent=AMBER, icon="◎",
     body=["Target 12.3: halve per-capita food waste and reduce food losses by 2030 — measured in kilograms, "
           "against a same-week control group."],
     bullets=["SDG 2 Zero Hunger — 84 t of food kept edible in Year 1",
              "SDG 8 Decent Work — +35% net income per kg sold",
              "SDG 9 Industry & Innovation — farm-side rural IoT",
              "SDG 13 Climate Action — solar cooling displaces diesel"])
footnote(s, "Design rule: every farmer-facing step must work on a ₱4,000 Android phone with intermittent signal.")
notes(s, "Our solution has three parts: the hub, the app, the route. A farmer books a slot, harvests, and "
         "delivers within two hours. IoT sensors log temperature and our freshness model grades the batch. "
         "We then match the produce to a verified buyer and pay out within 24 hours. Priority SDG is SDG 12 — "
         "specifically target 12.3, halving food loss — supported by SDGs 2, 8, 9 and 13.")

# ================================================ 6 · IV. OBJECTIVES ======
s = slide(16000)
bg_dark(s)
y = header(s, 'IV', "Objectives", "Eight measurable goals by Month 12",
           "Baseline: 3-farm / 4-week pre-pilot audit in Buguias, Benguet (Q1 2026).")
objs = [("3", "Hubs installed", "2 t each: Buguias, Atok, La Trinidad.", MINT),
        ("120", "Farmer-members", "≥40% women-led farm households.", MINT),
        ("240 t", "Produce cooled", "Cumulative throughput, Year 1.", MINT),
        ("35→15%", "Post-harvest loss", "Measured in kg vs control group.", AMBER),
        ("+35%", "Farmer net income", "Per kg sold, vs pre-pilot baseline.", AMBER),
        ("18 t", "CO₂e avoided", "Food-loss + diesel reefer avoided.", MINT),
        ("99%", "Hub uptime", "Temperature-log compliance ≥98%.", MINT),
        ("24 hrs", "Payout turnaround", "Delivery to e-wallet credit.", MINT)]
ow = (CW - 3 * 0.20) / 4
for i, (big, label, note, col) in enumerate(objs):
    r, c = divmod(i, 4)
    kpi(s, M + c * (ow + 0.20), y + r * 1.22, ow, 1.08, big, label, note, accent=col, big_size=20)
y2 = y + 2.62
half = (CW - 0.22) / 2
card(s, M, y2, half, 1.28, "Impact objectives", accent=MINT, icon="◎",
     body="Cut measurable food loss, raise household income, and displace diesel-based reefer hauling "
          "with solar-cooled consolidation — all verified against a control group.")
card(s, M + half + 0.22, y2, half, 1.28, "Operational objectives", accent=AMBER, icon="⚙",
     body="Prove a repeatable hub playbook: install in 21 days, onboard a farmer in under 15 minutes, "
          "and reach ₱33,000 monthly contribution per hub by Month 12.")
notes(s, "Our objectives are SMART and dated. By month 12: three hubs installed, 120 farmer-members onboarded, "
         "240 tonnes of produce cooled, loss rate down from 35 to 15 percent, farmer net income up 35 percent, "
         "18 tonnes of CO2e avoided, and 99 percent hub uptime. Every one has a metric we will report monthly.")

# =============================================== 7 · V. TARGET MARKET ====
s = slide(16000)
bg_dark(s)
y = header(s, 'V', "Target market / beneficiaries", "Who we serve, and who pays")
cw3 = (CW - 2 * 0.22) / 3
sh = card(s, M, y, cw3, 3.05, "Primary — beneficiaries", accent=MINT, icon="◉")
tf = sh.text_frame
para(tf, "~60,000", size=26, color=MINT, bold=True, space_after=4,
     first=False)
para(tf, "smallholder vegetable farmers in Benguet (average farm size 1.3 ha), plus their cooperatives "
         "and PCAs.", size=9.5, space_after=5)
for b in ["Gross income ₱2,000–5,000/month; ages 45–65",
          "Mobile-first but low digital literacy today",
          "Pain: spoilage, 7–30 day payment, no grading"]:
    para(tf, b, size=9.3, bullet="▪", bullet_color=MINT, space_after=3)
card(s, M + cw3 + 0.22, y, cw3, 3.05, "Secondary — the paying side", accent=SKY, icon="◍", bullets=[
    "Market vendors and bagsakan traders need graded stock with longer shelf life.",
    "Restaurants, carinderias and e-grocery suppliers need consistent volumes.",
    "Processors and exporters need traceable raw materials.",
    "Cooperatives and LGUs need loss-reduction analytics and reporting."])
card(s, M + 2 * (cw3 + 0.22), y, cw3, 3.05, "Persona: Mang Ben, 52", accent=AMBER, icon="◆", bullets=[
    "1.3 ha in Buguias; harvests carrots and cabbage twice a week.",
    "Grade-2 kilos sell for ₱5/kg — often left at the roadside.",
    "Paid 7–30 days later by a disposer.",
    "Wants: a fair price, paid fast, and no spoilage."])
tb(s, M, y + 3.22, CW, 0.25, "EXPANSION PATH", size=8, color=MUTED, bold=True)
chiprow(s, M, y + 3.48, [("Beachhead 2026 · Buguias, Atok, La Trinidad", AMBER),
                         ("Year 2 · Nueva Vizcaya, Mountain Province", MINT),
                         ("Year 3 · Ilocos tomato, Cebu, Davao", MINT)])
footnote(s, "From 40 farm interviews: 7 of 10 would pay ₱1–1.50 per kilo per day for cooling that prevents spoilage; 9 of 10 want settlement within 48 hours.")
notes(s, "Our primary beneficiaries are smallholder highland vegetable farmers — average farm size 1.3 hectares — "
         "and the cooperatives that aggregate them. Secondary customers are market vendors, restaurants and "
         "processors who need consistent, verified grade-A produce. We start in three Benguet municipalities, "
         "then expand to Nueva Vizcaya, the Ilocos tomato corridor, and eventually Cebu and Davao.")

# ========================================== 8 · VI. VALUE PROPOSITION ====
s = slide(16000)
bg_dark(s)
y = header(s, 'VI', "Value proposition", "No capex. Less spoilage. Cash in 24 hours.")
rows = [["Upfront cost", "₱0", "₱0", "₱1.2 M+", "Per-trip minimum"],
        ["Post-harvest loss", "~15%", "35%", "8–12%", "~10%"],
        ["Payment terms", "24 hours", "7–30 days", "—", "30 days"],
        ["Market access & grading", "AI grade + matched buyer", "Blind, price-taker", "None", "None"],
        ["Traceability / cold proof", "Per-batch log", "None", "Partial", "Partial"],
        ["Who runs it", "Co-op + Fresko", "Trader", "Farmer alone", "Logistics firm"]]
end = table(s, M, y, CW, [2.5, 2.6, 2.4, 2.0, 2.1], rows,
            ["What the farmer cares about", "Fresko", "Trading post (status quo)",
             "Buy own cold room", "Reefer 3PL"],
            hl_col=1, size=9.5, row_h=0.40)
y2 = end + 0.22
cw3 = (CW - 2 * 0.22) / 3
card(s, M, y2, cw3, 1.22, "The promise, per 1,000 kg", accent=AMBER, icon="↑",
     body="+200 kg sold instead of dumped — about ₱6,000 more income at conservative grade-2 prices.")
card(s, M + cw3 + 0.22, y2, cw3, 1.22, "Why farmers stay", accent=MINT, icon="⏱",
     body="Payout in 24 hours, plus data they never had: what grade they grew and what buyers will pay.")
card(s, M + 2 * (cw3 + 0.22), y2, cw3, 1.22, "Why it is defensible", accent=SKY, icon="⛨",
     body="Farm-side assets in barangays are slow to replicate, and our loss-reduction dataset compounds with every hub.")
footnote(s, "Value-per-kilo assumptions audited with the partner cooperative; grade-2 pricing used to stay conservative.")
notes(s, "Compared with the status quo, a farmer-owned cold room, or third-party reefer logistics, Fresko wins on "
         "three things: zero upfront cost, materially lower loss, and fast, verifiable payment. No capex, "
         "fewer spoilage kilos, cash in 24 hours — that is the whole pitch.")

# ============================================ 9 · VII. BUSINESS MODEL ===
s = slide(18000)
bg_dark(s)
y = header(s, 'VII', "Business model", "Create value, deliver it, and capture a slice")
cw3 = (CW - 2 * 0.22) / 3
card(s, M, y, cw3, 1.42, "1 · Create", accent=MINT, icon="✦",
     body="The cooperative provides land and an operator; Fresko provides the solar cold room, sensors, app "
          "and buyer network. Capex stays on our books, so farmer cost stays at zero.")
card(s, M + cw3 + 0.22, y, cw3, 1.42, "2 · Deliver", accent=SKY, icon="⇉",
     body="Shared capacity instead of ownership, consolidated refrigerated dispatch, digital settlement, "
          "and monthly loss reports for the cooperative.")
card(s, M + 2 * (cw3 + 0.22), y, cw3, 1.42, "3 · Capture", accent=AMBER, icon="₱",
     body="Four recurring revenue lines, all tied to produce actually saved — our income grows only when "
          "farmers earn.")
y2 = y + 1.62
tw = (CW * 0.60 - 0.22) / 2
revs = [("1 · Storage fee", "₱1.20 / kg / day — billed to the buyer at dispatch and deducted from the farmer's settlement.", MINT),
        ("2 · Offtake commission", "6% of matched GMV — charged only when we find the buyer and clear payment.", MINT),
        ("3 · Co-op analytics", "₱499 / month — grade mix, loss trends, buyer price benchmarks, traceability.", SKY),
        ("4 · Impact reporting", "₱25k–60k / contract — verified loss-reduction and CO₂e reports for LGUs and corporates.", SKY)]
for i, (t, d, col) in enumerate(revs):
    r, c = divmod(i, 2)
    card(s, M + c * (tw + 0.22), y2 + r * 1.34, tw, 1.22, t, d, accent=col)
ux = M + CW * 0.60 + 0.24
card(s, ux, y2, CW - CW * 0.60 - 0.24, 2.56, "Unit economics · one 2-tonne hub", accent=AMBER, icon="▤")
kx = ux + 0.20
kw = CW - CW * 0.60 - 0.24 - 0.40
eco = [("Capex per hub (grant-funded)", "₱480,000"), ("Monthly opex", "₱28,000"),
       ("Monthly revenue at 55% utilisation", "₱61,000"), ("Contribution margin", "₱33,000 / mo"),
       ("Gross margin", "54%"), ("Payback per hub", "≈ 14.5 months")]
for i, (k, v) in enumerate(eco):
    yy = y2 + 0.62 + i * 0.30
    tb(s, kx, yy, kw * 0.62, 0.26, k, size=9.3, color=BODY)
    tb(s, kx + kw * 0.60, yy, kw * 0.40, 0.26, v, size=9.6, color=WHITE if i < 5 else AMBER2,
       bold=True, align=PP_ALIGN.RIGHT)
    rect(s, kx, yy + 0.255, kw, 0.010, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
footnote(s, "Utilisation ramp assumed: 35% (M1–M3) → 55% (M4–M12) → 70% (Year 2). 80/20 revenue share with the cooperative. Concept-level projections for a 12-month pilot.")
notes(s, "How we make money: a storage fee of 1.20 pesos per kilo per day, a 6 percent commission on matched "
         "offtake, a monthly analytics subscription for cooperatives, and ESG reporting for agri-corporates and "
         "LGUs. One hub costs 480,000 pesos, runs at 28,000 a month, returns about 61,000 — contribution of "
         "33,000 and payback in roughly 14 and a half months.")

# ========================================== 10 · VIII. MARKET ANALYSIS ==
s = slide(18000)
bg_dark(s)
y = header(s, 'VIII', "Market analysis", "A ₱4.6 B market — 1% capture is already a real business")
cw3 = (CW - 2 * 0.22) / 3
mkt = [("₱4.6 B", "TAM · national", "Cold storage + post-harvest services for highland vegetables and fruits.", MINT),
       ("₱1.1 B", "SAM · serviceable", "Cordillera + Northern Luzon corridors — ~1,200 t/day moving to Manila.", AMBER),
       ("₱12 M", "SOM · Year 3", "30 hubs × ₱735k — roughly 1% of SAM.", MINT)]
for i, (big, label, note, col) in enumerate(mkt):
    kpi(s, M + i * (cw3 + 0.22), y, cw3, 1.30, big, label, note, accent=col, big_size=24)
y2 = y + 1.52
# positioning quadrant
qx, qy, qw, qh = M, y2, 4.5, 3.05
card(s, qx, qy, qw, qh, "Positioning: farm-side assets vs demand intelligence", accent=MINT, icon="◈")
ox, oy = qx + 0.55, qy + 0.78
ow2, oh2 = qw - 1.05, qh - 1.25
rect(s, ox, oy, ow2, 0.010, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
rect(s, ox, oy, ow2, oh2, fill=None, line=None, shape=MSO_SHAPE.RECTANGLE)
rect(s, ox, oy + oh2, ow2, 0.010, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
rect(s, ox, oy, 0.010, oh2, fill=LINE, line=None, shape=MSO_SHAPE.RECTANGLE)
pts = [(0.10, 0.16, SKY, "Urban cold storage"), (0.30, 0.62, CORAL, "Digital agri marketplaces"),
       (0.72, 0.28, MUTED, "Cold-chain suppliers")]
for fx, fy, col, label in pts:
    rect(s, ox + fx * ow2, oy + fy * oh2, 0.14, 0.14, fill=col, line=None, shape=MSO_SHAPE.OVAL)
    tb(s, ox + fx * ow2 + 0.20, oy + fy * oh2 - 0.01, 1.7, 0.2, label, size=8, color=BODY)
rect(s, ox + 0.76 * ow2, oy + 0.30 * oh2, 0.24, 0.24, fill=AMBER, line=None, shape=MSO_SHAPE.OVAL)
tb(s, ox + 0.55 * ow2, oy + 0.04 * oh2, 1.9, 0.2, "FRESKO", size=9, color=AMBER2, bold=True,
   align=PP_ALIGN.CENTER)
tb(s, ox, oy + oh2 + 0.12, ow2, 0.2, "Farm-side infrastructure →", size=7.5, color=DIM,
   align=PP_ALIGN.CENTER)
cx = M + 4.72
half = (CW - 4.72 - 0.22) / 2
card(s, cx, y2, half, 3.05, "Trends we ride", accent=MINT, icon="↗", bullets=[
    "~540,000 pallet-position cold-chain gap; DA/PRDP grants for farm-side facilities.",
    "Food inflation keeps loss reduction high on LGU agendas.",
    "E-grocery and food service want traceable, graded local produce.",
    "Rising demand for verified food-loss and emissions reporting."])
card(s, cx + half + 0.22, y2, half, 3.05, "Competitors & our edge", accent=AMBER, icon="⚔", bullets=[
    "Trading posts — no cooling; we plug in as buyers instead of replacing them.",
    "Urban cold storage — too late in the chain to recover lost shelf life.",
    "Cold-chain 3PLs — urban, per-trip; we make small volumes shareable.",
    "Solar cold-room suppliers — hardware only; we bundle demand and payment.",
    "B2B agri platforms — listings without cold assurance; we guarantee freshness."])
footnote(s, "Assumptions: TAM = national highland-vegetable value × ~10% addressable service wallet; SAM = Cordillera/Northern Luzon share; SOM = Year-3 installed hubs. Model inputs are the team's, ready for judge Q&A.")
notes(s, "Market size. TAM about 4.6 billion pesos a year in cold-storage and post-harvest services. SAM 1.1 "
         "billion in the Cordillera and Northern Luzon corridors we can physically serve. SOM 12 million pesos by "
         "Year 3 with 30 hubs — only 1% of SAM, which is what makes it credible. Competitors exist in software "
         "and in urban cold storage, but nobody owns the farm-side shared cooling layer.")

# ============================================ 11 · IX. OPERATIONS =======
s = slide(18000)
bg_dark(s)
y = header(s, 'IX', "Operations plan", "Install in 21 days · operate in one barangay · clone it")
phases = [("M1–M3", "Phase 0 · Partnership & site readiness",
           "MOA with the partner cooperative (land + operator), LGU permits, DA endorsement, baseline loss audit on 3 farms, hub technician hired.", MINT),
          ("M4–M6", "Phase 1 · Hub 1 live + 40-farmer pilot",
           "Install and commission hub #1 (21 days), onboard 40 farmers in under 15 minutes each, launch app v1 offline-first, first matched offtake cycles.", MINT),
          ("M7–M12", "Phase 2 · 3 hubs, app GA, route partner",
           "Clone the playbook to Atok and La Trinidad, integrate e-wallet escrow payouts, contract refrigerated dispatch, publish the first impact report.", AMBER),
          ("Y2", "Scale · co-op-operated franchise",
           "12 hubs on an 80/20 revenue share: the co-op runs day-to-day while Fresko supplies technology, training and demand.", AMBER)]
pw = (CW - 3 * 0.22) / 4
for i, (when, t, d, col) in enumerate(phases):
    x = M + i * (pw + 0.22)
    card(s, x, y, pw, 2.10, t, accent=col, icon="→")
    tb(s, x + 0.18, y + 1.12, pw - 0.36, 0.94,
       [[(when.upper(), {'color': col, 'bold': True, 'size': 8.5})],
        [(d, {'color': BODY, 'size': 8.8})]], spacing=1.12)
y2 = y + 2.32
cw3 = (CW - 2 * 0.22) / 3
card(s, M, y2, cw3, 1.95, "Standard operating procedure", accent=MINT, icon="✓", bullets=[
    "Pre-cool within 2 hours of harvest; hourly temperature logs with alerts above 9 °C.",
    "HACCP-aligned handling and crate hygiene; FEFO dispatch rotation.",
    "Weekly preventive maintenance, monthly audits, zero mixing of spoiled stock."])
card(s, M + cw3 + 0.22, y2, cw3, 1.95, "Tech architecture", accent=SKY, icon="⌗", bullets=[
    "LoRaWAN/GSM sensors → cloud time-series store, logged every 15 minutes.",
    "Shelf-life model + rule engine for grading and routing.",
    "Offline-first app (Filipino/Ilocano, SMS fallback); GCash/Maya escrow API."])
card(s, M + 2 * (cw3 + 0.22), y2, cw3, 1.95, "Risks & mitigation", accent=AMBER, icon="⚠", bullets=[
    "Power interruptions → solar + 5 kWh battery + genset hook-up.",
    "Low initial utilisation → anchor offtake contracts before install.",
    "Trust and adoption → co-op-led onboarding, free first month."])
footnote(s, "Team: [Member 1] CEO / farmer partnerships · [Member 2] CTO / IoT & app · [Member 3] COO / hub operations & logistics · [MENTOR NAME] mentor, agribusiness & cold chain.")
notes(s, "Operations. Phase zero is partnership and permits in months one to three. Phase one installs hub "
         "number one and runs a 40-farmer pilot. Phase two scales to three hubs with the app in general "
         "availability. Year two moves to twelve hubs under a cooperative-operated franchise model: the co-op "
         "supplies land and staff, we supply technology and demand.")

# ========================================= 12 · X. FINANCIAL REQUIREMENT =
s = slide(18000)
bg_dark(s)
y = header(s, 'X', "Financial requirement", "₱2,400,000 seed → breakeven in month 19",
           num_color=AMBER)
lw_ = CW * 0.55
card(s, M, y, lw_, 3.30, "Use of funds", accent=MINT, icon="◕")
bar(s, M + 0.20, y + 0.60, lw_ - 0.40, 0.34,
    [(0.600, MINT), (0.150, AMBER), (0.125, SKY), (0.075, CORAL), (0.050, MUTED)])
funds = [("Cold-room units (3 × ₱480,000)", "₱1,440,000", "60.0%", MINT),
         ("App & IoT stack", "₱360,000", "15.0%", AMBER),
         ("Pilot operations & logistics", "₱300,000", "12.5%", SKY),
         ("Training & cooperative onboarding", "₱180,000", "7.5%", CORAL),
         ("Contingency", "₱120,000", "5.0%", MUTED)]
for i, (k, v, pct, col) in enumerate(funds):
    yy = y + 1.12 + i * 0.40
    rect(s, M + 0.20, yy + 0.05, 0.14, 0.14, fill=col, line=None, shape=MSO_SHAPE.RECTANGLE)
    tb(s, M + 0.44, yy, lw_ * 0.55, 0.26, k, size=9.5, color=BODY)
    tb(s, M + lw_ * 0.50, yy, lw_ * 0.28, 0.26, v, size=9.8, color=WHITE, bold=True,
       align=PP_ALIGN.RIGHT)
    tb(s, M + lw_ * 0.80, yy, lw_ * 0.14, 0.26, pct, size=9.5, color=col, bold=True,
       align=PP_ALIGN.RIGHT)
rx = M + lw_ + 0.24
rw = CW - lw_ - 0.24
end = table(s, rx, y + 0.10, rw, [2.2, 1.0, 1.0, 1.0],
            [["Hubs live", "3", "12", "30"], ["Revenue (₱M)", "1.2", "6.9", "17.9"],
             ["Operating cost (₱M)", "2.0", "5.1", "11.2"], ["EBITDA (₱M)", "(0.8)", "+1.8", "+6.7"]],
            ["3-year projection", "Year 1", "Year 2", "Year 3"], hl_col=None, size=9.5, row_h=0.40)
card(s, rx, end + 0.16, rw * 0.48, 1.20, "Payback per hub", accent=AMBER, icon=None)
tb(s, rx + 0.18, end + 0.66, rw * 0.44, 0.5, "14.5 months", size=17, color=AMBER2, bold=True)
card(s, rx + rw * 0.52, end + 0.16, rw * 0.48, 1.20, "Farmer income per ₱1", accent=MINT, icon=None)
tb(s, rx + rw * 0.52 + 0.18, end + 0.66, rw * 0.44, 0.5, "₱8.50 generated", size=17, color=MINT,
   bold=True)
card(s, M, y + 3.48, CW, 0.90, "Funding structure & sustainability", accent=MINT, icon="✓",
     body="Grant/seed equity covers capex, and each hub becomes a revenue-generating asset from month 4. "
          "Year-2 growth can be financed from hub cash flow plus a DA/PRDP facility and cooperative in-kind "
          "equity (land and labour), keeping dilution minimal.")
footnote(s, "Assumptions: 55–70% utilisation · ₱1.20/kg/day storage · 6% offtake commission · 80/20 co-op revenue share · ₱480k hub capex. Full model available on request.")
notes(s, "We are asking for 2.4 million pesos. 60 percent goes to three pilot cold rooms, 15 percent to the app "
         "and IoT stack, 12.5 percent to pilot operations, 7.5 percent to farmer training, and 5 percent to "
         "contingency. With that we reach three hubs and 120 farmers in Year 1, twelve hubs in Year 2, and thirty "
         "hubs with 6.7 million EBITDA in Year 3. Breakeven in month 19.")

# ================================================== 13 · IMPACT & SDG ====
s = slide(16000)
bg_dark(s)
y = header(s, '◎', "Impact & SDG alignment", "Year-one impact we can audit, not just claim")
imp = [("84 t", "Food saved", "Edible produce not lost — about 560,000 meals.", MINT),
       ("₱2.5 M", "Farmer income unlocked", "120 households, Year 1.", MINT),
       ("18 tCO₂e", "Emissions avoided", "Food loss + diesel reefer avoided.", AMBER),
       ("392 hrs", "Cooling hours logged", "Across 3 hubs, monitored per batch.", MINT)]
iw = (CW - 3 * 0.22) / 4
for i, (big, label, note, col) in enumerate(imp):
    kpi(s, M + i * (iw + 0.22), y, iw, 1.30, big, label, note, accent=col, big_size=22)
y2 = y + 1.52
card(s, M, y2, CW * 0.56, 3.05, "SDG contributions", accent=MINT, icon="◎")
sdg = [("SDG 2 Zero hunger", "84 t of food kept edible in Year 1"),
       ("SDG 8 Decent work & growth", "+35% net income per kg sold; 6 hub jobs"),
       ("SDG 9 Industry & innovation", "Farm-side IoT infrastructure in rural areas"),
       ("SDG 12 Responsible production (priority)", "Loss 35% → 15% — target 12.3"),
       ("SDG 13 Climate action", "Solar cooling displaces diesel reefer")]
for i, (k, v) in enumerate(sdg):
    yy = y2 + 0.66 + i * 0.42
    tb(s, M + 0.20, yy, CW * 0.26, 0.26, k, size=9.5, color=WHITE, bold=True)
    tb(s, M + CW * 0.30, yy, CW * 0.24, 0.26, v, size=9.3, color=BODY)
    rect(s, M + 0.20, yy + 0.34, CW * 0.56 - 0.40, 0.010, fill=LINE, line=None,
         shape=MSO_SHAPE.RECTANGLE)
cx = M + CW * 0.56 + 0.24
cwid = CW - CW * 0.56 - 0.24
card(s, cx, y2, cwid, 1.62, "How we measure", accent=SKY, icon="📈", bullets=[
    "Control-group comparison: same barangay, same crop, same week.",
    "Temperature logs and weight reconciliation per batch.",
    "E-wallet settlement records as proof of income change.",
    "Third-party verification by the cooperative and LGU agri office."])
card(s, cx, y2 + 1.80, cwid, 1.25, "3-year roadmap", accent=AMBER, icon="→")
rx0 = cx + 0.28
rwid = cwid - 0.56
rect(s, rx0, y2 + 2.28, rwid, 0.020, fill=LEAF, line=None, shape=MSO_SHAPE.RECTANGLE)
road = [("Y1", "3 hubs · 120 farmers", True), ("Y2", "12 hubs · 600 farmers", False),
        ("Y3", "30 hubs · 1,500 farmers", False)]
for i, (yr, d, on) in enumerate(road):
    px = rx0 + i * (rwid / 2.5)
    rect(s, px, y2 + 2.20, 0.18, 0.18, fill=AMBER if on else PANEL2,
         line=AMBER if on else LEAF, lw=1.2, shape=MSO_SHAPE.OVAL)
    tb(s, px - 0.30, y2 + 2.46, 1.4, 0.5,
       [[(yr, {'color': WHITE, 'bold': True, 'size': 9.5})], [(d, {'color': MUTED, 'size': 8.2})]],
       spacing=1.1, align=PP_ALIGN.CENTER)
notes(s, "Impact. Every peso we deploy is designed to move three things: farmer income, food actually eaten, and "
         "emissions avoided. By month twelve that means 120 farm households earning more, 84 tonnes of food saved, "
         "and 18 tonnes of CO2e avoided — squarely on SDG 12.3 and SDG 2.")

# ==================================================== 14 · CLOSING =======
s = slide(15000)
rect(s, 0, 0, W, H, fill=CREAM, line=None, shape=MSO_SHAPE.RECTANGLE)
rect(s, 0, H - 0.10, W, 0.10, fill=AMBER, line=None, shape=MSO_SHAPE.RECTANGLE)
tb(s, M, 1.10, 7.0, 0.3, "CLOSING", size=9.5, color=LEAF, bold=True)
tb(s, M, 1.42, 7.6, 1.9,
   [[("Cooling exists.", {'color': INK, 'size': 40, 'bold': True})],
    [("It just isn't at the farm.", {'color': INK, 'size': 40, 'bold': True})]], spacing=1.02)
tb(s, M, 3.28, 7.0, 0.8,
   "Fresko puts it there — shared, solar-powered, and backed by real demand. Every kilo counts.",
   size=14, color=INK2, spacing=1.15)
chiprow(s, M, 4.30, [("Ask ① ₱2.4 M seed funding", LEAF), ("Ask ② 3 cooperative partners", LEAF),
                     ("Ask ③ 1 logistics partner", LEAF)], gap=0.14)
s.shapes.add_picture('assets/fresko-logo.png', Inches(8.55), Inches(1.42),
                     width=Inches(1.7), height=Inches(1.7))
tb(s, 8.55, 3.34, 4.2, 0.6, "Thank you", size=30, color=INK, bold=True)
tb(s, 8.55, 4.02, 4.2, 1.5,
   [[("Team [TEAM NAME]", {'color': INK, 'bold': True, 'size': 11.5})],
    [("[Member 1] · [Member 2] · [Member 3]", {'color': INK2, 'size': 11})],
    [("Mentor: [MENTOR NAME]", {'color': INK2, 'size': 11})],
    [("[email] · [mobile]", {'color': INK2, 'size': 11})]], spacing=1.3)
notes(s, "To close: cooling already exists in the Philippines — it just does not exist at the farm. Fresko puts it "
         "there: shared, solar-powered, and demand-backed. We are asking for 2.4 million pesos, three cooperative "
         "partners, and one logistics partner. Every kilo counts. Thank you — we are ready for your questions.")

# ==================================================== 15 · APPENDIX ======
s = slide(14000)
bg_dark(s)
y = header(s, 'A', "Appendix", "Sources & assumptions")
half = (CW - 0.24) / 2
card(s, M, y, half, 3.25, "Sources", accent=MINT, icon="⌘", bullets=[
    "PSA RSSO-CAR — Situation of Selected High-Value Vegetable Crops in Benguet, 2024 (253,543.95 MT).",
    "UN-CSAM / Mopera — Post-harvest Technology in the Philippines (42% vegetables, 28% fruits lost).",
    "PCAARRD (2025) — Luzon tomato farmgate ₱4–6/kg vs Metro Manila retail ₱25–60/kg.",
    "SEARCA / ADB post-harvest loss study (2022) — mango, tomato and onion route losses.",
    "UN Food Systems — Philippine Agrifood System Transformation Pathway (cold-chain gap).",
    "Industry estimate: ~860,000 of ~1.4 M cold-storage pallet positions available."])
card(s, M + half + 0.24, y, half, 3.25, "Key assumptions", accent=AMBER, icon="Σ", bullets=[
    "Hub capex ₱480,000 · opex ₱28,000/month · storage ₱1.20/kg/day.",
    "Utilisation ramp 35% → 55% → 70%; 2-tonne nominal capacity.",
    "Offtake commission 6% on matched GMV; 80/20 co-op revenue share.",
    "Loss reduction 35% → 15% validated against a same-week control group.",
    "₱30/kg average farmgate for value-of-loss estimates.",
    "All financials are concept-level projections for the 12-month pilot."])
tb(s, M, y + 3.50, CW, 0.7,
   [[("Ask us the hard questions — ", {'color': TEXT}),
     ("unit economics, permitting, or the model behind the 15% loss target.", {'color': AMBER2, 'bold': True}),
     ("  We brought the spreadsheet.", {'color': TEXT})]], size=13, spacing=1.15)
notes(s, "Appendix for Q and A: our sources and every assumption behind the numbers. All figures are traceable, "
         "and every projection has a stated utilisation and pricing assumption.")

# ------------------------------------------------------------------ save ---
out = 'Fresko-PSC-XI-Concept-Note.pptx'
prs.save(out)
print(f"saved {out} · {len(prs.slides.__iter__.__self__._sldIdLst)} slides · {os.path.getsize(out)/1e6:.2f} MB")
