# Indicators - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Indicators**

## Indicators

**Component 8 of the WHO SMART Guidelines L2 DAK structure.** This page enumerates the core indicators and performance metrics by which an implementation of Algorithm 5 can be monitored — screening coverage, cascade follow-through, losses to follow-up, clinical signal, and quality assurance.

Per [Section 3.1 of the SOP](https://smart.who.int/ig-starter-kit/l2_dak_authoring.html), Component 8 is a **"core set of indicators that need to be aggregated for decision-making, performance metrics, and subnational and national reporting, based on data that can feasibly be captured from a routine digital system, rather than survey-based tools."** Its organising principle is **collect once, use many** — indicators should reuse cascade data elements already captured in the course of clinical work, not require separate data collection exercises.

## Scope and authoring posture

**Algorithm-5 scope.** Consistent with the scope discipline applied across the DAK (see [cc-000](cc-000.md)), the indicators below are operationalised in Algorithm 5 cascade vocabulary — HPV DNA primary screening, VIA triage, thermal ablation / LLETZ / CKC treatment. Indicators whose numerators or denominators would require cascade artifacts this DAK does not model (cytology inadequate-sample rate, HPV mRNA positivity, dual-stain equivocal rate, colposcopy biopsy yield) are out of scope on the same grounds as recs 3a / 9 / 12 / 29 / 32 in the [recommendations table](interventions-and-recommendations.md#2021-07-guideline--general-population).

**Purpose versus definition.** The **purposes** behind most of these indicators are algorithm-neutral — screening coverage, cascade follow-through, suspected-cancer detection, and the WHO [Cervical Cancer Elimination Strategy](interventions-and-recommendations.md#source-documents) 90-70-90 targets do not prescribe an algorithm. The **definitions** in the table below are Algorithm-5-specific. A programme running a different cascade family would be pursuing the same targets but would need to re-express numerators in its own cascade vocabulary.

**Feasibility tiering — A versus B.** The SOP's **"feasibly captured from a routine digital system"** clause matters because cascade-tracking indicators and timing-based indicators place substantially higher infrastructure demands than period-count indicators. Each indicator below is tagged:

* **Tier A** — computable from counts within a single reporting period. Feasible from paper-based registers or minimally-integrated digital systems.
* **Tier B** — requires **longitudinal tracking of individual women** across multiple encounters within a cascade instance. Feasible only when the digital system links records across visits by stable patient identifier.

A programme may adopt Tier A indicators immediately and Tier B indicators as digital-system maturity allows. This staging is a deliberate feature of the indicator set, not a compromise.

**CDD gap, acknowledged.** Several indicators below reference data elements that are **not yet authored** in the [Core Data Dictionary](dictionary.md) — notably HPV DNA result, HPV sample date, triage date, treatment type and date, retest scheduled date, and retest actual date. These are listed in the [Data element dependencies](#data-element-dependencies) section and flagged as Phase-2 CDD work (either Kind-1 local authoring or Kind-3 proposals to a shared canonical dictionary).

**Phase-1 posture.** The ten indicators below are analytically derived from the Algorithm 5 cascade structure, the WHO elimination-strategy targets, and the operational concerns surfaced by the [Scheduling Logic](scheduling-logic.md) and [Business Processes](business-processes.md) components. SME validation inherits the same stratified deferral pattern as the earlier components — a screening programme manager in a low- or middle-income country setting is the specific SME domain whose consultation would close the validation gap on this page.

## Standard disaggregations

Declared once and referenced by every indicator below. Programmes are expected to report each indicator stratified across these dimensions.

| | |
| :--- | :--- |
| **Age band** | 25–29 (WLHIV only), 30–34, 35–39, 40–49, 50–64, 65+ |
| **HIV status** | General population, women living with HIV, HIV status unknown |
| **Facility** | By reporting facility; district and regional aggregations constructed from facility totals |
| **Reporting period** | Monthly, quarterly, annual — cohort windows as appropriate to the indicator |

The age bands align with the guideline's start-age thresholds (30 general, 25 WLHIV) and with the elimination-strategy 35-and-45 milestones. **HIV status unknown** is a deliberate third category; it should be treated as a data-quality flag, not folded into "general population", and its prevalence is itself an indirect programme-quality signal.

## Indicators

Ten indicators, organised in four clusters. Each indicator carries a numerator-and-denominator specification written at the prose-level of precision an L3 CQL author would need, but does not itself contain CQL.

### Coverage cluster — maps to WHO 90-70-90 "70% screened"

### IND-01 — Screening coverage within recommended interval

**Purpose.** Period-based coverage — the fraction of eligible women currently "up to date" on cervical cancer screening under the Algorithm 5 HPV DNA primary regime.

**Numerator.** Women in the denominator who have a valid HPV DNA primary-screen result recorded within the last 5 years (general population) or 3 years (WLHIV) as of the reporting date.

**Denominator.** All women in the facility catchment who are eligible for screening as of the reporting date — i.e., aged 30 or older (general population) or 25 or older (WLHIV) and not aged out of the programme per [cc-005](cc-005.md)'s stopping rule.

**Disaggregations.** Apply the standard disaggregations (age band × HIV status × facility × reporting period).

**Tier.** A — computable from a cross-sectional snapshot of the facility register plus HPV result records within the look-back window.

**Provenance.** [WHO Cervical Cancer Elimination Strategy](interventions-and-recommendations.md#source-documents) 70% target; interval values from [cc-005](cc-005.md).

### IND-02 — Lifetime coverage by elimination-strategy milestone ages

**Purpose.** Milestone-based coverage — the elimination-strategy phrasing ("each woman screened by age 35, and again by age 45") rather than rolling-window coverage. Captures programmes where women transit through the milestone ages during the reporting period.

**Numerator.** Women reaching age 35 (or 45) during the reporting period who have at least one HPV DNA primary-screen result recorded at any point before reaching that age.

**Denominator.** All women reaching age 35 (or 45) during the reporting period, in the facility catchment.

**Disaggregations.** Standard; split by milestone (35 vs 45) as an additional dimension.

**Tier.** A — birth-cohort-based. Feasible if the digital system holds a date of birth plus any recorded screening event.

**Provenance.** [WHO Cervical Cancer Elimination Strategy](interventions-and-recommendations.md#source-documents) milestone ages.

### Cascade follow-through cluster — maps to WHO 90-70-90 "90% pre-cancer treated"

### IND-03 — HPV positivity rate

**Purpose.** Epidemiological baseline — the underlying prevalence of HPV DNA positivity in the screened population. Informs cascade capacity planning (how many triage encounters per 1000 screens) and serves as a data-quality check (implausible values indicate assay or reporting issues).

**Numerator.** Primary screens in the reporting period with a valid HPV DNA result of **positive**.

**Denominator.** All primary screens in the reporting period with a valid HPV DNA result (positive or negative). Invalid / indeterminate results are excluded from both numerator and denominator and reported separately (IND-10's adequacy concept applies at the lab layer too).

**Disaggregations.** Standard.

**Tier.** A.

**Provenance.** Operational; aligns with national epidemiology reporting.

### IND-04 — Triage attendance rate

**Purpose.** First cascade-integrity indicator — the fraction of HPV-positive women who return for VIA triage within the programme-defined window.

**Numerator.** HPV-positive women whose result was reported in the period AND who had a VIA triage encounter recorded within the programme-defined reminder-plus-overdue window (see [Scheduling Logic — programme-level parameters](scheduling-logic.md#programme-level-parameters-deferred)).

**Denominator.** HPV-positive women whose result was reported in the period.

**Disaggregations.** Standard; additionally by **time since HPV+ result** for programmes that want to monitor the attendance curve.

**Tier.** B — requires linking HPV-result records to subsequent triage-encounter records by stable patient identifier.

**Provenance.** Operational cascade integrity.

### IND-05 — Treatment attendance rate

**Purpose.** Second cascade-integrity indicator — the fraction of triage-positive women who receive treatment within the programme-defined window. Primary measure against the 90% pre-cancer treatment target.

**Numerator.** Triage-positive women (result coded as ablation-eligible or non-ablation-eligible per [cc-003](cc-003.md)) in the period AND who received thermal ablation, LLETZ/LEEP, or cold-knife conization within the programme-defined window.

**Denominator.** Triage-positive women in the period, **excluding** those with the "suspected invasive cancer" result (routed to referral under [cc-003](cc-003.md), not to cascade treatment) and those with pregnancy-deferral under [cc-006](cc-006.md).

**Disaggregations.** Standard; additionally by triage-result stratum (ablation-eligible vs non-ablation-eligible).

**Tier.** B — requires linking triage results to treatment records.

**Provenance.** [WHO Cervical Cancer Elimination Strategy](interventions-and-recommendations.md#source-documents) 90% pre-cancer-treatment target.

### Cascade loss cluster — the inverse of follow-through; programme-manager-facing

### IND-06 — Attrition: HPV-positive without triage

**Purpose.** Programme operational — where losses occur, and to what magnitude. Complementary to IND-04.

**Numerator.** HPV-positive women in the period with **no** VIA triage encounter recorded within the programme-defined window.

**Denominator.** Same as IND-04's denominator.

**Disaggregations.** Standard; additionally by facility-level stratification to surface which facilities are driving losses.

**Tier.** B.

**Provenance.** Operational; directly surfaces the cascade point where the [Invitation workflow's **Identify overdue rescreen candidate**](business-processes.md#workflow-1--invitation) outreach should activate.

### IND-07 — Attrition: triage-positive without treatment

**Purpose.** Programme operational — second-stage cascade loss. Complementary to IND-05.

**Numerator.** Triage-positive women in the period with no treatment record within the programme-defined window. Same exclusions as IND-05 (cancer referrals, pregnancy deferrals).

**Denominator.** Same as IND-05's denominator.

**Disaggregations.** Standard; additionally by triage-result stratum.

**Tier.** B.

**Provenance.** Operational.

### IND-08 — Retest adherence

**Purpose.** Third cascade-integrity dimension — do women return for their scheduled retest? Applies to both the triage-negative retest (rec 11 / 31) and the post-treatment retest (rec 13 / 33).

**Numerator.** Women whose retest interval (triage-negative at 24/12 months, or post-treatment at 12 months per [cc-005](cc-005.md)) elapsed during the reporting period AND who have a subsequent cascade encounter recorded (a new primary screen or a retest-specific encounter, depending on programme configuration).

**Denominator.** All women whose retest interval elapsed during the reporting period.

**Disaggregations.** Standard; additionally by retest type (triage-negative vs post-treatment).

**Tier.** B.

**Provenance.** Operational; draws on the interval values owned by [cc-005](cc-005.md) and [cc-002](cc-002.md).

### Clinical-signal cluster

### IND-09 — Suspected invasive cancer detection rate at triage

**Purpose.** Clinical signal — the rate at which VIA triage flags findings suspicious for invasive cancer rather than treatable precancerous lesions. An unexpectedly low rate may suggest under-identification (quality concern); an unexpectedly high rate may reflect late-stage presentation (programme-coverage concern).

**Numerator.** VIA triage encounters in the period with the result coded as "suspicious for invasive cancer" per the operational definition in [cc-003](cc-003.md).

**Denominator.** All VIA triage encounters in the period with a recorded result.

**Disaggregations.** Standard.

**Tier.** A.

**Provenance.** Clinical monitoring; [cc-003](cc-003.md).

### Quality-assurance cluster

### IND-10 — VIA adequacy rate

**Purpose.** Quality assurance for the triage step. VIA's inter-observer variability was the quality-assurance concern that drove the original deprecation of VIA as a **primary** test (see [Algorithm Selection — Recommendation 1 context](algorithm-selection.md#recommendation-1-strong-hpv-dna-as-the-primary-screening-test)); the concern persists at the triage step, though with different clinical stakes. Low adequacy rates indicate training, supervision, or supply-chain issues (e.g., insufficient acetic acid, inadequate lighting).

**Numerator.** VIA encounters in the period with an adequate / interpretable result recorded.

**Denominator.** All VIA encounters attempted in the period (including those with inadequate, incomplete, or unrecorded results).

**Disaggregations.** Standard; additionally by provider / facility to surface training gaps.

**Tier.** A.

**Provenance.** Quality assurance; links to the [Algorithm Selection analysis](algorithm-selection.md#recommendation-1-strong-hpv-dna-as-the-primary-screening-test)'s treatment of VIA quality assurance.

## Data element dependencies

The table below maps each indicator to the data elements it reads. Elements currently in the [Core Data Dictionary](dictionary.md) are plain-text; elements **not yet authored** — Phase-2 CDD work — are **bolded**. The gap is real but bounded.

| | | |
| :--- | :--- | :--- |
| Age | In CDD (Kind 2, harvested from HIV DAK) | All |
| HIV status (**Living with HIV**) | In CDD (Kind 2) | All |
| Date of last cervical cancer screening test (`HIV.D.DE656`) | In CDD (Kind 2) | IND-01, IND-02, IND-08 |
| Prior screen result (`HIV.D.DE664`) | In CDD (Kind 2) | IND-01, IND-02 |
| VIA result (`HIV.D.DE668`) | In CDD (Kind 2) | IND-04, IND-05, IND-07, IND-09, IND-10 |
| **HPV DNA result (positive / negative / invalid)** | **Phase-2 gap**— candidate Kind-3 proposal | IND-01, IND-03, IND-04, IND-06 |
| **HPV sample collection date** | **Phase-2 gap** | IND-04, IND-06 |
| **Triage encounter date** | **Phase-2 gap** | IND-04, IND-06 |
| **Treatment type (ablation / LLETZ / CKC / none)** | **Phase-2 gap**— candidate Kind-3 proposal | IND-05, IND-07 |
| **Treatment date** | **Phase-2 gap** | IND-05, IND-07 |
| **Treatment status (delivered / deferred / referred)** | **Phase-2 gap** | IND-05, IND-07 |
| **Retest scheduled date** | **Phase-2 gap** | IND-08 |
| **Retest actual date** | **Phase-2 gap** | IND-08 |

Six of the ten indicators (IND-03, IND-04, IND-06 for the A-side HPV result; IND-05, IND-07 for treatment; IND-08 for retest) cannot be computed against the CDD in its current Phase-1 state. Closing this gap is the principal Phase-2 work item for this component and is tightly coupled to Phase-2 CDD work.

## Relation to other components

* **[Component 1 — Interventions and recommendations](interventions-and-recommendations.md).** Recs 8, 11, 13, 28, 31, 33 underwrite the interval logic that IND-01, IND-04, IND-05, IND-08 depend on for their "within window" phrasing.
* **[Component 4 — Business processes](business-processes.md).** Each cascade-integrity indicator (IND-04, IND-05, IND-06, IND-07, IND-08) measures the step-to-step transitions visible in the Overview and Follow-up workflows.
* **[Component 5 — Data dictionary](dictionary.md).** The Phase-2 CDD work named above is the principal dependency — without the bolded data elements authored, six of the ten indicators are L2-declarative-only. Kind-3 proposals to a shared canonical dictionary are consistent with the ecosystem contribution framing in the [Data Dictionary README](README.md).
* **[Component 6 — Decision logic](decision-logic.md).** The purposive DMN's **Due for Screening** decision is the computational anchor for IND-01's "within last 5y/3y" numerator. Parallel DMN tables for triage-negative retest and post-treatment retest (flagged Phase-2 in [Scheduling Logic](scheduling-logic.md#status)) would similarly anchor IND-08.
* **[Component 7 — Scheduling logic](scheduling-logic.md).** The **programme-defined window** phrasing used in IND-04, IND-05, IND-06, IND-07 resolves against the reminder lead time and overdue threshold parameters declared there as deferred country-adaptation parameters.

## Status

**Draft — Phase 1 of Component 8 authoring (2026-04-22).** Ten indicators analytically derived from the Algorithm 5 cascade and the WHO Cervical Cancer Elimination Strategy 90-70-90 targets, organised in four clusters (coverage, cascade follow-through, cascade loss, clinical signal, quality assurance — the first two reflecting the 90-70-90 targets directly). Each indicator carries a numerator-denominator specification, standard disaggregations, a feasibility tier (A or B), and a provenance pointer.

**Principal Phase-2 dependency: CDD data element authoring.** Six of the ten indicators read data elements not yet in the [Core Data Dictionary](dictionary.md). Authoring them — either as Kind-1 local elements or Kind-3 proposals to a shared canonical dictionary — is the gate on making this component executable. Until that happens, the indicators on this page are L2-declarative: the **intent** is specified, the **computation** is not yet instrumentable.

**Phase-2 follow-on work for this component, beyond the CDD dependency:**

* L3 Measure / CQL authoring — translating each indicator's prose numerator/denominator into FHIR `Measure` resources with population criteria expressed in CQL, in the style of CMS eCQM artifacts. Out of scope for L2 but the natural next artifact once the CDD gap is closed.
* SME validation — review by a screening programme manager in a low- or middle-income country, particularly on the feasibility tiering (A vs B) and whether the "programme-defined window" phrasing is workable at district-level reporting cadence.
* Cross-DAK indicator reuse analysis — the WHO HIV DAK and ANC DAK may publish comparable cascade-integrity indicators; harvesting their population-criteria patterns rather than re-authoring is consistent with the Kind-2 pattern already used in the CDD.

