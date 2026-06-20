# Green Human Resource Practices and Sustainable Advantage (Chilean Mining)

This repository contains the **data file** and the **SmartPLS model** used in the manuscript:

> **Green Human Resource Practices and Sustainable Advantage: Evidence from the Chilean Mining Sector**

The study examines how **Green Human Resource Practices (GHRP)** influence **Green Competitive Advantage (GCA)**, and tests the mediating roles of the three dimensions of **Green Intellectual Capital (GIC)**:
**Green Human Capital (GHC)**, **Green Structural Capital (GSC)**, and **Green Relational Capital (GRC)**.

## Contents

- **Data**
  - `data/raw/rrhhverdedatosperdidos2.txt` (original; `;`-separated)
  - `data/raw/rrhhverdedatosperdidos2.csv` (CSV copy)
- **SmartPLS**
  - `models/MODELO21.splsm`
- **Documentation**
  - `docs/data_dictionary.md`
- **Utilities**
  - `scripts/convert_to_csv.py`

## Data overview

- **Collection context:** EXPONOR 2024 (Antofagasta, Chile), June 3–6, 2024  
- **Respondents:** managerial/key-informant survey (N = 300)  
- **Scale:** 7-point Likert for substantive constructs

### Main variable blocks (item-level)

- **GHRP:** `PRHV1–PRHV6`
- **GHC:** `CHV1–CHV5` (plus `CHV` composite score)
- **GSC:** `CEV1–CEV8` (plus `CEV` composite score)
- **GRC:** `CRV1–CRV6` (plus `CRV` composite score)
- **GCA:** `VCV1–VCV11`

> Note: The dataset also includes `Ambidestreza_1–Ambidestreza_8` and several `Q*` questionnaire fields. If these are not part of the final manuscript model, you can safely ignore them.

## Reproducibility (SmartPLS 4)

1. Open **SmartPLS 4**.
2. Create a new project and **import** the dataset (recommended: `data/raw/rrhhverdedatosperdidos2.csv`).
3. Import/open the model file: `models/MODELO21.splsm`.
4. Run **PLS Algorithm** (default settings are typically fine for replication).
5. Run **Bootstrapping** (10,000 subsamples; bias-corrected confidence intervals if you are reporting BCa/percentile intervals).
6. Export results tables/figures as needed.

## Privacy & sharing

- The dataset in this repository is provided for replication of the manuscript’s results.  
- Before making a repository public, **double-check** that no direct identifiers (emails, names, phone numbers, IP addresses) are present.  
  (In this export, typical direct identifiers are not included, but always verify.)

## How to cite

Add the final citation once the manuscript is published. A suggested placeholder:

> Serrano‑Malebrán, J., *et al.* (forthcoming). *Green Human Resource Practices and Sustainable Advantage: Evidence from the Chilean Mining Sector*.



## License

- Code/scripts: MIT (see `LICENSE`)
- Data/model: please align with your journal/data policy (you may want a more restrictive license for the dataset).
