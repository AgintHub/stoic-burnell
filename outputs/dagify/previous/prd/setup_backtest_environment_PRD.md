# setup_backtest_environment PRD

## Description
Configures a comprehensive backtesting environment for trading strategies, integrating data adapters, simulation parameters, configuration, and execution metrics.


## Conceptual Info

Sets up the backtesting environment to evaluate trading strategies based on historical data.

## Docstring

### Summary
Establishes a robust backtesting framework for trading strategies, integrating data adapters, simulation parameters, configuration, and execution metrics.

### Parameters

- **backtesting_framework** (str): Type of backtesting framework to use (e.g., Zipline, backtrader)
- **data_adapters** (List[str]): Chosen data adapters for backtesting
- **simulation_parameters** (PrimitiveType.DICT): Simulation parameters object, including start and end dates, initial capital, frequency.
- **configuration** (PrimitiveType.DICT): Backtesting framework configuration object.

### Returns

PrimitiveType.DICT: Configuration dictionary with details about the backtesting environment.

### Raises

- Exception: Raised when setup fails due to configuration conflicts or missing dependencies.
