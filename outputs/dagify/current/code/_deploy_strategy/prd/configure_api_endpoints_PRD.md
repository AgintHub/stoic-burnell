# configure_api_endpoints PRD

## Description
Configure API endpoints for the deployment by creating a list of API endpoints based on the provided order workflow description and environment.


## Conceptual Info

This shim is responsible for creating a list of API endpoints based on the provided order workflow description and environment.

## Docstring

### Summary
Configure API endpoints for the deployment.

### Parameters

- **environment** (str): The environment for which the API endpoints are being configured (e.g., production, testing).
- **order_workflow** (str): The order workflow description to use when configuring the API endpoints.

### Returns

LIST_STR: A list of API endpoints used in the deployment.

### Raises

- ValueError: When the input environment or order workflow is invalid.
- TypeError: When the input environment or order workflow is not a string.

### Examples

```python
>>> configure_api_endpoints(environment='production', order_workflow='example_workflow')
>>> ['/api/endpoint1', '/api/endpoint2']
['/api/endpoint1', '/api/endpoint2']
```
