import csv
import io


def parse_category_csv_to_year_totals(csv_data: str) -> str:
    """
    Parses a CSV string of category spending data into a dictionary where keys
    are years and values are total expenditures for each category in that year.

    Parameters
    ----------
    csv_data : str
        A string containing CSV data with columns for year and category
        expenditures.

    Returns
    -------
    dict
        A dictionary where each key is a year and each value is the total
        expenditure for all categories in that year.

    Raises
    ------
    ValueError
        If the input CSV string is malformed or cannot be parsed.
    TypeError
        If the input is not a string or if the CSV data cannot be converted
        into the required dictionary format.

    Examples
    --------
    >>> csv_string = 'Year,Category,Expenditure'
    >>> csv_string += '\n2020,CategoryA,100'
    >>> csv_string += '\n2020,CategoryB,200'
    >>> csv_string += '\n2021,CategoryA,150'
    >>> result = parse_category_csv_to_year_totals(csv_string)
    {'2020': 300, '2021': 150}

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("Input must be a string")
    
    try:
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        year_totals = {}
        
        for row in csv_reader:
            if 'Year' not in row or 'Expenditure' not in row:
                raise ValueError("CSV must contain 'Year' and 'Expenditure' columns")
            
            year = str(row['Year']).strip()
            try:
                expenditure = float(row['Expenditure'])
            except ValueError:
                raise ValueError("Expenditure values must be numeric")
            
            if year in year_totals:
                year_totals[year] += expenditure
            else:
                year_totals[year] = expenditure
        
        return str(year_totals)
    
    except Exception as e:
        if isinstance(e, (ValueError, TypeError)):
            raise
        raise ValueError("Malformed CSV data") from e