This implementation guide presents Layer 2 (decision logic) artifacts for cervical cancer screening, modelling **Algorithm 5** (HPV DNA primary screening with VIA triage) from the [WHO 2021 Cervical Cancer Screening Guideline (2nd ed.)](https://www.who.int/publications/i/item/9789240030824).

### What this IG contains

This IG publishes the L2 artifacts of a cervical cancer screening Digital Adaptation Kit (DAK) authored using a textualist/purposive methodology:

- **Interpretation Register** — 8 entries documenting every interpretive decision made in translating the WHO guideline narrative (L1) into decision logic (L2). Each entry records the options considered, the option selected, and the rationale.
- **Core Data Dictionary** — 19 data elements covering every input and output of the decision logic, with linkages to harvested elements from existing WHO SMART DAKs (HIV, ANC, Immunizations).
- **Decision Logic** — Two parallel DMN (Decision Model and Notation) artifacts: a *textualist* version faithful to the guideline language, and a *purposive* version encoding the interpretive resolutions from the register.
- **Algorithm Selection Analysis** — A recommendation-by-recommendation walk-through of how the WHO guideline narrows the choice from seven candidate algorithms to Algorithm 5 for countries with the epidemiological profile described in the scope declaration.

### What this IG does not contain

**L3 (FHIR) artifacts are not yet authored.** This IG does not include FHIR profiles, CQL decision-support libraries, terminology bindings, or value sets. These are deferred to a future L3 authoring pass. The L2 artifacts are designed to be L3-ready: the Core Data Dictionary carries explicit L3-stub columns (ICD-11, SNOMED CT, LOINC, FHIR Resource, FHIR Profile, Canonical URI) that are intentionally blank, awaiting binding by a terminology specialist at country adaptation time.

**This is not a clinical recommendation.** The interpretive choices in this DAK belong to a hypothetical jurisdiction exercising a methodology. They are not recommendations for any real screening program. See the [Scope Declaration (cc-000)](cc-000.html) for the full disclaimer and the epidemiological regime the case study assumes.

### Reading order

The IG is organised by reading order, not by entry number. A reader encountering this material for the first time should proceed:

1. **[Algorithm Selection Analysis](algorithm-selection.html)** — Why Algorithm 5, and how the guideline narrows the field
2. **[Scope Declaration (cc-000)](cc-000.html)** — What the DAK models, what it excludes, and the epidemiological regime
3. **[Register overview](register.html)** — The interpretation register catalogue and reading guide
4. **Foundation clinical decisions** — [cc-002](cc-002.html), [cc-003](cc-003.html), [cc-004](cc-004.html)
5. **Specification** — [cc-005](cc-005.html) (screening interval resolution)
6. **Population and inclusion** — [cc-001](cc-001.html)
7. **Inferences over silences** — [cc-006](cc-006.html), [cc-007](cc-007.html)
8. **[Data Dictionary](dictionary.html)** and **[Decision Logic](decision-logic.html)**

### Background

This DAK was authored as a case study for a methodology that examines how WHO guideline narratives are translated into computable decision logic, with particular attention to the interpretive decisions that are typically invisible in published SMART DAKs. The methodology is documented in a [separate repository](https://github.com/dhes/dak-authoring-methodology) and summarised on the [Methodology](methodology.html) page.

### Status

This is a **draft** publication (version 0.1.0). All register entries are in `proposed` status. The DMN artifacts have been tested against Camunda 8.8 but have not been reviewed by clinical subject-matter experts.
