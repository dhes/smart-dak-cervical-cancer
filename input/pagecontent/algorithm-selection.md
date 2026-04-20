# Algorithm Selection Analysis: How the 2021 WHO Guideline Narrows the Choice

**Date:** 2026-04-13
**Authors:** Dan Heslinga, with Claude (Anthropic)
**Status:** Draft

## Purpose

This document walks through the WHO 2021 cervical cancer screening guideline's recommendations in sequence, asking the question a Ministry of Health from a country like Ethiopia, Ghana, Malawi, Zambia, or Zimbabwe might ask at the start of guideline implementation discussions:

> "Given what you know about our country, which of the seven screening algorithms should we look at first?"

The answer is not a single algorithm. The guideline deliberately leaves the triage method to country discretion. But it narrows the field systematically, and this document traces the narrowing logic so that it is visible rather than implicit in the case study's choice of Algorithm 5.

This document supports the scope declaration in [`../interpretation-register/cc-000-scope-declaration.md`](cc-000.html), which discloses the choice of Algorithm 5 and its biases. That entry summarises; this document shows the work.

## The seven algorithms

The 2021 guideline (Table 2.2, p.xi) presents seven screening algorithms in two groups:

**Screen-and-treat approaches** (primary test → treatment, no intermediate triage step):

| Algorithm | Primary Test | Triage | Treatment |
|---|---|---|---|
| 1 | VIA | none | direct |
| 2 | HPV DNA (self- or clinician-collected) | none | direct |

**Screen, triage and treat approaches** (primary test → triage → treatment):

| Algorithm | Primary Test | Triage | Treatment |
|---|---|---|---|
| 3 | Cytology | colposcopy | treatment |
| 4 | HPV DNA | HPV16/18 genotyping (with VIA for HPV16/18-negative) | treatment |
| 5 | HPV DNA | VIA | treatment |
| 6 | HPV DNA | colposcopy | treatment |
| 7 | HPV DNA | cytology + colposcopy | treatment |

The algorithms sit on an infrastructure gradient. Algorithm 1 requires no laboratory; Algorithms 2, 4, and 5 require HPV DNA testing; Algorithms 3, 6, and 7 require cytology labs and/or colposcopy. A country's position on this gradient determines which algorithms are feasible before it determines which are preferred.

## Walking through the recommendations

### Recommendation 1 (strong): HPV DNA as the primary screening test

> "WHO recommends using HPV DNA detection as the primary screening test rather than VIA or cytology in screening and treatment approaches among both the general population of women and women living with HIV."

This is a strong recommendation. It creates a clear preference for HPV DNA as the primary test, favouring Algorithms 2, 4, 5, 6, and 7.

Algorithms 1 (VIA primary) and 3 (cytology primary) are not eliminated but deprecated, with an asymmetry in urgency:

- **VIA primary (Algorithm 1):** "existing programmes using VIA as the primary screening test should transition rapidly because of the inherent challenges with quality assurance." Active deprecation.
- **Cytology primary (Algorithm 3):** "existing programmes with quality-assured cytology as the primary screening test should be continued until HPV DNA testing is operational." Tolerated transitionally, conditional on existing quality assurance.

**After Rec 1:** Algorithms 2, 4, 5, 6, 7 preferred. Algorithm 1 deprecated with urgency. Algorithm 3 tolerated transitionally.

### Recommendation 2 (conditional): Triage or no triage — general population

> "WHO suggests using an HPV DNA primary screening test either with triage or without triage to prevent cervical cancer among the general population of women."

This does not narrow the field among the five HPV DNA algorithms for the general population. Both screen-and-treat (Algorithm 2) and screen-triage-treat (Algorithms 4–7) remain viable.

Note the GRADE strength: "suggests" (conditional), not "recommends" (strong). Countries have latitude here.

### Recommendation 22 (conditional): Triage required — women living with HIV

> "WHO suggests using an HPV DNA primary screening test with triage rather than without triage to prevent cervical cancer among women living with HIV."

This is the critical fork for countries with significant HIV prevalence. Unlike Rec 2, this is directional: **triage is recommended for WLHIV**, not optional.

For Ethiopia, Ghana, Malawi, Zambia, and Zimbabwe — all countries with moderate-to-high HIV prevalence in the screening-age population — a meaningful fraction of women presenting for screening will be living with HIV. Rec 22 means any algorithm selected must include a triage pathway for the WLHIV subpopulation.

A country could in principle run two parallel pathways: screen-and-treat (Algorithm 2) for the general population, and a separate triage pathway for WLHIV. But a unified single-pathway approach using a triage algorithm for all women is operationally simpler and avoids the need to bifurcate the screening workflow at the point of care based on HIV status.

**After Recs 1–2 and 21–22:** For countries with significant HIV prevalence, the practical field narrows to Algorithms 4, 5, 6, and 7 (HPV DNA primary with triage).

### Recommendations 3b and 23: Triage method — explicitly left to country discretion

> "In a screen, triage and treat approach using HPV DNA detection as the primary screening test among [the general population of women / women living with HIV], WHO suggests using partial genotyping, colposcopy, VIA or cytology to triage women after a positive HPV DNA test."

The remarks are significant: "The benefits, harms and programmatic costs of the triage options are similar; therefore, **the choice of triage method will be dependent on feasibility, training, programme quality assurance and resources in countries.**"

This is WHO explicitly declining to pick a triage method on evidence grounds and delegating the choice to infrastructure and capacity assessment. The four triage options map directly to the four remaining algorithms:

| Triage method | Algorithm |
|---|---|
| HPV16/18 partial genotyping | 4 |
| VIA | 5 |
| Colposcopy | 6 |
| Cytology (then colposcopy) | 7 |

**After Recs 3b/23:** All four triage algorithms remain viable. The choice is infrastructure-dependent.

### Recommendation 4 / 24: Self-collection

> "When providing HPV DNA testing, WHO suggests using either samples taken by a health-care provider or self-collected samples among both the general population of women and women living with HIV."

Algorithm-neutral — this affects the logistics of HPV DNA primary testing, not which algorithm is selected. But operationally significant: self-collection reduces the need for facility visits for the primary screen, which matters in countries where facility access is the binding constraint on screening coverage.

### Recommendations 5–7 / 25–27: Age thresholds and prioritisation

Start at 30 (general population) or 25 (WLHIV). Prioritise 30–49 / 25–49. Stop after 50 with two consecutive negatives. These apply to all algorithms and do not affect algorithm selection.

The good practice statement (Rec 10/30) — "screening even just twice in a lifetime is beneficial" — acknowledges the low-coverage reality in many of these countries.

### Recommendations 8–9 / 28–29: Screening intervals

- HPV DNA primary: every 5–10 years (general population) or 3–5 years (WLHIV).
- VIA or cytology primary: every 3 years (both populations).

These do not directly select an algorithm, but they create a **resource efficiency argument for HPV DNA primary testing**: a 5–10 year screening interval requires far fewer lifetime encounters than a 3-year VIA interval. For countries with limited screening capacity and a large unscreened backlog, HPV DNA primary saves resources over the programme lifetime even if the per-test cost is higher. This reinforces the Rec 1 preference for HPV DNA and further weakens the case for remaining on Algorithm 1 (VIA primary, 3-year interval).

### Recommendations 11–13 / 31–33: Retesting after triage-negative and post-treatment

- Triage-negative retest: 24 months (general population) or 12 months (WLHIV).
- Post-treatment retest: 12 months (general population, single retest) or 12 months × 2 (WLHIV, "double follow-up").

Algorithm-neutral but these create a higher follow-up burden for WLHIV — further reinforcing Rec 22's insistence on triage for that population, as the follow-up cascade requires a robust pathway.

### Recommendation 14 / 34: Transition guidance

> "As programmes introduce HPV DNA testing, use this test at the woman's next routine screening date regardless of the test that was used at prior screening."

Practical transition instruction acknowledging that countries will run mixed programmes during the shift from VIA or cytology to HPV DNA. Does not affect algorithm selection.

### Recommendations 41–42: Treatment

Treat within 6 months. Defer during pregnancy. LLETZ or CKC for AIS. Algorithm-neutral.

### Summary recommendations (p.xvi)

The guideline concludes with explicit summary strategies:

**General population:**
> "WHO suggests using **either** of the following strategies:
> - HPV DNA detection in a screen-and-treat approach starting at the age of 30 years with regular screening every 5 to 10 years.
> - HPV DNA detection in a screen, triage and treat approach starting at the age of 30 years with regular screening every 5 to 10 years."

**Women living with HIV:**
> "WHO suggests using **the following** strategy:
> - HPV DNA detection in a screen, triage and treat approach starting at the age of 25 years with regular screening every 3 to 5 years."

Note the asymmetry: "either of the following" (general population) versus "the following" singular (WLHIV). Screen-and-treat is explicitly offered as an option for the general population but excluded for WLHIV.

## Mapping the narrowed field against infrastructure reality

After the full recommendation walk-through, the MOH's question has been narrowed to: **which triage method can our health system support?**

The infrastructure constraints relevant to this question, informed by published implementation experience in these countries (see [References](#references)), include the following. **A caveat:** the Muliokela and Tamrat publications document implementation of ANC, family planning, and HIV DAKs — not cervical cancer screening. No cervical cancer SMART DAK has been implemented in these countries to date. The papers are cited here for what they reveal about the digital health infrastructure and implementation capacity these countries actually have, which is relevant to algorithm selection regardless of the clinical domain.

**Fragmented digital health ecosystems.** Ethiopia, Ghana, Malawi, Zambia, and Zimbabwe each have multiple digital health platforms at varying maturity levels (Bahmni, DHIS2 Tracker, SmartCare, Impilo). Integration between systems is limited, documentation of existing system architecture is often inadequate, and interoperability standards are inconsistently adopted (Muliokela et al. 2024a, Tamrat et al. 2025).

**Device and infrastructure shortages.** Health workers face challenges using digital systems in real time at the point of service due to device shortages and infrastructure limitations (Tamrat et al. 2025). This affects the feasibility of algorithms that depend on laboratory results being available at the point of triage.

**Workforce constraints.** VIA is performed by nurses with variable training and limited routine quality assurance. Colposcopy and cytology require specialist skills and equipment that are scarce at peripheral facilities. Genotyping capability depends on the HPV DNA testing platform deployed.

**Existing VIA experience.** Many of these countries have been running VIA-based screening programmes (Algorithm 1), meaning a trained VIA workforce already exists — but the quality assurance challenges that prompted Rec 1's deprecation of VIA as a *primary* test also apply to VIA as a *triage* test, though the clinical stakes are different (triage of a known HPV-positive woman rather than population-level screening).

This infrastructure picture affects the four remaining algorithms differently:

| Algorithm | Triage | Infrastructure requirement | Feasibility in these countries |
|---|---|---|---|
| 4 | HPV16/18 genotyping | Integrated into HPV DNA platform | Feasible if the HPV DNA platform supports genotyping; no additional clinical skill required at point of care |
| 5 | VIA | Trained nurse, acetic acid, adequate light | Feasible — existing VIA workforce from Algorithm 1 programmes; quality assurance remains a concern |
| 6 | Colposcopy | Colposcope, trained colposcopist | Not feasible at peripheral facilities; limited to referral-level facilities |
| 7 | Cytology + colposcopy | Cytology lab, colposcope, trained personnel | Not feasible at scale; requires infrastructure these countries are not deploying |

**Algorithms 6 and 7 are infrastructure-excluded** for peripheral-level deployment in these countries. They remain viable at referral hospitals but cannot anchor a national screening programme that needs to reach women at primary care facilities.

**Algorithm 4 is viable if the HPV DNA platform supports genotyping.** Its advantage is that triage happens at the laboratory level (genotyping is part of the HPV test), reducing the clinical skill required at the point of care. Its constraint is platform-dependent: not all HPV DNA testing platforms support HPV16/18 partial genotyping.

**Algorithm 5 is viable with the existing workforce.** Its advantage is that VIA is a clinical skill these countries already deploy. Its constraint is the well-documented inter-observer variability of VIA, which is the same quality assurance challenge that prompted Rec 1's deprecation of VIA as a *primary* test.

## What the guideline does and does not say

The guideline does not say "use Algorithm 5." It says:

1. Use HPV DNA as the primary test (strong recommendation).
2. For WLHIV, use triage (conditional recommendation, directional).
3. The triage method is a country decision based on feasibility and resources (conditional recommendation, explicitly non-prescriptive).

For countries with moderate-to-high HIV prevalence, limited laboratory infrastructure, and existing VIA-trained workforces, the guideline's narrowing logic lands the conversation on **Algorithm 5 (VIA triage) or Algorithm 4 (genotyping triage)** — not because the evidence prefers them clinically, but because the infrastructure constraints select for them.

The choice between Algorithms 4 and 5 is then a platform question (does the HPV DNA test support genotyping?) and a workforce question (is the existing VIA workforce adequate for triage-level performance?), not an evidence question. The guideline explicitly declines to answer it.

## Methodology note: when does a guideline require an algorithm selection step?

The cervical cancer guideline's multi-algorithm structure is not unique among WHO guidelines — but the fact that it **leaves the selection open** may be. A comparison across three DAK domains illustrates the point.

**ANC (2016 guideline, oldest DAK).** The WHO 2016 ANC guideline faced a structurally comparable fork: the 4-visit focused ANC (FANC) model versus an 8-contact model. Both were alternative models of care with different resource implications. But unlike the cervical cancer guideline, WHO resolved the fork with a strong recommendation: "the four-visit focused ANC (FANC) model does not offer women adequate contact with health-care practitioners and is no longer recommended" (Recommendation E.7). The ANC DAK therefore did not need an upstream model-selection step — all 38 of its L2 decision tables operate within the single recommended 8-contact model.

**HIV (2024 repo, newest DAK).** The WHO smart-hiv DAK (created April 2024, actively maintained) presents a different structure entirely. Rather than alternative pathways, it is organised around ten additive business processes (Registration, Testing, PrEP, Care & Treatment, PMTCT, Infant Diagnosis, Diagnostics, Follow-up, Referral, Reporting) with approximately 11 decision tables that each handle a specific clinical question within the HIV care cascade. The source material is not a single guideline but a synthesis across multiple WHO publications (2016 consolidated ARV guidelines, 2017 PrEP implementation tool, 2019 testing services guidelines, 2021 consolidated guidelines). Countries make choices within this cascade — which ART regimen to stock, which testing strategy to deploy, whether to offer PrEP — but these are parameter-level decisions within a single pathway, not selections among alternative clinical cascades. There is no upstream algorithm selection decision comparable to the cervical cancer case.

**Cervical cancer (2021 guideline).** As documented in the analysis above, the guideline presents seven discrete algorithms and explicitly delegates the selection to countries based on infrastructure and capacity.

The three cases represent three distinct structural patterns:

| Pattern | Example | Source structure | Upstream selection needed? |
|---|---|---|---|
| **Guideline selects** | ANC (2016) | Single guideline, alternative models considered, one recommended | No — DAK proceeds within the selected model |
| **Additive composition** | HIV (2024) | Multiple guidelines, single cascade with parameter-level country choices | No — no structural alternatives to choose among |
| **Guideline delegates** | Cervical cancer (2021) | Single guideline, multiple algorithms, selection delegated to country | **Yes** — DAK must scope to one algorithm and document the choice |

The distinction that matters for DAK authoring methodology is not whether the source guideline considered alternative pathways — most do — but whether the guideline **selects among them or delegates the selection to countries**. When the guideline selects (as ANC did), the DAK can proceed directly to interpretive work within the chosen pathway. When the source material composes additively (as HIV does), there is no structural fork to resolve. When the guideline delegates (as cervical cancer does), the DAK authoring process needs an explicit upstream step to document which pathway was chosen, on what grounds, and with what consequences for the DAK's scope.

The current DAK authoring methodology ([`authoring-workflow.md` (see [Methodology](methodology.html))](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md)) does not include such a step, and the register schema ([`register-schema.md` (see [Methodology](methodology.html))](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/register-schema.md)) has no interpretive category for it. The `scope` category introduced for `cc-000` is the closest approximation, but it treats the selection as a scoping boundary rather than as a structured decision with documented alternatives and selection criteria. The three-DAK comparison suggests the gap is real but narrow: it surfaces only for guidelines that present discrete alternative pathways and decline to choose among them. Whether this pattern recurs in other WHO guideline domains (STI, immunisations, family planning) has not been verified in this analysis.

## Implications for this case study

This analysis supports the choice of Algorithm 5 as the case study's modelled algorithm, while making the reasoning path explicit. The choice is not arbitrary and not driven by evidence-preference — it is driven by the infrastructure-dependent narrowing the guideline itself prescribes.

However, Algorithm 4 is an equally defensible choice for the same countries, and a complete methodology exercise might eventually model both. The difference between the two is not in the screening or treatment cascade but in the triage step, which affects the data inputs required (genotyping result versus VIA finding) and the point-of-care workflow (laboratory triage versus clinical triage).

The scope declaration in `cc-000` should be read with this analysis as background. The disclosure of biases in that entry — the case study author's high-resource-setting perspective, the selection of a "comfortable middle ground" — remains valid but can now be understood alongside the systematic narrowing that makes Algorithm 5 a reasonable choice on infrastructure grounds, not just a convenient one.

## References

### Primary guideline documents

- **WHO 2021 (July):** WHO guideline for screening and treatment of cervical pre-cancer lesions for cervical cancer prevention, second edition. Geneva: World Health Organization; 2021. ISBN 9789240030824. [WHO publication page](https://www.who.int/publications/i/item/9789240030824)
- **WHO 2021 (December):** WHO guideline for screening and treatment of cervical pre-cancer lesions for cervical cancer prevention, second edition: use of mRNA tests for human papillomavirus (HPV). Geneva: World Health Organization; 2021. ISBN 9789240040434. [WHO publication page](https://www.who.int/publications/i/item/9789240040434)
- **WHO 2024 (June):** WHO guideline for screening and treatment of cervical pre-cancer lesions for cervical cancer prevention: use of dual-stain cytology to triage women after a positive test for human papillomavirus (HPV). Geneva: World Health Organization; 2024. ISBN 9789240091658. [WHO publication page](https://www.who.int/publications/i/item/9789240091658)

### Implementation experience

- **Muliokela et al. 2024a:** Muliokela RK, Banda K, Hussen AM, et al. Implementation of WHO SMART Guidelines-Digital Adaptation Kits in Pathfinder Countries in Africa: Processes and Early Lessons Learned. *JMIR Medical Informatics*. [`../../../methodology/publications/3-muliokela.pdf`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/publications/3-muliokela.pdf). Countries: Ethiopia, Ghana, Malawi, Zambia, Zimbabwe.
- **Muliokela et al. 2022:** Muliokela R, Uwayezu G, Tran Ngoc C, et al. Integration of new digital antenatal care tools using the WHO SMART guideline approach: Experiences from Rwanda and Zambia. *Digital Health*. 2022;8. DOI: 10.1177/20552076221076256. [`../../../methodology/publications/4-muliokela.pdf`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/publications/4-muliokela.pdf). Countries: Rwanda, Zambia.
- **Tamrat et al. 2025:** Tamrat T, Muliokela RK, Hussen AM, et al. The Guideline Uptake in Digital Ecosystems (GUIDE) study: protocol for implementation research on the impact of WHO SMART guidelines digital adaptation kits to improve quality of care. *Health Research Policy and Systems*. 2025;23:122. DOI: 10.1186/s12961-025-01397-7. [`../../../methodology/publications/5-tamrat-et-al.pdf`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/publications/5-tamrat-et-al.pdf). Countries: Ethiopia, Ghana.
