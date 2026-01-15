from pydantic import BaseModel, Field


class FetchHouseholdExpenditureDataOutput(BaseModel):
    """Pydantic model for fetch_household_expenditure_data node outputs."""
    expenditure_csv: str = (
        Field(..., description="CSV string of consolidated household expenditure data with columns: Year, Category, Location, Expenditure_Amount.")
    )
    is_data_successful: bool = (
        Field(..., description="Flag indicating whether data discovery, download, normalization, and CSV consolidation completed successfully.")
    )


def fetch_household_expenditure_data(general_input: str, **kwargs) -> FetchHouseholdExpenditureDataOutput:
    """
    Discover official U.S. household expenditure sources, retrieve and normalize
    the raw tables, validate and reconcile categories and locations, and return
    a consolidated CSV string plus a success flag describing whether the full
    pipeline completed successfully.

    Returns
    -------
    Tuple[str, bool]
        Tuple where the first element is a CSV string with columns (Year,
        Category, Location, Expenditure_Amount) representing consolidated,
        normalized expenditure observations; the second element is a boolean
        flag is_data_successful that is True when discovery, download,
        normalization, validation, and CSV consolidation all succeeded,
        otherwise False.

    Raises
    ------
    ConnectionError
        Raised when network or API errors prevent downloading required
        source files and a retry/backoff strategy fails or is not possible.
    LookupError
        Raised when no usable official data sources or required tables
        (year, category, location, expenditure) can be discovered for the
        requested scope.
    ValueError
        Raised when normalization rules cannot resolve mismatched category
        taxonomies or when mandatory fields are missing after parsing.
    RuntimeError
        Raised for unrecoverable validation failures (e.g., totals
        inconsistent with published aggregates) that prevent safe downstream
        index construction.

    Examples
    --------
    >>> fetch_household_expenditure_data()
    ('Year,Category,Location,Expenditure_Amount\n2020,Food,Urban,1200.00\n2020,H
    ousing,Urban,8000.00', True)

    >>> fetch_household_expenditure_data()
    ('', False)

    """
    return FetchHouseholdExpenditureDataOutput(
        expenditure_csv="",
        is_data_successful=False,
    )