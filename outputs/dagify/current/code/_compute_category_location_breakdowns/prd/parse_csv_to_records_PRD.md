# parse_csv_to_records PRD

## Description
A shim function that takes a CSV string as input, parses it, and returns a list of records.


## Conceptual Info

The parse_csv_to_records shim function is responsible for parsing a CSV string into a list of records, which can then be used for further processing and analysis.

## Docstring

### Summary
Parses a CSV string into a list of records.

### Parameters

- **csv_string** (str): The input CSV string to be parsed.

### Returns

list: A list of records parsed from the input CSV string, where each record is a dictionary representing a row in the CSV file.

### Raises

- ValueError: When the input CSV string is malformed or empty.
- TypeError: When the input is not a string.

### Examples

```python
>>> import csv
>>> def parse_csv_to_records(csv_string):
...     reader = csv.DictReader(csv_string.splitlines())
...     return list(reader)
>>> csv_string = "Name,Age,Country\nJohn,25,USA\nJane,30,UK"
>>> parse_csv_to_records(csv_string)
[{'Name': 'John', 'Age': '25', 'Country': 'USA'}, {'Name': 'Jane', 'Age': '30', 'Country': 'UK'}]
```
