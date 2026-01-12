# select_optimization_method PRD

## Description
Determines and returns the most suitable optimization method based on backtest performance and risk metrics as input.


## Conceptual Info

This shim analyzes backtest performance and risk metrics to select the most appropriate optimization strategy for strategy parameter tuning.

## Docstring

### Summary
Selects the optimal optimization method based on provided performance and risk data for strategy hyperparameter tuning.

### Parameters

- **performance_data** (str): Serialized string representing the backtest performance metrics.
- **risk_data** (str): Serialized string representing the backtest risk metrics.

### Returns

str: The suggested optimization method (e.g., 'grid search', 'Bayesian optimization') as a string.

### Raises

- ValueError: Raised if the input strings are improperly formatted or contain invalid data.
- TypeError: Raised if the inputs are not strings.

### Examples

```python
>>> select_optimization_method('performance_metrics_json', 'risk_metrics_json')
'Bayesian optimization'
```

```python
>>> select_optimization_method('performance_metrics_json', 'risk_metrics_json')
'grid search'
```
