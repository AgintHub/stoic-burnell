from pydantic import BaseModel, Field
from typing import List


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


def evaluate_backtest_performance(run_backtest_input: RunBacktestOutput, **kwargs) -> EvaluateBacktestPerformanceOutput:
    """
    Evaluates the performance of a backtested trading strategy.

    Returns
    -------
    Dict[str, object]
        A JSON object containing performance metrics and strategy evaluation
        results.
    """
    return EvaluateBacktestPerformanceOutput(
        meets_performance_goals=False,
        cumulative_return=0.0,
        sharpe_ratio=0.0,
        max_drawdown=0.0,
        win_rate=0.0,
        strengths=[],
        weaknesses=[],
    )