from ._evaluate_backtest_performance.get_performance_thresholds import get_performance_thresholds
from ._evaluate_backtest_performance.evaluate_against_goals import evaluate_against_goals
from ._evaluate_backtest_performance.identify_strategy_strengths import identify_strategy_strengths
from ._evaluate_backtest_performance.identify_strategy_weaknesses import identify_strategy_weaknesses

from pydantic import BaseModel, Field
from typing import List


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


def evaluate_backtest_performance(run_backtest_input: RunBacktestOutput, **kwargs) -> EvaluateBacktestPerformanceOutput:
    """
    Evaluates the performance of a backtested trading strategy.

    Returns
    -------
    Dict[str, object]
        A JSON object containing performance metrics and strategy evaluation
        results.
    """
    performance_thresholds: dict = get_performance_thresholds(**kwargs)
    
    meets_goals: bool = evaluate_against_goals(
        cumulative_return=run_backtest_input.cumulative_return,
        sharpe_ratio=run_backtest_input.sharpe_ratio,
        max_drawdown=run_backtest_input.max_drawdown,
        win_rate=run_backtest_input.win_rate,
        thresholds=performance_thresholds
    )
    
    strengths: List[str] = identify_strategy_strengths(
        cumulative_return=run_backtest_input.cumulative_return,
        sharpe_ratio=run_backtest_input.sharpe_ratio,
        max_drawdown=run_backtest_input.max_drawdown,
        win_rate=run_backtest_input.win_rate
    )
    
    weaknesses: List[str] = identify_strategy_weaknesses(
        cumulative_return=run_backtest_input.cumulative_return,
        sharpe_ratio=run_backtest_input.sharpe_ratio,
        max_drawdown=run_backtest_input.max_drawdown,
        win_rate=run_backtest_input.win_rate
    )
    
    return EvaluateBacktestPerformanceOutput(
        meets_performance_goals=meets_goals,
        cumulative_return=run_backtest_input.cumulative_return,
        sharpe_ratio=run_backtest_input.sharpe_ratio,
        max_drawdown=run_backtest_input.max_drawdown,
        win_rate=run_backtest_input.win_rate,
        strengths=strengths,
        weaknesses=weaknesses
    )