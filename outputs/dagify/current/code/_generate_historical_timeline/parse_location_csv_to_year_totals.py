import csv
import io
import json


def parse_location_csv_to_year_totals(csv_data: str) -> str:
    """
    Parses a CSV string containing location spending data and returns a
    dictionary with year-wise totals.

    Parameters
    ----------
    csv_data : str
        A CSV string containing location spending data with columns: Year,
        HouseholdLocation, and total expenditure.

    Returns
    -------
    str
        A dictionary with year-wise totals for location spending, where each
        key is a year and each value is the total expenditure for that year.

    Raises
    ------
    ValueError
        When the input CSV string is invalid or empty.
    TypeError
        When the input csv_data is not a string.

    Examples
    --------
    >>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2
    020,Location A,100\n2020,Location B,200\n2021,Location A,150')
    {'2020': 300, '2021': 150}

    >>> parse_location_csv_to_year_totals('Year,HouseholdLocation,Expenditure\n2
    019,Location C,50\n2020,Location C,75')
    {'2019': 50, '2020': 75}

    """
    
    if not isinstance(csv_data, str):
        raise TypeError("When the input csv_data is not a string.")
    
    if not csv_data.strip():
        raise ValueError("When the input CSV string is invalid or empty.")
    
    try:
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        year_totals = {}
        
        for row in csv_reader:
            if 'Year' not in row or 'Expenditure' not in row:
                raise ValueError("When the input CSV string is invalid or empty.")
            
            year = str(row['Year']).strip()
            expenditure = float(row['Expenditure'])
            
            if year in year_totals:
                year_totals[year] += expenditure
            else:
                year_totals[year] = expenditure
        
        for year in year_totals:
            if year_totals[year] == int(year_totals[year]):
                year_totals[year] = int(year_totals[year])
        
        return json.dumps(year_totals)
        
    except (csv.Error, ValueError, KeyError) as e:
        raise ValueError("When the input CSV string is invalid or empty.") from e