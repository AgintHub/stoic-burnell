# generate_alert_rules PRD

## Description
Generates a list of alert rules based on provided metrics, thresholds, and risk control rules.


## Conceptual Info

This shim node plays a key role in the design_monitoring_and_alerts function, responsible for generating alert rules based on provided metrics, thresholds, and risk control rules.

## Docstring

### Summary
Generates a list of alert rules from given metrics, thresholds, and risk control rules.

### Parameters

- **metrics** (List[str]): The list of key metrics to be monitored (e.g., PnL, risk limits, system health).
- **thresholds** (List[float]): The list of threshold values for each key metric.
- **risk_rules** (List[str]): The list of risk control rules to be used for generating alert rules.

### Returns

List[str]: A list of alert rules as strings in the format 'metric: condition > threshold'.

### Raises

- ValueError: Raised when the input validation fails or the metrics and thresholds do not match.
- TypeError: Raised when the input types are incorrect or the risk rules are not a list of strings.

### Examples

```python
>>> generate_alert_rules(metrics=['PnL', 'Risk Limits'], thresholds=[0.05, 0.1], risk_rules=['Risk is high', 'Risk is critical'])
['PnL: condition > 0.05', 'Risk Limits: condition > 0.1']
```
