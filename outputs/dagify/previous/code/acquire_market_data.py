from ._acquire_market_data.validate_data_sources import validate_data_sources
from ._acquire_market_data.establish_database_connection import establish_database_connection
from ._acquire_market_data.get_current_timestamp import get_current_timestamp
from ._acquire_market_data.get_source_credentials import get_source_credentials
from ._acquire_market_data.authenticate_data_source import authenticate_data_source
from ._acquire_market_data.fetch_market_data import fetch_market_data
from ._acquire_market_data.store_data_in_database import store_data_in_database
from ._acquire_market_data.format_error_message import format_error_message
from ._acquire_market_data.close_database_connection import close_database_connection
from ._acquire_market_data.format_source_list import format_source_list
from ._acquire_market_data.format_error_list import format_error_list

from pydantic import BaseModel, Field
from typing import List


class IdentifyDataSourcesOutput(BaseModel):
    """Pydantic model for identify_data_sources node outputs."""
    data_source_names: List[str] = (
        Field(..., description="List of data source names")
    )
    vendor_names: List[str] = (
        Field(..., description="List of vendor names for each data source")
    )
    data_frequencies: List[str] = (
        Field(..., description = (
            "List of data frequencies for each data source (e.g., real-time, 1min, 1day)")
        )
    )
    licensing_constraints: List[str] = (
        Field(..., description = (
            "List of licensing constraints for each data source")
        )
    )


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


def acquire_market_data(identify_data_sources_input: IdentifyDataSourcesOutput, **kwargs) -> AcquireMarketDataOutput:
    """
    Acquire market data from identified sources and store it in a database.

    Parameters
    ----------
    data_sources : List[str]
        List of data sources to acquire data from
    database_config : dict
        Dictionary containing database connection configuration
    authentication_credentials : dict
        Dictionary containing authentication credentials for data sources

    Returns
    -------
    dict
        Dictionary containing acquisition status, list of data sources,
        start and end timestamps, and error messages

    Raises
    ------
    Exception
        If an error occurs during data acquisition or storage

    Examples
    --------
    >>> data_sources = ['source1', 'source2']
    >>> database_config = {'host': 'localhost', 'port': 5432, 'database':
    'market_data'}
    >>> authentication_credentials = {'source1': 'username1:password1',
    'source2': 'username2:password2'}
    >>> result = acquire_market_data(data_sources, database_config,
    authentication_credentials)
    {'acquisition_successful': True, 'data_sources': ['source1', 'source2'],
    'start_timestamp': '2022-01-01 00:00:00', 'end_timestamp': '2022-01-01
    23:59:59', 'error_messages': []}

    """
    database_config: dict = kwargs.get('database_config', {})
    authentication_credentials: dict = kwargs.get('authentication_credentials', {})
    
    validated_sources: List[str] = validate_data_sources(data_sources=identify_data_sources_input.data_source_names)
    
    db_connection = establish_database_connection(config=database_config)
    
    error_messages: List[str] = []
    acquired_data_sources: List[str] = []
    start_time: str = get_current_timestamp()
    
    for source in validated_sources:
        try:
            credentials = get_source_credentials(source=source, auth_config=authentication_credentials)
            source_connection = authenticate_data_source(source=source, credentials=credentials)
            market_data: dict = fetch_market_data(source_connection=source_connection, source=source)
            store_data_in_database(db_connection=db_connection, data=market_data, source=source)
            acquired_data_sources.append(source)
        except Exception as e:
            error_msg: str = format_error_message(source=source, error=e)
            error_messages.append(error_msg)
    
    end_time: str = get_current_timestamp()
    close_database_connection(connection=db_connection)
    
    acquisition_success: bool = len(acquired_data_sources) > 0
    formatted_sources: str = format_source_list(sources=acquired_data_sources)
    formatted_errors: str = format_error_list(errors=error_messages)
    
    return AcquireMarketDataOutput(
        acquisition_successful=acquisition_success,
        data_sources=formatted_sources,
        start_timestamp=start_time,
        end_timestamp=end_time,
        error_messages=formatted_errors
    )