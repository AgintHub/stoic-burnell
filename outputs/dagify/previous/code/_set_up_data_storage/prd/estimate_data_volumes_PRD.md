# estimate_data_volumes PRD

## Description
This shim node estimates the data volumes for given data sources and their frequencies to support data storage planning.


## Conceptual Info

This shim estimates the data volumes for specified data sources based on their frequencies to facilitate subsequent database and storage design decisions.

## Docstring

### Summary
This function estimates the data volumes for input data sources based on their usage frequencies, serving as a critical step for storage planning and database design.

### Parameters

- **data_sources** (str): A string representing the list of validated data source identifiers, typically in JSON format or semicolon-separated.
- **frequencies** (str): A string indicating the data frequency categories (e.g., 'real-time', '1min', '1day') aligned with each data source.

### Returns

str: A JSON-formatted string representing a dictionary where keys are data source names and values are their estimated data volumes (e.g., in GB).

### Raises

- ValueError: Raised if input data sources or frequencies are improperly formatted or contain invalid data.
- TypeError: Raised if input parameters are not strings.

### Examples

```python
>>> estimate_data_volumes('source1;source2', 'real-time;1day')
{'source1': 500, 'source2': 300}
```

```python
>>> estimate_data_volumes('sensorA;sensorB', '1min;1hour')
{'sensorA': 50, 'sensorB': 200}
```
