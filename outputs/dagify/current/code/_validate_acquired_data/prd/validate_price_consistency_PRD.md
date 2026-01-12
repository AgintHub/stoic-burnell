# validate_price_consistency PRD

## Description
This shim function checks the consistency and validity of price data from specified data sources within the larger data validation workflow.


## Conceptual Info

The shim assess the consistency of price data from given data sources to ensure data integrity within the validation pipeline.

## Docstring

### Summary
Validate the consistency of price data obtained from specified data sources based on the provided timestamps or data characteristics.

### Parameters

- **data_sources** (str): A string identifier or list representing the sources of price data to be validated.

### Returns

bool: Returns True if the price data from the sources is consistent and passes validation checks; otherwise, False.

### Raises

- ValueError: Raised if the data sources input is invalid or if the validation cannot be performed due to missing or corrupt data.
- TypeError: Raised if the input data_sources parameter is not of type str.

### Examples

```python
>>> validate_price_consistency('data_source_name')
True
```

```python
>>> validate_price_consistency('invalid_source')
False
```
