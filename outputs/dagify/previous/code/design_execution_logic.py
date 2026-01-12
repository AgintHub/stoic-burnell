from pydantic import BaseModel, Field
from typing import List


class DesignStrategyLogicOutput(BaseModel):
    """Pydantic model for design_strategy_logic node outputs."""
    entry_signals: List[str] = (
        Field(..., description="List of conditions for entering a trade")
    )
    exit_rules: List[str] = (
        Field(..., description="List of conditions for exiting a trade")
    )
    position_sizing: str = (
        Field(..., description="Method for determining position size (e.g., fixed, risk-based)")
    )
    risk_limits: List[float] = (
        Field(..., description="List of risk limits (e.g., stop-loss, take-profit levels)")
    )
    decision_tree: str = (
        Field(..., description="High-level overview of the decision-making process")
    )


class DesignExecutionLogicOutput(BaseModel):
    """Pydantic model for design_execution_logic node outputs."""
    execution_algorithms: List[str] = (
        Field(..., description="List of execution algorithms used (e.g., VWAP, TWAP, Market)")
    )
    order_routing_info: str = (
        Field(..., description="Details about order routing, including routing protocols and destinations")
    )
    compliance_checks: List[str] = (
        Field(..., description="List of compliance checks performed during order execution (e.g., position limits, risk checks)")
    )
    is_auto_execution: bool = (
        Field(..., description="Whether the execution is automated")
    )


def design_execution_logic(design_strategy_logic_input: DesignStrategyLogicOutput, **kwargs) -> DesignExecutionLogicOutput:
    """
    Defines the execution logic for trading orders.

    Parameters
    ----------
    strategy_logic : dict
        The strategy logic defined in the parent node, including entry
        signals, exit rules, position sizing, and risk limits.

    Returns
    -------
    dict
        A dictionary containing the execution algorithms, order routing
        information, compliance checks, and auto-execution flag.

    Raises
    ------
    ValueError
        If the strategy logic is incomplete or invalid.

    Examples
    --------
    >>> design_execution_logic(strategy_logic={'entry_signals': ['signal1',
    'signal2'], 'exit_rules': ['rule1', 'rule2']})
    {'execution_algorithms': ['VWAP', 'TWAP'], 'order_routing_info':
    'routing_protocol: dest1', 'compliance_checks': ['position_limits',
    'risk_checks'], 'is_auto_execution': True}

    """
    return DesignExecutionLogicOutput(
        execution_algorithms=[],
        order_routing_info="",
        compliance_checks=[],
        is_auto_execution=False,
    )