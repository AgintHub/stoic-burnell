# create_workflow_description PRD

## Description
Generates a textual description of a trading workflow based on specified stages and routing info, serving as a preparatory step in order management system.


## Conceptual Info

This shim constructs a human-readable description of the trading workflow, integrating stages and routing information to facilitate understanding and documentation in the order management process.

## Docstring

### Summary
Creates a textual description of a trading workflow from given stages and routing information, serving as a placeholder for more complex description generation.

### Parameters

- **stages** (str): A string representing the sequence or types of stages involved in the trading workflow.
- **routing_info** (str): A string containing details about order routing protocols and destinations.

### Returns

str: A descriptive string summarizing the trading workflow based on input stages and routing info.

### Raises

- ValueError: Raised if input parameters are invalid or empty strings.
- TypeError: Raised if input parameters are not strings.

### Examples

```python
>>> create_workflow_description('Pre-trade, Execution, Post-trade', 'Direct Routing to Broker')
'Workflow stages: Pre-trade, Execution, Post-trade; Routing: Direct Routing to Broker'
```

```python
>>> create_workflow_description('Order Placement, Confirmation', 'Via Smart Order Router')
'Workflow stages: Order Placement, Confirmation; Routing: Via Smart Order Router'
```
