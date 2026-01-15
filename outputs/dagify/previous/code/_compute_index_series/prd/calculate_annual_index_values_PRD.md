# calculate_annual_index_values PRD

## Description
Calculates annual index values based on aggregated data, a base year, and target years.


## Conceptual Info

The calculate_annual_index_values shim function calculates annual index values based on aggregated data, a base year, and target years. It plays a crucial role in the computation of index series.

## Docstring

### Summary
Calculates annual index values based on aggregated data, a base year, and target years.

### Parameters

- **aggregated_data** (str): Aggregated data used for index calculation
- **base_year** (str): Base year used as reference for index calculation
- **target_years** (str): Target years for which index values are calculated

### Returns

List[float]: List of calculated annual index values

### Raises

- ValueError: When input validation fails or data is inconsistent
- TypeError: When input types are incorrect

### Examples

```python
>>> calculate_annual_index_values(aggregated_data='annual_data', base_year='2020', target_years='[2021, 2022]')
[1.0, 1.2]
```

```python
>>> calculate_annual_index_values(aggregated_data='annual_data', base_year='2019', target_years='[2020, 2021, 2022]')
[0.9, 1.1, 1.3]
```
