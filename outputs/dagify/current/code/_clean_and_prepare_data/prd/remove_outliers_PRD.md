# remove_outliers PRD

## Description
This shim function performs outlier removal on a dataset using a specified method and returns the processed dataset.


## Conceptual Info

This shim applies outlier removal techniques to a dataset using a specified method to improve data quality for subsequent analysis.

## Docstring

### Summary
Remove outliers from the dataset based on the specified method and return the cleaned dataset as a string.

### Parameters

- **dataset** (str): A serialized string representing the dataset to process.
- **method** (str): The outlier removal method to apply, e.g., 'zscore' or 'iqr'.

### Returns

str: A serialized string of the dataset after outlier removal has been applied.

### Raises

- ValueError: If the specified method is not supported or if dataset format is invalid.
- TypeError: If input types for dataset or method are incorrect.

### Examples

```python
>>> remove_outliers('dataset_string', method='zscore')
'cleaned_dataset_string'
```

```python
>>> remove_outliers('another_dataset_string', method='iqr')
'processed_dataset_string'
```
