# compute_index_series PRD

## Description
Compute annual alternative inflation index values from consolidated household expenditure data and a prescribed weighting scheme.


## Conceptual Info

Generates a time‑series of an alternative inflation index by weighting yearly household expenditure across categories according to a user‑defined methodology.

## Docstring

### Summary
Calculate a yearly alternative inflation index using category weights and raw expenditure data.

### Parameters

- **expenditure_csv** (str): CSV string where each row contains Year, Category, Location, and Expenditure_Amount.
- **index_weights_csv** (str): CSV string mapping each Category to a numeric Weight (the sum of weights should typically equal 1).

### Returns

Tuple[List[int], List[float], bool]: A tuple containing (years, index_values, is_index_successful).

### Raises

- ValueError: If either CSV string is malformed or empty.
- KeyError: If a Category present in the expenditure data does not have a corresponding weight.

### Examples

```python
>>> expenditure_csv = """Year,Category,Location,Expenditure_Amount
>>> 2020,Food,Urban,1000
>>> 2020,Transport,Urban,200
>>> 2020,Food,Rural,800
>>> 2020,Transport,Rural,150
>>> 2021,Food,Urban,1100
>>> 2021,Transport,Urban,210
>>> 2021,Food,Rural,850
>>> 2021,Transport,Rural,160
>>> """
>>> weights_csv = """Category,Weight
>>> Food,0.6
>>> Transport,0.4
>>> """
>>> years, index_vals, success = compute_index_series(expenditure_csv, weights_csv)
>>> print(years, index_vals, success)
[2020, 2021] [1220.0, 1318.0] True
```
