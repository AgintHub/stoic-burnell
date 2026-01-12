# define_order_status_options PRD

## Description
This shim function generates a list of valid order status options based on the provided execution algorithms.


## Conceptual Info

This shim determines the set of valid order status options based on the execution algorithms in use.

## Docstring

### Summary
Defines the list of valid order status options according to the specified execution algorithms.

### Parameters

- **execution_algorithms** (str): A string specifying the execution algorithms (e.g., 'VWAP', 'TWAP') used in order execution.

### Returns

list of str: A list of strings representing the allowed order status options.

### Raises

- ValueError: Raised if the execution_algorithms parameter is invalid or cannot be processed.
- TypeError: Raised if the input type of execution_algorithms is not a string.

### Examples

```python
>>> define_order_status_options('VWAP, TWAP')
['Pending', 'Executed', 'Cancelled', 'Failed', 'Replaced']
```

```python
>>> define_order_status_options('Market')
['Pending', 'Filled', 'Cancelled', 'Failed']
```
