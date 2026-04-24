# Decision Tables - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Decision Tables**

## Decision Tables

This page presents the decision tables from both the purposive and textualist DMN artifacts. The purposive tables encode the interpretive resolutions documented in the [Interpretation Register](register.md). The textualist tables preserve the 2021-07 guideline language verbatim. See [Decision Logic](decision-logic.md) for the DRD diagrams and a summary of differences.

## Purposive Decision Tables

**Auto-generated from `purposive.dmn` by `render-decision-tables.py`.**

### Eligible For Screening

**Decision:** Eligible For Screening

**Decision ID:** `CC.A.eligibility_p`

**Hit Policy:** UNIQUE

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | true | [30..49] | false | true | every 10 years | Rec 1; GPS 7 prioritizes age 30–49. Interval resolved per cc-005 to 10 years (upper bound of Rec 8 range). |
| 2 | true | <30 | false | false | **null** | Below general population screening age |
| 3 | true | >49 | not(null) | false | **null** | Above screening age range, HIV status known (both populations); null-HIV at age>49 delegated to catch-all per cc-008 |
| 4 | true | [25..49] | true | true | every 5 years | Rec 21; WLHIV screening starts at age 25. Interval resolved per cc-005 to 5 years (upper bound of Rec 28 range). |
| 5 | true | <25 | true | false | **null** | Below WLHIV screening age |
| 6 | false | **(any)** | **(any)** | false | **null** | Per L1 terminology; see Interpretation Register |
| 7 | true | **null** | **(any)** | false | **null** | Catch-all: woman with null age |
| 8 | true | not(null) | **null** | false | **null** | Catch-all: woman with valid age but null HIV status |
| 9 | **null** | **(any)** | **(any)** | false | **null** | Catch-all: null Client Is Woman |

### Due for Screening

**Decision:** Due for Screening

**Decision ID:** `CC.B.due_screening_p`

**Hit Policy:** UNIQUE

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | true | **(any)** | **null** | **(any)** | never screened — screen now | Never screened (YearsSinceLastScreen = null) — screen now regardless of interval or prior result |
| 2 | true | every 10 years | <10 | negative | not yet due | General population, negative prior, before rescreen target (cc-005: <10 years since last screen) |
| 3 | true | every 10 years | >=10 | negative | due | General population, negative prior, at or past rescreen target (cc-005: >=10 years; point-estimate two-bucket encoding — see cc-005 rationale) |
| 4 | true | every 5 years | <5 | negative | not yet due | WLHIV, negative prior, before rescreen target (cc-005: <5 years since last screen) |
| 5 | true | every 5 years | >=5 | negative | due | WLHIV, negative prior, at or past rescreen target (cc-005: >=5 years; point-estimate two-bucket encoding — see cc-005 rationale) |
| 6 | true | **(any)** | **(any)** | positive | prior positive — enter triage pathway | Prior positive result — bypass interval check, enter triage pathway |
| 7 | false | **(any)** | **(any)** | **(any)** | not eligible | Not eligible (upstream EligibleForScreening = false) — no screening indicated |

### Triage Decision

**Decision:** Triage Decision

**Decision ID:** `CC.C.triage_p`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | positive | **(any)** | VIA positive — eligible for treatment | VIA positive — proceed to treatment eligibility assessment |
| 2 | negative | false | VIA negative — repeat HPV test in 2 years | VIA negative, general population — repeat HPV in 2 years |
| 3 | negative | true | VIA negative — repeat HPV test in 1 year | VIA negative, WLHIV — repeat HPV in 1 year |
| 4 | suspected cancer | **(any)** | suspected cancer — refer for evaluation and biopsy | Suspected cancer — refer for evaluation and biopsy |
| 5 | **null** | **(any)** | unknown VIA result | Catch-all: unrecognized VIA result |

### Ablation Eligibility

**Decision:** Ablation Eligibility

**Decision ID:** `CC.D.ablation_p`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | true | **(any)** | false | Suspected cancer — not eligible for ablation |
| 2 | false | Type 1 | true | TZ Type 1 — eligible for ablation |
| 3 | false | Type 2 | true | TZ Type 2 — eligible for ablation |
| 4 | false | Type 3 | false | TZ Type 3 — not eligible for ablation, requires excision |
| 5 | **null** | **(any)** | false | Catch-all: null suspicion of cancer |
| 6 | false | **null** | false | Catch-all: null TZ type |

### Treatment Decision

**Decision:** Treatment Decision

**Decision ID:** `CC.D.treatment_p`

**Hit Policy:** FIRST

| | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | VIA positive — eligible for treatment | **(any)** | true | defer treatment until after pregnancy | Pregnancy deferral per GPS 41 (cc-006): defer ablation or LLETZ until after pregnancy. Fires before ablate/lletz rules under FIRST hit policy. |
| 2 | VIA positive — eligible for treatment | true | **(any)** | ablative treatment | VIA positive, eligible for ablation — ablative treatment (non-pregnant or pregnancy status unknown; null IsPregnant falls through to this rule per cc-006 implementation note) |
| 3 | VIA positive — eligible for treatment | false | **(any)** | LLETZ | VIA positive, not eligible for ablation — LLETZ (non-pregnant or pregnancy status unknown) |
| 4 | VIA negative — repeat HPV test in 2 years | **(any)** | **(any)** | no treatment — repeat HPV in 2 years | VIA negative, general population — no treatment, repeat HPV (pregnancy irrelevant; no procedure to defer) |
| 5 | VIA negative — repeat HPV test in 1 year | **(any)** | **(any)** | no treatment — repeat HPV in 1 year | VIA negative, WLHIV — no treatment, repeat HPV (pregnancy irrelevant; no procedure to defer) |
| 6 | suspected cancer — refer for evaluation and biopsy | **(any)** | **(any)** | refer for evaluation, biopsy and further management | Suspected cancer — refer for evaluation (per cc-006: pregnancy does NOT defer cancer evaluation; urgency is clinically appropriate regardless of pregnancy status) |
| 7 | **null** | **(any)** | **(any)** | unknown triage status | Catch-all: unrecognized triage status |

### Follow-up Decision

**Decision:** Follow-up Decision

**Decision ID:** `CC.E.followup_p`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ablative treatment | CIN3 or less | post-treatment follow-up after 1 year | Ablative treatment, histology CIN3 or less — follow-up after 1 year |
| 2 | ablative treatment | cancer | cancer — further management | Ablative treatment, histology shows cancer |
| 3 | LLETZ | CIN3 or less | post-treatment follow-up after 1 year | LLETZ, histology CIN3 or less — follow-up after 1 year |
| 4 | LLETZ | cancer | cancer — further management | LLETZ, histology shows cancer |
| 5 | no treatment — repeat HPV in 2 years | **(any)** | repeat HPV test after 2 years | No treatment, repeat HPV in 2 years (general population) |
| 6 | no treatment — repeat HPV in 1 year | **(any)** | repeat HPV test after 1 year | No treatment, repeat HPV in 1 year (WLHIV) |
| 7 | refer for evaluation, biopsy and further management | **(any)** | evaluation, biopsy and further management | Referred for evaluation — follow management pathway |
| 8 | **null** | **(any)** | unknown treatment plan | Catch-all: unrecognized treatment plan |

## Textualist Decision Tables

**Auto-generated from `textualist.dmn` by `render-decision-tables.py`.**

### Eligible For Screening

**Decision:** Eligible For Screening

**Decision ID:** `CC.A.eligibility_t`

**Hit Policy:** UNIQUE

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | true | [30..49] | false | true | every 5 to 10 years | Rec 1; GPS 7 prioritizes age 30–49 |
| 2 | true | <30 | false | false | **null** | Below general population screening age |
| 3 | true | >49 | **(any)** | false | **null** | Above screening age range (both populations) |
| 4 | true | [25..49] | true | true | every 3 to 5 years | Rec 21; WLHIV screening starts at age 25 |
| 5 | true | <25 | true | false | **null** | Below WLHIV screening age |
| 6 | false | **(any)** | **(any)** | false | **null** | Per L1 terminology; see Interpretation Register |
| 7 | true | **null** | **(any)** | false | **null** | Catch-all: woman with null age |
| 8 | **null** | **(any)** | **(any)** | false | **null** | Catch-all: null Client Is Woman |

### Due for Screening

**Decision:** Due for Screening

**Decision ID:** `CC.B.due_screening_t`

**Hit Policy:** UNIQUE

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | true | **(any)** | **null** | **(any)** | never screened — screen now | Never screened (YearsSinceLastScreen = null) — screen now regardless of interval or prior result |
| 2 | true | every 5 to 10 years | <5 | negative | not yet due | General population, negative prior, before rescreen window (<5 years since last screen) |
| 3 | true | every 5 to 10 years | [5..10] | negative | within screening window | General population, negative prior, within rescreen window (5–10 years since last screen) |
| 4 | true | every 5 to 10 years | >10 | negative | past screening window | General population, negative prior, past rescreen window (>10 years) — overdue |
| 5 | true | every 3 to 5 years | <3 | negative | not yet due | WLHIV, negative prior, before rescreen window (<3 years since last screen) |
| 6 | true | every 3 to 5 years | [3..5] | negative | within screening window | WLHIV, negative prior, within rescreen window (3–5 years since last screen) |
| 7 | true | every 3 to 5 years | >5 | negative | past screening window | WLHIV, negative prior, past rescreen window (>5 years) — overdue |
| 8 | true | **(any)** | **(any)** | positive | prior positive — enter triage pathway | Prior positive result — bypass interval check, enter triage pathway |
| 9 | false | **(any)** | **(any)** | **(any)** | not eligible | Not eligible (upstream EligibleForScreening = false) — no screening indicated |

### Triage Decision

**Decision:** Triage Decision

**Decision ID:** `CC.C.triage_t`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | positive | **(any)** | VIA positive — eligible for treatment | VIA positive — proceed to treatment eligibility assessment |
| 2 | negative | false | VIA negative — repeat HPV test in 2 years | VIA negative, general population — repeat HPV in 2 years |
| 3 | negative | true | VIA negative — repeat HPV test in 1 year | VIA negative, WLHIV — repeat HPV in 1 year |
| 4 | suspected cancer | **(any)** | suspected cancer — refer for evaluation and biopsy | Suspected cancer — refer for evaluation and biopsy |
| 5 | **null** | **(any)** | unknown VIA result | Catch-all: unrecognized VIA result |

### Ablation Eligibility

**Decision:** Ablation Eligibility

**Decision ID:** `CC.D.ablation_t`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | true | **(any)** | false | Suspected cancer — not eligible for ablation |
| 2 | false | Type 1 | true | TZ Type 1 — eligible for ablation |
| 3 | false | Type 2 | true | TZ Type 2 — eligible for ablation |
| 4 | false | Type 3 | false | TZ Type 3 — not eligible for ablation, requires excision |
| 5 | **null** | **(any)** | false | Catch-all: null suspicion of cancer |
| 6 | false | **null** | false | Catch-all: null TZ type |

### Treatment Decision

**Decision:** Treatment Decision

**Decision ID:** `CC.D.treatment_t`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | VIA positive — eligible for treatment | true | ablative treatment | VIA positive, eligible for ablation — ablative treatment |
| 2 | VIA positive — eligible for treatment | false | LLETZ | VIA positive, not eligible for ablation — LLETZ |
| 3 | VIA negative — repeat HPV test in 2 years | **(any)** | no treatment — repeat HPV in 2 years | VIA negative, general population — no treatment, repeat HPV |
| 4 | VIA negative — repeat HPV test in 1 year | **(any)** | no treatment — repeat HPV in 1 year | VIA negative, WLHIV — no treatment, repeat HPV |
| 5 | suspected cancer — refer for evaluation and biopsy | **(any)** | refer for evaluation, biopsy and further management | Suspected cancer — refer for evaluation |
| 6 | **null** | **(any)** | unknown triage status | Catch-all: unrecognized triage status |

### Follow-up Decision

**Decision:** Follow-up Decision

**Decision ID:** `CC.E.followup_t`

**Hit Policy:** UNIQUE

| | | | | |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ablative treatment | CIN3 or less | post-treatment follow-up after 1 year | Ablative treatment, histology CIN3 or less — follow-up after 1 year |
| 2 | ablative treatment | cancer | cancer — further management | Ablative treatment, histology shows cancer |
| 3 | LLETZ | CIN3 or less | post-treatment follow-up after 1 year | LLETZ, histology CIN3 or less — follow-up after 1 year |
| 4 | LLETZ | cancer | cancer — further management | LLETZ, histology shows cancer |
| 5 | no treatment — repeat HPV in 2 years | **(any)** | repeat HPV test after 2 years | No treatment, repeat HPV in 2 years (general population) |
| 6 | no treatment — repeat HPV in 1 year | **(any)** | repeat HPV test after 1 year | No treatment, repeat HPV in 1 year (WLHIV) |
| 7 | refer for evaluation, biopsy and further management | **(any)** | evaluation, biopsy and further management | Referred for evaluation — follow management pathway |
| 8 | **null** | **(any)** | unknown treatment plan | Catch-all: unrecognized treatment plan |

