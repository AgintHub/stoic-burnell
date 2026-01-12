# create_modification_rules PRD

## Description
Generates modification rules for existing orders based on compliance checks and status options.


## Conceptual Info

This shim node generates modification rules for existing orders by processing compliance checks and status options.

## Docstring

### Summary
Generates modification rules for existing orders based on compliance checks and status options.

### Parameters

- **status_options** (str): Input parameter describing possible order status options
- **compliance_checks** (str): Input parameter describing compliance checks performed during order execution

### Returns

PrimitiveType.LIST_STR: Output is a list of modification rules for existing orders, represented as strings

### Raises

- ValueError: Raised when input validation fails (e.g., invalid format or missing required fields)
- TypeError: Raised when input types are incorrect (e.g., non-string input for string parameter)

### Examples

```python
>>> create_modification_rules(status_options='active', compliance_checks='compliance_check1, compliance_check2')
['rule1', 'rule2']
```
