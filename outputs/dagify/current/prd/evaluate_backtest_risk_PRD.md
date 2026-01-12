# evaluate_backtest_risk PRD

## Description
Evaluate risk metrics from the backtest.


## Conceptual Info

This node evaluates the risk metrics of a backtest, including volatility, tail risk, position concentration, and liquidity impact.

## Docstring

### Summary
Evaluates risk metrics from the backtest returns.

### Parameters

- **backtest_returns** (float): The returns of the backtest.

### Returns

{ volatility: float, value_at_risk: float, expected_shortfall: float, max_drawdown: float, tail_risk: List[float], position_concentration: float, liquidity_impact: float }: A dictionary containing the risk metrics of the backtest.

### Raises

- ValueError: If the backtest returns are not provided or are empty.

### Examples

```python
>>> backtest_returns = [0.01, 0.02, -0.03, 0.04, -0.05]; evaluate_backtest_risk(backtest_returns)
{'volatility': 0.035, 'value_at_risk': -0.04, 'expected_shortfall': -0.045, 'max_drawdown': 0.06, 'tail_risk': [-0.05, -0.04], 'position_concentration': 0.5, 'liquidity_impact': 0.01}
```
