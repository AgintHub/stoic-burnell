# _define_alternative_inflation_index - Complete PRD Documentation

## Overview
PRDs for nodes in the '_define_alternative_inflation_index' module.

## Table of Contents

- [validate_expenditure_csv_format](#validate_expenditure_csv_format)

- [parse_expenditure_csv](#parse_expenditure_csv)

- [calculate_category_expenditure_totals](#calculate_category_expenditure_totals)

- [calculate_total_expenditure](#calculate_total_expenditure)

- [calculate_category_weights](#calculate_category_weights)

- [generate_index_name](#generate_index_name)

- [convert_weights_to_csv](#convert_weights_to_csv)

- [validate_methodology_completion](#validate_methodology_completion)



---

## validate_expenditure_csv_format

### Description
Validates the format of a given expenditure CSV string.

### Conceptual Info

The validate_expenditure_csv_format shim function checks if a given CSV string containing expenditure data conforms to the expected format, which includes columns for Year, Category, Location, and Expenditure_Amount.

### Docstring

**Summary:** Validates the format of a given expenditure CSV string.

**Parameters:**

- csv_data (str): The input CSV string to be validated, containing columns for Year, Category, Location, and Expenditure_Amount.
**Returns:** bool - True if the CSV string is well-formatted, False otherwise.

**Raises:**

- ValueError: When the input CSV string is empty or malformed.
- TypeError: When the input is not a string.
**Examples:**

```python
>>> import pandas as pd
>>> csv_data = 'Year,Category,Location,Expenditure_Amount\n2020,Food,New York,100.0\n2021,Housing,Los Angeles,200.0'
>>> validate_expenditure_csv_format(csv_data=csv_data)
True
```

```python
>>> csv_data = 'Invalid,Format'
>>> validate_expenditure_csv_format(csv_data=csv_data)
False
```



---

## parse_expenditure_csv

### Description
Parses a CSV string of expenditure data into a structured format.

### Conceptual Info

This shim function plays a crucial role in processing household expenditure data by converting raw CSV strings into a structured format for further analysis.

### Docstring

**Summary:** Parses a CSV string of expenditure data into a structured format.

**Parameters:**

- csv_data (str): CSV string of expenditure data with columns: Year, Category, Location, Expenditure_Amount.
**Returns:** list - List of dictionaries representing the parsed expenditure data.

**Raises:**

- ValueError: When the input CSV string is malformed or empty.
- TypeError: When the input type is not a string.
**Examples:**

```python
>>> parse_expenditure_csv('Year,Category,Location,Expenditure_Amount\\n2020,Food,New York,1000\\n2021,Housing,Los Angeles,2000')
[{'Year': '2020', 'Category': 'Food', 'Location': 'New York', 'Expenditure_Amount': '1000'}, {'Year': '2021', 'Category': 'Housing', 'Location': 'Los Angeles', 'Expenditure_Amount': '2000'}]
```

```python
>>> parse_expenditure_csv('')
 raises ValueError
```



---

## calculate_category_expenditure_totals

### Description
This shim calculates the total expenditure for each category from the provided expenditure data.

### Conceptual Info

The calculate_category_expenditure_totals shim plays a crucial role in calculating category-wise expenditures, which is essential for defining alternative inflation indices.

### Docstring

**Summary:** Calculates the total expenditure for each category from the provided expenditure data.

**Parameters:**

- expenditure_data (str): A string representing a list of dictionaries, where each dictionary contains 'Category', 'Year', 'Location', and 'Expenditure_Amount' keys.
**Returns:** str - A JSON string representing a dictionary with categories as keys and their total expenditures as values.

**Raises:**

- ValueError: When the input expenditure data is malformed or empty.
- TypeError: When the input expenditure data is not a string or does not match the expected format.
**Examples:**

```python
>>> expenditure_data = '[{"Category": "Food", "Year": 2020, "Location": "New York", "Expenditure_Amount": 1000.0}, {"Category": "Food", "Year": 2021, "Location": "New York", "Expenditure_Amount": 1200.0}]'
>>> result = calculate_category_expenditure_totals(expenditure_data)
{'Food': 2200.0}
```

```python
>>> expenditure_data = '[{"Category": "Housing", "Year": 2020, "Location": "Los Angeles", "Expenditure_Amount": 5000.0}, {"Category": "Transportation", "Year": 2021, "Location": "Chicago", "Expenditure_Amount": 2000.0}]'
>>> result = calculate_category_expenditure_totals(expenditure_data)
{'Housing': 5000.0, 'Transportation': 2000.0}
```



---

## calculate_total_expenditure

### Description
Calculates the total expenditure from a dictionary of category totals.

### Conceptual Info

This shim function calculates the total expenditure from a dictionary of category totals, which is used in the define_alternative_inflation_index function.

### Docstring

**Summary:** Calculates the total expenditure from a dictionary of category totals.

**Parameters:**

- category_totals (str): A string representation of the category totals.
**Returns:** float - The total expenditure.

**Raises:**

- ValueError: When the input category totals are invalid or empty.
- TypeError: When the input category totals are of incorrect type.
**Examples:**

```python
>>> category_totals = '{'Food': 100, 'Transportation': 200}'
>>> calculate_total_expenditure(category_totals=category_totals)
300.0
```

```python
>>> category_totals = '{'Housing': 500, 'Entertainment': 300}'
>>> calculate_total_expenditure(category_totals=category_totals)
800.0
```



---

## calculate_category_weights

### Description
This shim node calculates category weights based on category totals and total expenditure.

### Conceptual Info

The calculate_category_weights shim is responsible for determining the proportional weight of each category in the overall expenditure, which is crucial for defining an alternative inflation index.

### Docstring

**Summary:** Calculates category weights based on category totals and total expenditure, returning a dictionary with these weights.

**Parameters:**

- category_totals (dict): A dictionary where keys are category names and values are the total expenditure for each category.
- total_expenditure (float): The total expenditure across all categories.
**Returns:** str - A JSON string representing a dictionary where keys are category names and values are their respective weights in the overall expenditure.

**Raises:**

- ValueError: If the total expenditure is zero or negative, or if category totals are not provided.
- TypeError: If category totals are not a dictionary or if total expenditure is not a number.
**Examples:**

```python
>>> category_weights = calculate_category_weights(category_totals={'Food': 1000, 'Transport': 500}, total_expenditure=1500)
{'Food': 0.6666666666666666, 'Transport': 0.3333333333333333}
```

```python
>>> category_weights = calculate_category_weights(category_totals={'Housing': 2000, 'Utilities': 300}, total_expenditure=2300)
{'Housing': 0.8695652173913043, 'Utilities': 0.1304347826086957}
```



---

## generate_index_name

### Description
This shim generates a name for an alternative inflation index based on the input expenditure data.

### Conceptual Info

The generate_index_name shim is responsible for creating a unique and descriptive name for an alternative inflation index, which is crucial for identifying and distinguishing different inflation indices in the system.

### Docstring

**Summary:** Generates a name for an alternative inflation index.

**Returns:** str - A string representing the generated name of the alternative inflation index.

**Raises:**

- ValueError: If the index name generation fails due to internal errors.
- TypeError: If the input parameters are of incorrect type.
**Examples:**

```python
>>> index_name = generate_index_name()
'Alternative_Inflation_Index_1'
```

```python
>>> index_name = generate_index_name()
'Custom_Inflation_Index_2024'
```



---

## convert_weights_to_csv

### Description
Converts a dictionary of weights into a CSV-formatted string.

### Conceptual Info

The shim function convert_weights_to_csv is used to transform a dictionary of category weights into a CSV-formatted string, which is a required output format for the alternative inflation index weights.

### Docstring

**Summary:** Converts a dictionary of weights into a CSV-formatted string.

**Parameters:**

- weights_dict (str): A string representation of a dictionary containing category weights.
**Returns:** str - A CSV-formatted string of weights.

**Raises:**

- ValueError: When the input dictionary is empty or malformed.
- TypeError: When the input is not a string or the dictionary contains invalid types.
**Examples:**

```python
>>> weights_dict = '{'Category A': 0.5, 'Category B': 0.3, 'Category C': 0.2}'
>>> convert_weights_to_csv(weights_dict=weights_dict)
'Category,Weight
Category A,0.5
Category B,0.3
Category C,0.2'
```

```python
>>> weights_dict = '{'Food': 0.4, 'Housing': 0.3, 'Transportation': 0.3}'
>>> convert_weights_to_csv(weights_dict=weights_dict)
'Category,Weight
Food,0.4
Housing,0.3
Transportation,0.3'
```



---

## validate_methodology_completion

### Description
Validates the completion of a methodology based on the provided weights and index name.

### Conceptual Info

The validate_methodology_completion shim is responsible for verifying that a methodology is complete based on the provided weights and index name.

### Docstring

**Summary:** Validates the completion of a methodology based on the provided weights and index name.

**Parameters:**

- weights (str): The weights to be used for validation.
- index_name (str): The index name to be used for validation.
**Returns:** bool - A boolean indicating whether the methodology is complete.

**Raises:**

- ValueError: When the input validation fails.
- TypeError: When the input types are incorrect.
**Examples:**

```python
>>> validate_methodology_completion(weights='category1=0.5,category2=0.5', index_name='example_index')
True
```

```python
>>> validate_methodology_completion(weights='category1=0.3,category2=0.7', index_name='another_index')
True
```

