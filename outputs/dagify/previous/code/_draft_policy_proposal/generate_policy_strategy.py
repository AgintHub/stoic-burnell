def generate_policy_strategy(inflation_context: str) -> str:
    """
    Generates a policy strategy based on the provided inflation context.

    Parameters
    ----------
    inflation_context : str
        The input inflation context used to generate the policy strategy.

    Returns
    -------
    str
        The generated policy strategy as a string.

    Raises
    ------
    ValueError
        When the input inflation context is invalid or empty.
    TypeError
        When the input inflation context is not a string.

    Examples
    --------
    >>> policy_strategy =
    generate_policy_strategy(inflation_context='high_inflation')
    >>> print(policy_strategy)
    'Policy strategy for high inflation: increase interest rates'

    >>> policy_strategy =
    generate_policy_strategy(inflation_context='low_inflation')
    >>> print(policy_strategy)
    'Policy strategy for low inflation: decrease interest rates'

    """
    if not isinstance(inflation_context, str):
        raise TypeError("When the input inflation context is not a string.")
    
    if not inflation_context or inflation_context.strip() == "":
        raise ValueError("When the input inflation context is invalid or empty.")
    
    inflation_context_clean = inflation_context.strip().lower()
    
    if inflation_context_clean == "high_inflation":
        return "Policy strategy for high inflation: increase interest rates"
    elif inflation_context_clean == "low_inflation":
        return "Policy strategy for low inflation: decrease interest rates"
    elif inflation_context_clean == "moderate_inflation":
        return "Policy strategy for moderate inflation: maintain current interest rates"
    elif inflation_context_clean == "deflation":
        return "Policy strategy for deflation: implement quantitative easing"
    else:
        return f"Policy strategy for {inflation_context}: implement adaptive monetary policy"