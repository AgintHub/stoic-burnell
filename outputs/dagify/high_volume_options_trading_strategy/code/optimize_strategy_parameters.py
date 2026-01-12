from ._optimize_strategy_parameters.combine_performance_and_risk_metrics import combine_performance_and_risk_metrics
from ._optimize_strategy_parameters.select_optimization_method import select_optimization_method
from ._optimize_strategy_parameters.define_parameter_search_space import define_parameter_search_space
from ._optimize_strategy_parameters.run_optimization_algorithm import run_optimization_algorithm
from ._optimize_strategy_parameters.extract_best_parameters import extract_best_parameters
from ._optimize_strategy_parameters.validate_optimization_success import validate_optimization_success
from ._optimize_strategy_parameters.calculate_best_performance_metric import calculate_best_performance_metric

from pydantic import BaseModel, Field
from typing import List


class EvaluateBacktestPerformanceOutput(BaseModel):
    """Pydantic model for evaluate_backtest_performance node outputs."""
    meets_performance_goals: bool = (
        Field(..., description = (
            "Whether the strategy meets its performance goals")
        )
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
        Field(..., description = (
            "Value-at-Risk (VaR) of the backtest returns at 95% confidence level")
        )
    )
    expected_shortfall: float = (
        Field(..., description = (
            "Expected Shortfall (ES) of the backtest returns at 95% confidence level")
        )
    )
    max_drawdown: float = (
        Field(..., description="Maximum drawdown of the backtest returns")
    )
    tail_risk: List[float] = (
        Field(..., description = (
            "List of tail risk metrics (e.g., 1% and 5% quantile returns)")
        )
    )
    position_concentration: float = (
        Field(..., description = (
            "Herfindahl-Hirschman Index (HHI) of position concentration")
        )
    )
    liquidity_impact: float = (
        Field(..., description = (
            "Estimated liquidity impact of the strategy (e.g., price impact, slippage)")
        )
    )


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
    current_metrics = combine_performance_and_risk_metrics(performance=evaluate_backtest_performance_input, risk=evaluate_backtest_risk_input)
    optimization_method: str = select_optimization_method(performance_data=evaluate_backtest_performance_input, risk_data=evaluate_backtest_risk_input)
    parameter_space = define_parameter_search_space(current_performance=evaluate_backtest_performance_input, weaknesses=evaluate_backtest_performance_input.weaknesses)
    optimization_results = run_optimization_algorithm(method=optimization_method, parameter_space=parameter_space, target_metrics=current_metrics)
    optimized_params: List[str] = extract_best_parameters(results=optimization_results)
    is_successful: bool = validate_optimization_success(results=optimization_results, original_metrics=current_metrics)
    best_metric: float = calculate_best_performance_metric(results=optimization_results)
    return OptimizeStrategyParametersOutput(
        optimized_parameters=optimized_params,
        optimization_method=optimization_method,
        is_optimization_successful=is_successful,
        best_performance_metric=best_metric
    )