from pydantic import BaseModel, Field
from typing import List


class CleanAndPrepareDataOutput(BaseModel):
    """Pydantic model for clean_and_prepare_data node outputs."""
    cleaning_successful: bool = (
        Field(..., description="Whether the data cleaning and preparation were successful")
    )
    number_of_missing_values_handled: int = (
        Field(..., description="Number of missing values handled during the cleaning process")
    )
    derived_fields_calculated: str = (
        Field(..., description="List of derived fields calculated during the preparation process")
    )
    dataset_ready: bool = (
        Field(..., description="Whether the dataset is ready for feature engineering")
    )


class EngineerFeaturesOutput(BaseModel):
    """Pydantic model for engineer_features node outputs."""
    feature_list: List[str] = (
        Field(..., description="List of feature names engineered for the strategy")
    )
    feature_formulas: List[str] = (
        Field(..., description="Formulas or descriptions for each feature in the feature list")
    )
    feature_descriptions: List[str] = (
        Field(..., description="Descriptions of each feature in the feature list")
    )


def engineer_features(clean_and_prepare_data_input: CleanAndPrepareDataOutput, **kwargs) -> EngineerFeaturesOutput:
    """
    Engineer features for options trading strategy signals.

    Returns
    -------
    object
        Object containing feature_list, feature_formulas, and
        feature_descriptions
    """
    return EngineerFeaturesOutput(
        feature_list=[],
        feature_formulas=[],
        feature_descriptions=[],
    )