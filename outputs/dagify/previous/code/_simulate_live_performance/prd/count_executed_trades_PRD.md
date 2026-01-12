# count_executed_trades PRD

## Description
A shim function that retrieves the number of trades executed during a live trading simulation based on provided simulation results.


## Conceptual Info

This shim function extracts and returns the total number of trades executed from the simulation results, facilitating assessment of trading activity during live performance evaluation.

## Docstring

### Summary
Retrieve the number of trades executed in a live trading simulation from the simulation results data.

### Parameters

- **simulation_results** (str): A string representing the detailed results of a live trading simulation, from which the trade count will be extracted.

### Returns

int: An integer representing the total number of trades executed during the simulation.

### Raises

- ValueError: Raised if the simulation_results input is empty, improperly formatted, or does not contain trade data.
- TypeError: Raised if the simulation_results argument is not of type str.

### Examples

```python
>>> count_executed_trades('simulation results string with trade info')
125
```

```python
>>> count_executed_trades('another simulation result string')
87
```
