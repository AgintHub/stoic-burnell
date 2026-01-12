import json
import csv
from io import StringIO


def aggregate_by_category(data: str, year_col: str, category_col: str, amount_col: str) -> str:
    """
    Aggregate expenditure data by category, summing expenditure amounts for each
    category in a given year.

    Parameters
    ----------
    data : str
        The input data to be aggregated, expected to be a list of records or
        a string representing a CSV structure.
    year_col : str
        The column name in the data that represents the year.
    category_col : str
        The column name in the data that represents the category.
    amount_col : str
        The column name in the data that represents the expenditure amount.

    Returns
    -------
    dict
        A dictionary where keys are categories and values are the total
        expenditure amounts for each category, structured as '{category:
        total_amount}'.

    Raises
    ------
    ValueError
        If the input data is not in the expected format or if required
        columns are missing.
    TypeError
        If the input parameters are not of the expected types.

    Examples
    --------
    >>> data = [{'Year': '2022', 'Category': 'Food', 'Expenditure_Amount': 100},
    ...         {'Year': '2022', 'Category': 'Transport', 'Expenditure_Amount':
    50}]
    >>> year_col = 'Year'
    >>> category_col = 'Category'
    >>> amount_col = 'Expenditure_Amount'
    >>> result = aggregate_by_category(data, year_col, category_col, amount_col)
    {'Food': 100, 'Transport': 50}

    """
    
    try:
        parsed_data = json.loads(data)
    except json.JSONDecodeError:
        try:
            csv_reader = csv.DictReader(StringIO(data))
            parsed_data = list(csv_reader)
        except Exception:
            raise ValueError("Input data is not in expected format (JSON list or CSV)")
    
    if not isinstance(parsed_data, list):
        raise TypeError("Input data must be a list of records")
    
    if not parsed_data:
        return json.dumps({})
    
    required_columns = {year_col, category_col, amount_col}
    if parsed_data:
        available_columns = set(parsed_data[0].keys())
        missing_columns = required_columns - available_columns
        if missing_columns:
            raise ValueError(f"Required columns missing: {missing_columns}")
    
    category_totals = {}
    
    for record in parsed_data:
        if not isinstance(record, dict):
            raise TypeError("Each record must be a dictionary")
        
        category = record.get(category_col)
        amount_str = record.get(amount_col)
        
        if category is None or amount_str is None:
            continue
        
        try:
            amount = float(amount_str)
        except (ValueError, TypeError):
            continue
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    
    return json.dumps(category_totals)