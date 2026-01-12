# determine_validation_checks PRD

## Description
This shim function determines the set of validation checks to perform on acquired market data based on its attributes and context.


## Conceptual Info

The shim generates a list of validation checks tailored to the characteristics of the acquired market data, facilitating comprehensive data validation.

## Docstring

### Summary
Determine the list of validation checks to perform on acquired market data based on its source, timestamps, and other attributes.

### Parameters

- **data_input** (str): A string identifier or serialized representation of the acquired market data object, which includes its attributes necessary for deciding validation checks.

### Returns

str: A comma-separated string representing the list of validation checks to execute, or a list of check names.

### Raises

- ValueError: Raised if the input data input is invalid or missing required attributes.
- TypeError: Raised if the input parameter is not of type str.

### Examples

```python
>>> checks = determine_validation_checks('some_data_identifier')
>>> print(checks)
['timestamp_consistency', 'price_validation', 'missing_data_check']
```

```python
>>> checks = determine_validation_checks('another_data_source')
>>> print(checks)
['timestamp_consistency', 'price_validation']
```
