import ast


def convert_location_aggregation_to_csv(aggregated_data: str) -> str:
    """
    Converts aggregated location data into a CSV string.

    Parameters
    ----------
    aggregated_data : str
        Input parameter containing aggregated location data in a format that
        can be converted to CSV.

    Returns
    -------
    str
        CSV string representation of the aggregated location data, with
        columns for Year, Location, and Expenditure Amount.

    Raises
    ------
    ValueError
        When input validation fails, such as if the input data is not in a
        valid format.
    TypeError
        When input types are incorrect, such as if the input data is not a
        string.

    Examples
    --------
    >>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'New
    York': 1000, 'Los Angeles': 2000}, '2023': {'New York': 1500, 'Los Angeles':
    2500}})
    "Year,Location,Expenditure Amount\n2022,New York,1000\n2022,Los
    Angeles,2000\n2023,New York,1500\n2023,Los Angeles,2500"

    >>> convert_location_aggregation_to_csv(aggregated_data={'2022': {'Chicago':
    500, 'Houston': 750}, '2023': {'Chicago': 1000, 'Houston': 1250}})
    "Year,Location,Expenditure Amount\n2022,Chicago,500\n2022,Houston,750\n2023,
    Chicago,1000\n2023,Houston,1250"

    """
    
    if not isinstance(aggregated_data, str):
        raise TypeError("Input data must be a string")
    
    try:
        data_dict = ast.literal_eval(aggregated_data)
    except (ValueError, SyntaxError) as e:
        raise ValueError("Input data is not in a valid format") from e
    
    if not isinstance(data_dict, dict):
        raise ValueError("Input data is not in a valid format")
    
    csv_lines = ["Year,Location,Expenditure Amount"]
    
    for year, locations in data_dict.items():
        if not isinstance(locations, dict):
            raise ValueError("Input data is not in a valid format")
        for location, amount in locations.items():
            csv_lines.append(f"{year},{location},{amount}")
    
    return "\n".join(csv_lines)