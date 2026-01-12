# _engineer_features - Complete PRD Documentation

## Overview
PRDs for nodes in the '_engineer_features' module.

## Table of Contents

- [calculate_implied_volatility_features](#calculate_implied_volatility_features)

- [calculate_options_greeks_features](#calculate_options_greeks_features)

- [calculate_moneyness_features](#calculate_moneyness_features)

- [calculate_time_to_expiration_features](#calculate_time_to_expiration_features)

- [calculate_market_sentiment_features](#calculate_market_sentiment_features)

- [combine_feature_lists](#combine_feature_lists)

- [generate_feature_formulas](#generate_feature_formulas)

- [generate_feature_descriptions](#generate_feature_descriptions)



---

## calculate_implied_volatility_features

### Description
This shim generates implied volatility feature names based on the provided data, serving as a key step in feature engineering for options analysis.

### Conceptual Info

This shim extracts and generates a list of implied volatility feature names from the given options data for use in further feature engineering steps.

### Docstring

**Summary:** This function takes options data as input and returns a list of implied volatility feature names, facilitating the integration of implied volatility measures into the feature set.

**Parameters:**

- data (str): A string representing the options data input, which will be processed to extract implied volatility features.
**Returns:** str - A list of implied volatility feature names as strings, generated based on the input data.

**Raises:**

- ValueError: Raised if the input data is invalid or not in the expected format.
- TypeError: Raised if the input data is not a string.
**Examples:**

```python
>>> calculate_implied_volatility_features('option data string')
['implied_vol_1', 'implied_vol_2', 'implied_vol_sigma']
```

```python
>>> calculate_implied_volatility_features('another data string')
['implied_vol_a', 'implied_vol_b']
```



---

## calculate_options_greeks_features

### Description
Calculates the greeks features for a given options data.

### Conceptual Info

This shim node calculates the greeks features for a given options data, which is then used to engineer features for the strategy.

### Docstring

**Summary:** Calculates the greeks features for a given options data.

**Parameters:**

- data (str): The input options data as a string.
**Returns:** List[str] - The greeks features as a list of strings.

**Raises:**

- ValueError: When the input data is invalid or incomplete.
- TypeError: When the input data is not a string.
**Examples:**

```python
>>> from pydantic import BaseModel
>>> from typing import List
>>> class CleanAndPrepareDataOutput(BaseModel):
...     # ...
>>> data_input = CleanAndPrepareDataOutput(...)
>>> greeks_features = calculate_options_greeks_features(data_input.data)
'['delta', 'gamma', 'theta', 'vega', 'rho']'
```



---

## calculate_moneyness_features

### Description
This node generates a list of moneyness-related feature names based on the provided data for use in options strategy modeling.

### Conceptual Info

This shim computes and returns a list of feature names related to option moneyness, which will be used for feature engineering in trading strategies.

### Docstring

**Summary:** Generates a list of moneyness feature names based on the input data, ensuring the features pertain to the current dataset for accurate options analysis.

**Parameters:**

- data (str): A string representing the dataset or context from which moneyness features are derived, typically including relevant option and underlying asset information.
**Returns:** str - A comma-separated string or serialized list containing the names of generated moneyness features.

**Raises:**

- ValueError: Raised when the input data is invalid or missing required fields for moneyness calculation.
- TypeError: Raised when the input data is not of the expected string type.
**Examples:**

```python
>>> calculate_moneyness_features('dataset_with_option_data')
['option_moneyness_ratio', 'strike_price_moneyness', 'underlying_vs_strike']
```



---

## calculate_time_to_expiration_features

### Description
Computes features related to options' time to expiration from the dataset provided.

### Conceptual Info

This shim generates features that quantify the remaining time until options expire, facilitating time-based analyses within the larger options strategy pipeline.

### Docstring

**Summary:** Calculates a list of feature names capturing options' time to expiration based on the input dataset.

**Parameters:**

- data (str): A string identifier or dataset reference that contains relevant options data with expiration date information.
**Returns:** str - A comma-separated string listing feature names related to time to expiration.

**Raises:**

- ValueError: Raised if the input data is invalid or lacks necessary expiration date fields.
- TypeError: Raised if the input parameter is not of type str.
**Examples:**

```python
>>> calculate_time_to_expiration_features('options_data')
'time_to_exp_days,expiring_soon_days,expiration_months_left'
```

```python
>>> calculate_time_to_expiration_features('monthly_options')
'time_to_exp_days,expiring_soon_days,expiration_months_left'
```



---

## calculate_market_sentiment_features

### Description
This shim generates a list of market sentiment feature names based on the input data to be used in feature engineering for financial models.

### Conceptual Info

This shim extracts or computes sentiment-related feature names from the input data to enhance financial model feature sets.

### Docstring

**Summary:** Generate a list of market sentiment feature names based on input data, to be used in feature engineering pipelines.

**Parameters:**

- data (str): A string representing the input data context or dataset identifier containing market sentiment information.
**Returns:** list of str - A list of feature name strings related to market sentiment analysis.

**Raises:**

- ValueError: Raised if the input data string is empty or invalid.
- TypeError: Raised if the input data is not of type str.
**Examples:**

```python
>>> calculate_market_sentiment_features('latest_market_data')
['sentiment_news', 'social_media_sentiment', 'news_sentiment_index']
```

```python
>>> calculate_market_sentiment_features('previous_day_data')
['news_sentiment_index', 'social_media_trends', 'market_mood_score']
```



---

## combine_feature_lists

### Description
This shim function consolidates multiple feature lists into a single comprehensive feature list for downstream use.

### Conceptual Info

This shim aggregates multiple feature name lists into a unified list, enabling streamlined feature management for model training and analysis.

### Docstring

**Summary:** Combine multiple feature lists into a single list of feature names for further processing or model input.

**Parameters:**

- list1 (List[str]): First list of feature names to combine.
- list2 (List[str]): Second list of feature names to combine.
- list3 (List[str]): Third list of feature names to combine.
- list4 (List[str]): Fourth list of feature names to combine.
- list5 (List[str]): Fifth list of feature names to combine.
**Returns:** str - A list of feature names, resulting from concatenating all input lists.

**Raises:**

- TypeError: Raised if any of the inputs is not a list of strings.
**Examples:**

```python
>>> combine_feature_lists(['feat1', 'feat2'], ['feat3'], [], ['feat4', 'feat5'], [])
['feat1', 'feat2', 'feat3', 'feat4', 'feat5']
```

```python
>>> combine_feature_lists([], [], [], [], [])
[]
```



---

## generate_feature_formulas

### Description
This shim function generates feature formulas or descriptions based on a list of feature names, facilitating interpretability and downstream modeling.

### Conceptual Info

This shim generates formulas or descriptive representations for each feature name to aid interpretability and modeling.

### Docstring

**Summary:** The function takes a list of feature names and outputs a corresponding list of feature formulas or descriptions. It requires a list of feature names as input and produces a list of string formulas/descriptions as output. The implementation should generate meaningful formulas or descriptions aligned with each feature name. It should handle invalid inputs appropriately.

**Parameters:**

- feature_names (str): A string representing the list of feature names for which formulas or descriptions need to be generated.
**Returns:** list of str - A list of formulas or descriptive strings corresponding to each feature name provided.

**Raises:**

- ValueError: Raised if the input feature_names is not a string or is improperly formatted.
- TypeError: Raised if the input is not of type str.
**Examples:**

```python
>>> generate_feature_formulas('implied_volatility')
['IV(t) = implied_volatility', or other formula/description associated with 'implied_volatility']
```



---

## generate_feature_descriptions

### Description
This shim creates descriptive text for each feature based on their names within a feature engineering pipeline.

### Conceptual Info

This shim generates informative descriptions for features based on their names to enhance interpretability and documentation.

### Docstring

**Summary:** Generates a list of feature descriptions given a list of feature names to facilitate better understanding and documentation within feature engineering workflows.

**Parameters:**

- feature_names (str): A string representing the name of the feature set for which descriptions are to be generated.
**Returns:** list of str - A list of textual descriptions, each corresponding to a feature name, providing clarifications or summaries of the feature's purpose or calculation.

**Raises:**

- ValueError: Raised if the input feature_names is not a string.
- TypeError: Raised if the input feature_names is of an incorrect type other than string.
**Examples:**

```python
>>> generate_feature_descriptions(feature_names='implied_volatility')
[Calculates implied volatility based on options market data., Returns a descriptive string summarizing implied volatility features.]
```

```python
>>> generate_feature_descriptions(feature_names='moneyness')
[Computes the moneyness ratio of options to identify in-the-money or out-of-the-money states., Provides a brief description of the moneyness feature.]
```

