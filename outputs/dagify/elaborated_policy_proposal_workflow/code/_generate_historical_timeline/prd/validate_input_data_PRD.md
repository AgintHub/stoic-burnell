# validate_input_data PRD

## Description
Validates the input data for generating a historical timeline.


## Conceptual Info

The validate_input_data shim function checks if the provided input data for generating a historical timeline is valid and well-formed.

## Docstring

### Summary
Validates the input data for generating a historical timeline.

### Parameters

- **index_input** (str): Input parameter containing index series data. It should be a string representation of a ComputeIndexSeriesOutput object.
- **breakdown_input** (str): Input parameter containing category and location breakdown data. It should be a string representation of a ComputeCategoryLocationBreakdownsOutput object.

### Returns

bool: Boolean indicating whether the input data is valid.

### Raises

- ValueError: When input validation fails due to missing or incorrect data.
- TypeError: When input types are incorrect.

### Examples

```python
>>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120], 'is_index_successful': True})
>>> breakdown_input = str({'category_spending_csv': 'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv': 'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90', 'is_breakdown_successful': True})
>>> validate_input_data(index_input=index_input, breakdown_input=breakdown_input)
True
```

```python
>>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120]})
>>> breakdown_input = str({'category_spending_csv': 'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv': 'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90'})
>>> validate_input_data(index_input=index_input, breakdown_input=breakdown_input)
False
```
