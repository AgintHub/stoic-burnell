def validate_input_data(proposal: str, score: str) -> bool:
    """
    Validates the input policy proposal and feasibility score.

    Parameters
    ----------
    proposal : str
        The policy proposal string to be validated.
    score : str
        The feasibility score string to be validated.

    Returns
    -------
    bool
        True if the input data is valid, False otherwise.

    Raises
    ------
    ValueError
        If the input policy proposal or feasibility score is invalid or
        missing.
    TypeError
        If the input types are incorrect.

    Examples
    --------
    >>> validate_input_data(proposal='example policy proposal', score='0.8')
    True

    >>> validate_input_data(proposal='', score='')
    False

    """
    if not isinstance(proposal, str):
        raise TypeError("Proposal must be a string")
    if not isinstance(score, str):
        raise TypeError("Score must be a string")
    
    if not proposal or not proposal.strip():
        raise ValueError("Policy proposal is invalid or missing")
    
    if not score or not score.strip():
        raise ValueError("Feasibility score is invalid or missing")
    
    try:
        score_float = float(score)
        if score_float < 0.0 or score_float > 1.0:
            raise ValueError("Feasibility score must be between 0.0 and 1.0")
    except ValueError as e:
        if "could not convert" in str(e) or "invalid literal" in str(e):
            raise ValueError("Feasibility score is invalid or missing") from e
        raise
    
    return True