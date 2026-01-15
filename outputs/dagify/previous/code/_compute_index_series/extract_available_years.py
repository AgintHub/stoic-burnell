from typing import List

import json


def extract_available_years(aggregated_data: str) -> List[int]:
    """
    Extracts a list of available years from the aggregated data.

    Parameters
    ----------
    aggregated_data : str
        The aggregated data from which to extract available years.

    Returns
    -------
    List[int]
        A list of available years.

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> extract_available_years(aggregated_data='{"2020": 10, "2021": 20,
    "2022": 30}')
    [2020, 2021, 2022]

    >>> extract_available_years(aggregated_data='{}')
    []

    """
    
    if not isinstance(aggregated_data, str):
        raise TypeError("Input types are incorrect.")
    
    try:
        data = json.loads(aggregated_data)
    except json.JSONDecodeError:
        raise ValueError("When input validation fails.")
    
    if not isinstance(data, dict):
        raise ValueError("When input validation fails.")
    
    years = []
    for key in data.keys():
        try:
            year = int(key)
            years.append(year)
        except ValueError:
            continue
    
    return sorted(years)