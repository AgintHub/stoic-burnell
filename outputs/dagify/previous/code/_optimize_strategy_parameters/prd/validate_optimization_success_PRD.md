# validate_optimization_success PRD

## Description
Validate the success of optimization by comparing the optimized results with the original metrics.


## Conceptual Info

This shim node validates the success of optimization by comparing the optimized results with the original metrics.

## Docstring

### Summary
Validate the success of optimization by comparing the optimized results with the original metrics.

### Parameters

- **results** (str): Details about the optimization results.
- **original_metrics** (str): Original metrics used for optimization.

### Returns

dict: A dictionary with keys 'output' (BOOL), 'results' (STR), and 'original_metrics' (STR) indicating the validation result, optimization details, and original metrics, respectively.

### Raises

- ValueError: When the input validation fails.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> optimization_results = {'optimized_parameters': [...], 'optimization_method': 'grid_search', 'is_optimization_successful': True, 'best_performance_metric': 0.8}
>>> original_metrics = {'cumulative_return': 0.7, 'sharpe_ratio': 0.5, 'max_drawdown': 0.3}
>>> validate_optimization_success(results=optimization_results, original_metrics=original_metrics)
True
```

```python
>>> optimization_results = {'optimized_parameters': [...], 'optimization_method': 'grid_search', 'is_optimization_successful': False, 'best_performance_metric': 0.2}
>>> original_metrics = {'cumulative_return': 0.7, 'sharpe_ratio': 0.5, 'max_drawdown': 0.3}
>>> validate_optimization_success(results=optimization_results, original_metrics=original_metrics)
False
```
