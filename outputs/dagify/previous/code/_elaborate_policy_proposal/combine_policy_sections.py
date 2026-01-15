def combine_policy_sections(summary: str, recommendations: str, rationales: str, implementation: str) -> str:
    """
    Combines policy sections into a comprehensive policy proposal.

    Parameters
    ----------
    summary : str
        The policy proposal summary.
    recommendations : str
        The policy recommendations.
    rationales : str
        The policy rationales.
    implementation : str
        The policy implementation details.

    Returns
    -------
    str
        The combined policy proposal.

    Raises
    ------
    ValueError
        When any of the input parameters are empty or missing.
    TypeError
        When the input parameters are of incorrect type.

    Examples
    --------
    >>> combine_policy_sections(summary='Policy summary',
    recommendations='Policy recommendations', rationales='Policy rationales',
    implementation='Policy implementation details')
    'Combined policy proposal'

    """
    if not isinstance(summary, str):
        raise TypeError("Summary must be of type str")
    if not isinstance(recommendations, str):
        raise TypeError("Recommendations must be of type str")
    if not isinstance(rationales, str):
        raise TypeError("Rationales must be of type str")
    if not isinstance(implementation, str):
        raise TypeError("Implementation must be of type str")
    
    if not summary or not summary.strip():
        raise ValueError("Summary cannot be empty or missing")
    if not recommendations or not recommendations.strip():
        raise ValueError("Recommendations cannot be empty or missing")
    if not rationales or not rationales.strip():
        raise ValueError("Rationales cannot be empty or missing")
    if not implementation or not implementation.strip():
        raise ValueError("Implementation cannot be empty or missing")
    
    combined_policy = f"""POLICY PROPOSAL

SUMMARY:
{summary.strip()}

RECOMMENDATIONS:
{recommendations.strip()}

RATIONALES:
{rationales.strip()}

IMPLEMENTATION:
{implementation.strip()}"""
    
    return combined_policy