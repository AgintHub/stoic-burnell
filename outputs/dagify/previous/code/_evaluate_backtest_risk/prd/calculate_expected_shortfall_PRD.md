# calculate_expected_shortfall PRD

## Description
This shim computes the Expected Shortfall (Conditional VaR) at a specified confidence level based on backtest return data.


## Conceptual Info

The shim calculates the Expected Shortfall (ES) at a given confidence level from backtest return data, providing a measure of tail risk beyond Value-at-Risk.

## Docstring

### Summary
Calculates the Expected Shortfall (Conditional VaR) at a specified confidence level from backtest data to quantify tail risk.

### Parameters

- **backtest_data** (str): A string identifier or serialized data containing backtest return series, used as input for the calculation.
- **confidence_level** (str): A string representing the confidence level (e.g., '0.95') at which to compute the Expected Shortfall.

### Returns

float: The computed Expected Shortfall (ES) as a float value representing the average of losses that exceed the Value-at-Risk at the specified confidence level.

### Raises

- ValueError: Raised if the input data is invalid, missing, or cannot be processed to compute Expected Shortfall.
- TypeError: Raised if the input parameters are of incorrect types or improperly formatted.

### Examples

```python
>>> expected_shortfall = calculate_expected_shortfall(backtest_data='my_backtest_data', confidence_level='0.95')
0.0345
```

```python
>>> result = calculate_expected_shortfall(backtest_data='data_str', confidence_level='0.99')
0.0452
```
