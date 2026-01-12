import csv
import io


def validate_weights_data_format(csv_data: str) -> bool:
    """
    Validates the format of the weights data in a CSV string.

    Parameters
    ----------
    csv_data : str
        The input CSV string containing the weights data.

    Returns
    -------
    bool
        True if the weights data format is valid, False otherwise.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or empty.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>> validate_weights_data_format('Category,Weight\nFood,0.5\nHousing,0.3')
    >>> # Returns: True
    True

    >>> validate_weights_data_format('Invalid,Format')
    >>> # Returns: False
    False

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("Input must be a string")
    
    if not csv_data or csv_data.strip() == "":
        raise ValueError("Input CSV string is empty")
    
    try:
        csv_reader = csv.reader(io.StringIO(csv_data))
        rows = list(csv_reader)
        
        if len(rows) < 2:
            return False
        
        header = rows[0]
        if len(header) != 2:
            return False
        
        for row in rows[1:]:
            if len(row) != 2:
                return False
            try:
                float(row[1])
            except (ValueError, IndexError):
                return False
        
        return True
    except Exception:
        raise ValueError("Input CSV string is malformed")