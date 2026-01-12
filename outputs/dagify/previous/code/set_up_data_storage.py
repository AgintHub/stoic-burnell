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
        Field(..., description="List of data frequencies for each data source (e.g., real-time, 1min, 1day)")
    )
    licensing_constraints: List[str] = (
        Field(..., description="List of licensing constraints for each data source")
    )


class SetUpDataStorageOutput(BaseModel):
    """Pydantic model for set_up_data_storage node outputs."""
    database_type: str = (
        Field(..., description="Type of the database (e.g., relational, NoSQL, time-series)")
    )
    schema_outline: str = (
        Field(..., description="Detailed outline of the database schema")
    )
    partition_strategy: str = (
        Field(..., description="Strategy used for partitioning data (e.g., by date, by type)")
    )
    retention_policy: str = (
        Field(..., description="Policy for data retention (e.g., time-based, size-based)")
    )
    data_storage_size: int = (
        Field(..., description="Estimated size of the data storage needed")
    )
    is_cloud_based: bool = (
        Field(..., description="Whether the data storage solution is cloud-based")
    )


def set_up_data_storage(identify_data_sources_input: IdentifyDataSourcesOutput, **kwargs) -> SetUpDataStorageOutput:
    """
    Proposes a data storage solution suitable for high-volume option data.

    Parameters
    ----------
    data_sources : List[str]
        List of data sources required for the strategy

    Returns
    -------
    {database_type: str, schema_outline: str, partition_strategy: str, retention_policy: str, data_storage_size: int, is_cloud_based: bool}
        A dictionary containing the proposed data storage solution details

    Raises
    ------
    ValueError
        If the data source is invalid or unsupported

    Examples
    --------
    >>> set_up_data_storage(data_sources=['exchange_tick_data',
    'option_chain_feeds'])
    {'database_type': 'time-series', 'schema_outline': '...',
    'partition_strategy': 'by_date', 'retention_policy': 'time-based',
    'data_storage_size': 1000, 'is_cloud_based': True}

    """
    return SetUpDataStorageOutput(
        database_type="",
        schema_outline="",
        partition_strategy="",
        retention_policy="",
        data_storage_size=0,
        is_cloud_based=False,
    )