from ._generate_reports.create_performance_summary import create_performance_summary
from ._generate_reports.create_risk_assessment_summary import create_risk_assessment_summary
from ._generate_reports.create_monitoring_summary import create_monitoring_summary
from ._generate_reports.format_strengths_weaknesses import format_strengths_weaknesses
from ._generate_reports.compile_comprehensive_report import compile_comprehensive_report
from ._generate_reports.extract_performance_metrics import extract_performance_metrics
from ._generate_reports.format_monitoring_alerts import format_monitoring_alerts

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


class DesignMonitoringAndAlertsOutput(BaseModel):
    """Pydantic model for design_monitoring_and_alerts node outputs."""
    monitoring_dashboard_design: str = (
        Field(..., description="Description of the monitoring dashboard design")
    )
    alert_rules: List[str] = (
        Field(..., description="List of alert rules for key metrics")
    )
    alert_channels: List[str] = (
        Field(..., description = (
            "List of alert channels (e.g., email, SMS, webhook)")
        )
    )
    key_metrics: List[str] = (
        Field(..., description = (
            "List of key metrics to be monitored (e.g., PnL, risk limits, system health)")
        )
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
        Field(..., description = (
            "List of performance metrics (e.g., cumulative return, Sharpe ratio, max drawdown)")
        )
    )
    risk_assessment: str = (
        Field(..., description = (
            "Summary of risk assessment (e.g., volatility, tail risk, position concentration)")
        )
    )
    monitoring_alerts: List[str] = (
        Field(..., description = (
            "List of monitoring alerts and their configurations")
        )
    )


def generate_reports(evaluate_backtest_performance_input: EvaluateBacktestPerformanceOutput, evaluate_backtest_risk_input: EvaluateBacktestRiskOutput, design_monitoring_and_alerts_input: DesignMonitoringAndAlertsOutput, **kwargs) -> GenerateReportsOutput:
    performance_summary: str = create_performance_summary(
        cumulative_return=evaluate_backtest_performance_input.cumulative_return,
        sharpe_ratio=evaluate_backtest_performance_input.sharpe_ratio,
        max_drawdown=evaluate_backtest_performance_input.max_drawdown,
        win_rate=evaluate_backtest_performance_input.win_rate,
        meets_goals=evaluate_backtest_performance_input.meets_performance_goals
    )
    
    risk_summary: str = create_risk_assessment_summary(
        volatility=evaluate_backtest_risk_input.volatility,
        var=evaluate_backtest_risk_input.value_at_risk,
        expected_shortfall=evaluate_backtest_risk_input.expected_shortfall,
        tail_risk=evaluate_backtest_risk_input.tail_risk,
        concentration=evaluate_backtest_risk_input.position_concentration,
        liquidity_impact=evaluate_backtest_risk_input.liquidity_impact
    )
    
    monitoring_summary: str = create_monitoring_summary(
        dashboard_design=design_monitoring_and_alerts_input.monitoring_dashboard_design,
        alert_rules=design_monitoring_and_alerts_input.alert_rules,
        alert_channels=design_monitoring_and_alerts_input.alert_channels,
        key_metrics=design_monitoring_and_alerts_input.key_metrics,
        threshold_values=design_monitoring_and_alerts_input.threshold_values
    )
    
    strengths_weaknesses: str = format_strengths_weaknesses(
        strengths=evaluate_backtest_performance_input.strengths,
        weaknesses=evaluate_backtest_performance_input.weaknesses
    )
    
    report_markdown: str = compile_comprehensive_report(
        performance_section=performance_summary,
        risk_section=risk_summary,
        monitoring_section=monitoring_summary,
        strengths_weaknesses_section=strengths_weaknesses
    )
    
    performance_metrics: List[str] = extract_performance_metrics(
        performance_input=evaluate_backtest_performance_input
    )
    
    monitoring_alerts: List[str] = format_monitoring_alerts(
        alert_rules=design_monitoring_and_alerts_input.alert_rules,
        alert_channels=design_monitoring_and_alerts_input.alert_channels,
        key_metrics=design_monitoring_and_alerts_input.key_metrics,
        threshold_values=design_monitoring_and_alerts_input.threshold_values
    )
    
    return GenerateReportsOutput(
        report_markdown=report_markdown,
        performance_metrics=performance_metrics,
        risk_assessment=risk_summary,
        monitoring_alerts=monitoring_alerts
    )