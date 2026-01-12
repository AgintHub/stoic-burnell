# handle_missing_values PRD

## Description
This shim handles missing values in datasets by applying a specified strategy, facilitating data cleaning and preparation.


## Conceptual Info

This shim executes missing value handling in datasets based on the specified strategy to support data cleaning workflows.

## Docstring

### Summary
Handles missing values in a dataset according to the specified strategy and returns the count of handled missing values.

### Parameters

- **dataset** (str): A string identifier or representation of the dataset to process.
- **strategy** (str): The strategy to use for handling missing values, such as 'imputation' or 'removal'.

### Returns

int: The number of missing values that were handled in the dataset.

### Raises

- ValueError: Raised if the provided strategy is invalid or unsupported.
- TypeError: Raised if input parameters are of incorrect types.

### Examples

```python
>>> handle_missing_values('dataset1', strategy='imputation')
5
```

```python
>>> handle_missing_values('dataset2', strategy='removal')
10
```
