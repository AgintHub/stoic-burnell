# calculate_value_at_risk PRD

## Description
This shim computes the Value-at-Risk (VaR) of a trading strategy based on simulation results to quantify potential losses.


## Conceptual Info

This shim estimates the VaR metric from simulation data to assess potential risk exposure of a trading strategy.

## Docstring

### Summary
Calculates the Value-at-Risk (VaR) of a trading strategy from simulation results for risk management purposes.

### Parameters

- **simulation_results** (str): A string containing serialized or summarized simulation results for the trading strategy.

### Returns

float: A float representing the estimated value at risk, indicating potential losses at a specified confidence level.

### Raises

- ValueError: Raised if the simulation_results input is empty, improperly formatted, or invalid.
- TypeError: Raised if the input is not of type str.

### Examples

```python
>>> result_str = '{"losses": [1000, 2000, 3000], "confidence": 0.95}'
>>> value_at_risk = calculate_value_at_risk(result_str)
>>> print(value_at_risk)
2500.0
```

```python
>>> simulation_data = 'invalid format'
>>> calculate_value_at_risk(simulation_data)
ValueError: Invalid simulation results format
```
