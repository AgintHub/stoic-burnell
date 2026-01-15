import csv
import io


def validate_expenditure_csv_format(csv_data: str) -> bool:
    """
    Validates the format of a given expenditure CSV string.

    Parameters
    ----------
    csv_data : str
        The input CSV string to be validated, containing columns for Year,
        Category, Location, and Expenditure_Amount.

    Returns
    -------
    bool
        True if the CSV string is well-formatted, False otherwise.

    Raises
    ------
    ValueError
        When the input CSV string is empty or malformed.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>> import pandas as pd
    >>> csv_data = 'Year,Category,Location,Expenditure_Amount\n2020,Food,New
    York,100.0\n2021,Housing,Los Angeles,200.0'
    >>> validate_expenditure_csv_format(csv_data=csv_data)
    True

    >>> csv_data = 'Invalid,Format'
    >>> validate_expenditure_csv_format(csv_data=csv_data)
    False

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("When the input is not a string.")
    
    if not csv_data.strip():
        raise ValueError("When the input CSV string is empty or malformed.")
    
    try:
        csv_file = io.StringIO(csv_data)
        reader = csv.DictReader(csv_file)
        
        expected_columns = {'Year', 'Category', 'Location', 'Expenditure_Amount'}
        
        if not reader.fieldnames:
            return False
            
        actual_columns = set(reader.fieldnames)
        
        if actual_columns != expected_columns:
            return False
        
        for row in reader:
            if len(row) != 4:
                return False
            
            if not all(key in row for key in expected_columns):
                return False
        
        return True
        
    except Exception:
        raise ValueError("When the input CSV string is empty or malformed.")