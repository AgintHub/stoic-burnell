# build_decision_tree PRD

## Description
This shim generates a high-level decision tree process description based on specified trading signals, rules, position sizing, and risk limits.


## Conceptual Info

This shim constructs a comprehensive decision tree summary that encapsulates entry signals, exit rules, position sizing, and risk limits to facilitate strategic analysis and optimization.

## Docstring

### Summary
Constructs a detailed decision tree overview for a trading strategy based on provided signals, rules, sizing, and risk parameters.

### Parameters

- **entry_signals** (str): A string detailing the conditions or criteria for entering trades.
- **exit_rules** (str): A string outlining the conditions under which trades should be exited.
- **position_sizing** (str): A string indicating the method used to determine trade sizes, such as fixed amount or risk-based sizing.
- **risk_limits** (str): A string specifying the risk constraints or limits, such as stop-loss or take-profit levels.

### Returns

str: A string summarizing the decision logic or providing a visual/hierarchical representation of the trading decision process.

### Raises

- ValueError: Raised if any of the input strings are invalid or improperly formatted.
- TypeError: Raised if any input parameters are not of type str.

### Examples

```python
>>> build_decision_tree(
...     entry_signals='If RSI < 30 then buy',
...     exit_rules='If profit > 5% then exit',
...     position_sizing='Risk-based',
...     risk_limits='Stop-loss at 2%'
>>> )
'Decision Tree: Enter when RSI < 30; Exit on 5% profit or stop-loss at 2%; Position sizing risk-based.'
```

```python
>>> build_decision_tree(
...     entry_signals='Price crosses above moving average',
...     exit_rules='Price crosses below moving average',
...     position_sizing='Fixed size',
...     risk_limits='Max loss of $1000'
>>> )
'Decision Tree: Enter on price crossing above moving average; Exit on crossing below; Fixed position size; Max loss $1000.'
```
