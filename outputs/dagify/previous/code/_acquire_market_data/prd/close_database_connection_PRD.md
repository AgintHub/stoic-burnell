# close_database_connection PRD

## Description
This shim function handles closing an active database connection identified by the provided connection string.


## Conceptual Info

Provides the functionality to safely close an existing database connection using its connection identifier.

## Docstring

### Summary
Closes the specified database connection safely and returns a status message.

### Parameters

- **connection** (str): A string representing the database connection identifier to be closed.

### Returns

str: A string message indicating success, failure, or status of the connection closure.

### Raises

- ValueError: Raised if the connection parameter is empty or invalid.
- TypeError: Raised if the input parameter is not of type str.

### Examples

```python
>>> result = close_database_connection('db_conn_123')
'Database connection db_conn_123 closed successfully.'
```

```python
>>> result = close_database_connection('invalid_conn')
'Error: invalid connection identifier.'
```
