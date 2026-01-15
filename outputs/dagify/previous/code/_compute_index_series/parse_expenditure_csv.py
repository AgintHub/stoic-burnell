import csv
import json
import io


def parse_expenditure_csv(csv_data: str) -> str:
    """
    Parses a CSV string of expenditure data into a structured format.

    Parameters
    ----------
    csv_data : str
        The input CSV string of expenditure data with columns: Year,
        Category, Location, Expenditure_Amount.

    Returns
    -------
    str
        The parsed expenditure data in a structured format.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or missing required columns.
    TypeError
        When the input is not a string.

    Examples
    --------
    >>> parse_expenditure_csv('Year,Category,Location,Expenditure_Amount\n2020,F
    ood,New York,100.0\n2021,Housing,Los Angeles,200.0')
    {"output": "The parsed expenditure data in a structured format."}

    >>> parse_expenditure_csv('Invalid CSV string')
    {"error": "ValueError: Malformed CSV string"}

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("Input must be a string")
    
    try:
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        required_columns = {'Year', 'Category', 'Location', 'Expenditure_Amount'}
        
        if not required_columns.issubset(set(csv_reader.fieldnames or [])):
            raise ValueError("Malformed CSV string")
        
        parsed_data = []
        for row in csv_reader:
            try:
                parsed_row = {
                    'Year': int(row['Year']),
                    'Category': row['Category'],
                    'Location': row['Location'],
                    'Expenditure_Amount': float(row['Expenditure_Amount'])
                }
                parsed_data.append(parsed_row)
            except (ValueError, KeyError):
                raise ValueError("Malformed CSV string")
        
        return json.dumps({"data": parsed_data, "count": len(parsed_data)})
    
    except csv.Error:
        raise ValueError("Malformed CSV string")