# define_market_scope PRD

## Description
This shim determines the appropriate market scope string based on the provided constraints and market analysis data, facilitating targeted market strategy development.


## Conceptual Info

This shim generates a market scope designation based on market constraints and liquidity analysis to support strategic decisions.

## Docstring

### Summary
Constructs a market scope string based on market constraints and analysis data, ensuring alignment with regulatory, data, and trading considerations.

### Parameters

- **constraints** (str): A string or structured data outlining regulatory requirements, data availability, and trading hours constraints.
- **liquidity_analysis** (str): A string summarizing the market liquidity analysis, including bid-ask spreads, volumes, and execution needs.

### Returns

str: A string indicating the finalized market scope, such as 'US stocks', 'EU bonds', or 'forex'.

### Raises

- ValueError: Raised if input parameters are invalid or cannot be mapped to a valid market scope.
- TypeError: Raised if input parameters are not of the expected string type.

### Examples

```python
>>> final_scope = define_market_scope('regulatory_compliant=True, data_access=True, trading_hours=9-17', 'high_liquidity, tight_spreads')
'US stocks'
```

```python
>>> final_scope = define_market_scope('regulatory_compliant=False', 'low_liquidity, high_volatility')
'Emerging Markets'
```
