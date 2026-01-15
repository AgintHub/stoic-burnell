import random
import datetime


def generate_index_name() -> str:
    """
    Generates a name for an alternative inflation index.

    Returns
    -------
    str
        A string representing the generated name of the alternative
        inflation index.

    Raises
    ------
    ValueError
        If the index name generation fails due to internal errors.
    TypeError
        If the input parameters are of incorrect type.

    Examples
    --------
    >>> index_name = generate_index_name()
    'Alternative_Inflation_Index_1'

    >>> index_name = generate_index_name()
    'Custom_Inflation_Index_2024'

    """
    
    base_names = [
        "Alternative_Inflation_Index",
        "Custom_Inflation_Index",
        "Modified_Price_Index",
        "Adjusted_Inflation_Measure"
    ]
    
    try:
        current_year = datetime.datetime.now().year
        random_suffix = random.randint(1, 9999)
        
        if random.choice([True, False]):
            index_name = f"{random.choice(base_names)}_{random_suffix}"
        else:
            index_name = f"{random.choice(base_names)}_{current_year}"
        
        return index_name
    except Exception as e:
        raise ValueError("Index name generation failed due to internal errors") from e