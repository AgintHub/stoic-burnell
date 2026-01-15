def validate_policy_proposal_input(policy_summary: str, recommendations: str) -> str:
    """
    Validate the policy proposal input by checking the policy summary and
    recommendations for compliance with the required format and content
    standards.

    Parameters
    ----------
    policy_summary : str
        The executive summary of the policy proposal.
    recommendations : str
        The structured list of policy recommendations.

    Returns
    -------
    str
        A string indicating whether the policy proposal input is valid or
        not, potentially including error messages for invalid inputs.

    Raises
    ------
    ValueError
        Raised when the policy summary or recommendations do not meet the
        required standards, such as being empty or not in the correct
        format.
    TypeError
        Raised when the input parameters are not of the expected type, for
        instance, if policy_summary or recommendations are not strings.

    Examples
    --------
    >>> validate_policy_proposal_input(policy_summary='Example policy to reduce
    inflation.', recommendations='Increase interest rates.')
    >>> print(output)
    'Input is valid.'

    >>> validate_policy_proposal_input(policy_summary='',
    recommendations='Increase interest rates.')
    ValueError: Policy summary cannot be empty.

    """
    if not isinstance(policy_summary, str):
        raise TypeError("Policy summary must be a string")
    
    if not isinstance(recommendations, str):
        raise TypeError("Recommendations must be a string")
    
    if not policy_summary or policy_summary.strip() == "":
        raise ValueError("Policy summary cannot be empty.")
    
    if not recommendations or recommendations.strip() == "":
        raise ValueError("Recommendations cannot be empty.")
    
    return "Input is valid."