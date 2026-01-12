# validate_timestamp_consistency PRD

## Description
This shim performs validation of timestamp consistency between the start and end timestamps to ensure data integrity within the larger data processing pipeline.


## Conceptual Info

This shim verifies that provided start and end timestamps are logically consistent, ensuring chronological correctness before data processing continues.

## Docstring

### Summary
This function validates the consistency between start and end timestamps to confirm they represent a coherent time interval, raising errors if validation fails.

### Parameters

- **start_timestamp** (str): The start timestamp string, expected to be in a parseable date-time format.
- **end_timestamp** (str): The end timestamp string, expected to be in a parseable date-time format that must succeed the start timestamp.

### Returns

bool: Returns True if the timestamps are valid and logically ordered; otherwise, raises an error or returns False.

### Raises

- ValueError: Raised when the timestamp strings are improperly formatted or the end timestamp precedes the start timestamp.
- TypeError: Raised if input types are not strings.

### Examples

```python
>>> validate_timestamp_consistency('2023-01-01T00:00:00', '2023-01-02T00:00:00')
True
```

```python
>>> validate_timestamp_consistency('2023-01-02T00:00:00', '2023-01-01T00:00:00')
Error or False indicating invalid timestamp interval
```
