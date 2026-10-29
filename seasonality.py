"""Month (seasonality) helpers for the dashboard.

Kept separate from app.py so tests can import it without starting Streamlit.
"""

import pandas as pd

MONTH_ORDER = ["jan", "feb", "mar", "apr", "may", "jun",
               "jul", "aug", "sep", "oct", "nov", "dec"]


def monthly_summary(data):
    """Contacts, conversions and conversion rate for each calendar month.

    Expects a `month` column (jan..dec) and a 0/1 `converted` column.
    Always returns all 12 months in calendar order. A month with no contacts
    (for example after a sidebar filter) gets 0 contacts and a blank rate.
    """
    summary = (
        data.groupby("month")["converted"]
        .agg(Contacts="size", Conversions="sum")
        .reindex(MONTH_ORDER)
    )
    summary["Contacts"] = summary["Contacts"].fillna(0).astype(int)
    summary["Conversions"] = summary["Conversions"].fillna(0).astype(int)
    rate = summary["Conversions"] / summary["Contacts"] * 100
    summary["Conversion Rate (%)"] = rate.where(summary["Contacts"] > 0).round(2)
    summary = summary.rename_axis("month").reset_index()
    summary["Month"] = summary["month"].str.title()
    return summary
