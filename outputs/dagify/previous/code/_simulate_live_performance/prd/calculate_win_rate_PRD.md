# calculate_win_rate PRD

## Description
This shim computes the win rate of a trading strategy based on simulated trading results within a larger financial modeling system.


## Conceptual Info

This shim calculates the win rate of a trading strategy from simulation results, essential for evaluating strategy performance.

## Docstring

### Summary
Calculate and return the win rate of a trading strategy based on simulation data, ensuring the data is valid and correctly formatted.

### Parameters

- **simulation_results** (str): A string representing the serialized results of a trading simulation, from which the win rate will be extracted.

### Returns

float: A float value representing the win rate (percentage of winning trades) of the strategy.

### Raises

- ValueError: Raised if simulation_results does not contain the necessary structure or if the win rate cannot be determined.
- TypeError: Raised if the input simulation_results is not a string.

### Examples

```python
>>> calculate_win_rate('''{"trades": [{"result": "win"}, {"result": "loss"}, {"result": "win"}]}''')
0.6666666666666666
```

```python
>>> calculate_win_rate('''{"trades": [{"result": "loss"}, {"result": "loss"}]}''')
0.0
```
