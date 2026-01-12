# calculate_maximum_drawdown PRD

## Description
A shim node that computes the maximum drawdown value from stress testing results based on risk appetite and stress scenario analysis.


## Conceptual Info

This shim computes the maximum drawdown metric from stress test results, aiding risk management by quantifying potential peak-to-trough losses under modeled scenarios.

## Docstring

### Summary
Calculates the maximum drawdown value from given stress testing results, considering the specified risk appetite, to quantify the potential largest loss in portfolio value.

### Parameters

- **stress_results** (STR): A string representation of the stress testing results data, expected to contain scenario outcomes and loss metrics.
- **risk_appetite** (STR): A string indicating the risk appetite level ('low', 'moderate', 'high'), which may influence the interpretation of stress results.

### Returns

FLOAT: The maximum drawdown value as a float, representing the largest observed peak-to-trough decline during stress scenarios.

### Raises

- ValueError: Raised if the stress_results input is improperly formatted or missing required data to compute drawdown.
- TypeError: Raised if stress_results is not a string or risk_appetite is not a string.

### Examples

```python
>>> max_drawdown = calculate_maximum_drawdown(stress_results='scenario outcomes data', risk_appetite='moderate')
0.35
```

```python
>>> result = calculate_maximum_drawdown(stress_results='stress data', risk_appetite='high')
0.40
```
