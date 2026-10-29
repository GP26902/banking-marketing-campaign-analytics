"""Checks that the month chart numbers match a separate pandas calculation on the raw data."""

import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from seasonality import MONTH_ORDER, monthly_summary  # noqa: E402


@pytest.fixture(scope="module")
def raw():
    data = pd.read_csv(ROOT / "data" / "train.csv", sep=";")
    data["converted"] = (data["y"] == "yes").astype(int)
    return data


def expected_by_month(data):
    """Independent calculation: plain counts of rows and of y == 'yes' per month."""
    contacts = data["month"].value_counts()
    conversions = data.loc[data["y"] == "yes", "month"].value_counts()
    return contacts, conversions


def test_months_are_in_calendar_order(raw):
    result = monthly_summary(raw)
    assert result["month"].tolist() == MONTH_ORDER
    assert result["Month"].tolist()[:3] == ["Jan", "Feb", "Mar"]


def test_totals_match_raw_data(raw):
    result = monthly_summary(raw)
    assert result["Contacts"].sum() == len(raw)
    assert result["Conversions"].sum() == (raw["y"] == "yes").sum()


def test_each_month_matches_pandas(raw):
    result = monthly_summary(raw).set_index("month")
    contacts, conversions = expected_by_month(raw)
    for month in MONTH_ORDER:
        assert result.loc[month, "Contacts"] == contacts[month]
        assert result.loc[month, "Conversions"] == conversions[month]
        expected_rate = round(conversions[month] / contacts[month] * 100, 2)
        assert result.loc[month, "Conversion Rate (%)"] == pytest.approx(expected_rate)


def test_totals_match_with_sidebar_style_filters(raw):
    filtered = raw[(raw["job"] == "management") & (raw["contact"] == "cellular")]
    result = monthly_summary(filtered)
    assert result["Contacts"].sum() == len(filtered)
    assert result["Conversions"].sum() == (filtered["y"] == "yes").sum()


def test_month_with_no_contacts_has_zero_and_blank_rate(raw):
    only_may = raw[raw["month"] == "may"]
    result = monthly_summary(only_may).set_index("month")
    assert result.loc["jan", "Contacts"] == 0
    assert pd.isna(result.loc["jan", "Conversion Rate (%)"])
    assert result.loc["may", "Contacts"] == len(only_may)
