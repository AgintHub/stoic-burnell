# design_risk_controls PRD

## Description
Develops and deploys advanced risk management safeguards for live trading by creating data-driven risk control rules, enforcing position limits, Value-at-Risk (VaR) constraints, and stop-loss thresholds.


## Conceptual Info

This node develops and deploys advanced risk management safeguards for live trading by creating data-driven risk control rules.

## Docstring

### Summary
Designs and implements risk management controls for live trading.

### Parameters

- **backtest_risk_metrics** (dict): Input risk metrics from the evaluate_backtest_risk node.
- **risk_tolerance** (dict): Risk tolerance parameters, including position limits, VaR constraints, and stop-loss thresholds.

### Returns

dict: A set of risk control rules and an indicator of whether they are currently satisfied.

### Raises

- ValueError: Raised if input data is invalid or risk tolerance parameters are contradictory.

### Examples

```python
>>> backtest_risk_metrics = evaluate_backtest_risk().output
>>> risk_tolerance = {'position_limits': [100000, 500000], 'var_constraints': [0.05, 0.10], 'stop_loss_thresholds': [50, 100]}
>>> risk_control_rules, is_risk_control_satisfied = design_risk_controls(backtest_risk_metrics, risk_tolerance)
{'risk_control_rules': ['Position limit 100000 reached on asset A', 'VaR constraint 0.05 exceeded on asset B'], 'is_risk_control_satisfied': False}
```
