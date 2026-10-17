# Banking Marketing Campaign Analytics — Data Analysis Notebooks

## Overview

These notebooks support the Banking Marketing Campaign Analytics Dashboard by preparing the banking marketing dataset and exploring customer demographic and behavioral characteristics.

## Dataset

**Source:** [Banking Dataset - Marketing Targets (Kaggle)](https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets)

The analysis uses the training and test datasets supplied by the source.

## How the dashboard gets its data

These notebooks are for **exploration only**.

The dashboard does **not** read any notebook output. It uses [`data_prep.py`](../data_prep.py), which loads the raw `data/train.csv` and cleans it in code each time the app starts (cached by Streamlit). To reproduce the table the dashboard uses:

```python
import data_prep
df = data_prep.prepare()
```

Cleaned CSVs exported from notebooks are not stored in this repo. If a notebook step matters for the dashboard, it belongs in `data_prep.py` with a test in `tests/`.

## Notebooks

### 1. `01_data_inspection_preprocessing.ipynb`

This notebook performs:

* Initial inspection of the training and test datasets.
* Review of column names, data types, and sample records.
* Missing-value and duplicate-record checks.
* Standardization of categorical variables.
* Handling of special values, including `pdays = -1`.
* Creation of analysis-ready fields and cleaned datasets.

**Outputs:** `bank_marketing_train_clean.csv` and `bank_marketing_test_clean.csv`.

### 2. `02_customer_characteristics_eda.ipynb`

This notebook performs:

* Descriptive statistical analysis of customer age and account balance.
* Frequency analysis of occupation, education, marital status, and loan characteristics.
* Visualizations using histograms, bar charts, and box plots.
* Customer subscription response-rate comparisons across demographic groups.
* Potential outlier detection using the interquartile range (IQR) method.

**Outputs:** Visualization images and CSV summary tables.

## How to Run

1. Open the first notebook in Google Colab.
2. Upload the original `train.csv` and `test.csv` files when prompted.
3. Run the inspection and preprocessing code.
4. Download the generated cleaned training dataset.
5. Open the second notebook in Google Colab.
6. Upload `bank_marketing_train_clean.csv`.
7. Run all cells to generate descriptive statistics, visualizations, and findings.

## Libraries

* pandas
* numpy
* matplotlib
* seaborn
* Google Colab file-upload utilities

## Notes

* Original datasets are preserved during preprocessing.
* Unknown categorical values are standardized rather than assigned guessed values.
* Potential outliers are identified but not automatically removed.
* Exploratory response-rate comparisons are descriptive and do not establish causation.

## Contribution

**Contributor:** Keerthanaa Ellur

**Branch:** `keerthanaa-data-analysis`

**Tasks:** Download and initial inspection of selected dataset, Clean and preprocess the dataset, and Perform exploratory data analysis on customer characteristics.
