# _generate_historical_timeline - Complete PRD Documentation

## Overview
PRDs for nodes in the '_generate_historical_timeline' module.

## Table of Contents

- [validate_input_data](#validate_input_data)

- [parse_category_csv_to_year_totals](#parse_category_csv_to_year_totals)

- [parse_location_csv_to_year_totals](#parse_location_csv_to_year_totals)

- [create_year_index_mapping](#create_year_index_mapping)

- [merge_timeline_data](#merge_timeline_data)

- [format_timeline_as_csv](#format_timeline_as_csv)

- [verify_timeline_integrity](#verify_timeline_integrity)



---

## validate_input_data

### Description
Validates the input data for generating a historical timeline.

### Conceptual Info

The validate_input_data shim function checks if the provided input data for generating a historical timeline is valid and well-formed.

### Docstring

**Summary:** Validates the input data for generating a historical timeline.

**Parameters:**

- index_input (str): Input parameter containing index series data. It should be a string representation of a ComputeIndexSeriesOutput object.
- breakdown_input (str): Input parameter containing category and location breakdown data. It should be a string representation of a ComputeCategoryLocationBreakdownsOutput object.
**Returns:** bool - Boolean indicating whether the input data is valid.

**Raises:**

- ValueError: When input validation fails due to missing or incorrect data.
- TypeError: When input types are incorrect.
**Examples:**

```python
>>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120], 'is_index_successful': True})
>>> breakdown_input = str({'category_spending_csv': 'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv': 'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90', 'is_breakdown_successful': True})
>>> validate_input_data(index_input=index_input, breakdown_input=breakdown_input)
True
```

```python
>>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120]})
>>> breakdown_input = str({'category_spending_csv': 'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv': 'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90'})
>>> validate_input_data(index_input=index_input, breakdown_input=breakdown_input)
False
```



---

## parse_category_csv_to_year_totals

### Description
This shim function takes a CSV string containing category spending data and returns a dictionary where the keys are years and the values are the total expenditures for each category in that year.

### Conceptual Info

The parse_category_csv_to_year_totals shim is responsible for parsing category spending CSV data into a structured dictionary format for further analysis or processing.

### Docstring

**Summary:** Parses a CSV string of category spending data into a dictionary where keys are years and values are total expenditures for each category in that year.

**Parameters:**

- csv_data (str): A string containing CSV data with columns for year and category expenditures.
**Returns:** dict - A dictionary where each key is a year and each value is the total expenditure for all categories in that year.

**Raises:**

- ValueError: If the input CSV string is malformed or cannot be parsed.
- TypeError: If the input is not a string or if the CSV data cannot be converted into the required dictionary format.
**Examples:**

```python
>>> csv_string = 'Year,Category,Expenditure'
>>> csv_string += '\n2020,CategoryA,100'
>>> csv_string += '\n2020,CategoryB,200'
>>> csv_string += '\n2021,CategoryA,150'
>>> result = parse_category_csv_to_year_totals(csv_string)
{'2020': 300, '2021': 150}
```



---

## parse_location_csv_to_year_totals

### Description
A shim function that takes a CSV string containing location spending data and returns a dictionary with year-wise totals.

### Conceptual Info

This shim function is used to extract year-wise totals from a CSV string containing location spending data.

### Docstring

**Summary:** Parses a CSV string containing location spending data and returns a dictionary with year-wise totals.

**Parameters:**

- csv_data (str): A CSV string containing location spending data with columns: Year, HouseholdLocation, and total expenditure.
**Returns:** str - A dictionary with year-wise totals for location spending, where each key is a year and each value is the total expenditure for that year.

**Raises:**

- ValueError: When the input CSV string is invalid or empty.
- TypeError: When the input csv_data is not a string.
**Examples:**

```python
>>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2020,Location A,100\n2020,Location B,200\n2021,Location A,150')
{'2020': 300, '2021': 150}
```

```python
>>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2019,Location C,50\n2020,Location C,75')
{'2019': 50, '2020': 75}
```



---

## create_year_index_mapping

### Description
This shim function generates a dictionary mapping years to their corresponding index values.

### Conceptual Info

This shim is used to create a mapping of years to their respective index values, which is essential for generating historical timelines.

### Docstring

**Summary:** Generate a dictionary mapping years to index values from input strings of years and index values.

**Parameters:**

- years (str): A comma-separated string of years.
- index_values (str): A comma-separated string of index values corresponding to the years.
**Returns:** str - A dictionary as a string where keys are years and values are index values.

**Raises:**

- ValueError: If the lengths of the years and index values strings do not match.
- TypeError: If the input years or index values are not strings.
**Examples:**

```python
>>> create_year_index_mapping('2020,2021,2022', '10.5,11.2,12.1')
{'2020': 10.5, '2021': 11.2, '2022': 12.1}
```

```python
>>> create_year_index_mapping('2015,2016', '20,21')
{'2015': 20, '2016': 21}
```



---

## merge_timeline_data

### Description
Combines index data, category totals, and location totals into a unified timeline data structure.

### Conceptual Info

The merge_timeline_data shim function integrates data from different sources (index series, category breakdowns, and location breakdowns) into a cohesive timeline. This timeline is crucial for generating historical reports and analyses.

### Docstring

**Summary:** Merges index data, category totals, and location totals into a unified timeline data structure.

**Parameters:**

- index_by_year (dict): Dictionary containing index values organized by year.
- category_totals (dict): Dictionary containing category totals organized by year.
- location_totals (dict): Dictionary containing location totals organized by year.
**Returns:** list - A list representing the merged timeline data, where each element contains information about a specific year, including its index value, category totals, and location totals.

**Raises:**

- ValueError: When the input dictionaries (index_by_year, category_totals, location_totals) do not have consistent year ranges.
- TypeError: When the input parameters are not of the expected types (dict for index_by_year, category_totals, and location_totals).
**Examples:**

```python
>>> merge_timeline_data(index_by_year={2020: 100, 2021: 120}, category_totals={2020: {'A': 50, 'B': 60}, 2021: {'A': 70, 'B': 80}}, location_totals={2020: {'City': 40, 'Town': 30}, 2021: {'City': 50, 'Town': 40}})
[{'Year': 2020, 'Index': 100, 'CategoryTotals': {'A': 50, 'B': 60}, 'LocationTotals': {'City': 40, 'Town': 30}}, {'Year': 2021, 'Index': 120, 'CategoryTotals': {'A': 70, 'B': 80}, 'LocationTotals': {'City': 50, 'Town': 40}}]
```



---

## format_timeline_as_csv

### Description
Formats timeline data into a CSV string with specified headers.

### Conceptual Info

The format_timeline_as_csv shim function takes in timeline data and headers, and returns a formatted CSV string.

### Docstring

**Summary:** Formats timeline data into a CSV string with specified headers.

**Parameters:**

- timeline_data (str): The timeline data to be formatted into a CSV string. This should be a list or dictionary that can be converted into a CSV format.
- headers (str): The headers for the CSV string. This should be a list of column names.
**Returns:** str - The formatted CSV string.

**Raises:**

- ValueError: When the input timeline data or headers are invalid.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> format_timeline_as_csv(timeline_data=[{'Year': 2020, 'Index': 100, 'CategoryTotals': 1000, 'LocationTotals': 500}],
>>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
"Year,Index,CategoryTotals,LocationTotals\n2020,100,1000,500"
```

```python
>>> format_timeline_as_csv(timeline_data=[{'Year': 2021, 'Index': 120, 'CategoryTotals': 1200, 'LocationTotals': 600}],
>>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
"Year,Index,CategoryTotals,LocationTotals\n2021,120,1200,600"
```



---

## verify_timeline_integrity

### Description
Verifies the integrity of a timeline based on the provided CSV output and expected years.

### Conceptual Info

The verify_timeline_integrity shim function checks if the generated timeline matches the expected years and is correctly formatted.

### Docstring

**Summary:** Verifies the integrity of a timeline based on the provided CSV output and expected years.

**Parameters:**

- csv_output (str): The CSV output of the timeline.
- expected_years (str): The expected years in the timeline.
**Returns:** bool - Boolean indicating whether the timeline integrity verification was successful.

**Raises:**

- ValueError: When the CSV output is empty or does not contain the expected years.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,LocationTotals\n2020,1.0,100,200\n2021,1.1,120,250', expected_years='2020,2021')
True
```

```python
>>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,LocationTotals\n2020,1.0,100,200\n2022,1.1,120,250', expected_years='2020,2021')
False
```

