# parse_category_csv_to_year_totals PRD

## Description
This shim function takes a CSV string containing category spending data and returns a dictionary where the keys are years and the values are the total expenditures for each category in that year.


## Conceptual Info

The parse_category_csv_to_year_totals shim is responsible for parsing category spending CSV data into a structured dictionary format for further analysis or processing.

## Docstring

### Summary
Parses a CSV string of category spending data into a dictionary where keys are years and values are total expenditures for each category in that year.

### Parameters

- **csv_data** (str): A string containing CSV data with columns for year and category expenditures.

### Returns

dict: A dictionary where each key is a year and each value is the total expenditure for all categories in that year.

### Raises

- ValueError: If the input CSV string is malformed or cannot be parsed.
- TypeError: If the input is not a string or if the CSV data cannot be converted into the required dictionary format.

### Examples

```python
>>> csv_string = 'Year,Category,Expenditure'
>>> csv_string += '\n2020,CategoryA,100'
>>> csv_string += '\n2020,CategoryB,200'
>>> csv_string += '\n2021,CategoryA,150'
>>> result = parse_category_csv_to_year_totals(csv_string)
{'2020': 300, '2021': 150}
```
