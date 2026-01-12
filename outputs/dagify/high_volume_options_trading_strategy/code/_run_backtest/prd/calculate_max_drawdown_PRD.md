# calculate_max_drawdown PRD

## Description
A shim node that computes the maximum drawdown metric from given performance metrics data.


## Conceptual Info

This shim calculates the maximum drawdown metric based on performance metrics data to assess worst-case loss in strategy performance.

## Docstring

### Summary
Computes the maximum drawdown value from the provided performance metrics data, given as a string, and returns it as a float.

### Parameters

- **metrics** (str): A string containing serialized or processed performance metrics data from which the maximum drawdown is extracted.

### Returns

float: A float representing the maximum drawdown value, indicating the largest peak-to-trough decline observed.

### Raises

- ValueError: Raised if the input metrics data is invalid or cannot be parsed to extract the maximum drawdown.
- TypeError: Raised if the input is not of type str.

### Examples

```python
>>> calculate_max_drawdown('{"max_drawdown": 0.25}')
0.25
```

```python
>>> calculate_max_drawdown('metrics data with max drawdown of 0.15')
0.15
```
