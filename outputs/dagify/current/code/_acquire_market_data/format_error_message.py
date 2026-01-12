def format_error_message(source: str, error: str) -> str:
    """
    Formats an error message based on the provided source and error information.

    Parameters
    ----------
    source : str
        The source information related to the error.
    error : str
        The error information to be formatted.

    Returns
    -------
    str
        The formatted error message of type str.

    Raises
    ------
    TypeError
        When source or error is not of type str.

    Examples
    --------
    >>> format_error_message(source='example_source', error='error_occurred')
    'An error occurred while processing example_source.'

    >>> format_error_message(source='another_source', error='another_error')
    'An error occurred while processing another_source.'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")