def create_year_index_mapping(years: str, index_values: str) -> str:
    """
    Generate a dictionary mapping years to index values from input strings of
    years and index values.

    Parameters
    ----------
    years : str
        A comma-separated string of years.
    index_values : str
        A comma-separated string of index values corresponding to the years.

    Returns
    -------
    str
        A dictionary as a string where keys are years and values are index
        values.

    Raises
    ------
    ValueError
        If the lengths of the years and index values strings do not match.
    TypeError
        If the input years or index values are not strings.

    Examples
    --------
    >>> create_year_index_mapping('2020,2021,2022', '10.5,11.2,12.1')
    {'2020': 10.5, '2021': 11.2, '2022': 12.1}

    >>> create_year_index_mapping('2015,2016', '20,21')
    {'2015': 20, '2016': 21}

    """
    if not isinstance(years, str):
        raise TypeError("Input years must be a string")
    if not isinstance(index_values, str):
        raise TypeError("Input index values must be a string")
    
    years_list = [year.strip() for year in years.split(',')]
    index_list = [value.strip() for value in index_values.split(',')]
    
    if len(years_list) != len(index_list):
        raise ValueError("The lengths of the years and index values strings do not match")
    
    result_dict = {}
    for year, index_value in zip(years_list, index_list):
        try:
            numeric_value = float(index_value)
            if numeric_value.is_integer():
                numeric_value = int(numeric_value)
            result_dict[year] = numeric_value
        except ValueError:
            result_dict[year] = index_value
    
    return str(result_dict)