# get_current_timestamp PRD

## Description
This shim retrieves the current timestamp as a formatted string, to be used for marking data acquisition start and end times within the data pipeline.


## Conceptual Info

This shim provides a reliable way to obtain the current timestamp as a string, supporting data pipeline timing and logging.

## Docstring

### Summary
Retrieve the current system timestamp as a string for use in data pipeline timing, logging, and metadata purposes.

### Returns

str: A string representing the current timestamp when called, typically formatted in ISO 8601 or the system's standard timestamp format.

### Examples

```python
>>> current_time = get_current_timestamp()
>>> print(current_time)
"2024-04-27T10:15:30Z"
```

```python
>>> start_time = get_current_timestamp
>>> end_time = get_current_timestamp
"2024-04-27T10:15:30Z" and "2024-04-27T10:15:30Z" (example timestamps)
```
