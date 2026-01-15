import csv
import io


def validate_expenditure_data_format(csv_data: str) -> bool:
    """
    Validates the format of expenditure data in a given CSV string.

    Parameters
    ----------
    csv_data : str
        The input CSV string containing expenditure data with columns: Year,
        Category, Location, Expenditure_Amount.

    Returns
    -------
    bool
        True if the expenditure data format is valid, False otherwise.

    Raises
    ------
    ValueError
        When the input CSV string is empty or does not contain the required
        columns.
    TypeError
        When the input csv_data is not a string.

    Examples
    --------
    >>> validate_expenditure_data_format('Year,Category,Location,Expenditure_Amo
    unt\n2020,Food,New York,100.0')
    True

    >>> validate_expenditure_data_format('Invalid,Data,Format')
    False

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("When the input csv_data is not a string.")
    
    if not csv_data.strip():
        raise ValueError("When the input CSV string is empty or does not contain the required columns.")
    
    try:
        csv_reader = csv.reader(io.StringIO(csv_data))
        headers = next(csv_reader)
        
        required_columns = ['Year', 'Category', 'Location', 'Expenditure_Amount']
        
        if len(headers) != len(required_columns):
            return False
        
        for required_col in required_columns:
            if required_col not in headers:
                return False
        
        return True
        
    except (csv.Error, StopIteration):
        raise ValueError("When the input CSV string is empty or does not contain the required columns.")