# calculate_best_performance_metric PRD

## Description
This shim computes the optimal performance metric value based on optimization results obtained from evaluating backtest performance and risk, facilitating strategy selection.


## Conceptual Info

This shim evaluates optimization results to identify the highest or most suitable performance metric value for strategy assessment.

## Docstring

### Summary
Calculates the best performance metric from the optimization results based on performance and risk evaluations.

### Parameters

- **results** (str): A string representing the results object containing optimization output details.

### Returns

float: A float indicating the optimal performance metric value derived from the optimization results.

### Raises

- ValueError: Raised if the results input is invalid or cannot be parsed properly.
- TypeError: Raised if the results input is not of the expected type string.

### Examples

```python
>>> best_metric = calculate_best_performance_metric(results='{" + '"some', 'validation": "data"}' + "')
0.89
```

```python
>>> best_metric = calculate_best_performance_metric(results='{"result": "best", "metric": 0.95}')
0.95
```
