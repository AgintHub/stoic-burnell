# load_raw_dataset PRD

## Description
Loads a raw dataset from a specified input parameter.


## Conceptual Info

This shim function serves as an interface to load a raw dataset based on the provided input parameter.

## Docstring

### Summary
Loads a raw dataset from an input parameter.

### Parameters

- **validation_input** (str): The input parameter containing the raw dataset to be loaded.

### Returns

dict: A dictionary containing the loaded raw dataset and its associated input parameter.

### Raises

- ValueError: Raised when the input parameter is invalid or cannot be loaded as a dataset.
- TypeError: Raised when the input parameter is not a valid string type.

### Examples

```python
>>> load_raw_dataset(validation_input='example dataset')
>>> output = {"output": 'example dataset', "validation_input": 'example dataset'}
{"output": 'example dataset', "validation_input": 'example dataset'}
```

```python
>>> load_raw_dataset(validation_input='another dataset')
>>> output = {"output": 'another dataset', "validation_input": 'another dataset'}
{"output": 'another dataset', "validation_input": 'another dataset'}
```
