# format_monitoring_alerts PRD

## Description
This shim function formats monitoring dashboard design details and alert configurations into a structured report and alert list for system monitoring.


## Conceptual Info

The shim consolidates monitoring dashboard design details and alert settings into a structured report and alert list for effective system monitoring.

## Docstring

### Summary
Formats monitoring dashboard design and alert configuration parameters into a list of alert descriptions and configurations for monitoring purposes.

### Parameters

- **alert_rules** (str): Serialized string representing the alert rules for key metrics.
- **alert_channels** (str): Serialized string representing the alert channels (e.g., email, SMS, webhook) for notifications.
- **key_metrics** (str): Serialized string listing the key metrics to monitor (e.g., PnL, risk limits, system health).
- **threshold_values** (str): Serialized string of threshold values for each key metric to trigger alerts.

### Returns

str: A list of formatted alert configurations and descriptions based on input parameters.

### Raises

- ValueError: Raised if input strings are invalid or improperly formatted.
- TypeError: Raised if input parameters are not strings.

### Examples

```python
>>> format_monitoring_alerts('rule1, rule2', 'email, sms', 'PnL, risk', 'threshold1, threshold2')
['Alert rule: rule1, Channel: email, Metric: PnL, Threshold: threshold1', 'Alert rule: rule2, Channel: sms, Metric: risk, Threshold: threshold2']
```

```python
>>> format_monitoring_alerts('ruleA', 'webhook', 'system health', 'thresholdA')
['Alert rule: ruleA, Channel: webhook, Metric: system health, Threshold: thresholdA']
```
