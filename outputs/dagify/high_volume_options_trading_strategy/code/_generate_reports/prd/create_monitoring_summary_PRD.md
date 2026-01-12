# create_monitoring_summary PRD

## Description
A comprehensive function that generates a monitoring summary for a given dashboard design, alert rules, alert channels, key metrics, and threshold values.


## Conceptual Info

This shim function plays a crucial role in generating a comprehensive monitoring summary based on user input, enabling effective risk monitoring and management.

## Docstring

### Summary
Generates a monitoring summary with a comprehensive string output containing input parameters and user-configured settings.

### Parameters

- **dashboard_design** (str): The monitoring dashboard design to use.
- **alert_rules** (str): The alert rules to apply for monitoring.
- **alert_channels** (str): The alert channels to send notifications to.
- **key_metrics** (str): The key metrics to focus on for monitoring.
- **threshold_values** (str): The threshold values to use for monitoring alerts.

### Returns

str: A string representing the generated monitoring summary.

### Raises

- ValueError: Raised if the input parameters do not match the expected formats or are invalid.

### Examples

```python
>>> monitoring_summary = create_monitoring_summary(dashboard_design='design1',
...   alert_rules=['rule1', 'rule2'],
...   alert_channels=['channel1', 'channel2'],
...   key_metrics=['metric1', 'metric2'],
...   threshold_values=[100, 200])
Monitoring Summary:
design1
rule1, rule2
channel1, channel2
metric1, metric2
100, 200
```
