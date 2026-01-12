# calculate_category_weights PRD

## Description
This shim node calculates category weights based on category totals and total expenditure.


## Conceptual Info

The calculate_category_weights shim is responsible for determining the proportional weight of each category in the overall expenditure, which is crucial for defining an alternative inflation index.

## Docstring

### Summary
Calculates category weights based on category totals and total expenditure, returning a dictionary with these weights.

### Parameters

- **category_totals** (dict): A dictionary where keys are category names and values are the total expenditure for each category.
- **total_expenditure** (float): The total expenditure across all categories.

### Returns

str: A JSON string representing a dictionary where keys are category names and values are their respective weights in the overall expenditure.

### Raises

- ValueError: If the total expenditure is zero or negative, or if category totals are not provided.
- TypeError: If category totals are not a dictionary or if total expenditure is not a number.

### Examples

```python
>>> category_weights = calculate_category_weights(category_totals={'Food': 1000, 'Transport': 500}, total_expenditure=1500)
{'Food': 0.6666666666666666, 'Transport': 0.3333333333333333}
```

```python
>>> category_weights = calculate_category_weights(category_totals={'Housing': 2000, 'Utilities': 300}, total_expenditure=2300)
{'Housing': 0.8695652173913043, 'Utilities': 0.1304347826086957}
```
