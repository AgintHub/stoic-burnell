# select_backtesting_framework PRD

## Description
This shim selects the appropriate backtesting framework based on the provided strategy logic and available options, facilitating flexible setup of backtest environments.


## Conceptual Info

Determines and returns the most suitable backtesting framework for a given trading strategy based on specified criteria and available options.

## Docstring

### Summary
This function selects the appropriate backtesting framework based on strategy logic and available frameworks, enabling flexible backtest environment configuration.

### Parameters

- **strategy_logic** (str): A string representing the logical strategy instructions or specifications used to determine the suitable backtesting framework.
- **available_frameworks** (str): A comma-separated string of available backtesting framework names (e.g., 'Zipline, backtrader').

### Returns

str: The name of the selected backtesting framework as a string.

### Raises

- ValueError: If no suitable framework can be determined from the strategy logic and available options.
- TypeError: If input parameters are of incorrect types, e.g., non-string inputs.

### Examples

```python
>>> selected_framework = select_backtesting_framework('momentum-based strategy', 'Zipline, backtrader')
'Zipline'
```

```python
>>> result = select_backtesting_framework('mean reversion strategy', 'backtrader')
'backtrader'
```
