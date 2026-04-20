# Cervical Cancer Case Study — Core Data Dictionary

This IG contains the minimum-viable Core Data Dictionary (CDD) for the cervical cancer case study. The CDD itself is in [`dictionary`](dictionary.html); this README explains what the CDD is, how its columns are organised, what the Kind classification means, what the L2/L3 boundary does, and why the framing of that boundary is tri-purpose — layer, cross-DAK, and country-adaptation.

## What this CDD is

A structured L2 face of every input and output exercised by [`textualist.dmn`](l2/textualist.dmn), plus two deferred stub rows (pregnancy, vaccination) that reserve slots for planned register entries ([`cc-006`](cc-006.html), [`cc-004`](cc-004.html)). Nineteen rows total. The row selection principle is strict: every row in the CDD must be traceable to either (a) a decision input/output in `textualist.dmn`, or (b) a register entry — anything else is out of scope for this minimum-viable first pass.

The harvest script at [`dak-harvest/harvest-cdes.py`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/dak-harvest/harvest-cdes.py) produced a flat per-DAK filtered index at [`harvested-cdes-from-existing-daks.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/harvested-cdes-from-existing-daks.md) (harvest timestamp 2026-04-10). That index is the raw material; this CDD is the curated, structured, L2/L3-partitioned product that a country adaptation team could consume.

## Column structure

The CDD mirrors the SMART Guidelines DAK template column order as closely as markdown permits. See [`authoring-workflow.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md) lines 113–142 for the underlying boundary rule and [`cross-dak-data-harmonization.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/cross-dak-data-harmonization.md) line 50 for the canonical column list the template uses.

**L2 columns** (populated by every row):

- `Activity ID` — which decision table / workflow stage
- `Data Element ID` — `HIV.*.DE*` / `STI.*.DE*` / etc. for harvested (Kind 2), `CC.*.DE*` for novel (Kind 1)
- `Label` — short human-readable name
- `Description` — natural-language meaning
- `Data Type` — Boolean / Coding / Date / DateTime / Quantity / String / number
- `Input Options` — allowed values (for Coding)
- `Required` — R / C / O
- `Linkages (DMN)` — references to `textualist.dmn` decisions and rules
- `Linkages (Register)` — references to interpretation register entries
- `Annotations` — free-text notes

**L2/L3 bridge column** (populated by every row):

- `Terminology Intent` — natural-language description of what the element means, to inform L3 binding without prescribing it. This column is where the "what does this element represent" question is answered without making terminology-binding decisions.

**L3 columns** (intentionally blank on every row):

- `ICD-11`, `SNOMED CT`, `LOINC`, `ICHI`, `ICF`
- `FHIR Resource`, `FHIR Profile`, `Canonical URI`

**Kind classification column** (populated by every row):

- `Kind` — 1 (novel to CC), 2 (harvested with provenance), 3 (proposed to smart-core)

**Kind 2 provenance columns** (populated on Kind 2 rows only):

- `Source DAK` — e.g., `HIV`
- `Source DE ID` — e.g., `HIV.D.DE664`
- `Source Commit` — commit hash of the source DAK at harvest time (blank in this first pass; see Phase B note below)
- `Reuse Intent` — `reuse-as-is` / `extend` / `propose-to-core`

## Kind classification

Three kinds of entries, per [`smart-core-comments.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/smart-core-comments.md) Option 4 hybrid:

**Kind 1 — Locally-novel.** Elements genuinely novel to cervical cancer screening. Not found in any existing DAK's data dictionary. Authored fresh with CC-domain IDs (`CC.*.DE*`). In this CDD: transformation zone type, ablation eligibility, treatment plan, follow-up plan, suspicion of cancer, years since last screen, and the DAK-computed outputs.

**Kind 2 — Harvested with provenance.** Elements that already exist in another SMART Guidelines DAK and can be referenced rather than reinvented. The CDD row records the source DAK, source DE ID, source commit hash (blank in this first pass), and reuse intent (reuse-as-is / extend / propose-to-core). The snapshot approach — copy the L2-face at harvest time — gives point-in-time provenance and decouples the CC CDD from upstream drift, analogous to how `package-lock.json` works in the Node.js ecosystem. In this CDD: age, sex, living with HIV, date of last screening, prior screen result, VIA result, pregnancy status (stub), vaccination status (stub).

**Kind 3 — Proposed to smart-core.** Elements that should eventually live in the smart-core shared data dictionary (or its successor) and be referenced by every DAK that needs them, rather than being duplicated across domain DAKs. **Kind 3 is not exercised by any row in this first pass.** See the "Deferred as purposive refinement" section at the end of [`dictionary`](dictionary.html) for the `HasCervix` candidate that would populate Kind 3 if and when a Phase B triangulation artifact or a future purposive DMN authoring pass opens the venue for it.

## The L2/L3 boundary

The methodology's [`authoring-workflow.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md) lines 113–142 prescribes a column-level boundary between L2 (what a clinical SME can validate) and L3 (what a terminology specialist or FHIR implementer binds). This CDD is the first artifact that exercises the boundary on real data rather than asserting it rhetorically.

**What L2 contains.** Element identity, semantics, data type, allowed values, conditionality, decision-table linkages, free-text annotations, and the `Terminology Intent` bridge column. Everything a clinical SME or country adaptation team can read and validate without requiring FHIR or terminology expertise.

**What L3 contains.** Terminology bindings (ICD-11, SNOMED CT, LOINC, ICHI, ICF) and FHIR implementation mappings (resource type, profile, extension, canonical URI). Everything that requires a terminology specialist or a FHIR implementer to land correctly in a country's EHR.

**Why the L3 columns are blank in this CDD.** Not because the L3 work is unimportant but because the L3 work is *context-dependent*. A country deploying the CC DAK against Bahmni has different FHIR binding targets than a country deploying against eTracker or SmartCare or Impilo. A country whose national terminology server speaks SNOMED CT Global Patient Set has different binding paths than one that uses ICD-11 primary. Baking one country's L3 bindings into the generic CDD would force every other country to undo them. Leaving L3 blank and supplying `Terminology Intent` as a bridge lets every country's L3 implementers start from the same clinically-validated L2 content.

## The tri-purpose framing

The L2/L3 boundary does three jobs at once, not one. Naming all three is the conceptual contribution this CDD is trying to make; it is also what makes the CDD valuable to country adaptation teams, not only to methodology reviewers.

**Job 1 — Layer separation.** The one the methodology's [`authoring-workflow.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md) already articulates: clinical content (L2) is separable from FHIR and terminology binding (L3), so interpretive decisions made at L2 are not distorted by downstream implementation concerns. The register entries in the [interpretation register](https://github.com/dhes/dak-authoring-methodology/tree/main/case-studies/cervical-cancer/interpretation-register) respect this rule; [`cc-001`](cc-001.html) is the exemplar, with its inline terminology guidance deliberately omitted in favour of the per-row `Terminology Intent` bridge column.

**Job 2 — Cross-DAK harmonization.** The one the published literature points at without a fully functioning mechanism: Pretty et al. (2023) recommend a "master spreadsheet that standardises data elements repeated across sections, to reduce the time and potential inconsistencies in coding"; [`smart-core-comments.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/smart-core-comments.md) observes that the smart-core repo was set up by the right people (Rhodes, Leitner, Costa Teixeira, Stevenson) but has been dormant since ~2021, so cross-DAK harmonization happens accidentally via per-DAK harvests rather than deliberately via a canonical shared dictionary. The L2/L3 boundary is what makes harvest-based sharing tractable: the L2 side of a harvested element is the portable part, and each DAK that references it can do its own L3 binding if needed.

**Job 3 — Country-adaptation workflow.** The one Muliokela et al. (2025) implicitly surface but don't name explicitly. Their [`3-muliokela.pdf`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/publications/3-muliokela.pdf) describes five-country pathfinder DAK adaptation work in Ethiopia, Ghana, Malawi, Zambia, and Zimbabwe. Their Table 2 names "the initial content adaptation process might require more time due to the volume of DAK elements" as a core challenge, and recommends "conducting preparatory steps, such as guideline extraction and premapping, to assess/select initial areas for adaptation, prior to stakeholder validation." Their Premapping Tool (Tool 3 in their Table 1) asks three questions of each DAK data element: does it already exist in the country's protocols/guidelines/registers; should it be added to the country-adapted DAK; does it need modifications.

**The connection.** Muliokela's premapping workshops have two audiences with different concerns. Clinicians and MOH program staff care about whether a data element matches the country's clinical workflow (the L2 question). Digital-health implementers and terminology specialists care about how the element maps to the country's EHR schema and terminology server (the L3 question). Running both audiences through one wide table with mixed L2 and L3 content is exactly the "volume of DAK elements" overwhelm Muliokela names as a core challenge.

An L2-only view of the CDD — exactly what this CDD presents, with L3 columns blank — is what a clinical-review premapping workshop would consume. A L3-binding workshop, held separately with different participants and a narrower scope, would take the validated L2 subset and populate the L3 columns per the country's EHR and terminology infrastructure. Splitting the workshop along the L2/L3 line is a strict improvement over running one wide workshop, and it maps cleanly onto the methodology's boundary rule without requiring Muliokela's tool to be rewritten.

**The unification.** Jobs 2 and 3 are the same problem from different angles. Cross-DAK harmonization asks "how do we reuse an HIV DAK element in a CC DAK without copying its terminology binding and creating drift"; country adaptation asks "how does a country adopt a generic DAK element and bind it to their EMR." Both want a stable clinical spec (L2) separated from a re-doable layer of binding (L3). The L2/L3 boundary delivers that, and once articulated as tri-purpose, it positions the methodology's contribution as a bridge between the published literature (Pretty et al., Tamrat et al., the smart-core aspiration) and the field literature (Muliokela et al.'s country pathfinder experience).

## Scope limits

This is a minimum-viable CDD, not a complete CC DAK data dictionary. Explicitly out of scope:

- **Elements not consumed by the current `textualist.dmn`.** The plan file for this work (`silly-gathering-flamingo.md` in the user's local Claude state) originally listed `LifetimeScreeningTestNumber`, `PrimaryScreeningTestType`, and `TriageTestType` as candidate Kind 2 rows. Close reading of the textualist revealed that none of those are consumed by any current decision rule, and none map to a current register entry; by the plan's own verification rule ("every row traceable to a textualist decision input/output OR a register entry") they should not be in the CDD. They may be added in a more complete CC DAK CDD when the textualist or the register grows to cover them.
- **Algorithms 1–4, 6, 7 of the 2021-07 guideline.** The case study's scope declaration in [`cc-000`](cc-000.html) limits the DAK to Algorithm 5 (HPV DNA primary screening with VIA triage). Data elements specific to the other six algorithms (cytology, colposcopy, HPV16/18 genotyping triage, HPV mRNA, dual-stain cytology) are out of scope.
- **Programme-level / facility-readiness elements.** LBC capability, laboratory infrastructure, workforce training status. These are not patient-level decision inputs and belong in a facility-readiness dataset, not the clinical decision table CDD.
- **Upstream data-acquisition details.** The clinical acts that populate the boolean inputs (how a VIA reading is made, how TZ type is visually determined, how "cancer suspected" is decided in the clinic) are out of scope per the scope declaration. See [`cc-003`](cc-003.html) for the register entry that documents what the "cancer suspected" boolean hides.
- **L3 binding decisions.** The core of the tri-purpose framing: L3 work is deferred to country-adaptation implementers. This CDD deliberately does not prescribe SNOMED CT codes, FHIR resource types, or canonical URIs.

## Versioning and the Source Commit gap

The Kind 2 rows in this first pass have blank `Source Commit` fields. This is a known gap inherited from the harvest script's current behaviour: [`harvest-cdes.py`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/dak-harvest/harvest-cdes.py) ingests xlsx files from a local `xlsx/` directory and does not capture the source repository commit hashes at harvest time. The Option 4 hybrid in [`smart-core-comments.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/smart-core-comments.md) names this as a required capability for versioning-discipline ("periodic re-harvest to detect upstream drift"), and the plan file for this work scopes the harvest-script extension as Phase B tooling. Until Phase B is undertaken, the Kind 2 rows in this CDD reference the source DAKs by DE ID and label only, and the snapshot is dated 2026-04-10 via the harvest file header.

Consumers of this CDD should treat the Kind 2 rows as "current as of 2026-04-10 and subject to upstream drift detection when commit-capture is added." This is an honest acknowledgment of the current ecosystem's lack of a cross-DAK dependency management layer; it is not a claim that the methodology has solved the versioning problem.

## How to read the CDD

Two entry points, depending on why you're reading:

- **Quick scan.** Read the summary table at the top of [`dictionary`](dictionary.html). Nineteen rows, each with its DE ID, data type, kind, and source/linkage. Suitable for a country team evaluating whether the DAK's data surface maps to their EHR at all.
- **Detailed review.** Read the per-row blocks below the summary table. Each block carries the full L2 column set with decision-rule linkages, terminology intent, and annotations. Suitable for a clinical SME workshop reviewing the CC DAK's data-element-level content element by element.

Cross-references from the CDD to the interpretation register are bidirectional: every register entry that references a data element is cited in the corresponding CDD row's `Linkages (Register)` field. The CDD is intended to be navigable alongside the register, not as a replacement for it.

## Relationship to other methodology artifacts

- [`authoring-workflow.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/authoring-workflow.md) lines 113–142 — the underlying L2/L3 boundary rule.
- [`cross-dak-data-harmonization.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/methodology/cross-dak-data-harmonization.md) — the published-literature synthesis on cross-DAK harmonization (Pretty, Tamrat, Mehl, Muliokela, GUIDE).
- [`smart-core-comments.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/smart-core-comments.md) — the Option 4 hybrid and the dormant-smart-core observation.
- [`harvest-cdes.py`](https://github.com/dhes/dak-authoring-methodology/blob/main/tools/dak-harvest/harvest-cdes.py) — the harvest script that produced the raw per-DAK index this CDD curates.
- [`harvested-cdes-from-existing-daks.md`](https://github.com/dhes/dak-authoring-methodology/blob/main/case-studies/cervical-cancer/narrative/harvested-cdes-from-existing-daks.md) — the harvest snapshot (2026-04-10) that the Kind 2 rows draw from.
- [Interpretation register](https://github.com/dhes/dak-authoring-methodology/tree/main/case-studies/cervical-cancer/interpretation-register) — the interpretation register, which this CDD cross-references row-by-row. Its IG-rendered counterparts are [`cc-000`](cc-000.html) through [`cc-007`](cc-007.html).
- [`textualist.dmn`](l2/textualist.dmn) — the decision logic this CDD documents the L2 face of.
