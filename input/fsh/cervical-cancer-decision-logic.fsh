// Placeholder FHIR Library resource for the Cervical Cancer DAK's decision logic.
//
// Purpose of this file:
//   The FHIR ImplementationGuide structure requires at least one resource in
//   definition.resource. An L2-only DAK like this one has no authored FSH profiles,
//   CapabilityStatements, or other conformance resources until L3 authoring begins.
//   This Library resource satisfies the FHIR minimum-resource validation and acts
//   as a semantic anchor: when L3 CQL authoring eventually happens, the CQL
//   expressions will attach to this Library or replace it.
//
// The actual L2 decision logic currently lives in the DMN files at
// input/l2/purposive.dmn and input/l2/textualist.dmn, rendered on the
// Decision Logic page.

Instance: cervical-cancer-decision-logic
InstanceOf: Library
Usage: #definition
Title: "Cervical Cancer DAK — Decision Logic (placeholder)"
Description: "Placeholder FHIR Library resource for the Cervical Cancer DAK's decision logic. L3 CQL authoring is deferred to Phase 2; the current L2 artifacts are the DMN files at input/l2/purposive.dmn and input/l2/textualist.dmn, rendered on the Decision Logic page. This placeholder exists to satisfy the FHIR ImplementationGuide validation requirement that at least one resource be present in the IG definition, and it declares a commitment to author the CQL library in a subsequent L3 phase."

* status = #draft
* experimental = false
* type = http://terminology.hl7.org/CodeSystem/library-type#logic-library
* name = "CervicalCancerDecisionLogic"
* version = "0.1.0"
* date = "2026-04-23"
* publisher = "Dan Heslinga"
