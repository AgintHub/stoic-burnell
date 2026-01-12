from ._engineer_features.calculate_implied_volatility_features import calculate_implied_volatility_features
from ._engineer_features.calculate_options_greeks_features import calculate_options_greeks_features
from ._engineer_features.calculate_moneyness_features import calculate_moneyness_features
from ._engineer_features.calculate_time_to_expiration_features import calculate_time_to_expiration_features
from ._engineer_features.calculate_market_sentiment_features import calculate_market_sentiment_features
from ._engineer_features.combine_feature_lists import combine_feature_lists
from ._engineer_features.generate_feature_formulas import generate_feature_formulas
from ._engineer_features.generate_feature_descriptions import generate_feature_descriptions

from pydantic import BaseModel, Field
from typing import List


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


class EngineerFeaturesOutput(BaseModel):
    """Pydantic model for engineer_features node outputs."""
    feature_list: List[str] = (
        Field(..., description = (
            "List of feature names engineered for the strategy")
        )
    )
    feature_formulas: List[str] = (
        Field(..., description = (
            "Formulas or descriptions for each feature in the feature list")
        )
    )
    feature_descriptions: List[str] = (
        Field(..., description = (
            "Descriptions of each feature in the feature list")
        )
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
    iv_features: List[str] = calculate_implied_volatility_features(data=clean_and_prepare_data_input)
    greeks_features: List[str] = calculate_options_greeks_features(data=clean_and_prepare_data_input)
    moneyness_features: List[str] = calculate_moneyness_features(data=clean_and_prepare_data_input)
    time_features: List[str] = calculate_time_to_expiration_features(data=clean_and_prepare_data_input)
    sentiment_features: List[str] = calculate_market_sentiment_features(data=clean_and_prepare_data_input)
    
    feature_names: List[str] = combine_feature_lists(iv_features, greeks_features, moneyness_features, time_features, sentiment_features)
    feature_formulas: List[str] = generate_feature_formulas(feature_names=feature_names)
    feature_descriptions: List[str] = generate_feature_descriptions(feature_names=feature_names)
    
    return EngineerFeaturesOutput(
        feature_list=feature_names,
        feature_formulas=feature_formulas,
        feature_descriptions=feature_descriptions
    )