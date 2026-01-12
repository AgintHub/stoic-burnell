def analyze_inflation_context(years: str, values: str, trend_summary: str) -> str:
    """
    Creates a narrative summary of the inflation context based on input years,
    values, and trend summary.

    Parameters
    ----------
    years : str
        List of years corresponding to calculated inflation rates.
    values : str
        List of inflation rates as percent changes for each calculated year.
    trend_summary : str
        Narrative summary of inflation trends and benchmarking results.

    Returns
    -------
    str
        Narrative summary of the inflation context.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> analyze_inflation_context(years='2010, 2011, 2012', values='2.5, 3.1,
    2.8', trend_summary='Inflation trend summary')
    "The inflation rates for 2010, 2011, and 2012 were 2.5%, 3.1%, and 2.8%,
    respectively. The overall trend indicates a moderate increase in inflation
    rates over the three-year period."

    """
    if not isinstance(years, str) or not isinstance(values, str) or not isinstance(trend_summary, str):
        raise TypeError("All input parameters must be strings")
    
    if not years.strip() or not values.strip():
        raise ValueError("Years and values cannot be empty")
    
    try:
        years_list = [year.strip() for year in years.split(',')]
        values_list = [float(value.strip()) for value in values.split(',')]
    except ValueError as e:
        raise ValueError("Failed to parse years or values") from e
    
    if len(years_list) != len(values_list):
        raise ValueError("Number of years must match number of values")
    
    if len(years_list) == 0:
        raise ValueError("At least one year and value must be provided")
    
    narrative_parts = []
    
    if len(years_list) == 1:
        narrative_parts.append(f"The inflation rate for {years_list[0]} was {values_list[0]}%.")
    elif len(years_list) == 2:
        narrative_parts.append(f"The inflation rates for {years_list[0]} and {years_list[1]} were {values_list[0]}% and {values_list[1]}%, respectively.")
    else:
        year_value_pairs = [f"{year} ({value}%)" for year, value in zip(years_list[:-1], values_list[:-1])]
        narrative_parts.append(f"The inflation rates for {', '.join(year_value_pairs)}, and {years_list[-1]} were {', '.join(map(str, values_list[:-1]))}%, and {values_list[-1]}%, respectively.")
    
    if trend_summary.strip():
        narrative_parts.append(trend_summary.strip())
    
    return ' '.join(narrative_parts)