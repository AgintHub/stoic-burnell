from ._compute_category_location_breakdowns.validate_csv_format import validate_csv_format
from ._compute_category_location_breakdowns.parse_csv_to_records import parse_csv_to_records
from ._compute_category_location_breakdowns.aggregate_by_category import aggregate_by_category
from ._compute_category_location_breakdowns.aggregate_by_location import aggregate_by_location
from ._compute_category_location_breakdowns.convert_category_aggregation_to_csv import convert_category_aggregation_to_csv
from ._compute_category_location_breakdowns.convert_location_aggregation_to_csv import convert_location_aggregation_to_csv

from pydantic import BaseModel, Field


class FetchHouseholdExpenditureDataOutput(BaseModel):
    """Pydantic model for fetch_household_expenditure_data node outputs."""
    expenditure_csv: str = (
        Field(..., description="CSV string of consolidated household expenditure data with columns: Year, Category, Location, Expenditure_Amount.")
    )
    is_data_successful: bool = (
        Field(..., description="Flag indicating whether data discovery, download, normalization, and CSV consolidation completed successfully.")
    )


class ComputeCategoryLocationBreakdownsOutput(BaseModel):
    """Pydantic model for compute_category_location_breakdowns node outputs."""
    category_spending_csv: str = (
        Field(..., description="CSV string containing Year, Category, and the total expenditure for that category in that year.")
    )
    location_spending_csv: str = (
        Field(..., description="CSV string containing Year, HouseholdLocation, and the total expenditure for that household location in that year.")
    )
    is_breakdown_successful: bool = (
        Field(..., description="Flag indicating whether the aggregation succeeded.")
    )


def compute_category_location_breakdowns(fetch_household_expenditure_data_input: FetchHouseholdExpenditureDataOutput, **kwargs) -> ComputeCategoryLocationBreakdownsOutput:
    """
    Compute category-wise and household-location-wise expenditure breakdowns
    from consolidated household expenditure data.

    Parameters
    ----------
    expenditure_csv : str
        CSV string of consolidated household expenditure data with columns:
        Year, Category, Location, Expenditure_Amount.

    Returns
    -------
    dict
        A dictionary containing 'category_spending_csv',
        'location_spending_csv', and 'is_breakdown_successful' as keys.

    Raises
    ------
    ValueError
        If the input CSV string is empty or malformed.

    Examples
    --------
    >>> expenditure_data = 'Year,Category,Location,Expenditure_Amount'
    >>> expenditure_data += '\n2020,Food,Urban,1000'
    >>> expenditure_data += '\n2020,Food,Rural,500'
    >>> breakdowns = compute_category_location_breakdowns(expenditure_data)
    {'category_spending_csv': 'Year,Category,Total_Expenditure\n2020,Food,1500',
    'location_spending_csv':
    'Year,HouseholdLocation,Total_Expenditure\n2020,Urban,1000\n2020,Rural,500',
    'is_breakdown_successful': True}

    """
    expenditure_csv: str = fetch_household_expenditure_data_input.expenditure_csv
    
    is_valid_csv: bool = validate_csv_format(csv_data=expenditure_csv, required_columns=["Year", "Category", "Location", "Expenditure_Amount"])
    
    if not is_valid_csv:
        return ComputeCategoryLocationBreakdownsOutput(
            category_spending_csv="",
            location_spending_csv="",
            is_breakdown_successful=False,
        )
    
    parsed_data: list = parse_csv_to_records(csv_string=expenditure_csv)
    
    category_aggregated_data: dict = aggregate_by_category(data=parsed_data, year_col="Year", category_col="Category", amount_col="Expenditure_Amount")
    
    location_aggregated_data: dict = aggregate_by_location(data=parsed_data, year_col="Year", location_col="Location", amount_col="Expenditure_Amount")
    
    category_csv: str = convert_category_aggregation_to_csv(aggregated_data=category_aggregated_data)
    
    location_csv: str = convert_location_aggregation_to_csv(aggregated_data=location_aggregated_data)
    
    return ComputeCategoryLocationBreakdownsOutput(
        category_spending_csv=category_csv,
        location_spending_csv=location_csv,
        is_breakdown_successful=True,
    )