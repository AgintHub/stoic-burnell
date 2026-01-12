# engineer_features PRD

## Description
Create the feature set for strategy signals.


## Conceptual Info

This node generates a set of features relevant to options trading strategies, including implied volatility, Greeks, moneyness, time-to-expiration, and market sentiment indicators.

## Docstring

### Summary
Engineers features for options trading strategy signals.

### Parameters

- **cleaned_data** (pd.DataFrame): Cleaned and prepared dataset for feature engineering.

### Returns

dict: {feature_list: List of feature names., feature_formulas: List of formulas or descriptions for each feature., feature_descriptions: List of descriptions for each feature.}

### Raises

- ValueError: If the input dataset is not suitable for feature engineering.

### Examples

```python
>>> import pandas as pd
>>> cleaned_data = pd.DataFrame({'open': [1.0, 2.0], 'close': [1.1, 2.1]})
>>> features = engineer_features(cleaned_data)
{'feature_list': ['implied_volatility', 'delta'], 'feature_formulas': ['IV = ...', 'Δ = ...'], 'feature_descriptions': ['Implied volatility of the option.', 'Delta of the option.']}
```
