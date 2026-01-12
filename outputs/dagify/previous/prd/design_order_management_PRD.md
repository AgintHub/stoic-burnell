# design_order_management PRD

## Description
Plan how orders are tracked and updated.


## Conceptual Info

This node is responsible for designing the order management system, including the workflow for creating, modifying, and cancelling orders, as well as tracking their status.

## Docstring

### Summary
Designs the order management workflow and data structures for storing order information.

### Parameters

- **execution_logic** (dict): Details about the execution logic, including order routing, execution algorithms, and compliance checks.

### Returns

dict: A dictionary containing the order workflow description, order status options, data structures used, modification rules, cancellation procedures, and whether the order management process is automated.

### Raises

- ValueError: If the execution logic is not provided or is incomplete.

### Examples

```python
>>> order_management(design_execution_logic={'execution_algorithms': ['VWAP'], 'order_routing_info': ' routing_protocol'})
{order_workflow_description: The order management workflow includes creating, modifying, and cancelling orders., order_status_options: [pending, executed, cancelled], data_structures_used: [Order class, dictionary], modification_rules: [modify_quantity, modify_price], cancellation_procedures: Cancel an order by setting its status to 'cancelled'., is_order_management_automated: true}
```
