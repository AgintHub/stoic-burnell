# engineer_features PRD

## Description
Create the feature set for strategy signals.


## Conceptual Info

This node generates a set of features relevant to options trading strategies, including implied volatility, Greeks, moneyness, time-to-expiration, and market sentiment indicators.

## Docstring

### Summary
Engineers features for options trading strategy signals.

### Parameters

- **cleaned_data** (pandas.DataFrame): Cleaned and prepared dataset for feature engineering.

### Returns

dict: {feature_list: List of feature names., feature_formulas: Formulas or descriptions for each feature., feature_descriptions: Descriptions of each feature.}

### Raises

- ValueError: If the input dataset is not properly prepared.

### Examples

```python
>>> import pandas as pd
>>> data = pd.DataFrame({'underlying_price': [100], 'strike_price': [105], 'time_to_expiration': [30]})
>>> features = engineer_features(data)
{'feature_list': ['implied_volatility', 'delta', 'gamma'], 'feature_formulas': ['Black-Scholes formula', ' Greeks formula'], 'feature_descriptions': ['Implied volatility of the option', 'Rate of change of the option price with respect to the underlying price']}
```
