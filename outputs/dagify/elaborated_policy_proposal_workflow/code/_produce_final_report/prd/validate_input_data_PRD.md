# validate_input_data PRD

## Description
Validates the input data for policy proposal and feasibility score.


## Conceptual Info

The validate_input_data shim function checks if the provided policy proposal and feasibility score are valid and properly formatted.

## Docstring

### Summary
Validates the input policy proposal and feasibility score.

### Parameters

- **proposal** (str): The policy proposal string to be validated.
- **score** (str): The feasibility score string to be validated.

### Returns

bool: True if the input data is valid, False otherwise.

### Raises

- ValueError: If the input policy proposal or feasibility score is invalid or missing.
- TypeError: If the input types are incorrect.

### Examples

```python
>>> validate_input_data(proposal='example policy proposal', score='0.8')
True
```

```python
>>> validate_input_data(proposal='', score='')
False
```
