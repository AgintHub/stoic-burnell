# _compute_category_location_breakdowns - Complete PRD Documentation

## Overview
PRDs for nodes in the '_compute_category_location_breakdowns' module.

## Table of Contents

- [validate_csv_format](#validate_csv_format)

- [parse_csv_to_records](#parse_csv_to_records)

- [aggregate_by_category](#aggregate_by_category)

- [aggregate_by_location](#aggregate_by_location)

- [convert_category_aggregation_to_csv](#convert_category_aggregation_to_csv)

- [convert_location_aggregation_to_csv](#convert_location_aggregation_to_csv)



---

## validate_csv_format

### Description
Validates a given CSV string against a set of required columns.

### Conceptual Info

The validate_csv_format shim function checks if a given CSV string contains all the required columns, ensuring data consistency and integrity.

### Docstring

**Summary:** Validates a CSV string against a set of required columns.

**Parameters:**

- csv_data (str): The input CSV string to be validated.
- required_columns (str): A comma-separated string of required column names.
**Returns:** bool - True if the CSV string is valid, False otherwise.

**Raises:**

- ValueError: When the input CSV string is malformed or empty.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> import pandas as pd
>>> csv_data = 'Year,Category,Location,Expenditure_Amount\n2020,Food,New York,100'
>>> required_columns = 'Year,Category,Location,Expenditure_Amount'
>>> validate_csv_format(csv_data=csv_data, required_columns=required_columns)
True
```

```python
>>> import pandas as pd
>>> csv_data = 'Year,Category,Location'
>>> required_columns = 'Year,Category,Location,Expenditure_Amount'
>>> validate_csv_format(csv_data=csv_data, required_columns=required_columns)
False
```



---

## parse_csv_to_records

### Description
A shim function that takes a CSV string as input, parses it, and returns a list of records.

### Conceptual Info

The parse_csv_to_records shim function is responsible for parsing a CSV string into a list of records, which can then be used for further processing and analysis.

### Docstring

**Summary:** Parses a CSV string into a list of records.

**Parameters:**

- csv_string (str): The input CSV string to be parsed.
**Returns:** list - A list of records parsed from the input CSV string, where each record is a dictionary representing a row in the CSV file.

**Raises:**

- ValueError: When the input CSV string is malformed or empty.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> import csv
>>> def parse_csv_to_records(csv_string):
...     reader = csv.DictReader(csv_string.splitlines())
...     return list(reader)
>>> csv_string = "Name,Age,Country\nJohn,25,USA\nJane,30,UK"
>>> parse_csv_to_records(csv_string)
[{'Name': 'John', 'Age': '25', 'Country': 'USA'}, {'Name': 'Jane', 'Age': '30', 'Country': 'UK'}]
```



---

## aggregate_by_category

### Description
This shim aggregates expenditure data by category, summing the expenditure amounts for each category in a given year.

### Conceptual Info

The aggregate_by_category shim is designed to process expenditure data, grouping it by categories and summing the corresponding expenditure amounts for each year.

### Docstring

**Summary:** Aggregate expenditure data by category, summing expenditure amounts for each category in a given year.

**Parameters:**

- data (str): The input data to be aggregated, expected to be a list of records or a string representing a CSV structure.
- year_col (str): The column name in the data that represents the year.
- category_col (str): The column name in the data that represents the category.
- amount_col (str): The column name in the data that represents the expenditure amount.
**Returns:** dict - A dictionary where keys are categories and values are the total expenditure amounts for each category, structured as '{category: total_amount}'.

**Raises:**

- ValueError: If the input data is not in the expected format or if required columns are missing.
- TypeError: If the input parameters are not of the expected types.
**Examples:**

```python
>>> data = [{'Year': '2022', 'Category': 'Food', 'Expenditure_Amount': 100},
...         {'Year': '2022', 'Category': 'Transport', 'Expenditure_Amount': 50}]
>>> year_col = 'Year'
>>> category_col = 'Category'
>>> amount_col = 'Expenditure_Amount'
>>> result = aggregate_by_category(data, year_col, category_col, amount_col)
{'Food': 100, 'Transport': 50}
```



---

## aggregate_by_location

### Description
This shim aggregates expenditure data by location, returning a dictionary with location-based expenditure amounts for each year.

### Conceptual Info

The aggregate_by_location shim plays a crucial role in processing expenditure data, enabling the calculation of total expenditures by location across different years.

### Docstring

**Summary:** Aggregates expenditure data by location, calculating total expenditures for each location in each year.

**Parameters:**

- data (str): Input expenditure data as a string, expected to be a list of records containing year, location, and amount information.
- year_col (str): The column name in the data that represents the year.
- location_col (str): The column name in the data that represents the location.
- amount_col (str): The column name in the data that represents the expenditure amount.
**Returns:** str - A dictionary containing location-based expenditure amounts for each year, returned as a JSON string.

**Raises:**

- ValueError: When the input data does not contain the specified year, location, or amount columns.
- TypeError: When the input data or column names are of incorrect types.
**Examples:**

```python
>>> data = '[{"Year": 2020, "Location": "New York", "Expenditure_Amount": 100}, {"Year": 2020, "Location": "Chicago", "Expenditure_Amount": 200}]'
>>> year_col = 'Year'
>>> location_col = 'Location'
>>> amount_col = 'Expenditure_Amount'
>>> result = aggregate_by_location(data, year_col, location_col, amount_col)
{'2020': {'New York': 100, 'Chicago': 200}}
```



---

## convert_category_aggregation_to_csv

### Description
This shim function converts category aggregation data into a CSV string format.

### Conceptual Info

The convert_category_aggregation_to_csv shim is responsible for transforming aggregated category data into a comma-separated values string, facilitating data exchange and analysis.

### Docstring

**Summary:** Converts category aggregation data into a CSV string, where each row represents a unique category and its corresponding expenditure amount.

**Parameters:**

- aggregated_data (dict): A dictionary containing category aggregation data, where keys are category names and values are expenditure amounts.
**Returns:** str - A CSV string representation of the category aggregation data, with columns for category names and expenditure amounts.

**Raises:**

- ValueError: If the input aggregated data is empty or does not contain the expected category and expenditure amount information.
- TypeError: If the input aggregated data is not a dictionary or contains incorrect data types.
**Examples:**

```python
>>> category_data = {'Category A': 100.0, 'Category B': 200.0}
>>> csv_output = convert_category_aggregation_to_csv(category_data)
'Category,Expenditure Amount\nCategory A,100.0\nCategory B,200.0'
```

```python
>>> empty_data = {}
>>> csv_output = convert_category_aggregation_to_csv(empty_data)
ValueError: Input aggregated data is empty.
```



---

## convert_location_aggregation_to_csv

### Description
Converts aggregated location data into a CSV string.

### Conceptual Info

This shim function takes aggregated location data and converts it into a CSV string, which can be used for further processing or analysis.

### Docstring

**Summary:** Converts aggregated location data into a CSV string.

**Parameters:**

- aggregated_data (str): Input parameter containing aggregated location data in a format that can be converted to CSV.
**Returns:** str - CSV string representation of the aggregated location data, with columns for Year, Location, and Expenditure Amount.

**Raises:**

- ValueError: When input validation fails, such as if the input data is not in a valid format.
- TypeError: When input types are incorrect, such as if the input data is not a string.
**Examples:**

```python
>>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'New York': 1000, 'Los Angeles': 2000}, '2023': {'New York': 1500, 'Los Angeles': 2500}})
"Year,Location,Expenditure Amount\n2022,New York,1000\n2022,Los Angeles,2000\n2023,New York,1500\n2023,Los Angeles,2500"
```

```python
>>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'Chicago': 500, 'Houston': 750}, '2023': {'Chicago': 1000, 'Houston': 1250}})
"Year,Location,Expenditure Amount\n2022,Chicago,500\n2022,Houston,750\n2023,Chicago,1000\n2023,Houston,1250"
```

