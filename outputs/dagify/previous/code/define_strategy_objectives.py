from ._define_strategy_objectives.parse_strategy_input import parse_strategy_input
from ._define_strategy_objectives.fetch_market_historical_data import fetch_market_historical_data
from ._define_strategy_objectives.run_strategy_backtesting import run_strategy_backtesting
from ._define_strategy_objectives.calculate_target_annual_return import calculate_target_annual_return
from ._define_strategy_objectives.perform_stress_testing import perform_stress_testing
from ._define_strategy_objectives.determine_acceptable_volatility import determine_acceptable_volatility
from ._define_strategy_objectives.calculate_maximum_drawdown import calculate_maximum_drawdown
from ._define_strategy_objectives.analyze_market_liquidity import analyze_market_liquidity
from ._define_strategy_objectives.determine_liquidity_requirements import determine_liquidity_requirements
from ._define_strategy_objectives.evaluate_market_constraints import evaluate_market_constraints
from ._define_strategy_objectives.define_market_scope import define_market_scope

from pydantic import BaseModel, Field


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


def define_strategy_objectives(general_input: str, **kwargs) -> DefineStrategyObjectivesOutput:
    """
    Defines detailed quantitative objectives and their technical rationales for
    a high-frequency options trading strategy, supporting precise implementation
    and risk-adjusted performance targets.

    Parameters
    ----------
    target_annual_return : float
        Expected annualized return percentage, derived from backtesting and
        simulation under assumed market conditions, incorporating
        considerations for compounding, slippage, and transaction costs.
    acceptable_volatility : float
        Maximum acceptable annualized standard deviation of returns, based
        on historical data and stress test scenarios; controls exposure to
        risky market fluctuations and ensures manageable drawdowns.
    maximum_drawdown : float
        Predefined cap on the largest peak-to-trough decline during the
        strategy lifecycle, aligned with investor risk appetite, tolerances
        learned from historical market drawdowns, and postulated stress
        scenarios.
    liquidity_requirements : str
        Liquidity threshold setting, guiding the positioning and order size
        limits; derived from minimum bid-ask spreads, average daily volume,
        and settlement cycles, to ensure seamless trade execution without
        significant market impact.
    market_scope : str
        Explicit market universe inclusion criteria, considering regulatory
        constraints, data granularity, trading hours, and systemic risk
        factors, to ensure the strategy operates within feasible and
        compliant domains.

    Returns
    -------
    void
        This function outputs configuration parameters and constraints that
        inform downstream module design, risk controls, and performance
        monitoring protocols, serving as a blueprint for strategy
        implementation.

    Examples
    --------
    >>> Define target annual return as 20.0%
    >>> Set acceptable volatility to 10.0%
    >>> Limit maximum drawdown to 30.0%
    >>> Require high liquidity for execution reliability
    >>> Focus on US stock options market
    Configuration parameters established with justified thresholds, suitable for
    incorporation into trading system constraints and risk controls.

    """
    parsed_input: dict = parse_strategy_input(input_text=general_input, kwargs=kwargs)
    
    historical_data: dict = fetch_market_historical_data(market_scope=parsed_input.get('market_scope', 'US stock options'))
    
    backtesting_results: dict = run_strategy_backtesting(historical_data=historical_data, parameters=parsed_input)
    
    target_return: float = calculate_target_annual_return(backtesting_results=backtesting_results, compounding_factor=True, transaction_costs=True)
    
    stress_test_results: dict = perform_stress_testing(historical_data=historical_data, scenarios=['market_crash', 'volatility_spike', 'liquidity_crisis'])
    
    volatility_threshold: float = determine_acceptable_volatility(stress_results=stress_test_results, historical_volatility=historical_data)
    
    drawdown_limit: float = calculate_maximum_drawdown(stress_results=stress_test_results, risk_appetite='moderate')
    
    liquidity_analysis: dict = analyze_market_liquidity(market_data=historical_data, bid_ask_spreads=True, daily_volumes=True)
    
    liquidity_level: str = determine_liquidity_requirements(analysis=liquidity_analysis, execution_needs='high_frequency')
    
    market_constraints: dict = evaluate_market_constraints(regulatory_requirements=True, data_availability=True, trading_hours=True)
    
    final_market_scope: str = define_market_scope(constraints=market_constraints, liquidity_analysis=liquidity_analysis)
    
    return DefineStrategyObjectivesOutput(
        target_annual_return=target_return,
        acceptable_volatility=volatility_threshold,
        maximum_drawdown=drawdown_limit,
        liquidity_requirements=liquidity_level,
        market_scope=final_market_scope
    )