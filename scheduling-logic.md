# Scheduling Logic - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Scheduling Logic**

## Scheduling Logic

**Component 7 of the WHO SMART Guidelines L2 DAK structure.** This page declares the scheduling logic operative in this DAK — the interval rules that govern when a woman's next encounter with the cascade should occur, and the programme-level parameters a country must set to operationalise reminders and overdue tracking.

Per [Section 3.1 of the SOP](https://smart.who.int/ig-starter-kit/l2_dak_authoring.html), Component 7 covers **"the timing rules that drive reminders, next-appointment scheduling, and follow-up intervals."** It is adjacent to but distinct from Component 6 (decision logic), which handles clinical decisions like eligibility and triage disposition.

## Scope

This page is an **index and programme-parameter declaration**, not a re-statement. The interval values themselves live in the [Interpretation Register](register.md) and the purposive [Decision Logic](decision-logic.md) — scheduling logic reads those values, it does not own them. Where the guideline is silent on operational detail (reminder cadence, overdue threshold, treatment-window tracking), this page names the gap as a **country-adaptation parameter** rather than inventing a value.

## Scheduling rules by trigger

Each row below names a cascade event that produces a scheduled next encounter, the rule that governs the interval, and the artifact where the rule is authoritatively owned.

| | | |
| :--- | :--- | :--- |
| HPV-negative primary screen | 5–10 year interval (general); 3–5 year (WLHIV) | [cc-005](cc-005.md); recs 8 / 28 |
| HPV-positive, VIA-negative triage | 24-month retest (general); 12-month (WLHIV) | [cc-005](cc-005.md); recs 11 / 31 |
| Post-treatment retest (ablation or excision) | 12-month single retest; WLHIV collapsed from "double follow-up" per the purposive posture | [cc-002](cc-002.md),[cc-005](cc-005.md); recs 13 / 33 |
| Suspected invasive cancer identified at triage | Cascade exit; no scheduled DAK-side retest | [cc-003](cc-003.md) |
| Pregnancy identified at treatment | Defer treatment; re-enter Triage after pregnancy and defined recovery interval | [cc-006](cc-006.md); rec 41 (GPS) |

The BPMN [Follow-up workflow](business-processes.md#workflow-5--follow-up) is where these rules manifest as concrete **Schedule next routine screening**, **Schedule triage-negative retest**, and **Schedule post-treatment retest** activities. The DMN decision tables under [Decision Logic](decision-logic.md) compute whether a given woman is due for a next encounter given her cascade state and the applicable interval.

## Programme-level parameters (deferred)

Three scheduling-related choices are **not** specified by the 2021 guideline and must be set by each implementing programme. They are named here so that the gap is visible rather than implicit.

| | | |
| :--- | :--- | :--- |
| **Reminder lead time** | How far in advance of a scheduled encounter a reminder fires (to the target client and/or the community health worker) | The guideline addresses clinical interval values, not operational reminder cadence. Country programmes optimise this against SMS costs, adherence data, and infrastructure. |
| **"Overdue" threshold** | How far past a scheduled date before a woman is flagged for active outreach by the community health worker (the**Identify overdue rescreen candidate**activity in the Invitation workflow) | Same reasoning — the guideline does not define overdue. Country programmes tune this against realistic re-engagement windows. |
| **Treatment-within-6-months tracking** | How the**"treat within six months"**good practice statement (rec 41 GPS) is operationalised — whether as a scheduled reminder on the patient record, a programme-level exception list, or solely provider discretion | Rec 41 is a good practice statement, not a hard scheduling rule with a guideline-specified cadence. Programmes choose whether to instrument it as a schedulable event. |

These three parameters are the scheduling-logic face of the SOP's 80/20 rule: the cascade-general scheduling structure is encoded above; the operational 20% that varies by country context is declared here and left open.

## Relation to other components

* **[Component 1 — Interventions and recommendations](interventions-and-recommendations.md).** Recs 8, 11, 13, 28, 31, 33, and 41 are the L1 provenance for the intervals above.
* **[Component 4 — Business processes](business-processes.md).** The Follow-up workflow's three Schedule activities are the BPMN touchpoints where scheduling logic triggers; the Invitation workflow's **Identify overdue rescreen candidate** activity is where the overdue threshold gets applied.
* **[Component 5 — Data dictionary](dictionary.md).** The data elements **Date of last cervical cancer screening test** (`HIV.D.DE656`), **Prior screen result** (`HIV.D.DE664`), and **VIA result** (`HIV.D.DE668`) are the inputs to interval calculation; they are harvested from the WHO HIV DAK with provenance (Kind 2).
* **[Component 6 — Decision logic](decision-logic.md).** The purposive DMN's **Due for Screening** decision implements the interval arithmetic for the HPV-negative case; analogous logic for triage-negative retest and post-treatment retest is a gap flagged in [cc-005](cc-005.md).

## Status

**Draft — Phase 1 of Component 7 authoring (2026-04-22).** This page is an index and deferred-parameter declaration. No new scheduling rules are introduced here; all interval values are authoritatively owned by the interpretation register and the purposive DMN. Three country-adaptation parameters (reminder lead time, overdue threshold, 6-month treatment window tracking) are named as deferred.

**Phase-2 work for this component, should it be undertaken:**

* Author DMN decision tables for triage-negative retest and post-treatment retest interval calculation, parallel to the existing **Due for Screening** decision.
* Produce a programme-parameters reference page collecting all SOP-identified country-adaptation parameters across Components 4–9 in one place, with suggested ranges.
* Integrate rec 41 (6-month treatment) as a schedulable event on the patient record, with an explicit **Treat-by** date computed at triage-positive and a **Late-treatment list** surfaced for programme-manager review.

