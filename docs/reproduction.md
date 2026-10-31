# Environment setup and reproduction boundaries

## Choose the review mode

| Goal | Route | Effect on historical evidence |
|---|---|---|
| Review methodology and saved results | View the notebook on GitHub, or open it locally without executing | No new training required |
| Investigate reproducibility | Supply the CSV, prepare an environment, then intentionally execute a separate working copy | A new experiment; output may differ |
| Run the exported workflow | Execute `customer_churn_prediction.py` from the root | Trains in memory and shows a plot; no model is saved |

The documentation sprint used only the first mode. It did not execute the
notebook, import the ML script, install project dependencies, or download data.

## Environment inventory

[requirements.txt](../requirements.txt) lists `numpy`, `pandas`, `matplotlib`,
and `scikit-learn`, without version pins. Jupyter is not listed. The notebook's
metadata records Python 3.11.9, but no exact package versions, operating-system
record, environment lockfile, or fitted estimator parameter dump.

The [README setup commands](../README.md#14-installation-and-reproduction)
create an isolated environment and install a notebook frontend separately.
They use explicit interpreter paths so Windows users do not need to change
PowerShell's execution policy to activate a virtual environment. On Linux,
some distributions package Python's `venv` support separately. On macOS,
`python3.11` must already be installed and available on `PATH`.

Installing today's packages is not an exact restoration of the original
environment. In particular, categorical dtype selection has a saved pandas
compatibility warning. Do not promise that any broad Python version range or
new library release is supported without a deliberate compatibility check.

## Data and working directory

Follow [dataset acquisition and verification](dataset.md) before execution.
The required layout is the repository root with these three sibling files:

```text
customer_churn_prediction.ipynb
customer_churn_prediction.py
customer_churn_dataset-testing-master.csv    # external input, not tracked
```

The `pd.read_csv` path is relative to the process working directory, not
automatically to the Python file's location. Launch the script from the
repository root. For Jupyter, select the prepared environment as the kernel
and confirm its working directory points to this root. Do not move or edit
the original files to compensate for a wrong launch directory.

## Expected checkpoints for a future intentional run

| Stage | Historical checkpoint |
|---|---|
| Raw inspection | 64,374 × 12; no saved nulls |
| Selected categorical fields | `Gender`, `Subscription Type`, `Contract Length` |
| Selected numeric predictors | `Age`, `Tenure`, `Usage Frequency`, `Support Calls`, `Payment Delay`, `Total Spend`, `Last Interaction` |
| Encoded training / test matrices | `(51499, 15)` / `(12875, 15)` |
| Estimator constructor | `LogisticRegression(random_state=42)` |
| Test matrix counts | `[[5655, 1138], [1030, 5052]]` |
| Formatted accuracy | `83.16%` |

These checkpoints are comparison evidence, not acceptance conditions to force
by changing code or selecting a convenient dataset. Investigate mismatches in
source bytes, row order, schema, dtype inference, package versions, and solver
behavior. Record deviations separately and preserve the historical outputs.

The script contains bare expressions such as `df.describe()` that display in
Jupyter but do not print when run as a normal script. Its visible console
output therefore differs from the notebook even with the same workflow.

## Record a future reproduction responsibly

For a separately authorized experiment, capture the source/version/license and
SHA-256 of the input, exact Python and dependency versions, full estimator and
transformer parameters, working directory, warnings, split configuration, and
all per-class metrics. A fixed seed helps repeat the split for identical
ordered data; it does not identify the missing dataset or software versions.

Keep virtual environments, downloaded data, Jupyter checkpoints, and new plots
out of documentation commits. Review `git status --short` before staging.

[Return to installation and reproduction](../README.md#14-installation-and-reproduction)
