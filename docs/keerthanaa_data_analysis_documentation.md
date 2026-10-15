# Banking Marketing Campaign Analytics — Data Analysis Documentation

## 1. Project Objective

The purpose of this work is to inspect, clean, preprocess, and explore the Banking Marketing Campaign dataset to support development of an interactive analytics dashboard.

The analysis focuses on data quality, customer characteristics, customer response patterns, and potential outliers.

## 2. Dataset Description

**Source:** Banking Dataset - Marketing Targets, Kaggle.

The original training dataset contains **45,211 records and 17 columns**, while the test dataset contains **4,521 records and 17 columns**.

The original dataset includes seven integer columns and ten categorical/text columns.

The target variable `y` indicates whether a customer subscribed to a term deposit.

## 3. Initial Dataset Inspection

### Activities Performed

* Loaded both CSV datasets into pandas DataFrames.
* Reviewed column names, data types, and sample records.
* Examined numerical and categorical distributions.
* Checked standard missing values and duplicate records.
* Identified potential data quality issues.

### Findings

* No standard NaN missing values were identified.
* No exact duplicate rows were found in either dataset.
* Some categorical columns contained `"unknown"` values.
* The `pdays` variable contained `-1`, representing customers who had not previously been contacted.
* Negative account balances were present but were not automatically treated as errors.

## 4. Data Cleaning and Preprocessing

### 4.1 Standardizing Formats

Column names and categorical text were standardized using lowercase formatting and removal of unnecessary spaces.

### 4.2 Handling Unknown Values

Categorical `"unknown"` values were replaced with `"not_provided"`.

This approach preserves the distinction between known customer characteristics and unavailable information without introducing guessed values.

### 4.3 Handling `pdays`

The original `pdays = -1` values were handled by creating a `previously_contacted` variable.

* `yes`: Customer had previously been contacted.
* `no`: Customer had not previously been contacted.

The `-1` values were subsequently replaced with zero in the cleaned `pdays` column.

The `previously_contacted` field should be retained when interpreting this variable.

### 4.4 Data Types

Numerical variables were checked and converted to numeric types.

Categorical variables were assigned categorical data types.

The `month` variable was configured as an ordered categorical variable.

### 4.5 Target Encoding

A numeric `target` field was created:

* `yes = 1`
* `no = 0`

The original `y` column was preserved for readability.

### 4.6 Cleaned Outputs

Two cleaned datasets were generated:

* `bank_marketing_train_clean.csv`
* `bank_marketing_test_clean.csv`

## 5. Exploratory Data Analysis — Customer Characteristics

The customer EDA uses the cleaned training dataset.

### 5.1 Numerical Characteristics

Descriptive statistics were generated for customer age and account balance, including:

* Mean
* Median
* Mode
* Standard deviation
* Minimum and maximum
* Quartiles

### 5.2 Categorical Characteristics

Customer distributions were examined across:

* Occupation
* Marital status
* Education level
* Housing loan status
* Personal loan status

Frequency counts and percentages were calculated.

### 5.3 Visualizations

The EDA notebook generates visualizations covering:

* Age distribution
* Occupation distribution
* Education distribution
* Marital status distribution
* Account balance distribution
* Housing and personal loan characteristics
* Response rates by age group
* Response rates by occupation
* Age and account balance box plots

These charts provide an initial understanding of customer composition and response patterns.

## 6. Outlier Analysis

The interquartile range (IQR) method was used to identify potential outliers in age and account balance.

**IQR = Q3 − Q1**

**Lower bound = Q1 − 1.5 × IQR**

**Upper bound = Q3 + 1.5 × IQR**

Observations outside these bounds were flagged as potential outliers.

No records were automatically removed because extreme account balances and customer ages may represent legitimate observations.

## 7. Initial Findings

The initial inspection identified several noteworthy characteristics:

* The average customer age was approximately 40.94 years, with a median of 39 years.
* Blue-collar, management, and technician occupations were the most common.
* Secondary education was the most frequently recorded education level.
* Account balances showed substantial variation, including negative balances and unusually high positive balances.
* The original training dataset had 5,289 positive subscription responses out of 45,211 records, equivalent to approximately 11.70%.

The EDA notebook provides additional demographic distributions, group-level response rates, and IQR-based outlier counts. These outputs should be consulted for the final interpretation of customer-level patterns.

## 8. Limitations

* The analysis is exploratory and does not establish causal relationships.
* Unknown categories may limit interpretation of some customer attributes.
* The cleaned `pdays` field requires the `previously_contacted` indicator for correct interpretation.
* IQR outlier flags do not necessarily indicate invalid records.
* Response rates for small demographic groups should be interpreted cautiously.
* The training and test files are analyzed separately rather than assumed to be a conventional train/test split.

## 9. Deliverables

| Deliverable                              | Description                                                     |
| ---------------------------------------- | --------------------------------------------------------------- |
| `01_data_inspection_preprocessing.ipynb` | Dataset inspection and preprocessing                            |
| `02_customer_characteristics_eda.ipynb`  | Customer descriptive analysis and visualizations                |
| Cleaned training and test CSV files      | Analysis-ready datasets generated by preprocessing              |
| EDA charts                               | Visual evidence of customer distributions and response patterns |
| EDA summary CSV files                    | Descriptive statistics, response rates, and outlier summaries   |

## 10. Conclusion

The initial dataset inspection, cleaning, preprocessing, and customer characteristics EDA provide a foundation for the Banking Marketing Campaign Analytics Dashboard.

The cleaned datasets and descriptive analysis support subsequent dashboard development, customer segmentation, campaign performance comparisons, and evidence-based interpretation of customer response patterns.

## Contributor

**Keerthanaa Ellur**

**Branch:** `keerthanaa-data-analysis`

**Project:** Banking Marketing Campaign Analytics Dashboard
