# _clean_and_prepare_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_clean_and_prepare_data' module.

## Table of Contents

- [load_raw_dataset](#load_raw_dataset)

- [handle_missing_values](#handle_missing_values)

- [remove_outliers](#remove_outliers)

- [standardize_data](#standardize_data)

- [calculate_derived_features](#calculate_derived_features)

- [validate_cleaned_data](#validate_cleaned_data)

- [assess_dataset_readiness](#assess_dataset_readiness)



---

## load_raw_dataset

### Description
Loads a raw dataset from a specified input parameter.

### Conceptual Info

This shim function serves as an interface to load a raw dataset based on the provided input parameter.

### Docstring

**Summary:** Loads a raw dataset from an input parameter.

**Parameters:**

- validation_input (str): The input parameter containing the raw dataset to be loaded.
**Returns:** dict - A dictionary containing the loaded raw dataset and its associated input parameter.

**Raises:**

- ValueError: Raised when the input parameter is invalid or cannot be loaded as a dataset.
- TypeError: Raised when the input parameter is not a valid string type.
**Examples:**

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



---

## handle_missing_values

### Description
This shim handles missing values in datasets by applying a specified strategy, facilitating data cleaning and preparation.

### Conceptual Info

This shim executes missing value handling in datasets based on the specified strategy to support data cleaning workflows.

### Docstring

**Summary:** Handles missing values in a dataset according to the specified strategy and returns the count of handled missing values.

**Parameters:**

- dataset (str): A string identifier or representation of the dataset to process.
- strategy (str): The strategy to use for handling missing values, such as 'imputation' or 'removal'.
**Returns:** int - The number of missing values that were handled in the dataset.

**Raises:**

- ValueError: Raised if the provided strategy is invalid or unsupported.
- TypeError: Raised if input parameters are of incorrect types.
**Examples:**

```python
>>> handle_missing_values('dataset1', strategy='imputation')
5
```

```python
>>> handle_missing_values('dataset2', strategy='removal')
10
```



---

## remove_outliers

### Description
This shim function performs outlier removal on a dataset using a specified method and returns the processed dataset.

### Conceptual Info

This shim applies outlier removal techniques to a dataset using a specified method to improve data quality for subsequent analysis.

### Docstring

**Summary:** Remove outliers from the dataset based on the specified method and return the cleaned dataset as a string.

**Parameters:**

- dataset (str): A serialized string representing the dataset to process.
- method (str): The outlier removal method to apply, e.g., 'zscore' or 'iqr'.
**Returns:** str - A serialized string of the dataset after outlier removal has been applied.

**Raises:**

- ValueError: If the specified method is not supported or if dataset format is invalid.
- TypeError: If input types for dataset or method are incorrect.
**Examples:**

```python
>>> remove_outliers('dataset_string', method='zscore')
'cleaned_dataset_string'
```

```python
>>> remove_outliers('another_dataset_string', method='iqr')
'processed_dataset_string'
```



---

## standardize_data

### Description
A shim function that standardizes a dataset using a specified scaler type, facilitating data preprocessing for machine learning tasks.

### Conceptual Info

This shim function applies a standardization transformation to the input dataset using the specified scaler type to ensure features are on a comparable scale.

### Docstring

**Summary:** This function standardizes a given dataset based on the specified scaler type, transforming data to improve model training performance.

**Parameters:**

- dataset (str): A serialized representation of the dataset to be standardized.
- scaler_type (str): Type of scaler to use for standardization (e.g., 'standard', 'minmax', etc.).
**Returns:** str - A serialized string representing the standardized dataset.

**Raises:**

- ValueError: Raised if an unsupported scaler_type is specified or dataset is invalid.
- TypeError: Raised if the inputs are not of the expected types.
**Examples:**

```python
>>> standardize_data('sample_dataset', 'standard')
'standardized_dataset_string_representation'
```

```python
>>> standardize_data('another_dataset', 'minmax')
'minmax_scaled_dataset_string'
```



---

## calculate_derived_features

### Description
This shim computes derived features from a dataset to enhance feature engineering for predictive modeling.

### Conceptual Info

This shim function generates additional features from the provided dataset to support advanced feature engineering steps in the data pipeline.

### Docstring

**Summary:** Compute derived features from the given dataset to facilitate enhanced feature engineering for predictive tasks.

**Parameters:**

- dataset (str): A serialized or identifier string of the dataset from which derived features are to be calculated.
**Returns:** str - A string listing the names of derived features calculated, typically separated by commas.

**Raises:**

- ValueError: Raised if the input dataset string is invalid or missing required information.
- TypeError: Raised if the input type is not a string.
**Examples:**

```python
>>> calculate_derived_features('dataset_v1')
'interaction_term_A_B,previous_days_diff,normalized_value'
```

```python
>>> calculate_derived_features('sales_data')
'month_over_month_growth,average_sales_last_week'
```



---

## validate_cleaned_data

### Description
This shim function validates the cleaned dataset and summarizes the validation results for use in a data processing pipeline.

### Conceptual Info

This shim assesses the quality of cleaned and prepared data to ensure it meets validation criteria before further processing.

### Docstring

**Summary:** Validate the cleaned dataset for quality issues, returning a boolean indicating overall validity.

**Parameters:**

- dataset (str): The dataset in a serialized or filepath format that needs validation.
**Returns:** bool - A boolean indicating whether the dataset passed all validation checks.

**Raises:**

- ValueError: Raised if the input dataset is invalid or cannot be parsed.
- TypeError: Raised if the input parameter is not of type str.
**Examples:**

```python
>>> validate_cleaned_data('path/to/cleaned_dataset.csv')
True
```

```python
>>> validate_cleaned_data('invalid/path')
False
```



---

## assess_dataset_readiness

### Description
Determines whether a dataset is ready for feature engineering based on its quality evaluation.

### Conceptual Info

This shim assesses the readiness of a dataset for feature engineering by evaluating its quality metrics and overall passing status.

### Docstring

**Summary:** This function evaluates dataset readiness for feature engineering based on its quality assessment, returning True if the dataset passes quality checks, otherwise False.

**Parameters:**

- dataset (str): Identifier or path for the dataset whose readiness is to be assessed.
- quality_passed (str): String indicating whether the dataset's quality checks have been passed ('yes' or 'no').
**Returns:** bool - A boolean value indicating whether the dataset is ready for feature engineering (True) or not (False).

**Raises:**

- ValueError: Raised if the input parameters are invalid or missing required values.
- TypeError: Raised if input parameters are of incorrect types.
**Examples:**

```python
>>> dataset_path = 'data/financial_data.csv'
>>> quality_status = 'yes'
>>> is_ready = assess_dataset_readiness(dataset=dataset_path, quality_passed=quality_status)
True
```

```python
>>> dataset_path = 'data/market_data.csv'
>>> quality_status = 'no'
>>> is_ready = assess_dataset_readiness(dataset=dataset_path, quality_passed=quality_status)
False
```

