import csv
import io
import json


def validate_and_parse_csv(csv_string: str) -> str:
    """
    Validates and parses a CSV string into a structured format.

    Parameters
    ----------
    csv_string : str
        The input CSV string to be validated and parsed.

    Returns
    -------
    dict
        A dictionary containing a boolean 'is_valid' indicating whether the
        CSV string is valid, and a list of dictionaries 'parsed_data'
        containing the parsed CSV data.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or invalid.
    TypeError
        When the input type is not a string.

    Examples
    --------
    >>> validate_and_parse_csv('Year,Index,CategoryTotals,LocationTotals')
    >>> validate_and_parse_csv('2022,100,1000,5000')
    {'is_valid': True, 'parsed_data': [{'Year': '2022', 'Index': '100',
    'CategoryTotals': '1000', 'LocationTotals': '5000'}]}

    >>> validate_and_parse_csv('invalid_csv_string')
    {'is_valid': False, 'parsed_data': []}

    """
    
    if not isinstance(csv_string, str):
        raise TypeError("Input must be a string")
    
    try:
        csv_file = io.StringIO(csv_string.strip())
        
        reader = csv.DictReader(csv_file)
        
        parsed_data = list(reader)
        
        if not parsed_data and csv_string.strip():
            return json.dumps({'is_valid': False, 'parsed_data': []})
        
        result = {
            'is_valid': True,
            'parsed_data': parsed_data
        }
        
        return json.dumps(result)
        
    except (csv.Error, UnicodeDecodeError):
        return json.dumps({'is_valid': False, 'parsed_data': []})
    except Exception:
        return json.dumps({'is_valid': False, 'parsed_data': []})