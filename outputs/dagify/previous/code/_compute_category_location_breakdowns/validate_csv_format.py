import csv
from io import StringIO


def validate_csv_format(csv_data: str, required_columns: str) -> bool:
    """
    Validates a CSV string against a set of required columns.

    Parameters
    ----------
    csv_data : str
        The input CSV string to be validated.
    required_columns : str
        A comma-separated string of required column names.

    Returns
    -------
    bool
        True if the CSV string is valid, False otherwise.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or empty.
    TypeError
        When the input types are incorrect.

    Examples
    --------
    >>> import pandas as pd
    >>> csv_data = 'Year,Category,Location,Expenditure_Amount\n2020,Food,New
    York,100'
    >>> required_columns = 'Year,Category,Location,Expenditure_Amount'
    >>> validate_csv_format(csv_data=csv_data,
    required_columns=required_columns)
    True

    >>> import pandas as pd
    >>> csv_data = 'Year,Category,Location'
    >>> required_columns = 'Year,Category,Location,Expenditure_Amount'
    >>> validate_csv_format(csv_data=csv_data,
    required_columns=required_columns)
    False

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("csv_data must be a string")
    if not isinstance(required_columns, str):
        raise TypeError("required_columns must be a string")
    
    if not csv_data.strip():
        raise ValueError("CSV data cannot be empty")
    
    try:
        csv_reader = csv.reader(StringIO(csv_data))
        header = next(csv_reader)
    except (csv.Error, StopIteration):
        raise ValueError("Malformed CSV string")
    
    required_cols = [col.strip() for col in required_columns.split(',')]
    
    return set(required_cols).issubset(set(header))