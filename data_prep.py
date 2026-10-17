"""Data preparation for the Bank Marketing dashboard.

The dashboard reads the raw UCI file (data/train.csv) and cleans it in code,
so anyone can reproduce the exact table the app uses. No cleaned CSV is
committed to the repo.

Typical use:
    import data_prep
    df = data_prep.prepare()       # load_raw() -> clean() -> validate()

This module must not import Streamlit, so it can be tested on its own.
Caching (st.cache_data) is applied in app.py.
"""

from pathlib import Path

import numpy as np
import pandas as pd

# --- Settings -----------------------------------------------------------------

DATA_PATH = Path(__file__).resolve().parent / "data" / "train.csv"
EXPECTED_ROWS = 45_211

RAW_COLUMNS = [
    "age", "job", "marital", "education", "default", "balance", "housing",
    "loan", "contact", "day", "month", "duration", "campaign", "pdays",
    "previous", "poutcome", "y",
]
DERIVED_COLUMNS = ["age_group", "converted", "previously_contacted"]
EXPECTED_COLUMNS = RAW_COLUMNS + DERIVED_COLUMNS

NUMERIC_COLUMNS = ["age", "balance", "day", "duration", "campaign", "pdays", "previous"]
MONTH_ORDER = ["jan", "feb", "mar", "apr", "may", "jun",
               "jul", "aug", "sep", "oct", "nov", "dec"]

# Same bins and labels the dashboard has always used (left edge included).
AGE_BINS = [0, 25, 35, 50, 65, 120]
AGE_LABELS = ["<25", "25-34", "35-49", "50-64", "65+"]


class DataValidationError(ValueError):
    """Raised when the data does not look the way the dashboard expects."""


# --- Steps --------------------------------------------------------------------

def load_raw(path=DATA_PATH):
    """Read the raw semicolon-separated UCI file exactly as it is on disk."""
    return pd.read_csv(path, sep=";")


def clean(raw):
    """Return a cleaned copy of the raw data. The input is not modified.

    - Text columns are trimmed and lowercased. The label "unknown" is kept as is.
    - Numeric columns are converted to numbers (bad values become NaN, which
      validate() then catches).
    - month becomes an ordered category (jan ... dec).
    - age_group is added from age.
    - converted is added: 1 if y == "yes", otherwise 0.
    - previously_contacted is added: "yes" if pdays != -1, otherwise "no".
      pdays itself is left unchanged (-1 still means "not previously contacted").
    """
    df = raw.copy()

    text_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in text_cols:
        df[col] = df[col].str.strip().str.lower()

    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            if not df[col].isna().any():
                df[col] = df[col].astype("int64")

    if "month" in df.columns:
        df["month"] = pd.Categorical(df["month"], categories=MONTH_ORDER, ordered=True)

    if "age" in df.columns:
        df["age_group"] = pd.cut(df["age"], bins=AGE_BINS, labels=AGE_LABELS, right=False)

    if "y" in df.columns:
        df["converted"] = (df["y"] == "yes").astype(int)

    if "pdays" in df.columns:
        df["previously_contacted"] = np.where(df["pdays"] != -1, "yes", "no")

    return df


def validate(df, expected_rows=EXPECTED_ROWS):
    """Fail loudly (DataValidationError) if the data is not what the app expects."""
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise DataValidationError(f"Missing expected columns: {missing}")

    null_counts = df[EXPECTED_COLUMNS].isna().sum()
    null_counts = null_counts[null_counts > 0]
    if not null_counts.empty:
        raise DataValidationError(f"Null values found: {null_counts.to_dict()}")

    bad_y = sorted(set(df["y"].unique()) - {"yes", "no"})
    if bad_y:
        raise DataValidationError(f"Column y must be 'yes' or 'no', found: {bad_y}")

    if len(df) != expected_rows:
        raise DataValidationError(f"Expected {expected_rows:,} rows, found {len(df):,}")

    return df


def prepare(path=DATA_PATH):
    """Load, clean and validate the data. This is what app.py calls."""
    return validate(clean(load_raw(path)))