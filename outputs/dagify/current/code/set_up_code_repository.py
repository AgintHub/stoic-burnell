from pydantic import BaseModel, Field
from typing import List


class DefineStrategyObjectivesOutput(BaseModel):
    """Pydantic model for define_strategy_objectives node outputs."""
    target_annual_return: float = (
        Field(..., description="Target annual return for the strategy (e.g., 20.0 for 20%)")
    )
    acceptable_volatility: float = (
        Field(..., description="Acceptable volatility for the strategy (e.g., 10.0 for 10%)")
    )
    maximum_drawdown: float = (
        Field(..., description="Maximum drawdown for the strategy (e.g., 30.0 for 30%)")
    )
    liquidity_requirements: str = (
        Field(..., description="Liquidity requirements for the strategy (e.g., 'high', 'medium', 'low')")
    )
    market_scope: str = (
        Field(..., description="Market scope for the strategy (e.g., 'US stocks', 'EU stocks', 'currencies')")
    )


class SetUpCodeRepositoryOutput(BaseModel):
    """Pydantic model for set_up_code_repository node outputs."""
    repository_layout: str = (
        Field(..., description="Description of the repository layout")
    )
    folder_names: List[str] = (
        Field(..., description="List of folder names in the repository")
    )
    file_templates: List[str] = (
        Field(..., description="List of file templates in the repository")
    )


def set_up_code_repository(define_strategy_objectives_input: DefineStrategyObjectivesOutput, **kwargs) -> SetUpCodeRepositoryOutput:
    """
    Configures a code repository structure for high-volume options trading,
    encapsulating core components, supporting libraries, and testing
    infrastructure.

    Parameters
    ----------
    strategy_components : list
        List of key components to be included in the repository
    repository_layout : dict
        Customizable layout for the repository

    Returns
    -------
    dict
        Mapped output structure with repository layout and essential files

    Raises
    ------
    RepositoryError
        Raised when repository setup fails due to incompatible system or
        library versions

    Examples
    --------
    >>> Repository layout: {core: module, data: {loading: data_loader.py,
    calculations: data_calculations.py}}
    Repository created with core module and data subdirectories containing
    essential files

    """
    return SetUpCodeRepositoryOutput(
        repository_layout="",
        folder_names=[],
        file_templates=[],
    )