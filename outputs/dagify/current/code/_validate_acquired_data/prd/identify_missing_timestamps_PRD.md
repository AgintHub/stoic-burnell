# identify_missing_timestamps PRD

## Description
A shim function that determines the list of timestamps missing data within a specified time range.


## Conceptual Info

This shim identifies timestamps with missing data between the provided start and end timestamps to support data validation and completeness checks.

## Docstring

### Summary
The function receives start and end timestamps as strings and returns a list of integer timestamps where data is missing within this range; it assumes timestamps are in ISO format or comparable string format appropriately parsed into integers.

### Parameters

- **start_timestamp** (str): The starting timestamp of the data range, in a recognizable string format such as ISO 8601.
- **end_timestamp** (str): The ending timestamp of the data range, in a recognizable string format such as ISO 8601.

### Returns

LIST_INT: A list of integers representing timestamps with missing data within the specified range.

### Raises

- ValueError: Raised if the input timestamps are in an invalid format or cannot be parsed into comparable timestamps.
- TypeError: Raised if the inputs are not of type str.

### Examples

```python
>>> identify_missing_timestamps('2023-01-01T00:00:00', '2023-01-01T01:00:00')
[2, 5, 7]
```

```python
>>> identify_missing_timestamps('2023-06-01T00:00:00', '2023-06-01T00:10:00')
[0, 3, 4]
```
