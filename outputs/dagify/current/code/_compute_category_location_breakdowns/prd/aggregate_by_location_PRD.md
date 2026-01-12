# aggregate_by_location PRD

## Description
This shim aggregates expenditure data by location, returning a dictionary with location-based expenditure amounts for each year.


## Conceptual Info

The aggregate_by_location shim plays a crucial role in processing expenditure data, enabling the calculation of total expenditures by location across different years.

## Docstring

### Summary
Aggregates expenditure data by location, calculating total expenditures for each location in each year.

### Parameters

- **data** (str): Input expenditure data as a string, expected to be a list of records containing year, location, and amount information.
- **year_col** (str): The column name in the data that represents the year.
- **location_col** (str): The column name in the data that represents the location.
- **amount_col** (str): The column name in the data that represents the expenditure amount.

### Returns

str: A dictionary containing location-based expenditure amounts for each year, returned as a JSON string.

### Raises

- ValueError: When the input data does not contain the specified year, location, or amount columns.
- TypeError: When the input data or column names are of incorrect types.

### Examples

```python
>>> data = '[{"Year": 2020, "Location": "New York", "Expenditure_Amount": 100}, {"Year": 2020, "Location": "Chicago", "Expenditure_Amount": 200}]'
>>> year_col = 'Year'
>>> location_col = 'Location'
>>> amount_col = 'Expenditure_Amount'
>>> result = aggregate_by_location(data, year_col, location_col, amount_col)
{'2020': {'New York': 100, 'Chicago': 200}}
```
