# Reliability and leakage review

This review describes the current experiment; it does not certify a production
system or report newly performed checks. Its evidence is the unchanged
[notebook](../customer_churn_prediction.ipynb) and
[Python export](../customer_churn_prediction.py).

## Implemented boundaries

The target `Churn` and identifier `CustomerID` are excluded from `X` before
splitting. After `train_test_split`, categorical columns are selected from
`X_train`. The column transformer fits on training data and transforms the test
partition. The scaler then fits on transformed training data and transforms
the encoded test data. The classifier fits with `y_train`; `y_test` is used
for the confusion matrix and reported metrics.

These calls keep test observations out of the learned category vocabulary and
scaling statistics. Dropping an identifier is sensible, but does not prove
that every remaining predictor is appropriate or available at prediction time.

## Inspection before the split

`df.info()`, `df.describe()`, null counts, and dtypes inspect the entire input
before the split. These descriptive calls do not fit the encoder, scaler, or
classifier. They do expose information about the future holdout. The saved
workflow contains no evidence that this information was used for iterative
selection, but it also does not record an experiment history proving that the
holdout was never reused.

A careful claim is therefore **training-only fitted transformations**, rather
than “the test set was never inspected” or “the workflow has no leakage.”

## Unchecked risks and missing evidence

| Question | Current evidence | Evidence needed for stronger assurance |
|---|---|---|
| Were predictors known before churn? | Field names only; no measurement windows | Data dictionary with observation cutoff and label horizon |
| Can related rows cross the split? | Random row split; no duplicate/group audit | Entity identifiers, duplicate review, group-aware split where appropriate |
| Does the split reflect future use? | Shuffled 80/20 split; no timestamps evaluated | Time-aware external validation for a defined deployment setting |
| How variable is performance? | One seed and one holdout | Repeated/stratified cross-validation, with transforms fitted within folds |
| Are categories stable? | Default encoder; historical test transform succeeded | Category drift review and an explicitly chosen unseen-category policy |
| Are probabilities reliable? | Only hard predictions evaluated | Probability capture, calibration analysis, and held-out threshold assessment |
| Are errors consistent across customers? | Only overall and per-label metrics | Subgroup error analysis, including the use of `Age` and `Gender` |
| Can the exact run be restored? | Seed 42; Python 3.11.9 metadata | Original CSV identity, full dependency versions, parameters, and environment |

These are potential failure modes and evidence gaps. The notebook does not
demonstrate that duplicate leakage, temporal leakage, unfairness, or category
drift actually occurred.

## Evaluation and business limits

The saved matrix contains 1,138 false positives and 1,030 false negatives.
Selecting a retention workflow would require an explicit review budget and
error-cost assumptions. None is supplied, so neither the default classification
decision nor 83.16% accuracy establishes the best operating point.

No intervention study measures incremental retention, customer response, or
financial impact. Likewise, a classifier's association with churn does not
establish why customers leave or whether changing a feature changes that
outcome.

## Engineering limits

There is no saved fitted encoder, scaler, estimator, or reusable inference
pipeline. There is no API, deployment configuration, monitoring, schema
validation, model comparison, or cross-validation implementation. The script
trains each time it runs. Unpinned dependencies and the saved pandas warning
introduce compatibility uncertainty even before performance is considered.

See [reproduction](reproduction.md) for environment limits and
[evaluation](evaluation.md) for the metric evidence. Addressing the gaps above
requires separately planned implementation and experiments; it was outside
this documentation-only sprint.

[Return to reliability and data leakage](../README.md#12-reliability-and-data-leakage)
