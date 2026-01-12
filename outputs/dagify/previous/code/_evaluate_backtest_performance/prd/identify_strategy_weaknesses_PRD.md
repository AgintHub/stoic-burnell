# identify_strategy_weaknesses PRD

## Description
Identifies the weaknesses of a trading strategy based on its cumulative return, sharpe ratio, max drawdown, and win rate.


## Conceptual Info

This shim node identifies the weaknesses of a trading strategy based on its performance metrics.

## Docstring

### Summary
Identifies the weaknesses of a trading strategy based on its cumulative return, sharpe ratio, max drawdown, and win rate.

### Parameters

- **cumulative_return** (str): Cumulative return of the trading strategy
- **sharpe_ratio** (str): Sharpe ratio of the trading strategy
- **max_drawdown** (str): Maximum drawdown of the trading strategy
- **win_rate** (str): Win rate of the trading strategy

### Returns

dict: Return a dictionary containing the weaknesses of the trading strategy as a list and the performance metrics as separate values.

### Raises

- ValueError: Raised when the input performance metrics are invalid.
- TypeError: Raised when the input performance metrics are of incorrect type.

### Examples

```python
>>> shim_input = {'cumulative_return': '0.5', 'sharpe_ratio': '1.2', 'max_drawdown': '0.3', 'win_rate': '0.6'}
>>> identify_strategy_weaknesses(**shim_input)
{'output': ['weak strength 1', 'weak strength 2'], 'cumulative_return': 0.5, 'sharpe_ratio': 1.2, 'max_drawdown': 0.3, 'win_rate': 0.6}
```
