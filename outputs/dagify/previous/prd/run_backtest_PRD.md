# run_backtest PRD

## Description
Perform the strategy backtest.


## Conceptual Info

This node performs a backtest of a trading strategy using prepared data and strategy logic.

## Docstring

### Summary
Executes a backtest of a trading strategy and returns key performance metrics.

### Parameters

- **backtesting_environment** (dict): Backtesting environment setup, including framework, data adapters, and simulation parameters.
- **prepared_data** (pandas.DataFrame): Prepared data for the backtest, including features and target variables.
- **strategy_logic** (function): Strategy logic defining entry and exit rules, position sizing, and risk management.

### Returns

dict: Dictionary containing key performance metrics: cumulative return, Sharpe ratio, max drawdown, and win rate.

### Raises

- ValueError: If the backtesting environment is not properly set up or if the strategy logic is invalid.

### Examples

```python
>>> backtesting_environment = {'framework': 'Zipline', 'data_adapters': ['CSV'], 'simulation_parameters': {'start_date': '2020-01-01', 'end_date': '2020-12-31'}}
>>> prepared_data = pd.read_csv('prepared_data.csv')
>>> strategy_logic = lambda x: x > 0
>>> run_backtest(backtesting_environment, prepared_data, strategy_logic)
{'cumulative_return': 0.1, 'sharpe_ratio': 1.2, 'max_drawdown': 0.05, 'win_rate': 0.6}
```
