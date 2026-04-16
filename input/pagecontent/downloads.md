### L2 Decision Logic (DMN)

The following DMN files are available for download:

- **[textualist.dmn](l2/textualist.dmn)** — Faithful encoding of Algorithm 5 from the WHO 2021 guideline. 6 decisions, 43 rules. Preserves guideline range strings and population language verbatim.

- **[purposive.dmn](l2/purposive.dmn)** — Purposive encoding with interpretive resolutions from the register. 6 decisions, 42 rules. Resolves screening intervals to point estimates per [cc-005](cc-005.html), adds pregnancy handling per [cc-006](cc-006.html).

Both files are DMN 1.3 XML, tested against Camunda 8.8. They can be deployed to any DMN-compliant engine.

### Execution

To evaluate the decision logic:

1. Deploy the DMN file to a Camunda 8 instance (or compatible DMN engine)
2. POST to the decision evaluation endpoint with the decision ID and input variables

Example (purposive, Eligible For Screening):

```json
POST /v2/decision-definitions/evaluation

{
  "decisionDefinitionId": "CC.A.eligibility_p",
  "variables": {
    "ClientIsWoman": true,
    "AgeInYears": 35,
    "LivingWithHIV": false
  }
}
```

Decision IDs follow the convention `CC.<activity>.<name>_{t,p}` where `_t` denotes textualist and `_p` purposive. See the [Decision Logic](decision-logic.html) page for the full list.

### Source repository

The working repository for this DAK (including test fixtures, narrative analysis documents, and the full methodology) is at [github.com/dhes/dak-authoring-methodology](https://github.com/dhes/dak-authoring-methodology).
