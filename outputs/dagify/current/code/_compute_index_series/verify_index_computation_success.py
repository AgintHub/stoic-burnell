import re


def verify_index_computation_success(years: str, index_values: str) -> bool:
    """
    Verifies if the index computation was successful based on the provided years
    and index values.

    Parameters
    ----------
    years : str
        Input parameter representing the years for which the index was
        calculated.
    index_values : str
        Input parameter representing the corresponding index values for each
        year.

    Returns
    -------
    bool
        Boolean indicating whether the index computation was successful.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> verify_index_computation_success(years='2020,2021,2022',
    index_values='100.0,120.0,110.0')
    True

    >>> verify_index_computation_success(years='2020,2021,2022',
    index_values='100.0,NaN,110.0')
    False

    """
    
    if not isinstance(years, str) or not isinstance(index_values, str):
        raise TypeError("Input types are incorrect")
    
    if not years.strip() or not index_values.strip():
        raise ValueError("When input validation fails")
    
    try:
        years_list = [year.strip() for year in years.split(',')]
        index_values_list = [value.strip() for value in index_values.split(',')]
        
        if len(years_list) != len(index_values_list):
            return False
        
        if len(years_list) == 0:
            return False
        
        for year in years_list:
            if not re.match(r'^\d{4}$', year):
                return False
        
        for value in index_values_list:
            if value.lower() in ['nan', 'null', 'none', '']:
                return False
            try:
                float(value)
            except ValueError:
                return False
        
        return True
        
    except Exception:
        raise ValueError("When input validation fails")