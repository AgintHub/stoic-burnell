# validate_acquired_data PRD

## Description
Ensure the quality and integrity of acquired market data.


## Conceptual Info

This node ensures the quality and integrity of acquired market data.

## Docstring

### Summary
Validates acquired market data against established baseline standards for completeness and accuracy.

### Parameters

- **acquired_data** (List[dict]): List of dictionaries containing the acquired market data with fields matching the schema definition.

### Returns

dict: Returns a dictionary with validation status (`validation_status`), checks performed (`checks_performed`), and validation results (`check_results`).

### Raises

- RuntimeError: Raised when encountering unexpected errors during validation, such as data format inconsistencies or missing fields.

### Examples

```python
>>> data = [{'time': '2023-01-01T00:00:00', 'price': 100.0, 'volume': 1001}]" + "
 result = validate_acquired_data(data)
>>> print(result)
{'validation_status': True, 'checks_performed': ['schema_validation', 'data_type_check'], 'check_results': [True, True]}
```
