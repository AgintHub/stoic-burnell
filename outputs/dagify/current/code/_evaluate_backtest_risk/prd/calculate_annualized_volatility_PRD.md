# calculate_annualized_volatility PRD

## Description
Calculates the annualized volatility of a given backtest data.


## Conceptual Info

This shim node calculates the annualized volatility of a backtest data, which is a measure of the overall risk of the investments.

## Docstring

### Summary
Calculates the annualized volatility of a given backtest data.

### Parameters

- **backtest_data** (str): The data of the backtest returns, represented as a string.

### Returns

float: The annualized volatility of the backtest returns, represented as a float.

### Raises

- ValueError: Raised when the input backtest data is invalid or malformed.
- TypeError: Raised when the input backtest data is not a string.

### Examples

```python
>>> backtest_returns = ['0.01', '0.02', '0.03', '0.04', '0.05']
>>> calculate_annualized_volatility(backtest_data=' '.join(backtest_returns))
0.0208
```
