# design_monitoring_and_alerts PRD

## Description
Configure operational oversight.


## Conceptual Info

Designs monitoring dashboards and alert systems for operational oversight.

## Docstring

### Summary
Configures operational oversight by designing monitoring dashboards and alert rules for key metrics.

### Parameters

- **risk_controls** (dict): Risk control rules and settings from design_risk_controls node

### Returns

{ monitoring_dashboard_design: str, alert_rules: List[str], alert_channels: List[str], key_metrics: List[str], threshold_values: List[float] }: Configuration for monitoring dashboards and alerts

### Raises

- ValueError: If risk_controls is not provided or is invalid

### Examples

```python
>>> design_monitoring_and_alerts({
...   'position_limits': [1000.0],
...   'var_constraints': [0.05],
...   'stop_loss_thresholds': [0.1]
>>> })
{'monitoring_dashboard_design': 'PnL and risk dashboard', 'alert_rules': ['PnL < -1000', 'VaR > 0.05'], 'alert_channels': ['email', 'SMS'], 'key_metrics': ['PnL', 'VaR'], 'threshold_values': [-1000.0, 0.05]}
```
