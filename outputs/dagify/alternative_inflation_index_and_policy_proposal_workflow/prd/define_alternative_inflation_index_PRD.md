# define_alternative_inflation_index PRD

## Description
Specifies the methodology and weights for an alternative inflation index derived from household expenditure data.


## Conceptual Info

This node consumes consolidated household expenditure data and defines a transparent, expenditure-share-based weighting scheme for an alternative inflation index. It parses the raw expenditure CSV, computes average budget shares by category across all available years (and, where desired, across locations), normalizes these into a consistent set of index weights, and returns the index name and a Category–Weight CSV suitable for later index computation.

## Docstring

### Summary
Define an alternative inflation index and its category weights from consolidated household expenditure data.

### Parameters

- **expenditure_csv** (str): CSV string produced by `fetch_household_expenditure_data` with schema `Year,Category,Location,Expenditure_Amount`. Each row represents total household expenditure in a given category, location, and year (aggregated from survey or administrative data). The method parses this CSV to derive expenditure shares by category.
- **is_data_successful** (bool): Flag propagated from `fetch_household_expenditure_data`. If `False`, the function skips methodology definition, marks the methodology as unsuccessful, and returns empty outputs (rather than attempting to parse incomplete or missing data).

### Returns

Tuple[str, str, bool]: A 3-tuple `(index_name, index_weights_csv, is_methodology_successful)` where:

- `index_name` (str): Human-readable name of the alternative inflation index. Typically a fixed, descriptive string such as 'Household-Weighted Cost-of-Living Index (HW-COLI)'.
- `index_weights_csv` (str): CSV string with header `Category,Weight` and one row per expenditure category. `Weight` values are non-negative floats that sum to 1.0 (within a small numerical tolerance). These weights represent long-run average household budget shares and will be used later by `compute_index_series`.
- `is_methodology_successful` (bool): Indicates whether the index methodology was successfully specified. `True` if the input data could be parsed and at least one valid category weight was computed; `False` if upstream data failed or if methodology validation checks did not pass.

### Raises

- ValueError: Raised if `is_data_successful` is True but `expenditure_csv` is empty, missing required columns, or cannot be parsed as CSV.
- KeyError: Raised if the parsed CSV does not contain the required columns `Year`, `Category`, and `Expenditure_Amount` (case-sensitive), preventing computation of category shares.
- ZeroDivisionError: Raised if total expenditure across all categories is zero after filtering invalid rows, making it impossible to normalize category shares into weights.
- RuntimeError: Raised if, after all processing steps, no valid categories remain or if the resulting weights fail internal validation (e.g., negative weights or sum outside an acceptable tolerance).

### Examples

```python
>>> expenditure_csv = '''Year,Category,Location,Expenditure_Amount
>>> 2020,Food,Urban,12000
>>> 2020,Housing,Urban,18000
>>> 2020,Transport,Urban,6000
>>> 2021,Food,Rural,8000
>>> 2021,Housing,Rural,10000
>>> 2021,Transport,Rural,4000
>>> '''
>>> index_name, index_weights_csv, ok = define_alternative_inflation_index(
...     expenditure_csv=expenditure_csv,
...     is_data_successful=True,
>>> )
>>> print(index_name)
>>> print(index_weights_csv)
>>> print(ok)
Household-Weighted Cost-of-Living Index (HW-COLI)
Category,Weight
Food,0.3333
Housing,0.4167
Transport,0.2500
True
```

```python
>>> bad_expenditure_csv = ''  # Upstream node failed or returned nothing
>>> index_name, index_weights_csv, ok = define_alternative_inflation_index(
...     expenditure_csv=bad_expenditure_csv,
...     is_data_successful=False,
>>> )
>>> print(index_name, repr(index_weights_csv), ok)
'' '' False
```
