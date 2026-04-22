**Component 4 of the WHO SMART Guidelines L2 DAK structure.** This page presents the business processes and workflows that operationalise the Algorithm 5 cascade — the sequence of activities, the actors who perform them, the decision points that branch between cascade paths, and the handoffs between actors.

Per [Section 3.1 of the SOP](https://smart.who.int/ig-starter-kit/l2_dak_authoring.html), a business process is *"a set of related activities or tasks performed together to achieve the objectives of the health programme area."* A workflow is the visual representation of one such process, showing "the progression of activities (tasks, decision points, interactions)" through its participants. The component's two required deliverables are an **overview matrix** of the processes and **workflow diagrams** for each process, annotated, following BPMN 2.0 notation.

The workflows here are the visual spine that Components 5 (data dictionary), 6 (decision logic), and 7 (scheduling logic) will hang their downstream work from — data elements are collected *at* the points an activity occurs; decision-support logic triggers *when* the workflow reaches a gateway; scheduling rules apply *when* the workflow reaches a follow-up activity.

## Scope and authoring posture

The same Phase-1 posture applies as for [personas](generic-personas.html#scope-and-authoring-posture) and [user scenarios](user-scenarios.html#scope-and-authoring-posture): the processes below are *analytically derived* from the Algorithm 5 cascade and the seven scenarios in Component 3. The three SOP-named derivation paths (L1 guidance, SME consultation, facility interviews) yielded skeleton only at this phase; SME validation is deferred with the same stratified closure path — per the personas whose activities each workflow assigns.

**Design decisions committed in Component 3.** Four strategic choices were settled during the Component 3 authoring pass and carry forward here:

1. **Five business processes**, matching the five BPMN modules pre-committed in [Planning for Component 4](user-scenarios.html#planning-for-component-4): *Invitation*, *Primary Screening*, *Triage*, *Treatment*, *Follow-up*. Referral for suspected invasive cancer is an exit branch within Treatment, not a separate process. Programme-level oversight is Component 8 territory, not modelled in BPMN.

2. **Pool/lane convention.** Pools represent actor groups (Community, Facility, Laboratory, District Hospital, Client); lanes within each pool represent the generic personas. This visualises cross-pool handoffs (sample collection → laboratory; result return → facility) as BPMN message flows, which is the notation's idiom for "one actor hands off to another."

3. **80/20 level of detail.** Workflows are modelled at the cascade-general level — activity sequence is declared but visit-boundary grouping (single-visit screen-triage-and-treat versus multi-visit programmes) is not imposed. Both implementation patterns inherit the same BPMN. Activities that are "too specific and don't hold across various settings" (SOP §3.1) — specific device models, national lab network identifiers, country cadre titles — are excluded.

4. **Counselling and informed consent — sub-process.** The SOP explicitly asks authors to decide how to model counselling and consent. This DAK declares them as a single reusable sub-process *Counselling and informed consent*, referenced as a call activity from the three main workflows where they apply (Primary Screening, Triage, Treatment). This keeps the activities visible in the BPMN spine without repeating them inline in each diagram.

**Activity vocabulary.** The BPMN activity labels are lifted verbatim from the [action vocabulary table](user-scenarios.html#action-vocabulary) in Component 3. No activity is introduced here that isn't already in that table, with the exception of the sub-process-internal activities of *Counselling and informed consent*, which the SOP flagged as a separate design choice. The vocabulary reuse across Components 3 and 4 makes the scenario-to-workflow handoff mechanical.

## Overview matrix

The five processes, their purposes, primary personas, and the inter-process transitions that stitch them into the end-to-end cascade:

| # | Process | Purpose | Primary personas | Entry condition | Exit condition |
|---|---|---|---|---|---|
| 1 | Invitation | Bring eligible women into the cascade — routine invitation and overdue-rescreen identification | Community health worker | Eligible woman identified in catchment; or overdue rescreen candidate surfaced by programme list | Invitation issued |
| 2 | Primary Screening | Take and assay an HPV DNA sample; return result to the referring facility | Nurse/midwife, Laboratory technician, Target client | Client attends facility following invitation (or self-presents) | HPV result recorded at facility |
| 3 | Triage | Perform VIA on HPV-positive women; record the triage finding as negative, positive (ablation-eligible or not), or suspicious for invasive cancer | Nurse/midwife, Target client | Prior HPV result is positive | Triage result recorded |
| 4 | Treatment | Deliver thermal ablation, LLETZ/LEEP, or CKC per triage finding; defer for pregnancy where indicated; refer for suspected invasive cancer as a terminal cascade exit | Nurse/midwife, Advanced clinician, Target client | Prior triage result is positive (ablation-eligible, non-ablation-eligible, or suspicious) | Treatment delivered, deferred, or referral initiated |
| 5 | Follow-up | Schedule and track the appropriate rescreening interval — routine after HPV-negative, triage-negative retest, or post-treatment retest | Nurse/midwife, Target client | Prior HPV-negative, triage-negative, or treatment-complete | Next encounter scheduled |

Transitions between processes:

- Invitation → Primary Screening (client attends)
- Primary Screening → *HPV result* gateway: **negative** → Follow-up (routine); **positive** → Triage
- Triage → *VIA result* gateway: **negative** → Follow-up (triage-negative retest); **positive** → Treatment; **suspicious** → Treatment (referral exit)
- Treatment → *treatment disposition* gateway: **delivered** → Follow-up (post-treatment retest); **deferred (pregnancy)** → re-entry to Triage after pregnancy; **referred for suspected cancer** → cascade exit
- Follow-up → Primary Screening (when the scheduled retest interval elapses, a new screening instance begins)

## Overview diagram

The overview diagram depicts the five processes as BPMN call activities linked by the gateways listed above, with a terminal end event for the suspected-invasive-cancer referral exit. It is the navigational map for the page and the spine from which Components 5–7 will read triggers.

![Algorithm 5 cascade overview — call activities for the five process modules (Invitation, Primary Screening, Triage, Treatment, Follow-up) connected by HPV-result and VIA-result gateways; terminal end events for routine cycle completion and suspected-cancer referral](workflow-overview.svg)

**Diagram file:** `input/bpmn/workflow-overview.bpmn` (source) → `input/images/workflow-overview.svg` (rendered).

## Workflow 1 — Invitation

**Purpose.** The community health worker brings eligible women into the cascade through routine invitation (for first-time and interval-due screening) and through identification of women overdue for rescreening.

**Pools and lanes.**

- *Community* pool: Community health worker lane
- *Client* pool: Target client lane

**Activities and flow.**

1. Start event — *Invitation cycle begins* (triggered by programme schedule, outreach event, or list-based catch-up campaign)
2. Gateway (exclusive) — *Routine invitation or overdue rescreen?*
   - Routine path → proceed to step 3
   - Overdue path → **Identify overdue rescreen candidate** (CHW) → proceed to step 3
3. **Issue screening invitation** (CHW)
4. Message flow — CHW → Target client (invitation delivered)
5. End event — *Invitation complete*

**Calls sub-process.** None.

**Activity references.** `Identify overdue rescreen candidate`, `Issue screening invitation`.

![Invitation workflow — Community pool with CHW lane containing start event, routine-or-overdue gateway, identify-overdue-rescreen-candidate task, issue-screening-invitation task, end event; Client pool as recipient of the invitation-delivered message flow](workflow-invitation.svg)

**Diagram file:** `input/bpmn/workflow-invitation.bpmn` → `input/images/workflow-invitation.svg`.

## Workflow 2 — Primary Screening

**Purpose.** Sample collection, laboratory assay, and result return — the cascade's generative step. All downstream decisions depend on a valid HPV result being recorded at the facility.

**Pools and lanes.**

- *Facility* pool: Nurse/midwife lane
- *Laboratory* pool: Laboratory technician lane
- *Client* pool: Target client lane

**Activities and flow.**

1. Start event — *Client attends facility*
2. Call activity — *Counselling and informed consent* (sub-process; see below)
3. **Collect HPV sample** (Nurse/midwife)
4. Message flow — Nurse/midwife → Laboratory technician (sample handoff with chain-of-custody documentation)
5. **Run HPV DNA assay** (Laboratory technician)
6. **Report HPV result** (Laboratory technician)
7. Message flow — Laboratory technician → Nurse/midwife (result return)
8. End event — *HPV result recorded at facility*

**Calls sub-process.** *Counselling and informed consent* (between steps 1 and 3).

**Activity references.** `Collect HPV sample`, `Run HPV DNA assay`, `Report HPV result`.

![Primary Screening workflow — three pools (Facility, Laboratory, Client); Facility sequence: start, counselling call activity, collect HPV sample, intermediate message-catch for HPV result received, end event; Laboratory sequence: message-start sample-received, run HPV DNA assay, report HPV result, end event; two cross-pool message flows for sample handoff and result return](workflow-primary-screening.svg)

**Diagram file:** `input/bpmn/workflow-primary-screening.bpmn` → `input/images/workflow-primary-screening.svg`.

## Workflow 3 — Triage

**Purpose.** For HPV-positive women, VIA triage partitions the path forward into routine follow-up (triage-negative), treatment (triage-positive), or suspected-cancer referral.

**Pools and lanes.**

- *Facility* pool: Nurse/midwife lane
- *Client* pool: Target client lane

**Activities and flow.**

1. Start event — *Prior HPV result positive*
2. **Schedule triage encounter** (Nurse/midwife)
3. Message flow — Nurse/midwife → Target client (recall for triage)
4. *Intermediate event* — Target client attends triage encounter
5. Call activity — *Counselling and informed consent*
6. **Perform VIA triage** (Nurse/midwife)
7. **Record triage result** (Nurse/midwife)
8. Gateway (exclusive) — *VIA result?*
   - Negative → End event *Triage-negative* → feeds Follow-up (triage-negative retest)
   - Positive → End event *Triage-positive* → feeds Treatment
   - Suspicious for invasive cancer → End event *Suspected invasive cancer* → feeds Treatment (referral exit)

**Calls sub-process.** *Counselling and informed consent* (between steps 4 and 6).

**Activity references.** `Schedule triage encounter`, `Perform VIA triage`, `Record triage result`.

**Register references.** [cc-003](cc-003.html) (operational definition of "suspected invasive cancer" governing the third gateway branch).

![Triage workflow — Facility pool with Nurse/midwife lane: start event (prior HPV result positive), schedule triage encounter, intermediate event for client attendance, counselling call activity, perform VIA triage, record triage result, three-way exclusive gateway branching to end events for triage-negative, triage-positive, and suspected invasive cancer; Client pool receives recall-for-triage message flow](workflow-triage.svg)

**Diagram file:** `input/bpmn/workflow-triage.bpmn` → `input/images/workflow-triage.svg`.

## Workflow 4 — Treatment

**Purpose.** Deliver treatment appropriate to the triage finding — thermal ablation for ablation-eligible lesions, LLETZ/LEEP or CKC for non-ablation-eligible lesions, referral for suspected invasive cancer. Handle pregnancy-deferral as a distinct branch that returns to Triage after delivery rather than proceeding to Treatment.

**Pools and lanes.**

- *Facility* pool: Nurse/midwife lane
- *District Hospital* pool: Advanced clinician lane
- *Client* pool: Target client lane

**Activities and flow.**

1. Start event — *Triage-positive or suspected-invasive-cancer result received*
2. Gateway (exclusive) — *Was the triage result suspected invasive cancer?*
   - Yes → Message flow to District Hospital → **Refer for suspected invasive cancer** (Nurse/midwife or Advanced clinician) → End event *Referred — cascade exit*
   - No → proceed to step 3
3. Call activity — *Counselling and informed consent*
4. **Determine treatment eligibility** (Nurse/midwife)
5. Gateway (exclusive) — *Treatment disposition?*
   - Ablation-eligible AND not pregnant → **Perform thermal ablation** (Nurse/midwife) → End event *Treatment delivered* → feeds Follow-up
   - Non-ablation-eligible AND not pregnant → Message flow to District Hospital → **Perform LLETZ/LEEP** OR **Perform cold-knife conization** (Advanced clinician) → End event *Treatment delivered* → feeds Follow-up
   - Pregnant (any eligibility) → **Defer treatment (pregnancy)** (Nurse/midwife) → End event *Treatment deferred* → (after delivery and recovery interval, cascade re-enters Triage for re-evaluation)

**Calls sub-process.** *Counselling and informed consent* (between steps 2 and 4, when treatment is actually proceeding).

**Activity references.** `Determine treatment eligibility`, `Perform thermal ablation`, `Perform LLETZ/LEEP`, `Perform cold-knife conization`, `Refer for suspected invasive cancer`, `Defer treatment (pregnancy)`.

**Register references.** [cc-003](cc-003.html) (suspected invasive cancer branch), [cc-006](cc-006.html) (pregnancy-deferral branch).

![Treatment workflow — three pools (Facility, District Hospital, Client); Facility branch: start, suspected-cancer gateway routing to refer-for-cancer task and cascade-exit end event OR to counselling call activity, determine treatment eligibility, disposition gateway routing to thermal ablation, sent-for-excision end event, or defer-treatment task; District Hospital: message-start received-for-excision, lesion-type gateway routing to LLETZ/LEEP or cold-knife conization tasks, each to its own end event; cross-pool message flows for cancer referral and excision handoff](workflow-treatment.svg)

**Diagram file:** `input/bpmn/workflow-treatment.bpmn` → `input/images/workflow-treatment.svg`.

## Workflow 5 — Follow-up

**Purpose.** Schedule and track the appropriate rescreening interval per the cascade state that produced the referral to Follow-up — routine rescreening after HPV-negative, triage-negative retest, or post-treatment retest. Each of the three follow-up types carries a different interval, and for women living with HIV the intervals are shorter than for the general population.

**Pools and lanes.**

- *Facility* pool: Nurse/midwife lane
- *Client* pool: Target client lane

**Activities and flow.**

1. Start event — *Referred to Follow-up from Primary Screening, Triage, or Treatment*
2. Gateway (exclusive) — *Follow-up type?*
   - Post-HPV-negative → **Schedule next routine screening** (Nurse/midwife) → Message flow to Target client (reminder near scheduled date) → *Intermediate event*: interval elapses → End event *Rescreen due* → re-enters Primary Screening
   - Post-triage-negative → **Schedule triage-negative retest** (Nurse/midwife) → Message flow to Target client → *Intermediate event*: interval elapses → End event *Retest due* → **Attend scheduled retest** (Target client) → re-enters Primary Screening
   - Post-treatment → **Schedule post-treatment retest** (Nurse/midwife) → Message flow to Target client → *Intermediate event*: interval elapses → End event *Retest due* → **Attend scheduled retest** (Target client) → re-enters Primary Screening

**Calls sub-process.** None.

**Activity references.** `Schedule next routine screening`, `Schedule triage-negative retest`, `Schedule post-treatment retest`, `Attend scheduled retest`.

**Register references.** [cc-002](cc-002.html) (WLHIV intervals), [cc-005](cc-005.html) (all three interval values).

![Follow-up workflow — Facility pool with Nurse/midwife lane: start event (referred to Follow-up), follow-up-type gateway routing to three parallel schedule tasks (schedule next routine screening, schedule triage-negative retest, schedule post-treatment retest), each leading to a message-throw end event; Client pool receives three reminder message flows from the end events](workflow-follow-up.svg)

**Diagram file:** `input/bpmn/workflow-follow-up.bpmn` → `input/images/workflow-follow-up.svg`.

## Sub-process — Counselling and informed consent

**Purpose.** A reusable sub-process capturing the counselling and informed-consent activities that precede any clinical procedure in the cascade — sample collection, VIA triage, or treatment. Modelling this once as a call activity keeps the activities visible in the BPMN spine without repeating them inline in each workflow, and gives a single place to update if country adaptation alters counselling content or consent conventions.

**Pool/lane.** Executed within whichever lane invokes it (Nurse/midwife for Primary Screening / Triage / ablation in Treatment; Advanced clinician for LLETZ/LEEP / CKC in Treatment).

**Activities.**

1. Start event
2. *Explain procedure* — the provider explains what will be done, the purpose, the common discomforts, and the alternatives if any
3. *Confirm understanding* — the provider confirms the client has understood, using teach-back or equivalent technique where programme guidance specifies it
4. *Obtain informed consent* — consent is documented per local programme requirements (written, witnessed-verbal, or electronic as applicable)
5. End event

**Called from.** Workflow 2 (Primary Screening, before sample collection); Workflow 3 (Triage, before VIA); Workflow 4 (Treatment, before ablation, LLETZ/LEEP, or CKC — not before referral for suspected invasive cancer, which involves a different counselling conversation about suspected malignancy that programmes typically handle in a separate pathway outside the DAK's scope).

**Activity references.** Sub-process-internal only — not present in the main action vocabulary, consistent with the SOP's framing of counselling/consent as a cross-cutting concern rather than a cascade-activity-proper.

![Counselling and informed consent sub-process — linear sequence of start event, explain procedure, confirm understanding, obtain informed consent, end event](subprocess-counselling-consent.svg)

**Diagram file:** `input/bpmn/subprocess-counselling-consent.bpmn` → `input/images/subprocess-counselling-consent.svg`.

## BPMN source files and rendering

This DAK commits BPMN source in the IG repository as editable `.bpmn` files (BPMN 2.0 XML) and renders them to SVG for IG publication.

| Path | Contents |
|---|---|
| `input/bpmn/workflow-*.bpmn` | BPMN 2.0 source files — the editable canonical representation of each workflow |
| `input/images/workflow-*.svg` | Rendered SVG exports — what the IG page embeds |

**Tooling.** [Camunda Modeler](https://camunda.com/download/modeler/) (free, desktop, offline). Open the `.bpmn` file, edit visually, save. Export to SVG via *File → Save File As… → .svg*, writing to `input/images/`. Commit both the updated `.bpmn` and the regenerated `.svg`.

**Why this convention.** BPMN XML is text, diffable under git — though diffs are noisy when visual layout changes, because coordinates move around. Committing the source alongside the rendered image keeps the diagram authoritatively reproducible (re-render at any time) and version-controlled at the semantic level (activity names, flows, gateways are diffable even when coordinates are not). This matches the repository's general rule: *commit the format git understands; render the format the audience expects.*

## Status

*Draft — Phase 1 of Component 4 authoring (2026-04-22).* The page declares five workflows and one reusable sub-process, each specified at the level of detail Component 4 requires: pools, lanes, activity sequence, gateways with branch conditions, message flows, sub-process calls, and register-entry references where interpretive choices bear. Activity labels are lifted verbatim from the Component 3 action vocabulary.

**BPMN source authoring — pending.** The `.bpmn` XML files and their SVG exports are not in the repository yet. The semantic content of each workflow is fully specified above, so the authoring step from here is mechanical: open Camunda Modeler, create one diagram per workflow (and one for the sub-process, and one overview diagram), drop in the pools/lanes/activities exactly as listed, connect with sequence flows and message flows per the descriptions, save to `input/bpmn/`, export to `input/images/`, and commit. No new design decisions are deferred to that pass — only the visual rendering.

**SME validation — pending, inherited.** Each workflow's validation domain is the same as that of the personas whose lanes it contains; the [personas page's per-persona SME notes](generic-personas.html#personas) apply by reference.

**Cross-DAK reuse — deferred.** Whether to harvest workflow patterns or sub-processes from the WHO ANC or HIV DAKs (which may publish comparable counselling-and-consent patterns, for instance) is a deferred analysis, not blocking this Phase-1 draft.

**L3 representation — deferred.** Whether FHIR `PlanDefinition` and `ActivityDefinition` resources should be authored as L3 machine-readable counterparts to these workflows is a separate decision and is not required by Component 4 itself.
