# calculate_year_over_year_inflation PRD

## Description
Calculates year-over-year inflation rates from a given timeline data.


## Conceptual Info

This shim function calculates year-over-year inflation rates from a given timeline data, which is a crucial step in trend analysis and benchmarking.

## Docstring

### Summary
Calculates year-over-year inflation rates from a given timeline data.

### Parameters

- **timeline_data** (List[dict]): A list of dictionaries representing the timeline data, where each dictionary contains information about a specific year.

### Returns

dict: A dictionary containing two keys: 'years' and 'rates', where 'years' is a list of years and 'rates' is a list of corresponding inflation rates.

### Raises

- ValueError: When the input timeline data is malformed or incomplete.
- TypeError: When the input timeline data is not a list of dictionaries.

### Examples

```python
>>> calculate_year_over_year_inflation(timeline_data=[{'year': 2020, 'value': 100}, {'year': 2021, 'value': 110}])
{'years': [2020, 2021], 'rates': [0, 0.1]}
```

```python
>>> calculate_year_over_year_inflation(timeline_data=[{'year': 2019, 'value': 90}, {'year': 2020, 'value': 100}, {'year': 2021, 'value': 110}])
{'years': [2019, 2020, 2021], 'rates': [0, 0.1111, 0.1]}
```
