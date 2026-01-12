# determine_optimal_database_type PRD

## Description
This shim determines the most appropriate database type based on data source volumes and characteristics for optimal storage configuration.


## Conceptual Info

This shim analyzes data source volumes and criteria to recommend the most suitable database type for storage efficiency and performance.

## Docstring

### Summary
Determines the optimal database type for data storage based on volume estimates and data source attributes.

### Parameters

- **data_sources** (str): A string (or serialized representation) containing information about data sources relevant for evaluation.
- **volume_estimates** (str): A string (or serialized format) representing volume estimates and related metrics used to decide the database type.

### Returns

str: The name of the chosen database type suitable for the analyzed data sources, such as 'relational', 'NoSQL', or 'time-series'.

### Raises

- ValueError: Raised if input data sources or volume estimates are invalid or improperly formatted.
- TypeError: Raised if input parameters are not of the expected string type.

### Examples

```python
>>> determine_optimal_database_type('"data_source_1, data_source_2"', '"volume_estimate data"')
'relational'
```

```python
>>> determine_optimal_database_type('"sensor_data"', '"high_volume"')
'time-series'
```
