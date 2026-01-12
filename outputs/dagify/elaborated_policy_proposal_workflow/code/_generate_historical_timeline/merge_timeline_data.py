import json


def merge_timeline_data(index_by_year: str, category_totals: str, location_totals: str) -> str:
    """
    Merges index data, category totals, and location totals into a unified
    timeline data structure.

    Parameters
    ----------
    index_by_year : dict
        Dictionary containing index values organized by year.
    category_totals : dict
        Dictionary containing category totals organized by year.
    location_totals : dict
        Dictionary containing location totals organized by year.

    Returns
    -------
    list
        A list representing the merged timeline data, where each element
        contains information about a specific year, including its index
        value, category totals, and location totals.

    Raises
    ------
    ValueError
        When the input dictionaries (index_by_year, category_totals,
        location_totals) do not have consistent year ranges.
    TypeError
        When the input parameters are not of the expected types (dict for
        index_by_year, category_totals, and location_totals).

    Examples
    --------
    >>> merge_timeline_data(index_by_year={2020: 100, 2021: 120},
    category_totals={2020: {'A': 50, 'B': 60}, 2021: {'A': 70, 'B': 80}},
    location_totals={2020: {'City': 40, 'Town': 30}, 2021: {'City': 50, 'Town':
    40}})
    [{'Year': 2020, 'Index': 100, 'CategoryTotals': {'A': 50, 'B': 60},
    'LocationTotals': {'City': 40, 'Town': 30}}, {'Year': 2021, 'Index': 120,
    'CategoryTotals': {'A': 70, 'B': 80}, 'LocationTotals': {'City': 50, 'Town':
    40}}]

    """
    
    try:
        index_dict = json.loads(index_by_year)
        category_dict = json.loads(category_totals)
        location_dict = json.loads(location_totals)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format in input parameters") from e
    
    if not isinstance(index_dict, dict):
        raise TypeError("index_by_year must be a dictionary")
    if not isinstance(category_dict, dict):
        raise TypeError("category_totals must be a dictionary")
    if not isinstance(location_dict, dict):
        raise TypeError("location_totals must be a dictionary")
    
    index_years = set(index_dict.keys())
    category_years = set(category_dict.keys())
    location_years = set(location_dict.keys())
    
    if not (index_years == category_years == location_years):
        raise ValueError("Input dictionaries do not have consistent year ranges")
    
    timeline = []
    for year in sorted(index_years, key=lambda x: int(x) if isinstance(x, str) and x.isdigit() else x):
        timeline_entry = {
            'Year': int(year) if isinstance(year, str) and year.isdigit() else year,
            'Index': index_dict[year],
            'CategoryTotals': category_dict[year],
            'LocationTotals': location_dict[year]
        }
        timeline.append(timeline_entry)
    
    return json.dumps(timeline)