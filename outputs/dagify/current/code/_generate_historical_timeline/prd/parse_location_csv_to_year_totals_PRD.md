# parse_location_csv_to_year_totals PRD

## Description
A shim function that takes a CSV string containing location spending data and returns a dictionary with year-wise totals.


## Conceptual Info

This shim function is used to extract year-wise totals from a CSV string containing location spending data.

## Docstring

### Summary
Parses a CSV string containing location spending data and returns a dictionary with year-wise totals.

### Parameters

- **csv_data** (str): A CSV string containing location spending data with columns: Year, HouseholdLocation, and total expenditure.

### Returns

str: A dictionary with year-wise totals for location spending, where each key is a year and each value is the total expenditure for that year.

### Raises

- ValueError: When the input CSV string is invalid or empty.
- TypeError: When the input csv_data is not a string.

### Examples

```python
>>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2020,Location A,100\n2020,Location B,200\n2021,Location A,150')
{'2020': 300, '2021': 150}
```

```python
>>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2019,Location C,50\n2020,Location C,75')
{'2019': 50, '2020': 75}
```
