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


class DesignMonitoringAndAlertsOutput(BaseModel):
    """Pydantic model for design_monitoring_and_alerts node outputs."""
    monitoring_dashboard_design: str = (
        Field(..., description="Description of the monitoring dashboard design")
    )
    alert_rules: List[str] = (
        Field(..., description="List of alert rules for key metrics")
    )
    alert_channels: List[str] = (
        Field(..., description="List of alert channels (e.g., email, SMS, webhook)")
    )
    key_metrics: List[str] = (
        Field(..., description="List of key metrics to be monitored (e.g., PnL, risk limits, system health)")
    )
    threshold_values: List[float] = (
        Field(..., description="List of threshold values for each key metric")
    )


class GenerateReportsOutput(BaseModel):
    """Pydantic model for generate_reports node outputs."""
    report_markdown: str = (
        Field(..., description="The comprehensive report in Markdown format")
    )
    performance_metrics: List[str] = (
        Field(..., description="List of performance metrics (e.g., cumulative return, Sharpe ratio, max drawdown)")
    )
    risk_assessment: str = (
        Field(..., description="Summary of risk assessment (e.g., volatility, tail risk, position concentration)")
    )
    monitoring_alerts: List[str] = (
        Field(..., description="List of monitoring alerts and their configurations")
    )


def generate_reports(evaluate_backtest_performance_input: EvaluateBacktestPerformanceOutput, evaluate_backtest_risk_input: EvaluateBacktestRiskOutput, design_monitoring_and_alerts_input: DesignMonitoringAndAlertsOutput, **kwargs) -> GenerateReportsOutput:
    """Delivers an actionable, data-driven performance and risk report to support strategic decision-making, providing a comprehensive synthesis of backtesting output, risk assessment, and live simulation insights.

    Args:
        evaluate_backtest_performance_input: Input from the 'evaluate_backtest_performance' node.
        evaluate_backtest_risk_input: Input from the 'evaluate_backtest_risk' node.
        design_monitoring_and_alerts_input: Input from the 'design_monitoring_and_alerts' node.
        **kwargs: Additional keyword arguments.

    Returns:
        GenerateReportsOutput: Object containing outputs for this node.
    """
    # TODO: Implement this function

    # Return stub output with placeholder values
    return GenerateReportsOutput(
        report_markdown="",
        performance_metrics=[],
        risk_assessment="",
        monitoring_alerts=[],
    )