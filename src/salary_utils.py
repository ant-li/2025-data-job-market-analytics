import pandas as pd
import numpy as np
import re

HOURS_PER_YEAR = 2080
MONTHS_PER_YEAR = 12


def parse_salary_row(pay, rate):
    """
    Parses salary text and converts it to annualized min/max values.

    Parameters:
        pay (str): Salary text (e.g. "$60K-$80K", "$40/hour")
        rate (str): Pay frequency ("an hour", "a month", "a year")

    Returns:
        pd.Series: [min_annual, max_annual, salary_type]
    """

    if pd.isna(pay):
        return pd.Series([np.nan, np.nan, np.nan])

    text = str(pay).replace("–", "-").replace(",", "").strip().upper()

    numbers = re.findall(r"\d+\.?\d*", text)
    numbers = [float(n) for n in numbers]

    if not numbers:
        return pd.Series([np.nan, np.nan, np.nan])

    min_val = numbers[0]
    max_val = numbers[1] if len(numbers) > 1 else numbers[0]

    if "K" in text:
        min_val *= 1000
        max_val *= 1000

    # --- Determine salary type ---
    if isinstance(rate, str):
        rate = rate.lower()

    if rate == "an hour":
        salary_type = "hourly"
        min_annual = min_val * HOURS_PER_YEAR
        max_annual = max_val * HOURS_PER_YEAR

    elif rate == "a month":
        salary_type = "monthly"
        min_annual = min_val * MONTHS_PER_YEAR
        max_annual = max_val * MONTHS_PER_YEAR

    else:  # 'a year' OR NaN → treat as annual
        salary_type = "annual"
        min_annual = min_val
        max_annual = max_val

    return pd.Series([min_annual, max_annual, salary_type])