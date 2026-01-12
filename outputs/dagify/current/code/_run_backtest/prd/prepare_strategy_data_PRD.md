# prepare_strategy_data PRD

## Description
This shim prepares strategy data to be used in a backtest, given a list of data adapters and the cleaned data.


## Conceptual Info

The `prepare_strategy_data` shim prepares strategy data by combining cleaned data and data adapters, and returns the prepared data as a string.

## Docstring

### Summary
Prepare strategy data from cleaned data and data adapters.

### Parameters

- **data_adapters** (LIST_STR): List of data adapters used in the strategy data preparation.
- **cleaned_data** (STR): Cleaned data used in the strategy data preparation.

### Returns

STR: Strategy data ready for backtesting in string format, including data adapters and cleaned data.

### Raises

- ValueError: When input data adapters or cleaned data are invalid or missing.
- TypeError: When input data adapters or cleaned data are of incorrect types.

### Examples

```python
>>> data_adapters = ['CSV', 'database connection']
>>> cleaned_data = 'cleaned_data.csv'
>>> output = prepare_strategy_data(data_adapters, cleaned_data)
'Strategy data prepared with data adapters CSV and database connection, and cleaned data cleaned_data.csv.'
```

```python
>>> data_adapters = ['Pandas', 'database connection']
>>> cleaned_data = 'cleaned_data.csv'
>>> output = prepare_strategy_data(data_adapters, cleaned_data)
'Strategy data prepared with data adapters Pandas and database connection, and cleaned data cleaned_data.csv.'
```
