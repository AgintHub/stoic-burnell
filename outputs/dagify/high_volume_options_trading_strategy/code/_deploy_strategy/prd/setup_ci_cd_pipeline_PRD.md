# setup_ci_cd_pipeline PRD

## Description
Sets up the Continuous Integration and Continuous Deployment pipeline with the provided version, environment, and canary percentage.


## Conceptual Info

This shim node is responsible for setting up the Continuous Integration and Continuous Deployment pipeline with the specified version, environment, and canary percentage.

## Docstring

### Summary
Sets up the CI/CD pipeline with the provided version, environment, and canary percentage.

### Parameters

- **version** (str): The version of the deployment.
- **environment** (str): The environment where the deployment will run.
- **canary_percentage** (str): The percentage of the canary release.

### Returns

str: The output of the CI/CD pipeline setup process.

### Raises

- ValueError: When input validation fails (e.g., invalid version or environment).
- TypeError: When input types are incorrect (e.g., non-string version or environment).

### Examples

```python
>>> setup_ci_cd_pipeline(version='latest', environment='production', canary_percentage='0.2')
Setup CI/CD pipeline with version 'latest', environment 'production', and canary percentage '0.2' completed.
```

```python
>>> setup_ci_cd_pipeline(version='stable', environment='staging', canary_percentage='0.5')
Setup CI/CD pipeline with version 'stable', environment 'staging', and canary percentage '0.5' completed.
```
