import csv
import io


def verify_timeline_integrity(csv_output: str, expected_years: str) -> bool:
    """
    Verifies the integrity of a timeline based on the provided CSV output and
    expected years.

    Parameters
    ----------
    csv_output : str
        The CSV output of the timeline.
    expected_years : str
        The expected years in the timeline.

    Returns
    -------
    bool
        Boolean indicating whether the timeline integrity verification was
        successful.

    Raises
    ------
    ValueError
        When the CSV output is empty or does not contain the expected years.
    TypeError
        When the input types are incorrect.

    Examples
    --------
    >>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,Location
    Totals\n2020,1.0,100,200\n2021,1.1,120,250', expected_years='2020,2021')
    True

    >>> verify_timeline_integrity(csv_output='Year,Index,CategoryTotals,Location
    Totals\n2020,1.0,100,200\n2022,1.1,120,250', expected_years='2020,2021')
    False

    """
    
    if not isinstance(csv_output, str):
        raise TypeError("csv_output must be a string")
    if not isinstance(expected_years, str):
        raise TypeError("expected_years must be a string")
    
    if not csv_output.strip():
        raise ValueError("CSV output is empty")
    
    expected_years_list = [year.strip() for year in expected_years.split(',')]
    
    try:
        csv_reader = csv.DictReader(io.StringIO(csv_output))
        csv_years = set()
        
        for row in csv_reader:
            if 'Year' in row:
                csv_years.add(row['Year'].strip())
        
        expected_years_set = set(expected_years_list)
        
        if not expected_years_set.issubset(csv_years):
            return False
            
        return True
        
    except Exception as e:
        raise ValueError(f"Failed to parse CSV output: {str(e)}")