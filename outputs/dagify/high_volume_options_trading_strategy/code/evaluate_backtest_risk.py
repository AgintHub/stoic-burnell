from ._evaluate_backtest_risk.calculate_annualized_volatility import calculate_annualized_volatility
from ._evaluate_backtest_risk.calculate_value_at_risk import calculate_value_at_risk
from ._evaluate_backtest_risk.calculate_expected_shortfall import calculate_expected_shortfall
from ._evaluate_backtest_risk.extract_max_drawdown import extract_max_drawdown
from ._evaluate_backtest_risk.calculate_tail_risk_metrics import calculate_tail_risk_metrics
from ._evaluate_backtest_risk.calculate_position_concentration_hhi import calculate_position_concentration_hhi
from ._evaluate_backtest_risk.estimate_liquidity_impact import estimate_liquidity_impact

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


def evaluate_backtest_risk(run_backtest_input: RunBacktestOutput, **kwargs) -> EvaluateBacktestRiskOutput:
    """
    Evaluates the risk metrics of a backtest, including volatility, value-at-
    risk, expected shortfall, maximum drawdown, tail risk, position
    concentration, and liquidity impact.

    Returns
    -------
    dict
        A dictionary containing the calculated risk metrics

    Examples
    --------
    >>> return evaluate_backtest_risk(backtest_result)
    A dictionary with the following structure:
    
    {'volatility': 0.12, 'value_at_risk': 0.05, 'expected_shortfall': 0.03,
    'max_drawdown': 0.25, 'tail_risk': [0.01, 0.05], 'position_concentration':
    0.8, 'liquidity_impact': 0.05}

    """
    volatility: float = calculate_annualized_volatility(backtest_data=run_backtest_input)
    var_95: float = calculate_value_at_risk(backtest_data=run_backtest_input, confidence_level=0.95)
    expected_shortfall: float = calculate_expected_shortfall(backtest_data=run_backtest_input, confidence_level=0.95)
    max_dd: float = extract_max_drawdown(backtest_data=run_backtest_input)
    tail_metrics: List[float] = calculate_tail_risk_metrics(backtest_data=run_backtest_input, quantiles=[0.01, 0.05])
    position_conc: float = calculate_position_concentration_hhi(backtest_data=run_backtest_input)
    liquidity_impact: float = estimate_liquidity_impact(backtest_data=run_backtest_input)
    
    return EvaluateBacktestRiskOutput(
        volatility=volatility,
        value_at_risk=var_95,
        expected_shortfall=expected_shortfall,
        max_drawdown=max_dd,
        tail_risk=tail_metrics,
        position_concentration=position_conc,
        liquidity_impact=liquidity_impact
    )