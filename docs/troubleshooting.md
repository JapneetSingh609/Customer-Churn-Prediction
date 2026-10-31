# Setup and evidence troubleshooting

These notes diagnose the current workflow without changing its historical
implementation. Use [dataset setup](dataset.md) and
[environment guidance](reproduction.md) first. Opening saved notebook outputs
does not require running the model.

## Input CSV cannot be found

`FileNotFoundError` for `customer_churn_dataset-testing-master.csv` usually
means the input is absent or the process started in a different directory.
The file is not included in the repository. Supply it separately with the
exact filename in the repository root, and launch from that directory.

On Windows, check that the file has not acquired a second `.csv` extension
when extensions are hidden. An extracted archive directory is not itself the
CSV. On case-sensitive systems, spelling and capitalization must match.
Do not edit the script's path or rename a different dataset as a workaround.

## Notebook path or Jupyter command fails

The correct notebook path is `customer_churn_prediction.ipynb` at the root;
there is no `notebooks/` folder. `requirements.txt` does not include Jupyter.
Install `notebook` into the prepared environment, then launch through that
environment's Python using `-m notebook`, as shown in the
[README](../README.md#14-installation-and-reproduction).

If `py -3.11` or `python3.11` cannot be found, an appropriate Python installation
must be available first. Python 3.11.9 is the recorded version; compatibility
with other versions has not been established here.

## Imports fail despite installation

A missing `pandas`, `numpy`, `matplotlib`, or `sklearn` import can indicate that
the notebook kernel is using a different interpreter from the one used for
installation. Check the selected kernel and environment. The distribution is
installed as `scikit-learn` but imported as `sklearn`.

Use the explicit virtual-environment interpreter paths in the README for
both `-m pip` and execution. Changing global packages or PowerShell execution
policy is not necessary for those commands.

## Categorical selection emits a pandas warning

The saved notebook already contains a `Pandas4Warning`: string columns selected
with `include=[object]` are included for backward compatibility, and that
behavior is deprecated. The historical run still selected `Gender`,
`Subscription Type`, and `Contract Length` and completed.

This is a real version-compatibility concern, not evidence of a newly broken
model. Record your installed pandas version and compare the selected column
names with the saved output. Consult the official
[pandas migration guides](https://pandas.pydata.org/docs/user_guide/migration.html).
No replacement selector, warning suppression, or dependency pin was implemented
as part of this documentation sprint. A supported-version policy or code change
requires a separate implementation task.

## Encoder encounters an unknown category

The workflow uses `OneHotEncoder()` without an explicit `handle_unknown`
policy. The [documented default is an error](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
when transforming an unseen category. A different CSV, dtype inference, or
category distribution may expose this limitation.

Check source identity and schema first. Do not fit the encoder on combined
training and test data to remove the error; that would change the evaluation
boundary. A different category policy is future implementation work, not an
existing capability.

## Shapes or metrics differ from the README

The historical encoded shapes are `(51499, 15)` and `(12875, 15)`. These are
observations of the saved experiment, not hard-coded promises for arbitrary
data. Confirm the filename, input row order, 12-column schema, selected
categorical fields, and dependency versions before comparing scores.

Even a matching row count does not prove the original CSV has been recovered.
The source checksum and original package versions are unknown. Log differences
without altering saved cells, seeds, or parameters to force 83.16% accuracy.

If the only discrepancy is `0.83` versus `83.16%`, check formatting: the
classification report prints two decimals, while the accuracy cell prints a
percentage to two decimal places. Positive-class precision/F1 are `0.82`;
macro and weighted values round to `0.83`. See [evaluation](evaluation.md).

## The script prints less than the notebook or waits at a plot

Notebook display expressions such as `df.describe()` do not print by themselves
in a normal Python script. The exported script also calls `plt.show()`, which
may block until its plot window closes in an interactive environment. These
are expected differences between notebook and script use.

No model is written to disk by either route. A headless environment may handle
Matplotlib display differently; no alternate backend configuration or chart
export was added here.

## Documentation changes unexpectedly include ML files

Stop and inspect `git status --short` and the diff. Opening and saving a notebook
can change JSON, outputs, metadata, or line endings without an intentional ML
edit. Preserve the changed state for investigation; do not automatically reset
user work. For documentation commits, stage only the reviewed paths and follow
the [contribution guide](../CONTRIBUTING.md).

[Return to installation and reproduction](../README.md#14-installation-and-reproduction)
