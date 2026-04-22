**Component 1 of the WHO SMART Guidelines L2 DAK structure.** This page summarises the health interventions and health-specific recommendations repackaged into this Digital Adaptation Kit (DAK), the L1 guidance documents they are drawn from, and the position of the DAK within the wider SMART Guidelines ecosystem.

A DAK is not original clinical work. It is a repackaging of WHO normative guidance into software-neutral operational artifacts — here, for cervical cancer screening per the WHO 2021 guideline in its Algorithm 5 form (HPV DNA primary screening with VIA triage, treatment by ablation or excision, referral for suspected invasive cancer).

## What this DAK integrates with

The integration work performed in this DAK spans four axes. Each axis is a distinct kind of cross-referencing the DAK commits to.

1. **Across source documents within the cervical cancer domain** — the 2021-07 guideline, its two addenda (2021-12 mRNA, 2024-06 dual-stain cytology), embedded good practice statements, the IARC evidence base, and the Cervical Cancer Elimination Strategy's programmatic framing. See the [Source documents](#source-documents) section below and the [Scope Declaration's addendum reconciliation](cc-000.html).

2. **Across WHO classifications and shared vocabularies** — the UHC Compendium codes that identify the clinical interventions, the CDHI codes that classify the digital interventions. See [Health interventions](#health-interventions) and [Digital health interventions](#digital-health-interventions). *Phase 2 — codes to be added.*

3. **Across WHO SMART DAKs in the ecosystem** — data elements harvested from the WHO HIV DAK (age, sex, HIV status, prior screening history, VIA result) rather than re-authored, with provenance captured in the Core Data Dictionary. See [Related DAKs](#related-daks).

4. **Across the DAK's own 9 components** — personas referenced in scenarios, data elements consumed by decision logic, indicators derived from captured data. *This integration becomes visible only as Components 2–4 and 8–9 are authored; it is declared here as a commitment, not yet demonstrated.*

The methodology layer operating over this DAK (textualist/purposive split, interpretation register) is documented separately on the [Methodology](methodology.html) page and is not required by the WHO SMART Guidelines L2 SOP. It is adjacent to the repackaging work, not a substitute for it.

## Source documents

The L1 materials integrated by this DAK.

| Document | Date | Role | Reference |
|---|---|---|---|
| WHO guideline for screening and treatment of cervical pre-cancer lesions, 2nd edition | 2021-07 | **Primary** — Algorithm 5 source; all cascade decisions trace to its recommendations | ISBN 9789240030824. [WHO publication page](https://www.who.int/publications/i/item/9789240030824) |
| WHO guideline on use of mRNA tests for human papillomavirus (HPV) | 2021-12 | Addendum — adds HPV mRNA as alternative primary test for the general population; no change to Algorithm 5's WLHIV pathway or post-treatment cascade | ISBN 9789240040434. [WHO publication page](https://www.who.int/publications/i/item/9789240040434) |
| WHO guideline on use of dual-stain cytology to triage women after a positive HPV test | 2024-06 | Addendum — adds dual-stain cytology as alternative triage for the general population; explicit deferral on WLHIV | ISBN 9789240091658. [WHO publication page](https://www.who.int/publications/i/item/9789240091658) |
| IARC Handbook of Cancer Prevention, Volume 18 — Cervical Cancer Screening | 2022 | Evidence base — cited by the 2021 guideline's GRADE process; source for the screening-interval evidence that cc-005 specifies | [IARC publication page](https://publications.iarc.who.int/604) |
| WHO Global Strategy to Accelerate the Elimination of Cervical Cancer | 2020 | Programmatic context — the "90-70-90" targets that frame screening programme scale-up and that [cc-000](cc-000.html) positions this DAK within | [WHO publication page](https://www.who.int/publications/i/item/9789240014107) |

The addendum reconciliation in [cc-000](cc-000.html) traces which recommendations each addendum modifies, preserves, or defers.

## Health interventions

*Phase 2 — UHC Compendium codes to be added.*

This section will list the clinical interventions repackaged by this DAK, with their identifiers from the [WHO UHC Compendium](https://www.who.int/universal-health-coverage/compendium) and the cascade step at which each is invoked. Anticipated entries:

- HPV DNA testing — primary screening
- Visual inspection with acetic acid (VIA) — triage
- Thermal ablation — treatment of eligible precancerous lesions
- Large-loop excision of the transformation zone (LLETZ / LEEP) — treatment of non-ablation-eligible precancerous lesions
- Cold-knife conization — treatment of adenocarcinoma in situ (AIS)
- Referral for suspected invasive cervical cancer — specialist evaluation and biopsy

Each row will carry the Compendium identifier, the intervention short name, the L1 recommendation(s) that govern it, and the cascade decision in the [Decision Logic](decision-logic.html) that triggers or conditions it.

## Digital health interventions

*Phase 2 — CDHI codes to be added.*

This section will classify the DAK's functional contribution using the [WHO Classification of Digital Health Interventions (CDHI) v1.0, 2018](https://www.who.int/publications/i/item/9789241550154). Anticipated entries:

- **1.6.2 Provide prompts and alerts according to clinical protocol** — the primary classification for this DAK; the DMN decision tables *are* this intervention.
- **1.8.1 Referral coordination** — the "suspected cancer → refer" pathway in the Triage Decision.
- **1.4.1 Transmit diagnostic results** — the HPV DNA result → Triage Decision pathway.
- **2.4.1 Targeted client communication** — screening invitation and rescreen reminder logic derivable from the Due-for-Screening decision.
- **2.7.1 Client identification and registration** — prerequisite to any cascade decision; the DAK consumes registration data but does not define it.
- **2.6.1 Routine health indicator data collection and management** — the indicators component (Component 8, not yet authored) will instantiate this classification.

Each row will carry the CDHI identifier, the classification title, and the DAK artifact that instantiates it.

## Recommendations

The numbered recommendations and good practice statements from the three source documents that this DAK traces to.

The **Operational relevance** column uses four values:

- **Encoded** — the recommendation is directly represented in one or more DMN decision tables. Removing it from the source would require changing the rules.
- **Partially encoded** — some aspects of the recommendation are in the DMN, others are deliberately deferred. See the referenced register entry, where present, for the deferral rationale.
- **Contextual** — the recommendation informs the DAK's scope or framing but is not instantiated as a rule.
- **Not encoded** — the recommendation is acknowledged as within the cervical cancer domain but sits outside the DMN cascade (upstream data collection, operational timing, transition guidance, or governing an algorithm not selected — see [cc-000](cc-000.html) for scope boundaries).

### 2021-07 guideline — general population

| # | Strength | Topic | Cascade step | Operational relevance | Register entry |
|---|---|---|---|---|---|
| 1 | Strong | HPV DNA as primary test (rather than VIA or cytology) | Algorithm selection | Encoded | — |
| 2 | Conditional | HPV DNA with or without triage for general population | Algorithm selection | Contextual — Algorithm 5 uses triage | — |
| 3a | Conditional | Treat HPV DNA+ without triage (screen-and-treat approach) | Algorithm selection | Not encoded — Algorithm 5 uses screen-triage-and-treat | [cc-000](cc-000.html) |
| 3b | Conditional | Screen-triage-and-treat: HPV DNA primary + triage (partial genotyping, colposcopy, VIA, or cytology) | Algorithm selection | Encoded — VIA chosen | [algorithm-selection](algorithm-selection.html) |
| 4 | Conditional | Self-collection of HPV samples acceptable | Data collection (upstream) | Not encoded — upstream of DAK cascade | — |
| 5–7 | Conditional | Age thresholds and prioritisation (start 30, prioritise 30–49, stop after 50 with two consecutive negatives) | Eligibility | Partially encoded — `<30`, `30–49`, `>49` branches encoded; two-consecutive-negatives stopping rule deferred | — |
| 8 | Conditional | Screening every 5–10 years with HPV DNA primary | Due for Screening | Encoded | [cc-005](cc-005.html) |
| 9 | Conditional | 3-yearly screening when using VIA or cytology primary (HPV DNA not operational) | Due for Screening | Not encoded — Algorithm 5 uses HPV DNA primary | [cc-000](cc-000.html) |
| 10 (GPS) | GPS | Screening even twice in a lifetime is beneficial | Programmatic | Contextual — shapes [cc-000](cc-000.html)'s low-coverage regime framing | [cc-000](cc-000.html) |
| 11 | Conditional | Triage-negative retest at 24 months (general population) | Triage | Encoded | — |
| 12 | Conditional | Post-colposcopy-normal retest at 12 months after cytology-primary positive | Follow-up | Not encoded — Algorithm 5 uses HPV DNA primary | [cc-000](cc-000.html) |
| 13 | Conditional | Post-treatment retest at 12 months (general population, single retest) | Follow-up | Encoded | — |
| 14 | Conditional | Use HPV DNA at next screening regardless of prior test | Transition | Not encoded — transition guidance, not cascade logic | — |

### 2021-07 guideline — women living with HIV

| # | Strength | Topic | Cascade step | Operational relevance | Register entry |
|---|---|---|---|---|---|
| 21 | Conditional | WLHIV screening starts at age 25 | Eligibility | Encoded | [cc-002](cc-002.html) |
| 22 | Conditional | Triage required for WLHIV | Algorithm selection | Encoded — binds Algorithm 5 to the triage pathway | [cc-002](cc-002.html) |
| 23 | Conditional | Screen-triage-and-treat for WLHIV; triage method country-selected (partial genotyping, colposcopy, VIA, cytology) | Algorithm selection | Encoded — VIA chosen | [algorithm-selection](algorithm-selection.html) |
| 24 | Conditional | Self-collection acceptable (WLHIV) | Data collection (upstream) | Not encoded | — |
| 25–27 | Conditional | WLHIV age prioritisation and stopping (mirroring Recs 5–7 for general population) | Eligibility | Partially encoded — WLHIV age branches encoded; stopping rule deferred | — |
| 28 | Conditional | WLHIV screening every 3–5 years | Due for Screening | Encoded | [cc-005](cc-005.html) |
| 29 | Conditional | 3-yearly screening when using VIA or cytology primary (HPV DNA not operational) | Due for Screening | Not encoded — Algorithm 5 uses HPV DNA primary | [cc-000](cc-000.html) |
| 30 (GPS) | GPS | Screening twice in a lifetime is beneficial (WLHIV) | Programmatic | Contextual | [cc-000](cc-000.html) |
| 31 | Conditional | WLHIV triage-negative retest at 12 months | Triage | Encoded | — |
| 32 | Conditional | Post-colposcopy-normal retest at 12 months after cytology-primary positive | Follow-up | Not encoded — Algorithm 5 uses HPV DNA primary | [cc-000](cc-000.html) |
| 33 | Conditional | WLHIV post-treatment "double follow-up" — retest at 12 and 24 months | Follow-up | Partially encoded — textualist collapses to single retest; tracked gap, see [register index](register.html) | [cc-002](cc-002.html) |
| 34 | Conditional | Transition guidance (WLHIV) | Transition | Not encoded | — |

### Treatment and good practice statements

| # | Strength | Topic | Cascade step | Operational relevance | Register entry |
|---|---|---|---|---|---|
| 41 (GPS) | Good practice | Treat within 6 months; defer during pregnancy; re-evaluate before treatment if 6-month window missed | Treatment | Partially encoded — pregnancy-deferral encoded purposive-only (textualist has no pregnancy input); 6-month timing and re-evaluation not encoded (operational) | [cc-006](cc-006.html) |
| 42 | Conditional | LLETZ or CKC for adenocarcinoma in situ (AIS) | Treatment | Encoded — informs treatment modality | — |

### Addenda

| Source | Scope of change | Applies to Algorithm 5 as modelled? | Register treatment |
|---|---|---|---|
| 2021-12 mRNA addendum | Adds HPV mRNA as alternative primary test, general population only, 5-year interval; no change to any Algorithm 5 cascade element | No — Algorithm 5's HPV DNA + VIA + treatment + follow-up cascade is preserved unchanged | [cc-000](cc-000.html) addendum reconciliation |
| 2024-06 dual-stain addendum | Adds dual-stain cytology as alternative triage for general population; explicit WLHIV deferral | No — Algorithm 5 retains VIA triage; retained as context for triage-evidence volatility in [cc-003](cc-003.html) | [cc-000](cc-000.html) addendum reconciliation |

## Related DAKs

### Data-element integration with the WHO HIV DAK

The [Core Data Dictionary](dictionary.html) harvests six data elements from the WHO HIV DAK rather than re-authoring them:

- Age (HIV.A registration cluster)
- Sex (`HIV.A.DE25`)
- Living with HIV (HIV.B HIV-status cluster)
- Date of last cervical cancer screening test (`HIV.D.DE656`)
- Prior screen result (`HIV.D.DE664`)
- VIA result (`HIV.D.DE668`)

These are classified as "Kind 2 — harvested with provenance" in the Core Data Dictionary. The harvest approach records the source DAK, the source element ID, and (in a planned Phase B) the commit hash of the source DAK at harvest time, giving point-in-time provenance and decoupling this DAK from upstream drift. See the [Data Dictionary README](README.html) for the full Kind classification and the tri-purpose framing of the L2/L3 boundary.

### Deferred linkage to a WHO Immunizations DAK

HPV vaccination status is an acknowledged input gap in this DAK, tracked in [cc-004](cc-004.html). The unvaccinated-cohort assumption inherited from the 2021 guideline is still approximately valid under the epidemiological regime declared in [cc-000](cc-000.html), but will not remain so indefinitely. When vaccinated cohorts age into screening eligibility and WHO issues vaccination-modulated screening guidance, this DAK will need to consume vaccination status from the Immunizations DAK's data elements (candidate `IMMZ.*` cluster identified in the Core Data Dictionary as a deferred Kind 2 stub).

### Ecosystem contribution: shared canonical dictionary

The Kind 2 harvesting pattern and the Kind 3 "propose to smart-core" classification used in the Core Data Dictionary are contributions toward a shared canonical SMART Guidelines data dictionary — the proposal being that future DAKs reference harmonised elements rather than harvest per-project. See the [Data Dictionary README](README.html) and its cited references to Pretty et al. (2023) and Muliokela et al. (2024) for the full grounding.

## Status

*Draft — Phase 1 of Component 1 authoring (2026-04-21).* Sections 1, 2, 5, and 6 are populated from material already present in the repository (scope declaration, algorithm selection analysis, register entries, data dictionary). Sections 3 (Health interventions — UHC Compendium codes) and 4 (Digital health interventions — CDHI codes) are placeholders pending Phase 2 external-vocabulary lookup.
