def validate_input_parameters(years: str, values: str, summary: str, analysis_success: str) -> bool:
    """
    Validates the input parameters for the analyze trends and benchmark node.

    Parameters
    ----------
    years : str
        Input parameter representing years.
    values : str
        Input parameter representing values.
    summary : str
        Input parameter representing summary.
    analysis_success : str
        Input parameter representing analysis success.

    Returns
    -------
    bool
        Boolean indicating whether the input parameters are valid.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> validate_input_parameters(years='2020,2021,2022',
    values='10.0,20.0,30.0', summary='Inflation trend summary',
    analysis_success='True')
    True

    >>> validate_input_parameters(years='2020,2021', values='10.0,20.0,30.0',
    summary='Inflation trend summary', analysis_success='True')
    False

    """
    try:
        if not isinstance(years, str) or not isinstance(values, str) or not isinstance(summary, str) or not isinstance(analysis_success, str):
            raise TypeError("All input parameters must be strings")
        
        if not years.strip() or not values.strip() or not summary.strip() or not analysis_success.strip():
            raise ValueError("Input parameters cannot be empty")
        
        years_list = [year.strip() for year in years.split(',') if year.strip()]
        values_list = [value.strip() for value in values.split(',') if value.strip()]
        
        if len(years_list) != len(values_list):
            return False
        
        for year in years_list:
            try:
                int(year)
            except ValueError:
                raise ValueError(f"Invalid year format: {year}")
        
        for value in values_list:
            try:
                float(value)
            except ValueError:
                raise ValueError(f"Invalid value format: {value}")
        
        if analysis_success.lower() not in ['true', 'false']:
            raise ValueError("analysis_success must be 'True' or 'False'")
        
        return True
        
    except (ValueError, TypeError):
        raise