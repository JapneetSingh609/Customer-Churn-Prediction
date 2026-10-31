# Evaluation evidence and metric interpretation

All counts and report values come from
[the saved notebook](../customer_churn_prediction.ipynb), not a new experiment.
The [evidence map](evidence.md#evidence-map) identifies the source cells.

## Confusion matrix orientation

The notebook calls `confusion_matrix(y_test, y_pred)` and
`ConfusionMatrixDisplay.from_predictions(y_test, y_pred)` without custom label
ordering. Both saved images show labels `0`, `1`, with true classes on rows
and predicted classes on columns.

| Actual / predicted | 0 — stays | 1 — churns | Actual support |
|---|---:|---:|---:|
| 0 — stays | 5,655 (TN) | 1,138 (FP) | 6,793 |
| 1 — churns | 1,030 (FN) | 5,052 (TP) | 6,082 |
| Predicted total | 6,685 | 6,190 | 12,875 |

Positive means **churn** throughout this document. A false positive consumes
potential retention attention on a customer labeled as staying; a false
negative misses a customer labeled as churning. The data does not establish
the financial cost of either error.

## Arithmetic from the saved counts

The extra digits below are **derived from the matrix**, not additional saved
precision or a new prediction run.

| Measure | Calculation | Derived value | Saved display |
|---|---|---:|---:|
| Accuracy | `(5655 + 5052) / 12875` | 0.831612 | 83.16% in accuracy cell |
| Churn precision | `5052 / (5052 + 1138)` | 0.816155 | 0.82 |
| Churn recall | `5052 / (5052 + 1030)` | 0.830648 | 0.83 |
| Churn F1 | `2*5052 / (2*5052 + 1138 + 1030)` | 0.823338 | 0.82 |
| Stay precision | `5655 / (5655 + 1030)` | 0.845924 | 0.85 |
| Stay recall | `5655 / (5655 + 1138)` | 0.832475 | 0.83 |
| Stay F1 | `2*5655 / (2*5655 + 1030 + 1138)` | 0.839145 | 0.84 |

The printed classification report rounds accuracy to `0.83`, while the
separate accuracy cell formats it as `83.16%`. Those displays are consistent.

## Averaging is part of the metric definition

- **Per-class:** treat the specified class as positive. Churn precision answers
  how many predicted churn cases are actually class 1.
- **Macro average:** calculate the metric for each class, then take an
  unweighted mean. Each class has equal influence regardless of support.
- **Weighted average:** average the per-class metrics with weights 6,793 and
  6,082. Each class's influence follows its actual holdout count.
- **F1:** the harmonic mean of precision and recall. Averaged F1 is an average
  of per-class F1 values, not generally F1 recomputed from averaged precision
  and recall.

The saved macro and weighted precision, recall, and F1 all display as `0.83`.
Their equality after rounding does not prove equal error costs, fairness,
robustness, or that each class has precision and F1 of 0.83.

## Scope of the result

This is one shuffled, non-stratified split with seed 42. There are no saved
cross-validation folds, confidence intervals, probability outputs, threshold
sweeps, subgroup scores, or external validation results. ROC-AUC and PR-AUC
cannot be reconstructed from this single confusion matrix. There is also no
measured retention intervention or business return.

The chart in [Images/confusion_matrix.png](../Images/confusion_matrix.png) and
the notebook's embedded plot were visually inspected; their counts agree.
Neither image was regenerated or modified.

[Return to model evaluation](../README.md#09-model-evaluation)
