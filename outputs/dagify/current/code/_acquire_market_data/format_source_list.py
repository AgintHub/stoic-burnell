def format_source_list(sources: str) -> str:
    """
    Format a list of data sources into a comma-separated string.  Parameters:
    ``sources`` (list): A list of data sources to be formatted.  Returns:
    ``str``: The formatted string of data sources.  Raises: ``ValueError``: If
    the input list is empty. ``TypeError``: If the input is not a list.
    Examples: >>> format_source_list(['source1', 'source2', 'source3'])
    'source1, source2, source3' >>> format_source_list([])  ValueError: Input
    list is empty

    Parameters
    ----------
    sources : List[str]
        A list of data sources to be formatted

    Returns
    -------
    STR
        The formatted string of data sources

    Raises
    ------
    ValueError
        If the input list is empty
    TypeError
        If the input is not a list

    Examples
    --------
    >>> format_source_list(['source1', 'source2', 'source3'])
    'source1, source2, source3'

    >>> format_source_list([])
    ValueError: Input list is empty

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")