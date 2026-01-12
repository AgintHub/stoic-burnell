# evaluate_backtest_performance PRD

## Description
Enhanced evaluation of backtest results against predefined performance objectives. Provides a rigorous, transparent, and actionable assessment of how well the strategy performs, including pass/fail determination, key metrics, and guidance for improvements. Maintains strict output shape to ensure downstream nodes can consume the results without additional parsing.


## Conceptual Info

Evaluates backtest results against predefined performance objectives, producing a structured, interpretable assessment that informs decision-making. It handles missing data gracefully, documents limitations, and outputs a consistent schema for downstream consumption.

## Docstring

### Summary
Compute a structured performance assessment from backtest metrics, comparing them to predefined objectives. Return a dictionary conforming to the node's output_structure with diagnostic narrative and improvement guidance.

### Parameters

- **backtest_metrics** (dict): Backtest outputs from run_backtest. Required keys: cumulative_return (float), sharpe_ratio (float), max_drawdown (float), win_rate (float). Optional keys may include annualized_return (float), drawdown_duration (float), etc.
- **objectives** (dict): Performance thresholds guiding the evaluation. Optional; defaults applied if absent. Suggested keys: min_cumulative_return (float), min_sharpe_ratio (float), max_drawdown_allowed (float), min_win_rate (float), benchmark (float, optional), consider_costs (bool, optional).

### Returns

dict: A structured performance assessment with fields matching output_structure: meets_performance_goals, cumulative_return, sharpe_ratio, max_drawdown, win_rate, strengths, weaknesses.

### Raises

- ValueError: Raised if required metrics are missing and cannot be reasonably inferred.

### Examples

```python
>>> def evaluate_backtest_performance(backtest_metrics, objectives=None):
...     # Implementation uses backtest_metrics and thresholds to produce the structured output
{ 'meets_performance_goals': true, 'cumulative_return': 0.18, 'sharpe_ratio': 0.92, 'max_drawdown': -0.22, 'win_rate': 0.45, 'strengths': ['robust uptrends', 'stable drawdown management'], 'weaknesses': ['moderate win rate during sideways markets'] }
```
