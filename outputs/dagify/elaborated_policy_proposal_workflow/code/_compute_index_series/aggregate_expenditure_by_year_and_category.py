import pandas as pd
from io import StringIO


def aggregate_expenditure_by_year_and_category(merged_data: str) -> str:
    """
    Aggregates expenditure data by year and category.

    Parameters
    ----------
    merged_data : str
        Input parameter of type str containing expenditure data

    Returns
    -------
    str
        Aggregated expenditure data

    Raises
    ------
    ValueError
        When input validation fails.
    TypeError
        When input types are incorrect.

    Examples
    --------
    >>> import pandas as pd
    >>> data = {'Year': [2020, 2020, 2021], 'Category': ['A', 'B', 'A'],
    'Expenditure_Amount': [100, 200, 300]}
    >>> df = pd.DataFrame(data)
    >>> aggregate_expenditure_by_year_and_category(merged_data=df.to_csv())
    output

    """
    
    if not isinstance(merged_data, str):
        raise TypeError("Input must be a string")
    
    if not merged_data.strip():
        raise ValueError("Input data cannot be empty")
    
    try:
        df = pd.read_csv(StringIO(merged_data))
    except Exception as e:
        raise ValueError("Failed to parse CSV data") from e
    
    required_columns = ['Year', 'Category', 'Expenditure_Amount']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    try:
        aggregated_df = df.groupby(['Year', 'Category'])['Expenditure_Amount'].sum().reset_index()
    except Exception as e:
        raise ValueError("Failed to aggregate data") from e
    
    return aggregated_df.to_csv(index=False)