import json


def calculate_category_weights(category_totals: str, total_expenditure: str) -> str:
    """
    Calculates category weights based on category totals and total expenditure,
    returning a dictionary with these weights.

    Parameters
    ----------
    category_totals : dict
        A dictionary where keys are category names and values are the total
        expenditure for each category.
    total_expenditure : float
        The total expenditure across all categories.

    Returns
    -------
    str
        A JSON string representing a dictionary where keys are category
        names and values are their respective weights in the overall
        expenditure.

    Raises
    ------
    ValueError
        If the total expenditure is zero or negative, or if category totals
        are not provided.
    TypeError
        If category totals are not a dictionary or if total expenditure is
        not a number.

    Examples
    --------
    >>> category_weights = calculate_category_weights(category_totals={'Food':
    1000, 'Transport': 500}, total_expenditure=1500)
    {'Food': 0.6666666666666666, 'Transport': 0.3333333333333333}

    >>> category_weights =
    calculate_category_weights(category_totals={'Housing': 2000, 'Utilities':
    300}, total_expenditure=2300)
    {'Housing': 0.8695652173913043, 'Utilities': 0.1304347826086957}

    """
    
    try:
        category_totals_dict = json.loads(category_totals)
    except (json.JSONDecodeError, TypeError):
        raise TypeError("category_totals must be a valid JSON string representing a dictionary")
    
    if not isinstance(category_totals_dict, dict):
        raise TypeError("category_totals must be a dictionary")
    
    if not category_totals_dict:
        raise ValueError("category totals are not provided")
    
    try:
        total_exp = float(total_expenditure)
    except (ValueError, TypeError):
        raise TypeError("total expenditure is not a number")
    
    if total_exp <= 0:
        raise ValueError("total expenditure is zero or negative")
    
    weights = {}
    for category, total in category_totals_dict.items():
        weights[category] = total / total_exp
    
    return json.dumps(weights)