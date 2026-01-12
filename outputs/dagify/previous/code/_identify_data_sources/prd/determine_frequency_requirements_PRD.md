# determine_frequency_requirements PRD

## Description
This shim function determines suitable data frequency requirements based on specified volatility and liquidity constraints for integration into data sourcing workflows.


## Conceptual Info

This shim function evaluates the input volatility and liquidity parameters to output a list of appropriate data frequency requirements for sourcing data in financial strategies.

## Docstring

### Summary
Determine data frequency requirements based on volatility and liquidity constraints, facilitating optimal data sourcing for strategy development.

### Parameters

- **volatility** (str): The acceptable volatility level indicating the risk appetite (e.g., 'low', 'medium', 'high').
- **liquidity** (str): The liquidity requirement reflecting how liquid the data should be ('high', 'medium', 'low').

### Returns

LIST_STR: A list of suitable data frequency strings that meet the specified volatility and liquidity preferences.

### Raises

- ValueError: Raised if the input parameters are invalid or unrecognized strings.
- TypeError: Raised if the input parameters are not of type str.

### Examples

```python
>>> determine_frequency_requirements('medium', 'high')
['realtime', '1min']
```

```python
>>> determine_frequency_requirements('low', 'low')
['1day', '1week']
```
