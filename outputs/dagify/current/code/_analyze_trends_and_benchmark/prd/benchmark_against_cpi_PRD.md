# benchmark_against_cpi PRD

## Description
Compares inflation rates against a Consumer Price Index (CPI) baseline to provide benchmarking results.


## Conceptual Info

The benchmark_against_cpi shim function provides a comparison of inflation rates against a Consumer Price Index (CPI) baseline, generating benchmarking results that can be used for trend analysis and decision-making.

## Docstring

### Summary
Compares inflation rates against a Consumer Price Index (CPI) baseline to provide benchmarking results.

### Parameters

- **inflation_rates** (str): A string representation of a list of inflation rates as percent changes.
- **years** (str): A string representation of a list of years corresponding to the inflation rates.
- **cpi_data** (str): A string representation of the CPI data used as a baseline for benchmarking.

### Returns

str: A dictionary containing benchmarking results, including comparisons of inflation rates against the CPI baseline.

### Raises

- ValueError: When input validation fails due to incorrect or missing data.
- TypeError: When input types are incorrect or incompatible with expected formats.

### Examples

```python
>>> benchmark_against_cpi(inflation_rates='[0.02, 0.03, 0.01]', years='[2020, 2021, 2022]', cpi_data='{'2020': 100, '2021': 105, '2022': 110}')
{'benchmarking_results': [1.05, 1.02, 0.95], 'comparison_summary': 'Inflation rates are 5% higher than CPI in 2020, 2% higher in 2021, and 5% lower in 2022'}
```
