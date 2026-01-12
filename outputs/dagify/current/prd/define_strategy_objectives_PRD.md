# define_strategy_objectives PRD

## Description
Specify the main financial and operational goals for the high-volume options trading strategy. Produce concrete numeric and categorical targets that downstream nodes (data sourcing, repository setup, risk controls) will use.


## Conceptual Info

Set quantifiable financial and operational targets for a high-volume options trading strategy so downstream components (data sourcing, repository structure, risk controls) can be aligned to measurable objectives. This node converts business constraints and risk appetite into a compact set of outputs: target annual return, acceptable volatility, maximum drawdown, liquidity requirement, and market scope.

## Docstring

### Summary
Determine concrete financial and operational objectives for a high-volume options trading strategy. Transforms business inputs (risk appetite, capital, trading frequency, constraints) into standardized strategy targets used by downstream pipeline components.

### Parameters

- **desired_return** (float | None): Optional business target for annual return (%) the firm hopes to achieve (e.g., 20.0 for 20%). If None, the function will propose a target consistent with risk_profile and market_scope.
- **risk_profile** (str): High-level risk appetite: one of {'low', 'medium', 'high'}. Influences acceptable volatility and maximum drawdown settings.
- **liquidity_preference** (str | None): Optional categorical liquidity requirement: 'high', 'medium', or 'low'. If None, liquidity will be inferred from trading frequency and market_scope.
- **market_scope_input** (str | None): Optional market universe hint (e.g., 'US options on large-cap equities', 'global equities', 'currencies'). If None, default to 'US options on liquid underlying' for high-volume strategies.
- **initial_capital** (float | None): Optional starting capital (USD). Useful to calibrate liquidity needs and position sizing; if omitted, outputs remain in percentage/ categorical terms.

### Returns

dict: A dictionary with keys: 'target_annual_return' (float), 'acceptable_volatility' (float), 'maximum_drawdown' (float), 'liquidity_requirements' (str), 'market_scope' (str). Percentages are expressed as numeric values (e.g., 20.0 for 20%).

### Raises

- ValueError: If risk_profile is not one of {'low','medium','high'} or liquidity_preference is invalid.
- TypeError: If numeric inputs are of incorrect type (e.g., non-float for desired_return or initial_capital).

### Examples

```python
>>> define_strategy_objectives(
...     desired_return=20.0,
...     risk_profile='medium',
...     liquidity_preference='high',
...     market_scope_input='US options on large-cap equities',
...     initial_capital=5_000_000.0
>>> )
{
  'target_annual_return': 20.0,
  'acceptable_volatility': 12.0,
  'maximum_drawdown': 25.0,
  'liquidity_requirements': 'high',
  'market_scope': 'US options on large-cap equities'
}
```

```python
>>> define_strategy_objectives(
...     desired_return=None,
...     risk_profile='low',
...     liquidity_preference=None,
...     market_scope_input=None,
...     initial_capital=None
>>> )
{
  'target_annual_return': 8.0,
  'acceptable_volatility': 6.0,
  'maximum_drawdown': 12.0,
  'liquidity_requirements': 'high',
  'market_scope': 'US options on liquid large-cap equities'
}
```
