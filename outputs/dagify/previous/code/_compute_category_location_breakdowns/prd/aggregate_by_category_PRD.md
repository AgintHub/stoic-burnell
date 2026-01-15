# aggregate_by_category PRD

## Description
This shim aggregates expenditure data by category, summing the expenditure amounts for each category in a given year.


## Conceptual Info

The aggregate_by_category shim is designed to process expenditure data, grouping it by categories and summing the corresponding expenditure amounts for each year.

## Docstring

### Summary
Aggregate expenditure data by category, summing expenditure amounts for each category in a given year.

### Parameters

- **data** (str): The input data to be aggregated, expected to be a list of records or a string representing a CSV structure.
- **year_col** (str): The column name in the data that represents the year.
- **category_col** (str): The column name in the data that represents the category.
- **amount_col** (str): The column name in the data that represents the expenditure amount.

### Returns

dict: A dictionary where keys are categories and values are the total expenditure amounts for each category, structured as '{category: total_amount}'.

### Raises

- ValueError: If the input data is not in the expected format or if required columns are missing.
- TypeError: If the input parameters are not of the expected types.

### Examples

```python
>>> data = [{'Year': '2022', 'Category': 'Food', 'Expenditure_Amount': 100},
...         {'Year': '2022', 'Category': 'Transport', 'Expenditure_Amount': 50}]
>>> year_col = 'Year'
>>> category_col = 'Category'
>>> amount_col = 'Expenditure_Amount'
>>> result = aggregate_by_category(data, year_col, category_col, amount_col)
{'Food': 100, 'Transport': 50}
```
