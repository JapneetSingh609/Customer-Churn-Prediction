# Evidence and documentation audit

This case study describes the implementation and saved outputs in
[the notebook](../customer_churn_prediction.ipynb) and its
[Python export](../customer_churn_prediction.py). No training was rerun during
the documentation sprint. Saved outputs are historical evidence, not an
independently reproduced experiment.

## Evidence map

Cell numbers below are **one-based positions in notebook order**, including
Markdown cells. They are not the saved execution counters (103–120).

| Claim | Evidence | Verified observation |
|---|---|---|
| Input filename | Cell 4, `pd.read_csv` | `customer_churn_dataset-testing-master.csv` |
| Dataset dimensions | Cell 6, saved `df.info()` | 64,374 rows; 12 columns |
| Model inputs | Cell 4 | Drop `CustomerID` and `Churn` from `X`; assign `Churn` to `y` |
| Missing values | Cell 8, saved null counts | Zero in every column; no imputation or row deletion implemented |
| Target prevalence | Cell 7, saved `describe()` | Binary target, mean 0.473685; approximately 47.37% class 1 |
| Split | Cell 11 | `test_size=0.2`, `random_state=42`; no `stratify` argument |
| Categorical fields | Cell 14, saved printed selection | `Gender`, `Subscription Type`, `Contract Length` |
| Numeric fields | Cell 14, saved printed selection | Seven numeric predictors |
| Encoding | Cell 15 | `ColumnTransformer`, `OneHotEncoder()`, numeric remainder passed through |
| Encoded shapes | Cells 16–17, saved outputs | Training `(51499, 15)`; test `(12875, 15)` |
| Scaling | Cell 19 | `StandardScaler()` fitted on encoded training data; test transformed only |
| Estimator | Cell 21 | `LogisticRegression(random_state=42)`; other parameters omitted |
| Predictions | Cell 23 | `classifier.predict(X_test)` |
| Matrix | Cell 26, saved image | `[[5655, 1138], [1030, 5052]]`; true labels on rows |
| Accuracy | Cell 28, saved text | `Accuracy: 83.16%` |
| Classification report | Cell 30, saved text | Per-class, macro, and weighted scores; see below |
| Python version | Notebook `language_info.version` | 3.11.9; package versions absent |

## Saved classification report

Values below preserve the notebook's two-decimal rounding.

| Label / averaging | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| 0 — stays | 0.85 | 0.83 | 0.84 | 6,793 |
| 1 — churns | 0.82 | 0.83 | 0.82 | 6,082 |
| Macro average | 0.83 | 0.83 | 0.83 | 12,875 |
| Weighted average | 0.83 | 0.83 | 0.83 | 12,875 |

Accuracy reconstructed from the matrix is
`(5655 + 5052) / 12875 = 0.8316116505`, consistent with the printed 83.16%.
This arithmetic uses saved counts and does not rerun inference.

## Corrections to the previous README

| Previous claim or presentation | Evidence-based correction |
|---|---|
| Precision, recall, and F1 all described as positive-class 0.83 | Churn precision and F1 are 0.82; 0.83 values belong to aggregate rows or rounded recall |
| Equal rounded metrics prove balanced performance | Averaging and rounding do not establish balanced errors or deployment fitness |
| `data/customer_churn.csv` in the tree | No dataset is tracked; the code expects a differently named CSV in the working directory |
| `notebooks/customer_churn_prediction.ipynb` | The notebook is at the repository root |
| Split occurs before any processing | Identifier/target separation and descriptive inspection precede the split; learned transforms follow it |
| Numeric features alone are scaled | Scaling is applied to all 15 encoded columns, including one-hot indicators |
| Python 3.8+ advertised as supported | Only Python 3.11.9 is recorded; no supported-version test matrix exists |
| Dependency install is sufficient for notebook use | Jupyter is not included in `requirements.txt` and needs separate installation |
| A complete deployable solution is implied | The repository contains an experiment, with no serving interface or serialized model |

## Evidence boundaries

- **Provenance:** no original download URL, dataset version, checksum, or data
  license is recorded. A matching external catalog can help locate a candidate
  CSV; it cannot establish which exact bytes produced these outputs.
- **EDA:** only information, descriptive statistics, null counts, and dtypes are
  inspected. No correlation, segmentation, feature importance, or causal
  analysis is implemented.
- **Visuals:** the sole tracked evaluation chart is
  [the confusion matrix](../Images/confusion_matrix.png). Its four counts match
  the notebook's embedded chart; their image dimensions differ.
- **Environment:** dependencies are unpinned. Cell 14 saves a `Pandas4Warning`
  about selecting string columns with `include=[object]`. No package lockfile
  or complete environment capture accompanies the result.
- **Reproducibility:** without the CSV and original package versions, matching
  the saved score cannot be guaranteed. A fixed split seed does not close these
  gaps.

## Preservation baseline

The sprint began at Git commit
`e42a115b3e599873227e9faac9bd48b14f4068f8` with a clean working tree.
The following SHA-256 values were recorded before editing documentation.

| Protected original file | SHA-256 |
|---|---|
| `customer_churn_prediction.py` | `f0cdc55c5ee89e1769cc1cedcfdedfb5494329d392ee75ba4f3d54b3e63791af` |
| `customer_churn_prediction.ipynb` | `89d20b32e057bbc91f76b7c7e12881e6ac5eb4e0daabd11e294a6ae307a21501` |
| `Images/confusion_matrix.png` | `7757c480406c63fc8a493d60e8c8eabf4a6b64122690ad5f0918881cdd0a4b3b` |
| `requirements.txt` | `3f6f76469ed99dca3927abfc33c0b81bb3071077c621d681254d0347b8b7e31f` |
| `LICENSE` | `72a967ad8f5674562cd5bcc81b8665f2791382f23a671d5e7ce595954f636d69` |
| `Images/.gitkeep` | `7eb70257593da06f682a3ddda54a9d260d4fc514f645237f5ca74b08f8da61a6` |

## Documentation verification

Validation for the documentation sprint included:

- SHA-256 comparisons against all six protected original files above, before
  each commit and at final review. No protected bytes changed.
- Review of allowed paths, staged diffs, Markdown links, heading fragments,
  code fences, image paths, and `git diff --check` against the starting commit.
- Markdown parsing with Mistune, including tables; Mermaid parsing with the
  Mermaid library, which identifies the diagram as `flowchart-v2`.
- SVG XML checks for a 3:1 viewBox, descriptive accessibility elements, and
  absence of scripts, external resources, embedded HTML, and animation.
- Banner rendering with Resvg and visual inspection at widths of 1440 and
  390 pixels. Text and network artwork remain separate and unclipped; the
  adjacent Markdown title/subtitle supplies readable text at narrow widths.
- Comparison of both existing confusion-matrix images and arithmetic checks
  against the saved accuracy and per-class report. No model or chart was rerun.
- Comparison of the README tree with the tracked file list.

The browser preview service was unavailable, and native browser automation
stopped before navigation. **Full README browser previews and GitHub rendering
were not verified.** Local Markdown parsing, Mermaid parsing, and SVG rendering
do not certify GitHub's complete rendering or sanitizer behavior. Isolated
rendering tools were installed only in the system temporary directory; project
dependencies were unchanged.

Setup commands were checked against the actual paths and dependency list but
were not executed as a reproduction. Dataset identity, upstream terms, exact
package versions, and future-sample performance remain unresolved.

[Return to the project README](../README.md)
