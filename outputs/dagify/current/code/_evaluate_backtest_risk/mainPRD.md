# _evaluate_backtest_risk - Complete PRD Documentation

## Overview
PRDs for nodes in the '_evaluate_backtest_risk' module.

## Table of Contents

- [calculate_annualized_volatility](#calculate_annualized_volatility)

- [calculate_value_at_risk](#calculate_value_at_risk)

- [calculate_expected_shortfall](#calculate_expected_shortfall)

- [extract_max_drawdown](#extract_max_drawdown)

- [calculate_tail_risk_metrics](#calculate_tail_risk_metrics)

- [calculate_position_concentration_hhi](#calculate_position_concentration_hhi)

- [estimate_liquidity_impact](#estimate_liquidity_impact)



---

## calculate_annualized_volatility

### Description
Calculates the annualized volatility of a given backtest data.

### Conceptual Info

This shim node calculates the annualized volatility of a backtest data, which is a measure of the overall risk of the investments.

### Docstring

**Summary:** Calculates the annualized volatility of a given backtest data.

**Parameters:**

- backtest_data (str): The data of the backtest returns, represented as a string.
**Returns:** float - The annualized volatility of the backtest returns, represented as a float.

**Raises:**

- ValueError: Raised when the input backtest data is invalid or malformed.
- TypeError: Raised when the input backtest data is not a string.
**Examples:**

```python
>>> backtest_returns = ['0.01', '0.02', '0.03', '0.04', '0.05']
>>> calculate_annualized_volatility(backtest_data=' '.join(backtest_returns))
0.0208
```



---

## calculate_value_at_risk

### Description
This shim computes the Value-at-Risk (VaR) for backtest return data at a specified confidence level.

### Conceptual Info

The shim calculates the Value-at-Risk (VaR) metric to assess potential loss levels under adverse conditions in backtest data.

### Docstring

**Summary:** Computes the Value-at-Risk (VaR) for given backtest return data at a specified confidence level.

**Parameters:**

- backtest_data (str): A string representing serialized or formatted backtest data, including returns for risk calculation.
- confidence_level (str): A string indicating the confidence level (e.g., '0.95' or '95%') at which to calculate VaR.
**Returns:** float - The numerical Value-at-Risk (VaR) value corresponding to the specified confidence level.

**Raises:**

- ValueError: Raised if the input data is invalid or cannot be parsed properly for computation.
- TypeError: Raised if the input parameters are of incorrect types.
**Examples:**

```python
>>> calculate_value_at_risk(backtest_data='some serialized data', confidence_level='0.95')
0.025
```

```python
>>> calculate_value_at_risk(backtest_data='another data format', confidence_level='0.99')
0.045
```



---

## calculate_expected_shortfall

### Description
This shim computes the Expected Shortfall (Conditional VaR) at a specified confidence level based on backtest return data.

### Conceptual Info

The shim calculates the Expected Shortfall (ES) at a given confidence level from backtest return data, providing a measure of tail risk beyond Value-at-Risk.

### Docstring

**Summary:** Calculates the Expected Shortfall (Conditional VaR) at a specified confidence level from backtest data to quantify tail risk.

**Parameters:**

- backtest_data (str): A string identifier or serialized data containing backtest return series, used as input for the calculation.
- confidence_level (str): A string representing the confidence level (e.g., '0.95') at which to compute the Expected Shortfall.
**Returns:** float - The computed Expected Shortfall (ES) as a float value representing the average of losses that exceed the Value-at-Risk at the specified confidence level.

**Raises:**

- ValueError: Raised if the input data is invalid, missing, or cannot be processed to compute Expected Shortfall.
- TypeError: Raised if the input parameters are of incorrect types or improperly formatted.
**Examples:**

```python
>>> expected_shortfall = calculate_expected_shortfall(backtest_data='my_backtest_data', confidence_level='0.95')
0.0345
```

```python
>>> result = calculate_expected_shortfall(backtest_data='data_str', confidence_level='0.99')
0.0452
```



---

## extract_max_drawdown

### Description
A shim that computes the maximum drawdown from backtest data to identify the largest peak-to-trough decline during the period.

### Conceptual Info

This shim computes the maximum drawdown from backtest results to assess risk exposure during the trading period.

### Docstring

**Summary:** This function calculates the maximum drawdown from provided backtest data to quantify the largest peak-to-trough loss.

**Parameters:**

- backtest_data (str): A string representing serialized backtest data or an identifier from which the maximum drawdown can be extracted.
**Returns:** float - The maximum drawdown value indicating the largest percentage decline observed during the backtest period.

**Raises:**

- ValueError: Raised when the input backtest_data is invalid or cannot be parsed.
- TypeError: Raised when backtest_data is not of type str.
**Examples:**

```python
>>> max_dd = extract_max_drawdown('serialized_backtest_result')
>>> print(max_dd)
0.25
```

```python
>>> max_dd = extract_max_drawdown('another_backtest_id')
>>> print(max_dd)
0.15
```



---

## calculate_tail_risk_metrics

### Description
A typed node for shim calculate_tail_risk_metrics that computes and returns tail risk metrics.

### Conceptual Info

This shim calculates tail risk metrics for a backtest data set.

### Docstring

**Summary:** Calculates and returns tail risk metrics for a given backtest data set.

**Parameters:**

- backtest_data (PrimitiveType.STR): Input backtest data in string format.
- quantiles (PrimitiveType.STR): Input quantiles in string format.
**Returns:** PrimitiveType.LIST_FLOAT - List of tail risk metrics, including e.g., 1% and 5% quantile returns.

**Raises:**

- ValueError: If the input backtest data or quantiles are invalid.
- TypeError: If the input types are incorrect.
**Examples:**

```python
>>> shim_function('example_backtest_data', 'example_quantiles')
['expected_output_metric_1', 'expected_output_metric_2']
```

```python
>>> shim_function('another_backtest_data', 'another_quantiles')
['another_output_metric_1', 'another_output_metric_2']
```



---

## calculate_position_concentration_hhi

### Description
Computes the Herfindahl-Hirschman Index (HHI) of position concentration from backtest data to assess portfolio diversification.

### Conceptual Info

This shim calculates the Herfindahl-Hirschman Index (HHI) to quantify the concentration of positions within the backtest data, aiding in risk assessment and portfolio diversification analysis.

### Docstring

**Summary:** Computes the Herfindahl-Hirschman Index (HHI) of position concentration based on provided backtest data. This function requires input data representing a backtest's trading positions and must return a float value indicating the HHI. It raises errors if input data is improperly formatted or missing necessary fields.

**Parameters:**

- backtest_data (str): String representation of the backtest data containing position information used to calculate the HHI.
**Returns:** float - The Herfindahl-Hirschman Index (HHI) value, indicating the level of position concentration (0 to 1).

**Raises:**

- ValueError: Raised if the input data is missing, improperly formatted, or contains invalid position information.
- TypeError: Raised if the input is not of type str.
**Examples:**

```python
>>> calculate_position_concentration_hhi('{"positions": [0.2, 0.3, 0.5]}')
0.58
```

```python
>>> calculate_position_concentration_hhi('{"positions": [0.1, 0.1, 0.8]}')
0.35
```



---

## estimate_liquidity_impact

### Description
Estimates the liquidity impact (e.g., price impact or slippage) of executing a trading strategy based on backtest data.

### Conceptual Info

This shim computes an estimate of the liquidity impact associated with executing a trading strategy using backtest data, aiding in risk assessment and strategy tuning.

### Docstring

**Summary:** Computes an estimate of the strategy's liquidity impact from provided backtest data, intended for risk evaluation and strategy optimization.

**Parameters:**

- backtest_data (str): A serialized string representing the backtest data used to estimate liquidity impact.
**Returns:** float - A floating-point number representing the estimated liquidity impact, such as expected slippage or price movement caused by the strategy execution.

**Raises:**

- ValueError: Raised if the input string is invalid or cannot be parsed into expected backtest data format.
- TypeError: Raised if the input type is not a string.
**Examples:**

```python
>>> estimate_liquidity_impact('serialized backtest data string')
0.025
```

```python
>>> estimate_liquidity_impact('another backtest data string')
0.041
```

