from pydantic import BaseModel, Field
from typing import List


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


class DesignRiskControlsOutput(BaseModel):
    """Pydantic model for design_risk_controls node outputs."""
    position_limits: List[float] = (
        Field(..., description="List of position limits for each asset")
    )
    var_constraints: List[float] = (
        Field(..., description="List of Value-at-Risk (VaR) constraints for each asset")
    )
    stop_loss_thresholds: List[float] = (
        Field(..., description="List of stop-loss thresholds for each asset")
    )
    risk_control_rules: List[str] = (
        Field(..., description="List of risk control rules")
    )
    is_risk_control_satisfied: bool = (
        Field(..., description="Whether the risk control rules are satisfied")
    )


def design_risk_controls(evaluate_backtest_risk_input: EvaluateBacktestRiskOutput, **kwargs) -> DesignRiskControlsOutput:
    """
    Designs and implements risk management controls for live trading.

    Parameters
    ----------
    backtest_risk_metrics : dict
        Input risk metrics from the evaluate_backtest_risk node.
    risk_tolerance : dict
        Risk tolerance parameters, including position limits, VaR
        constraints, and stop-loss thresholds.

    Returns
    -------
    dict
        A set of risk control rules and an indicator of whether they are
        currently satisfied.

    Raises
    ------
    ValueError
        Raised if input data is invalid or risk tolerance parameters are
        contradictory.

    Examples
    --------
    >>> backtest_risk_metrics = evaluate_backtest_risk().output
    >>> risk_tolerance = {'position_limits': [100000, 500000],
    'var_constraints': [0.05, 0.10], 'stop_loss_thresholds': [50, 100]}
    >>> risk_control_rules, is_risk_control_satisfied =
    design_risk_controls(backtest_risk_metrics, risk_tolerance)
    {'risk_control_rules': ['Position limit 100000 reached on asset A', 'VaR
    constraint 0.05 exceeded on asset B'], 'is_risk_control_satisfied': False}

    """
    return DesignRiskControlsOutput(
        position_limits=[],
        var_constraints=[],
        stop_loss_thresholds=[],
        risk_control_rules=[],
        is_risk_control_satisfied=False,
    )