import csv
import io


def parse_expenditure_csv(csv_data: str) -> str:
    """
    Parses a CSV string of expenditure data into a structured format.

    Parameters
    ----------
    csv_data : str
        CSV string of expenditure data with columns: Year, Category,
        Location, Expenditure_Amount.

    Returns
    -------
    list
        List of dictionaries representing the parsed expenditure data.

    Raises
    ------
    ValueError
        When the input CSV string is malformed or empty.
    TypeError
        When the input type is not a string.

    Examples
    --------
    >>> parse_expenditure_csv('Year,Category,Location,Expenditure_Amount\\n2020,
    Food,New York,1000\\n2021,Housing,Los Angeles,2000')
    [{'Year': '2020', 'Category': 'Food', 'Location': 'New York',
    'Expenditure_Amount': '1000'}, {'Year': '2021', 'Category': 'Housing',
    'Location': 'Los Angeles', 'Expenditure_Amount': '2000'}]

    >>> parse_expenditure_csv('')
     raises ValueError

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("Input must be a string")
    
    if not csv_data or csv_data.strip() == '':
        raise ValueError("Input CSV string is empty")
    
    try:
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        result = []
        for row in csv_reader:
            result.append(dict(row))
        
        if not result:
            raise ValueError("CSV string is malformed or contains no data")
        
        return str(result)
    except csv.Error as e:
        raise ValueError("CSV string is malformed") from e