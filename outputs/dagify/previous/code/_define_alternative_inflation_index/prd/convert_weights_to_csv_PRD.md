# convert_weights_to_csv PRD

## Description
Converts a dictionary of weights into a CSV-formatted string.


## Conceptual Info

The shim function convert_weights_to_csv is used to transform a dictionary of category weights into a CSV-formatted string, which is a required output format for the alternative inflation index weights.

## Docstring

### Summary
Converts a dictionary of weights into a CSV-formatted string.

### Parameters

- **weights_dict** (str): A string representation of a dictionary containing category weights.

### Returns

str: A CSV-formatted string of weights.

### Raises

- ValueError: When the input dictionary is empty or malformed.
- TypeError: When the input is not a string or the dictionary contains invalid types.

### Examples

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
