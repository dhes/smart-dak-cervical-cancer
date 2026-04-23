This page lists the versions of this IG with a brief description of the major changes in each. Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html) — `major.minor.patch`.

## Version 0.1.0 (CI build) — 2026-04-23

**First publication of the Layer 2 artifacts for cervical cancer screening, Algorithm 5.** This is a draft release at FHIR Maturity Model (FMM) level 0; the content has not undergone SME validation or WHO SMART Guidelines submission. Expect material changes in subsequent versions.

### Content in this version

- **Interpretation Register** — 9 entries (`cc-000` through `cc-008`) documenting every interpretive decision in translating the WHO 2021 guideline narrative into decision logic.
- **Nine Tier-1 SOP components** — Interventions and Recommendations (Component 1), Generic Personas (Component 2), User Scenarios (Component 3), Business Processes and Workflows (Component 4 — including seven BPMN source files), Core Data Dictionary (Component 5), Decision Logic (Component 6 — DMN, textualist and purposive parallel artifacts), Scheduling Logic (Component 7), Indicators and Performance Metrics (Component 8 — 10 indicators), High-level Functional and Non-functional Requirements (Component 9 — 20 FRs and 12 NFRs).
- **Algorithm Selection Analysis** — methodology-layer walk-through of why Algorithm 5 was selected for this case study's epidemiological regime.
- **Supporting narrative** — scope declaration, methodology description, data-dictionary README, glossary of concepts, dependencies, license.
- **One placeholder FHIR resource** — `Library/cervical-cancer-decision-logic`, a semantic anchor for future L3 CQL authoring.

### Known limitations

- No FHIR L3 resources beyond the placeholder Library. Profiles, ValueSets, CodeSystems, and CQL libraries are deferred to a subsequent L3 authoring pass.
- No SME validation. All register entries are in `proposed` status; personas, scenarios, and indicators are analytically derived rather than interview-validated.
- Six of ten indicators depend on data elements not yet in the Core Data Dictionary (HPV DNA result, treatment type/date, retest dates, etc.) — a known Phase-2 gap.
- BPMN source files are authored but visual layout is first-pass; no cross-DAK reuse analysis of persona or workflow patterns has been performed.

### Issues list

No formally-tracked issues in this release. Future versions will enumerate issues by impact.

---

*When subsequent versions are cut, they will be added above this entry in reverse-chronological order, per HL7 IG convention.*
