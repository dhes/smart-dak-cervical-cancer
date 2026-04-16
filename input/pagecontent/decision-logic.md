This page describes the decision-support logic for cervical cancer screening Algorithm 5, encoded as DMN (Decision Model and Notation) artifacts.

### Decision Requirements Diagram

The DAK models six decisions in a cascade:

1. **Eligible For Screening** (`CC.A.eligibility_{t,p}`) — by age, sex/anatomy, HIV status
2. **Due for Screening** (`CC.B.due_screening_{t,p}`) — by time since last screen, prior result, interval
3. **Triage Decision** (`CC.C.triage_{t,p}`) — HPV-positive → VIA; VIA result → treatment pathway
4. **Ablation Eligibility** (`CC.D.ablation_{t,p}`) — by transformation zone type and cancer suspicion
5. **Treatment Decision** (`CC.D.treatment_{t,p}`) — ablation, excision, deferral, or referral
6. **Follow-up Decision** (`CC.E.followup_{t,p}`) — post-treatment retest schedule

Decision IDs use the convention `CC.<activity>.<name>_{t,p}` where `_t` denotes the textualist variant and `_p` the purposive variant.

### Two parallel L2 artifacts

This DAK provides two DMN files, each encoding Algorithm 5 but with different interpretive postures:

**Textualist** (`textualist.dmn`) — A faithful encoding of the 2021-07 guideline as written. Preserves range strings where the guideline gives ranges (e.g., "every 5 to 10 years"), uses the guideline's population language verbatim (`ClientIsWoman`), and makes no interpretive choices beyond what is necessary to produce a functioning decision table.

**Purposive** (`purposive.dmn`) — Encodes the interpretive resolutions documented in the [Interpretation Register](register.html). Key differences from the textualist:

| Change | Register entry | Textualist | Purposive |
|---|---|---|---|
| Screening interval (general pop) | [cc-005](cc-005.html) | `"every 5 to 10 years"` | `"every 10 years"` |
| Screening interval (WLHIV) | [cc-005](cc-005.html) | `"every 3 to 5 years"` | `"every 5 years"` |
| Due-for-screening status buckets | [cc-005](cc-005.html) | 3 buckets (not yet due / within window / past window) | 2 buckets (not yet due / due) |
| Pregnancy handling | [cc-006](cc-006.html) | Not modelled | `IsPregnant` input at Treatment Decision; GPS 41 deferral |
| Treatment Decision hit policy | [cc-006](cc-006.html) | UNIQUE | FIRST (pregnancy rule takes precedence) |

All other decisions are identical between the two files. The textualist encodings for [cc-001](cc-001.html) (population as `Sex = Female`), [cc-002](cc-002.html) (WLHIV as boolean), [cc-003](cc-003.html) (cancer suspected as boolean), [cc-004](cc-004.html) (no vaccination input), and [cc-007](cc-007.html) (no sexual history input) are carried forward into the purposive unchanged, as documented in each entry's rationale.

### Rule descriptions

Every rule in both DMN files carries a `<description>` element documenting the clinical condition it encodes, the guideline recommendation it traces to, and (in the purposive) the register entry that authorises any divergence from the textualist. Rules are identified by Camunda Modeler-generated IDs (e.g., `DecisionRule_1yry35i`) consistent with WHO DAK convention, where rule identity is positional rather than semantic.

### DMN format note

The L2 decision logic is encoded as DMN XML executable on Camunda 8. This is a methodology choice for this case study, not a WHO SMART Guidelines convention. Published WHO DAKs represent L2 as structured decision-support tables in Excel/spreadsheet format within the DAK document. The DMN encoding is a parallel representation that enables automated testing against a DMN engine. See the [Methodology](methodology.html) page for discussion of this format choice and its implications.

### Downloads

The DMN files are available on the [Downloads](downloads.html) page.
