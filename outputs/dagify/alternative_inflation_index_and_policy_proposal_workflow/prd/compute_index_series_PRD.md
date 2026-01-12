# compute_index_series PRD

## Description
Compute annual alternative inflation index values from consolidated household expenditure data and a prescribed weighting scheme.


## Conceptual Info

Takes raw household expenditure data and a category‑weight matrix to produce a year‑by‑year alternative inflation index.

## Docstring

### Summary
Compute a yearly alternative inflation index from expenditure CSV and category weights.

### Parameters

- **expenditure_csv** (str): CSV string with columns: Year, Category, Location, Expenditure_Amount.
- **is_data_successful** (bool): Flag indicating whether data collection succeeded.
- **index_weights_csv** (str): CSV string with columns: Category, Weight describing the weighting scheme.
- **is_methodology_successful** (bool): Flag indicating whether the methodology definition succeeded.

### Returns

Tuple[List[int], List[float], bool]: A tuple containing the list of years, the calculated index values for each year, and a boolean flag indicating success.

### Raises

- ValueError: If either is_data_successful or is_methodology_successful is False, or if input CSVs are malformed.

### Examples

```python
>>> expenditure_csv = "Year,Category,Location,Expenditure_Amount\n2020,Food,NY,200\n2021,Food,NY,210"
>>> index_weights_csv = "Category,Weight\nFood,1.0"
>>> years, index_values, success = compute_index_series(expenditure_csv, True, index_weights_csv, True)
>>> print(years)
>>> print(index_values)
>>> print(success)
[2020, 2021]\n[200.0, 210.0]\nTrue
```

```python
>>> expenditure_csv = "Year,Category,Location,Expenditure_Amount\n2020,Food,NY,200"
>>> index_weights_csv = "Category,Weight\nFood,1.0"
>>> try:
...     compute_index_series(expenditure_csv, False, index_weights_csv, True)
>>> except ValueError as e:
...     print(str(e))
"Data collection failed. Cannot compute index series."
```
