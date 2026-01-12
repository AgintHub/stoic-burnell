# create_file_templates PRD

## Description
Generate a list of file templates suitable for initializing a code repository based on provided components, layout, and trading type.


## Conceptual Info

This shim generates appropriate file templates for setting up a code repository tailored to specific trading components, layout, and type.

## Docstring

### Summary
Create a list of file templates for repository initialization given components, layout, and trading type, ensuring suitability for the strategy setup.

### Parameters

- **components** (str): A string representing the strategy components to be included, such as 'risk_management, data_loading'.
- **layout** (str): A string describing the repository layout, including directory structure and organization.
- **trading_type** (str): Type of trading strategy, e.g., 'options', 'equity', 'forex'.

### Returns

str: A list of file template names or contents pertinent to the provided components, layout, and trading type.

### Raises

- ValueError: Raised if any required parameter is missing or invalid, such as empty strings or unsupported trading types.
- TypeError: Raised if input parameters are of incorrect types, e.g., non-string for components, layout, or trading_type.

### Examples

```python
>>> create_file_templates('risk_management,data_loading', 'standard_layout', 'options')
[ 'risk_management_template.py', 'data_loading_template.py' ]
```

```python
>>> create_file_templates('analytics', 'advanced_layout', 'equity')
[ 'analytics_template.py' ]
```
