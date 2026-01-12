# calculate_target_annual_return PRD

## Description
A shim function that computes the target annual return of a trading strategy based on backtesting results, compounding, and transaction costs.


## Conceptual Info

This shim calculates the target annual return of the strategy based on backtesting data, considering compounding and transaction costs, to inform strategic decision-making.

## Docstring

### Summary
Compute the target annual return of a trading strategy from backtesting results, factoring in compounding and transaction costs.

### Parameters

- **backtesting_results** (STR): A string encoding the backtesting outcomes, which should include relevant performance metrics for return calculation.
- **compounding_factor** (STR): A string indicating whether the return should account for compounding effects ('True' or 'False').
- **transaction_costs** (STR): A string indicating if transaction costs are included ('True' or 'False') in the calculation.

### Returns

FLOAT: The target annual return as a float, representing the strategy's expected yearly performance.

### Raises

- ValueError: Raised if necessary data is missing or cannot be parsed from the input string.
- TypeError: Raised if the input parameters are of incorrect types or formatted improperly.

### Examples

```python
>>> calculate_target_annual_return('backtest results data', 'True', 'True')
0.18
```

```python
>>> calculate_target_annual_return('results', 'False', 'False')
0.12
```
