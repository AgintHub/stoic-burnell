# extract_max_drawdown PRD

## Description
A shim that computes the maximum drawdown from backtest data to identify the largest peak-to-trough decline during the period.


## Conceptual Info

This shim computes the maximum drawdown from backtest results to assess risk exposure during the trading period.

## Docstring

### Summary
This function calculates the maximum drawdown from provided backtest data to quantify the largest peak-to-trough loss.

### Parameters

- **backtest_data** (str): A string representing serialized backtest data or an identifier from which the maximum drawdown can be extracted.

### Returns

float: The maximum drawdown value indicating the largest percentage decline observed during the backtest period.

### Raises

- ValueError: Raised when the input backtest_data is invalid or cannot be parsed.
- TypeError: Raised when backtest_data is not of type str.

### Examples

```python
>>> max_dd = extract_max_drawdown('serialized_backtest_result')
>>> print(max_dd)
0.25
```

```python
>>> max_dd = extract_max_drawdown('another_backtest_id')
>>> print(max_dd)
0.15
```
