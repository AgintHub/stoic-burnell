# extract_available_years PRD

## Description
Extracts a list of available years from the aggregated data.


## Conceptual Info

The extract_available_years shim function takes aggregated data as input and returns a list of available years.

## Docstring

### Summary
Extracts a list of available years from the aggregated data.

### Parameters

- **aggregated_data** (str): The aggregated data from which to extract available years.

### Returns

List[int]: A list of available years.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> extract_available_years(aggregated_data='{"2020": 10, "2021": 20, "2022": 30}')
[2020, 2021, 2022]
```

```python
>>> extract_available_years(aggregated_data='{}')
[]
```
