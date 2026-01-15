# parse_expenditure_csv PRD

## Description
Parses a CSV string of expenditure data into a structured format.


## Conceptual Info

This shim function plays a crucial role in processing household expenditure data by converting raw CSV strings into a structured format for further analysis.

## Docstring

### Summary
Parses a CSV string of expenditure data into a structured format.

### Parameters

- **csv_data** (str): CSV string of expenditure data with columns: Year, Category, Location, Expenditure_Amount.

### Returns

list: List of dictionaries representing the parsed expenditure data.

### Raises

- ValueError: When the input CSV string is malformed or empty.
- TypeError: When the input type is not a string.

### Examples

```python
>>> parse_expenditure_csv('Year,Category,Location,Expenditure_Amount\\n2020,Food,New York,1000\\n2021,Housing,Los Angeles,2000')
[{'Year': '2020', 'Category': 'Food', 'Location': 'New York', 'Expenditure_Amount': '1000'}, {'Year': '2021', 'Category': 'Housing', 'Location': 'Los Angeles', 'Expenditure_Amount': '2000'}]
```

```python
>>> parse_expenditure_csv('')
 raises ValueError
```
