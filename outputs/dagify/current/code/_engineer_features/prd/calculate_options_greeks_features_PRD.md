# calculate_options_greeks_features PRD

## Description
Calculates the greeks features for a given options data.


## Conceptual Info

This shim node calculates the greeks features for a given options data, which is then used to engineer features for the strategy.

## Docstring

### Summary
Calculates the greeks features for a given options data.

### Parameters

- **data** (str): The input options data as a string.

### Returns

List[str]: The greeks features as a list of strings.

### Raises

- ValueError: When the input data is invalid or incomplete.
- TypeError: When the input data is not a string.

### Examples

```python
>>> from pydantic import BaseModel
>>> from typing import List
>>> class CleanAndPrepareDataOutput(BaseModel):
...     # ...
>>> data_input = CleanAndPrepareDataOutput(...)
>>> greeks_features = calculate_options_greeks_features(data_input.data)
'['delta', 'gamma', 'theta', 'vega', 'rho']'
```
