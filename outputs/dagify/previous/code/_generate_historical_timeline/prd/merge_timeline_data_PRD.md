# merge_timeline_data PRD

## Description
Combines index data, category totals, and location totals into a unified timeline data structure.


## Conceptual Info

The merge_timeline_data shim function integrates data from different sources (index series, category breakdowns, and location breakdowns) into a cohesive timeline. This timeline is crucial for generating historical reports and analyses.

## Docstring

### Summary
Merges index data, category totals, and location totals into a unified timeline data structure.

### Parameters

- **index_by_year** (dict): Dictionary containing index values organized by year.
- **category_totals** (dict): Dictionary containing category totals organized by year.
- **location_totals** (dict): Dictionary containing location totals organized by year.

### Returns

list: A list representing the merged timeline data, where each element contains information about a specific year, including its index value, category totals, and location totals.

### Raises

- ValueError: When the input dictionaries (index_by_year, category_totals, location_totals) do not have consistent year ranges.
- TypeError: When the input parameters are not of the expected types (dict for index_by_year, category_totals, and location_totals).

### Examples

```python
>>> merge_timeline_data(index_by_year={2020: 100, 2021: 120}, category_totals={2020: {'A': 50, 'B': 60}, 2021: {'A': 70, 'B': 80}}, location_totals={2020: {'City': 40, 'Town': 30}, 2021: {'City': 50, 'Town': 40}})
[{'Year': 2020, 'Index': 100, 'CategoryTotals': {'A': 50, 'B': 60}, 'LocationTotals': {'City': 40, 'Town': 30}}, {'Year': 2021, 'Index': 120, 'CategoryTotals': {'A': 70, 'B': 80}, 'LocationTotals': {'City': 50, 'Town': 40}}]
```
