# load_trading_strategy PRD

## Description
This shim loads a trading strategy based on provided strategy parameters within a larger trading backtest framework.


## Conceptual Info

This shim retrieves or constructs a trading strategy configuration based on input parameters for use in backtesting or live trading.

## Docstring

### Summary
Loads a trading strategy based on provided strategy parameters; required to be implemented to parse and instantiate strategy data from parameters.

### Parameters

- **strategy_params** (str): A string containing serialized or configuration-based parameters that define the trading strategy to load.

### Returns

str: A string representing the loaded trading strategy, suitable for execution within the backtest engine.

### Raises

- ValueError: Raised if strategy_params is invalid or cannot be parsed into a strategy.
- TypeError: Raised if strategy_params is not of type str.

### Examples

```python
>>> strategy_str = load_trading_strategy('{"type": "mean_reversion", "parameters": {"window": 20}}')
'strategy_representation_string_or_object'
```

```python
>>> strategy_str = load_trading_strategy('default_strategy_params')
'strategy_representation_string_or_object'
```
