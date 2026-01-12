from ._design_execution_logic.validate_strategy_logic import validate_strategy_logic
from ._design_execution_logic.select_execution_algorithms import select_execution_algorithms
from ._design_execution_logic.determine_order_routing import determine_order_routing
from ._design_execution_logic.generate_compliance_checks import generate_compliance_checks
from ._design_execution_logic.determine_auto_execution import determine_auto_execution

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
        Field(..., description = (
            "Method for determining position size (e.g., fixed, risk-based)")
        )
    )
    risk_limits: List[float] = (
        Field(..., description = (
            "List of risk limits (e.g., stop-loss, take-profit levels)")
        )
    )
    decision_tree: str = (
        Field(..., description = (
            "High-level overview of the decision-making process")
        )
    )


class DesignExecutionLogicOutput(BaseModel):
    """Pydantic model for design_execution_logic node outputs."""
    execution_algorithms: List[str] = (
        Field(..., description = (
            "List of execution algorithms used (e.g., VWAP, TWAP, Market)")
        )
    )
    order_routing_info: str = (
        Field(..., description = (
            "Details about order routing, including routing protocols and destinations")
        )
    )
    compliance_checks: List[str] = (
        Field(..., description = (
            "List of compliance checks performed during order execution (e.g., position limits, risk checks)")
        )
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
    validated_strategy: DesignStrategyLogicOutput = validate_strategy_logic(strategy=design_strategy_logic_input)
    
    selected_algorithms: List[str] = select_execution_algorithms(
        entry_signals=validated_strategy.entry_signals,
        exit_rules=validated_strategy.exit_rules,
        position_sizing=validated_strategy.position_sizing
    )
    
    routing_config: str = determine_order_routing(
        algorithms=selected_algorithms,
        risk_limits=validated_strategy.risk_limits
    )
    
    compliance_list: List[str] = generate_compliance_checks(
        strategy=validated_strategy,
        algorithms=selected_algorithms
    )
    
    auto_execution_flag: bool = determine_auto_execution(
        strategy=validated_strategy,
        compliance_checks=compliance_list
    )
    
    return DesignExecutionLogicOutput(
        execution_algorithms=selected_algorithms,
        order_routing_info=routing_config,
        compliance_checks=compliance_list,
        is_auto_execution=auto_execution_flag
    )