# merge_risk_and_custom_thresholds PRD

## Description
A shim function that consolidates various risk limits, constraints, stop-loss thresholds, and custom thresholds into a unified list of thresholds for monitoring and alerting purposes.


## Conceptual Info

This shim function merges various risk control parameters—such as position limits, VaR constraints, stop-loss thresholds, and custom thresholds—into a single list of thresholds used for risk assessment and automated alerting mechanisms.

## Docstring

### Summary
This function consolidates multiple risk parameters and custom thresholds into a single list of thresholds for monitoring and alerting, ensuring all relevant risk limits are effectively managed.

### Parameters

- **risk_limits** (str): A string representing serialized or encoded position limit data for each asset.
- **var_constraints** (str): A string representing serialized or encoded VaR constraint data for each asset.
- **stop_loss_thresholds** (str): A string representing serialized or encoded stop-loss threshold data for each asset.
- **custom_thresholds** (str): A string representing serialized or encoded custom thresholds provided by the user.

### Returns

LIST_FLOAT: A list of floating-point numbers representing the merged thresholds for risk monitoring.

### Raises

- ValueError: Raised if input strings cannot be properly parsed into their respective numerical threshold values.
- TypeError: Raised if any of the inputs are not of type str.

### Examples

```python
>>> merged_thresholds = merge_risk_and_custom_thresholds(
...     risk_limits='[0.1, 0.2, 0.3]',
...     var_constraints='[0.05, 0.1, 0.15]',
...     stop_loss_thresholds='[0.2, 0.25, 0.3]',
...     custom_thresholds='[0.05, 0.1, 0.2]'
>>> )
[0.1, 0.2, 0.3, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.05, 0.1, 0.2]
```

```python
>>> merged_thresholds = merge_risk_and_custom_thresholds(
...     risk_limits='[0.05, 0.1]',
...     var_constraints='[0.02, 0.04]',
...     stop_loss_thresholds='[0.1, 0.15]',
...     custom_thresholds='[0.01, 0.02]'
>>> )
[0.05, 0.1, 0.02, 0.04, 0.1, 0.15, 0.01, 0.02]
```
