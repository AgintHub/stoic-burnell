# evaluate_backtest_risk PRD

## Description
Evaluate risk metrics from the backtest.


## Conceptual Info

Evaluates risk metrics from a backtest, including volatility, tail risk, position concentration, and liquidity impact.

## Docstring

### Summary
Evaluates risk metrics from the backtest returns.

### Parameters

- **backtest_returns** (List[float]): The returns of the backtest.

### Returns

dict: A dictionary containing risk metrics: volatility, value_at_risk, expected_shortfall, max_drawdown, tail_risk, position_concentration, liquidity_impact.

### Raises

- ValueError: If backtest_returns is empty.

### Examples

```python
>>> backtest_returns = [0.01, 0.02, -0.03, 0.04, -0.05]
>>> evaluate_backtest_risk(backtest_returns)
{'volatility': 0.035, 'value_at_risk': -0.04, 'expected_shortfall': -0.045, 'max_drawdown': 0.05, 'tail_risk': [-0.1, -0.05], 'position_concentration': 0.2, 'liquidity_impact': 0.01}
```
