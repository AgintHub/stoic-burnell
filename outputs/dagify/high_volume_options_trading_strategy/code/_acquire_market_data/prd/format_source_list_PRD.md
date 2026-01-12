# format_source_list PRD

## Description
A function that formats a list of data sources into a comma-separated string.


## Conceptual Info

The format_source_list shim node is responsible for formatting a list of data sources into a comma-separated string, which will be used as the output of the acquire_market_data node.

## Docstring

### Summary
Format a list of data sources into a comma-separated string.

Parameters:
``sources`` (list): A list of data sources to be formatted.

Returns:
``str``: The formatted string of data sources.

Raises:
``ValueError``: If the input list is empty.
``TypeError``: If the input is not a list.

Examples:
>>> format_source_list(['source1', 'source2', 'source3'])

'source1, source2, source3'
>>> format_source_list([])

ValueError: Input list is empty


### Parameters

- **sources** (List[str]): A list of data sources to be formatted

### Returns

STR: The formatted string of data sources

### Raises

- ValueError: If the input list is empty
- TypeError: If the input is not a list

### Examples

```python
>>> format_source_list(['source1', 'source2', 'source3'])
'source1, source2, source3'
```

```python
>>> format_source_list([])
ValueError: Input list is empty
```
