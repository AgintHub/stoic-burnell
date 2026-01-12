def extract_cumulative_return(metrics: str) -> float:
    """
    Extracts the 'cumulative_return' float value from a metrics dictionary
    containing backtest performance results.

    Parameters
    ----------
    metrics : str
        A string identifier for the metrics, typically a JSON-formatted
        string or a key to locate the metrics dictionary containing
        performance data.

    Returns
    -------
    float
        The total cumulative return metric as a floating-point number.

    Raises
    ------
    ValueError
        Raised if the metrics input does not contain the 'cumulative_return'
        key or if the data is malformed.
    TypeError
        Raised if the input 'metrics' is not a string or a compatible data
        structure.

    Examples
    --------
    >>> performance_metrics = {'cumulative_return': 0.15, 'sharpe_ratio': 1.2,
    'max_drawdown': 0.05, 'win_rate': 0.6}
    >>> output = extract_cumulative_return(metrics=performance_metrics)
    0.15

    >>> performance_metrics = '{"cumulative_return": 0.25, "sharpe_ratio": 1.3}'
    >>> output = extract_cumulative_return(metrics=performance_metrics)
    0.25

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")