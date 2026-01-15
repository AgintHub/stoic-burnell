# convert_location_aggregation_to_csv PRD

## Description
Converts aggregated location data into a CSV string.


## Conceptual Info

This shim function takes aggregated location data and converts it into a CSV string, which can be used for further processing or analysis.

## Docstring

### Summary
Converts aggregated location data into a CSV string.

### Parameters

- **aggregated_data** (str): Input parameter containing aggregated location data in a format that can be converted to CSV.

### Returns

str: CSV string representation of the aggregated location data, with columns for Year, Location, and Expenditure Amount.

### Raises

- ValueError: When input validation fails, such as if the input data is not in a valid format.
- TypeError: When input types are incorrect, such as if the input data is not a string.

### Examples

```python
>>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'New York': 1000, 'Los Angeles': 2000}, '2023': {'New York': 1500, 'Los Angeles': 2500}})
"Year,Location,Expenditure Amount\n2022,New York,1000\n2022,Los Angeles,2000\n2023,New York,1500\n2023,Los Angeles,2500"
```

```python
>>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'Chicago': 500, 'Houston': 750}, '2023': {'Chicago': 1000, 'Houston': 1250}})
"Year,Location,Expenditure Amount\n2022,Chicago,500\n2022,Houston,750\n2023,Chicago,1000\n2023,Houston,1250"
```
