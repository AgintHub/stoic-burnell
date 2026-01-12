# calculate_value_at_risk PRD

## Description
This shim computes the Value-at-Risk (VaR) for backtest return data at a specified confidence level.


## Conceptual Info

The shim calculates the Value-at-Risk (VaR) metric to assess potential loss levels under adverse conditions in backtest data.

## Docstring

### Summary
Computes the Value-at-Risk (VaR) for given backtest return data at a specified confidence level.

### Parameters

- **backtest_data** (str): A string representing serialized or formatted backtest data, including returns for risk calculation.
- **confidence_level** (str): A string indicating the confidence level (e.g., '0.95' or '95%') at which to calculate VaR.

### Returns

float: The numerical Value-at-Risk (VaR) value corresponding to the specified confidence level.

### Raises

- ValueError: Raised if the input data is invalid or cannot be parsed properly for computation.
- TypeError: Raised if the input parameters are of incorrect types.

### Examples

```python
>>> calculate_value_at_risk(backtest_data='some serialized data', confidence_level='0.95')
0.025
```

```python
>>> calculate_value_at_risk(backtest_data='another data format', confidence_level='0.99')
0.045
```
