# generate_reports PRD

## Description
Produce a final performance and risk report.


## Conceptual Info

This node generates a comprehensive report summarizing backtest results, risk assessment, and live simulation outputs.

## Docstring

### Summary
Generate a comprehensive report summarizing backtest results, risk assessment, and live simulation outputs.

### Parameters

- **backtest_performance** (dict): Backtest performance metrics from evaluate_backtest_performance
- **backtest_risk** (dict): Backtest risk assessment from evaluate_backtest_risk
- **monitoring_alerts_config** (dict): Monitoring alerts configuration from design_monitoring_and_alerts

### Returns

dict: A dictionary containing the report in Markdown format, performance metrics, risk assessment, and monitoring alerts

### Raises

- ValueError: If any of the input parameters are missing or invalid

### Examples

```python
>>> backtest_performance = {'cumulative_return': 0.1, 'sharpe_ratio': 1.5}
>>> backtest_risk = {'volatility': 0.05, 'value_at_risk': 0.03}
>>> monitoring_alerts_config = {'alert_rules': ['rule1', 'rule2']}
>>> generate_reports(backtest_performance, backtest_risk, monitoring_alerts_config)
{report_markdown: # Performance Report

* Cumulative Return: 10%
* Sharpe Ratio: 1.5, performance_metrics: [cumulative_return: 10%, sharpe_ratio: 1.5], risk_assessment: Volatility: 5%, Value-at-Risk: 3%, monitoring_alerts: [rule1, rule2]}
```
