# Task Summary: Data Prep Module and Accuracy Tests

**Project:** Banking Marketing Campaign Analytics Dashboard
**Deliverable:** `data_prep.py`, a `tests/` folder, and supporting docs
**Dataset:** UCI Bank Marketing dataset (`data/train.csv`), 45,211 customers

## 1. Objective

Make the data cleaning reproducible from the repo and prove that the dashboard numbers are correct. Before this task the app read the raw `data/train.csv` directly, and the cleaning steps lived only in Colab notebooks whose cleaned CSVs are not in the repo.

## 2. Decisions

- **`unknown` stays `unknown`.** It is not renamed to `not_provided`, because all four tabs, every task summary and the UCI documentation use `unknown`.
- **`pdays = -1` is unchanged.** The EDA tab explains it on screen. A new `previously_contacted` (yes/no) column is added instead.
- **No cleaned CSV is committed.** The app cleans the raw file in code at load time (cached by Streamlit), so anyone can reproduce the result from the raw file.

## 3. Acceptance Criteria

| Criterion | Status | Where |
|---|---|---|
| `pytest` passes from the repo root | ✅ Done (22 passed) | `tests/` |
| Full-dataset KPIs: 45,211 customers, 11.70% conversion, $1,362.27 average balance | ✅ Done | `tests/test_dashboard_numbers.py` |
| Filtered case: telephone + success gives 114 customers at 65.79% | ✅ Done | `tests/test_dashboard_numbers.py` |
| Segment spot checks: retired 65+ 43.56%, student under 25 35.78%, blue-collar 35-49 6.58% | ✅ Done | `tests/test_dashboard_numbers.py` |
| Filter options and chart labels unchanged on all four tabs; load time under 5 seconds | ✅ Done | See section 6 |

## 4. What Changed

| File | Change |
|---|---|
| `data_prep.py` (new) | `load_raw()`, `clean()`, `validate()` and `prepare()` |
| `app.py` | `load_banking_data()` now calls `data_prep.prepare()`. Nothing else changed. |
| `tests/` (new) | `conftest.py`, `test_data_prep.py` (15 tests), `test_dashboard_numbers.py` (7 tests) |
| `requirements-dev.txt` (new) | `pytest` |
| `pytest.ini` (new) | Lets pytest find `data_prep.py` from the repo root |
| `README.md` | Added a "Running tests" section, updated the dataset row and the project structure |
| `notebooks/README.md` | States that the dashboard uses `data_prep.py` and the notebooks are for exploration |

## 5. How `data_prep.py` Works

- **`load_raw()`** reads `data/train.csv` with `sep=";"`, exactly as it is on disk.
- **`clean()`** returns a cleaned copy and does not modify the input:
  - Text columns are trimmed and lowercased.
  - Numeric columns are converted to integers.
  - `month` becomes an ordered category (jan to dec).
  - `age_group` is added, using the same bins and labels as before.
  - `converted` is added (1 if `y` is "yes", otherwise 0).
  - `previously_contacted` is added ("yes" if `pdays` is not -1, otherwise "no").
- **`validate()`** fails loudly with a `DataValidationError` if expected columns are missing, any value is null, `y` is not yes/no, or the row count is not 45,211.
- **`prepare()`** runs the three steps in order. The app shows any validation message in its existing error box.

## 6. Verification

- `pytest` from the repo root: 22 passed.
- The filter options and KPI values on the unfiltered dashboard match the version before this change.
- The tests recompute each expected number with plain pandas, independent of `app.py`, so a mistake in the app logic cannot hide a mistake in the data.
- Loading and cleaning the data takes a fraction of a second. A full run of the app in a headless test took about 2 seconds, under the 5-second target.
- The tests also confirm that `unknown` is kept, `pdays` is unchanged, `previously_contacted` matches `pdays`, `converted` matches `y`, and each `validate()` check fails when it should.

## 7. Notes & Limitations

- Only the notebook cleaning steps that matter for the dashboard were ported. The notebooks remain as exploration.
- `previously_contacted` is defined from `pdays` (`pdays != -1`). Check this against the notebook version.
- `validate()` expects exactly 45,211 rows. If the dataset is ever replaced, update `EXPECTED_ROWS` in `data_prep.py` and the test numbers.
- The tests check the numbers behind the dashboard, not how the pages look. The charts and tabs were checked by running the app.
- `app.py` still creates its own `converted` column on the filtered data. It gives the same values as the one from `data_prep.py`, so it was left alone to avoid changing app behavior.
- The raw data table at the bottom of the app now also shows the new `previously_contacted` column.

## 8. Next Steps (Suggested)

- Add `.DS_Store` to `.gitignore` so macOS files stop appearing in `git status`.
- Run `pytest` automatically on every pull request (for example with GitHub Actions).
- Move the app's filter and segment logic into functions that can be tested directly, so the tests can check the app's own code too.