# generate_historical_timeline PRD

## Description
Build a comprehensive historical timeline report by joining the annual index series with per‑year category and household‑location expenditure breakdowns into a single, analysis‑ready CSV.


## Conceptual Info

This node merges the computed alternative inflation index series with annual category‑wise and household‑location‑wise spending breakdowns, producing a single historical timeline CSV that downstream nodes can use for trend analysis and benchmarking.

## Docstring

### Summary
Generate a historical timeline CSV by combining the index series with category and location expenditure breakdowns on a per‑year basis.

### Parameters

- **years** (List[int]): List of calendar years for which the alternative inflation index was successfully computed (from `compute_index_series.years`). Each element corresponds by position to an entry in `index_values`.
- **index_values** (List[float]): Alternative inflation index values corresponding to each entry in `years` (from `compute_index_series.index_values`). Must be the same length as `years`.
- **is_index_successful** (bool): Whether the index computation completed successfully in the upstream `compute_index_series` node. If False, this node should not attempt to build the timeline and must mark `is_timeline_successful` as False.
- **category_spending_csv** (str): CSV string from `compute_category_location_breakdowns.category_spending_csv` containing at least the columns `Year`, `Category`, and a numeric total expenditure column (e.g. `TotalExpenditure`). Each row represents the annual total for a given category.
- **location_spending_csv** (str): CSV string from `compute_category_location_breakdowns.location_spending_csv` containing at least the columns `Year`, `HouseholdLocation`, and a numeric total expenditure column (e.g. `TotalExpenditure`). Each row represents the annual total for a given household location.
- **is_breakdown_successful** (bool): Whether the category and location breakdown aggregation completed successfully in the upstream `compute_category_location_breakdowns` node. If False, this node should not attempt to build the timeline and must mark `is_timeline_successful` as False.
- **category_column** (str): Name of the numeric column in `category_spending_csv` that represents the total expenditure per (Year, Category). Default is `'TotalExpenditure'`. Used to construct the per‑year `CategoryTotals` mapping.
- **location_column** (str): Name of the numeric column in `location_spending_csv` that represents the total expenditure per (Year, HouseholdLocation). Default is `'TotalExpenditure'`. Used to construct the per‑year `LocationTotals` mapping.

### Returns

Dict[str, Any]: A dictionary with two keys: 

- `timeline_report_csv` (str): A CSV string where each row aggregates all available information for a given year. The schema is strictly:

  - `Year` (int): Calendar year.
  - `Index` (float): Alternative inflation index value for that year.
  - `CategoryTotals` (str): JSON‑encoded object mapping category names to annual expenditure totals for that year, e.g. `{"Housing": 1234.5, "Food": 987.6}`.
  - `LocationTotals` (str): JSON‑encoded object mapping household location labels to annual expenditure totals for that year, e.g. `{"Urban": 5000.0, "Rural": 2300.0}`.

- `is_timeline_successful` (bool): True if and only if upstream dependencies reported success and the CSVs could be parsed, joined, and serialized without error.

### Raises

- ValueError: Raised if `years` and `index_values` have different lengths, if they are empty when upstream reports success, or if required columns (`Year`, `Category`, `HouseholdLocation`, and the specified numeric total columns) are missing from the breakdown CSVs.
- RuntimeError: Raised if `is_index_successful` or `is_breakdown_successful` is False but the function is invoked in a mode that requires successful upstream computation (e.g. strict mode), or if no overlapping years can be found between the index series and the breakdown CSVs.
- KeyError: Raised if expected field names such as `Year`, `Category`, `HouseholdLocation`, or the configured numeric total columns cannot be found during CSV parsing or aggregation.
- TypeError: Raised if the data types of `years`, `index_values`, or parsed numeric totals are incompatible with the expected numeric operations (e.g. non‑numeric totals that cannot be coerced).

### Examples

```python
>>> from pprint import pprint
>>> years = [2020, 2021]
>>> index_values = [100.0, 103.5]
>>> is_index_successful = True
>>> category_spending_csv = (
...     'Year,Category,TotalExpenditure\n'
...     '2020,Housing,1200\n'"
                "    '2020,Food,800\n'"
                "    '2021,Housing,1300\n'"
                "    '2021,Food,850\n'
>>> )
>>> location_spending_csv = (
...     'Year,HouseholdLocation,TotalExpenditure\n'"
                "    '2020,Urban,1500\n'"
                "    '2020,Rural,500\n'"
                "    '2021,Urban,1600\n'"
                "    '2021,Rural,550\n'
>>> )
>>> is_breakdown_successful = True
>>> result = generate_historical_timeline(
...     years=years,
...     index_values=index_values,
...     is_index_successful=is_index_successful,
...     category_spending_csv=category_spending_csv,
...     location_spending_csv=location_spending_csv,
...     is_breakdown_successful=is_breakdown_successful,
...     category_column='TotalExpenditure',
...     location_column='TotalExpenditure',
>>> )
>>> print(result['is_timeline_successful'])
>>> print(result['timeline_report_csv'])
True
Year,Index,CategoryTotals,LocationTotals
2020,100.0,"{""Housing"": 1200.0, ""Food"": 800.0}","{""Urban"": 1500.0, ""Rural"": 500.0}"
2021,103.5,"{""Housing"": 1300.0, ""Food"": 850.0}","{""Urban"": 1600.0, ""Rural"": 550.0}"
```

```python
>>> # Example with a missing year in breakdowns: 2019 index exists but has no spend data.
>>> years = [2019, 2020]
>>> index_values = [97.0, 100.0]
>>> is_index_successful = True
>>> category_spending_csv = (
...     'Year,Category,TotalExpenditure\n'"
                "    '2020,Housing,1200\n'"
                "    '2020,Food,800\n'
>>> )
>>> location_spending_csv = (
...     'Year,HouseholdLocation,TotalExpenditure\n'"
                "    '2020,Urban,1500\n'"
                "    '2020,Rural,500\n'
>>> )
>>> is_breakdown_successful = True
>>> result = generate_historical_timeline(
...     years=years,
...     index_values=index_values,
...     is_index_successful=is_index_successful,
...     category_spending_csv=category_spending_csv,
...     location_spending_csv=location_spending_csv,
...     is_breakdown_successful=is_breakdown_successful,
>>> )
>>> print(result['timeline_report_csv'])
Year,Index,CategoryTotals,LocationTotals
2019,97.0,"{}","{}"
2020,100.0,"{""Housing"": 1200.0, ""Food"": 800.0}","{""Urban"": 1500.0, ""Rural"": 500.0}"
```
