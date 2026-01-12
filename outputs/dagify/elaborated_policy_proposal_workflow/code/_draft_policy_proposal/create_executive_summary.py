def create_executive_summary(inflation_context: str, policy_strategy: str) -> str:
    """
    Creates an executive summary based on the inflation context and policy
    strategy.

    Parameters
    ----------
    inflation_context : str
        A description of the current inflation context.
    policy_strategy : str
        The overarching strategy for addressing the inflation context.

    Returns
    -------
    str
        The generated executive summary.

    Raises
    ------
    ValueError
        When either the inflation context or policy strategy is empty or
        missing.
    TypeError
        When the inflation context or policy strategy is not a string.

    Examples
    --------
    >>> create_executive_summary(inflation_context='The current inflation rate
    is 5%, significantly higher than the 2% target.', policy_strategy='Monetary
    policy tightening')
    >>> create_executive_summary(inflation_context='The inflation rate has been
    steadily decreasing over the past year.', policy_strategy='Fiscal policy
    stimulus')
    'The current inflation rate of 5% necessitates a tightening of monetary
    policy to curb inflationary pressures.'

    """
    if not isinstance(inflation_context, str):
        raise TypeError("When the inflation context or policy strategy is not a string.")
    if not isinstance(policy_strategy, str):
        raise TypeError("When the inflation context or policy strategy is not a string.")
    
    if not inflation_context or not inflation_context.strip():
        raise ValueError("When either the inflation context or policy strategy is empty or missing.")
    if not policy_strategy or not policy_strategy.strip():
        raise ValueError("When either the inflation context or policy strategy is empty or missing.")
    
    
    inflation_context_clean = inflation_context.strip()
    policy_strategy_clean = policy_strategy.strip().lower()
    
    if 'tightening' in policy_strategy_clean or 'monetary' in policy_strategy_clean:
        if any(keyword in inflation_context_clean.lower() for keyword in ['high', 'above', 'target', '%']):
            return f"The current inflation situation necessitates a tightening of monetary policy to curb inflationary pressures."
        else:
            return f"Given the inflation context, monetary policy tightening is recommended to maintain price stability."
    elif 'stimulus' in policy_strategy_clean or 'fiscal' in policy_strategy_clean:
        return f"Based on current inflation trends, fiscal policy stimulus measures are being considered to support economic growth."
    else:
        return f"The current inflation environment requires careful policy consideration to balance economic growth and price stability."