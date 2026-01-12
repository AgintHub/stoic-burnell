from ._run_backtest.initialize_backtest_engine import initialize_backtest_engine
from ._run_backtest.prepare_strategy_data import prepare_strategy_data
from ._run_backtest.parse_simulation_parameters import parse_simulation_parameters
from ._run_backtest.load_trading_strategy import load_trading_strategy
from ._run_backtest.execute_backtest import execute_backtest
from ._run_backtest.calculate_performance_metrics import calculate_performance_metrics
from ._run_backtest.extract_cumulative_return import extract_cumulative_return
from ._run_backtest.calculate_sharpe_ratio import calculate_sharpe_ratio
from ._run_backtest.calculate_max_drawdown import calculate_max_drawdown
from ._run_backtest.calculate_win_rate import calculate_win_rate

from pydantic import BaseModel, Field
from typing import List


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


class CleanAndPrepareDataOutput(BaseModel):
    """Pydantic model for clean_and_prepare_data node outputs."""
    cleaning_successful: bool = (
        Field(..., description = (
            "Whether the data cleaning and preparation were successful")
        )
    )
    number_of_missing_values_handled: int = (
        Field(..., description = (
            "Number of missing values handled during the cleaning process")
        )
    )
    derived_fields_calculated: str = (
        Field(..., description = (
            "List of derived fields calculated during the preparation process")
        )
    )
    dataset_ready: bool = (
        Field(..., description = (
            "Whether the dataset is ready for feature engineering")
        )
    )


class RunBacktestOutput(BaseModel):
    """Pydantic model for run_backtest node outputs."""
    cumulative_return: float = (
        Field(..., description = (
            "The total return of the strategy over the backtest period")
        )
    )
    sharpe_ratio: float = (
        Field(..., description = (
            "A measure of the strategy's risk-adjusted return")
        )
    )
    max_drawdown: float = (
        Field(..., description = (
            "The maximum peak-to-trough decline in the strategy's value during the backtest")
        )
    )
    win_rate: float = (
        Field(..., description = (
            "The percentage of trades that resulted in a profit")
        )
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
    backtest_engine = initialize_backtest_engine(framework=setup_backtest_environment_input.backtesting_framework, config=setup_backtest_environment_input.configuration)
    strategy_data = prepare_strategy_data(data_adapters=setup_backtest_environment_input.data_adapters, cleaned_data=clean_and_prepare_data_input)
    simulation_config = parse_simulation_parameters(parameters=setup_backtest_environment_input.simulation_parameters)
    trading_strategy = load_trading_strategy(strategy_params=simulation_config)
    backtest_results = execute_backtest(engine=backtest_engine, strategy=trading_strategy, data=strategy_data)
    performance_metrics = calculate_performance_metrics(results=backtest_results)
    cumulative_return: float = extract_cumulative_return(metrics=performance_metrics)
    sharpe_ratio: float = calculate_sharpe_ratio(metrics=performance_metrics)
    max_drawdown: float = calculate_max_drawdown(metrics=performance_metrics)
    win_rate: float = calculate_win_rate(metrics=performance_metrics)
    return RunBacktestOutput(
        cumulative_return=cumulative_return,
        sharpe_ratio=sharpe_ratio,
        max_drawdown=max_drawdown,
        win_rate=win_rate
    )