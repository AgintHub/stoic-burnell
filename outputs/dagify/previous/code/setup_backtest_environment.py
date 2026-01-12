from ._setup_backtest_environment.select_backtesting_framework import select_backtesting_framework
from ._setup_backtest_environment.configure_data_adapters import configure_data_adapters
from ._setup_backtest_environment.setup_simulation_parameters import setup_simulation_parameters
from ._setup_backtest_environment.create_framework_configuration import create_framework_configuration
from ._setup_backtest_environment.validate_environment_setup import validate_environment_setup

from pydantic import BaseModel, Field
from typing import List


class DesignStrategyLogicOutput(BaseModel):
    """Pydantic model for design_strategy_logic node outputs."""
    entry_signals: List[str] = (
        Field(..., description="List of conditions for entering a trade")
    )
    exit_rules: List[str] = (
        Field(..., description="List of conditions for exiting a trade")
    )
    position_sizing: str = (
        Field(..., description = (
            "Method for determining position size (e.g., fixed, risk-based)")
        )
    )
    risk_limits: List[float] = (
        Field(..., description = (
            "List of risk limits (e.g., stop-loss, take-profit levels)")
        )
    )
    decision_tree: str = (
        Field(..., description = (
            "High-level overview of the decision-making process")
        )
    )


class SetupBacktestEnvironmentOutput(BaseModel):
    """Pydantic model for setup_backtest_environment node outputs."""
    backtesting_framework: str = (
        Field(..., description = (
            "The name of the backtesting framework used (e.g., Zipline, backtrader)")
        )
    )
    data_adapters: List[str] = (
        Field(..., description = (
            "List of data adapters used for the backtest (e.g., CSV, database connections)")
        )
    )
    simulation_parameters: str = (
        Field(..., description = (
            "Simulation parameters such as start and end dates, initial capital, and frequency")
        )
    )
    configuration: str = (
        Field(..., description = (
            "Any additional configuration details for the backtesting framework")
        )
    )
    is_setup_successful: bool = (
        Field(..., description = (
            "Whether the backtesting environment was successfully set up")
        )
    )


def setup_backtest_environment(design_strategy_logic_input: DesignStrategyLogicOutput, **kwargs) -> SetupBacktestEnvironmentOutput:
    """
    Establishes a robust backtesting framework for trading strategies,
    integrating data adapters, simulation parameters, configuration, and
    execution metrics.

    Parameters
    ----------
    backtesting_framework : str
        Type of backtesting framework to use (e.g., Zipline, backtrader)
    data_adapters : List[str]
        Chosen data adapters for backtesting
    simulation_parameters : PrimitiveType.DICT
        Simulation parameters object, including start and end dates, initial
        capital, frequency.
    configuration : PrimitiveType.DICT
        Backtesting framework configuration object.

    Returns
    -------
    PrimitiveType.DICT
        Configuration dictionary with details about the backtesting
        environment.

    Raises
    ------
    Exception
        Raised when setup fails due to configuration conflicts or missing
        dependencies.
    """
    backtesting_framework: str = select_backtesting_framework(strategy_logic=design_strategy_logic_input, available_frameworks=["Zipline", "backtrader"])
    data_adapters: List[str] = configure_data_adapters(framework=backtesting_framework, strategy_requirements=design_strategy_logic_input)
    simulation_params: str = setup_simulation_parameters(strategy=design_strategy_logic_input, kwargs=kwargs)
    config_dict: str = create_framework_configuration(framework=backtesting_framework, adapters=data_adapters, params=simulation_params)
    setup_success: bool = validate_environment_setup(framework=backtesting_framework, adapters=data_adapters, config=config_dict)
    return SetupBacktestEnvironmentOutput(
        backtesting_framework=backtesting_framework,
        data_adapters=data_adapters,
        simulation_parameters=simulation_params,
        configuration=config_dict,
        is_setup_successful=setup_success,
    )