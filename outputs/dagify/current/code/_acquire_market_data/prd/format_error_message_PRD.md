# format_error_message PRD

## Description
Formats an error message based on the provided source and error information.


## Conceptual Info

This shim function takes a source and error as input and returns a formatted error message.

## Docstring

### Summary
Formats an error message based on the provided source and error information.

### Parameters

- **source** (str): The source information related to the error.
- **error** (str): The error information to be formatted.

### Returns

str: The formatted error message of type str.

### Raises

- TypeError: When source or error is not of type str.

### Examples

```python
>>> format_error_message(source='example_source', error='error_occurred')
'An error occurred while processing example_source.'
```

```python
>>> format_error_message(source='another_source', error='another_error')
'An error occurred while processing another_source.'
```
