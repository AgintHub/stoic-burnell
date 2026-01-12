# aggregate_expenditure_by_year_and_category PRD

## Description
Aggregates expenditure data by year and category.


## Conceptual Info

This shim function aggregates expenditure data by year and category, which is a crucial step in calculating the index series.

## Docstring

### Summary
Aggregates expenditure data by year and category.

### Parameters

- **merged_data** (str): Input parameter of type str containing expenditure data

### Returns

str: Aggregated expenditure data

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> import pandas as pd
>>> data = {'Year': [2020, 2020, 2021], 'Category': ['A', 'B', 'A'], 'Expenditure_Amount': [100, 200, 300]}
>>> df = pd.DataFrame(data)
>>> aggregate_expenditure_by_year_and_category(merged_data=df.to_csv())
output
```
