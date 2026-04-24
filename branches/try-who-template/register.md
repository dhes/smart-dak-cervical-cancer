# Interpretation Register - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Interpretation Register**

## Interpretation Register

This page provides the catalogue and reading guide for the Interpretation Register. Each entry documents one interpretive decision made in translating the WHO 2021 cervical cancer screening guideline into L2 decision logic.

See the [Methodology](methodology.md) page for the register schema and the reasoning behind the entry categories.

### Reading this register

Entries are listed in **reading order**, not by numerical ID. Entry IDs (`cc-000`, `cc-001`, etc.) are stable identifiers assigned in drafting order; they do not determine reading sequence.

### Entry Catalogue

#### Section 1 — Scope and Foundation

| | | | |
| :--- | :--- | :--- | :--- |
| [cc-000](cc-000.md) | scope | DAK scope, inheritance, and epidemiological regime | proposed |

#### Section 2 — Foundation clinical decisions

| | | | |
| :--- | :--- | :--- | :--- |
| [cc-002](cc-002.md) | inference | WLHIV operationalisation as patient-level boolean | proposed |
| [cc-003](cc-003.md) | inference | "Cancer suspected" as boolean input hiding clinical judgment | proposed |
| [cc-004](cc-004.md) | inference | Vaccination status as missing DAK input (unvaccinated-cohort assumption) | proposed |

#### Section 3 — Specifications (evidence-bounded policy choices)

| | | | |
| :--- | :--- | :--- | :--- |
| [cc-005](cc-005.md) | specification | Screening interval resolution (general population and WLHIV) | proposed |

#### Section 4 — Population and Inclusion

| | | | |
| :--- | :--- | :--- | :--- |
| [cc-001](cc-001.md) | disambiguation | "Woman" operationalised as "has cervix" | accepted (first case study) |

#### Section 5 — Inferences over silences in the guideline

| | | | |
| :--- | :--- | :--- | :--- |
| [cc-006](cc-006.md) | inference | Pregnancy handling across the cascade | proposed |
| [cc-007](cc-007.md) | inference (deliberate simplification) | Sexual exposure precondition implicit in age thresholds | proposed |
| [cc-008](cc-008.md) | inference | HIV status absent/unknown: semantics and handling | proposed |

### Status Legend

* **proposed** — entry drafted, awaiting review
* **accepted** — entry reviewed and stable; the purposive DMN encodes this decision
* **flagged-for-sme-review** — entry written, DMN has provisional encoding, choice held open pending clinical SME input
* **deferred** — entry identified but not yet drafted

