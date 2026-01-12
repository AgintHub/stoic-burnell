# determine_auto_execution PRD

## Description
This shim determines whether automated execution should be enabled based on the given strategy and compliance checks.


## Conceptual Info

This shim assesses whether automated execution is permissible based on the proposed strategy and compliance evaluations, enabling or disabling auto-trading accordingly.

## Docstring

### Summary
Implement a function that evaluates the provided trading strategy and compliance checks to determine if automatic execution should be activated.

### Parameters

- **strategy** (str): A string representing the selected trading strategy identifier or description.
- **compliance_checks** (str): A string summarizing the compliance checks performed, such as risk and position limit evaluations.

### Returns

bool: Returns True if the strategy passes compliance and conditions for auto-execution, otherwise False.

### Raises

- ValueError: Raised if either input is empty or not a string, indicating invalid input parameters.
- TypeError: Raised if inputs are of incorrect types other than str, or if the logic cannot process given data.

### Examples

```python
>>> determine_auto_execution(strategy='MomentumStrategy', compliance_checks='Risk limits and position checks passed')
True
```

```python
>>> determine_auto_execution(strategy='ArbitrageStrategy', compliance_checks='Position limit exceeded')
False
```
