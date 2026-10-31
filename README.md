<p align="center">
  <img src="Images/customer-intelligence-banner.svg" alt="Customer Intelligence banner" width="100%" />
</p>

# Customer Churn Prediction

A machine learning project for predicting whether a customer is likely to leave a business using historical profile, subscription, usage, and support data.

## Overview

This repository implements a classic binary classification workflow:

- Load customer data
- Separate the target (`Churn`) from the features
- Encode categorical variables
- Scale numerical features
- Train a Logistic Regression model
- Evaluate performance on a held-out test set

The project is built as a notebook and a Python script, making it easy to inspect the full workflow and rerun the training process locally.

## Why it matters

Customer churn is a major business problem because acquiring a replacement customer often costs more than retaining an existing one. A churn model helps teams:

- identify at-risk customers earlier
- prioritize outreach and support efforts
- understand which factors correlate with churn
- measure the value of retention campaigns

This project focuses on the model-building and evaluation stage rather than deployment or production monitoring.

## Model and results

The saved experiment uses a Logistic Regression classifier on 64,374 customer records.

- Train/test split: 80/20
- Test set size: 12,875 rows
- Preprocessing: one-hot encoding for categorical fields + standard scaling
- Model: Logistic Regression

Saved evaluation results on the holdout set:

- Accuracy: 83.16%
- Precision: 0.82
- Recall: 0.83
- F1-score: 0.82

These numbers come from the repository's saved notebook outputs. Training was not rerun for this README, and the original dataset file is not included in the repository.

## Repository contents

```text
.
├── customer_churn_prediction.ipynb   # Notebook version of the workflow
├── customer_churn_prediction.py      # Script version of the workflow
├── requirements.txt                  # Python dependencies
├── LICENSE                           # MIT license
├── Images/
│   ├── confusion_matrix.png
│   └── customer-intelligence-banner.svg
├── docs/
│   ├── dataset.md
│   ├── evaluation.md
│   ├── evidence.md
│   ├── reliability.md
│   ├── reproduction.md
│   ├── troubleshooting.md
│   └── visual-identity.md
├── CONTRIBUTING.md
├── README.md
└── customer_churn_dataset-testing-master.csv  # expected external input
```

> Note: the dataset CSV is expected to be added manually in the project root before running the notebook or script.

## Getting started

### 1) Clone the repository

```bash
git clone https://github.com/JapneetSingh609/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2) Create a virtual environment

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**macOS/Linux:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3) Add the dataset

Place the dataset file named `customer_churn_dataset-testing-master.csv` in the repository root.

### 4) Run the project

**Script version:**

```bash
python customer_churn_prediction.py
```

**Notebook version:**

```bash
jupyter notebook customer_churn_prediction.ipynb
```

## Project workflow

The workflow includes:

1. loading the raw customer dataset
2. dropping the identifier and target columns from the feature set
3. checking basic dataset structure and missing values
4. splitting the data into training and test sets
5. preprocessing categorical features with `OneHotEncoder`
6. scaling transformed features with `StandardScaler`
7. training a `LogisticRegression` model
8. generating predictions and evaluation metrics

## Files and documentation

For deeper context, see:

- [docs/dataset.md](docs/dataset.md)
- [docs/evaluation.md](docs/evaluation.md)
- [docs/evidence.md](docs/evidence.md)
- [docs/reliability.md](docs/reliability.md)
- [docs/reproduction.md](docs/reproduction.md)
- [docs/troubleshooting.md](docs/troubleshooting.md)

## Notes and limitations

- This project is a study and experimental workflow, not a production-ready deployed model.
- The exact dataset provenance and dependency versions are not fully pinned in the repository.
- Model performance should be interpreted as a baseline result, not as a guaranteed outcome for future data.
- For a more rigorous production setup, you would want stronger validation, threshold tuning, drift monitoring, and a reproducible model artifact pipeline.

## License

This project is licensed under the [MIT License](LICENSE).
