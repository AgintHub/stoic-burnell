# analyze_market_liquidity PRD

## Description
This shim function analyzes market data to produce insights on market liquidity, including bid-ask spreads and daily trading volumes.


## Conceptual Info

This shim analyzes raw market data to extract liquidity metrics that inform trading strategies and risk assessments.

## Docstring

### Summary
Analyze market data to determine liquidity characteristics, including bid-ask spreads and daily volumes, based on provided market data summaries.

### Parameters

- **market_data** (str): A serialized string representing market data loaded from historical or live sources, to be analyzed for liquidity metrics.
- **bid_ask_spreads** (str): A string indicating whether to include bid-ask spread analysis; typically 'True' or 'False'.
- **daily_volumes** (str): A string indicating whether to include daily trading volume analysis; typically 'True' or 'False'.

### Returns

str: A JSON-formatted string encapsulating the results of liquidity analysis, such as calculated bid-ask spreads and daily volumes for the market data provided.

### Raises

- ValueError: Raised if the input strings for analysis flags are not recognizable boolean values or if market_data is invalid.
- TypeError: Raised if the input parameters are not of type str.

### Examples

```python
>>> analyze_market_liquidity('{"market": "NASDAQ", "data": [...] }', 'True', 'True')
{"bid_ask_spread": 0.05, "average_daily_volume": 1000000}
```

```python
>>> analyze_market_liquidity('{"market": "FOREX", "data": [...] }', 'False', 'True')
{"bid_ask_spread": null, "average_daily_volume": 500000}
```
