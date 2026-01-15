import re


def determine_base_year(aggregated_data: str) -> int:
    """
    Determines the base year from the provided aggregated data.

    Parameters
    ----------
    aggregated_data : str
        A string containing aggregated data, expected to be in a format that
        allows for year identification.

    Returns
    -------
    int
        The determined base year.

    Raises
    ------
    ValueError
        When the input aggregated data is empty or does not contain a valid
        year.
    TypeError
        When the input aggregated data is not of type str.

    Examples
    --------
    >>> determine_base_year(aggregated_data='2020:100,2021:120,2022:150')
    >>> determine_base_year(aggregated_data='2010:50,2011:60,2012:70')
    2020

    >>> determine_base_year(aggregated_data='')
    >>> determine_base_year(aggregated_data=None)
    ValueError: Input aggregated data is empty or not provided.

    """
    if not isinstance(aggregated_data, str):
        raise TypeError("When the input aggregated data is not of type str.")
    
    if not aggregated_data or aggregated_data.strip() == "":
        raise ValueError("Input aggregated data is empty or not provided.")
    
    
    year_pattern = r'\b(19|20)\d{2}\b'
    matches = re.findall(year_pattern, aggregated_data)
    
    if not matches:
        raise ValueError("When the input aggregated data is empty or does not contain a valid year.")
    
    years = []
    for match in re.finditer(year_pattern, aggregated_data):
        years.append(int(match.group()))
    
    if not years:
        raise ValueError("When the input aggregated data is empty or does not contain a valid year.")
    
    return min(years)