# set_up_data_storage PRD

## Description
Designs an optimized data storage solution tailored for market data, ensuring high-performance, scalability, and reliability.


## Conceptual Info

Data Storage Solution for Market Data

## Docstring

### Summary
Designs an optimized data storage solution tailored for market data, ensuring high-performance, scalability, and reliability.

### Parameters

- **identify_data_sources** (node): Output of the `identify_data_sources` node

### Returns

{key: database_type, type: str, description: Type of the database (e.g., relational, NoSQL, time-series)}: Output of the data storage solution

### Raises

- ErrorOccured: Raised when an error occurs during data storage setup

### Examples

```python
>>> Input: identify_data_sources node output
>>> Output: Database type (str), Schema outline (str), Partition strategy (str), Retention policy (str), Data storage size (int), and Cloud-based (bool)
>>> ...
...
```
