from ._set_up_code_repository.extract_strategy_components import extract_strategy_components
from ._set_up_code_repository.create_base_repository_structure import create_base_repository_structure
from ._set_up_code_repository.customize_repository_for_options_trading import customize_repository_for_options_trading
from ._set_up_code_repository.validate_system_compatibility import validate_system_compatibility
from ._set_up_code_repository.generate_folder_names import generate_folder_names
from ._set_up_code_repository.create_file_templates import create_file_templates
from ._set_up_code_repository.format_repository_description import format_repository_description

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
    strategy_components: List[str] = extract_strategy_components(objectives=define_strategy_objectives_input)
    
    base_repository_layout: dict = create_base_repository_structure()
    
    customized_layout: dict = customize_repository_for_options_trading(
        base_layout=base_repository_layout,
        components=strategy_components,
        market_scope=define_strategy_objectives_input.market_scope,
        liquidity_needs=define_strategy_objectives_input.liquidity_requirements
    )
    
    validate_system_compatibility(layout=customized_layout)
    
    folder_structure: List[str] = generate_folder_names(layout=customized_layout)
    
    template_files: List[str] = create_file_templates(
        components=strategy_components,
        layout=customized_layout,
        trading_type="options"
    )
    
    layout_description: str = format_repository_description(layout=customized_layout)
    
    return SetUpCodeRepositoryOutput(
        repository_layout=layout_description,
        folder_names=folder_structure,
        file_templates=template_files
    )