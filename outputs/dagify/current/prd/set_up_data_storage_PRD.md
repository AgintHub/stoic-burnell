# set_up_data_storage PRD

## Description
Select and describe the database for storing market data.


## Conceptual Info

This node proposes a data storage solution for high-volume option data.

## Docstring

### Summary
Proposes a data storage solution suitable for high-volume option data.

### Parameters

- **data_sources** (List[str]): List of data sources required for the strategy

### Returns

{database_type: str, schema_outline: str, partition_strategy: str, retention_policy: str, data_storage_size: int, is_cloud_based: bool}: A dictionary containing the proposed data storage solution details

### Raises

- ValueError: If the data source is invalid or unsupported

### Examples

```python
>>> set_up_data_storage(data_sources=['exchange_tick_data', 'option_chain_feeds'])
{'database_type': 'time-series', 'schema_outline': '...', 'partition_strategy': 'by_date', 'retention_policy': 'time-based', 'data_storage_size': 1000, 'is_cloud_based': True}
```
