# create_year_index_mapping PRD

## Description
This shim function generates a dictionary mapping years to their corresponding index values.


## Conceptual Info

This shim is used to create a mapping of years to their respective index values, which is essential for generating historical timelines.

## Docstring

### Summary
Generate a dictionary mapping years to index values from input strings of years and index values.

### Parameters

- **years** (str): A comma-separated string of years.
- **index_values** (str): A comma-separated string of index values corresponding to the years.

### Returns

str: A dictionary as a string where keys are years and values are index values.

### Raises

- ValueError: If the lengths of the years and index values strings do not match.
- TypeError: If the input years or index values are not strings.

### Examples

```python
>>> create_year_index_mapping('2020,2021,2022', '10.5,11.2,12.1')
{'2020': 10.5, '2021': 11.2, '2022': 12.1}
```

```python
>>> create_year_index_mapping('2015,2016', '20,21')
{'2015': 20, '2016': 21}
```
