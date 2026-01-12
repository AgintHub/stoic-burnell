# determine_base_year PRD

## Description
Determines the base year from the aggregated data.


## Conceptual Info

The determine_base_year shim function plays a crucial role in identifying the base year for index calculations, ensuring accurate and consistent results across various economic and financial analyses.

## Docstring

### Summary
Determines the base year from the provided aggregated data.

### Parameters

- **aggregated_data** (str): A string containing aggregated data, expected to be in a format that allows for year identification.

### Returns

int: The determined base year.

### Raises

- ValueError: When the input aggregated data is empty or does not contain a valid year.
- TypeError: When the input aggregated data is not of type str.

### Examples

```python
>>> determine_base_year(aggregated_data='2020:100,2021:120,2022:150')
>>> determine_base_year(aggregated_data='2010:50,2011:60,2012:70')
2020
```

```python
>>> determine_base_year(aggregated_data='')
>>> determine_base_year(aggregated_data=None)
ValueError: Input aggregated data is empty or not provided.
```
