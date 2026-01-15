from ._define_alternative_inflation_index.validate_expenditure_csv_format import validate_expenditure_csv_format
from ._define_alternative_inflation_index.parse_expenditure_csv import parse_expenditure_csv
from ._define_alternative_inflation_index.calculate_category_expenditure_totals import calculate_category_expenditure_totals
from ._define_alternative_inflation_index.calculate_total_expenditure import calculate_total_expenditure
from ._define_alternative_inflation_index.calculate_category_weights import calculate_category_weights
from ._define_alternative_inflation_index.generate_index_name import generate_index_name
from ._define_alternative_inflation_index.convert_weights_to_csv import convert_weights_to_csv
from ._define_alternative_inflation_index.validate_methodology_completion import validate_methodology_completion

from pydantic import BaseModel, Field


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


def define_alternative_inflation_index(fetch_household_expenditure_data_input: FetchHouseholdExpenditureDataOutput, **kwargs) -> DefineAlternativeInflationIndexOutput:
    """
    Derives an alternative inflation index by defining its methodology and
    category weights from consolidated household expenditure data.

    Parameters
    ----------
    expenditure_csv : str
        CSV string of consolidated household expenditure data with columns:
        Year, Category, Location, Expenditure_Amount.

    Returns
    -------
    dict
        Dictionary containing the index name, category weights as a CSV
        string, and a success flag for the methodology definition.

    Raises
    ------
    ValueError
        If the input expenditure CSV is malformed or empty.

    Examples
    --------
    >>> expenditure_data = 'Year,Category,Location,Expenditure_Amount'
    >>> expenditure_data += '\n2022,Food,New York,1000'
    >>> define_alternative_inflation_index(expenditure_data)
    {'index_name': 'AlternativeInflationIndex', 'index_weights_csv':
    'Category,Weight\nFood,0.3', 'is_methodology_successful': True}

    """
    expenditure_data: str = fetch_household_expenditure_data_input.expenditure_csv
    
    validated_data: bool = validate_expenditure_csv_format(csv_data=expenditure_data)
    if not validated_data:
        raise ValueError("Input expenditure CSV is malformed or empty")
    
    parsed_expenditure_data: list = parse_expenditure_csv(csv_data=expenditure_data)
    
    category_totals: dict = calculate_category_expenditure_totals(expenditure_data=parsed_expenditure_data)
    
    total_expenditure: float = calculate_total_expenditure(category_totals=category_totals)
    
    category_weights: dict = calculate_category_weights(category_totals=category_totals, total_expenditure=total_expenditure)
    
    index_name: str = generate_index_name()
    
    weights_csv: str = convert_weights_to_csv(weights_dict=category_weights)
    
    methodology_success: bool = validate_methodology_completion(weights=category_weights, index_name=index_name)
    
    return DefineAlternativeInflationIndexOutput(
        index_name=index_name,
        index_weights_csv=weights_csv,
        is_methodology_successful=methodology_success
    )