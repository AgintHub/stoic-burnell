# format_error_list PRD

## Description
This shim formats a list of error messages into a single consolidated string for reporting.


## Conceptual Info

The shim takes a list of error messages and produces a single formatted string that summarizes all errors for reporting purposes.

## Docstring

### Summary
Formats a list of error messages into a single string representation.

### Parameters

- **errors** (str): A string containing multiple error messages, typically separated or combined.

### Returns

str: A single string that consolidates all error messages for clear reporting.

### Raises

- ValueError: Raised if the input 'errors' is not a string.

### Examples

```python
>>> format_error_list('Error 1; Error 2; Error 3')
'Error 1; Error 2; Error 3'
```

```python
>>> format_error_list('Failed to connect; Timeout occurred')
'Failed to connect; Timeout occurred'
```
