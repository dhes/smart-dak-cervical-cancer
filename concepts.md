# Concepts - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* **Concepts**

## Concepts

This page defines the key terms and concepts used across the IG — clinical vocabulary from the WHO 2021 cervical cancer guideline, interpretive terms this DAK uses when recording its repackaging of the guideline, WHO SMART Guidelines conventions, and the programmatic frameworks (GRADE, 90-70-90) the DAK references.

Terms are grouped by domain. Where a concept has its own page in this IG, the entry links to that page rather than duplicating content.

## Clinical concepts

| | |
| :--- | :--- |
| **Algorithm 5** | The cervical cancer screening cascade modelled by this DAK: HPV DNA as the primary screen, VIA as the triage test for HPV-positive women, thermal ablation or excision as treatment. One of seven candidate algorithms the 2021 WHO guideline enumerates; selection rationale at[Algorithm Selection](algorithm-selection.md). |
| **HPV DNA** | Human papillomavirus DNA test — the primary screening test in Algorithm 5. Returns a positive / negative / invalid result per tested woman. |
| **VIA** | Visual Inspection with Acetic acid — a triage test in which a clinician applies acetic acid to the cervix and visually inspects for acetowhite changes. Used in Algorithm 5 as the triage step after an HPV-positive primary screen. |
| **WLHIV** | Women Living with HIV. A distinct cascade population under the 2021 guideline: screening starts at age 25 (vs. 30 for the general population), triage is mandatory (rec 22), retest intervals are shorter. |
| **Thermal ablation** | A treatment modality in which the precancerous lesion is destroyed with heat. Suitable for ablation-eligible lesions; performed by a nurse/midwife with training. |
| **LLETZ / LEEP** | Large-Loop Excision of the Transformation Zone / Loop Electrosurgical Excision Procedure — an excision treatment for lesions too large or deep for ablation. Performed by an advanced clinician. |
| **CKC** | Cold-Knife Conization — a deeper excision procedure, primarily used for adenocarcinoma in situ (AIS). Performed by an advanced clinician at referral-hospital level. |
| **AIS** | Adenocarcinoma In Situ — a glandular precancerous lesion. Treatment of choice is CKC rather than LLETZ/LEEP. |
| **Ablation-eligible lesion** | A precancerous lesion meeting criteria for thermal ablation: small, fully visible on the ectocervix, clearly defined margins, no suspicion of invasive cancer. |
| **Suspected invasive cancer** | Triage findings suggestive of invasive cervical cancer rather than a treatable precancer. In Algorithm 5 these are routed to specialist referral rather than to cascade treatment. Operational definition in[cc-003](cc-003.md). |
| **Cascade** | The end-to-end cervical cancer screening-and-treatment flow: invitation → primary screening → triage → treatment → follow-up. "Cascade attrition" refers to women lost between steps. |
| **Transformation zone** | The region of the cervix where glandular epithelium meets squamous epithelium — the site where most precancerous lesions arise. Visibility of the transformation zone is one of the criteria for ablation-eligibility. |

## Interpretive work

| | |
| :--- | :--- |
| **Textualist interpretation** | An interpretation strategy that stays faithful to the literal guideline language. For recommendations that permit multiple valid readings, the textualist interpretation selects the reading with the strongest explicit textual warrant. The[textualist DMN](decision-logic.md)encodes this strategy. |
| **Purposive interpretation** | An interpretation strategy that resolves textual ambiguity by reference to the guideline's stated purpose (elimination-strategy targets, recommendations' underlying rationale). The[purposive DMN](decision-logic.md)encodes this strategy. Divergences from the textualist DMN are documented in individual register entries. |
| **Interpretation register** | The ledger of interpretive decisions this DAK makes in translating the WHO guideline narrative (L1) into decision logic (L2). See the[Interpretation Register overview](register.md); individual entries are`cc-000`through`cc-008`. |
| **Register entry** | A single documented interpretive decision (`cc-NNN`), recording the options considered, the option selected, and the rationale. Entry categories include**scope**,**specification**,**clinical**,**inference over silence**, and**semantics**. |
| **Scope declaration** | The register entry ([cc-000](cc-000.md)) that establishes what this DAK models, what it explicitly excludes, and what epidemiological regime it assumes. The most important single entry for understanding the DAK's applicability. |
| **Kind 1 / Kind 2 / Kind 3** | Classification applied to Core Data Dictionary elements:**Kind 1**— authored locally to this DAK;**Kind 2**— harvested from another WHO SMART DAK with provenance;**Kind 3**— proposed for a shared canonical dictionary. Full definition in the[Data Dictionary README](README.md). |
| **Tier A / Tier B indicators** | Classification applied to indicators (Component 8):**Tier A**— computable from period counts, feasible from paper-based registers;**Tier B**— requires longitudinal tracking by stable patient identifier. See[Indicators scope](indicators.md#scope-and-authoring-posture). |
| **Algorithm selection analysis** | The recommendation-by-recommendation walk-through ([Algorithm Selection](algorithm-selection.md)) showing how the 2021 guideline narrows the field from seven candidate algorithms to Algorithm 5 for countries with the epidemiological profile in cc-000. |

## WHO SMART Guidelines conventions

| | |
| :--- | :--- |
| **DAK** | Digital Adaptation Kit — WHO's framework for packaging clinical guideline content as computable, software-neutral artifacts. |
| **L1 / L2 / L3 / L4** | The four layers of a SMART Guideline:**L1**narrative normative guidance (the WHO guideline itself);**L2**operational artifacts (this IG's scope — decision logic, workflows, data dictionary);**L3**machine-readable FHIR artifacts (profiles, CQL, value sets — deferred in this DAK);**L4**implementation in a live digital system. |
| **SOP** | Standard Operating Procedure — WHO's prescriptive authoring process for SMART Guidelines. The L2 SOP is at[smart.who.int/ig-starter-kit/l2_dak_authoring.html](https://smart.who.int/ig-starter-kit/l2_dak_authoring.html). |
| **FHIR** | Fast Healthcare Interoperability Resources — the HL7 standard underlying WHO SMART Guidelines at L3. |
| **DMN** | Decision Model and Notation — the OMG standard for decision-table and decision-requirements-diagram authoring. This DAK's decision logic (Component 6) is authored in DMN. |
| **BPMN** | Business Process Model and Notation — the OMG standard for workflow authoring. This DAK's business processes (Component 4) are authored in BPMN. |
| **CDD** | Core Data Dictionary — the DAK's catalogue of data elements (Component 5). |
| **CDHI** | Classification of Digital Health Interventions — WHO's taxonomy for classifying digital-system functionality. |
| **UHC Compendium** | WHO's Universal Health Coverage Compendium — a catalogue of clinical interventions with identifiers. |
| **CI build** | "Continuous integration" build — the rolling version of an IG served at its canonical URL, not a formally frozen release. |

## Programmatic frameworks

| | |
| :--- | :--- |
| **90-70-90 targets** | The WHO[Cervical Cancer Elimination Strategy](https://www.who.int/publications/i/item/9789240014107)'s targets:**90%**of girls HPV-vaccinated by age 15;**70%**of women screened with a high-performance test by ages 35 and 45;**90%**of women with precancer treated and 90% of women with invasive cancer managed. |
| **GRADE — Strong recommendation** | A GRADE classification indicating high confidence that desirable effects outweigh undesirable effects. Marked "Strong" in the 2021 guideline; e.g., rec 1 (HPV DNA as primary test). |
| **GRADE — Conditional recommendation** | A GRADE classification indicating that desirable effects**probably**outweigh undesirable effects, but the balance depends on context. Most of the 2021 guideline's recommendations are conditional. |
| **Good Practice Statement (GPS)** | A normative statement made outside the GRADE framework, typically when a recommendation is uncontroversial enough that formal evidence review is not required. E.g., rec 41 (treat within 6 months; defer during pregnancy). |
| **Capability Maturity Model (CMM)** | A framework for describing process maturity, used by WHO SMART Guidelines to indicate IG status. Level 1 (Initial) → Level 5 (Optimising). |
| **FHIR Maturity Model (FMM)** | A related framework used by FHIR IGs. FMM 0 (draft) → FMM 5 (normative). This IG is at FMM 0. |

