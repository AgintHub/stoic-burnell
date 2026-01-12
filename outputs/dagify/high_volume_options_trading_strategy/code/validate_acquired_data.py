from ._validate_acquired_data.determine_validation_checks import determine_validation_checks
from ._validate_acquired_data.validate_timestamp_consistency import validate_timestamp_consistency
from ._validate_acquired_data.validate_price_consistency import validate_price_consistency
from ._validate_acquired_data.identify_missing_timestamps import identify_missing_timestamps
from ._validate_acquired_data.identify_price_consistency_issues import identify_price_consistency_issues
from ._validate_acquired_data.determine_overall_validation_status import determine_overall_validation_status
from ._validate_acquired_data.raise_invalid_data_error import raise_invalid_data_error

from pydantic import BaseModel, Field
from typing import List


class AcquireMarketDataOutput(BaseModel):
    """Pydantic model for acquire_market_data node outputs."""
    acquisition_successful: bool = (
        Field(..., description="Whether data acquisition was successful")
    )
    data_sources: str = (
        Field(..., description = (
            "List of data sources from which data was acquired")
        )
    )
    start_timestamp: str = (
        Field(..., description="Start timestamp of the acquired data")
    )
    end_timestamp: str = (
        Field(..., description="End timestamp of the acquired data")
    )
    error_messages: str = (
        Field(..., description = (
            "List of error messages encountered during data acquisition")
        )
    )


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


def validate_acquired_data(acquire_market_data_input: AcquireMarketDataOutput, **kwargs) -> ValidateAcquiredDataOutput:
    """
    Ensures the accuracy and consistency of the ingested market data.

    Returns
    -------
    dict
        Validation results with pass/fail indicators and explanations

    Raises
    ------
    InvalidDataError
        Invalid market data detected.

    Examples
    --------
    >>> acquired_data = acquire_market_data()
    >>> validation_results = validate_acquired_data(acquired_data)
    validation_results = {'valid': True, 'checks_performed': ['timestamp
    consistency', 'price consistency'], 'check_results': [True, True],
    'missing_timestamps': [123456, 654321], 'price_consistency_issues': ['Issue
    1', 'Issue 2']}

    """
    checks_to_perform: List[str] = determine_validation_checks(data_input=acquire_market_data_input)
    
    timestamp_check_result: bool = validate_timestamp_consistency(
        start_timestamp=acquire_market_data_input.start_timestamp,
        end_timestamp=acquire_market_data_input.end_timestamp
    )
    
    price_check_result: bool = validate_price_consistency(
        data_sources=acquire_market_data_input.data_sources
    )
    
    missing_timestamps: List[int] = identify_missing_timestamps(
        start_timestamp=acquire_market_data_input.start_timestamp,
        end_timestamp=acquire_market_data_input.end_timestamp
    )
    
    price_issues: List[str] = identify_price_consistency_issues(
        data_sources=acquire_market_data_input.data_sources
    )
    
    check_results: List[bool] = [timestamp_check_result, price_check_result]
    overall_validation_status: bool = determine_overall_validation_status(
        check_results=check_results,
        acquisition_successful=acquire_market_data_input.acquisition_successful
    )
    
    if not overall_validation_status:
        raise_invalid_data_error(issues=price_issues, missing_data=missing_timestamps)
    
    return ValidateAcquiredDataOutput(
        validation_status=overall_validation_status,
        checks_performed=checks_to_perform,
        check_results=check_results,
        missing_timestamps=missing_timestamps,
        price_consistency_issues=price_issues
    )