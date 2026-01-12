# store_data_in_database PRD

## Description
Stores market data in the database for later retrieval.


## Conceptual Info

store_data_in_database is a shim that stores market data in the database for later retrieval. The shim connects to the database using the provided connection string, authenticates the source, fetches market data, and stores it in the database.

## Docstring

### Summary
store_data_in_database connects to the database, authenticates the source, fetches market data, and stores it in the database.

### Parameters

- **db_connection** (str): A connection string used to connect to the database.
- **data** (str): Market data to be stored in the database.
- **source** (str): Source of the market data.

### Returns

str: A success or failure message after storing data in the database. The message will be of type 'str'.

### Raises

- ValueError: When database connection or authentication fails.
- TypeError: When input types are incorrect (e.g., invalid database connection string).
- Exception: When unexpected errors occur during database operations.

### Examples

```python
>>> db_connection = 'postgresql://username:password@localhost/database'
>>> data = {'key': 'value'}
>>> source = 'market_data_src'
>>> store_data_in_database(db_connection=db_connection, data=data, source=source)
'Data stored successfully in database.'
```

```python
>>> db_connection = 'invalid_connection'
>>> data = {'key': 'value'}
>>> source = 'market_data_src'
>>> store_data_in_database(db_connection=db_connection, data=data, source=source)
'Unable to connect to database.'
```
