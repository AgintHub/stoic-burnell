# calculate_total_expenditure PRD

## Description
Calculates the total expenditure from a dictionary of category totals.


## Conceptual Info

This shim function calculates the total expenditure from a dictionary of category totals, which is used in the define_alternative_inflation_index function.

## Docstring

### Summary
Calculates the total expenditure from a dictionary of category totals.

### Parameters

- **category_totals** (str): A string representation of the category totals.

### Returns

float: The total expenditure.

### Raises

- ValueError: When the input category totals are invalid or empty.
- TypeError: When the input category totals are of incorrect type.

### Examples

```python
>>> category_totals = '{'Food': 100, 'Transportation': 200}'
>>> calculate_total_expenditure(category_totals=category_totals)
300.0
```

```python
>>> category_totals = '{'Housing': 500, 'Entertainment': 300}'
>>> calculate_total_expenditure(category_totals=category_totals)
800.0
```
