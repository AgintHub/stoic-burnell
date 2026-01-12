# verify_index_computation_success PRD

## Description
Verifies if the index computation was successful based on the provided years and index values.


## Conceptual Info

The verify_index_computation_success shim function validates the success of index computation based on the provided years and index values.

## Docstring

### Summary
Verifies if the index computation was successful based on the provided years and index values.

### Parameters

- **years** (str): Input parameter representing the years for which the index was calculated.
- **index_values** (str): Input parameter representing the corresponding index values for each year.

### Returns

bool: Boolean indicating whether the index computation was successful.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> verify_index_computation_success(years='2020,2021,2022', index_values='100.0,120.0,110.0')
True
```

```python
>>> verify_index_computation_success(years='2020,2021,2022', index_values='100.0,NaN,110.0')
False
```
