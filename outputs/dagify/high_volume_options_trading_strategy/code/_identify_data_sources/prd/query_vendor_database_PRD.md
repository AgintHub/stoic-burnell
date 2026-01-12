# query_vendor_database PRD

## Description
Retrieves the list of vendors matching the market and frequency requirements.


## Conceptual Info

This shim retrieves vendors based on market and frequency requirements to support data sourcing for a strategy.

## Docstring

### Summary
This function takes market and frequency requirements as inputs and returns the list of matching vendors.

### Parameters

- **market_requirements** (str): Market requirements to filter vendors.
- **frequency_requirements** (str): Frequency requirements to filter vendors.

### Returns

LIST_STR: List of vendors matching both market and frequency requirements.

### Raises

- ValueError: Raised when input validation fails.
- TypeError: Raised when input types are incorrect.

### Examples

```python
>>> market_requirements = 'high_market' and 'low_frequency';"
              "frequency_requirements = 'low_market' and 'high_frequency';"
              "output = query_vendor_database(market_requirements, frequency_requirements);
['Vendor 1', 'Vendor 2']
```

```python
>>> market_requirements = 'global_market' and 'real_time_frequency';"
              "frequency_requirements = 'us_market' and 'daily_frequency';"
              "output = query_vendor_database(market_requirements, frequency_requirements);
[]
```
