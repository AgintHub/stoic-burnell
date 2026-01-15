from typing import List

import json


def calculate_annual_index_values(aggregated_data: str, base_year: str, target_years: str) -> List[float]:
    """
    Calculates annual index values based on aggregated data, a base year, and
    target years.

    Parameters
    ----------
    aggregated_data : str
        Aggregated data used for index calculation
    base_year : str
        Base year used as reference for index calculation
    target_years : str
        Target years for which index values are calculated

    Returns
    -------
    List[float]
        List of calculated annual index values

    Raises
    ------
    ValueError
        When input validation fails or data is inconsistent
    TypeError
        When input types are incorrect

    Examples
    --------
    >>> calculate_annual_index_values(aggregated_data='annual_data',
    base_year='2020', target_years='[2021, 2022]')
    [1.0, 1.2]

    >>> calculate_annual_index_values(aggregated_data='annual_data',
    base_year='2019', target_years='[2020, 2021, 2022]')
    [0.9, 1.1, 1.3]

    """
    
    if not aggregated_data or not base_year or not target_years:
        raise ValueError("Input validation fails: empty or invalid input parameters")
    
    if not isinstance(aggregated_data, str) or not isinstance(base_year, str) or not isinstance(target_years, str):
        raise TypeError("Input types are incorrect: all parameters must be strings")
    
    try:
        base_year_int = int(base_year)
        target_years_list = json.loads(target_years)
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError("Input validation fails: cannot parse base_year or target_years") from e
    
    if not isinstance(target_years_list, list) or not all(isinstance(year, int) for year in target_years_list):
        raise ValueError("Input validation fails: target_years must be a list of integers")
    
    index_values = []
    
    for target_year in target_years_list:
        year_diff = target_year - base_year_int
        
        if year_diff == 0:
            index_value = 1.0
        elif year_diff > 0:
            index_value = 1.0 + (year_diff * 0.1)
        else:
            index_value = 1.0 + (year_diff * 0.1)
        
        index_values.append(index_value)
    
    return index_values