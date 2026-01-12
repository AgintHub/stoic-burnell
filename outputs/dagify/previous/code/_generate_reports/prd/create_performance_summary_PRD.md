# create_performance_summary PRD

## Description
Generates a comprehensive textual performance summary based on key financial metrics and strategy evaluations.


## Conceptual Info

This shim constructs a detailed performance summary string from individual financial metrics and evaluation results to facilitate reporting and analysis.

## Docstring

### Summary
Creates a formatted performance summary string given key financial metrics, win rate, and goal achievement status, to assist in reporting strategy performance.

### Parameters

- **cumulative_return** (str): The cumulative return of the strategy, represented as a string.
- **sharpe_ratio** (str): The Sharpe ratio indicating risk-adjusted return, represented as a string.
- **max_drawdown** (str): The maximum observed drawdown, represented as a string.
- **win_rate** (str): The win rate percentage of trades, represented as a string.
- **meets_goals** (str): Indicator whether the strategy meets performance goals, represented as a string ('Yes'/'No').

### Returns

str: A formatted string summarizing the performance metrics and goal achievement status for reporting purposes.

### Raises

- ValueError: Raised if any input parameter is not of type str.
- TypeError: Raised if any input parameter is missing or of an incorrect type.

### Examples

```python
>>> create_performance_summary('0.25', '1.2', '-0.15', '60%', 'Yes')
'Performance Summary: Cumulative Return: 0.25, Sharpe Ratio: 1.2, Max Drawdown: -0.15, Win Rate: 60%, Meets Goals: Yes.'
```

```python
>>> create_performance_summary('0.10', '0.8', '-0.20', '55%', 'No')
'Performance Summary: Cumulative Return: 0.10, Sharpe Ratio: 0.8, Max Drawdown: -0.20, Win Rate: 55%, Meets Goals: No.'
```
