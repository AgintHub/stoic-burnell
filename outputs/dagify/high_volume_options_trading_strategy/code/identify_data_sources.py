from ._identify_data_sources.analyze_market_scope_requirements import analyze_market_scope_requirements
from ._identify_data_sources.determine_frequency_requirements import determine_frequency_requirements
from ._identify_data_sources.query_vendor_database import query_vendor_database
from ._identify_data_sources.map_vendors_to_data_sources import map_vendors_to_data_sources
from ._identify_data_sources.retrieve_licensing_constraints import retrieve_licensing_constraints

from pydantic import BaseModel, Field
from typing import List


class DefineStrategyObjectivesOutput(BaseModel):
    """Pydantic model for define_strategy_objectives node outputs."""
    target_annual_return: float = (
        Field(..., description = (
            "Target annual return for the strategy (e.g., 20.0 for 20%)")
        )
    )
    acceptable_volatility: float = (
        Field(..., description = (
            "Acceptable volatility for the strategy (e.g., 10.0 for 10%)")
        )
    )
    maximum_drawdown: float = (
        Field(..., description = (
            "Maximum drawdown for the strategy (e.g., 30.0 for 30%)")
        )
    )
    liquidity_requirements: str = (
        Field(..., description = (
            "Liquidity requirements for the strategy (e.g., 'high', 'medium', 'low')")
        )
    )
    market_scope: str = (
        Field(..., description = (
            "Market scope for the strategy (e.g., 'US stocks', 'EU stocks', 'currencies')")
        )
    )


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


def identify_data_sources(define_strategy_objectives_input: DefineStrategyObjectivesOutput, **kwargs) -> IdentifyDataSourcesOutput:
    market_data_requirements: List[str] = analyze_market_scope_requirements(market_scope=define_strategy_objectives_input.market_scope)
    frequency_needs: List[str] = determine_frequency_requirements(volatility=define_strategy_objectives_input.acceptable_volatility, liquidity=define_strategy_objectives_input.liquidity_requirements)
    available_vendors: List[str] = query_vendor_database(market_requirements=market_data_requirements, frequency_requirements=frequency_needs)
    data_sources: List[str] = map_vendors_to_data_sources(vendors=available_vendors, market_scope=define_strategy_objectives_input.market_scope)
    licensing_info: List[str] = retrieve_licensing_constraints(vendors=available_vendors, data_sources=data_sources)
    
    return IdentifyDataSourcesOutput(
        data_source_names=data_sources,
        vendor_names=available_vendors,
        data_frequencies=frequency_needs,
        licensing_constraints=licensing_info
    )