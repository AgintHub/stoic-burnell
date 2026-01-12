# validate_data_sources PRD

## Description
This shim function validates and filters a list of data source names to ensure they conform to expected criteria before further processing.


## Conceptual Info

The shim validates and filters the provided list of data source names to ensure only valid and recognized sources are processed further.

## Docstring

### Summary
Validates and filters a list of data source names, ensuring they meet specified criteria before downstream use.

### Parameters

- **data_sources** (str): A string representing the list of data source names to be validated, usually from an external source.

### Returns

list[str]: A list of validated data source names that are suitable for subsequent processing.

### Raises

- ValueError: Raised if the input data_sources string is malformed or contains invalid entries.
- TypeError: Raised if the input data_sources is not of type str.

### Examples

```python
>>> validated_sources = validate_data_sources('source1, source2, invalid_source')
>>> print(validated_sources)
['source1', 'source2']
```

```python
>>> validated_sources = validate_data_sources('')
>>> print(validated_sources)
[]
```
