# calculate_position_limits PRD

## Description
This shim computes asset position limits based on risk metrics and tolerances, facilitating risk-aware portfolio management.


## Conceptual Info

The shim derives position limits for assets using risk metrics such as volatility, maximum drawdown, and concentration, considering specified tolerances to ensure risk-managed allocations.

## Docstring

### Summary
Calculates asset position limits based on risk indicators and tolerances to support risk-aware portfolio sizing.

### Parameters

- **volatility** (str): A string parameter representing the asset return volatility metric, potentially as a numerical value or descriptive label.
- **max_drawdown** (str): A string parameter capturing the maximum drawdown measure, indicating downturn severity, in a format suitable for interpretation.
- **concentration** (str): A string indicating the level of position concentration, possibly as a numeric or categorical descriptor.
- **tolerance_limits** (str): A string encoding the tolerances for position limits, such as thresholds or bounds, to be applied during calculation.

### Returns

list_float: A list of float values representing the calculated position limits for each asset based on the input risk metrics and tolerances.

### Raises

- ValueError: Raised if input parameters are invalid, missing, or improperly formatted.
- TypeError: Raised if input parameters are of incorrect types, ensuring they conform to expected string formats.

### Examples

```python
>>> calculate_position_limits(volatility='0.2', max_drawdown='0.3', concentration='high', tolerance_limits='[0.05, 0.1]')
[0.05, 0.1, 0.07, 0.08]
```

```python
>>> calculate_position_limits(volatility='low', max_drawdown='0.15', concentration='medium', tolerance_limits='[0.02, 0.04]')
[0.02, 0.04, 0.03, 0.035]
```
