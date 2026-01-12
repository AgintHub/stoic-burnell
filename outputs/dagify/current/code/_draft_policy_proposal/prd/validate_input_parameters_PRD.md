# validate_input_parameters PRD

## Description
Validates the input parameters for the analyze trends and benchmark node.


## Conceptual Info

The validate_input_parameters shim function checks if the input parameters for the analyze trends and benchmark node are valid and correctly formatted.

## Docstring

### Summary
Validates the input parameters for the analyze trends and benchmark node.

### Parameters

- **years** (str): Input parameter representing years.
- **values** (str): Input parameter representing values.
- **summary** (str): Input parameter representing summary.
- **analysis_success** (str): Input parameter representing analysis success.

### Returns

bool: Boolean indicating whether the input parameters are valid.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> validate_input_parameters(years='2020,2021,2022', values='10.0,20.0,30.0', summary='Inflation trend summary', analysis_success='True')
True
```

```python
>>> validate_input_parameters(years='2020,2021', values='10.0,20.0,30.0', summary='Inflation trend summary', analysis_success='True')
False
```
