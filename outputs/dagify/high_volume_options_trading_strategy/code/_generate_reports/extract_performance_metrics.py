from typing import List


def extract_performance_metrics(performance_input: str) -> List[str]:
    """
    Extracts and returns a list of key performance metrics from the input object
    containing backtest performance data.

    Parameters
    ----------
    performance_input : str
        String identifier or description referencing the evaluation backtest
        performance input object.

    Returns
    -------
    str
        A list of strings representing the names of performance metrics
        extracted from the input.

    Raises
    ------
    TypeError
        Raised if 'performance_input' is not a string.
    ValueError
        Raised if 'performance_input' does not contain expected data or
        keys.

    Examples
    --------
    >>> metrics =
    extract_performance_metrics(evaluate_backtest_performance_input)
    >>> print(metrics)
    ['meets_performance_goals', 'cumulative_return', 'sharpe_ratio',
    'max_drawdown', 'win_rate', 'strengths', 'weaknesses']

    >>> metrics = extract_performance_metrics('performance_data')
    >>> print(metrics)
    ['meets_performance_goals', 'cumulative_return', 'sharpe_ratio',
    'max_drawdown', 'win_rate', 'strengths', 'weaknesses']

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")