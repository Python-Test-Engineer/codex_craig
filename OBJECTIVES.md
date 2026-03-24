# Oncological Research Objectives — ds01.csv

## Dataset Overview
Neuroblastoma patient cohort (`n` ≈ 500+) containing:
- **Demographics**: age at diagnosis (months), sex, weight
- **Disease staging**: INRG stage (1, 2A, 2B, 3, 4, 4S), risk group (low / intermediate / high)
- **Molecular markers**: MYCN amplification, ploidy, del(1p), gain(17q), 11q aberration, segmental chromosomal aberrations (SCA)
- **Histology**: favorable / unfavorable
- **Serum biomarkers**: LDH (IU/L), ferritin (ng/mL), NSE (ng/mL)
- **Treatment**: observation, induction chemotherapy, surgery only
- **Treatment response**: CR, PR, MR, NR, PD
- **Gene expression (log2)**: MYCN, ALK, PHOX2B, TH, CHGB, DBH, NTRK1, NTRK2, MDM2, CDK4, BIRC5, CCND1, MYC, TERT, ATRX, TP53, CDK6, CDKN2A, RB1, VEGF, HIF1A, HAND2, ID2, FOXO1
- **Outcomes**: event-free survival (EFS, months), overall survival (OS, months), event flags

---

## Research Objectives

### 1. Survival Analysis
- **O1.1** Generate Kaplan-Meier curves for EFS and OS stratified by risk group (low / intermediate / high).
- **O1.2** Compare OS and EFS between MYCN-amplified and non-amplified patients using log-rank tests.
- **O1.3** Perform multivariate Cox proportional-hazards regression for OS including stage, risk group, MYCN amplification, ploidy, histology, LDH, ferritin, and NSE as covariates.
- **O1.4** Determine 3-year and 5-year OS and EFS rates per disease stage.
- **O1.5** Assess whether age at diagnosis (< 18 months vs. ≥ 18 months) is an independent prognostic factor for EFS.

### 2. Biomarker Correlation & Prognostic Value
- **O2.1** Evaluate whether elevated LDH (above median) at diagnosis is associated with worse OS.
- **O2.2** Correlate serum ferritin levels with disease stage and risk group.
- **O2.3** Determine the optimal NSE cut-off for discriminating high-risk from non-high-risk patients (ROC / AUC analysis).
- **O2.4** Assess whether the combination of LDH + ferritin + NSE improves prognostic classification over any single marker alone.

### 3. Molecular & Genomic Risk Stratification
- **O3.1** Quantify the co-occurrence of MYCN amplification with del(1p), gain(17q), and 11q aberration.
- **O3.2** Determine whether segmental chromosomal aberrations (SCA) independently predict outcome when controlling for MYCN status.
- **O3.3** Compare EFS distributions across ploidy groups (diploid, near-triploid, hyperdiploid).
- **O3.4** Identify which combination of genomic markers (MYCN, del_1p, gain_17q, aberration_11q, ploidy) best stratifies patients into distinct survival clusters.

### 4. Gene Expression Profiling
- **O4.1** Identify gene expression features (from the 24 profiled genes) that are significantly differentially expressed between MYCN-amplified and non-amplified tumors (t-test / Mann-Whitney, FDR-corrected).
- **O4.2** Determine whether high TERT expression is associated with shorter EFS independent of MYCN amplification.
- **O4.3** Correlate NTRK1 and NTRK2 expression levels with histological classification (favorable vs. unfavorable) and with EFS.
- **O4.4** Assess whether ATRX expression differs significantly across ploidy groups.
- **O4.5** Build a gene expression signature (from the 24 genes) that predicts treatment response category (CR/PR vs. MR/NR/PD) using logistic regression or random forest.
- **O4.6** Cluster patients by gene expression profile (unsupervised hierarchical clustering or k-means) and test whether the resulting clusters align with established risk groups.

### 5. Treatment Response Prediction
- **O5.1** Identify pre-treatment clinical and molecular variables (stage, risk group, MYCN, biomarkers) that are the strongest predictors of complete response (CR).
- **O5.2** Compare response rates (CR vs. non-CR) between treatment modalities (observation, induction chemotherapy, surgery only).
- **O5.3** Determine whether gene expression of VEGF and HIF1A predicts response to induction chemotherapy.
- **O5.4** Build a multivariate model to predict progressive disease (PD) as an outcome; report sensitivity, specificity, and AUC.

### 6. Subgroup & Demographic Analysis
- **O6.1** Compare OS between male and female patients within each risk group.
- **O6.2** Characterise the stage 4S subgroup: distribution of molecular markers, response rates, and OS vs. other stage 4 patients.
- **O6.3** Assess whether weight at diagnosis (as a proxy for nutritional/physiological status) correlates with any clinical or molecular variable.

### 7. Integrated Risk Score Development
- **O7.1** Construct a composite prognostic score integrating clinical (stage, age), molecular (MYCN, SCA, ploidy), and gene expression features; validate using leave-one-out cross-validation.
- **O7.2** Compare the discriminative power (C-index) of the new composite score vs. the current INRG risk classification for predicting 5-year OS.

---

## Suggested Analytical Outputs
| Output | Description |
|--------|-------------|
| KM plots | Stratified survival curves with 95% CI and p-values |
| Forest plot | Hazard ratios from Cox multivariate model |
| Heatmap | Gene expression × patient cluster (with clinical annotations) |
| ROC curves | For biomarker and predictive model evaluations |
| Boxplots / violins | Biomarker distributions across risk/response groups |
| Correlation matrix | Pairwise relationships among continuous variables |
| Confusion matrix | For response-prediction classifiers |
