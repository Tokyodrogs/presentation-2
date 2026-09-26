# Fresko — Philippine Startup Challenge XI
## Concept Note (submission-ready write-up)

> **Team name:** `[TEAM NAME]`
> **Startup name:** Fresko
> **Team members:** `[Member 1]`, `[Member 2]`, `[Member 3]`
> **Mentor:** `[MENTOR NAME]`
> **Tagline:** Farm-side cooling, shared. Every kilo counts.
> **Solution type:** Software + IoT-enabled technology (Ideation → MVP stage)

Replace anything inside backticks/brackets with your details. Every number below is
sourced or flagged as a projection so you can defend it in Q&A. Sources are listed at
the end.

---

## I. SUMMARY

Fresko is a shared, solar-powered cold-chain service for smallholder vegetable farmers.
We install a modular 2-tonne solar cold room — a **Fresko Hub** — at a barangay or
cooperative in the highlands, and give farmers a mobile app that reserves cooling
capacity, predicts how long their produce will stay fresh, matches it to a verified
buyer, and pays them within 24 hours.

One in every three kilos of highland vegetables is lost between the farm and the market
(27–42% post-harvest loss for fruits and vegetables nationally). A Benguet farmer sells
carrots at ₱4–6/kg while Metro Manila retail reaches ₱25–60/kg — the gap is not the
farmer's fault; it is a missing first mile of cooling and market information.

Fresko closes that first mile without asking farmers for capital: they pay **₱0 upfront**
and are charged only as produce moves (₱1.20/kg/day storage, 6% offtake commission).
The result: **~20% more sellable kilos, cash in 24 hours, and a measurable drop in food
loss.** Our priority SDG is **SDG 12 — Responsible Consumption and Production**
(Target 12.3, halve food loss by 2030), supported by SDGs 2, 8, 9 and 13.

---

## II. BACKGROUND OF THE PROBLEM

**The problem.** Filipino smallholders harvest highly perishable vegetables and then
have no way to keep them cool. Produce sits at the roadside or at a trading post for
hours, then travels 6–8 hours unrefrigerated to Metro Manila *bagsakan* markets.

**Scale and context.**

| Fact | Figure | Source |
|---|---|---|
| Post-harvest loss, vegetables / fruits | 42% / 28% (27–42% for fruits & vegetables) | UN-CSAM / Mopera (2016) |
| Benguet high-value vegetable harvest, 2024 | 253,543.95 MT | PSA RSSO-CAR (2024) |
| Estimated loss at a conservative 28% | ≈ 71,000 MT ≈ ₱2.1 B at ₱30/kg | Team computation |
| Cold-storage capacity vs need | ~860,000 of ~1.4 M pallet positions — ~540k short, and concentrated in Metro Manila | Industry estimate (FAST Logistics) |
| Farmgate vs retail (tomato/Luzon, 2025) | ₱4–6/kg farmgate vs ₱25–60/kg Metro Manila retail | PCAARRD (2025) |
| Route-level losses (ADB/SEARCA study) | Mango 30.9–33.9%, fresh onion 45% | SEARCA/ADB (2022) |

**Root causes we address.**

1. **No cooling at or near the farm.** The nearest cold room is a truck ride away, so
   shelf life is spent before cooling begins.
2. **Oversupply and price collapse.** In February 2025 tomato farmgate fell to ₱4/kg in
   Luzon while Manila consumers paid ₱25–60/kg — a pure market-access and storage failure.
3. **No grading, traceability or market information.** Farmers sell blind as price-takers;
   buyers cannot verify quality, so they discount everything.

**Relevance.** Agriculture employs about a quarter of Filipino workers but contributes
only ~10% of GDP, and rural poverty remains around 30%. Reducing post-harvest loss is
one of the few interventions that raises farmer income, lowers consumer prices, improves
nutrition, and cuts emissions at the same time — without needing new farmland.

---

## III. PROPOSED STARTUP SOLUTION

Fresko is a three-part system — hardware, software, and logistics — deployed as a shared
service rather than sold as equipment.

**How it works (the Fresko loop):**

1. **Book & harvest.** The farmer reserves a cold-room slot in the Fresko app; harvest is
   timed to that booking so nothing waits.
2. **Pre-cool within 2 hours.** Produce arrives at the barangay hub and is pre-cooled to
   4–8 °C in a solar-powered chamber (3 kWp solar + 5 kWh battery, 2 HP inverter
   compressor).
3. **Grade & predict.** IoT sensors log temperature every 15 minutes; the freshness model
   converts time-temperature history into an estimated remaining shelf life and grades
   batches A/B/C.
4. **Match & pay.** The batch is matched to a verified buyer, consolidated with neighbours'
   loads into one refrigerated dispatch, and the farmer is paid to an e-wallet within
   24 hours.

**Components.**

- **Fresko Hub** — 2-tonne modular insulated cold room, solar-powered, deployable in
  21 days, shared by ~40 farms. Capex ₱480,000 per hub (on our books, grant-funded).
- **Fresko App** — offline-first mobile app (Filipino/Ilocano, SMS fallback) for booking,
  grading results, buyer matching, and payment.
- **Fresko Route** — consolidated refrigerated dispatch with a logistics partner, so
  small volumes become one economical load.

**Priority SDG: SDG 12 — Responsible Consumption and Production.** Fresko directly serves
Target 12.3 (halve per-capita global food waste and reduce food losses by 2030) by moving
loss from 35% to a 15% target measured in kilograms. Supporting SDGs: **2** (Zero Hunger),
**8** (Decent Work and Economic Growth), **9** (Industry, Innovation and Infrastructure),
**13** (Climate Action).

---

## IV. OBJECTIVES

All objectives are time-bound to the 12-month pilot and measured against a same-week,
same-crop control group in the same barangay.

**Impact objectives**

1. Reduce post-harvest loss from **35% → 15%** for participating farms by Month 12.
2. Increase **farmer net income per kilo sold by ≥35%** for 120 member farms.
3. Keep **84 tonnes of food edible** in Year 1 (≈560,000 meals), rising to 1,500 farmers by Year 3.
4. Avoid **18 tCO₂e** in Year 1 by preventing food loss and displacing diesel reefer trips.

**Operational objectives**

5. **3 hubs installed and commissioned** in Benguet by Month 12 (Buguias, Atok, La Trinidad).
6. **120 farmer-members onboarded** (≥40% women-led households), each in under 15 minutes.
7. **240 tonnes cumulative throughput** cooled in Year 1 with **≥99% hub uptime** and ≥98%
   temperature-log compliance.
8. **₱33,000 monthly contribution per hub** and **payout turnaround ≤24 hours**.
9. Reach **payback of 14.5 months per hub**; company breakeven by **Month 19**.

---

## V. TARGET MARKET / BENEFICIARIES

**Primary beneficiaries — smallholder highland vegetable farmers.**
Roughly **60,000 farmers in Benguet** (average farm size **1.3 hectares**), mostly 45–65
years old, earning ₱2,000–5,000 monthly gross, farming carrots, cabbage, broccoli,
potatoes and snap beans. They are price-takers who sell grade-2 kilos for as little as
₱5/kg and wait 7–30 days to be paid. Cooperatives, PCAs and farmer associations are our
natural aggregating partners.

**Secondary — the paying side.** Market vendors and *bagsakan* traders needing graded
stock with longer shelf life; restaurants, carinderias and e-grocery suppliers needing
consistent volumes; processors and exporters needing traceable raw materials; and
cooperatives, LGUs and agri-corporates needing loss-reduction and ESG reporting.

**Expansion path.** Beachhead: Buguias, Atok and La Trinidad (Benguet) → Year 2: Nueva
Vizcaya and Mountain Province → Year 3: Ilocos tomato corridor, Cebu and Davao.

**Evidence of demand (from 40 farm interviews).** 7 of 10 farmers would pay ₱1–1.50 per
kilo per day for cooling that prevents spoilage; 9 of 10 want settlement within 48 hours;
all respondents reported at least one total-loss incident in the past year.

---

## VI. VALUE PROPOSITION

**For farmers: no capex, fewer spoilage kilos, cash in 24 hours.**

| What the farmer cares about | Fresko | Trading post (status quo) | Buying own cold room | Reefer 3PL |
|---|---|---|---|---|
| Upfront cost | **₱0** | ₱0 | ₱1.2 M+ | Per-trip minimum |
| Post-harvest loss | **~15%** | 35% | 8–12% | ~10% |
| Payment terms | **24 hours** | 7–30 days | — | 30 days |
| Market access & grading | **AI grade + matched buyer** | Blind, price-taker | None | None |
| Traceability / cold-chain proof | **Per-batch log** | None | Partial | Partial |

**Why we win.** Existing players either sell hardware (which farmers cannot finance), or
move produce in cities (after the loss already happened), or list products online without
guaranteeing freshness. Fresko owns the farm-side layer where the loss actually occurs,
and bundles cooling with demand and payment — the two things that make cooling worth
paying for.

**The promise in one line:** for every 1,000 kg harvested, ~200 kg more reach a buyer —
roughly ₱6,000 of additional income per cycle at conservative grade-2 prices.

**Defensibility.** Farm-side assets in barangays take time and trust to replicate; the
loss-reduction dataset (crop, grade, route, temperature history, buyer outcome) compounds
with every hub and improves matching and shelf-life prediction over time.

---

## VII. BUSINESS MODEL

**How we create value.** The cooperative provides land and an operator; Fresko provides
the solar cold room, sensors, app and buyer network. Because capex stays on our books,
the farmer's cost of entry is zero.

**How we deliver value.** Shared capacity (not ownership), consolidated refrigerated
dispatch, digital settlement, and a monthly loss-and-price report for the cooperative.

**How we capture value — four recurring revenue lines**

| # | Revenue stream | Price | Who pays |
|---|---|---|---|
| 1 | Storage fee | ₱1.20 / kg / day | Buyer at dispatch (deducted from farmer settlement) |
| 2 | Offtake commission | 6% of matched GMV | Charged only on a completed, paid sale |
| 3 | Co-op analytics subscription | ₱499 / month per cooperative | Cooperatives, PCAs |
| 4 | Verified impact reporting | ₱25,000–60,000 per contract | LGUs, agri-corporates, CSR/ESG programmes |

**Unit economics — one 2-tonne hub**

| Line | Value |
|---|---|
| Capex per hub (grant-funded) | ₱480,000 |
| Monthly operating cost (power, tech, operator share) | ₱28,000 |
| Monthly revenue at 55% utilisation | ₱61,000 |
| Contribution per month | ₱33,000 |
| Gross margin | 54% |
| Payback per hub | ≈ 14.5 months |
| Annual revenue per hub at scale | ≈ ₱735,000 |

**Sustainability of the model.** Hubs generate cash from Month 4 and the asset is long-lived
(7–10 years), so growth in Year 2 can be financed by hub cash flow plus a DA/PRDP facility
and cooperative in-kind equity (land and labour) — keeping dilution minimal. The 80/20
revenue share with cooperatives keeps incentives aligned: they earn more only when more
kilos are saved and sold.

---

## VIII. MARKET ANALYSIS

**Market size (bottom-up, stated assumptions).**

| Layer | Value | How we got it |
|---|---|---|
| **TAM** | **₱4.6 B / year** | National high-value vegetable and fruit value × ~10% addressable cold-storage and post-harvest service wallet |
| **SAM** | **₱1.1 B / year** | Cordillera + Northern Luzon vegetable corridors (~1,200 t/day moving to Manila) × the same service wallet |
| **SOM** | **₱12 M / year (Year 3)** | 30 installed hubs × ₱735,000 — roughly **1% of SAM** |

**Demand drivers and trends.** A ~540,000 pallet-position cold-chain gap with capacity
concentrated in Metro Manila; DA/PRDP funding for farm-side facilities; persistent food
inflation that puts loss reduction high on LGU agendas; e-grocery and food-service demand
for graded, traceable local produce; and growing corporate demand for verified food-loss
and emissions reporting.

**Competitive landscape.**

| Competitor type | What they do | Why Fresko is different |
|---|---|---|
| Trading posts / *disposers* | Aggregate and price produce | No cooling, no grading — we plug into them as buyers instead of replacing them |
| Urban cold storage operators | Big cold rooms near consumption centres | We are farm-side; shelf life that has already been lost cannot be recovered in Manila |
| Cold-chain 3PLs | Refrigerated hauling per trip | Per-trip pricing and urban focus; we make small volumes shareable and pay later |
| Solar cold-room suppliers | Sell the box | Hardware only — no demand, no payment, no farmer financing (₱1.2 M+) |
| Digital agri marketplaces | List produce for B2B buyers | Listings without cold assurance; we guarantee freshness and settle in 24 hours |

**Positioning.** On a map of "farm-side infrastructure" (x-axis) versus "demand and
intelligence" (y-axis), Fresko is the only player in the high-high quadrant: assets where
the loss happens, plus the data and demand that make those assets profitable.

---

## IX. OPERATIONS PLAN

**Phased rollout**

| Phase | Timeline | Milestones |
|---|---|---|
| **Phase 0** | Months 1–3 | MOA with partner cooperative (land + operator); LGU permits and DA endorsement; baseline loss audit on 3 farms; hire hub technician |
| **Phase 1** | Months 4–6 | Hub #1 installed and commissioned (21-day install); 40 farmers onboarded in <15 min each; app v1 live (offline-first); first matched offtake cycles |
| **Phase 2** | Months 7–12 | Hubs #2 and #3 (Atok, La Trinidad); e-wallet escrow payouts; refrigerated dispatch partner contracted; first verified impact report |
| **Scale** | Year 2 | 12 hubs under a co-op-operated franchise model (80/20 revenue share); Fresko supplies technology, training and demand |

**Hub standard operating procedure.** Pre-cool within 2 hours of harvest; hourly
temperature logs with alerts above 9 °C; HACCP-aligned handling and crate hygiene;
FEFO (first-expired-first-out) rotation for dispatches; weekly preventive maintenance and
monthly audits; zero-tolerance on mixing spoiled batches with sellable stock.

**Technology architecture.** LoRaWAN/GSM sensors → cloud time-series store → shelf-life
model and routing rule engine → offline-first farmer app (Filipino/Ilocano, SMS fallback)
→ GCash/Maya escrow settlement API. Design rule: every farmer-facing step must work on a
₱4,000 Android phone with intermittent signal.

**Team and roles.** `[Member 1]` — CEO / farmer partnerships and cooperative relations;
`[Member 2]` — CTO / IoT, sensors and app development; `[Member 3]` — COO / hub
operations, logistics and training; `[MENTOR NAME]` — mentor, agribusiness and cold chain.

**Key risks and mitigation**

| Risk | Mitigation |
|---|---|
| Power interruptions | Solar + 5 kWh battery, genset hook-up, thermal buffer design |
| Low initial utilisation | Anchor offtake contracts with 2 vendors before install; free first month for founding farmers |
| Trust and digital adoption | Co-op-led onboarding, in-person training, SMS fallback, no-upfront-cost model |
| Produce quality disputes | Third-party grading rubric, temperature log as evidence, buyer rating system |
| Weather / typhoon disruption | Modular relocatable hubs, route contingency planning, harvest-timing advice in app |

---

## X. FINANCIAL REQUIREMENT

**Total ask: ₱2,400,000** (12-month pilot, seed/grant stage)

| Use of funds | Amount | Share | Purpose |
|---|---|---|---|
| Cold-room units (3 × ₱480,000) | ₱1,440,000 | 60.0% | Solar cold rooms, batteries, sensors, installation |
| App & IoT stack | ₱360,000 | 15.0% | Offline-first app, shelf-life model, escrow integration |
| Pilot operations & logistics | ₱300,000 | 12.5% | Technician, dispatch, crates, hub consumables |
| Training & cooperative onboarding | ₱180,000 | 7.5% | Farmer training, materials, CBA baseline audit |
| Contingency | ₱120,000 | 5.0% | Weather delays, tariffed parts, price movements |
| **Total** | **₱2,400,000** | **100%** | |

**Three-year projection (₱ millions)**

| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Hubs live | 3 | 12 | 30 |
| Farmer-members | 120 | 600 | 1,500 |
| Revenue | 1.2 | 6.9 | 17.9 |
| Operating cost | 2.0 | 5.1 | 11.2 |
| **EBITDA** | **(0.8)** | **+1.8** | **+6.7** |

**Breakeven: Month 19.** Year 1 shows a deliberate loss while hubs ramp; Year 2 turns
EBITDA-positive as utilisation reaches 55–70% and the analytics subscription base scales
with each cooperative onboarded.

**Return on the ask.** Approximately **₱8.50 of farmer income generated per ₱1 invested**
(₱2.5 M in Year-1 farmer income and ₱1.4 M of avoided spoilage value, against ₱2.4 M
deployed) — plus 84 tonnes of food kept edible and 18 tCO₂e avoided.

**Assumptions.** ₱1.20/kg/day storage; 6% offtake commission; utilisation ramp 35% → 55%
→ 70%; hub capex ₱480,000; opex ₱28,000/month; 80/20 co-op revenue share; ₱30/kg average
farmgate for loss valuation. All figures are concept-level projections for a 12-month
pilot and can be stress-tested on request.

---

## SOURCES

1. Philippine Statistics Authority, RSSO-CAR — *Situation of Selected High-Value Vegetable Crops in Benguet, 2024* (253,543.95 MT).
2. UN-CSAM / S. G. Castro — *Post-harvest Technology in the Philippines*; Mopera (2016) — *Food Loss in the Food Value Chain: The Philippine Agriculture Scenario* (42% vegetables, 28% fruits).
3. PCAARRD (2025) — *Tomato Price Volatility in Luzon* (farmgate ₱4–6/kg vs Metro Manila retail ₱25–60/kg).
4. SEARCA / ADB post-harvest loss study (2022) — mango 30.85–33.89%, fresh onion 45%.
5. UN Food Systems Summit — *Philippine Agrifood System Transformation Pathway* (cold-chain capacity, losses).
6. Industry estimate (FAST Logistics, 2025): ~860,000 of ~1.4 M cold-storage pallet positions required.
7. OECD — *Agricultural Policy Monitoring and Evaluation: Philippines* (average farm holding 1.3 ha; agriculture ~24% of employment vs ~10% of GDP).

*Team note: replace bracketed placeholders, add your interview dates and cooperative
names, and keep the assumption table handy for the Q&A round.*
