# evaluate_backtest_risk PRD

## Description
Evaluates the risk metrics of a backtest, including volatility, value-at-risk, expected shortfall, maximum drawdown, tail risk, position concentration, and liquidity impact. This node provides a comprehensive risk report with detailed metrics and visualizations to support strategic decision-making.


## Conceptual Info

Risk Evaluation for Backtesting

## Docstring

### Summary
Evaluates the risk metrics of a backtest, including volatility, value-at-risk, expected shortfall, maximum drawdown, tail risk, position concentration, and liquidity impact.

### Returns

dict: A dictionary containing the calculated risk metrics

### Examples

```python
>>> return evaluate_backtest_risk(backtest_result)
A dictionary with the following structure:

{'volatility': 0.12, 'value_at_risk': 0.05, 'expected_shortfall': 0.03, 'max_drawdown': 0.25, 'tail_risk': [0.01, 0.05], 'position_concentration': 0.8, 'liquidity_impact': 0.05}
```
