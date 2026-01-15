import csv
from io import StringIO


def merge_expenditure_with_weights(expenditure_data: str, weights_data: str) -> str:
    """
    Merges expenditure data with weights data to produce a combined dataset.

    Parameters
    ----------
    expenditure_data : str
        The input expenditure data as a string representation.
    weights_data : str
        The input weights data as a string representation.

    Returns
    -------
    str
        The merged dataset as a string representation.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> expenditure_data = 'Year,Category,Location,Expenditure_Amount'
    >>> weights_data = 'Category,Weight'
    >>> merge_expenditure_with_weights(expenditure_data, weights_data)
    'Merged dataset as a string representation'

    """
    
    if not isinstance(expenditure_data, str):
        raise TypeError("expenditure_data must be a string")
    if not isinstance(weights_data, str):
        raise TypeError("weights_data must be a string")
    
    if not expenditure_data.strip():
        raise ValueError("expenditure_data cannot be empty")
    if not weights_data.strip():
        raise ValueError("weights_data cannot be empty")
    
    try:
        expenditure_reader = csv.DictReader(StringIO(expenditure_data))
        expenditure_rows = list(expenditure_reader)
    except Exception as e:
        raise ValueError("Failed to parse expenditure_data as CSV") from e
    
    try:
        weights_reader = csv.DictReader(StringIO(weights_data))
        weights_rows = list(weights_reader)
    except Exception as e:
        raise ValueError("Failed to parse weights_data as CSV") from e
    
    weights_dict = {}
    for row in weights_rows:
        category = row.get('Category')
        weight = row.get('Weight')
        if category and weight:
            weights_dict[category] = weight
    
    merged_rows = []
    for exp_row in expenditure_rows:
        category = exp_row.get('Category')
        weight = weights_dict.get(category, '')
        merged_row = exp_row.copy()
        merged_row['Weight'] = weight
        merged_rows.append(merged_row)
    
    if not merged_rows:
        return ""
    
    output = StringIO()
    fieldnames = list(merged_rows[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(merged_rows)
    
    return output.getvalue()