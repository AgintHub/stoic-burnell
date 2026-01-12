from ._design_order_management.analyze_execution_algorithms import analyze_execution_algorithms
from ._design_order_management.create_workflow_description import create_workflow_description
from ._design_order_management.define_order_status_options import define_order_status_options
from ._design_order_management.determine_data_structures import determine_data_structures
from ._design_order_management.create_modification_rules import create_modification_rules
from ._design_order_management.design_cancellation_procedures import design_cancellation_procedures
from ._design_order_management.determine_automation_feasibility import determine_automation_feasibility

from pydantic import BaseModel, Field
from typing import List


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


class DesignOrderManagementOutput(BaseModel):
    """Pydantic model for design_order_management node outputs."""
    order_workflow_description: str = (
        Field(..., description="Description of the order management workflow")
    )
    order_status_options: List[str] = (
        Field(..., description="List of possible order status options")
    )
    data_structures_used: List[str] = (
        Field(..., description = (
            "List of data structures used to store order information")
        )
    )
    modification_rules: List[str] = (
        Field(..., description="List of rules for modifying existing orders")
    )
    cancellation_procedures: str = (
        Field(..., description = (
            "Description of the procedures for cancelling orders")
        )
    )
    is_order_management_automated: bool = (
        Field(..., description = (
            "Whether the order management process is automated")
        )
    )


def design_order_management(design_execution_logic_input: DesignExecutionLogicOutput, **kwargs) -> DesignOrderManagementOutput:
    """
    Designs a comprehensive order management workflow, including creation,
    modification, cancellation, and status tracking, and determines if the order
    management process can be automated.

    Returns
    -------
    PrimitiveType.DICT
        A dictionary containing the order workflow description, order status
        options, data structures used, modification rules, cancellation
        procedures, and automation status.
    """
    workflow_stages: List[str] = analyze_execution_algorithms(algorithms=design_execution_logic_input.execution_algorithms)
    workflow_description: str = create_workflow_description(stages=workflow_stages, routing_info=design_execution_logic_input.order_routing_info)
    
    status_options: List[str] = define_order_status_options(execution_algorithms=design_execution_logic_input.execution_algorithms)
    
    data_structures: List[str] = determine_data_structures(workflow_stages=workflow_stages, compliance_checks=design_execution_logic_input.compliance_checks)
    
    modification_rules: List[str] = create_modification_rules(status_options=status_options, compliance_checks=design_execution_logic_input.compliance_checks)
    
    cancellation_procedures: str = design_cancellation_procedures(workflow_stages=workflow_stages, routing_info=design_execution_logic_input.order_routing_info)
    
    automation_status: bool = determine_automation_feasibility(is_auto_execution=design_execution_logic_input.is_auto_execution, compliance_checks=design_execution_logic_input.compliance_checks)
    
    return DesignOrderManagementOutput(
        order_workflow_description=workflow_description,
        order_status_options=status_options,
        data_structures_used=data_structures,
        modification_rules=modification_rules,
        cancellation_procedures=cancellation_procedures,
        is_order_management_automated=automation_status
    )