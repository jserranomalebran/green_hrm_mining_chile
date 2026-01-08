# Data dictionary (rrhhverdedatosperdidos2)

**File(s):**
- `data/raw/rrhhverdedatosperdidos2.txt` (original; semicolon-separated)
- `data/raw/rrhhverdedatosperdidos2.csv` (CSV copy)

## General
- **Unit of analysis:** individual manager/key informant (organization-level perceptions)
- **Response format:** 7-point Likert for substantive constructs.
- **Notes:** Some columns appear to be computed composite scores (e.g., `CHV`, `CEV`, `CRV`). The current manuscript model typically uses item-level indicators; keep or drop composites depending on your analysis workflow.

## Green Human Resource Practices (GHRP)
Variables (items):
- `PRHV1`
- `PRHV2`
- `PRHV3`
- `PRHV4`
- `PRHV5`
- `PRHV6`

## Green Human Capital (GHC)
Variables (composite + items):
- `CHV1`
- `CHV2`
- `CHV3`
- `CHV4`
- `CHV5`
- `CHV`

## Green Structural Capital (GSC)
Variables (composite + items):
- `CEV1`
- `CEV2`
- `CEV3`
- `CEV4`
- `CEV5`
- `CEV6`
- `CEV7`
- `CEV8`
- `CEV`

## Green Relational Capital (GRC)
Variables (composite + items):
- `CRV1`
- `CRV2`
- `CRV3`
- `CRV4`
- `CRV5`
- `CRV6`
- `CRV`

## Green Competitive Advantage (GCA)
Variables (items):
- `VCV1`
- `VCV2`
- `VCV3`
- `VCV4`
- `VCV5`
- `VCV6`
- `VCV7`
- `VCV8`
- `VCV9`
- `VCV10`
- `VCV11`

## Ambidexterity (optional / not used in the current GHRP→GIC→GCA model)
Variables (items):
- `Ambidestreza1`
- `Ambidestreza2`
- `Ambidestreza3`
- `Ambidestreza4`
- `Ambidestreza5`
- `Ambidestreza6`
- `Ambidestreza7`
- `Ambidestreza8`

## Sociodemographics / controls (as coded in the questionnaire)
Variables:
- `Q4`
- `Q2`
- `Q3`
- `QID5`
- `Q6`
- `Q7`
- `Q8`
- `Q9`
- `Q10`
- `Q18`

## Recommended cleaning
- Remove any direct identifiers before public release (e.g., IP addresses, names, emails).
- Verify the final indicator set used in the manuscript (e.g., `CRV1–CRV5` vs `CRV1–CRV6`) and align the measurement-scale description accordingly.
