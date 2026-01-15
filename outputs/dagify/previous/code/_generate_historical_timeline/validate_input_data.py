import ast


def validate_input_data(index_input: str, breakdown_input: str) -> bool:
    """
    Validates the input data for generating a historical timeline.

    Parameters
    ----------
    index_input : str
        Input parameter containing index series data. It should be a string
        representation of a ComputeIndexSeriesOutput object.
    breakdown_input : str
        Input parameter containing category and location breakdown data. It
        should be a string representation of a
        ComputeCategoryLocationBreakdownsOutput object.

    Returns
    -------
    bool
        Boolean indicating whether the input data is valid.

    Raises
    ------
    ValueError
        When input validation fails due to missing or incorrect data.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120],
    'is_index_successful': True})
    >>> breakdown_input = str({'category_spending_csv':
    'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv':
    'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90',
    'is_breakdown_successful': True})
    >>> validate_input_data(index_input=index_input,
    breakdown_input=breakdown_input)
    True

    >>> index_input = str({'years': [2020, 2021], 'index_values': [100, 120]})
    >>> breakdown_input = str({'category_spending_csv':
    'Year,Category,Total\n2020,A,100\n2021,B,120', 'location_spending_csv':
    'Year,HouseholdLocation,Total\n2020,Urban,80\n2021,Rural,90'})
    >>> validate_input_data(index_input=index_input,
    breakdown_input=breakdown_input)
    False

    """
    
    try:
        index_data = ast.literal_eval(index_input)
        breakdown_data = ast.literal_eval(breakdown_input)
        
        if not isinstance(index_data, dict):
            return False
            
        if 'is_index_successful' not in index_data:
            return False
            
        if not index_data.get('is_index_successful', False):
            return False
            
        if 'years' not in index_data or 'index_values' not in index_data:
            return False
            
        if not isinstance(index_data['years'], list) or not isinstance(index_data['index_values'], list):
            return False
            
        if not isinstance(breakdown_data, dict):
            return False
            
        if 'is_breakdown_successful' not in breakdown_data:
            return False
            
        if not breakdown_data.get('is_breakdown_successful', False):
            return False
            
        if 'category_spending_csv' not in breakdown_data or 'location_spending_csv' not in breakdown_data:
            return False
            
        if not isinstance(breakdown_data['category_spending_csv'], str) or not isinstance(breakdown_data['location_spending_csv'], str):
            return False
            
        return True
        
    except (ValueError, SyntaxError, TypeError):
        return False