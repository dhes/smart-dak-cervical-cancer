# Cervical Cancer Case Study — Core Data Dictionary (minimum-viable)

**Scope.** L2 face of every input and output of [`../textualist.dmn`](downloads.html), plus two deferred rows (pregnancy, vaccination) that map to planned register entries. The column structure follows the SMART Guidelines DAK template as closely as markdown permits. See the [CDD README](README.html) for the column semantics, the Kind classification, the L2/L3 boundary, and the tri-purpose framing that motivates the partition.

**Status.** First pass, 2026-04-11. Drafted from the harvest snapshot at [`../narrative/harvested-cdes-from-existing-daks.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/harvested-cdes-from-existing-daks.md) (harvested 2026-04-10). Kind 2 rows do not carry source commit hashes in this first pass; the commit-hash backfill is Phase B work per `silly-gathering-flamingo.md` (local plan file, not published) (the plan file in the user's local Claude state — not a committed project artifact, but the decision record for this work).

**L2/L3 boundary discipline.** Every L3 column below (ICD-11, SNOMED CT, LOINC, ICHI, ICF, FHIR Resource, FHIR Profile, Canonical URI) is intentionally blank. These are L3 concerns — to be bound by a terminology specialist or FHIR implementer at the point of country adaptation — and leaving them blank is a feature, not an omission. The per-row `Terminology Intent` column carries natural-language meaning to inform but not prescribe the L3 binding. See [`../../../methodology/authoring-workflow.md#the-l2-boundary-rule`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md) lines 113–142.

## Summary table

| # | Element | Data Element ID | Data Type | Kind | Source / Linkage |
|---|---|---|---|---|---|
| 1 | Age in years | `HIV.A.DE-age` (demographic) | number | 2 | HIV demographic; textualist input `AgeInYears` |
| 2 | Sex | `HIV.A.DE25` | Coding | 2 | HIV.A Registration; textualist input `ClientIsWoman` via `Sex = Female`; see [`cc-001`](cc-001.html) |
| 3 | Living With HIV | `HIV.B.DE-hiv-status` | boolean | 2 | HIV.B HIV-status cluster; textualist input `LivingWithHIV`; see [`cc-002`](cc-002.html) |
| 4 | Date of last cervical cancer screening test | `HIV.D.DE656` | DateTime | 2 | HIV.D Care-Treatment; upstream source of textualist-derived `YearsSinceLastScreen` |
| 5 | Years since last screen (derived) | `CC.B.DE01` | number | 1 | derived from row 4; textualist input `YearsSinceLastScreen` |
| 6 | Prior screen result | `HIV.D.DE664` | Coding | 2 | HIV.D Care-Treatment ("HPV-DNA cervical cancer screening test result"); textualist input `PriorResult` |
| 7 | VIA result | `HIV.D.DE668` | Coding | 2 | HIV.D Care-Treatment ("VIA cervical cancer screening test result"); textualist input `VIAResult` |
| 8 | Suspicion of cancer (clinical judgment) | `CC.C.DE01` | boolean | 1 | novel; textualist input `SuspicionOfCancer`; see [`cc-003`](cc-003.html) |
| 9 | Transformation zone type | `CC.D.DE01` | Coding | 1 | novel; textualist input `TZType` |
| 10 | Histology result | `CC.E.DE01` | Coding | 1 | novel; textualist input `HistologyResult` |
| 11 | Eligible for screening | `CC.A.DE01` | boolean | 1 | textualist output of Eligible For Screening decision |
| 12 | Screening interval | `CC.A.DE02` | string | 1 | textualist output (range string); purposive output (point estimate per [`cc-005`](cc-005.html)) |
| 13 | Screening status | `CC.B.DE02` | string | 1 | textualist output (3-bucket); purposive output (2-bucket "due"/"not yet due" per [`cc-005`](cc-005.html)) |
| 14 | Triage status | `CC.C.DE02` | string | 1 | textualist output of Triage Decision |
| 15 | Ablation eligible | `CC.D.DE02` | boolean | 1 | textualist output of Ablation Eligibility decision |
| 16 | Treatment plan | `CC.D.DE03` | string | 1 | textualist output of Treatment Decision |
| 17 | Follow-up plan | `CC.E.DE02` | string | 1 | textualist output of Follow-up Decision |
| 18 | Pregnancy status | `HIV.B.DE160`-family (candidate) | boolean | 2 | purposive-only input to Treatment Decision per [`cc-006`](cc-006.html); not consumed by textualist |
| 19 | Vaccination status | `IMMZ.*` (candidate cluster) | Coding | 2 (defer) | not consumed by textualist; stub for [`cc-004`](cc-004.html) |

---

## Detailed rows

Each row below carries the full L2 column set. L3 columns are shown but left blank by design. The summary table above is the quick-scan view; this is the authoritative per-row content.

### Row 1 — Age in years

- **Activity ID:** `CC.A` (Eligible For Screening) and `CC.B` (Due for Screening)
- **Data Element ID:** `HIV.A.DE-age` (placeholder; in the harvest snapshot, HIV.A Registration contains the date-of-birth and age elements; exact DE ID to be fixed in a re-harvest with commit capture in Phase B)
- **Label:** Age in years
- **Description:** The client's age in years, derived from date of birth.
- **Data Type:** number
- **Input Options:** N/A (continuous)
- **Required:** R
- **Linkages (DMN):** `textualist.dmn#CC.A.eligibility_t` (Eligible For Screening); used as the second input `AgeInYears` in rules `DecisionRule_1yry35i` (30–49 general population), `DecisionRule_17r1uyq` (<30), `DecisionRule_1l3rrvn` (>49), `DecisionRule_1925hkc` (25–49 WLHIV), `DecisionRule_1gyepae` (<25 WLHIV), and the null catch-all `DecisionRule_catchall_s_nullage`
- **Annotations:** The textualist computes `AgeInYears` from a date-of-birth input at evaluation time. Countries whose EHR only carries a date field will need to compute the derivation; countries whose EHR exposes a derived age may populate directly.
- **Terminology Intent:** Age at the time of screening evaluation, calibrated in completed years, expressed as a non-negative integer.
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** HIV.A Registration (date-of-birth / age cluster — exact DE ID pending commit-captured re-harvest)
- **Source Commit:** *(blank; backfill planned in Phase B)*
- **Reuse Intent:** reuse-as-is
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 2 — Sex (populates textualist `ClientIsWoman`)

- **Activity ID:** `CC.A` (Eligible For Screening)
- **Data Element ID:** `HIV.A.DE25`
- **Label:** Sex
- **Description:** Sex of the client assigned at birth.
- **Data Type:** Coding
- **Input Options:** Female (`HIV.A.DE26`), Male (`HIV.A.DE27`), Other (`HIV.A.DE28`)
- **Required:** R
- **Linkages (DMN):** `textualist.dmn#CC.A.eligibility_t` (Eligible For Screening); populates the first input `ClientIsWoman` as `ClientIsWoman = (Sex = Female)`. Used by rules `DecisionRule_1yry35i`, `DecisionRule_17r1uyq`, `DecisionRule_1l3rrvn`, `DecisionRule_1925hkc`, `DecisionRule_1gyepae`, `DecisionRule_05t3z2o`, and the null catch-all `DecisionRule_catchall_s_nullwoman`. The textualist rule `DecisionRule_05t3z2o` carries the description `"Per L1 terminology; see Interpretation Register"` as a forward reference to `cc-001`.
- **Linkages (Register):** [`cc-001`](cc-001.html) — this row is the first-case-study resolution of the population-definition question. See the "Deferred as purposive refinement: `HasCervix`" section below for the candidate element's shape and the conditions under which it would become a row.
- **Annotations:** The textualist input name `ClientIsWoman` is preserved as-is; a future purposive DMN authoring pass may rename it to `ClientSex` or similar to reduce the sex/gender/identity conflation implicit in the current name. That rename is not bundled into this documentary CDD addition because it has test-suite impact.
- **Terminology Intent:** The patient attribute representing sex as recorded in the EHR at registration. In the textualist, `ClientIsWoman = true` whenever `Sex = Female`, consistent with the 2021-07 guideline's Recommendation 1 language ("women") and with deployment reality in LMIC public-sector EHRs that do not carry anatomical-inventory fields. The guideline's Section 3.1 broader population (transgender men and non-binary / intersex individuals with a cervix) is served by targeted outreach in a parallel workflow and is not represented in this element; see the "Deferred as purposive refinement: `HasCervix`" block below for the register-level treatment of the broader and narrower refinements this element does not encode. See [`cc-001`](cc-001.html) for the interpretive reasoning and its first-case-study resolution.
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** `HIV.A.DE25`
- **Source Commit:** *(blank; backfill planned in Phase B)*
- **Reuse Intent:** reuse-as-is
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3; `Patient.gender` is the obvious L3 FHIR target but that decision is deferred to the L3 binding step at country adaptation time)*

### Row 3 — Living With HIV

- **Activity ID:** `CC.A` (Eligible For Screening), `CC.C` (Triage Decision)
- **Data Element ID:** `HIV.B.DE-hiv-status` (placeholder; exact DE ID for the generic HIV-status boolean pending commit-captured re-harvest)
- **Label:** Living with HIV
- **Description:** Whether the client is a person living with HIV.
- **Data Type:** boolean
- **Input Options:** true / false / null
- **Input Option Semantics:** `true` = the client is documented or disclosed as living with HIV at the time of the screening encounter. `false` = the client is documented-negative for HIV, *or* presumed-negative at the encounter per the country's operational convention for absent HIV records; the boolean does not distinguish these two cases. `null` = HIV status is not available at the screening decision point (never tested, records incomplete, or linkage to the HIV care system failed); handling is governed by [`cc-008`](cc-008.html).
- **Required:** R
- **Linkages (DMN):** `textualist.dmn#CC.A.eligibility_t` (Eligible For Screening) rules `DecisionRule_1yry35i`, `DecisionRule_1925hkc`, `DecisionRule_1gyepae` (the former null-HIV catch-all `DecisionRule_catchall_s_nullhiv` was removed per [`cc-008`](cc-008.html) to restore guideline-silence fidelity for absent HIV status). `purposive.dmn#CC.A.eligibility_p` (Eligible For Screening) retains a narrowed catch-all `DecisionRule_catchall_s_nullhiv` encoding the fail-closed policy per [`cc-008`](cc-008.html); the above-age-range rule `DecisionRule_1l3rrvn` is correspondingly narrowed to `LivingWithHIV = not(null)` to avoid overlap. Also `textualist.dmn#CC.C.triage_t` (Triage Decision) rules `DecisionRule_triage_neg_gen` and `DecisionRule_triage_neg_hiv` (population-specific re-screen interval after VIA-negative triage).
- **Linkages (Register):** [`cc-002-wlhiv-operationalisation.md`](cc-002.html) — this row is the data element the WLHIV register entry operates on. The `evidence_volatile: true` flag on `cc-002` applies to this element: the encoding as a single boolean is a deliberate simplification over the finer-grained HIV-status stratification (CD4, viral suppression, ART duration) that the evidence base is moving toward. [`cc-008-hiv-status-absent.md`](cc-008.html) — covers the distinct question of how the cascade behaves when this element is absent or unknown at the screening decision point; selects fail-closed in the purposive and guideline-silence-revealing in the textualist.
- **Annotations:** The textualist treats this as a patient-level boolean throughout the cascade. The boolean's three input options map to more than three real-world states: `false` collapses "documented-negative" and "presumed-negative-at-encounter," and `null` covers at least three distinct missingness modes (never tested, records incomplete, linkage failed). The stratification question is addressed by [`cc-002`](cc-002.html); the missingness question is addressed by [`cc-008`](cc-008.html). Countries where HIV status is held in a separate HIV-care system (HIV-specific EMR module or standalone system like SmartCare) need an L3 data-linkage step to populate this at the screening encounter. A future register entry may refine the encoding to a finer-grained element or to a set of related elements covering viral-suppression status.
- **Terminology Intent:** Whether the client is a person living with HIV at the time of the screening encounter. A `true` value triggers the WLHIV-specific screening-age threshold (25 rather than 30) and interval (3–5 years rather than 5–10 years) per 2021-07 Recommendations 21 and 22, and the WLHIV-specific post-treatment follow-up schedule per Recommendation 33 (the "double follow-up" — see [`addendum-2021-12-reconciliation.md` (see [source repo](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md))](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md)).
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** HIV.B HIV-status cluster (exact DE ID pending commit-captured re-harvest)
- **Source Commit:** *(blank)*
- **Reuse Intent:** reuse-as-is
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 4 — Date of last cervical cancer screening test

- **Activity ID:** `CC.B` (Due for Screening — upstream source for the derived input)
- **Data Element ID:** `HIV.D.DE656`
- **Label:** Date of cervical cancer screening test
- **Description:** The date on which the client's most recent cervical cancer screening test was performed.
- **Data Type:** DateTime
- **Input Options:** N/A
- **Required:** O
- **Linkages (DMN):** Upstream source of the textualist-derived input `YearsSinceLastScreen` (row 5). Not consumed directly by any DMN decision rule; the derivation `YearsSinceLastScreen = now() - DateOfLastScreening` is performed outside the decision table.
- **Annotations:** Included as a row so the data lineage from harvested upstream source to derived textualist input is documented. Countries whose EHR stores the last screen date can populate this directly; countries whose EHR only stores a years-since-last-screen computation can skip this row and populate row 5 directly.
- **Terminology Intent:** The calendar date on which the most recent cervical cancer screening test was performed for this client. If the client has never been screened, this element is null and the textualist `YearsSinceLastScreen` is also null.
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** `HIV.D.DE656`
- **Source Commit:** *(blank)*
- **Reuse Intent:** reuse-as-is
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 5 — Years since last screen (derived)

- **Activity ID:** `CC.B` (Due for Screening)
- **Data Element ID:** `CC.B.DE01`
- **Label:** Years since last screen
- **Description:** Years elapsed between the date of the client's most recent cervical cancer screening test and the current screening evaluation.
- **Data Type:** number
- **Input Options:** N/A (continuous; null if never screened)
- **Required:** C (conditional — null when `DateOfLastScreening` is null)
- **Linkages (DMN):** `textualist.dmn#CC.B.due_screening_t` (Due for Screening); third input `YearsSinceLastScreen` in rules `DecisionRule_0hrknh0` (never screened), `DecisionRule_1kowjor` (`<5` general pop), `DecisionRule_1623wc6` (`[5..10]`), `DecisionRule_0d7mryk` (`>10`), `DecisionRule_0v20651` (`<3` WLHIV), `DecisionRule_0esotny` (`[3..5]`), `DecisionRule_018yt1f` (`>5`).
- **Annotations:** Derived from row 4 at evaluation time. The textualist takes this as a direct input; the derivation happens upstream.
- **Terminology Intent:** The elapsed time in completed years between the date stored in row 4 and the date of the current evaluation. Null when no prior screen exists.
- **Kind:** 1 (derived)
- **Source DAK:** N/A (novel, derived)
- **Source DE ID:** N/A
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 6 — Prior screen result

- **Activity ID:** `CC.B` (Due for Screening)
- **Data Element ID:** `HIV.D.DE664`
- **Label:** HPV-DNA cervical cancer screening test result (case study label: Prior screen result)
- **Description:** The result of the client's most recent cervical cancer screening test. In Algorithm 5 (HPV DNA primary screening), this is the HPV DNA test result; in a purposive that uses a different primary test (cytology, HPV mRNA, dual-stain), the same slot holds the result of whichever primary test was used.
- **Data Type:** Coding (textualist uses string: "positive" / "negative" / null)
- **Input Options:** positive / negative / (null)
- **Required:** C (null when no prior screen)
- **Linkages (DMN):** `textualist.dmn#CC.B.due_screening_t` (Due for Screening); fourth input `PriorResult` in rules `DecisionRule_1kowjor` through `DecisionRule_018yt1f` (all checking `"negative"` to partition the screening window) and `DecisionRule_1cti1wm` (checking `"positive"` to route to triage pathway).
- **Annotations:** The textualist's abstract `PriorResult` string corresponds to the HIV DAK's `HIV.D.DE664` "HPV-DNA cervical cancer screening test result" under Algorithm 5. If a purposive DMN is authored for Algorithm 2 or 6 (cytology or colposcopy triage), the same slot would be filled from `HIV.D.DE673` (cytology) or similar. A more complete CC DAK CDD would carry a `PrimaryScreeningTestType` element alongside this and partition the result rows by primary-test type; that expansion is out of scope for the minimum-viable first pass.
- **Terminology Intent:** The binary result of the client's most recent primary cervical cancer screening test, where "positive" triggers the triage pathway and "negative" supports the rescreen-window calculation.
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** `HIV.D.DE664`
- **Source Commit:** *(blank)*
- **Reuse Intent:** extend (the CC DAK may need a broader type that covers all primary-test results across Algorithms 1–7, not only HPV DNA)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 7 — VIA result

- **Activity ID:** `CC.C` (Triage Decision)
- **Data Element ID:** `HIV.D.DE668`
- **Label:** VIA cervical cancer screening test result
- **Description:** The result of visual inspection with acetic acid (VIA), performed as a triage test after a positive HPV screening result in Algorithm 5.
- **Data Type:** Coding (textualist uses string: "positive" / "negative" / "suspected cancer" / null)
- **Input Options:** positive / negative / suspected cancer / (null)
- **Required:** C (null when not yet performed)
- **Linkages (DMN):** `textualist.dmn#CC.C.triage_t` (Triage Decision); first input `VIAResult` in rules `DecisionRule_triage_pos`, `DecisionRule_triage_neg_gen`, `DecisionRule_triage_neg_hiv`, `DecisionRule_triage_cancer`, and catch-all `DecisionRule_triage_catchall`.
- **Linkages (Register):** The "suspected cancer" category within VIA result is the clinical-judgment boolean that [`cc-003`](cc-003.html) flags. See row 8 (Suspicion of cancer) for the separated-out boolean that the Ablation Eligibility decision consumes; the two are related but distinct — row 7 is the triage result category, row 8 is the standalone clinical judgment the Ablation Eligibility table uses.
- **Annotations:** VIA triage has well-documented inter-observer variability; `cc-003` names this as the most clinically loaded boolean input the DAK takes as given. The element itself is straightforward; the variability is in the clinical act of performing the VIA and interpreting the acetowhite reaction.
- **Terminology Intent:** The provider's interpretation of the VIA triage step: positive (acetowhite lesion; route to treatment), negative (no acetowhite lesion; route to re-screen), or suspected cancer (findings concerning for invasive disease; route to referral).
- **Kind:** 2 (harvested)
- **Source DAK:** HIV
- **Source DE ID:** `HIV.D.DE668`
- **Source Commit:** *(blank)*
- **Reuse Intent:** reuse-as-is
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 8 — Suspicion of cancer

- **Activity ID:** `CC.D` (Ablation Eligibility)
- **Data Element ID:** `CC.D.DE01`
- **Label:** Suspicion of cancer
- **Description:** A boolean representing the clinician's judgment that invasive cervical cancer is suspected from the current examination (visual inspection, lesion characteristics, bleeding pattern, or symptomatic presentation), independent of histopathology confirmation.
- **Data Type:** boolean
- **Input Options:** true / false / null
- **Required:** R (at the Ablation Eligibility decision point)
- **Linkages (DMN):** `textualist.dmn#CC.D.ablation_t` (Ablation Eligibility); first input `SuspicionOfCancer` in rules `DecisionRule_ablation_cancer` (any suspicion → not ablation-eligible), `DecisionRule_ablation_tz1`, `DecisionRule_ablation_tz2`, `DecisionRule_ablation_tz3`, and catch-all `DecisionRule_ablation_ca_nullsusp`.
- **Linkages (Register):** [`cc-003-cancer-suspected.md`](cc-003.html) — this row is the data element the "cancer suspected" register entry operates on.
- **Annotations:** A clinically loaded boolean. `cc-003` documents what it hides: training, experience, time pressure, and systematic under- or over-calling of "suspected cancer" across providers. The DAK treats it as given input; upstream clinical quality assurance is a deployment-context concern, not a DAK decision rule.
- **Terminology Intent:** The clinician's determination, made at the time of the screening or triage encounter, that invasive cervical cancer is suspected and further evaluation (biopsy, colposcopy, oncology referral) is warranted instead of or in addition to the ablation-vs-excision treatment pathway.
- **Kind:** 1 (novel to CC)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 9 — Transformation zone type

- **Activity ID:** `CC.D` (Ablation Eligibility)
- **Data Element ID:** `CC.D.DE02`
- **Label:** Transformation zone type
- **Description:** The anatomical classification of the cervical transformation zone, per the 2021-07 guideline's Annex 5 Section 5.1.1 typology.
- **Data Type:** Coding
- **Input Options:** `Type 1` (entirely visible, ectocervical), `Type 2` (entirely visible, endocervical component), `Type 3` (not entirely visible, extends into endocervical canal), null
- **Required:** R (at Ablation Eligibility)
- **Linkages (DMN):** `textualist.dmn#CC.D.ablation_t` (Ablation Eligibility); second input `TZType` in rules `DecisionRule_ablation_tz1`, `DecisionRule_ablation_tz2`, `DecisionRule_ablation_tz3`, and catch-all `DecisionRule_ablation_ca_nulltz`.
- **Annotations:** Cervical-cancer-specific anatomical typology; does not exist in any harvested DAK as a reusable element. Novel to the CC DAK.
- **Terminology Intent:** The classification of the cervical transformation zone based on its visibility and position on the ectocervix/endocervical canal, determining whether the lesion can be treated by ablation (Types 1 and 2) or requires excision (Type 3).
- **Kind:** 1 (novel to CC)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 10 — Histology result

- **Activity ID:** `CC.E` (Follow-up Decision)
- **Data Element ID:** `CC.E.DE01`
- **Label:** Histology result
- **Description:** The histopathological finding from the tissue specimen obtained during ablation or LLETZ treatment, used at the Follow-up Decision to route women with invasive cancer to further management and women with CIN3 or less to post-treatment follow-up.
- **Data Type:** Coding
- **Input Options:** `CIN3 or less` / `cancer` / (null; histology unavailable in some settings per the 2021-07 Annex 4 footnote)
- **Required:** C
- **Linkages (DMN):** `textualist.dmn#CC.E.followup_t` (Follow-up Decision); second input `HistologyResult` in rules `DecisionRule_followup_ablation_cin`, `DecisionRule_followup_ablation_cancer`, `DecisionRule_followup_lletz_cin`, `DecisionRule_followup_lletz_cancer`.
- **Annotations:** Histopathology may not be available in some settings; the 2021-07 guideline's post-treatment follow-up flow (p.71, general pop; p.72, WLHIV) explicitly handles the "treated with ablation or LLETZ without histopathology results available" case. The textualist does not currently model the null-histology branch explicitly; this is a fidelity gap independent of this first-pass CDD and is adjacent to the pre-existing WLHIV double-follow-up gap confirmed in [`addendum-2021-12-reconciliation.md` (see [source repo](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md))](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md).
- **Terminology Intent:** The histopathologist's reading of the tissue specimen: presence or absence of invasive cancer, and if non-invasive, the CIN grade.
- **Kind:** 1 (novel to CC)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 11 — Eligible for screening (output)

- **Activity ID:** `CC.A` (Eligible For Screening)
- **Data Element ID:** `CC.A.DE01`
- **Label:** Eligible for screening
- **Description:** Output boolean of the Eligible For Screening decision, indicating whether the client meets the age and population criteria for cervical cancer screening under the guideline.
- **Data Type:** boolean
- **Input Options:** true / false / null
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.A.eligibility_t` output `EligibleForScreening`; consumed as first input of `textualist.dmn#CC.B.due_screening_t` (Due for Screening) via `ScreeningDecision.EligibleForScreening`.
- **Annotations:** This is an output data element — the result of the first decision table's evaluation. It is not populated from any EHR; it is computed by the DAK.
- **Terminology Intent:** A DAK-computed judgment on whether the client is in scope for the cervical cancer screening program at this encounter.
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 12 — Screening interval (output)

- **Activity ID:** `CC.A` (Eligible For Screening)
- **Data Element ID:** `CC.A.DE02`
- **Label:** Screening interval
- **Description:** Output string of the Eligible For Screening decision, carrying the recommended rescreen interval. Textualist preserves the guideline's range language; purposive resolves to a point estimate per [`cc-005`](cc-005.html).
- **Data Type:** string
- **Input Options (textualist):** `"every 5 to 10 years"` (general population), `"every 3 to 5 years"` (WLHIV), null (not eligible)
- **Input Options (purposive):** `"every 10 years"` (general population), `"every 5 years"` (WLHIV), null (not eligible)
- **Required:** R (output; paired with row 11)
- **Linkages (DMN):** `textualist.dmn#CC.A.eligibility_t` output `ScreeningInterval`; `purposive.dmn#CC.A.eligibility_p` output `ScreeningInterval` (point estimate per cc-005). Consumed as second input of `CC.B.due_screening_{t,p}` (Due for Screening) via `ScreeningDecision.ScreeningInterval`.
- **Linkages (Register):** [`cc-005`](cc-005.html) (proposed) — screening interval resolution. Resolves both populations to the upper bound of their respective WHO ranges based on the epidemiological regime declared in `cc-000` (first-time-screenee backlog as binding resource constraint).
- **Annotations:** The textualist preserves the guideline range verbatim; the purposive encodes the resolved point estimate. The per-population resolutions are documented in `cc-005`, including the reasoning for landing at the upper bound and the conditions under which a future regime change would flip the resolution to the lower bound.
- **Terminology Intent:** The WHO-recommended rescreen interval, expressed as a range rather than a scalar, reflecting the evidence base's uncertainty over the optimal rescreen frequency.
- **Kind:** 1 (DAK output; preserved range)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 13 — Screening status (output)

- **Activity ID:** `CC.B` (Due for Screening)
- **Data Element ID:** `CC.B.DE02`
- **Label:** Screening status
- **Description:** Output string of the Due for Screening decision, categorising where the client sits in the screening schedule.
- **Data Type:** string
- **Input Options (textualist):** `"never screened — screen now"`, `"not yet due"`, `"within screening window"`, `"past screening window"`, `"prior positive — enter triage pathway"`, `"not eligible"`
- **Input Options (purposive):** `"never screened — screen now"`, `"not yet due"`, `"due"`, `"prior positive — enter triage pathway"`, `"not eligible"`
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.B.due_screening_t` output `ScreeningStatus`; `purposive.dmn#CC.B.due_screening_p` output `ScreeningStatus` (two-bucket encoding per [`cc-005`](cc-005.html)).
- **Annotations:** The output value set is declared in the DMN via a `<outputValues>` element; see `DecisionTable_1jr7lzl` `UnaryTests_1h5h3n3`. The purposive encoding collapses the textualist's `"within screening window"` and `"past screening window"` into a single `"due"` value, reflecting cc-005's point-estimate resolution of the screening interval range. Downstream schedulers that need to distinguish "just-barely due" from "substantially overdue" should read `YearsSinceLastScreen` directly rather than pattern-matching on `ScreeningStatus`.
- **Terminology Intent:** A categorical label summarising the client's position in the screening schedule at this encounter.
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 14 — Triage status (output)

- **Activity ID:** `CC.C` (Triage Decision)
- **Data Element ID:** `CC.C.DE01`
- **Label:** Triage status
- **Description:** Output string of the Triage Decision, routing HPV-positive women based on their VIA triage result and HIV status.
- **Data Type:** string
- **Input Options:** `"VIA positive — eligible for treatment"`, `"VIA negative — repeat HPV test in 2 years"` (general population), `"VIA negative — repeat HPV test in 1 year"` (WLHIV), `"suspected cancer — refer for evaluation and biopsy"`, `"unknown VIA result"`
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.C.triage_t` output `TriageStatus`; consumed as input `TriageDecision` in `CC.D.treatment_{t,p}` (Treatment Decision).
- **Annotations:** The population-specific re-screen intervals ("in 2 years" / "in 1 year") after VIA-negative triage are the rows that [`cc-002`](cc-002.html) observes and that the pre-existing WLHIV follow-up gap should be examined against when `cc-002` is drafted.
- **Terminology Intent:** A categorical routing outcome for HPV-positive women based on their VIA triage step.
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 15 — Ablation eligible (output)

- **Activity ID:** `CC.D` (Ablation Eligibility)
- **Data Element ID:** `CC.D.DE03`
- **Label:** Ablation eligible
- **Description:** Output boolean of the Ablation Eligibility decision.
- **Data Type:** boolean
- **Input Options:** true / false
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.D.ablation_t` output `AblationEligible`; consumed as second input of `CC.D.treatment_{t,p}` (Treatment Decision) via `AblationDecision`.
- **Terminology Intent:** Whether the client's lesion is suitable for ablative treatment (cryotherapy or thermal ablation) given transformation zone type and absence of suspicion of cancer, per the 2021-07 Annex 5 Section 5.1.2 criteria.
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 16 — Treatment plan (output)

- **Activity ID:** `CC.D` (Treatment Decision)
- **Data Element ID:** `CC.D.DE04`
- **Label:** Treatment plan
- **Description:** Output string of the Treatment Decision, naming the selected treatment modality.
- **Data Type:** string
- **Input Options:** `"ablative treatment"`, `"LLETZ"`, `"no treatment — repeat HPV in 2 years"`, `"no treatment — repeat HPV in 1 year"`, `"refer for evaluation, biopsy and further management"`, `"unknown triage status"`
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.D.treatment_t` output `TreatmentPlan`; consumed as first input of `CC.E.followup_{t,p}` (Follow-up Decision) via `TreatmentDecision`.
- **Terminology Intent:** The DAK-computed treatment modality for this encounter, which may be an active treatment (ablation or LLETZ), a deferred-with-re-screen plan (VIA-negative follow-up), or a referral (suspected cancer).
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 17 — Follow-up plan (output)

- **Activity ID:** `CC.E` (Follow-up Decision)
- **Data Element ID:** `CC.E.DE02`
- **Label:** Follow-up plan
- **Description:** Output string of the Follow-up Decision, naming the post-treatment follow-up schedule or the further-management routing for suspected cancer.
- **Data Type:** string
- **Input Options:** `"post-treatment follow-up after 1 year"`, `"cancer — further management"`, `"repeat HPV test after 2 years"`, `"repeat HPV test after 1 year"`, `"evaluation, biopsy and further management"`, `"unknown treatment plan"`
- **Required:** R (output)
- **Linkages (DMN):** `textualist.dmn#CC.E.followup_t` output `FollowUpPlan`.
- **Annotations:** The "post-treatment follow-up after 1 year" output is the first 12-month check after treatment; for the general population this returns to routine on negative, for WLHIV there is a second 12-month check per 2021-07 Rec 33 ("double follow-up") that the textualist does not currently encode — see [`addendum-2021-12-reconciliation.md` (see [source repo](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md))](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/addendum-2021-12-reconciliation.md) for the confirmed fidelity gap.
- **Terminology Intent:** The DAK-computed next-encounter schedule for the client after the Treatment Decision has fired.
- **Kind:** 1 (DAK output)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

### Row 18 — Pregnancy status (Treatment Decision input, purposive only)

- **Activity ID:** `CC.D` (Treatment Decision, purposive only — no corresponding input in the textualist)
- **Data Element ID:** `HIV.B.DE160`-family (candidate; the HIV DAK has multiple "check pregnancy status" elements across visit types; the correct CDD reuse target may ultimately be an ANC DAK element rather than an HIV check-flag; pending re-harvest)
- **Label:** Pregnancy status
- **Description:** Whether the client is currently pregnant at the time of the Treatment Decision. Consumed only at the Treatment Decision in the purposive DMN to implement GPS 41's treatment-deferral-in-pregnancy per [`cc-006`](cc-006.html).
- **Data Type:** boolean
- **Input Options:** `true` (pregnant), `false` (not pregnant), `null` (unknown — treated as not-pregnant per cc-006 null-handling)
- **Required:** C (conditional — required at the Treatment Decision only; not consulted elsewhere in the cascade)
- **Linkages (DMN):** `purposive.dmn#CC.D.treatment_p` input `IsPregnant` via `InputData_pregnancy`. Not present in `textualist.dmn`. Rule `DecisionRule_treatment_pregnancy_defer` fires when `IsPregnant = true` and triage is `"VIA positive — eligible for treatment"`, emitting `"defer treatment until after pregnancy"`. Cancer-suspected referrals are not deferred (see cc-006 rationale).
- **Linkages (Register):** [`cc-006`](cc-006.html) (proposed) — pregnancy handling across the cascade. Selects `add-input-at-treatment-only` option, encoding GPS 41 at the Treatment Decision while leaving other cascade points pregnancy-unaware.
- **Annotations:** The purposive DMN changes the Treatment Decision's hit policy from `UNIQUE` to `FIRST` to permit the pregnancy deferral rule to precede the ablate/LLETZ rules. L3 implementers should confirm their EHR reliably populates pregnancy status for screening-age women at the Treatment Decision point; unknown status defaults to the pregnancy-unaware path for safety-vs-fidelity reasons documented in cc-006.
- **Terminology Intent:** Current-pregnancy boolean at the moment the Treatment Decision is made. Post-delivery re-entry into the cascade is a country-level operational concern (not a DAK concern) and does not need a separate data element here.
- **Kind:** 2 (harvested, candidate pending re-harvest)
- **Source DAK:** HIV (candidate; pending re-harvest with a broader search for ANC and FP pregnancy-status elements that may be better reuse targets)
- **Source DE ID:** `HIV.B.DE160` (candidate; may be replaced when a re-harvest identifies an ANC pregnancy-status element as the canonical reuse source)
- **Source Commit:** *(blank; backfill planned in Phase B)*
- **Reuse Intent:** reuse-pending (re-harvest needed to confirm the right source DAK element)
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3; `Observation` with SNOMED `77386006 | Pregnant` or an equivalent ANC-DAK-sourced binding are the obvious L3 candidates, deferred to country adaptation)*

### Row 19 — Vaccination status (deferred stub)

- **Activity ID:** *(out of scope for current textualist)*
- **Data Element ID:** `IMMZ.*` (candidate cluster; pending specific harvest)
- **Label:** HPV vaccination status
- **Description:** Whether and how the client has been vaccinated against HPV, including dose count, vaccine type, and age at vaccination.
- **Data Type:** Coding or compound (candidate; actual shape pending cc-004 drafting)
- **Input Options:** *(to be determined by cc-004)*
- **Required:** O (unless/until the guideline catches up)
- **Linkages (DMN):** Not yet in `textualist.dmn`. The 2021-07 guideline pre-dates the large-scale arrival of HPV-vaccinated cohorts at screening age and does not model vaccination status as a screening input.
- **Linkages (Register):** [`cc-004-vaccination-status.md`](cc-004.html).
- **Annotations:** This row is a stub reserved for a future vaccination-modulated screening refinement. The evidence update that would populate this row is the 2022 SAGE single-dose HPV vaccination position paper plus ongoing cohort follow-up, not any of the three 2021–2024 WHO cervical cancer documents. Re-visit this row when `cc-004` is drafted.
- **Kind:** 2 (defer)
- **Source DAK:** IMMZ (candidate; pending re-harvest)
- **Source DE ID:** `IMMZ.*` (candidate cluster)
- **Source Commit:** *(blank)*
- **Reuse Intent:** pending
- **ICD-11 / SNOMED CT / LOINC / ICHI / ICF:** *(blank — L3)*
- **FHIR Resource / FHIR Profile / Canonical URI:** *(blank — L3)*

---

## Deferred as purposive refinement: `HasCervix`

This section documents an element that is **not** a row in the current CDD but is retained in the case study's thinking for a future purposive refinement and as a candidate contribution to a future smart-core Kind-3 entry.

**The element.** A boolean (`HasCervix`) representing whether the client has a cervix anatomically present, regardless of sex assigned at birth or gender identity. The purpose is to encode, at the L2, the two naive-reader instincts that the current `Sex = Female` encoding leaves unanswered: **broader**, to admit transgender men and non-binary and intersex individuals with a cervix per the 2021-07 guideline's Section 3.1 "Programme considerations" body narrative (p. 21); and **narrower**, to exclude women who have had a total hysterectomy, a filter the 2021-07 guideline does not address and which today lives at the encounter as clinical common sense rather than as a DAK rule. A single `HasCervix` element addresses both instincts at the same input slot. See [`cc-001`](cc-001.html) for the register-level deferral record.

**Why not a row in the first-pass CDD.** Three reasons, in descending order of weight:

1. **Deployment reality (shared ground, both directions).** `Sex = Female` passes the Muliokela premapping test in every LMIC pathfinder country; `HasCervix` fails it because no current public-sector EHR (Bahmni, eTracker, SmartCare, Impilo, iHRIS, OpenMRS-based systems) carries `BodyStructure` or anatomical-inventory fields, and hysterectomy history is not reliably surfaced at registration in the way `Sex` is. This is the binding implementability constraint and applies equally to the broader and narrower refinements.
2. **Source-document grounding (per direction, not shared).** *For the broader refinement:* Recommendation 1 is the output of a GRADE process whose trial base — HPV primary screening trials — enrolled predominantly cisgender women, and the 2021-07 guideline's Section 3.1 broader-population language sits in programme-considerations body narrative at lower evidential stringency than Rec 1; the split between numbered recommendations and Section 3.1 prose was a deliberate GDG compromise, not an inconsistency to be resolved at the L2. Committing the first-pass CDD to a `HasCervix` row in the broader role would assert a claim at higher stringency than the trial base currently supports. *For the narrower refinement:* the 2021-07 guideline is silent on hysterectomy as a screening-eligibility criterion ("hysterectom-" appears only in Annex 5 as a surgical specimen type and as a rare treatment complication), and the L2 mirrors what the guideline asserts rather than what it assumes to be too clinically obvious to say.
3. **Textualist/CDD consistency.** The textualist DMN uses `ClientIsWoman`, not `HasCervix`. The CDD documents what the DMN actually consumes; a `HasCervix` row would describe a hypothetical purposive refinement, not the textualist.

**Why document it at all.** Because the three-Kind classification in this CDD has Kind 3 (proposed-to-core) as a framework category, and no row in the first pass exercises Kind 3. Rather than pretend a row demonstrates Kind 3 that doesn't, the CDD carries `HasCervix` as the named candidate contribution to a future smart-core Kind-3 entry. When a Phase B triangulation artifact is produced (per the plan file), or when a future purposive DMN authoring pass pursues the convergent refinement, `HasCervix` is the first element that would be lifted into that Kind-3 slot.

**Expected candidate shape, if it were populated:**

- **Label:** Has cervix
- **Description:** Whether the client has a cervix anatomically present.
- **Data Type:** boolean
- **Terminology Intent:** Anatomical presence of a cervix, independent of sex assigned at birth or gender identity, used to determine screening eligibility across the two naive-reader instincts the current `Sex = Female` encoding leaves unanswered: broader admission of transgender men and non-binary and intersex individuals with a cervix per the 2021-07 guideline's Section 3.1 programme-considerations narrative, and narrower exclusion of post-total-hysterectomy women which the 2021-07 guideline does not address.
- **Kind:** 3 (proposed to smart-core)
- **Source DAK:** None at present in any harvested DAK; the HIV DAK and maternal-health DAK may have adjacent elements (hysterectomy history, genital examination findings) that would need to be reviewed for reuse rather than inventing fresh.
- **L3 work deferred:** A `HasCervix` element at the smart-core level would need `BodyStructure` FHIR resource selection, SNOMED binding (e.g. `71854001` as the historical starting point, subject to terminology specialist review), and null-handling semantics for systems that cannot express anatomical inventory. None of that is L2 work and none of it is in scope for this DAK. See [`cc-001`](cc-001.html) for the register-level record of the deferral decision.

**When this deferred element would become a row.** Two conditions:

1. A future purposive DMN authoring pass chooses to rename `ClientIsWoman` → `HasCervix` as a semantic refinement. The register entry [`cc-001`](cc-001.html) would update its `selected` value to record both the textualist's `sex-female` and the purposive's `has-cervix`, and this CDD would gain a row 20 for `HasCervix` (Kind 1 + Kind 3) alongside row 2 (`Sex`, Kind 2) with the textualist continuing to use row 2 and the purposive using row 20.
2. Or: a Phase B smart-core-candidates triangulation artifact picks up `HasCervix` as a proposed-to-core element, at which point the CDD would add it as a Kind-3 row with a pointer to the candidate artifact.

Neither condition is met in this first pass; the section above is the full documentation of the deferral.
