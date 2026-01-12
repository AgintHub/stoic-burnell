from ._design_risk_controls.validate_input_data import validate_input_data
from ._design_risk_controls.calculate_position_limits import calculate_position_limits
from ._design_risk_controls.determine_var_constraints import determine_var_constraints
from ._design_risk_controls.compute_stop_loss_thresholds import compute_stop_loss_thresholds
from ._design_risk_controls.generate_risk_control_rules import generate_risk_control_rules
from ._design_risk_controls.evaluate_risk_control_satisfaction import evaluate_risk_control_satisfaction

from pydantic import BaseModel, Field
from typing import List


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


class DesignRiskControlsOutput(BaseModel):
    """Pydantic model for design_risk_controls node outputs."""
    position_limits: List[float] = (
        Field(..., description="List of position limits for each asset")
    )
    var_constraints: List[float] = (
        Field(..., description = (
            "List of Value-at-Risk (VaR) constraints for each asset")
        )
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
    risk_tolerance = kwargs.get('risk_tolerance', {})
    
    validate_input_data(backtest_metrics=evaluate_backtest_risk_input, tolerance_params=risk_tolerance)
    
    position_limits: List[float] = calculate_position_limits(
        volatility=evaluate_backtest_risk_input.volatility,
        max_drawdown=evaluate_backtest_risk_input.max_drawdown,
        concentration=evaluate_backtest_risk_input.position_concentration,
        tolerance_limits=risk_tolerance.get('position_limits', [])
    )
    
    var_constraints: List[float] = determine_var_constraints(
        current_var=evaluate_backtest_risk_input.value_at_risk,
        expected_shortfall=evaluate_backtest_risk_input.expected_shortfall,
        tolerance_constraints=risk_tolerance.get('var_constraints', [])
    )
    
    stop_loss_thresholds: List[float] = compute_stop_loss_thresholds(
        tail_risk=evaluate_backtest_risk_input.tail_risk,
        max_drawdown=evaluate_backtest_risk_input.max_drawdown,
        tolerance_thresholds=risk_tolerance.get('stop_loss_thresholds', [])
    )
    
    risk_control_rules: List[str] = generate_risk_control_rules(
        position_limits=position_limits,
        var_constraints=var_constraints,
        stop_loss_thresholds=stop_loss_thresholds,
        current_metrics=evaluate_backtest_risk_input
    )
    
    is_risk_control_satisfied: bool = evaluate_risk_control_satisfaction(
        rules=risk_control_rules,
        current_metrics=evaluate_backtest_risk_input,
        limits=position_limits,
        constraints=var_constraints,
        thresholds=stop_loss_thresholds
    )
    
    return DesignRiskControlsOutput(
        position_limits=position_limits,
        var_constraints=var_constraints,
        stop_loss_thresholds=stop_loss_thresholds,
        risk_control_rules=risk_control_rules,
        is_risk_control_satisfied=is_risk_control_satisfied
    )