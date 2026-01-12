# compute_category_location_breakdowns PRD

## Description
Create category‑wise and location‑wise expenditure breakdowns from consolidated household expenditure data.


## Conceptual Info

Aggregates raw household expenditure records into summarized yearly totals by category and by location, facilitating further index and trend analysis.

## Docstring

### Summary
Aggregates expenditure data into yearly category and location totals.

### Parameters

- **expenditure_csv** (str): CSV string produced by `fetch_household_expenditure_data`. Each row must contain `Year,Category,Location,Expenditure_Amount`.

### Returns

Tuple[str, str, bool]: A tuple containing:
  1. `category_spending_csv`: CSV of `Year,Category,Total_Expenditure`.
  2. `location_spending_csv`: CSV of `Year,Location,Total_Expenditure`.
  3. `is_breakdown_successful`: Boolean flag.

### Raises

- ValueError: Raised if `expenditure_csv` is empty, malformed, or missing required columns.

### Examples

```python
>>> sample_csv = "Year,Category,Location,Expenditure_Amount\n2020,Food,NY,12000\n2020,Food,CA,13000\n2020,Utilities,NY,8000\n2021,Food,NY,12500\n2021,Utilities,CA,9000"
>>> cat_csv, loc_csv, success = compute_category_location_breakdowns(sample_csv)
>>> print(cat_csv)
>>> print(loc_csv)
>>> print(success)
Year,Category,Total_Expenditure\n2020,Food,25000\n2020,Utilities,8000\n2021,Food,12500\n2021,Utilities,9000\nYear,Location,Total_Expenditure\n2020,NY,20000\n2020,CA,13000\n2021,NY,12500\n2021,CA,9000\nTrue
```

```python
>>> empty_csv = ""
>>> try:
...     compute_category_location_breakdowns(empty_csv)
>>> except ValueError as e:
...     print(e)
ValueError: expenditure_csv must contain data and include columns Year, Category, Location, Expenditure_Amount.
```
