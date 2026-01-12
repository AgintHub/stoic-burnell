# recommend_cloud_deployment PRD

## Description
Determines whether cloud deployment is recommended based on storage requirements and data sources.


## Conceptual Info

This shim evaluates storage size and data sources to recommend cloud deployment, facilitating decisions on cloud infrastructure use.

## Docstring

### Summary
This function assesses whether cloud deployment is advisable based on the estimated data storage size and relevant data sources.

### Parameters

- **storage_size** (str): A string representing the estimated size of data storage needed, typically formatted as a size indicator (e.g., '500GB').
- **data_sources** (str): A string listing the data sources involved, possibly comma-separated or encoded, used to inform deployment decisions.

### Returns

bool: A boolean value indicating whether cloud deployment is recommended (true) or not (false).

### Raises

- ValueError: Raised if input storage size or data sources are invalid or improperly formatted.
- TypeError: Raised if input parameters are of incorrect types.

### Examples

```python
>>> recommend_cloud_deployment('100GB', 'SensorData,Logs')
true
```

```python
>>> recommend_cloud_deployment('10TB', 'VideoStreams')
true
```
