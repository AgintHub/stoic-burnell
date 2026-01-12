# evaluate_backtest_performance PRD

## Description
Assess how well the strategy meets performance goals.


## Conceptual Info

Evaluates the performance of a strategy against predefined objectives.

## Docstring

### Summary
Assesses how well a strategy meets its performance goals based on backtest metrics.

### Parameters

- **backtest_metrics** (dict): Backtest metrics including cumulative return, Sharpe ratio, max drawdown, and win rate.
- **performance_goals** (dict): Performance goals including target cumulative return, acceptable Sharpe ratio, maximum drawdown, and minimum win rate.

### Returns

dict: A dictionary containing meets_performance_goals, cumulative_return, sharpe_ratio, max_drawdown, win_rate, strengths, and weaknesses.

### Raises

- ValueError: If backtest metrics or performance goals are missing required fields.

### Examples

```python
>>> backtest_metrics = {
...     'cumulative_return': 0.1,
...     'sharpe_ratio': 1.2,
...     'max_drawdown': 0.05,
...     'win_rate': 0.6
>>> }
>>> performance_goals = {
...     'target_cumulative_return': 0.08,
...     'acceptable_sharpe_ratio': 1.0,
...     'maximum_drawdown': 0.1,
...     'minimum_win_rate': 0.55
>>> }
>>> evaluate_backtest_performance(backtest_metrics, performance_goals)
{'meets_performance_goals': True, 'cumulative_return': 0.1, 'sharpe_ratio': 1.2, 'max_drawdown': 0.05, 'win_rate': 0.6, 'strengths': ['strong return', 'low drawdown'], 'weaknesses': []}
```
