# fetch_household_expenditure_data PRD

## Description
Gather and consolidate US household expenditure data from official statistical sources into a normalized CSV format for downstream inflation index calculation and analysis.


## Conceptual Info

This node bootstraps the entire alternative inflation workflow by discovering, downloading, and harmonizing US household expenditure data (e.g., from the Consumer Expenditure Survey) across all available years into a single, schema-consistent CSV string. It abstracts away source-specific complexities so that downstream nodes can treat the data as a uniform panel of Year–Category–Location–Expenditure_Amount records.

## Docstring

### Summary
Fetch, normalize, and consolidate US household expenditure data from official sources into a single CSV suitable for inflation index construction and breakdown analyses.

### Returns

dict[str, object]: Dictionary with consolidated CSV data and a success flag.

Keys
----
expenditure_csv : str
    A single CSV string containing household expenditure records harmonized across all available years.
    The minimal required schema is::

        Year,Category,Location,Expenditure_Amount
        2005,Housing,Northeast,12345.67
        2005,Food,Midwest,2345.89
        ...

    Where:
    * ``Year`` is a four-digit integer year.
    * ``Category`` is a normalized expenditure category label (e.g., 'Housing', 'Food', 'Transportation').
    * ``Location`` is a normalized household location descriptor (e.g., Census region, division, or metro/non-metro).
    * ``Expenditure_Amount`` is a numeric value representing annual household expenditure in inflation-unadjusted currency units.

is_data_successful : bool
    Indicates whether the data fetch and consolidation workflow completed without critical errors. Must be ``True`` for downstream nodes to rely on ``expenditure_csv``.

### Raises

- ConnectionError: If official data sources (e.g., BLS Consumer Expenditure Survey endpoints or bulk download servers) are unreachable, time out, or return HTTP errors during retrieval.
- ValueError: If downloaded datasets cannot be aligned to the required schema (missing essential fields like year, category, location, or expenditure; or irreconcilable category/location codings).
- RuntimeError: If no valid expenditure records are obtained after processing all available sources/years, or if the final consolidated dataset is empty.
- CSVError: If an internal CSV serialization error occurs while converting cleaned tabular data into a single CSV text blob.

### Examples

```python
>>> result = fetch_household_expenditure_data()
>>> result.keys()
dict_keys(['expenditure_csv', 'is_data_successful'])
```

```python
>>> result = fetch_household_expenditure_data()
>>> print(result['is_data_successful'])
>>> print('\n'.join(result['expenditure_csv'].splitlines()[:5]))
True
Year,Category,Location,Expenditure_Amount
2005,Housing,Northeast,12345.67
2005,Food,Northeast,4567.89
2005,Transportation,Midwest,2345.10
2005,Healthcare,South,1678.45
```
