# banking-marketing-campaign-analytics
Analytics and decision-support dashboard for evaluating banking marketing campaign performance, customer response, and conversion outcomes.


An interactive analytics dashboard built with **Python, Pandas, Plotly, and Streamlit** that turns the public UCI Bank Marketing dataset into an easy-to-explore tool for understanding campaign performance, customer demographics, and the key drivers of term-deposit conversion.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly&logoColor=white)

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Key Performance Indicators](#-key-performance-indicators)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Findings Report](#-findings-report)
- [Getting Started](#-getting-started)
- [Running tests](#-running-tests)
- [Project Structure](#-project-structure)
- [Project Standards](#-project-standards)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔎 Overview

This project helps marketing stakeholders answer practical questions about a bank's term-deposit campaigns:

- Which **contact channels** convert best?
- Which **customer segments** (job, age group, education) respond most?
- Does a **previous successful campaign** make a client more likely to subscribe again?
- At what point does **repeated contact** stop paying off?

---

## ✨ Features

| Feature | Description |
|---|---|
| **Dataset integration** | Loads the raw UCI Bank Marketing dataset (`data/train.csv`, semicolon-separated) and cleans it in code with `data_prep.py` at load time (cached). No cleaned CSV is stored in the repo. |
| **5 dynamic filters** | Sidebar filters for **Occupation/Job**, **Age Group** (auto-binned from raw age), **Education Level**, **Contact Method**, and **Previous Outcome**. |
| **Live KPI cards** | Filtered Customer Count, Average Account Balance ($), and Campaign Conversion Rate (%). |
| **Interactive visualizations** | Three tabs: demographics and balances, campaign characteristics (EDA), and response rates by customer characteristics. |
| **Customer segmentation** | A fourth tab combines any two of six characteristics into a response-rate heatmap, with an adjustable minimum segment size and ranked top/bottom 10 segments. |
| **Raw data explorer** | Expandable table to inspect the underlying filtered data. |

---

## 📈 Key Performance Indicators

### 1. Campaign Response & Conversion Rate
The share of contacted clients who responded positively and subscribed to a term deposit. In this dataset, response and conversion are the same binary target outcome.

```
Conversion Rate = (Clients with y = "yes" / Total Contacted Clients) × 100
```

### 2. Contact Channel Effectiveness
Conversion rate broken down by communication method (e.g., cellular, telephone) to show which channel drives the most engagement.

```
Channel Conversion = (Subscribed Clients per Channel / Total Contacts per Channel) × 100
```

### 3. Segment Targeting Efficiency (Job & Age Group)
Conversion rate across demographic and professional segments to pinpoint high-value customer profiles.

```
Segment Conversion = (Subscribed Clients in Segment / Total Contacts in Segment) × 100
```

---

## 🧪 Exploratory Data Analysis

### Descriptive Statistics

- **Contact methods:** distribution and frequency across cellular, telephone, and unknown channels.
- **Previous campaign outcomes:** historical success, failure, and unknown records, used to gauge retention and retargeting potential.
- **Campaign frequency:** contact attempts per client (`campaign` variable) to track outreach intensity and avoid contact fatigue.

### Visualizations

1. **Conversion Rate by Contact Method**: cellular vs. telephone performance.
2. **Impact of Previous Campaign Outcome**: how past success (`poutcome == 'success'`) relates to current conversion.
3. **Campaign Frequency vs. Conversion**: box plot and distribution of contact attempts against subscriptions.

### Key Findings

- **Past success matters.** Clients with a previously successful campaign subscribe at a dramatically higher rate than cold contacts.
- **Cellular dominates.** Cellular contacts account for most engagement and convert better than landlines.
- **Diminishing returns.** Conversions concentrate in the first 1–4 contact attempts; 10+ attempts show steep drop-off and are operational outliers.

### Response Rates by Customer Characteristics

The **📊 Response Rates by Customer** tab shows response rates by age group, occupation, education level and marital status. Each chart marks the overall rate with a dashed line and responds to the sidebar filters.

- **Highest-response groups:** customers aged 65+ (42.10%), students (28.68%) and retirees (22.79%), compared with an overall rate of 11.70%.
- **Lowest-response groups:** ages 35-49 (9.62%) and blue-collar workers (7.27%).
- **Caution:** the highest-response age groups have only about 800 customers each, so treat their rates with care.

---

## 📄 Findings Report

A plain-language summary of the data, methods, KPI definitions and key findings is in [docs/findings-report.md](docs/findings-report.md).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 (tested)
- `pip`

### Installation

```bash
# Clone the repository
git clone https://github.com/Community-Dreams-Foundation-ProjectPool/banking-marketing-campaign-analytics.git
cd banking-marketing-campaign-analytics

# Install dependencies
pip install -r requirements.txt
```

### Run the dashboard

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

> **Note:** The app reads the dataset from `data/train.csv`, so run the command from the repository root.

---

## 🧪 Running tests

The tests check the data preparation steps and confirm that the dashboard numbers are correct (45,211 customers, 11.70% conversion, $1,362.27 average balance, a filtered case and three segment spot checks).

```bash
# From the repository root
pip install -r requirements-dev.txt
pytest
```

The tests read `data/train.csv`, so run them from the repository root.

---

## 🗂 Project Structure

```
banking-marketing-campaign-analytics/
├── app.py                  # Streamlit dashboard
├── data_prep.py            # Loads, cleans and validates the raw data
├── seasonality.py          # Monthly seasonality calculations
├── requirements.txt        # Python dependencies
├── requirements-dev.txt    # Test dependencies (pytest)
├── pytest.ini              # pytest settings
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── .github/
│   └── pull_request_template.md
├── data/
│   ├── train.csv           # UCI Bank Marketing dataset (used by the app)
│   └── test.csv
├── tests/                  # pytest tests for data prep and dashboard numbers
├── docs/
│   ├── findings-report.md  # Findings and methodology report
│   ├── task-summaries/     # One summary per completed task
│   └── screenshots/        # Dashboard screenshots
└── notebooks/              # Exploratory notebooks (the app uses data_prep.py)
```

---

## ✅ Project Standards

- **Performance:** optimized for load times under 5 seconds.
- **Architecture:** clean, open-source structure.
- **Documentation:** structured, commented code following Python best practices.
- **Version control:** maintained in this GitHub repository.

---

## 📂 Dataset

[UCI Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing): data from direct marketing campaigns (phone calls) of a Portuguese banking institution, where the goal is to predict whether a client subscribes to a term deposit.

---

## 🤝 Contributing

Work on a branch, open a pull request into `main`, and add the project manager as a reviewer. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

---

## 📄 License

Released under the [MIT License](LICENSE).