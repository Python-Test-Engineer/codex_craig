# Response to Objectives

_Generated: 2026-03-24 15:36 UTC · Model: claude-opus-4-6 with extended thinking_

---

# Response to Research Objectives — Neuroblastoma Cohort (n = 400)

---

## Objective 1.1
**Generate Kaplan-Meier curves for EFS and OS stratified by risk group (low / intermediate / high).**

### Current Pipeline Evidence

The pipeline has generated `survival_km_by_risk.png`, which displays Kaplan-Meier–style curves stratified by the three INRG risk groups. The accompanying insight confirms visible separation across risk strata, with the high-risk group exhibiting the lowest median EFS and the low-risk group the highest. The pipeline report further quantifies event rates: high = 77.78%, intermediate = 33.33%, low = 11.57%. The `clinical_efs_by_risk.png` boxplot corroborates the distributional differences in EFS across strata.

However, the pipeline output does not confirm whether:
- A formal **log-rank test p-value** is annotated on the KM curve.
- **95% confidence intervals** (Greenwood formula) are displayed.
- **OS-specific** KM curves have been generated (only EFS appears explicitly referenced).
- Median survival with confidence bounds is tabulated per group.
- Number-at-risk tables are appended below the x-axis.

### Gaps & Recommended Analyses

| Gap | Required Action |
|-----|-----------------|
| OS KM curve stratified by risk group | Generate a second KM plot using OS as the time variable and the OS event flag as the censor indicator |
| Log-rank test statistic and p-value | Compute and annotate on both EFS and OS KM plots; for three-group comparison use the omnibus log-rank, then pairwise post-hoc with Bonferroni or Holm correction |
| 95% CI bands | Plot pointwise 95% CIs using the Greenwood standard error |
| Number-at-risk table | Append below each KM plot at regular time intervals (e.g., 0, 12, 24, 36, 48, 60 months) |
| Median survival table | Report median EFS and OS per risk group with 95% CI |

The recommended implementation uses `lifelines.KaplanMeierFitter` or R `survminer::ggsurvplot` with `risk.table = TRUE` and `pval = TRUE`.

### Biomedical Interpretation

The observed event rate gradient (low 11.6% → intermediate 33.3% → high 77.8%) is consistent with the established INRG risk classification framework. The roughly seven-fold difference in event rates between low- and high-risk groups validates the clinical utility of the risk assignment in this cohort. The intermediate group's 33% event rate occupies the expected middle ground and reinforces the need for refined molecular sub-stratification in this heterogeneous category. The cohort composition (198 high-risk, with remaining patients in low and intermediate) means that the KM curves for the high-risk group will have adequate statistical power, while the intermediate and low groups will require scrutiny for adequate sample size at later time points where censoring may thin the at-risk population.

---

## Objective 1.2
**Compare OS and EFS between MYCN-amplified and non-amplified patients using log-rank tests.**

### Current Pipeline Evidence

The pipeline produced `survival_km_by_mycn.png`, confirming visible time-to-event separation between MYCN-amplified (coded 1) and non-amplified (coded 0) patients. The report provides event rates: MYCN-amplified = 84.62%, non-amplified = 40.06%. This is a striking 44.6 percentage-point absolute difference in event incidence.

The pipeline does **not** report:
- A formal log-rank test statistic or p-value for EFS or OS.
- Whether the KM plot represents EFS, OS, or both.
- Median EFS/OS per MYCN group with 95% CI.

### Gaps & Recommended Analyses

1. **Log-rank test** (Mantel-Cox formulation) for both EFS and OS, reported with χ² statistic, degrees of freedom, and two-sided p-value.
2. **Univariate Cox regression** for MYCN status to produce a hazard ratio (HR) with 95% CI, complementing the non-parametric log-rank test with a semi-parametric effect size.
3. **Proportional hazards assumption check** via Schoenfeld residual test (`cox.zph` in R). MYCN-amplified tumors may have non-proportional hazards if early mortality is disproportionately high.
4. If the PH assumption is violated, report restricted mean survival time (RMST) differences at τ = 36 and τ = 60 months as supplementary measures.
5. Generate **separate KM plots for EFS and OS**, each annotated with log-rank p-value, median survival, and 95% CI.

### Biomedical Interpretation

An event rate of 84.6% among MYCN-amplified patients is among the highest reported in contemporary neuroblastoma cohorts and confirms MYCN amplification as the single most powerful adverse prognostic marker. The 40% event rate in non-amplified patients reflects the heterogeneous nature of MYCN-non-amplified disease, which includes both favorable (stage 1/2, favourable histology) and unfavorable (11q-aberrant, high-stage) subgroups. A formal log-rank test is expected to be highly significant (p < 0.001), but the associated HR is essential for quantifying the magnitude of risk elevation for comparison with published literature (typically HR 3–6 for OS in MYCN-amplified disease).

---

## Objective 1.3
**Perform multivariate Cox proportional-hazards regression for OS including stage, risk group, MYCN amplification, ploidy, histology, LDH, ferritin, and NSE as covariates.**

### Current Pipeline Evidence

**Not addressed.** No Cox regression output, forest plot, or multivariate hazard ratio table is present in the pipeline deliverables.

### Gaps & Recommended Analyses

This objective requires full de novo execution:

1. **Model specification**: Fit a Cox PH model with OS as the dependent variable. Covariates:
   - Stage: factor with 6 levels (1, 2A, 2B, 3, 4, 4S); reference = stage 1 or the most prevalent low-risk stage.
   - Risk group: ordinal factor (low, intermediate, high). **Note potential collinearity with stage**; consider including only one or using a variance inflation factor (VIF) diagnostic.
   - MYCN amplification: binary.
   - Ploidy: categorical (diploid / near-triploid / hyperdiploid).
   - Histology: binary (favorable / unfavorable).
   - LDH, ferritin, NSE: continuous; log-transform recommended given typical right-skew.

2. **Diagnostics**:
   - Schoenfeld residuals test for proportional hazards assumption on each covariate.
   - Martingale residuals for functional form of continuous covariates (assess non-linearity).
   - dfbeta residuals for influential observations.
   - Multicollinearity assessment (stage and risk group are partially deterministic of each other in INRG; risk group also incorporates MYCN, ploidy, and histology, creating embedded confounding).

3. **Presentation**: Forest plot with HR, 95% CI, and p-value per covariate. Report concordance index (C-index) for overall model discrimination. Include likelihood ratio test, Wald test, and score test global p-values.

4. **Sensitivity analyses**: Fit a reduced model excluding risk group (since it is a composite of several included covariates) to avoid collinearity; compare via AIC/BIC.

5. **Missing data handling**: Multiple imputation (MICE) if missingness in LDH/ferritin/NSE exceeds 5%; otherwise, complete-case analysis with sensitivity check.

### Biomedical Interpretation

This is the cornerstone analysis for identifying independent prognostic factors. In the INRG system, risk group is itself derived from stage, MYCN, ploidy, histology, and age — so including both risk group and its component variables in the same model introduces severe structural collinearity. The recommended approach is to run **two models**: (A) a clinical/molecular model without risk group, and (B) a model with risk group alone, then compare C-indices to assess whether the individual covariates provide prognostic discrimination beyond the composite classification. Serum biomarkers (LDH, ferritin, NSE) have historically shown prognostic value in univariate analyses but are variably independent in multivariate models; their role here will be informative for biomarker panel development (Objective 2.4).

---

## Objective 1.4
**Determine 3-year and 5-year OS and EFS rates per disease stage.**

### Current Pipeline Evidence

**Not directly addressed.** The pipeline provides KM curves by risk group but not by stage, and does not extract landmark survival probabilities at specific time points.

### Gaps & Recommended Analyses

1. Fit KM estimators separately for each INRG stage (1, 2A, 2B, 3, 4, 4S).
2. Extract survival probability estimates at t = 36 months and t = 60 months using the KM step function; compute 95% CIs via Greenwood's formula or log-log transformation.
3. Present results in a table:

| Stage | n | 3-yr EFS (95% CI) | 5-yr EFS (95% CI) | 3-yr OS (95% CI) | 5-yr OS (95% CI) |
|-------|---|--------------------|--------------------|-------------------|-------------------|
| 1     |   |                    |                    |                   |                   |
| …     |   |                    |                    |                   |                   |

4. Note: If maximum follow-up in a stage subgroup does not reach 60 months, the 5-year estimate will be unreliable (wide CI) or non-estimable. Report censoring proportions per stage.

5. Given cohort median EFS of 30.1 months, 5-year estimates for some subgroups (especially 4S, which tends to have small n) may be unstable.

### Biomedical Interpretation

Stage-specific survival rates are the fundamental benchmarking metric for neuroblastoma outcomes. Expected 5-year OS benchmarks from the literature: stage 1 > 95%, stage 2 ≈ 85–95%, stage 3 ≈ 60–75%, stage 4 ≈ 30–40% (pre-immunotherapy era), stage 4S ≈ 75–85%. Deviations from these benchmarks in this cohort should be interpreted in the context of treatment era, geographic/institutional factors, and potential selection bias. With 400 patients distributed across 6 stages, some stages (e.g., 2A, 2B, 4S) may have very small subgroups (n < 30), limiting precision.

---

## Objective 1.5
**Assess whether age at diagnosis (< 18 months vs. ≥ 18 months) is an independent prognostic factor for EFS.**

### Current Pipeline Evidence

The pipeline provides the clinical age distribution plot (`clinical_age_distribution.png`) showing the cohort's age profile, with a median of 30 months. However, no age-dichotomized survival analysis has been performed.

### Gaps & Recommended Analyses

1. **Dichotomize** age at 18 months (the clinically established INRG cutoff).
2. **Univariate analysis**: KM curves for EFS by age group (< 18 mo vs. ≥ 18 mo) with log-rank test.
3. **Multivariate analysis**: Cox PH regression for EFS with age group as the variable of interest, adjusting for stage, MYCN status, ploidy, and histology. The key test is whether the age group HR remains statistically significant after adjustment — this defines "independence."
4. **Alternative threshold**: Consider testing < 12 months as a secondary analysis (used in some INRG protocols for 4S staging).
5. **Continuous age**: Fit restricted cubic splines in a Cox model to assess non-linearity of the age-EFS relationship, which can reveal whether 18 months is indeed the optimal threshold in this dataset.

### Biomedical Interpretation

The 18-month age cutoff is a cornerstone of INRG risk stratification and has been validated across multiple large cohorts (COG, SIOPEN). Younger children (< 18 months) tend to have biologically favorable disease: near-triploid DNA content, favourable histology, high NTRK1 expression, and a propensity for spontaneous regression. In this cohort with a median age of 30 months, the majority of patients fall into the ≥ 18-month group, which may reflect enrichment for higher-risk disease (consistent with the cohort's 48.75% overall event rate and predominance of high-risk classification). Independence from MYCN status is critical, as MYCN amplification is enriched in older patients and may confound the age-EFS relationship.

---

## Objective 2.1
**Evaluate whether elevated LDH (above median) at diagnosis is associated with worse OS.**

### Current Pipeline Evidence

**Partially addressed.** The biomarker correlation heatmap (`biomarker_correlation_heatmap.png`) provides some information about inter-biomarker relationships, but no LDH-specific survival analysis has been conducted. LDH is listed as a variable in the dataset, and its correlation with EFS is not explicitly reported in the "Top Biomarker-EFS Associations" list, which focuses on gene expression features.

### Gaps & Recommended Analyses

1. **Compute median LDH** in the cohort; dichotomize patients into LDH-high (≥ median) and LDH-low (< median).
2. **KM analysis** for OS stratified by LDH group, with log-rank test.
3. **Cox univariate regression** for OS with LDH as a continuous variable (log-transformed due to expected right-skew) and as a binary variable (above/below median).
4. **Multivariate Cox regression** adjusting for stage, MYCN status, and risk group to assess whether LDH retains prognostic significance independently.
5. **Report**: HR with 95% CI, log-rank p-value, and KM plot with CI bands and number-at-risk table.
6. **Data quality**: Report missingness in LDH values. LDH is susceptible to hemolysis artifact; if outlier values exist (> 10× ULN), consider sensitivity analysis excluding them.

### Biomedical Interpretation

Serum LDH reflects tumor burden and cellular turnover and has been a prognostic marker in neuroblastoma since the 1980s. Elevated LDH is strongly associated with advanced stage, MYCN amplification, and unfavorable histology. Its independent contribution beyond these established prognosticators is the critical question. In many published multivariate models, LDH loses significance after adjustment for stage and MYCN, suggesting it is a surrogate rather than independent marker. This analysis will clarify its role in this specific cohort.

---

## Objective 2.2
**Correlate serum ferritin levels with disease stage and risk group.**

### Current Pipeline Evidence

**Not directly addressed.** Ferritin is available in the dataset but no ferritin-specific analyses are present in the pipeline outputs.

### Gaps & Recommended Analyses

1. **Descriptive statistics**: Report median, IQR, and range of serum ferritin per disease stage and per risk group.
2. **Visualization**: Boxplots or violin plots of ferritin distribution across stages and risk groups.
3. **Statistical tests**:
   - Kruskal-Wallis test for ferritin across stages (6 levels) and across risk groups (3 levels), given expected non-normality.
   - Post-hoc pairwise Mann-Whitney U tests with Holm correction.
4. **Correlation**: Spearman rank correlation between ferritin (continuous) and ordinal-encoded stage, and between ferritin and ordinal risk group.
5. **Clinical threshold analysis**: Additionally evaluate proportion of patients with ferritin > 142 ng/mL (a commonly used clinical threshold in neuroblastoma) per stage/risk group.

### Biomedical Interpretation

Elevated serum ferritin (> 142 ng/mL) at diagnosis is an established adverse prognostic marker in neuroblastoma, associated with advanced-stage disease, MYCN amplification, and high-risk classification. Ferritin reflects both tumor burden and systemic inflammatory response. A monotonic increase in median ferritin from stage 1 through stage 4 is expected. Stage 4S may show moderately elevated ferritin despite its generally favourable prognosis, which would be of interest for the 4S subgroup characterization (Objective 6.2).

---

## Objective 2.3
**Determine the optimal NSE cut-off for discriminating high-risk from non-high-risk patients (ROC/AUC analysis).**

### Current Pipeline Evidence

**Not addressed.** No ROC curve or AUC analysis for NSE is present in the pipeline outputs.

### Gaps & Recommended Analyses

1. **Binary outcome definition**: High-risk vs. non-high-risk (intermediate + low combined).
2. **ROC analysis**: Plot the receiver operating characteristic curve for NSE as a continuous predictor of high-risk classification.
3. **AUC**: Report with 95% CI (DeLong method or bootstrap, 2000 replicates).
4. **Optimal cut-off**: Determine via Youden index (maximizes sensitivity + specificity − 1). Also report cut-offs at fixed sensitivity ≥ 90% (clinically relevant for screening) and fixed specificity ≥ 90%.
5. **Report**: Sensitivity, specificity, PPV, NPV, and accuracy at the Youden-optimal cut-off.
6. **Visualization**: ROC curve with AUC annotation and the optimal operating point marked.
7. **Internal validation**: Bootstrap-corrected AUC to account for optimism.

### Biomedical Interpretation

NSE (neuron-specific enolase) is a glycolytic enzyme released by neuroblastoma cells and serves as a surrogate for tumor burden. Historically, an NSE threshold of 100 ng/mL has been used clinically. The ROC-derived optimal cutoff may differ from this historical threshold depending on assay calibration, cohort composition, and the specific outcome (high-risk classification vs. survival). An AUC > 0.75 would suggest clinically useful discrimination; AUC > 0.85 would be excellent. Given that high-risk classification is itself multi-factorial, NSE alone is unlikely to exceed AUC 0.85, but the analysis quantifies its standalone contribution.

---

## Objective 2.4
**Assess whether the combination of LDH + ferritin + NSE improves prognostic classification over any single marker alone.**

### Current Pipeline Evidence

**Not addressed.** The correlation heatmap suggests moderate inter-biomarker correlations (max ~0.29), implying that these biomarkers capture partially non-redundant information — a favourable prerequisite for additive prognostic value.

### Gaps & Recommended Analyses

1. **Outcome definition**: Use high-risk classification (binary) or, preferably, EFS event as the outcome for prognostic classification.
2. **Single-marker models**: Logistic regression with each biomarker individually as predictor. Report AUC for each.
3. **Combined model**: Logistic regression with LDH + ferritin + NSE (all log-transformed). Report AUC.
4. **Comparison**: DeLong test for pairwise AUC comparison between each single-marker model and the combined model.
5. **Net Reclassification Improvement (NRI)** and **Integrated Discrimination Improvement (IDI)** to quantify added value beyond AUC.
6. **Internal validation**: 10-fold CV or bootstrap-corrected AUC for the combined model to adjust for optimism.
7. **If predicting OS**: Use time-dependent AUC (Heagerty method) at 3 and 5 years.

### Biomedical Interpretation

The moderate inter-biomarker correlation (~0.29) observed in the heatmap is encouraging: it suggests that LDH (tumor turnover), ferritin (inflammation/burden), and NSE (neuronal tumor mass) capture distinct biological dimensions. If the combined model significantly outperforms each individual marker, this supports the development of a composite serum biomarker panel for risk stratification at diagnosis — a clinically actionable result with minimal additional cost, since all three markers are routinely measured.

---

## Objective 3.1
**Quantify the co-occurrence of MYCN amplification with del(1p), gain(17q), and 11q aberration.**

### Current Pipeline Evidence

**Not directly addressed.** The event rate heatmap (`survival_event_rate_heatmap.png`) cross-tabulates risk group and MYCN status but does not address specific cytogenetic co-occurrences.

### Gaps & Recommended Analyses

1. **Cross-tabulation**: 2×2 contingency tables for MYCN amplification × each of {del(1p), gain(17q), 11q aberration}.
2. **Frequencies**: Report counts and proportions of co-occurrence.
3. **Association tests**: Fisher's exact test or chi-squared test for each pair; report odds ratios with 95% CI.
4. **Multi-way analysis**: An UpSet plot or Venn diagram showing all 2^4 = 16 possible combinations of the four markers.
5. **Conditional probabilities**: P(del(1p) | MYCN-amp), P(gain(17q) | MYCN-amp), P(11q | MYCN-amp), and their complements.
6. **Visualisation**: Tiled heatmap or mosaic plot.

### Biomedical Interpretation

In neuroblastoma, MYCN amplification is known to co-occur strongly with del(1p36) (60–80% overlap) and gain(17q) (>80% overlap), while 11q aberration is typically **mutually exclusive** with MYCN amplification (occurring predominantly in MYCN-non-amplified high-risk disease). Confirming this pattern in the current cohort validates data quality and biological consistency. Deviation from these expected patterns would warrant investigation into staging accuracy or molecular assay methodology. The MYCN/11q mutual exclusivity is particularly important, as it defines two molecularly distinct high-risk subtypes with potentially different therapeutic vulnerabilities.

---

## Objective 3.2
**Determine whether segmental chromosomal aberrations (SCA) independently predict outcome when controlling for MYCN status.**

### Current Pipeline Evidence

**Not addressed.** SCA is listed as a dataset variable but appears in no pipeline analysis.

### Gaps & Recommended Analyses

1. **Univariate KM + log-rank**: EFS and OS stratified by SCA presence/absence.
2. **Stratified analysis**: KM curves for SCA within MYCN-amplified and MYCN-non-amplified subgroups separately.
3. **Multivariate Cox PH regression**: EFS and OS as outcomes, with SCA and MYCN as covariates. Test the MYCN × SCA interaction term.
4. **Extended model**: Add stage, ploidy, and age to assess whether SCA retains significance after full adjustment.
5. **Effect metric**: Report adjusted HR for SCA with 95% CI and p-value.

### Biomedical Interpretation

Segmental chromosomal aberrations (as opposed to whole-chromosome numerical changes) are increasingly recognized as a prognostic factor in neuroblastoma, particularly in the MYCN-non-amplified subset. SCAs — which include del(1p), gain(17q), and del(11q) — reflect genomic instability associated with aggressive tumor biology. The key question is whether the SCA binary variable provides prognostic information **beyond** MYCN status alone, especially for intermediate-risk patients where treatment de-escalation or intensification decisions hinge on molecular risk markers. The interaction term (MYCN × SCA) will reveal whether SCA's effect is uniform or restricted to non-amplified patients.

---

## Objective 3.3
**Compare EFS distributions across ploidy groups (diploid, near-triploid, hyperdiploid).**

### Current Pipeline Evidence

**Not addressed.** Ploidy is listed as a dataset variable but no ploidy-stratified survival analysis has been performed.

### Gaps & Recommended Analyses

1. **Group definition**: Verify ploidy encoding in the dataset (categorical or continuous DNA index). If continuous, dichotomize or trichotomize using standard thresholds (DI < 1.0 = hypodiploid/diploid; 1.0 ≤ DI < 1.5 = near-triploid; DI ≥ 1.5 = hyperdiploid). If already categorical, use as-is.
2. **KM curves**: EFS stratified by ploidy group, with log-rank test.
3. **Pairwise comparisons**: Log-rank with Holm correction for each pair.
4. **Cox univariate and multivariate regression**: Adjust for MYCN, stage, and age.
5. **Sample size check**: Report n per ploidy group; hyperdiploid neuroblastoma is rare and may have very small n.

### Biomedical Interpretation

Near-triploid (hyperdiploid) DNA content is a hallmark of favourable neuroblastoma biology, typically seen in infants with whole-chromosome gains and absence of segmental aberrations. Diploid tumors tend to carry segmental aberrations and have worse outcomes. The expected hierarchy is: near-triploid > hyperdiploid > diploid for EFS. However, ploidy's prognostic value is strongest in infants (< 18 months) and may be attenuated in older children with high-risk disease, underscoring the need for the multivariate adjustment.

---

## Objective 3.4
**Identify which combination of genomic markers (MYCN, del_1p, gain_17q, aberration_11q, ploidy) best stratifies patients into distinct survival clusters.**

### Current Pipeline Evidence

**Not addressed.** The event rate heatmap provides a two-way (risk × MYCN) view, but no multi-marker survival clustering has been performed.

### Gaps & Recommended Analyses

1. **Recursive partitioning**: Apply a survival tree (conditional inference tree or CART with EFS/OS as the endpoint) using MYCN, del(1p), gain(17q), 11q, and ploidy as candidate split variables. This will identify the hierarchically most discriminating markers.
2. **LASSO-penalized Cox regression**: Fit a Cox model with L1 penalty on all five genomic markers; the non-zero coefficients indicate the independently prognostic markers.
3. **Consensus clustering**: Use all five binary/categorical markers to cluster patients (k = 2 to 6), then compare cluster-specific KM curves. Optimal k selected by gap statistic or silhouette width.
4. **Model comparison**: Compare C-indices of models with different marker combinations using bootstrap-corrected estimates.
5. **Visualization**: Dendrogram or alluvial plot mapping genomic marker combinations to survival clusters and to established risk groups.

### Biomedical Interpretation

This objective seeks to derive a data-driven molecular risk stratification that may capture prognostic heterogeneity missed by the current INRG classification. The expected result is that MYCN amplification will emerge as the primary split, followed by 11q aberration and gain(17q) in MYCN-non-amplified patients, with del(1p) and ploidy providing further refinement. If the data-driven clusters align closely with existing risk groups, it validates the current system; if they diverge, it identifies potential refinement opportunities with direct translational implications.

---

## Objective 4.1
**Identify gene expression features significantly differentially expressed between MYCN-amplified and non-amplified tumors (t-test / Mann-Whitney, FDR-corrected).**

### Current Pipeline Evidence

**Partially addressed.** The `biomarker_expression_summary.png` provides overall expression distributions, and `biomarker_mycn_vs_alk.png` shows the bivariate relationship between MYCN and ALK expression. The pipeline report notes that expr_mycn has the strongest negative correlation with EFS (r = −0.306). However, no formal differential expression analysis between MYCN-amplified and non-amplified groups has been conducted.

### Gaps & Recommended Analyses

1. **Statistical test**: For each of the 24 profiled genes, perform a two-group comparison (MYCN-amp vs. non-amp):
   - **Shapiro-Wilk test** per group to assess normality.
   - If normal: Welch's t-test. If not: Mann-Whitney U test.
   - Alternatively, apply Mann-Whitney U uniformly for robustness.
2. **Multiple testing correction**: Apply Benjamini-Hochberg FDR correction across 24 tests. Report both raw p-values and q-values.
3. **Effect size**: Report median difference or fold-change (in log2 space, this is directly the difference in medians) and Cohen's d or rank-biserial correlation.
4. **Visualization**: Volcano plot (log2 fold-change vs. −log10 q-value) and a grouped boxplot/violin for the top differentially expressed genes.
5. **Expected findings**: MYCN, MDM2, CDK4, and CCND1 (all located on or co-amplified with chromosome 2p24) should be significantly upregulated in MYCN-amplified tumors. NTRK1 should be downregulated.

### Biomedical Interpretation

MYCN-amplified neuroblastoma represents a distinct transcriptional program characterized by upregulation of cell-cycle drivers (CDK4, CCND1, BIRC5) and downregulation of neuronal differentiation genes (NTRK1, CHGB). The 24-gene panel appears curated to capture this biology. FDR correction is essential despite the small number of tests (24), as the results will inform downstream model building (Objectives 4.5, 7.1). The expr_mycn correlation with EFS (r = −0.306) already hints at the expected relationship, but this conflates gene expression with amplification status and must be disentangled.

---

## Objective 4.2
**Determine whether high TERT expression is associated with shorter EFS independent of MYCN amplification.**

### Current Pipeline Evidence

**Partially addressed.** The pipeline generated `survival_km_median_split_tert.png`, which shows KM curves for EFS stratified by TERT expression (median split). The top biomarker-EFS correlations list expr_tert with r = −0.288, the second-strongest negative correlation. The insight notes visible curve separation, suggesting an association between high TERT expression and shorter EFS.

### Gaps & Recommended Analyses

1. **Univariate confirmation**: Log-rank test p-value for TERT median-split KM curves (this may already be on the plot but is not confirmed).
2. **Multivariate Cox model**: EFS ~ TERT (continuous or binary) + MYCN amplification status. The key result is the adjusted HR for TERT after controlling for MYCN.
3. **Interaction test**: TERT × MYCN interaction term to determine whether TERT's prognostic effect is confined to MYCN-non-amplified patients (biologically plausible, as TERT upregulation via rearrangement is an alternative telomere maintenance mechanism to MYCN-driven telomerase activation).
4. **Stratified KM**: KM curves for TERT-high vs. TERT-low within MYCN-non-amplified patients only.
5. **Extended multivariate model**: Add stage, age, and ploidy to confirm independence.

### Biomedical Interpretation

TERT (telomerase reverse transcriptase) expression is a critical prognostic marker in neuroblastoma. TERT rearrangements have been identified as a mechanism of telomere maintenance in MYCN-non-amplified high-risk neuroblastoma, making TERT expression a potential marker for this specific adverse subgroup. The observed r = −0.288 with EFS is notable. The critical clinical question is whether TERT adds prognostic information beyond MYCN, which would support its inclusion in risk stratification algorithms and potentially identify patients for TERT-targeted therapeutic strategies. The interaction analysis is essential: if TERT's effect is entirely within MYCN-non-amplified disease, this defines a biologically distinct high-risk subtype.

---

## Objective 4.3
**Correlate NTRK1 and NTRK2 expression levels with histological classification (favorable vs. unfavorable) and with EFS.**

### Current Pipeline Evidence

**Not addressed.** NTRK1 and NTRK2 are available in the expression data but no specific analyses have been performed.

### Gaps & Recommended Analyses

1. **NTRK1/NTRK2 vs. histology**:
   - Boxplots/violins of NTRK1 and NTRK2 expression stratified by histological classification.
   - Mann-Whitney U test for each gene between favorable and unfavorable histology.
   - Report effect sizes (rank-biserial correlation or Cohen's d).

2. **NTRK1/NTRK2 vs. EFS**:
   - Spearman correlation of each with EFS.
   - KM curves for EFS stratified by median-split NTRK1 and NTRK2, with log-rank tests.
   - Cox univariate and multivariate (adjusting for MYCN and stage) models.

3. **NTRK1/NTRK2 ratio**: Consider computing the NTRK1/NTRK2 ratio (in log2 space: difference), as this ratio has been shown to have prognostic significance, with high NTRK1/low NTRK2 being favorable.

### Biomedical Interpretation

NTRK1 (TrkA) expression is a well-established marker of favorable neuroblastoma biology, associated with differentiation potential and favourable histology. Conversely, NTRK2 (TrkB) co-expression with its ligand BDNF is associated with aggressive, MYCN-amplified disease and resistance to apoptosis. A strong positive association between NTRK1 and favourable histology (and EFS), with an inverse pattern for NTRK2, is expected. These genes are also therapeutic targets: larotrectinib and entrectinib are approved for NTRK-fusion–positive tumors, making the expression characterization clinically relevant.

---

## Objective 4.4
**Assess whether ATRX expression differs significantly across ploidy groups.**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Descriptive statistics**: Median and IQR of ATRX expression per ploidy group.
2. **Visualization**: Boxplot or violin plot of ATRX by ploidy group.
3. **Statistical test**: Kruskal-Wallis test across ploidy groups; if significant, post-hoc pairwise Mann-Whitney U tests with Holm correction.
4. **Sample size**: Verify adequate n per ploidy group (especially hyperdiploid, which may be rare).

### Biomedical Interpretation

ATRX loss-of-function mutations are a hallmark of the alternative lengthening of telomeres (ALT) pathway, found predominantly in older children with MYCN-non-amplified, diploid neuroblastoma. If diploid tumors show significantly lower ATRX expression than near-triploid tumors, this would be consistent with the known biology of ALT-positive neuroblastoma and may indicate that ATRX expression can serve as a proxy for ALT status in the absence of direct ALT assays. This has implications for prognosis (ALT-positive tumors have poor outcomes) and for therapeutic targeting.

---

## Objective 4.5
**Build a gene expression signature (from the 24 genes) that predicts treatment response category (CR/PR vs. MR/NR/PD) using logistic regression or random forest.**

### Current Pipeline Evidence

**Not addressed.** No predictive model for treatment response has been built.

### Gaps & Recommended Analyses

1. **Outcome definition**: Binary — favorable response (CR + PR) vs. unfavorable response (MR + NR + PD).
2. **Feature set**: 24 gene expression features (log2 values).
3. **Modeling approaches**:
   - **Logistic regression with elastic net penalty** (glmnet): Handles collinearity and performs variable selection. Tune λ and α via 10-fold CV.
   - **Random forest**: 500+ trees, tune mtry via OOB error. Extract variable importance (Gini or permutation-based).
4. **Evaluation**: 10-fold stratified CV. Report AUC, accuracy, sensitivity, specificity, F1 score. Generate confusion matrix and ROC curve.
5. **Comparison**: Compare logistic regression and random forest performance.
6. **Class imbalance**: If response categories are imbalanced, apply SMOTE or class weighting.
7. **Feature importance**: Report the top 5–10 genes by importance in both models.
8. **Confounding**: Response is heavily influenced by treatment modality (observation patients cannot achieve CR to chemotherapy). Stratify by treatment or include treatment as a covariate.

### Biomedical Interpretation

Predicting treatment response from pre-treatment gene expression is a high-value translational objective. However, the response variable is treatment-dependent — patients on observation follow a different trajectory than those on induction chemotherapy. The model must either stratify by treatment modality or include it as a covariate. Expected informative genes include BIRC5 (survivin, associated with chemoresistance), MYCN (associated with aggressive disease and variable response), and VEGF/HIF1A (angiogenesis pathway, relevant to treatment resistance).

---

## Objective 4.6
**Cluster patients by gene expression profile (unsupervised hierarchical clustering or k-means) and test whether the resulting clusters align with established risk groups.**

### Current Pipeline Evidence

**Not addressed.** The biomarker correlation heatmap exists but does not cluster patients.

### Gaps & Recommended Analyses

1. **Data preparation**: Z-score normalize all 24 gene expression variables across patients.
2. **Unsupervised clustering**:
   - **Hierarchical clustering**: Ward's method with Euclidean distance. Produce a dendrogram with clinical annotation sidebars (risk group, MYCN status, stage, histology).
   - **k-means**: Test k = 2 to 6. Select optimal k by silhouette width, gap statistic, and within-cluster sum of squares (elbow method).
   - **Consensus clustering** (e.g., ConsensusClusterPlus in R): For robustness assessment.
3. **Cluster-risk alignment**: Chi-squared test or Fisher's exact test comparing cluster assignments to risk group. Report Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI) as quantitative alignment metrics.
4. **Survival validation**: KM curves for EFS/OS stratified by expression-defined clusters.
5. **Visualization**: Heatmap with dual annotation bars (expression clusters + risk group), as specified in the suggested outputs.

### Biomedical Interpretation

If unsupervised expression clusters recapitulate risk groups, it validates the biological basis of the clinical classification. If they identify substructure within risk groups — e.g., two distinct expression subtypes within high-risk — this would be a novel and potentially clinically important finding. Prior studies (e.g., Oberthuer et al., Asgharzadeh et al.) have demonstrated that gene expression profiling can identify prognostic subtypes beyond established classifications. The 24-gene panel used here, while not genome-wide, captures key biological axes (differentiation, cell cycle, telomere maintenance, angiogenesis).

---

## Objective 5.1
**Identify pre-treatment clinical and molecular variables that are the strongest predictors of complete response (CR).**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Outcome**: Binary — CR vs. non-CR.
2. **Candidate predictors**: Stage, risk group, MYCN, ploidy, histology, del(1p), gain(17q), 11q, SCA, LDH, ferritin, NSE, age, sex.
3. **Univariate screening**: Logistic regression or chi-squared/Mann-Whitney for each predictor. Report OR with 95% CI.
4. **Multivariate logistic regression**: Include predictors significant at p < 0.10 in univariate analysis. Use stepwise (AIC-based) or LASSO for variable selection.
5. **Performance**: AUC, calibration plot (Hosmer-Lemeshow), confusion matrix.
6. **Confounding**: Treatment modality strongly determines the possibility of CR. Analysis must be stratified by treatment or restricted to patients receiving induction chemotherapy.
7. **Random forest or gradient boosting**: As secondary analysis, for variable importance ranking without linearity assumptions.

### Biomedical Interpretation

CR to induction chemotherapy is a strong surrogate for long-term survival in high-risk neuroblastoma. Pre-treatment predictors of CR can guide treatment intensification decisions. Expected strong predictors include MYCN amplification (negative), favorable histology (positive), lower stage (positive), and lower serum biomarkers. The analysis must account for treatment selection bias: observation patients and surgery-only patients are fundamentally different populations.

---

## Objective 5.2
**Compare response rates (CR vs. non-CR) between treatment modalities (observation, induction chemotherapy, surgery only).**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Contingency table**: Treatment modality × response (CR vs. non-CR). Report counts and proportions.
2. **Statistical test**: Chi-squared test or Fisher's exact test. Report p-value and Cramér's V.
3. **Important caveat**: This is a **non-randomized comparison**. Patients assigned to observation vs. chemotherapy vs. surgery differ systematically in disease characteristics (stage, risk group, MYCN status). Any difference in CR rates reflects both treatment effect and selection bias.
4. **Adjusted analysis**: Logistic regression for CR with treatment modality and confounders (stage, risk, MYCN) as covariates. Alternatively, propensity score–weighted analysis.
5. **Response definition**: "CR" may have different clinical meaning across modalities (e.g., spontaneous regression in observation patients vs. chemotherapy-induced CR). Define clearly.

### Biomedical Interpretation

Observation is typically reserved for low-risk patients (stage 1/2, favorable biology) who are expected to do well regardless. Surgery only applies to localized disease. Induction chemotherapy is given to intermediate and high-risk patients. Comparing CR rates across these groups without adjustment is misleading and constitutes a form of confounding by indication. The adjusted analysis is essential for any meaningful interpretation.

---

## Objective 5.3
**Determine whether gene expression of VEGF and HIF1A predicts response to induction chemotherapy.**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Restrict cohort** to patients who received induction chemotherapy.
2. **Outcome**: Binary — favorable response (CR/PR) vs. unfavorable (MR/NR/PD), or CR vs. non-CR.
3. **Univariate analysis**: Mann-Whitney U test for VEGF and HIF1A expression between responders and non-responders. Boxplot visualization.
4. **Logistic regression**: VEGF and HIF1A (individually and combined) as predictors of response. Report OR, 95% CI, p-value.
5. **Adjusted model**: Add MYCN, stage, and risk group as confounders.
6. **ROC/AUC**: For VEGF, HIF1A, and their combination.
7. **Biological interaction**: Test VEGF × HIF1A interaction (HIF1A is a transcriptional activator of VEGF, so collinearity is expected).

### Biomedical Interpretation

VEGF and HIF1A represent the hypoxia-angiogenesis axis, which is implicated in chemoresistance in many solid tumors. In neuroblastoma, tumor hypoxia drives a stem-like phenotype with reduced chemosensitivity. If high VEGF/HIF1A expression predicts poor response to induction chemotherapy, this supports the rationale for anti-angiogenic combination strategies (e.g., bevacizumab) in high-expressing patients. The expected collinearity between VEGF and HIF1A (HIF1A transcriptionally regulates VEGF) should be assessed and managed in the multivariate model.

---

## Objective 5.4
**Build a multivariate model to predict progressive disease (PD) as an outcome; report sensitivity, specificity, and AUC.**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Outcome**: Binary — PD vs. non-PD (all other response categories).
2. **Candidate predictors**: All pre-treatment clinical, molecular, and gene expression variables.
3. **Class imbalance**: PD is likely a rare outcome; report class distribution. If severely imbalanced (< 10% PD), use SMOTE, class weighting, or penalized likelihood.
4. **Model**: Logistic regression (LASSO-penalized) and/or random forest.
5. **Evaluation**: 10-fold stratified CV. Report:
   - AUC with 95% CI (bootstrap).
   - Sensitivity, specificity at optimal threshold (Youden index).
   - PPV, NPV.
   - Calibration (Hosmer-Lemeshow).
   - Confusion matrix.
6. **ROC curve**: Plot and annotate with AUC.
7. **Clinical utility**: Decision curve analysis (DCA) to assess net benefit at various threshold probabilities.

### Biomedical Interpretation

Predicting progressive disease (PD) at diagnosis has high clinical value, as PD patients represent treatment failures who may benefit from upfront alternative strategies (experimental agents, targeted therapy, intensified immunotherapy). Given the likely low prevalence of PD (perhaps 5–15% of the cohort), the model must be evaluated with attention to both sensitivity (identify PD patients) and PPV (avoid over-treatment of non-PD patients). The specificity-sensitivity trade-off will be guided by the clinical context: in a screening tool, high sensitivity is prioritized; in a treatment-intensification decision, high PPV may be preferred.

---

## Objective 6.1
**Compare OS between male and female patients within each risk group.**

### Current Pipeline Evidence

**Not addressed.**

### Gaps & Recommended Analyses

1. **Stratified KM curves**: For each risk group (low, intermediate, high), generate KM curves for OS stratified by sex.
2. **Log-rank tests**: Within each risk group (3 tests total).
3. **Multiple testing correction**: Bonferroni or Holm across the 3 comparisons.
4. **Cox regression**: OS ~ sex + risk group + sex × risk group interaction. The interaction term tests whether the sex effect varies across risk groups.
5. **Sample size**: Report n per sex per risk group; some cells may be underpowered.

### Biomedical Interpretation

Sex-based differences in neuroblastoma outcome are generally considered modest. Some studies have reported a slight female advantage in survival, potentially related to hormonal or immune factors, but this is not consistently observed. Within-risk-group comparisons are appropriate, as confounding by risk distribution between sexes would otherwise distort the result. A significant sex × risk interaction would be novel and hypothesis-generating.

---

## Objective 6.2
**Characterise the stage 4S subgroup: distribution of molecular markers, response rates, and OS vs. other stage 4 patients.**

### Current Pipeline Evidence

The clinical stage distribution plot (`clinical_stage_distribution.png`) shows the frequency of each stage but does not specifically characterize 4S.

### Gaps & Recommended Analyses

1. **Descriptive profile of 4S patients**: n, age distribution, sex, MYCN amplification rate, ploidy, del(1p), gain(17q), 11q, SCA, histology, LDH, ferritin, NSE, treatment modality.
2. **Comparison with stage 4**: Chi-squared / Fisher's exact for categorical and Mann-Whitney U for continuous variables, comparing 4S vs. 4.
3. **Response rates**: Tabulate treatment responses for 4S patients. Note that many 4S patients are observed, so response categories may differ.
4. **OS comparison**: KM curves for OS in 4S vs. stage 4, with log-rank test.
5. **Within-4S prognostic factors**: If n is sufficient (typically 4S = 5–10% of cohort, so ~20–40 patients), identify adverse features within 4S (MYCN amplification, unfavorable histology, diploid ploidy, high LDH).

### Biomedical Interpretation

Stage 4S (special) neuroblastoma is defined by age < 12 months (or < 18 months in revised criteria), localized primary tumor, and metastases limited to skin, liver, and/or bone marrow (< 10%). It is biologically distinct from stage 4, with a high rate of spontaneous regression and excellent prognosis (5-year OS > 80%) in the absence of unfavorable features. MYCN amplification in 4S is rare but, when present, confers a significantly worse prognosis. Characterizing this subgroup is essential for validating the cohort's consistency with known neuroblastoma biology.

---

## Objective 6.3
**Assess whether weight at diagnosis correlates with any clinical or molecular variable.**

### Current Pipeline Evidence

**Not addressed.** Weight is listed as a dataset variable but has not been analyzed.

### Gaps & Recommended Analyses

1. **Descriptive statistics**: Median, IQR, range of weight. Scatterplot of weight vs. age (to distinguish weight as a nutritional variable from an age surrogate).
2. **Age-adjusted analysis**: Since weight is strongly collinear with age, compute weight-for-age z-scores (WHO growth standards) if possible, or use residuals from a weight ~ age regression.
3. **Correlations**:
   - Spearman correlations of weight (or weight-for-age z-score) with: LDH, ferritin, NSE, EFS, OS.
   - Mann-Whitney U tests for weight across: MYCN status, ploidy, histology, risk group, sex.
   - Kruskal-Wallis for weight across stage.
4. **Multiple testing correction**: FDR across all tests.
5. **Caution**: Confounding by age is the primary concern. Any weight-outcome association that disappears after age adjustment is age-driven, not nutrition-driven.

### Biomedical Interpretation

Weight at diagnosis in young children is predominantly determined by age, not nutritional status per se. Neuroblastoma patients may have weight loss from advanced disease (cachexia) or abdominal distension from tumor mass, complicating interpretation. Without age-standardization, any observed correlations are likely spurious. The weight-for-age z-score approach is strongly recommended. If low weight-for-age is associated with adverse molecular features or outcomes after age adjustment, this could reflect tumor-related catabolism and would be a clinically relevant finding.

---

## Objective 7.1
**Construct a composite prognostic score integrating clinical (stage, age), molecular (MYCN, SCA, ploidy), and gene expression features; validate using leave-one-out cross-validation.**

### Current Pipeline Evidence

**Not addressed.** This is a complex modeling task requiring full de novo development.

### Gaps & Recommended Analyses

1. **Outcome**: 5-year OS (binary, event within 60 months) or time-to-event (Cox-based score).
2. **Feature set**:
   - Clinical: stage (categorical, dummy-coded), age (continuous or binary at 18 months).
   - Molecular: MYCN (binary), SCA (binary), ploidy (categorical).
   - Gene expression: 24 genes (log2). Use LASSO pre-selection to reduce dimensionality.
3. **Modeling approaches**:
   - **LASSO-penalized Cox regression**: Select features and derive a linear prognostic index (PI).
   - **Random survival forest**: As comparison for non-linear relationships.
4. **Score construction**: Linear predictor from the penalized Cox model, or the ensemble-based risk score from the survival forest.
5. **LOOCV**: For each of 400 patients, fit the model on 399, predict the held-out patient. Compile predictions.
6. **Evaluation from LOOCV**:
   - C-index (Harrell's) from the cross-validated predictions.
   - Time-dependent AUC at 3 and 5 years.
   - Calibration plot (predicted vs. observed survival).
7. **Score categorization**: Divide the continuous score into tertiles or quartiles; generate KM curves for the resulting risk strata.
8. **Computational note**: LOOCV with 400 patients is computationally feasible but requires 400 model fits. 10-fold CV with multiple repeats (e.g., 5 × 10-fold) is a reasonable alternative with lower variance.

### Biomedical Interpretation

An integrated prognostic score combining clinical, molecular, and transcriptomic features represents the logical extension of the INRG framework. The value proposition is clear: if gene expression features (e.g., TERT, NTRK1, BIRC5) add discriminative power beyond established clinical and molecular markers, this justifies the cost and complexity of expression profiling in clinical practice. The LOOCV design provides an honest (though potentially high-variance) estimate of out-of-sample performance. The resulting score should be interpretable: a linear combination from LASSO Cox is preferred over a black-box model for clinical adoption.

---

## Objective 7.2
**Compare the discriminative power (C-index) of the new composite score vs. the current INRG risk classification for predicting 5-year OS.**

### Current Pipeline Evidence

**Not addressed.** Requires the composite score from Objective 7.1.

### Gaps & Recommended Analyses

1. **INRG baseline model**: Fit a Cox model with only risk group (low/intermediate/high) as a factor variable. Compute C-index.
2. **Composite model**: Compute C-index from the LOOCV predictions of Objective 7.1.
3. **Comparison**:
   - **C-index difference** with 95% CI (bootstrap, 2000 replicates). Test H0: ΔC = 0.
   - **Likelihood ratio test**: Nested model comparison if the composite model includes risk group.
   - **Net Reclassification Improvement (NRI)** at clinically meaningful risk thresholds (e.g., 20%, 50%, 80% 5-year event risk).
   - **Integrated Discrimination Improvement (IDI)**.
4. **Time-dependent AUC comparison**: At τ = 60 months (5-year OS).
5. **Clinical calibration**: Compare calibration of both models (predicted vs. observed 5-year OS).

### Biomedical Interpretation

The INRG risk classification is the current clinical standard, achieving C-indices of approximately 0.75–0.80 for OS prediction in large validation cohorts. A composite score incorporating gene expression would need to demonstrate a statistically significant and clinically meaningful improvement (ΔC-index ≥ 0.03–0.05 is often considered meaningful) to justify clinical adoption. The NRI is arguably more clinically interpretable than the C-index: it quantifies how many patients are correctly reclassified upward (into higher risk) or downward (into lower risk) by the new score. If the improvement is concentrated in the intermediate-risk group — where clinical decision-making is most uncertain — this would be the strongest argument for clinical utility.

---

## Summary Table

| Objective | Status | Key Method(s) Needed |
|-----------|--------|---------------------|
| **O1.1** | Partially Addressed | KM with log-rank, CI bands, number-at-risk table; OS KM still needed |
| **O1.2** | Partially Addressed | Formal log-rank test + univariate Cox HR for both EFS and OS |
| **O1.3** | Not Yet Addressed | Multivariate Cox PH regression with PH diagnostics, forest plot |
| **O1.4** | Not Yet Addressed | Stage-stratified KM with landmark survival extraction at 36 & 60 months |
| **O1.5** | Not Yet Addressed | Age-dichotomized KM + multivariate Cox for EFS |
| **O2.1** | Not Yet Addressed | LDH-stratified KM for OS + Cox regression |
| **O2.2** | Not Yet Addressed | Ferritin descriptive stats + Kruskal-Wallis across stage/risk |
| **O2.3** | Not Yet Addressed | ROC/AUC analysis for NSE; Youden-optimal cut-off |
| **O2.4** | Not Yet Addressed | Multi-marker logistic regression; AUC comparison (DeLong test) |
| **O3.1** | Not Yet Addressed | Cross-tabulation + Fisher's exact test; UpSet/Venn diagram |
| **O3.2** | Not Yet Addressed | Stratified KM + Cox with SCA × MYCN interaction |
| **O3.3** | Not Yet Addressed | Ploidy-stratified KM + Kruskal-Wallis / log-rank |
| **O3.4** | Not Yet Addressed | Survival tree / LASSO-Cox / consensus clustering |
| **O4.1** | Not Yet Addressed | Mann-Whitney U across 24 genes, BH-FDR correction, volcano plot |
| **O4.2** | Partially Addressed | Multivariate Cox for EFS: TERT + MYCN + interaction term |
| **O4.3** | Not Yet Addressed | NTRK1/NTRK2 vs. histology (Mann-Whitney) + vs. EFS (Cox) |
| **O4.4** | Not Yet Addressed | ATRX expression across ploidy groups (Kruskal-Wallis) |
| **O4.5** | Not Yet Addressed | Penalized logistic regression / random forest; 10-fold CV |
| **O4.6** | Not Yet Addressed | Hierarchical / k-means clustering + ARI alignment with risk groups |
| **O5.1** | Not Yet Addressed | Univariate screening + multivariate logistic regression for CR |
| **O5.2** | Not Yet Addressed | Chi-squared / Fisher's exact; propensity-adjusted analysis |
| **O5.3** | Not Yet Addressed | VEGF/HIF1A vs. chemo response in treated subset; logistic regression |
| **O5.4** | Not Yet Addressed | LASSO logistic / random forest for PD; AUC, sensitivity, specificity |
| **O6.1** | Not Yet Addressed | Sex-stratified KM within risk groups; Cox interaction model |
| **O6.2** | Partially Addressed | 4S molecular/clinical profile; 4S vs. 4 KM comparison |
| **O6.3** | Not Yet Addressed | Weight-for-age z-scores; Spearman correlations with adjustment |
| **O7.1** | Not Yet Addressed | LASSO-Cox composite score; LOOCV; C-index + calibration |
| **O7.2** | Not Yet Addressed | C-index comparison (bootstrap); NRI/IDI vs. INRG classification |

---

### Overall Assessment

The current pipeline has successfully executed **exploratory data characterization** (cohort demographics, stage/risk distributions, gene expression summaries) and generated **preliminary survival visualizations** (KM curves by risk group, MYCN status, and median-split TERT/CHGB). These address the descriptive foundation of the study. However, the vast majority of the 29 research objectives — particularly those requiring formal statistical testing, multivariate modeling, predictive classification, and integrated scoring — remain unaddressed and require dedicated analytical implementation. The pipeline has, importantly, validated the data structure and identified no apparent data quality issues (0 missing cells reported), which is an encouraging foundation for the remaining analyses. Priority should be given to the Cox multivariate model (O1.3), the differential expression analysis (O4.1), and the composite score development (O7.1/7.2), as these are the highest-impact deliverables and inform multiple downstream objectives.