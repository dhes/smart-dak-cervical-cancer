# Methodology - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Methodology**

## Methodology

This page describes how this DAK repackages the WHO 2021 cervical cancer guideline into L2 artifacts — the interpretive strategies used, how interpretive choices were recorded, how data elements were classified, and the format choices made.

### Textualist and purposive interpretive strategies

This DAK uses two parallel interpretive strategies when encoding the guideline's recommendations:

* **Textualist** — A faithful reading of the WHO guideline as written. Where the guideline gives a range ("every 5 to 10 years"), the textualist preserves it. Where the guideline uses specific language ("women"), the textualist mirrors it. The textualist makes no interpretive choices beyond what is necessary to produce a functioning decision table.
* **Purposive** — An encoding that resolves the interpretive questions the textualist leaves open, grounded in an epidemiological regime and evidence base declared in the scope entry. Every purposive divergence from the textualist is documented in an interpretation register entry with options considered, option selected, and rationale.

The textualist is the baseline; the purposive is the deployment-ready artifact. The register is the audit trail between them.

### The interpretation register

Each interpretive decision is recorded as a register entry with structured metadata:

* **Category** — `scope`, `disambiguation`, `specification`, `inference`, or `correction`
* **L1 provenance** — which guideline text is being interpreted, with epistemic status
* **Evidence provenance** — underlying evidence base (required for `specification` entries)
* **Options** — the alternatives considered
* **Selected** — which option was chosen
* **Rationale** — why this interpretation, not the others
* **Status** — lifecycle position (`proposed`, `accepted`, `flagged-for-sme-review`, etc.)

See the [Register](register.md) for the full catalogue.

### The Core Data Dictionary

The CDD documents every input and output of the decision logic with:

* **Data Element IDs** following the `CC.<activity>.DE<N>` convention
* **Kind classification** — Kind 1 (authored locally), Kind 2 (harvested from existing WHO SMART DAKs with provenance), Kind 3 (proposed to smart-core for cross-DAK reuse)
* **Explicit L3 stubs** — ICD-11, SNOMED CT, LOINC, FHIR columns are present but intentionally blank, awaiting L3 binding

### Algorithm selection

The WHO 2021 cervical cancer screening guideline presents seven candidate algorithms and delegates the choice between them to countries based on feasibility, training, programme quality assurance, and resources. The [Algorithm Selection Analysis](algorithm-selection.md) traces the recommendation-by-recommendation narrowing that leads to Algorithm 5 for countries with the epidemiological profile this DAK assumes.

### DMN as the L2 format

This DAK uses DMN (Decision Model and Notation) as the L2 representation, executed on Camunda 8. This is a provisional format choice. Published WHO DAKs represent L2 decision logic as structured tables in xlsx spreadsheet format. The DMN encoding enables automated testing and precise version comparison between textualist and purposive but diverges from the ecosystem's tooling pipeline. The format choice is documented as a resolved-for-now blocker in the register's [index](register.md) and may be revisited.

