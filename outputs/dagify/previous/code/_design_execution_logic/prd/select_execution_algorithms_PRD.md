# select_execution_algorithms PRD

## Description
This shim determines the appropriate execution algorithms based on trading signals, exit rules, and position sizing strategies to support order execution decision-making.


## Conceptual Info

The shim selects appropriate execution algorithms based on trading signals, exit rules, and position sizing to guide order execution strategies.

## Docstring

### Summary
Determines the list of execution algorithms to use based on entry signals, exit rules, and position sizing strategies, providing configuration for order execution modules.

### Parameters

- **entry_signals** (str): A string detailing conditions or signals for initiating trades, which influence algorithm selection.
- **exit_rules** (str): A string defining conditions for exiting trades, used to refine algorithm choices.
- **position_sizing** (str): A string indicating the strategy for determining trade size, affecting algorithm selection.

### Returns

list of str: A list of execution algorithm names suitable for the current trading scenario.

### Raises

- ValueError: Raised if input parameters are invalid or cannot be processed properly.
- TypeError: Raised if input parameters are of incorrect types.

### Examples

```python
>>> select_execution_algorithms(
...     entry_signals='Momentum, Breakout',
...     exit_rules='StopLoss, TakeProfit',
...     position_sizing='RiskBased'
>>> )
['TWAP', 'VWAP']
```

```python
>>> select_execution_algorithms(
...     entry_signals='MeanReversion',
...     exit_rules='TimeStop',
...     position_sizing='Fixed'
>>> )
['Market', 'Limit']
```
