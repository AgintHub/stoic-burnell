# format_timeline_as_csv PRD

## Description
Formats timeline data into a CSV string with specified headers.


## Conceptual Info

The format_timeline_as_csv shim function takes in timeline data and headers, and returns a formatted CSV string.

## Docstring

### Summary
Formats timeline data into a CSV string with specified headers.

### Parameters

- **timeline_data** (str): The timeline data to be formatted into a CSV string. This should be a list or dictionary that can be converted into a CSV format.
- **headers** (str): The headers for the CSV string. This should be a list of column names.

### Returns

str: The formatted CSV string.

### Raises

- ValueError: When the input timeline data or headers are invalid.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> format_timeline_as_csv(timeline_data=[{'Year': 2020, 'Index': 100, 'CategoryTotals': 1000, 'LocationTotals': 500}],
>>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
"Year,Index,CategoryTotals,LocationTotals\n2020,100,1000,500"
```

```python
>>> format_timeline_as_csv(timeline_data=[{'Year': 2021, 'Index': 120, 'CategoryTotals': 1200, 'LocationTotals': 600}],
>>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
"Year,Index,CategoryTotals,LocationTotals\n2021,120,1200,600"
```
