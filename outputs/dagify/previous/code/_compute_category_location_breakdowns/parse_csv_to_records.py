import csv


def parse_csv_to_records(csv_string: str) -> str:
    """
    Parses a CSV string into a list of records.

    Parameters
    ----------
    csv_string : str
        The input CSV string to be parsed.

    Returns
    -------
    list
        A list of records parsed from the input CSV string, where each
        record is a dictionary representing a row in the CSV file.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or empty.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>> import csv
    >>> def parse_csv_to_records(csv_string):
    ...     reader = csv.DictReader(csv_string.splitlines())
    ...     return list(reader)
    >>> csv_string = "Name,Age,Country\nJohn,25,USA\nJane,30,UK"
    >>> parse_csv_to_records(csv_string)
    [{'Name': 'John', 'Age': '25', 'Country': 'USA'}, {'Name': 'Jane', 'Age':
    '30', 'Country': 'UK'}]

    """
    
    if not isinstance(csv_string, str):
        raise TypeError("Input must be a string")
    
    if not csv_string.strip():
        raise ValueError("CSV string cannot be empty")
    
    try:
        lines = csv_string.splitlines()
        if not lines:
            raise ValueError("CSV string is malformed or empty")
        
        reader = csv.DictReader(lines)
        records = list(reader)
        
        if not records:
            raise ValueError("CSV string is malformed or empty")
            
        return records
    except csv.Error as e:
        raise ValueError("CSV string is malformed or empty") from e