# Cervical Cancer DAK — Decision Logic (placeholder) - WHO SMART DAK — Cervical Cancer Screening (L2) v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Cervical Cancer DAK — Decision Logic (placeholder)**

## Library: Cervical Cancer DAK — Decision Logic (placeholder) 

| | |
| :--- | :--- |
| *Official URL*:https://dhes.github.io/smart-dak-cervical-cancer/Library/cervical-cancer-decision-logic | *Version*:0.1.0 |
| Draft as of 2026-04-23 | *Computable Name*:CervicalCancerDecisionLogic |

 
Placeholder FHIR Library resource for the Cervical Cancer DAK's decision logic. L3 CQL authoring is deferred to Phase 2; the current L2 artifacts are the DMN files at input/l2/purposive.dmn and input/l2/textualist.dmn, rendered on the Decision Logic page. This placeholder exists to satisfy the FHIR ImplementationGuide validation requirement that at least one resource be present in the IG definition, and it declares a commitment to author the CQL library in a subsequent L3 phase. 

* **Type: **: **Id: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: cervical-cancer-decision-logic
* **Type: **: **Version: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: 0.1.0
* **Type: **: **Url: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: [Cervical Cancer DAK — Decision Logic (placeholder)](Library-cervical-cancer-decision-logic.md)
* **Type: **: **Status: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: draft
* **Type: **: **Date: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: 2026-04-23
* **Type: **: **Publisher: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: Dan Heslinga
* **Type: **: **Description: **
  * **system: ** [http://terminology.hl7.org/CodeSystem/library-type](http://terminology.hl7.org/7.1.0/CodeSystem-library-type.html)  **code: ** logic-library: Placeholder FHIR Library resource for the Cervical Cancer DAK's decision logic. L3 CQL authoring is deferred to Phase 2; the current L2 artifacts are the DMN files at input/l2/purposive.dmn and input/l2/textualist.dmn, rendered on the Decision Logic page. This placeholder exists to satisfy the FHIR ImplementationGuide validation requirement that at least one resource be present in the IG definition, and it declares a commitment to author the CQL library in a subsequent L3 phase.



## Resource Content

```json
{
  "resourceType" : "Library",
  "id" : "cervical-cancer-decision-logic",
  "url" : "https://dhes.github.io/smart-dak-cervical-cancer/Library/cervical-cancer-decision-logic",
  "version" : "0.1.0",
  "name" : "CervicalCancerDecisionLogic",
  "title" : "Cervical Cancer DAK — Decision Logic (placeholder)",
  "status" : "draft",
  "experimental" : false,
  "type" : {
    "coding" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/library-type",
      "code" : "logic-library"
    }]
  },
  "date" : "2026-04-23",
  "publisher" : "Dan Heslinga",
  "contact" : [{
    "name" : "Dan Heslinga",
    "telecom" : [{
      "system" : "url",
      "value" : "https://github.com/dhes"
    }]
  }],
  "description" : "Placeholder FHIR Library resource for the Cervical Cancer DAK's decision logic. L3 CQL authoring is deferred to Phase 2; the current L2 artifacts are the DMN files at input/l2/purposive.dmn and input/l2/textualist.dmn, rendered on the Decision Logic page. This placeholder exists to satisfy the FHIR ImplementationGuide validation requirement that at least one resource be present in the IG definition, and it declares a commitment to author the CQL library in a subsequent L3 phase."
}

```
