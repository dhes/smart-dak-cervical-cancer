**Component 3 of the WHO SMART Guidelines L2 DAK structure.** This page presents narrative user scenarios illustrating how the [generic personas](generic-personas.html) interact with one another — and with a digital system implementing this DAK — to carry a woman through the Algorithm 5 cascade (HPV DNA primary screening with VIA triage, treatment by ablation or excision, referral for suspected invasive cancer).

A user scenario, in SMART DAK terms, is an illustrative narrative — not a formal use case with preconditions and postconditions. Per [Section 3.1 of the SOP](https://smart.who.int/ig-starter-kit/l2_dak_authoring.html), scenarios "describe typical interactions that one would expect to happen in the specific health programme area" and are "only illustrative and intended to give an idea of a typical workflow." Their authoring weight sits on *typicality* and *realism*, not on taxonomic completeness.

The SOP also states the structural handoff that shapes how this page is written: *"the actions performed by the generic personas in the user scenarios define the activities and their sequence"* in Component 4 (BPMN workflows). Scenarios are therefore not free-form storytelling; the actions named in them are the canonical activity vocabulary Component 4 will lift unchanged.

## Scope and authoring posture

The same three derivation paths apply here as for the [personas page](generic-personas.html#scope-and-authoring-posture): L1 normative guidance (sparse — the 2021-07 guideline narrates the cascade in the abstract but names no scenarios), SME consultation (none to date), facility interviews (none to date).

**Phase-1 posture.** The seven scenarios below are therefore *analytically derived* from the Algorithm 5 cascade structure, using the six personas already enumerated in Component 2. Each scenario enumerates the subset of cascade actions it exercises. Each one carries a deferred SME validation closure path by inheritance from the personas it involves — a scenario is validated when the personas it depicts are validated and when a practising cascade operator reviews the action sequence and confirms it matches working reality.

## Planning for Component 4

This section is an authoring discipline the SOP does not prescribe but which this DAK adds deliberately. The SOP only requires that the scenarios exist; it does not require that they share a canonical action vocabulary. But because Component 4 lifts scenario actions into BPMN as-is, and because Component 5 (decision logic) further references those activities as decision inputs and outputs, any inconsistency introduced at the Component 3 layer propagates downstream. Settling the vocabulary once, here, pays dividends in Components 4 and 5.

### BPMN module decomposition

Component 4 (BPMN workflows) will consist of five modules, corresponding to the natural cascade decomposition of Algorithm 5:

1. **Invitation** — community-health-worker-led outreach; screening invitations; rescreen reminders
2. **Primary Screening** — facility encounter, HPV DNA sample collection, laboratory assay, result return
3. **Triage** — VIA triage for HPV-positive women
4. **Treatment** — thermal ablation, LLETZ/LEEP, cold-knife conization, or referral for suspected invasive cancer
5. **Follow-up** — triage-negative retest, post-treatment retest, routine rescreening

Referral for suspected invasive cancer does not get its own module — it is an exit branch from Treatment, not a separate process flow. Programme-level oversight (cohort tracking, indicator reporting, recall campaigns) is deferred to Component 8's indicator work rather than modelled as a BPMN process.

### Action vocabulary

One canonical action name per cascade step. Scenarios use these names verbatim; Component 4 lifts them as BPMN activity labels; Component 5 references them as decision-logic anchors.

| Module | Action | Performing persona(s) |
|---|---|---|
| Invitation | Issue screening invitation | Community health worker |
| Invitation | Identify overdue rescreen candidate | Community health worker |
| Primary Screening | Collect HPV sample | Nurse/midwife (or Target client, self-collection) |
| Primary Screening | Run HPV DNA assay | Laboratory technician |
| Primary Screening | Report HPV result | Laboratory technician |
| Triage | Schedule triage encounter | Nurse/midwife |
| Triage | Perform VIA triage | Nurse/midwife |
| Triage | Record triage result | Nurse/midwife |
| Treatment | Determine treatment eligibility | Nurse/midwife |
| Treatment | Perform thermal ablation | Nurse/midwife |
| Treatment | Perform LLETZ/LEEP | Advanced clinician |
| Treatment | Perform cold-knife conization | Advanced clinician |
| Treatment | Refer for suspected invasive cancer | Nurse/midwife or Advanced clinician |
| Treatment | Defer treatment (pregnancy) | Nurse/midwife or Advanced clinician |
| Follow-up | Schedule next routine screening | Nurse/midwife |
| Follow-up | Schedule triage-negative retest | Nurse/midwife |
| Follow-up | Schedule post-treatment retest | Nurse/midwife |
| Follow-up | Attend scheduled retest | Target client |

Self-collection of HPV samples is listed parenthetically against "Collect HPV sample" for vocabulary-completeness reasons; no scenario below exercises it, consistent with [rec 4 being Not encoded as upstream of the DAK cascade](interventions-and-recommendations.html#recommendations).

## Scenarios

Seven scenarios below. Each names personas inline, closes with an explicit action sequence using the vocabulary above, and lists the modules traversed and any interpretation register entries the scenario depends on.

### 1. Golden path — HPV-negative result, routine rescreening

Amina is a woman in the general-population age band (35 years old). A community health worker visits her neighbourhood during a screening outreach campaign and issues her a screening invitation. Amina attends her primary-care facility the following week.

At the facility, the nurse/midwife counsels Amina on the screening procedure and consent, performs a speculum examination, and collects an HPV DNA sample. The sample is couriered with the week's batch to the district laboratory. A laboratory technician runs the HPV DNA assay; Amina's result is negative. The laboratory reports the result back to the facility.

The nurse/midwife contacts Amina, communicates the negative result, and schedules her next routine screening per the 5–10 year interval for the general population (see [cc-005](cc-005.html)).

**Actions (in sequence):**

1. Issue screening invitation — Community health worker
2. Collect HPV sample — Nurse/midwife
3. Run HPV DNA assay — Laboratory technician
4. Report HPV result — Laboratory technician
5. Schedule next routine screening — Nurse/midwife

**Modules traversed:** Invitation → Primary Screening → Follow-up
**Register references:** [cc-005](cc-005.html) (screening interval)

### 2. HPV-positive, triage-negative — retest scheduled

Blessing is a 42-year-old woman in the general population. She attends her primary-care facility for screening following a community invitation. The nurse/midwife collects an HPV DNA sample; the laboratory technician runs the assay and reports a positive result.

The nurse/midwife contacts Blessing and schedules her triage encounter. Blessing attends. The nurse performs VIA triage; the result is negative — no acetowhite lesions visible. The nurse records the negative triage result, counsels Blessing, and schedules her triage-negative retest at 24 months per the general-population interval ([cc-005](cc-005.html)).

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Schedule triage-negative retest — Nurse/midwife

**Modules traversed:** Primary Screening → Triage → Follow-up
**Register references:** [cc-005](cc-005.html) (triage-negative retest interval)

### 3. Ablation-eligible lesion — thermal ablation and post-treatment retest

Chipo is a 38-year-old woman in the general population. Her HPV DNA test returned positive. She attends triage; the nurse/midwife performs VIA and identifies a small acetowhite lesion, fully visible on the ectocervix, with clearly defined margins — meeting ablation-eligibility criteria.

The nurse records the positive triage result and determines treatment eligibility: ablation-eligible. The facility is configured for single-visit screen-triage-and-treat, so the nurse counsels Chipo, obtains consent, and performs thermal ablation in the same encounter. She counsels Chipo on post-treatment expectations and schedules her post-treatment retest at 12 months ([cc-005](cc-005.html)).

Twelve months later Chipo attends her scheduled post-treatment retest. (The retest itself begins a new instance of Primary Screening; it is not depicted further in this scenario.)

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Determine treatment eligibility — Nurse/midwife
8. Perform thermal ablation — Nurse/midwife
9. Schedule post-treatment retest — Nurse/midwife
10. Attend scheduled retest — Target client

**Modules traversed:** Primary Screening → Triage → Treatment → Follow-up
**Register references:** [cc-005](cc-005.html) (post-treatment retest interval)

### 4. Non-ablation-eligible lesion — LLETZ and post-treatment retest

Dafu is a 44-year-old woman in the general population. Her HPV DNA test returned positive; she attended triage. The nurse/midwife performed VIA and identified a larger acetowhite lesion extending into the endocervical canal, with margins that could not be fully visualised — not ablation-eligible.

The nurse records the positive triage result, determines treatment eligibility as non-ablation-eligible, and refers Dafu to the district hospital. At the district hospital an advanced clinician reviews Dafu's findings, confirms the indication for excision, and performs LLETZ under local anaesthesia.

The advanced clinician (or the nurse on return to the primary-care facility, depending on local follow-up practice) schedules Dafu's post-treatment retest at 12 months. Twelve months later Dafu attends her scheduled retest.

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Determine treatment eligibility — Nurse/midwife
8. Perform LLETZ/LEEP — Advanced clinician
9. Schedule post-treatment retest — Nurse/midwife or Advanced clinician
10. Attend scheduled retest — Target client

**Modules traversed:** Primary Screening → Triage → Treatment → Follow-up
**Register references:** [cc-005](cc-005.html) (post-treatment retest interval)

### 5. Suspected invasive cancer — referral out of cascade

Esi is a 49-year-old woman in the general population. Her HPV DNA test was positive; she attended triage. On VIA the nurse/midwife observed a large, friable, bleeding lesion with irregular margins and abnormal surface vasculature — findings suspicious for invasive cancer rather than a treatable precancerous lesion.

The nurse recorded the triage result with the "suspected invasive cancer" designation per the operational definition this DAK uses (see [cc-003](cc-003.html)) and initiated referral to the advanced clinician for specialist evaluation — rather than attempting triage-based treatment, which is contraindicated in the presence of suspicious findings.

The advanced clinician examined Esi, performed a cervical biopsy, and referred her onward to tertiary oncology services pending histopathology. Esi's subsequent care — confirmation, staging, treatment of invasive disease — falls outside the DAK's cascade scope.

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Refer for suspected invasive cancer — Nurse/midwife

**Modules traversed:** Primary Screening → Triage → Treatment (referral exit)
**Register references:** [cc-003](cc-003.html) (suspected invasive cancer — operational definition)

### 6. Woman living with HIV — shorter interval, mandatory triage

Fatima is a 32-year-old woman living with HIV, attending her primary-care facility for routine ART follow-up. She is within the WLHIV screening age range (25+) defined in [cc-002](cc-002.html) and due for cervical screening under the WLHIV 3–5 year interval ([cc-005](cc-005.html)).

The nurse/midwife integrates the screening into Fatima's ART visit, counsels her, and collects an HPV DNA sample. The lab result returns positive. The nurse contacts Fatima to return for triage — mandatory for WLHIV per rec 22, not optional as for the general population.

Fatima attends triage. The nurse performs VIA; no acetowhite lesion is visible. The nurse records the negative triage result and schedules Fatima's triage-negative retest at **12 months** — the shorter WLHIV interval per rec 31, compared to 24 months for the general population ([cc-005](cc-005.html)).

*Interpretive note — textualist versus purposive divergence.* This scenario does not exercise the post-treatment follow-up path. If it did, the WLHIV "double follow-up" (retest at 12 *and* 24 months) specified in rec 33 would apply in the textualist reading; this DAK's purposive posture collapses that to a single 12-month retest, a divergence documented in [cc-002](cc-002.html). Any future scenario covering WLHIV treatment and follow-up carries that interpretive choice forward.

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Schedule triage-negative retest — Nurse/midwife (12-month WLHIV interval)

**Modules traversed:** Primary Screening → Triage → Follow-up
**Register references:** [cc-002](cc-002.html) (WLHIV operationalisation), [cc-005](cc-005.html) (intervals)

### 7. Pregnant woman, triage-positive — treatment deferred until after pregnancy

Grace is a 29-year-old woman in the general population. Her HPV DNA test was positive. At triage the nurse/midwife performs VIA and identifies an ablation-eligible lesion.

During the counselling preceding treatment, Grace discloses that she is 16 weeks pregnant — confirmed in her ANC record. The nurse determines treatment eligibility as ablation-eligible in principle, but per the pregnancy-deferral good practice statement (rec 41 GPS; see [cc-006](cc-006.html)) does not treat. She defers treatment, counsels Grace on the importance of returning after delivery, and documents the deferred-treatment status in Grace's record so that programme follow-up captures her as pending treatment rather than closing the cascade.

After delivery and the programme-defined post-partum recovery interval, Grace returns. The nurse re-evaluates the lesion — repeating VIA to confirm findings are unchanged — re-determines treatment eligibility, and performs thermal ablation. The post-treatment retest is scheduled at 12 months as in the non-deferred ablation path.

**Actions (in sequence):**

1. Collect HPV sample — Nurse/midwife
2. Run HPV DNA assay — Laboratory technician
3. Report HPV result — Laboratory technician
4. Schedule triage encounter — Nurse/midwife
5. Perform VIA triage — Nurse/midwife
6. Record triage result — Nurse/midwife
7. Determine treatment eligibility — Nurse/midwife
8. Defer treatment (pregnancy) — Nurse/midwife

*After delivery and recovery interval:*

9. Perform VIA triage — Nurse/midwife (re-evaluation)
10. Determine treatment eligibility — Nurse/midwife
11. Perform thermal ablation — Nurse/midwife
12. Schedule post-treatment retest — Nurse/midwife

**Modules traversed:** Primary Screening → Triage → Treatment (deferral) → Triage (re-evaluation) → Treatment → Follow-up
**Register references:** [cc-006](cc-006.html) (pregnancy handling)

## Scenario-to-module coverage

The matrix below shows which BPMN modules each scenario exercises. All five modules have at least one scenario exercising them, confirming that the seven scenarios between them give Component 4 complete coverage of the cascade.

| Scenario | Invitation | Primary Screening | Triage | Treatment | Follow-up |
|---|---|---|---|---|---|
| 1. Golden path (HPV−) | ✓ | ✓ | — | — | ✓ |
| 2. HPV+ / VIA− | — | ✓ | ✓ | — | ✓ |
| 3. Ablation | — | ✓ | ✓ | ✓ | ✓ |
| 4. LLETZ | — | ✓ | ✓ | ✓ | ✓ |
| 5. Suspected cancer | — | ✓ | ✓ | ✓ (referral exit) | — |
| 6. WLHIV | — | ✓ | ✓ | — | ✓ |
| 7. Pregnancy deferral | — | ✓ | ✓ | ✓ | ✓ |

The Invitation module is exercised only by Scenario 1. A future pass could broaden Invitation coverage with a rescreen-reminder scenario (the "identify overdue rescreen candidate" action is in the vocabulary but unexercised by the current set). This is a coverage gap, not an authoring error — the cascade's initiation modalities are genuinely under-modelled in the first pass.

## Status

*Draft — Phase 1 of Component 3 authoring (2026-04-22).* Seven scenarios analytically derived from the Algorithm 5 cascade, using the six personas enumerated in [Component 2](generic-personas.html) and a canonical action vocabulary settled deliberately before scenario drafting to prepay the handoff to Component 4. SME validation inherits the stratified deferral pattern from the personas page. Known coverage gap: Invitation module exercised by only one scenario; a rescreen-invitation scenario is a candidate Phase-2 addition. Self-collection of HPV samples (rec 4) is listed in the action vocabulary but unexercised, consistent with its *Not encoded — upstream of DAK cascade* classification in Component 1.
