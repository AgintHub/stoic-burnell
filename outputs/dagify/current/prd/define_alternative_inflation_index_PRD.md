# define_alternative_inflation_index PRD

## Description
Specifies the methodology and weights for an alternative inflation index derived from household expenditure data.


## Conceptual Info

Defines a custom inflation index by assigning weights to spending categories based on aggregate household expenditure.

## Docstring

### Summary
Create an alternative inflation index from a CSV of household expenditures.

### Parameters

- **expenditure_csv** (str): CSV string where each row contains Year, Category, Location, and Expenditure_Amount.

### Returns

tuple[str, str, bool]: A tuple containing the index name, a CSV of Category,Weight pairs, and a boolean flag indicating success.

### Raises

- ValueError: If the input CSV is empty or malformed.
- KeyError: If expected columns (Year, Category, Location, Expenditure_Amount) are missing.

### Examples

```python
>>> expenditure_csv = (
...     "Year,Category,Location,Expenditure_Amount\n"
...     "2020,Food,NY,200\n"
...     "2020,Food,CA,250\n"
...     "2020,Clothing,NY,100\n"
>>> )
>>> name,weights,success = define_alternative_inflation_index(expenditure_csv)
>>> print(name)
>>> print(weights)
>>> print(success)
"Alternative CPI\nCategory,Weight\nFood,0.6\nClothing,0.4\nTrue"
```

```python
>>> try:
...     define_alternative_inflation_index("")
>>> except ValueError as e:
...     print("Caught error:", e)
"Caught error: Input CSV is empty or malformed."
```
