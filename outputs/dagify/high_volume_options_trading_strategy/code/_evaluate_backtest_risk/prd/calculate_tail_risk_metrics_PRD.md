# calculate_tail_risk_metrics PRD

## Description
A typed node for shim calculate_tail_risk_metrics that computes and returns tail risk metrics.


## Conceptual Info

This shim calculates tail risk metrics for a backtest data set.

## Docstring

### Summary
Calculates and returns tail risk metrics for a given backtest data set.

### Parameters

- **backtest_data** (PrimitiveType.STR): Input backtest data in string format.
- **quantiles** (PrimitiveType.STR): Input quantiles in string format.

### Returns

PrimitiveType.LIST_FLOAT: List of tail risk metrics, including e.g., 1% and 5% quantile returns.

### Raises

- ValueError: If the input backtest data or quantiles are invalid.
- TypeError: If the input types are incorrect.

### Examples

```python
>>> shim_function('example_backtest_data', 'example_quantiles')
['expected_output_metric_1', 'expected_output_metric_2']
```

```python
>>> shim_function('another_backtest_data', 'another_quantiles')
['another_output_metric_1', 'another_output_metric_2']
```
