from ._compute_index_series.validate_expenditure_data_format import validate_expenditure_data_format
from ._compute_index_series.validate_weights_data_format import validate_weights_data_format
from ._compute_index_series.parse_expenditure_csv import parse_expenditure_csv
from ._compute_index_series.parse_weights_csv import parse_weights_csv
from ._compute_index_series.merge_expenditure_with_weights import merge_expenditure_with_weights
from ._compute_index_series.aggregate_expenditure_by_year_and_category import aggregate_expenditure_by_year_and_category
from ._compute_index_series.determine_base_year import determine_base_year
from ._compute_index_series.extract_available_years import extract_available_years
from ._compute_index_series.calculate_annual_index_values import calculate_annual_index_values
from ._compute_index_series.verify_index_computation_success import verify_index_computation_success

from pydantic import BaseModel, Field
from typing import List


class FetchHouseholdExpenditureDataOutput(BaseModel):
    """Pydantic model for fetch_household_expenditure_data node outputs."""
    expenditure_csv: str = (
        Field(..., description="CSV string of consolidated household expenditure data with columns: Year, Category, Location, Expenditure_Amount.")
    )
    is_data_successful: bool = (
        Field(..., description="Flag indicating whether data discovery, download, normalization, and CSV consolidation completed successfully.")
    )


class DefineAlternativeInflationIndexOutput(BaseModel):
    """Pydantic model for define_alternative_inflation_index node outputs."""
    index_name: str = (
        Field(..., description="Name of the alternative inflation index whose weights are being defined.")
    )
    index_weights_csv: str = (
        Field(..., description="CSV string containing the category weighting scheme used in the alternative inflation index.")
    )
    is_methodology_successful: bool = (
        Field(..., description="Flag indicating whether the index methodology and weights were successfully defined from the input expenditure data.")
    )


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


def compute_index_series(fetch_household_expenditure_data_input: FetchHouseholdExpenditureDataOutput, define_alternative_inflation_index_input: DefineAlternativeInflationIndexOutput, **kwargs) -> ComputeIndexSeriesOutput:
    """
    Compute annual alternative inflation index values.

    Parameters
    ----------
    expenditure_data : str
        Consolidated household expenditure data in CSV format.
    weighting_scheme : str
        Prescribed weighting scheme in CSV format.

    Returns
    -------
    dict
        A dictionary containing the list of years, corresponding index
        values, and a flag indicating whether index computation succeeded.

    Raises
    ------
    ValueError
        If the input expenditure data or weighting scheme is invalid.

    Examples
    --------
    >>> expenditure_data = 'Year,Category,Location,Expenditure_Amount'
    >>> weighting_scheme = 'Category,Weight'
    >>> result = compute_index_series(expenditure_data, weighting_scheme)
    {'years': [2020, 2021, 2022], 'index_values': [100.0, 102.0, 104.0],
    'is_index_successful': True}

    """
    if not fetch_household_expenditure_data_input.is_data_successful or not define_alternative_inflation_index_input.is_methodology_successful:
        return ComputeIndexSeriesOutput(
            years=[],
            index_values=[],
            is_index_successful=False
        )
    
    validated_expenditure_data: bool = validate_expenditure_data_format(csv_data=fetch_household_expenditure_data_input.expenditure_csv)
    validated_weights_data: bool = validate_weights_data_format(csv_data=define_alternative_inflation_index_input.index_weights_csv)
    
    if not validated_expenditure_data or not validated_weights_data:
        return ComputeIndexSeriesOutput(
            years=[],
            index_values=[],
            is_index_successful=False
        )
    
    expenditure_df = parse_expenditure_csv(csv_data=fetch_household_expenditure_data_input.expenditure_csv)
    weights_df = parse_weights_csv(csv_data=define_alternative_inflation_index_input.index_weights_csv)
    
    merged_data = merge_expenditure_with_weights(expenditure_data=expenditure_df, weights_data=weights_df)
    
    annual_aggregated_data = aggregate_expenditure_by_year_and_category(merged_data=merged_data)
    
    base_year: int = determine_base_year(aggregated_data=annual_aggregated_data)
    
    calculated_years: List[int] = extract_available_years(aggregated_data=annual_aggregated_data)
    
    index_values: List[float] = calculate_annual_index_values(
        aggregated_data=annual_aggregated_data,
        base_year=base_year,
        target_years=calculated_years
    )
    
    computation_success: bool = verify_index_computation_success(
        years=calculated_years,
        index_values=index_values
    )
    
    return ComputeIndexSeriesOutput(
        years=calculated_years,
        index_values=index_values,
        is_index_successful=computation_success
    )