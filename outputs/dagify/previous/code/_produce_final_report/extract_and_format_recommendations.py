import re


def extract_and_format_recommendations(proposal: str) -> str:
    """
    Extracts and formats policy recommendations from a given proposal.

    Parameters
    ----------
    proposal : str
        The policy proposal from which to extract and format
        recommendations.

    Returns
    -------
    str
        Formatted policy recommendations.

    Raises
    ------
    ValueError
        When the input proposal is invalid or missing.
    TypeError
        When the input proposal is not a string.

    Examples
    --------
    >>> extract_and_format_recommendations(proposal='This is a sample policy
    proposal.')
    'This is a formatted recommendation based on the proposal.'

    >>> extract_and_format_recommendations(proposal='Another sample policy
    proposal')
    'Another formatted recommendation.'

    """
    
    if not isinstance(proposal, str):
        raise TypeError("The input proposal is not a string.")
    
    if not proposal or not proposal.strip():
        raise ValueError("When the input proposal is invalid or missing.")
    
    proposal_text = proposal.strip()
    
    recommendation_patterns = [
        r'(?:recommend|suggest|propose)(?:s|ed)?\s+(?:that\s+)?([^.!?]+)',
        r'(?:should|must|ought to|need to)\s+([^.!?]+)',
        r'(?:it is|we are)\s+(?:recommended|suggested)\s+(?:that\s+)?([^.!?]+)',
        r'(?:policy|recommendation|suggestion):\s*([^.!?]+)'
    ]
    
    recommendations = []
    
    for pattern in recommendation_patterns:
        matches = re.finditer(pattern, proposal_text, re.IGNORECASE)
        for match in matches:
            rec = match.group(1).strip()
            if rec and len(rec) > 3:
                recommendations.append(rec)
    
    if not recommendations:
        sentences = re.split(r'[.!?]+', proposal_text)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 20:
                recommendations.append(sentence)
    
    if not recommendations:
        return f"Formatted recommendation: {proposal_text}"
    
    formatted_recommendations = []
    for i, rec in enumerate(recommendations[:5], 1):
        rec = rec.strip().capitalize()
        if not rec.endswith(('.', '!', '?')):
            rec += '.'
        formatted_recommendations.append(f"{i}. {rec}")
    
    return "Policy Recommendations:\n" + "\n".join(formatted_recommendations)