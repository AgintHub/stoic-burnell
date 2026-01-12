# identify_key_metrics PRD

## Description
This shim determines the key metrics to monitor based on risk controls and system requirements within a larger risk management and monitoring framework.


## Conceptual Info

This shim identifies and returns the list of key metrics to be monitored, which are crucial for effective risk oversight and operational awareness within financial or risk management systems.

## Docstring

### Summary
Compute and return the list of key metrics to monitor based on the provided risk control configuration and system parameters.

### Parameters

- **risk_controls** (str): A string representing specific risk control metrics or rules to guide the selection of key metrics.

### Returns

str: A list of strings, each representing a key metric identifier or name, that should be monitored for risk and operational performance.

### Raises

- ValueError: Raised if 'risk_controls' is not provided or is invalid, indicating missing or malformed risk control configuration.
- TypeError: Raised if 'risk_controls' is not of type str, indicating an incorrect input type.

### Examples

```python
>>> identify_key_metrics('comprehensive risk controls enabled')
["PnL", "risk_limits", "system_health", "liquidity"]
```

```python
>>> identify_key_metrics('volume-based risk rules')
["trade_volume", "market_volatility", "margin_usage"]
```
