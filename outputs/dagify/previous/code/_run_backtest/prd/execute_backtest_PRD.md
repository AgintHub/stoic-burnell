# execute_backtest PRD

## Description
This shim executes a backtest of a trading strategy given environment setup, cleaned data, and configuration parameters, returning performance metrics.


## Conceptual Info

This shim encapsulates the complex process of running a backtest across configured environments, applying strategies, and calculating performance metrics, serving as a bridge between setup and analysis.

## Docstring

### Summary
Executes a backtest of a trading strategy based on provided environment setup, cleaned data, and configuration parameters, returning performance metrics as a JSON string.

### Parameters

- **setup_backtest_environment_input** (SetupBacktestEnvironmentOutput): Object containing environment configuration such as backtesting framework, data adapters, simulation parameters, and additional configuration.
- **clean_and_prepare_data_input** (CleanAndPrepareDataOutput): Object containing information about data cleaning success, missing values handled, derived fields, and dataset readiness.

### Returns

STR: A JSON-formatted string with performance metrics: cumulative return, Sharpe ratio, max drawdown, and win rate.

### Raises

- ValueError: Raised if input parameters fail validation or required fields are missing.
- TypeError: Raised if input parameters are of incorrect types.

### Examples

```python
>>> result = execute_backtest(setup_backtest_environment_input, clean_and_prepare_data_input)
>>> print(result)
'{"cumulative_return": 0.15, "sharpe_ratio": 1.2, "max_drawdown": 0.05, "win_rate": 0.6}'
```

```python
>>> result = execute_backtest(env_config, cleaned_data)
>>> print(result)
'{"cumulative_return": 0.25, "sharpe_ratio": 1.5, "max_drawdown": 0.03, "win_rate": 0.65}'
```
