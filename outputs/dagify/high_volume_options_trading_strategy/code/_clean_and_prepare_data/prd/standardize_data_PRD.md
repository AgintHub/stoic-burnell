# standardize_data PRD

## Description
A shim function that standardizes a dataset using a specified scaler type, facilitating data preprocessing for machine learning tasks.


## Conceptual Info

This shim function applies a standardization transformation to the input dataset using the specified scaler type to ensure features are on a comparable scale.

## Docstring

### Summary
This function standardizes a given dataset based on the specified scaler type, transforming data to improve model training performance.

### Parameters

- **dataset** (str): A serialized representation of the dataset to be standardized.
- **scaler_type** (str): Type of scaler to use for standardization (e.g., 'standard', 'minmax', etc.).

### Returns

str: A serialized string representing the standardized dataset.

### Raises

- ValueError: Raised if an unsupported scaler_type is specified or dataset is invalid.
- TypeError: Raised if the inputs are not of the expected types.

### Examples

```python
>>> standardize_data('sample_dataset', 'standard')
'standardized_dataset_string_representation'
```

```python
>>> standardize_data('another_dataset', 'minmax')
'minmax_scaled_dataset_string'
```
