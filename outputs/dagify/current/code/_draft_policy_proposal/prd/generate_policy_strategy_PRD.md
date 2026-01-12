# generate_policy_strategy PRD

## Description
Generates a policy strategy based on the provided inflation context.


## Conceptual Info

The generate_policy_strategy shim is responsible for creating a policy strategy based on the inflation context, which is then used in the draft_policy_proposal function.

## Docstring

### Summary
Generates a policy strategy based on the provided inflation context.

### Parameters

- **inflation_context** (str): The input inflation context used to generate the policy strategy.

### Returns

str: The generated policy strategy as a string.

### Raises

- ValueError: When the input inflation context is invalid or empty.
- TypeError: When the input inflation context is not a string.

### Examples

```python
>>> policy_strategy = generate_policy_strategy(inflation_context='high_inflation')
>>> print(policy_strategy)
'Policy strategy for high inflation: increase interest rates'
```

```python
>>> policy_strategy = generate_policy_strategy(inflation_context='low_inflation')
>>> print(policy_strategy)
'Policy strategy for low inflation: decrease interest rates'
```
