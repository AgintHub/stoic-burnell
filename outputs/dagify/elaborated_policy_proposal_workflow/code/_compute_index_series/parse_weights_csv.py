import csv
import io


def parse_weights_csv(csv_data: str) -> str:
    """
    Parses a CSV string containing category weights into a structured format.

    Parameters
    ----------
    csv_data : str
        The input CSV string containing category weights.

    Returns
    -------
    str
        The parsed weights data in a structured format.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or empty.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>>
    parse_weights_csv('category,weight\nfood,0.5\nclothing,0.3\nhousing,0.2')
    A structured representation of the weights data (e.g., a Pandas DataFrame).

    >>> parse_weights_csv('')
    Raises ValueError: Input CSV string is empty.

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("Input must be a string")
    
    if not csv_data.strip():
        raise ValueError("Input CSV string is empty")
    
    try:
        csv_reader = csv.reader(io.StringIO(csv_data.strip()))
        rows = list(csv_reader)
        
        if len(rows) < 2:
            raise ValueError("CSV must contain header and at least one data row")
        
        header = rows[0]
        if len(header) != 2:
            raise ValueError("CSV must have exactly 2 columns")
        
        result_data = []
        for i, row in enumerate(rows[1:], 1):
            if len(row) != 2:
                raise ValueError(f"Row {i} does not have exactly 2 columns")
            
            category, weight_str = row
            try:
                weight = float(weight_str)
            except ValueError:
                raise ValueError(f"Weight value '{weight_str}' in row {i} is not a valid number")
            
            result_data.append([category, weight])
        
        structured_result = {
            'columns': header,
            'data': result_data
        }
        
        return str(structured_result)
        
    except csv.Error as e:
        raise ValueError(f"Malformed CSV: {e}")