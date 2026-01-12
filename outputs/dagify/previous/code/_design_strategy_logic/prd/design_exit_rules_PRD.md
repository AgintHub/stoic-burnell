# design_exit_rules PRD

## Description
This shim extracts and formulates exit rules for trading strategies based on the specified framework and entry signals.


## Conceptual Info

The shim generates exit rules for a trading strategy given a framework and entry signals, facilitating strategy automation.

## Docstring

### Summary
Generates a list of exit rule conditions based on the provided framework and entry signals for trading strategy development.

### Parameters

- **framework** (str): A string identifier or detailed description of the trading framework used for generating rules.
- **entry_signals** (str): A string detailing the entry signals already defined, which influence the exit rule formulation.

### Returns

list of str: A list of exit rule conditions expressed as string conditions.

### Raises

- ValueError: Raised if the framework or entry_signals are invalid, missing, or improperly formatted.
- TypeError: Raised if the input types are not strings.

### Examples

```python
>>> rules = design_exit_rules(framework='TrendFollowing', entry_signals='Price > MovingAverage')
['Price crosses below MovingAverage', 'Price falls below support level']
```

```python
>>> exit_conditions = design_exit_rules(framework='MomentumStrategy', entry_signals='RSI > 70')
['RSI drops below 70', 'Price shows divergence']
```
