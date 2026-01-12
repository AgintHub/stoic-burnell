# determine_var_constraints PRD

## Description
This shim function determines variable constraints such as VaR and ES thresholds based on current and expected risk metrics.


## Conceptual Info

This shim computes variable constraints including VaR and Expected Shortfall thresholds based on current risk metrics and tolerance parameters, supporting risk management decision-making.

## Docstring

### Summary
Calculates variable constraints for risk control based on current metrics, expected shortfall, and tolerance constraints.

### Parameters

- **current_var** (str): Current Value-at-Risk (VaR) metric as a string representation.
- **expected_shortfall** (str): Expected Shortfall (ES) metric as a string representation.
- **tolerance_constraints** (str): String representing tolerance parameters for constraints.

### Returns

list_float: A list of float values representing the computed variable constraints such as VaR and ES thresholds.

### Raises

- ValueError: Raised if input strings cannot be parsed into numeric values or if constraints cannot be determined.
- TypeError: Raised if input parameters are not of type str.

### Examples

```python
>>> determine_var_constraints('0.05', '0.10', 'default_tolerance')
[0.05, 0.10]
```

```python
>>> determine_var_constraints('0.02', '0.08', 'custom_tolerance')
[0.02, 0.08]
```
