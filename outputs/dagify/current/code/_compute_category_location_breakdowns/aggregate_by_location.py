import json


def aggregate_by_location(data: str, year_col: str, location_col: str, amount_col: str) -> str:
    """
    Aggregates expenditure data by location, calculating total expenditures for
    each location in each year.

    Parameters
    ----------
    data : str
        Input expenditure data as a string, expected to be a list of records
        containing year, location, and amount information.
    year_col : str
        The column name in the data that represents the year.
    location_col : str
        The column name in the data that represents the location.
    amount_col : str
        The column name in the data that represents the expenditure amount.

    Returns
    -------
    str
        A dictionary containing location-based expenditure amounts for each
        year, returned as a JSON string.

    Raises
    ------
    ValueError
        When the input data does not contain the specified year, location,
        or amount columns.
    TypeError
        When the input data or column names are of incorrect types.

    Examples
    --------
    >>> data = '[{"Year": 2020, "Location": "New York", "Expenditure_Amount":
    100}, {"Year": 2020, "Location": "Chicago", "Expenditure_Amount": 200}]'
    >>> year_col = 'Year'
    >>> location_col = 'Location'
    >>> amount_col = 'Expenditure_Amount'
    >>> result = aggregate_by_location(data, year_col, location_col, amount_col)
    {'2020': {'New York': 100, 'Chicago': 200}}

    """
    
    try:
        records = json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format in input data") from e
    
    if not isinstance(records, list):
        raise TypeError("Input data must be a list of records")
    
    if not isinstance(year_col, str) or not isinstance(location_col, str) or not isinstance(amount_col, str):
        raise TypeError("Column names must be strings")
    
    result = {}
    
    for record in records:
        if not isinstance(record, dict):
            continue
            
        if year_col not in record:
            raise ValueError(f"Year column '{year_col}' not found in data")
        if location_col not in record:
            raise ValueError(f"Location column '{location_col}' not found in data")
        if amount_col not in record:
            raise ValueError(f"Amount column '{amount_col}' not found in data")
        
        year = str(record[year_col])
        location = record[location_col]
        amount = record[amount_col]
        
        if year not in result:
            result[year] = {}
        
        if location not in result[year]:
            result[year][location] = 0
        
        result[year][location] += amount
    
    return json.dumps(result)