# generate_historical_timeline PRD

## Description
Generate a historical timeline CSV by combining the index series with category and location expenditure breakdowns on a per-year basis.


## Conceptual Info

This node generates a historical timeline by combining index series data with category and location expenditure breakdowns.

## Docstring

### Summary
Generate a historical timeline CSV by combining index series data with category and location expenditure breakdowns.

### Parameters

- **index_series** (dict): Dictionary containing index series data with keys 'years' and 'index_values'.
- **category_breakdowns** (dict): Dictionary containing category breakdown data with keys 'category_spending_csv' and 'is_breakdown_successful'.
- **location_breakdowns** (dict): Dictionary containing location breakdown data with keys 'location_spending_csv' and 'is_breakdown_successful'.

### Returns

tuple: A tuple containing the historical timeline CSV string and a boolean flag indicating success.

### Raises

- ValueError: If input data is missing or malformed.

### Examples

```python
>>> index_series = {'years': [2020, 2021], 'index_values': [100.0, 105.0]}
>>> category_breakdowns = {'category_spending_csv': 'Year,Category,Total\n2020,Food,1000\n2021,Food,1100', 'is_breakdown_successful': True}
>>> location_breakdowns = {'location_spending_csv': 'Year,Location,Total\n2020,Urban,500\n2021,Urban,550', 'is_breakdown_successful': True}
>>> generate_historical_timeline(index_series, category_breakdowns, location_breakdowns)
'Year,Index,CategoryTotals,LocationTotals\n2020,100.0,1000,500\n2021,105.0,1100,550', True
```
