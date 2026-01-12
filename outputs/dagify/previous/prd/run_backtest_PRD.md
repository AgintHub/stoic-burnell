# run_backtest PRD

## Description
Perform the strategy backtest.


## Conceptual Info

This node performs a backtest of a trading strategy using prepared data and strategy logic.

## Docstring

### Summary
Executes a backtest of a trading strategy and returns key performance metrics.

### Parameters

- **backtest_environment** (dict): Backtesting environment setup, including framework, data adapters, and simulation parameters.
- **prepared_data** (dict): Prepared data for the backtest, including cleaned and feature-engineered datasets.
- **strategy_logic** (dict): Strategy logic, including entry and exit rules, position sizing, and risk limits.

### Returns

dict: Dictionary containing key performance metrics: cumulative_return, sharpe_ratio, max_drawdown, win_rate.

### Raises

- Exception: If there is an error in the backtest environment setup or strategy logic.

### Examples

```python
>>> backtest_env = {'framework': 'Zipline', 'data_adapter': 'CSV', 'simulation_params': {'start_date': '2020-01-01', 'end_date': '2020-12-31'}}
>>> prepared_data = {'cleaned_dataset': ..., 'feature_engineered_dataset': ...}
>>> strategy_logic = {'entry_rule': ..., 'exit_rule': ..., 'position_sizing': ...}
>>> run_backtest(backtest_env, prepared_data, strategy_logic)
{'cumulative_return': 0.2, 'sharpe_ratio': 1.5, 'max_drawdown': 0.1, 'win_rate': 0.6}
```
