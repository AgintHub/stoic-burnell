# validate_acquired_data PRD

## Description
Ensure the ingested data is correct and complete.


## Conceptual Info

Validates the completeness and accuracy of acquired market data.

## Docstring

### Summary
Validates acquired market data for completeness and accuracy.

### Parameters

- **acquired_data** (dict): Dictionary containing the acquired market data. It should include keys such as 'data_sources', 'start_timestamp', 'end_timestamp', and 'data'.

### Returns

dict: A dictionary containing the validation status, checks performed, results of checks, missing timestamps, and price consistency issues.

### Raises

- ValueError: If the acquired data is not provided or is empty.

### Examples

```python
>>> acquired_data = {
...     'data_sources': ['source1', 'source2'],
...     'start_timestamp': '2022-01-01',
...     'end_timestamp': '2022-01-02',
...     'data': [...]
>>> }
>>> validate_acquired_data(acquired_data)
{'validation_status': True, 'checks_performed': ['timestamp_check', 'price_consistency_check'], 'check_results': [True, True], 'missing_timestamps': [], 'price_consistency_issues': []}
```

```python
>>> acquired_data = {
...     'data_sources': ['source1', 'source2'],
...     'start_timestamp': '2022-01-01',
...     'end_timestamp': '2022-01-02',
...     'data': [...]
>>> }
>>> validate_acquired_data(acquired_data)
{'validation_status': False, 'checks_performed': ['timestamp_check', 'price_consistency_check'], 'check_results': [False, True], 'missing_timestamps': [1640995200], 'price_consistency_issues': ['inconsistent_price']}
```
