# design_risk_controls PRD

## Description
Set up live risk management safeguards.


## Conceptual Info

This node sets up live risk management safeguards by creating risk control rules that enforce position limits, VaR constraints, and stop-loss thresholds during live trading.

## Docstring

### Summary
Design risk controls for live trading by setting position limits, VaR constraints, and stop-loss thresholds.

### Parameters

- **backtest_risk_metrics** (dict): Risk metrics from the backtest, including volatility, value_at_risk, expected_shortfall, max_drawdown, tail_risk, position_concentration, and liquidity_impact.

### Returns

dict: A dictionary containing the position limits, VaR constraints, stop-loss thresholds, risk control rules, and a boolean indicating whether the risk control rules are satisfied.

### Raises

- ValueError: If the input risk metrics are invalid or incomplete.

### Examples

```python
>>> backtest_risk_metrics = {
...     'volatility': 0.1,
...     'value_at_risk': 0.05,
...     'expected_shortfall': 0.03,
...     'max_drawdown': 0.2,
...     'tail_risk': [0.01, 0.005],
...     'position_concentration': 0.5,
...     'liquidity_impact': 0.1
>>> }
>>> design_risk_controls(backtest_risk_metrics)
{'position_limits': [1000.0, 500.0], 'var_constraints': [0.05, 0.03], 'stop_loss_thresholds': [0.1, 0.05], 'risk_control_rules': ['rule1', 'rule2'], 'is_risk_control_satisfied': True}
```
