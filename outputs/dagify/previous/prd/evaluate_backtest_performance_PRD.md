# evaluate_backtest_performance PRD

## Description
Assess how well the strategy meets performance goals.


## Conceptual Info

Evaluates the performance of a trading strategy based on backtest results.

## Docstring

### Summary
Assesses how well a trading strategy meets its performance goals based on backtest metrics.

### Parameters

- **backtest_metrics** (dict): Backtest metrics including cumulative return, Sharpe ratio, max drawdown, and win rate.
- **performance_goals** (dict): Performance goals including target cumulative return, acceptable Sharpe ratio, maximum drawdown, and minimum win rate.

### Returns

dict: A dictionary containing boolean indicating if performance goals are met, and lists of strengths and weaknesses.

### Raises

- ValueError: If backtest metrics or performance goals are not provided in the correct format.

### Examples

```python
>>> backtest_metrics = {'cumulative_return': 0.1, 'sharpe_ratio': 1.2, 'max_drawdown': 0.05, 'win_rate': 0.6}
>>> performance_goals = {'target_cumulative_return': 0.05, 'acceptable_sharpe_ratio': 1.0, 'max_drawdown': 0.1, 'min_win_rate': 0.55}
>>> evaluate_backtest_performance(backtest_metrics, performance_goals)
{'meets_performance_goals': True, 'cumulative_return': 0.1, 'sharpe_ratio': 1.2, 'max_drawdown': 0.05, 'win_rate': 0.6, 'strengths': ['High cumulative return', 'Good Sharpe ratio'], 'weaknesses': []}
```
