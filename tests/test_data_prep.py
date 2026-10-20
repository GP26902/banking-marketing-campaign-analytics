"""Tests for the cleaning and validation steps in data_prep.py."""

import pandas as pd
import pytest

import data_prep
from data_prep import DataValidationError


def test_prepare_returns_expected_shape_and_columns(df):
    assert len(df) == data_prep.EXPECTED_ROWS
    assert list(df.columns) == data_prep.EXPECTED_COLUMNS


def test_cleaning_does_not_change_the_raw_input(raw):
    before = raw.copy()
    data_prep.clean(raw)
    pd.testing.assert_frame_equal(raw, before)


def test_unknown_label_is_kept(df):
    # Decision: "unknown" stays "unknown" (not renamed to "not_provided").
    assert "unknown" in set(df["contact"])
    assert "unknown" in set(df["poutcome"])
    assert "not_provided" not in set(df.to_numpy().ravel())


def test_pdays_is_unchanged(raw, df):
    # Decision: pdays = -1 stays as it is.
    assert df["pdays"].equals(raw["pdays"])
    assert (df["pdays"] == -1).sum() == (raw["pdays"] == -1).sum()


def test_previously_contacted_matches_pdays(df):
    assert set(df["previously_contacted"]) == {"yes", "no"}
    assert ((df["pdays"] != -1) == (df["previously_contacted"] == "yes")).all()


def test_converted_matches_y(raw, df):
    assert set(df["converted"]) == {0, 1}
    assert df["converted"].sum() == (raw["y"] == "yes").sum()
    assert ((df["y"] == "yes") == (df["converted"] == 1)).all()


def test_month_is_ordered_calendar_month(df):
    assert df["month"].cat.ordered
    assert list(df["month"].cat.categories) == data_prep.MONTH_ORDER


def test_age_group_labels_and_bins(df):
    assert list(df["age_group"].cat.categories) == ["<25", "25-34", "35-49", "50-64", "65+"]
    # Left edge is included: age 25 is "25-34", age 65 is "65+"
    sample = data_prep.clean(pd.DataFrame({"age": [24, 25, 34, 35, 64, 65]}))
    assert list(sample["age_group"]) == ["<25", "25-34", "25-34", "35-49", "50-64", "65+"]


def test_text_is_trimmed_and_lowercased(raw):
    messy = raw.head(5).copy()
    messy["job"] = "  Management "
    messy["y"] = " YES"
    cleaned = data_prep.clean(messy)
    assert set(cleaned["job"]) == {"management"}
    assert set(cleaned["y"]) == {"yes"}


def test_numeric_columns_are_integers(df):
    for col in data_prep.NUMERIC_COLUMNS:
        assert pd.api.types.is_integer_dtype(df[col]), col


# --- validate() must fail loudly ---------------------------------------------

def test_validate_fails_on_missing_column(df):
    with pytest.raises(DataValidationError, match="Missing expected columns"):
        data_prep.validate(df.drop(columns=["balance"]))


def test_validate_fails_on_null_values(df):
    broken = df.copy()
    broken.loc[broken.index[0], "job"] = None
    with pytest.raises(DataValidationError, match="Null values"):
        data_prep.validate(broken)


def test_validate_fails_when_y_is_not_yes_no(df):
    broken = df.copy()
    broken.loc[broken.index[0], "y"] = "maybe"
    with pytest.raises(DataValidationError, match="'yes' or 'no'"):
        data_prep.validate(broken)


def test_validate_fails_on_wrong_row_count(df):
    with pytest.raises(DataValidationError, match="Expected 45,211 rows"):
        data_prep.validate(df.iloc[:-1])


def test_bad_numbers_are_caught_by_validate(raw):
    broken = raw.copy()
    broken["balance"] = broken["balance"].astype(object)
    broken.loc[0, "balance"] = "not a number"
    with pytest.raises(DataValidationError, match="Null values"):
        data_prep.validate(data_prep.clean(broken))