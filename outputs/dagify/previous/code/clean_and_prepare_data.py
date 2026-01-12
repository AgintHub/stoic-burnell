from ._clean_and_prepare_data.load_raw_dataset import load_raw_dataset
from ._clean_and_prepare_data.handle_missing_values import handle_missing_values
from ._clean_and_prepare_data.remove_outliers import remove_outliers
from ._clean_and_prepare_data.standardize_data import standardize_data
from ._clean_and_prepare_data.calculate_derived_features import calculate_derived_features
from ._clean_and_prepare_data.validate_cleaned_data import validate_cleaned_data
from ._clean_and_prepare_data.assess_dataset_readiness import assess_dataset_readiness

from pydantic import BaseModel, Field
from typing import List


class ValidateAcquiredDataOutput(BaseModel):
    """Pydantic model for validate_acquired_data node outputs."""
    validation_status: bool = (
        Field(..., description="Whether the data is valid")
    )
    checks_performed: List[str] = (
        Field(..., description="List of checks performed during validation")
    )
    check_results: List[bool] = (
        Field(..., description="List of results for each check performed")
    )
    missing_timestamps: List[int] = (
        Field(..., description="List of timestamps with missing data")
    )
    price_consistency_issues: List[str] = (
        Field(..., description="List of price consistency issues found")
    )


class CleanAndPrepareDataOutput(BaseModel):
    """Pydantic model for clean_and_prepare_data node outputs."""
    cleaning_successful: bool = (
        Field(..., description = (
            "Whether the data cleaning and preparation were successful")
        )
    )
    number_of_missing_values_handled: int = (
        Field(..., description = (
            "Number of missing values handled during the cleaning process")
        )
    )
    derived_fields_calculated: str = (
        Field(..., description = (
            "List of derived fields calculated during the preparation process")
        )
    )
    dataset_ready: bool = (
        Field(..., description = (
            "Whether the dataset is ready for feature engineering")
        )
    )


def clean_and_prepare_data(validate_acquired_data_input: ValidateAcquiredDataOutput, **kwargs) -> CleanAndPrepareDataOutput:
    """
    Performs a series of data cleaning and transformation operations.

    Returns
    -------
    Pandas DataFrame
        The transformed dataset in a suitable format for modeling.

    Examples
    --------
    >>> import pandas as pd
    >>> from sklearn.impute import SimpleImputer
    >>> from sklearn.preprocessing import StandardScaler
    Cleaned DataFrame

    """
    raw_dataset = load_raw_dataset(validation_input=validate_acquired_data_input)
    
    missing_value_count: int = handle_missing_values(dataset=raw_dataset, strategy="imputation")
    
    cleaned_dataset = remove_outliers(dataset=raw_dataset, method="zscore")
    
    standardized_dataset = standardize_data(dataset=cleaned_dataset, scaler_type="standard")
    
    derived_fields: str = calculate_derived_features(dataset=standardized_dataset)
    
    data_quality_check: bool = validate_cleaned_data(dataset=standardized_dataset)
    
    dataset_readiness: bool = assess_dataset_readiness(dataset=standardized_dataset, quality_passed=data_quality_check)
    
    return CleanAndPrepareDataOutput(
        cleaning_successful=data_quality_check,
        number_of_missing_values_handled=missing_value_count,
        derived_fields_calculated=derived_fields,
        dataset_ready=dataset_readiness
    )