# verify_timeline_integrity PRD

## Description
Verifies the integrity of a timeline based on the provided CSV output and expected years.


## Conceptual Info

The verify_timeline_integrity shim function checks if the generated timeline matches the expected years and is correctly formatted.

## Docstring

### Summary
Verifies the integrity of a timeline based on the provided CSV output and expected years.

### Parameters

- **csv_output** (str): The CSV output of the timeline.
- **expected_years** (str): The expected years in the timeline.

### Returns

bool: Boolean indicating whether the timeline integrity verification was successful.

### Raises

- ValueError: When the CSV output is empty or does not contain the expected years.
- TypeError: When the input types are incorrect.

### Examples

```python
>>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,LocationTotals\n2020,1.0,100,200\n2021,1.1,120,250', expected_years='2020,2021')
True
```

```python
>>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,LocationTotals\n2020,1.0,100,200\n2022,1.1,120,250', expected_years='2020,2021')
False
```
