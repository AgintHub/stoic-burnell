def calculate_feasibility_score(recommendations: str, inflation_severity: str) -> float:
    """
    Calculates the feasibility score of a policy proposal based on the provided
    recommendations and inflation severity.

    Parameters
    ----------
    recommendations : str
        A string containing the policy recommendations.
    inflation_severity : str
        A string describing the current inflation severity level.

    Returns
    -------
    float
        The calculated feasibility score, ranging from 0 (completely
        infeasible) to 1 (fully feasible).

    Raises
    ------
    ValueError
        If the input recommendations or inflation severity are invalid or
        cannot be processed.
    TypeError
        If the input types do not match the expected string for
        recommendations and inflation severity.

    Examples
    --------
    >>> calculate_feasibility_score(recommendations="Increase funding for
    education", inflation_severity="Moderate")
    0.8

    >>> calculate_feasibility_score(recommendations="Implement strict budget
    cuts", inflation_severity="Severe")
    0.4

    """
    
    if not isinstance(recommendations, str):
        raise TypeError("Input recommendations must be a string")
    if not isinstance(inflation_severity, str):
        raise TypeError("Input inflation_severity must be a string")
    
    if not recommendations.strip():
        raise ValueError("Recommendations cannot be empty")
    if not inflation_severity.strip():
        raise ValueError("Inflation severity cannot be empty")
    
    recommendations_lower = recommendations.lower()
    inflation_lower = inflation_severity.lower()
    
    inflation_impact = 0.0
    if "low" in inflation_lower or "mild" in inflation_lower:
        inflation_impact = 0.9
    elif "moderate" in inflation_lower or "medium" in inflation_lower:
        inflation_impact = 0.7
    elif "high" in inflation_lower or "severe" in inflation_lower:
        inflation_impact = 0.3
    elif "critical" in inflation_lower or "extreme" in inflation_lower:
        inflation_impact = 0.1
    else:
        raise ValueError("Invalid inflation severity level")
    
    policy_feasibility = 0.5
    
    positive_indicators = ["increase funding", "invest", "support", "enhance", "improve", "expand"]
    negative_indicators = ["cut", "reduce", "eliminate", "strict", "austerity", "slash"]
    
    positive_count = sum(1 for indicator in positive_indicators if indicator in recommendations_lower)
    negative_count = sum(1 for indicator in negative_indicators if indicator in recommendations_lower)
    
    if positive_count > negative_count:
        policy_feasibility = 0.8
    elif negative_count > positive_count:
        policy_feasibility = 0.4
    
    feasibility_score = (policy_feasibility + inflation_impact) / 2.0
    feasibility_score = max(0.0, min(1.0, feasibility_score))
    
    return feasibility_score