# run_backtest PRD

## Description
Executes a rigorous backtest of a well-defined trading strategy, leveraging validated data and optimized parameters to deliver actionable insights.


## Conceptual Info

This node executes a backtest of a trading strategy using validated data and optimized parameters.

## Docstring

### Summary
Executes a rigorous backtest of a trading strategy and returns key performance metrics.

### Returns

JSON object: Backtest results with cumulative return, Sharpe ratio, max drawdown, and win rate

### Examples

```python
>>> from backtest_framework import Backtest
>>> bp = Backtest(data, strategy, params)
Backtest results: cumulative_return=1.2ℕ, sharpe_ratio=1.5ℕℕ, max_drawdown=0.8ℕ, win_rate=60%
```
