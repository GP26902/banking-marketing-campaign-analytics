"""Accuracy tests: the numbers shown in the dashboard, checked against the data.

The expected values come from the task summaries. They are recomputed here
with plain pandas, independent of app.py, so a mistake in the app logic
would not be able to hide a mistake in the data (and vice versa).
"""

import pytest


def conversion_rate(data):
    """Same definition as the KPI card: share of y == 'yes', in percent."""
    return (data["y"] == "yes").sum() / len(data) * 100


# --- Full-dataset KPIs ---------------------------------------------------------

def test_total_customers(df):
    assert len(df) == 45_211


def test_overall_conversion_rate(df):
    assert round(conversion_rate(df), 2) == 11.70


def test_average_account_balance(df):
    assert round(df["balance"].mean(), 2) == 1362.27


# --- One filtered case (sidebar: contact + previous outcome) --------------------

def test_telephone_and_success_filter(df):
    filtered = df[(df["contact"] == "telephone") & (df["poutcome"] == "success")]
    assert len(filtered) == 114
    assert round(conversion_rate(filtered), 2) == 65.79


# --- Segmentation spot checks (Customer Segments tab: Job x Age group) ---------

@pytest.mark.parametrize(
    "job, age_group, expected_rate",
    [
        ("retired", "65+", 43.56),
        ("student", "<25", 35.78),
        ("blue-collar", "35-49", 6.58),
    ],
)
def test_segment_response_rates(df, job, age_group, expected_rate):
    segment = df[(df["job"] == job) & (df["age_group"] == age_group)]
    assert len(segment) > 0
    assert round(conversion_rate(segment), 2) == expected_rate