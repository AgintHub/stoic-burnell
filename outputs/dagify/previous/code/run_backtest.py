from pydantic import BaseModel, Field
from typing import List


class SetupBacktestEnvironmentOutput(BaseModel):
    """Pydantic model for setup_backtest_environment node outputs."""
    backtesting_framework: str = (
        Field(..., description="The name of the backtesting framework used (e.g., Zipline, backtrader)")
    )
    data_adapters: List[str] = (
        Field(..., description="List of data adapters used for the backtest (e.g., CSV, database connections)")
    )
    simulation_parameters: str = (
        Field(..., description="Simulation parameters such as start and end dates, initial capital, and frequency")
    )
    configuration: str = (
        Field(..., description="Any additional configuration details for the backtesting framework")
    )
    is_setup_successful: bool = (
        Field(..., description="Whether the backtesting environment was successfully set up")
    )


class CleanAndPrepareDataOutput(BaseModel):
    """Pydantic model for clean_and_prepare_data node outputs."""
    cleaning_successful: bool = (
        Field(..., description="Whether the data cleaning and preparation were successful")
    )
    number_of_missing_values_handled: int = (
        Field(..., description="Number of missing values handled during the cleaning process")
    )
    derived_fields_calculated: str = (
        Field(..., description="List of derived fields calculated during the preparation process")
    )
    dataset_ready: bool = (
        Field(..., description="Whether the dataset is ready for feature engineering")
    )


class RunBacktestOutput(BaseModel):
    """Pydantic model for run_backtest node outputs."""
    cumulative_return: float = (
        Field(..., description="The total return of the strategy over the backtest period")
    )
    sharpe_ratio: float = (
        Field(..., description="A measure of the strategy's risk-adjusted return")
    )
    max_drawdown: float = (
        Field(..., description="The maximum peak-to-trough decline in the strategy's value during the backtest")
    )
    win_rate: float = (
        Field(..., description="The percentage of trades that resulted in a profit")
    )


def run_backtest(setup_backtest_environment_input: SetupBacktestEnvironmentOutput, clean_and_prepare_data_input: CleanAndPrepareDataOutput, **kwargs) -> RunBacktestOutput:
    """
    Executes a rigorous backtest of a trading strategy and returns key
    performance metrics.

    Returns
    -------
    JSON object
        Backtest results with cumulative return, Sharpe ratio, max drawdown,
        and win rate

    Examples
    --------
    >>> from backtest_framework import Backtest
    >>> bp = Backtest(data, strategy, params)
    Backtest results: cumulative_return=1.2ℕ, sharpe_ratio=1.5ℕℕ,
    max_drawdown=0.8ℕ, win_rate=60%

    """
    return RunBacktestOutput(
        cumulative_return=0.0,
        sharpe_ratio=0.0,
        max_drawdown=0.0,
        win_rate=0.0,
    )