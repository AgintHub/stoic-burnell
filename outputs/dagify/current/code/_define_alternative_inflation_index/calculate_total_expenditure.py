import ast


def calculate_total_expenditure(category_totals: str) -> float:
    """
    Calculates the total expenditure from a dictionary of category totals.

    Parameters
    ----------
    category_totals : str
        A string representation of the category totals.

    Returns
    -------
    float
        The total expenditure.

    Raises
    ------
    ValueError
        When the input category totals are invalid or empty.
    TypeError
        When the input category totals are of incorrect type.

    Examples
    --------
    >>> category_totals = '{'Food': 100, 'Transportation': 200}'
    >>> calculate_total_expenditure(category_totals=category_totals)
    300.0

    >>> category_totals = '{'Housing': 500, 'Entertainment': 300}'
    >>> calculate_total_expenditure(category_totals=category_totals)
    800.0

    """
    
    if not isinstance(category_totals, str):
        raise TypeError("Input category totals must be of type str")
    
    if not category_totals or category_totals.strip() == "":
        raise ValueError("Input category totals are invalid or empty")
    
    try:
        category_dict = ast.literal_eval(category_totals)
    except (ValueError, SyntaxError) as e:
        raise ValueError("Input category totals are invalid or empty") from e
    
    if not isinstance(category_dict, dict):
        raise ValueError("Input category totals are invalid or empty")
    
    if len(category_dict) == 0:
        raise ValueError("Input category totals are invalid or empty")
    
    total = 0.0
    for value in category_dict.values():
        if not isinstance(value, (int, float)):
            raise ValueError("Input category totals are invalid or empty")
        total += float(value)
    
    return total