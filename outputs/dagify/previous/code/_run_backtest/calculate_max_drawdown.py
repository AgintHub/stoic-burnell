def calculate_max_drawdown(metrics: str) -> float:
    """
    Computes the maximum drawdown value from the provided performance metrics
    data, given as a string, and returns it as a float.

    Parameters
    ----------
    metrics : str
        A string containing serialized or processed performance metrics data
        from which the maximum drawdown is extracted.

    Returns
    -------
    float
        A float representing the maximum drawdown value, indicating the
        largest peak-to-trough decline observed.

    Raises
    ------
    ValueError
        Raised if the input metrics data is invalid or cannot be parsed to
        extract the maximum drawdown.
    TypeError
        Raised if the input is not of type str.

    Examples
    --------
    >>> calculate_max_drawdown('{"max_drawdown": 0.25}')
    0.25

    >>> calculate_max_drawdown('metrics data with max drawdown of 0.15')
    0.15

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")