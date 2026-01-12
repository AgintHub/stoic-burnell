# _generate_reports - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_reports' module.

## Table of Contents

- [create_performance_summary](#create_performance_summary)

- [create_risk_assessment_summary](#create_risk_assessment_summary)

- [create_monitoring_summary](#create_monitoring_summary)

- [format_strengths_weaknesses](#format_strengths_weaknesses)

- [compile_comprehensive_report](#compile_comprehensive_report)

- [extract_performance_metrics](#extract_performance_metrics)

- [format_monitoring_alerts](#format_monitoring_alerts)



---

## create_performance_summary

### Description
Generates a comprehensive textual performance summary based on key financial metrics and strategy evaluations.

### Conceptual Info

This shim constructs a detailed performance summary string from individual financial metrics and evaluation results to facilitate reporting and analysis.

### Docstring

**Summary:** Creates a formatted performance summary string given key financial metrics, win rate, and goal achievement status, to assist in reporting strategy performance.

**Parameters:**

- cumulative_return (str): The cumulative return of the strategy, represented as a string.
- sharpe_ratio (str): The Sharpe ratio indicating risk-adjusted return, represented as a string.
- max_drawdown (str): The maximum observed drawdown, represented as a string.
- win_rate (str): The win rate percentage of trades, represented as a string.
- meets_goals (str): Indicator whether the strategy meets performance goals, represented as a string ('Yes'/'No').
**Returns:** str - A formatted string summarizing the performance metrics and goal achievement status for reporting purposes.

**Raises:**

- ValueError: Raised if any input parameter is not of type str.
- TypeError: Raised if any input parameter is missing or of an incorrect type.
**Examples:**

```python
>>> create_performance_summary('0.25', '1.2', '-0.15', '60%', 'Yes')
'Performance Summary: Cumulative Return: 0.25, Sharpe Ratio: 1.2, Max Drawdown: -0.15, Win Rate: 60%, Meets Goals: Yes.'
```

```python
>>> create_performance_summary('0.10', '0.8', '-0.20', '55%', 'No')
'Performance Summary: Cumulative Return: 0.10, Sharpe Ratio: 0.8, Max Drawdown: -0.20, Win Rate: 55%, Meets Goals: No.'
```



---

## create_risk_assessment_summary

### Description
Generates a comprehensive risk assessment summary report based on multiple risk metrics provided as inputs.

### Conceptual Info

This shim constructs a detailed risk assessment summary report from individual risk metrics such as volatility, VaR, expected shortfall, tail risk, concentration, and liquidity impact, integrating them into a structured overview for further reporting or analysis.

### Docstring

**Summary:** This function creates a comprehensive risk assessment summary report by combining various risk metrics provided as string inputs, facilitating consistent and formatted reporting of risk factors.

**Parameters:**

- volatility (str): A string representing the annualized volatility of the backtest returns.
- var (str): A string representing the Value-at-Risk (VaR) at a specified confidence level.
- expected_shortfall (str): A string representing the Expected Shortfall (ES) at a specified confidence level.
- tail_risk (str): A string describing tail risk metrics or quantile return measures, typically summarizing potential extreme losses.
- concentration (str): A string indicating the position concentration metric (e.g., Herfindahl-Hirschman Index).
- liquidity_impact (str): A string assessing the estimated liquidity impact, such as price impact or slippage.
**Returns:** str - A formatted string encapsulating the combined risk metrics into a structured summary report.

**Raises:**

- ValueError: Raised if any input string contains invalid or unparseable data that prevents proper report formatting.
- TypeError: Raised if any of the inputs are not of type str.
**Examples:**

```python
>>> create_risk_assessment_summary(
...     volatility='0.25',
...     var='-0.10',
...     expected_shortfall='-0.15',
...     tail_risk='5%, 1%',
...     concentration='0.25',
...     liquidity_impact='0.02'
>>> )
'Risk Assessment Report:\n- Volatility: 0.25\n- Value at Risk: -0.10\n- Expected Shortfall: -0.15\n- Tail Risk (5%, 1%): 5%, 1%\n- Position Concentration: 0.25\n- Liquidity Impact: 0.02\n'
```

```python
>>> create_risk_assessment_summary(
...     volatility='high',
...     var='-0.05',
...     expected_shortfall='-0.07',
...     tail_risk='3%, 0.5%',
...     concentration='0.30',
...     liquidity_impact='0.05'
>>> )
'Risk Assessment Report:\n- Volatility: high\n- Value at Risk: -0.05\n- Expected Shortfall: -0.07\n- Tail Risk (3%, 0.5%): 3%, 0.5%\n- Position Concentration: 0.30\n- Liquidity Impact: 0.05\n'
```



---

## create_monitoring_summary

### Description
A comprehensive function that generates a monitoring summary for a given dashboard design, alert rules, alert channels, key metrics, and threshold values.

### Conceptual Info

This shim function plays a crucial role in generating a comprehensive monitoring summary based on user input, enabling effective risk monitoring and management.

### Docstring

**Summary:** Generates a monitoring summary with a comprehensive string output containing input parameters and user-configured settings.

**Parameters:**

- dashboard_design (str): The monitoring dashboard design to use.
- alert_rules (str): The alert rules to apply for monitoring.
- alert_channels (str): The alert channels to send notifications to.
- key_metrics (str): The key metrics to focus on for monitoring.
- threshold_values (str): The threshold values to use for monitoring alerts.
**Returns:** str - A string representing the generated monitoring summary.

**Raises:**

- ValueError: Raised if the input parameters do not match the expected formats or are invalid.
**Examples:**

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



---

## format_strengths_weaknesses

### Description
This shim creates a structured string summary of the strategy's strengths and weaknesses for reporting purposes.

### Conceptual Info

This shim generates a coherent text summary combining the provided strengths and weaknesses of a trading strategy for inclusion in reports and documentation.

### Docstring

**Summary:** This function formats the given strengths and weaknesses strings into a structured summary suitable for reporting and presentation.

**Parameters:**

- strengths (str): A string listing the strengths of the strategy, typically separated by commas or newline characters.
- weaknesses (str): A string listing the weaknesses of the strategy, typically separated by commas or newline characters.
**Returns:** str - A formatted, coherent string that combines the strengths and weaknesses for easy inclusion in comprehensive reports.

**Raises:**

- ValueError: Raised if either 'strengths' or 'weaknesses' is not a string or is empty when improper context is detected.
- TypeError: Raised if the inputs are not of type str.
**Examples:**

```python
>>> format_strengths_weaknesses('Strong analytical capabilities, Good risk management', 'Limited scalability, High dependency on market conditions')
'Strengths include: Strong analytical capabilities, Good risk management. Weaknesses include: Limited scalability, High dependency on market conditions.'
```

```python
>>> format_strengths_weaknesses('Advanced modeling skills', 'Potential overfitting')
'Strengths include: Advanced modeling skills. Weaknesses include: Potential overfitting.'
```



---

## compile_comprehensive_report

### Description
Generates a comprehensive report by combining performance, risk, and monitoring sections.

### Conceptual Info

The shim generates a consolidated report by combining performance, risk, and monitoring sections for a comprehensive analysis.

### Docstring

**Summary:** Compile a comprehensive report from performance, risk, and monitoring sections.

**Parameters:**

- performance_section (str): A summary of the performance metrics, including cumulative return, Sharpe ratio, and max drawdown.
- risk_section (str): A summary of the risk assessment, including volatility, VaR, and ES.
- monitoring_section (str): A description of the monitoring dashboard design, alert rules, and key metrics.
- strengths_weaknesses_section (str): A list of strengths and weaknesses of the strategy.
**Returns:** str - The compiled comprehensive report as a string, combining the input sections.

**Raises:**

- ValueError: If input values are invalid or incomplete.
- TypeError: If input types are incorrect.
**Examples:**

```python
>>> compile_comprehensive_report(performance_section='performance summary', risk_section='risk summary', monitoring_section='monitoring summary', strengths_weaknesses_section='strengths and weaknesses')
The compiled comprehensive report.
```

```python
>>> compile_comprehensive_report(performance_section='updated performance summary', risk_section='updated risk summary', monitoring_section='updated monitoring summary', strengths_weaknesses_section='updated strengths and weaknesses')
The updated compiled comprehensive report.
```



---

## extract_performance_metrics

### Description
This shim function extracts key performance metrics from the evaluation backtest performance input object.

### Conceptual Info

This shim extracts a list of relevant performance metric names from the provided evaluation data object, facilitating downstream reporting and analysis.

### Docstring

**Summary:** Extracts and returns a list of key performance metrics from the input object containing backtest performance data.

**Parameters:**

- performance_input (str): String identifier or description referencing the evaluation backtest performance input object.
**Returns:** str - A list of strings representing the names of performance metrics extracted from the input.

**Raises:**

- TypeError: Raised if 'performance_input' is not a string.
- ValueError: Raised if 'performance_input' does not contain expected data or keys.
**Examples:**

```python
>>> metrics = extract_performance_metrics(evaluate_backtest_performance_input)
>>> print(metrics)
['meets_performance_goals', 'cumulative_return', 'sharpe_ratio', 'max_drawdown', 'win_rate', 'strengths', 'weaknesses']
```

```python
>>> metrics = extract_performance_metrics('performance_data')
>>> print(metrics)
['meets_performance_goals', 'cumulative_return', 'sharpe_ratio', 'max_drawdown', 'win_rate', 'strengths', 'weaknesses']
```



---

## format_monitoring_alerts

### Description
This shim function formats monitoring dashboard design details and alert configurations into a structured report and alert list for system monitoring.

### Conceptual Info

The shim consolidates monitoring dashboard design details and alert settings into a structured report and alert list for effective system monitoring.

### Docstring

**Summary:** Formats monitoring dashboard design and alert configuration parameters into a list of alert descriptions and configurations for monitoring purposes.

**Parameters:**

- alert_rules (str): Serialized string representing the alert rules for key metrics.
- alert_channels (str): Serialized string representing the alert channels (e.g., email, SMS, webhook) for notifications.
- key_metrics (str): Serialized string listing the key metrics to monitor (e.g., PnL, risk limits, system health).
- threshold_values (str): Serialized string of threshold values for each key metric to trigger alerts.
**Returns:** str - A list of formatted alert configurations and descriptions based on input parameters.

**Raises:**

- ValueError: Raised if input strings are invalid or improperly formatted.
- TypeError: Raised if input parameters are not strings.
**Examples:**

```python
>>> format_monitoring_alerts('rule1, rule2', 'email, sms', 'PnL, risk', 'threshold1, threshold2')
['Alert rule: rule1, Channel: email, Metric: PnL, Threshold: threshold1', 'Alert rule: rule2, Channel: sms, Metric: risk, Threshold: threshold2']
```

```python
>>> format_monitoring_alerts('ruleA', 'webhook', 'system health', 'thresholdA')
['Alert rule: ruleA, Channel: webhook, Metric: system health, Threshold: thresholdA']
```

