# _validate_acquired_data - Complete PRD Documentation

## Overview
PRDs for nodes in the '_validate_acquired_data' module.

## Table of Contents

- [determine_validation_checks](#determine_validation_checks)

- [validate_timestamp_consistency](#validate_timestamp_consistency)

- [validate_price_consistency](#validate_price_consistency)

- [identify_missing_timestamps](#identify_missing_timestamps)

- [identify_price_consistency_issues](#identify_price_consistency_issues)

- [determine_overall_validation_status](#determine_overall_validation_status)

- [raise_invalid_data_error](#raise_invalid_data_error)



---

## determine_validation_checks

### Description
This shim function determines the set of validation checks to perform on acquired market data based on its attributes and context.

### Conceptual Info

The shim generates a list of validation checks tailored to the characteristics of the acquired market data, facilitating comprehensive data validation.

### Docstring

**Summary:** Determine the list of validation checks to perform on acquired market data based on its source, timestamps, and other attributes.

**Parameters:**

- data_input (str): A string identifier or serialized representation of the acquired market data object, which includes its attributes necessary for deciding validation checks.
**Returns:** str - A comma-separated string representing the list of validation checks to execute, or a list of check names.

**Raises:**

- ValueError: Raised if the input data input is invalid or missing required attributes.
- TypeError: Raised if the input parameter is not of type str.
**Examples:**

```python
>>> checks = determine_validation_checks('some_data_identifier')
>>> print(checks)
['timestamp_consistency', 'price_validation', 'missing_data_check']
```

```python
>>> checks = determine_validation_checks('another_data_source')
>>> print(checks)
['timestamp_consistency', 'price_validation']
```



---

## validate_timestamp_consistency

### Description
This shim performs validation of timestamp consistency between the start and end timestamps to ensure data integrity within the larger data processing pipeline.

### Conceptual Info

This shim verifies that provided start and end timestamps are logically consistent, ensuring chronological correctness before data processing continues.

### Docstring

**Summary:** This function validates the consistency between start and end timestamps to confirm they represent a coherent time interval, raising errors if validation fails.

**Parameters:**

- start_timestamp (str): The start timestamp string, expected to be in a parseable date-time format.
- end_timestamp (str): The end timestamp string, expected to be in a parseable date-time format that must succeed the start timestamp.
**Returns:** bool - Returns True if the timestamps are valid and logically ordered; otherwise, raises an error or returns False.

**Raises:**

- ValueError: Raised when the timestamp strings are improperly formatted or the end timestamp precedes the start timestamp.
- TypeError: Raised if input types are not strings.
**Examples:**

```python
>>> validate_timestamp_consistency('2023-01-01T00:00:00', '2023-01-02T00:00:00')
True
```

```python
>>> validate_timestamp_consistency('2023-01-02T00:00:00', '2023-01-01T00:00:00')
Error or False indicating invalid timestamp interval
```



---

## validate_price_consistency

### Description
This shim function checks the consistency and validity of price data from specified data sources within the larger data validation workflow.

### Conceptual Info

The shim assess the consistency of price data from given data sources to ensure data integrity within the validation pipeline.

### Docstring

**Summary:** Validate the consistency of price data obtained from specified data sources based on the provided timestamps or data characteristics.

**Parameters:**

- data_sources (str): A string identifier or list representing the sources of price data to be validated.
**Returns:** bool - Returns True if the price data from the sources is consistent and passes validation checks; otherwise, False.

**Raises:**

- ValueError: Raised if the data sources input is invalid or if the validation cannot be performed due to missing or corrupt data.
- TypeError: Raised if the input data_sources parameter is not of type str.
**Examples:**

```python
>>> validate_price_consistency('data_source_name')
True
```

```python
>>> validate_price_consistency('invalid_source')
False
```



---

## identify_missing_timestamps

### Description
A shim function that determines the list of timestamps missing data within a specified time range.

### Conceptual Info

This shim identifies timestamps with missing data between the provided start and end timestamps to support data validation and completeness checks.

### Docstring

**Summary:** The function receives start and end timestamps as strings and returns a list of integer timestamps where data is missing within this range; it assumes timestamps are in ISO format or comparable string format appropriately parsed into integers.

**Parameters:**

- start_timestamp (str): The starting timestamp of the data range, in a recognizable string format such as ISO 8601.
- end_timestamp (str): The ending timestamp of the data range, in a recognizable string format such as ISO 8601.
**Returns:** LIST_INT - A list of integers representing timestamps with missing data within the specified range.

**Raises:**

- ValueError: Raised if the input timestamps are in an invalid format or cannot be parsed into comparable timestamps.
- TypeError: Raised if the inputs are not of type str.
**Examples:**

```python
>>> identify_missing_timestamps('2023-01-01T00:00:00', '2023-01-01T01:00:00')
[2, 5, 7]
```

```python
>>> identify_missing_timestamps('2023-06-01T00:00:00', '2023-06-01T00:10:00')
[0, 3, 4]
```



---

## identify_price_consistency_issues

### Description
This shim determines and returns a list of identified price consistency issues based on given data sources to support validation processes.

### Conceptual Info

This shim detects discrepancies or issues related to price consistency within data sourced from various inputs to facilitate data validation.

### Docstring

**Summary:** Identify and return a list of price consistency issues found across the specified data sources.

**Parameters:**

- data_sources (str): A string indicating the sources of the data to analyze for price issues.
**Returns:** list of str - List containing descriptions of each detected price consistency issue.

**Raises:**

- ValueError: Raised if data_sources is empty or improperly formatted.
- TypeError: Raised if data_sources is not a string.
**Examples:**

```python
>>> identify_price_consistency_issues('sourceA, sourceB')
['Price discrepancy detected in sourceA', 'Price spike observed in sourceB']
```

```python
>>> identify_price_consistency_issues('market_data_feed')
[]  # No issues found
```



---

## determine_overall_validation_status

### Description
This shim function computes an overall boolean validation status based on individual check results and acquisition success indicator.

### Conceptual Info

The function evaluates multiple validation check results along with acquisition success status to determine an aggregate boolean validation outcome, facilitating decision-making in data processing workflows.

### Docstring

**Summary:** Determine an overall boolean validation status based on individual check results and acquisition success indicator.

**Parameters:**

- check_results (STR): A JSON-formatted string representing the list of boolean check results performed during data validation.
- acquisition_successful (STR): A JSON-formatted string indicating whether data acquisition was successful ('true' or 'false').
**Returns:** str - A string 'true' or 'false' representing the overall validation status.

**Raises:**

- ValueError: Raised if the input strings cannot be parsed as valid JSON lists or contain invalid values.
- TypeError: Raised if the inputs are not strings.
**Examples:**

```python
>>> determine_overall_validation_status('{"check_results": [true, true], "acquisition_successful": "true"}')
'true'
```

```python
>>> determine_overall_validation_status('{"check_results": [true, false], "acquisition_successful": "true"}')
'false'
```



---

## raise_invalid_data_error

### Description
This shim function raises a structured validation error when data integrity or consistency checks fail based on provided issues and missing data details.

### Conceptual Info

The shim raises an invalid data error with detailed issues and missing data information to enforce data validation and trigger downstream error handling.

### Docstring

**Summary:** Raises an invalid data error with detailed issues and missing data descriptions, ensuring data integrity checks are enforced in the workflow.

**Parameters:**

- issues (str): A string describing the issues or errors identified during data validation.
- missing_data (str): A string listing the missing data points or timestamps causing validation failure.
**Returns:** str - A message indicating the error was raised, or the function may not return if it raises an exception.

**Raises:**

- ValueError: Always raises a ValueError to indicate invalid data with detailed issues, halting further processing.
**Examples:**

```python
>>> raise_invalid_data_error(issues='Price discrepancies found', missing_data='Timestamps missing')
'Invalid data error raised due to price discrepancies and missing timestamps.'
```

```python
>>> try:
...     raise_invalid_data_error(issues='Corrupted data', missing_data='')
>>> except ValueError as e:
...     print(str(e))
'Invalid data error raised due to corrupted data.'
```

