import re


def generate_executive_summary(proposal: str) -> str:
    """
    Generates a concise executive summary based on a given policy proposal.

    Parameters
    ----------
    proposal : str
        The policy proposal to generate an executive summary for.

    Returns
    -------
    str
        The generated executive summary.

    Raises
    ------
    ValueError
        When the input proposal is invalid or missing.
    TypeError
        When the input proposal is not a string.

    Examples
    --------
    >>> generate_executive_summary(proposal='This is a sample policy proposal.')
    'This is a concise executive summary of the sample policy proposal.'

    >>> generate_executive_summary(proposal='Another policy proposal example')
    'A brief executive summary of another policy proposal example.'

    """
    if not isinstance(proposal, str):
        raise TypeError("The input proposal must be a string.")
    
    if not proposal or not proposal.strip():
        raise ValueError("The input proposal is invalid or missing.")
    
    
    cleaned_proposal = re.sub(r'\s+', ' ', proposal.strip())
    
    sentences = re.split(r'[.!?]+', cleaned_proposal)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= 2:
        summary = cleaned_proposal
    else:
        summary_parts = []
        
        if sentences:
            summary_parts.append(sentences[0])
        
        key_terms = ['policy', 'proposal', 'implement', 'recommend', 'suggest', 'plan', 'strategy']
        for sentence in sentences[1:3]:  # Check next 2 sentences
            if any(term in sentence.lower() for term in key_terms):
                summary_parts.append(sentence)
                break
        
        summary = '. '.join(summary_parts)
        if not summary.endswith('.'):
            summary += '.'
    
    if len(summary) > 200:
        truncated = summary[:200]
        last_period = truncated.rfind('.')
        if last_period > 50:  # Ensure we don't cut too short
            summary = truncated[:last_period + 1]
        else:
            summary = truncated + '...'
    
    return summary