import json
import csv
import io


def format_timeline_as_csv(timeline_data: str, headers: str) -> str:
    """
    Formats timeline data into a CSV string with specified headers.

    Parameters
    ----------
    timeline_data : str
        The timeline data to be formatted into a CSV string. This should be
        a list or dictionary that can be converted into a CSV format.
    headers : str
        The headers for the CSV string. This should be a list of column
        names.

    Returns
    -------
    str
        The formatted CSV string.

    Raises
    ------
    ValueError
        When the input timeline data or headers are invalid.
    TypeError
        When the input types are incorrect.

    Examples
    --------
    >>> format_timeline_as_csv(timeline_data=[{'Year': 2020, 'Index': 100,
    'CategoryTotals': 1000, 'LocationTotals': 500}],
    >>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
    "Year,Index,CategoryTotals,LocationTotals\n2020,100,1000,500"

    >>> format_timeline_as_csv(timeline_data=[{'Year': 2021, 'Index': 120,
    'CategoryTotals': 1200, 'LocationTotals': 600}],
    >>> headers=['Year', 'Index', 'CategoryTotals', 'LocationTotals'])
    "Year,Index,CategoryTotals,LocationTotals\n2021,120,1200,600"

    """
    
    try:
        if isinstance(timeline_data, str):
            parsed_data = json.loads(timeline_data)
        else:
            parsed_data = timeline_data
    except (json.JSONDecodeError, TypeError) as e:
        raise ValueError("Invalid timeline data format") from e
    
    try:
        if isinstance(headers, str):
            parsed_headers = json.loads(headers)
        else:
            parsed_headers = headers
    except (json.JSONDecodeError, TypeError) as e:
        raise ValueError("Invalid headers format") from e
    
    if not isinstance(parsed_data, list):
        raise TypeError("Timeline data must be a list")
    
    if not isinstance(parsed_headers, list):
        raise TypeError("Headers must be a list")
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(parsed_headers)
    
    for row_data in parsed_data:
        if isinstance(row_data, dict):
            row = [row_data.get(header, '') for header in parsed_headers]
        else:
            raise TypeError("Each timeline data item must be a dictionary")
        writer.writerow(row)
    
    return output.getvalue().strip()