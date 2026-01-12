from pydantic import BaseModel, Field


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
    return DefineStrategyObjectivesOutput(
        target_annual_return=0.0,
        acceptable_volatility=0.0,
        maximum_drawdown=0.0,
        liquidity_requirements="",
        market_scope="",
    )