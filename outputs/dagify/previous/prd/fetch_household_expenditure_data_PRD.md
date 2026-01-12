# fetch_household_expenditure_data PRD

## Description
Gather and consolidate household expenditure data into a CSV format.


## Conceptual Info

Collects US household expenditure data from official sources, aggregates it across all available years, and outputs a single CSV string that can be consumed by downstream nodes for index construction and breakdown analysis.

## Docstring

### Summary
Retrieves US household expenditure data for all available years from official sources and consolidates it into a single CSV string. The function returns the CSV string along with a boolean flag indicating whether the data retrieval and consolidation succeeded.

### Returns

Tuple[str, bool]: A tuple where the first element is the consolidated CSV string and the second element is a boolean flag signifying success.

### Raises

- ValueError: Raised if the function cannot access any official data source or if the retrieved data is empty.

### Examples

```python
>>> csv_str, success = fetch_household_expenditure_data()
>>> print(success)
>>> print(csv_str.splitlines()[0])
True
Year,Category,Location,Expenditure_Amount
```

```python
>>> csv_str, success = fetch_household_expenditure_data()
>>> if not success:
...     print('Data retrieval failed.')
Data retrieval failed.
```
