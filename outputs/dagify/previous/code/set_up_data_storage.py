from ._set_up_data_storage.validate_data_sources import validate_data_sources
from ._set_up_data_storage.estimate_data_volumes import estimate_data_volumes
from ._set_up_data_storage.determine_optimal_database_type import determine_optimal_database_type
from ._set_up_data_storage.design_database_schema import design_database_schema
from ._set_up_data_storage.define_partition_strategy import define_partition_strategy
from ._set_up_data_storage.define_retention_policy import define_retention_policy
from ._set_up_data_storage.calculate_storage_requirements import calculate_storage_requirements
from ._set_up_data_storage.recommend_cloud_deployment import recommend_cloud_deployment

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


class SetUpDataStorageOutput(BaseModel):
    """Pydantic model for set_up_data_storage node outputs."""
    database_type: str = (
        Field(..., description = (
            "Type of the database (e.g., relational, NoSQL, time-series)")
        )
    )
    schema_outline: str = (
        Field(..., description="Detailed outline of the database schema")
    )
    partition_strategy: str = (
        Field(..., description = (
            "Strategy used for partitioning data (e.g., by date, by type)")
        )
    )
    retention_policy: str = (
        Field(..., description = (
            "Policy for data retention (e.g., time-based, size-based)")
        )
    )
    data_storage_size: int = (
        Field(..., description="Estimated size of the data storage needed")
    )
    is_cloud_based: bool = (
        Field(..., description = (
            "Whether the data storage solution is cloud-based")
        )
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
    validated_sources: List[str] = validate_data_sources(data_sources=identify_data_sources_input.data_source_names)
    
    volume_estimates: dict = estimate_data_volumes(data_sources=validated_sources, frequencies=identify_data_sources_input.data_frequencies)
    
    optimal_db_type: str = determine_optimal_database_type(data_sources=validated_sources, volume_estimates=volume_estimates)
    
    schema_design: str = design_database_schema(database_type=optimal_db_type, data_sources=validated_sources, frequencies=identify_data_sources_input.data_frequencies)
    
    partition_plan: str = define_partition_strategy(database_type=optimal_db_type, data_volume=volume_estimates, frequencies=identify_data_sources_input.data_frequencies)
    
    retention_plan: str = define_retention_policy(data_sources=validated_sources, licensing_constraints=identify_data_sources_input.licensing_constraints)
    
    storage_size: int = calculate_storage_requirements(volume_estimates=volume_estimates, retention_policy=retention_plan)
    
    cloud_recommendation: bool = recommend_cloud_deployment(storage_size=storage_size, data_sources=validated_sources)
    
    return SetUpDataStorageOutput(
        database_type=optimal_db_type,
        schema_outline=schema_design,
        partition_strategy=partition_plan,
        retention_policy=retention_plan,
        data_storage_size=storage_size,
        is_cloud_based=cloud_recommendation
    )