# Task Summary: Demographics Tab Upgrade and Seasonality

**Project:** Banking Marketing Campaign Analytics Dashboard
**Deliverable:** Upgraded **👥 Demographics & Balances** tab in `app.py`, a new `seasonality.py` helper, and a new test in `tests/`
**Dataset:** UCI Bank Marketing dataset (`data/train.csv`), 45,211 customers

## 1. Objective

Bring the first tab up to the standard of the other three tabs (interactive Plotly charts, dark template, hover detail, axis labels) and add the `month` field from the Technical Approach so seasonal patterns can be explored.

## 2. Acceptance Criteria

| Criterion | Status | Where |
|---|---|---|
| Every chart in tab 1 is an interactive Plotly chart and responds to all five filters | ✅ Done | Average balance by job, outcomes by job, conversion by month, age/balance histogram. All use `filtered_df`. |
| Month chart totals match a pandas calculation in a new test in `tests/` | ✅ Done | `tests/test_seasonality.py` (5 tests) |
| Task summary states the main seasonal pattern with its numbers and a short caveat | ✅ Done | Section 4 below |

## 3. What Changed

- **Two `st.bar_chart` charts replaced** with Plotly bar charts (hover detail, axis labels, `plotly_dark`).
- **New conversion rate by month chart.** Bars show contacts, the line shows conversion rate on a second axis, months in calendar order (Jan to Dec). A "View month table" expander shows the numbers behind it.
- **New histogram of age or account balance**, split by subscribed vs. not subscribed. A radio button switches the field. Each group is scaled to 100% on its own because far fewer customers subscribed. For balance, the lowest and highest 1% are left out so the axis stays readable.
- **New rate tables** for housing loan, personal loan and credit default (contacts, % of contacts, conversions, conversion rate).
- **Empty-filter message** added to tab 1, matching the other tabs.
- **"(unchanged)" leftover comment removed** from `app.py`.
- The month calculation lives in `seasonality.py` so the test can import it without starting Streamlit.

## 4. Main Seasonal Pattern (full dataset, no filters)

Overall conversion is 11.70%. Four months stand far above it: **March (51.99%), December (46.73%), September (46.46%) and October (43.77%)**. Together they are 2,008 contacts (4.4% of all contacts) with 940 subscriptions, a combined rate of 46.81%, and 17.8% of all subscriptions.

The busiest month is the weakest: **May has 13,766 contacts (30.4% of the total) but converts at only 6.72%.** July (9.09%) is also below average. The other eight months combined convert at 10.07%.

| Month | Contacts | Conversions | Rate (%) |
|---|---:|---:|---:|
| Jan | 1,403 | 142 | 10.12 |
| Feb | 2,649 | 441 | 16.65 |
| Mar | 477 | 248 | 51.99 |
| Apr | 2,932 | 577 | 19.68 |
| May | 13,766 | 925 | 6.72 |
| Jun | 5,341 | 546 | 10.22 |
| Jul | 6,895 | 627 | 9.09 |
| Aug | 6,247 | 688 | 11.01 |
| Sep | 579 | 269 | 46.46 |
| Oct | 738 | 323 | 43.77 |
| Nov | 3,970 | 403 | 10.15 |
| Dec | 214 | 100 | 46.73 |

**Caveat:** the high-rate months have very few contacts (214 to 738 each, versus 13,766 in May), so the rates are less stable. The data has no year column, so months from different years are pooled, and the bank did not contact customers evenly across the year. A high rate in a month may reflect who was contacted that month, not the month itself. This is an observed association, not a cause.

## 5. Loans and Credit Default (full dataset)

| Field | Value | Contacts | Rate (%) |
|---|---|---:|---:|
| Housing loan | no | 20,081 | 16.70 |
| Housing loan | yes | 25,130 | 7.70 |
| Personal loan | no | 37,967 | 12.66 |
| Personal loan | yes | 7,244 | 6.68 |
| Credit default | no | 44,396 | 11.80 |
| Credit default | yes | 815 | 6.38 |

Customers with a housing loan or personal loan convert at roughly half the rate of those without. Only 815 customers have a credit default, so that rate should be read with care.

## 6. How It Was Checked

- `pytest tests` passes (5 tests): months in calendar order, totals equal the raw row and "yes" counts, each month matches a separate pandas `value_counts` calculation, totals still match under a job + contact filter, and a month with no contacts shows 0 contacts and a blank rate.
- The app was run with several filter combinations (including a combination with no matching records) with no errors.

## 7. Notes & Limitations

- The histogram shows share within each group, not raw counts.
- The balance histogram excludes the lowest and highest 1% of balances for readability.
- Month and loan/default patterns are descriptive and have not been tested for statistical significance.
