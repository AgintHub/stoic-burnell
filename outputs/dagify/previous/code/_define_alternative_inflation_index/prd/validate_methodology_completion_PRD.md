# validate_methodology_completion PRD

## Description
Validates the completion of a methodology based on the provided weights and index name.


## Conceptual Info

The validate_methodology_completion shim is responsible for verifying that a methodology is complete based on the provided weights and index name.

## Docstring

### Summary
Validates the completion of a methodology based on the provided weights and index name.

### Parameters

- **weights** (str): The weights to be used for validation.
- **index_name** (str): The index name to be used for validation.

### Returns

bool: A boolean indicating whether the methodology is complete.

### Raises

- ValueError: When the input validation fails.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> validate_methodology_completion(weights='category1=0.5,category2=0.5', index_name='example_index')
True
```

```python
>>> validate_methodology_completion(weights='category1=0.3,category2=0.7', index_name='another_index')
True
```
