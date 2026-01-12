# combine_performance_and_risk_metrics PRD

## Description
This shim function combines performance and risk metrics into a unified data structure for use in strategy optimization processes.


## Conceptual Info

This shim function aggregates performance and risk data into a cohesive representation to facilitate strategy evaluation and optimization.

## Docstring

### Summary
Combines performance and risk metrics provided as input objects into a single, structured string representation for downstream analysis.

### Parameters

- **performance** (str): Serialized performance metrics data, typically from evaluate_backtest_performance node
- **risk** (str): Serialized risk metrics data, typically from evaluate_backtest_risk node

### Returns

str: A JSON string encapsulating combined performance and risk metrics for further processing

### Raises

- ValueError: Raised if inputs cannot be parsed or are missing required fields
- TypeError: Raised if input types are not strings

### Examples

```python
>>> performance_data = '{"meets_performance_goals": true, "cumulative_return": 0.15, "sharpe_ratio": 1.2, "max_drawdown": 0.05, "win_rate": 0.6, "strengths": ["robustness"], "weaknesses": ["overfitting"]}'
>>> risk_data = '{"volatility": 0.2, "value_at_risk": -0.05, "expected_shortfall": -0.07, "max_drawdown": 0.1, "tail_risk": [ -0.1, -0.2 ], "position_concentration": 0.25, "liquidity_impact": 0.02}'
>>> combined_metrics = combine_performance_and_risk_metrics(performance=performance_data, risk=risk_data)
>>> print(combined_metrics)
{"performance": {"meets_performance_goals": true, "cumulative_return": 0.15, "sharpe_ratio": 1.2, "max_drawdown": 0.05, "win_rate": 0.6, "strengths": ["robustness"], "weaknesses": ["overfitting"]}, "risk": {"volatility": 0.2, "value_at_risk": -0.05, "expected_shortfall": -0.07, "max_drawdown": 0.1, "tail_risk": [ -0.1, -0.2 ], "position_concentration": 0.25, "liquidity_impact": 0.02}}
```
