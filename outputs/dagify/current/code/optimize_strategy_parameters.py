from pydantic import BaseModel, Field
from typing import List


class EvaluateBacktestPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_backtest_performance node outputs."""
    meets_performance_goals: bool = (
        Field(..., description="Whether the strategy meets its performance goals")
    )
    cumulative_return: float = (
        Field(..., description="Cumulative return of the strategy")
    )
    sharpe_ratio: float = Field(..., description="Sharpe ratio of the strategy")
    max_drawdown: float = (
        Field(..., description="Maximum drawdown of the strategy")
    )
    win_rate: float = Field(..., description="Win rate of the strategy")
    strengths: List[str] = (
        Field(..., description="List of strengths of the strategy")
    )
    weaknesses: List[str] = (
        Field(..., description="List of weaknesses of the strategy")
    )


class EvaluateBacktestRiskOutput(BaseModel):
    """Pydantic model for evaluate_backtest_risk node outputs."""
    volatility: float = (
        Field(..., description="Annualized volatility of the backtest returns")
    )
    value_at_risk: float = (
        Field(..., description="Value-at-Risk (VaR) of the backtest returns at 95% confidence level")
    )
    expected_shortfall: float = (
        Field(..., description="Expected Shortfall (ES) of the backtest returns at 95% confidence level")
    )
    max_drawdown: float = (
        Field(..., description="Maximum drawdown of the backtest returns")
    )
    tail_risk: List[float] = (
        Field(..., description="List of tail risk metrics (e.g., 1% and 5% quantile returns)")
    )
    position_concentration: float = (
        Field(..., description="Herfindahl-Hirschman Index (HHI) of position concentration")
    )
    liquidity_impact: float = (
        Field(..., description="Estimated liquidity impact of the strategy (e.g., price impact, slippage)")
    )


class OptimizeStrategyParametersOutput(BaseModel):
    """Pydantic model for optimize_strategy_parameters node outputs."""
    optimized_parameters: List[str] = (
        Field(..., description="List of optimized strategy hyperparameters")
    )
    optimization_method: str = (
        Field(..., description="Method used for optimization (e.g., grid search, Bayesian)")
    )
    is_optimization_successful: bool = (
        Field(..., description="Whether the optimization process was successful")
    )
    best_performance_metric: float = (
        Field(..., description="Value of the best performance metric achieved")
    )


def optimize_strategy_parameters(evaluate_backtest_performance_input: EvaluateBacktestPerformanceOutput, evaluate_backtest_risk_input: EvaluateBacktestRiskOutput, **kwargs) -> OptimizeStrategyParametersOutput:
    """
    Optimizes strategy hyperparameters to achieve improved performance and risk
    profiles

    Returns
    -------
    dict
        Dictionary containing the optimized strategy hyperparameters, the
        optimization method used, and the best performance metric achieved
    """
    return OptimizeStrategyParametersOutput(
        optimized_parameters=[],
        optimization_method="",
        is_optimization_successful=False,
        best_performance_metric=0.0,
    )