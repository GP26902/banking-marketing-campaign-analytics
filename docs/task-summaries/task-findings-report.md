# Task Summary: Findings and Methodology Report

**Project:** Banking Marketing Campaign Analytics Dashboard
**Deliverable:** `docs/findings-report.md`, plus a link from `README.md`
**Dataset:** UCI Bank Marketing dataset (`data/train.csv`), 45,211 customers

## 1. Objective

Write one document that a business stakeholder can read without opening the code. It explains the data, how it was prepared, how each KPI is defined, what the dashboard found, and what the findings cannot tell us.

## 2. Acceptance Criteria

| Criterion | Status | Where / how checked |
|---|---|---|
| Every number matches the dashboard on the full dataset with no filters | ✅ Done | Each figure was recalculated from `data/train.csv` and then compared with the running dashboard on all four tabs |
| Contact-attempt numbers use the dashboard's buckets (1, 2, 3, 4, 5-10, 11+) | ✅ Done | Section 5.3 |
| Each finding names the dashboard tab that supports it | ✅ Done | Section 5, one tab named per finding |
| No code in sections 1, 5 and 7 | ✅ Done | Plain language only; setup steps are left to the README |
| README links to the report | ✅ Done | New contents entry and a short "Findings Report" section |
| One non-technical reviewer confirms it reads clearly | ⏳ Pending | Requested in the pull request |

## 3. What the Report Contains

1. **Summary:** five headline findings, one line each.
2. **Dataset:** source link, 45,211 customers, 17 fields, no personal data.
3. **Data preparation:** the three steps in `data_prep.py` (load, clean, validate), the three decisions (unknown kept, `pdays = -1` kept with `previously_contacted` added, no cleaned CSV committed), and how the 27 automated tests check the numbers (15 data preparation, 7 headline numbers, 5 month figures).
4. **KPI definitions:** conversion rate, channel conversion, segment conversion and lift, with formulas and a worked example.
5. **Key findings:** seven findings, each with its number and dashboard tab.
6. **Limitations:** association not cause; small groups; unknown categories; months pooled across years; minimum segment size is a choice; historical data.
7. **How to use the dashboard:** the five filters, what each of the four tabs answers, and one screenshot per tab.

## 4. Key Numbers Confirmed

- Overall conversion 11.70%; previous success 64.73%.
- Channel: cellular 14.92%, telephone 13.42%, unknown 4.07%.
- Attempts: 14.60%, 11.20%, 11.19%, 9.00%, 7.01%, 3.93%; 92.6% of subscriptions within 4 attempts.
- Customers: 65+ 42.10%, students 28.68%, retirees 22.79%, blue-collar 7.27%.
- Segments: retired 65+ 43.56% (3.72x lift), student under 25 35.78% (3.06x lift).
- Months: Mar, Sep, Oct, Dec at 44-52% on few contacts; May 6.72% on 30.4% of contacts (13,766 of 45,211).
- Loans: housing 7.70% vs 16.70%; personal 6.68% vs 12.66%.

## 5. Verification

- `python -m pytest`: 27 collected, 27 passed.
- Figures in the report were compared with the running dashboard on every tab with all filters on "All".

## 6. Notes & Limitations

- The report describes the dashboard as it stands today. If a tab, chart or number changes, the report needs a matching update.
- Screenshots are taken with all filters on "All". The Demographics screenshot is wide, so its text appears small when displayed on GitHub.
- The report states associations, not causes.

## 7. Next Steps (Suggested)

- Have a non-technical team member read the report and note anything unclear.
- Update the report when the dashboard or the underlying data changes.
