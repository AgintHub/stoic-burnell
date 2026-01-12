# calculate_max_drawdown PRD

## Description
This shim function computes and returns the maximum drawdown from provided simulation results to assess the worst-case loss scenario.


## Conceptual Info

Calculates the maximum drawdown from simulation results to evaluate the worst-case loss in strategy performance.

## Docstring

### Summary
This shim function computes the maximum drawdown from simulation results provided as input, enabling risk assessment of trading strategies.

### Parameters

- **simulation_results** (str): A string representation of the simulation results, expected to contain necessary data for max drawdown calculation.

### Returns

float: A floating-point number indicating the maximum drawdown derived from the simulation results.

### Raises

- ValueError: Raised if the simulation_results input is empty or cannot be parsed properly.
- TypeError: Raised if the input is not of type str.

### Examples

```python
>>> calculate_max_drawdown('{"trades": [{"peak": 100, "trough": 80}, {"peak": 120, "trough": 70}]}')
50.0
```

```python
>>> calculate_max_drawdown('{"trades": [{"peak": 200, "trough": 150}]}')
50.0
```
