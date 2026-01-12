import ast


def convert_weights_to_csv(weights_dict: str) -> str:
    """
    Converts a dictionary of weights into a CSV-formatted string.

    Parameters
    ----------
    weights_dict : str
        A string representation of a dictionary containing category weights.

    Returns
    -------
    str
        A CSV-formatted string of weights.

    Raises
    ------
    ValueError
        When the input dictionary is empty or malformed.
    TypeError
        When the input is not a string or the dictionary contains invalid
        types.

    Examples
    --------
    >>> weights_dict = '{'Category A': 0.5, 'Category B': 0.3, 'Category C':
    0.2}'
    >>> convert_weights_to_csv(weights_dict=weights_dict)
    'Category,Weight
    Category A,0.5
    Category B,0.3
    Category C,0.2'

    >>> weights_dict = '{'Food': 0.4, 'Housing': 0.3, 'Transportation': 0.3}'
    >>> convert_weights_to_csv(weights_dict=weights_dict)
    'Category,Weight
    Food,0.4
    Housing,0.3
    Transportation,0.3'

    """
    
    if not isinstance(weights_dict, str):
        raise TypeError("When the input is not a string or the dictionary contains invalid types.")
    
    try:
        parsed_dict = ast.literal_eval(weights_dict)
    except (ValueError, SyntaxError):
        raise ValueError("When the input dictionary is empty or malformed.")
    
    if not isinstance(parsed_dict, dict):
        raise TypeError("When the input is not a string or the dictionary contains invalid types.")
    
    if len(parsed_dict) == 0:
        raise ValueError("When the input dictionary is empty or malformed.")
    
    for key, value in parsed_dict.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            raise TypeError("When the input is not a string or the dictionary contains invalid types.")
    
    csv_lines = ["Category,Weight"]
    for category, weight in parsed_dict.items():
        csv_lines.append(f"{category},{weight}")
    
    return "\n".join(csv_lines)