# reassess_feasibility_score PRD

## Description
Reassesses the feasibility score of a policy proposal based on its elaborated proposal.


## Conceptual Info

The reassess_feasibility_score shim function is used to reassess the feasibility score of a policy proposal after it has been elaborated.

## Docstring

### Summary
Reassesses the feasibility score of a policy proposal based on its elaborated proposal.

### Parameters

- **original_score** (str): The original feasibility score of the policy proposal
- **elaborated_proposal** (str): The elaborated policy proposal

### Returns

float: The reassessed feasibility score

### Raises

- ValueError: When the original score is not a valid float
- TypeError: When the input types are incorrect

### Examples

```python
>>> reassess_feasibility_score(original_score='0.5', elaborated_proposal='This is an elaborated proposal')
0.6
```

```python
>>> reassess_feasibility_score(original_score='0.8', elaborated_proposal='This is another elaborated proposal')
0.7
```
