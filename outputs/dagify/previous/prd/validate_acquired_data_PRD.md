# validate_acquired_data PRD

## Description
Ensure the ingested data is correct and complete.


## Conceptual Info

Validates the completeness and accuracy of acquired market data.

## Docstring

### Summary
Validates the acquired market data for completeness and accuracy.

### Parameters

- **acquired_data** (dict): The acquired market data to be validated. It should contain fields like 'timestamps', 'prices', etc.

### Returns

dict: A dictionary containing the validation status, checks performed, results of checks, missing timestamps, and price consistency issues.

### Raises

- ValueError: If the input data is not in the expected format.

### Examples

```python
>>> data = {'timestamps': [1, 2, 3], 'prices': [10.0, 20.0, 30.0]}
>>> validate_acquired_data(data)
{'validation_status': True, 'checks_performed': ['timestamp_check', 'price_check'], 'check_results': [True, True], 'missing_timestamps': [], 'price_consistency_issues': []}
```

```python
>>> data = {'timestamps': [1, 2], 'prices': [10.0, 20.0, 30.0]}
>>> validate_acquired_data(data)
{'validation_status': False, 'checks_performed': ['timestamp_check', 'price_check'], 'check_results': [False, True], 'missing_timestamps': [3], 'price_consistency_issues': ['Price list is longer than timestamp list']}
```
