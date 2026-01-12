from ._generate_historical_timeline.validate_input_data import validate_input_data
from ._generate_historical_timeline.parse_category_csv_to_year_totals import parse_category_csv_to_year_totals
from ._generate_historical_timeline.parse_location_csv_to_year_totals import parse_location_csv_to_year_totals
from ._generate_historical_timeline.create_year_index_mapping import create_year_index_mapping
from ._generate_historical_timeline.merge_timeline_data import merge_timeline_data
from ._generate_historical_timeline.format_timeline_as_csv import format_timeline_as_csv
from ._generate_historical_timeline.verify_timeline_integrity import verify_timeline_integrity

from pydantic import BaseModel, Field
from typing import List


class ComputeIndexSeriesOutput(BaseModel):
    """Pydantic model for compute_index_series node outputs."""
    years: List[int] = (
        Field(..., description="List of years for which the index was calculated.")
    )
    index_values: List[float] = (
        Field(..., description="Corresponding index values for each year.")
    )
    is_index_successful: bool = (
        Field(..., description="Indicates whether index computation succeeded.")
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


class GenerateHistoricalTimelineOutput(BaseModel):
    """Pydantic model for generate_historical_timeline node outputs."""
    timeline_report_csv: str = (
        Field(..., description="CSV string of the historical timeline with columns: Year, Index, CategoryTotals, LocationTotals.")
    )
    is_timeline_successful: bool = (
        Field(..., description="Flag indicating whether the timeline was generated successfully from the index series and breakdown CSVs.")
    )


def generate_historical_timeline(compute_index_series_input: ComputeIndexSeriesOutput, compute_category_location_breakdowns_input: ComputeCategoryLocationBreakdownsOutput, **kwargs) -> GenerateHistoricalTimelineOutput:
    """
    Generate a historical timeline CSV by combining index series data with
    category and location expenditure breakdowns.

    Parameters
    ----------
    index_series : dict
        Dictionary containing index series data with keys 'years' and
        'index_values'.
    category_breakdowns : dict
        Dictionary containing category breakdown data with keys
        'category_spending_csv' and 'is_breakdown_successful'.
    location_breakdowns : dict
        Dictionary containing location breakdown data with keys
        'location_spending_csv' and 'is_breakdown_successful'.

    Returns
    -------
    tuple
        A tuple containing the historical timeline CSV string and a boolean
        flag indicating success.

    Raises
    ------
    ValueError
        If input data is missing or malformed.

    Examples
    --------
    >>> index_series = {'years': [2020, 2021], 'index_values': [100.0, 105.0]}
    >>> category_breakdowns = {'category_spending_csv':
    'Year,Category,Total\n2020,Food,1000\n2021,Food,1100',
    'is_breakdown_successful': True}
    >>> location_breakdowns = {'location_spending_csv':
    'Year,Location,Total\n2020,Urban,500\n2021,Urban,550',
    'is_breakdown_successful': True}
    >>> generate_historical_timeline(index_series, category_breakdowns,
    location_breakdowns)
    'Year,Index,CategoryTotals,LocationTotals\n2020,100.0,1000,500\n2021,105.0,1
    100,550', True

    """
    validated_inputs: bool = validate_input_data(index_input=compute_index_series_input, breakdown_input=compute_category_location_breakdowns_input)
    
    if not validated_inputs:
        return GenerateHistoricalTimelineOutput(timeline_report_csv="", is_timeline_successful=False)
    
    category_totals_by_year: dict = parse_category_csv_to_year_totals(csv_data=compute_category_location_breakdowns_input.category_spending_csv)
    location_totals_by_year: dict = parse_location_csv_to_year_totals(csv_data=compute_category_location_breakdowns_input.location_spending_csv)
    
    index_data_by_year: dict = create_year_index_mapping(years=compute_index_series_input.years, index_values=compute_index_series_input.index_values)
    
    combined_timeline_data: list = merge_timeline_data(index_by_year=index_data_by_year, category_totals=category_totals_by_year, location_totals=location_totals_by_year)
    
    timeline_csv: str = format_timeline_as_csv(timeline_data=combined_timeline_data, headers=["Year", "Index", "CategoryTotals", "LocationTotals"])
    
    is_successful: bool = verify_timeline_integrity(csv_output=timeline_csv, expected_years=compute_index_series_input.years)
    
    return GenerateHistoricalTimelineOutput(timeline_report_csv=timeline_csv, is_timeline_successful=is_successful)