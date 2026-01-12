# compute_stop_loss_thresholds PRD

## Description
A shim function that calculates stop-loss thresholds based on tail risk, max drawdown, and tolerance parameters.


## Conceptual Info

This shim computes stop-loss threshold values for assets based on tail risk metrics, maximum drawdown, and specified tolerances to support risk management in trading strategies.

## Docstring

### Summary
This function calculates stop-loss thresholds based on tail risk metrics, maximum drawdown, and tolerance parameters to aid in risk management decisions.

### Parameters

- **tail_risk** (str): String representing the type or level of tail risk (e.g., '1%', '5%').
- **max_drawdown** (str): String indicating the maximum drawdown threshold (e.g., '10%').
- **tolerance_thresholds** (str): String encoding the tolerance thresholds for stop-loss calculations, possibly in JSON or comma-separated format.

### Returns

LIST_FLOAT: A list of floating-point numbers representing the calculated stop-loss thresholds for each asset.

### Raises

- ValueError: Raised if input strings are improperly formatted or contain invalid values.
- TypeError: Raised if any input is not of type str.

### Examples

```python
>>> compute_stop_loss_thresholds('1%', '10%', '0.05, 0.1, 0.15')
[0.05, 0.1, 0.15]
```

```python
>>> compute_stop_loss_thresholds('5%', '15%', '0.02, 0.03')
[0.02, 0.03]
```
