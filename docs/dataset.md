# Dataset acquisition and verification

## What is established

Both [the notebook](../customer_churn_prediction.ipynb) and
[the Python export](../customer_churn_prediction.py) load exactly
`customer_churn_dataset-testing-master.csv` with `pd.read_csv` and no path
prefix. Python resolves this relative to the process's working directory.

The repository contains no CSV, automatic downloader, checksum, original
download URL, dataset version, or dataset-specific license. The notebook's
saved inspection, rather than a newly inspected CSV, establishes the schema
and dimensions described here.

| Saved property | Expected observation |
|---|---|
| Record count | 64,374 |
| Column count | 12 |
| Numeric source columns | 9, including identifier and target |
| Text source columns | `Gender`, `Subscription Type`, `Contract Length` |
| Missing entries | Zero in every column |
| Target minimum / maximum | 0 / 1 |
| Target mean | 0.473685, rounded in `describe()` |

For a binary target, the saved mean implies approximately 47.37% class 1 and
52.63% class 0 in the complete input. Holdout support is separately recorded as
6,082 class-1 and 6,793 class-0 observations. Do not substitute the holdout
distribution for the full-input distribution.

## Candidate source and provenance gap

A likely catalog match is the
[Customer Churn Dataset by Muhammad Shahid Azeem on Kaggle](https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset).
The catalog association is an inference, not an original citation recovered
from the project. The catalog's client-rendered details were not retrievable
through the documentation review's web reader. No downloaded file was
compared with the historical experiment.

Consequently, the original provider, collection process, real/synthetic status,
observation period, churn definition/horizon, feature units, and data license
remain unverified. The repository's [MIT license](../LICENSE) does not resolve
those dataset questions.

## Supply the input without changing the implementation

1. Locate the candidate catalog and inspect its owner, file listing, version,
   documentation, and applicable terms. Download through the provider's normal
   interface if the intended file is available.
2. Select the file named `customer_churn_dataset-testing-master.csv`. The
   implementation does not combine separate upstream training and testing
   files. A similarly named larger training file is not an equivalent input.
3. Put the CSV alongside the root-level notebook and Python file. Keep the
   exact spelling and extension, including the hyphen in `testing-master`.
4. Inspect its header, dimensions, null counts, and target coding against the
   saved observations above before executing any ML cells. Matching summaries
   alone cannot establish byte identity.
5. Record the actual source URL, download date, catalog version, SHA-256,
   applicable data license, and any discrepancies for a future reproducibility
   record. No historical checksum exists for comparison today.

Expected columns in source order:

```text
CustomerID, Age, Gender, Tenure, Usage Frequency, Support Calls,
Payment Delay, Subscription Type, Contract Length, Total Spend,
Last Interaction, Churn
```

Do not rename a different dataset to make it appear equivalent. Missing values,
new categories, or changed schema need investigation; the current workflow
contains no imputer or input validation layer. Keep externally acquired data
out of documentation commits.

## Limits on interpretation

The feature names suggest customer activity and subscription records. They do
not establish when a feature was measured relative to churn. Claims about
predicting *future* churn require an explicit observation window, prediction
horizon, and availability check for each feature. The current notebook does
not provide these.

[Return to the dataset overview](../README.md#03-dataset-intelligence)
