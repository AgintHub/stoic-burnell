# compute_index_series PRD

## Description
Compute annual alternative inflation index values from consolidated household expenditure data and a prescribed weighting scheme.


## Conceptual Info

This node calculates annual alternative inflation index values based on consolidated household expenditure data and a prescribed weighting scheme.

## Docstring

### Summary
Compute annual alternative inflation index values.

### Parameters

- **expenditure_data** (str): Consolidated household expenditure data in CSV format.
- **weighting_scheme** (str): Prescribed weighting scheme in CSV format.

### Returns

dict: A dictionary containing the list of years, corresponding index values, and a flag indicating whether index computation succeeded.

### Raises

- ValueError: If the input expenditure data or weighting scheme is invalid.

### Examples

```python
>>> expenditure_data = 'Year,Category,Location,Expenditure_Amount'
>>> weighting_scheme = 'Category,Weight'
>>> result = compute_index_series(expenditure_data, weighting_scheme)
{'years': [2020, 2021, 2022], 'index_values': [100.0, 102.0, 104.0], 'is_index_successful': True}
```
