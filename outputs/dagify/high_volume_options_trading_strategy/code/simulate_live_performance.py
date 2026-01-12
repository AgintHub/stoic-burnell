from ._simulate_live_performance.validate_optimization_parameters import validate_optimization_parameters
from ._simulate_live_performance.fetch_realistic_market_data import fetch_realistic_market_data
from ._simulate_live_performance.configure_trading_strategy import configure_trading_strategy
from ._simulate_live_performance.run_live_trading_simulation import run_live_trading_simulation
from ._simulate_live_performance.calculate_expected_annual_return import calculate_expected_annual_return
from ._simulate_live_performance.calculate_expected_volatility import calculate_expected_volatility
from ._simulate_live_performance.calculate_sharpe_ratio import calculate_sharpe_ratio
from ._simulate_live_performance.calculate_max_drawdown import calculate_max_drawdown
from ._simulate_live_performance.count_executed_trades import count_executed_trades
from ._simulate_live_performance.calculate_win_rate import calculate_win_rate
from ._simulate_live_performance.calculate_value_at_risk import calculate_value_at_risk

from pydantic import BaseModel, Field
from typing import List


class OptimizeStrategyParametersOutput(BaseModel):
    """Pydantic model for optimize_strategy_parameters node outputs."""
    optimized_parameters: List[str] = (
        Field(..., description="List of optimized strategy hyperparameters")
    )
    optimization_method: str = (
        Field(..., description = (
            "Method used for optimization (e.g., grid search, Bayesian)")
        )
    )
    is_optimization_successful: bool = (
        Field(..., description = (
            "Whether the optimization process was successful")
        )
    )
    best_performance_metric: float = (
        Field(..., description="Value of the best performance metric achieved")
    )


class SimulateLivePerformanceOutput(BaseModel):
    """Pydantic model for simulate_live_performance node outputs."""
    expected_annual_return: float = (
        Field(..., description="The expected annual return of the strategy")
    )
    expected_volatility: float = (
        Field(..., description="The expected volatility of the strategy")
    )
    sharpe_ratio: float = (
        Field(..., description="The Sharpe ratio of the strategy")
    )
    max_drawdown: float = (
        Field(..., description="The maximum drawdown of the strategy")
    )
    trade_count: int = Field(..., description="The number of trades executed")
    win_rate: float = Field(..., description="The win rate of the strategy")
    value_at_risk: float = (
        Field(..., description="The Value-at-Risk (VaR) of the strategy")
    )


def simulate_live_performance(optimize_strategy_parameters_input: OptimizeStrategyParametersOutput, **kwargs) -> SimulateLivePerformanceOutput:
    """
    Simulates live trading performance using optimized strategy parameters and
    realistic market conditions.

    Parameters
    ----------
    optimized_parameters : List[str]
        List of optimized strategy hyperparameters
    optimization_method : str
        Method used for optimization (e.g., grid search, Bayesian)

    Returns
    -------
    dict
        Dictionary containing performance metrics: expected_annual_return,
        expected_volatility, sharpe_ratio, max_drawdown, trade_count,
        win_rate, value_at_risk

    Raises
    ------
    ValueError
        If optimized_parameters is empty or invalid

    Examples
    --------
    >>> simulate_live_performance(optimized_parameters=['param1', 'param2'],
    optimization_method='grid_search')
    {'expected_annual_return': 0.2, 'expected_volatility': 0.1, 'sharpe_ratio':
    1.5, 'max_drawdown': 0.3, 'trade_count': 1000, 'win_rate': 0.6,
    'value_at_risk': 0.05}

    """
    if not optimize_strategy_parameters_input.optimized_parameters:
        raise ValueError("Optimized parameters cannot be empty")
    
    validated_parameters: List[str] = validate_optimization_parameters(
        parameters=optimize_strategy_parameters_input.optimized_parameters,
        method=optimize_strategy_parameters_input.optimization_method
    )
    
    market_data: dict = fetch_realistic_market_data(
        parameters=validated_parameters
    )
    
    trading_strategy: dict = configure_trading_strategy(
        parameters=validated_parameters,
        optimization_method=optimize_strategy_parameters_input.optimization_method
    )
    
    simulation_results: dict = run_live_trading_simulation(
        strategy=trading_strategy,
        market_data=market_data,
        parameters=validated_parameters
    )
    
    annual_return: float = calculate_expected_annual_return(
        simulation_results=simulation_results
    )
    
    volatility: float = calculate_expected_volatility(
        simulation_results=simulation_results
    )
    
    sharpe: float = calculate_sharpe_ratio(
        annual_return=annual_return,
        volatility=volatility
    )
    
    drawdown: float = calculate_max_drawdown(
        simulation_results=simulation_results
    )
    
    trades: int = count_executed_trades(
        simulation_results=simulation_results
    )
    
    win_rate: float = calculate_win_rate(
        simulation_results=simulation_results
    )
    
    var: float = calculate_value_at_risk(
        simulation_results=simulation_results
    )
    
    return SimulateLivePerformanceOutput(
        expected_annual_return=annual_return,
        expected_volatility=volatility,
        sharpe_ratio=sharpe,
        max_drawdown=drawdown,
        trade_count=trades,
        win_rate=win_rate,
        value_at_risk=var
    )