# setup_backtest_environment PRD

## Description
Prepare the backtesting platform.


## Conceptual Info

This node sets up the backtesting environment for a trading strategy.

## Docstring

### Summary
Sets up a backtesting framework with specified configuration, data adapters, and simulation parameters.

### Parameters

- **strategy_logic** (dict): The decision rules of the strategy, including entry signals, exit rules, position sizing, and risk limits.
- **backtesting_framework** (str): The name of the backtesting framework to use (e.g., Zipline, backtrader).
- **data_adapters** (List[str]): List of data adapters to use for the backtest (e.g., CSV, database connections).
- **simulation_parameters** (str): Simulation parameters such as start and end dates, initial capital, and frequency.
- **configuration** (str): Any additional configuration details for the backtesting framework.

### Returns

dict: A dictionary containing the backtesting framework used, data adapters, simulation parameters, configuration, and setup success status.

### Raises

- ValueError: If the backtesting framework is not supported or if there is an issue with the configuration.

### Examples

```python
>>> setup_backtest_environment(strategy_logic={'entry_signals': ['SMA crossover']}, backtesting_framework='Zipline', data_adapters=['CSV'], simulation_parameters={'start_date': '2020-01-01', 'end_date': '2020-12-31'}, configuration={'initial_capital': 10000})
{'backtesting_framework': 'Zipline', 'data_adapters': ['CSV'], 'simulation_parameters': {'start_date': '2020-01-01', 'end_date': '2020-12-31'}, 'configuration': {'initial_capital': 10000}, 'is_setup_successful': True}
```
