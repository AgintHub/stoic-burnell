# get_performance_thresholds PRD

## Description
This shim retrieves and returns performance threshold settings used to evaluate backtest performance against desired goals.


## Conceptual Info

The get_performance_thresholds shim fetches configuration parameters that define acceptable performance metrics for strategy evaluation, enabling flexible and configurable assessment criteria.

## Docstring

### Summary
Retrieve and return performance thresholds used to evaluate whether a trading strategy meets predefined goals.

### Parameters

- **kwargs** (dict): Optional keyword arguments specifying configuration options or identifiers for obtaining performance thresholds.

### Returns

str: A string representing a JSON-formatted dictionary with performance threshold parameters such as minimum return, maximum drawdown, minimum Sharpe ratio, and minimum win rate.

### Raises

- ValueError: Raised if the retrieved thresholds are invalid or malformed.
- TypeError: Raised if the returned object is not a string or cannot be serialized to a string.

### Examples

```python
>>> performance_thresholds_str = get_performance_thresholds()
>>> print(performance_thresholds_str)
'{"min_return": 0.05, "max_drawdown": 0.2, "min_sharpe": 1.0, "min_win_rate": 0.55}'
```

```python
>>> thresholds_json = get_performance_thresholds(dashboard_id='abc123')
>>> print(thresholds_json)
'{"min_return": 0.07, "max_drawdown": 0.15, "min_sharpe": 1.2, "min_win_rate": 0.6}'
```
