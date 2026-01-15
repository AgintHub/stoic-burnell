import json


def calculate_category_expenditure_totals(expenditure_data: str) -> str:
    """
    Calculates the total expenditure for each category from the provided
    expenditure data.

    Parameters
    ----------
    expenditure_data : str
        A string representing a list of dictionaries, where each dictionary
        contains 'Category', 'Year', 'Location', and 'Expenditure_Amount'
        keys.

    Returns
    -------
    str
        A JSON string representing a dictionary with categories as keys and
        their total expenditures as values.

    Raises
    ------
    ValueError
        When the input expenditure data is malformed or empty.
    TypeError
        When the input expenditure data is not a string or does not match
        the expected format.

    Examples
    --------
    >>> expenditure_data = '[{"Category": "Food", "Year": 2020, "Location": "New
    York", "Expenditure_Amount": 1000.0}, {"Category": "Food", "Year": 2021,
    "Location": "New York", "Expenditure_Amount": 1200.0}]'
    >>> result = calculate_category_expenditure_totals(expenditure_data)
    {'Food': 2200.0}

    >>> expenditure_data = '[{"Category": "Housing", "Year": 2020, "Location":
    "Los Angeles", "Expenditure_Amount": 5000.0}, {"Category": "Transportation",
    "Year": 2021, "Location": "Chicago", "Expenditure_Amount": 2000.0}]'
    >>> result = calculate_category_expenditure_totals(expenditure_data)
    {'Housing': 5000.0, 'Transportation': 2000.0}

    """
    
    if not isinstance(expenditure_data, str):
        raise TypeError("Input expenditure data must be a string")
    
    if not expenditure_data.strip():
        raise ValueError("Input expenditure data cannot be empty")
    
    try:
        data = json.loads(expenditure_data)
    except json.JSONDecodeError:
        raise ValueError("Input expenditure data is malformed - not valid JSON")
    
    if not isinstance(data, list):
        raise TypeError("Expenditure data must be a list of dictionaries")
    
    if len(data) == 0:
        raise ValueError("Expenditure data cannot be empty")
    
    category_totals = {}
    
    for item in data:
        if not isinstance(item, dict):
            raise TypeError("Each item in expenditure data must be a dictionary")
        
        required_keys = ['Category', 'Year', 'Location', 'Expenditure_Amount']
        for key in required_keys:
            if key not in item:
                raise ValueError(f"Missing required key: {key}")
        
        category = item['Category']
        expenditure_amount = item['Expenditure_Amount']
        
        if not isinstance(expenditure_amount, (int, float)):
            raise TypeError("Expenditure_Amount must be a number")
        
        if category in category_totals:
            category_totals[category] += expenditure_amount
        else:
            category_totals[category] = expenditure_amount
    
    return json.dumps(category_totals)