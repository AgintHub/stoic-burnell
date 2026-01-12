from pydantic import BaseModel, Field
from typing import List


class AcquireMarketDataOutput(BaseModel):
    """Pydantic model for acquire_market_data node outputs."""
    acquisition_successful: bool = (
        Field(..., description="Whether data acquisition was successful")
    )
    data_sources: str = (
        Field(..., description="List of data sources from which data was acquired")
    )
    start_timestamp: str = (
        Field(..., description="Start timestamp of the acquired data")
    )
    end_timestamp: str = (
        Field(..., description="End timestamp of the acquired data")
    )
    error_messages: str = (
        Field(..., description="List of error messages encountered during data acquisition")
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
    return ValidateAcquiredDataOutput(
        validation_status=False,
        checks_performed=[],
        check_results=[],
        missing_timestamps=[],
        price_consistency_issues=[],
    )