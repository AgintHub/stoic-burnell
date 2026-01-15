import re


def validate_report_quality(report: str) -> bool:
    """
    Validates the quality of a given report.

    Parameters
    ----------
    report : str
        The report to be validated.

    Returns
    -------
    bool
        True if the report quality is valid, False otherwise.

    Raises
    ------
    ValueError
        When the input report is empty or None.
    TypeError
        When the input report is not a string.

    Examples
    --------
    >>> validate_report_quality(report='This is a high-quality report.')
    True

    >>> validate_report_quality(report='This is a low-quality report.')
    False

    """
    if report is None:
        raise ValueError("When the input report is empty or None.")
    if not isinstance(report, str):
        raise TypeError("When the input report is not a string.")
    if len(report.strip()) == 0:
        raise ValueError("When the input report is empty or None.")
    
    
    if len(report.strip()) < 50:
        return False
    
    has_sentences = len(re.findall(r'[.!?]+', report)) >= 3
    has_proper_words = len(re.findall(r'\b[A-Za-z]{3,}\b', report)) >= 10
    
    word_count = len(report.split())
    if word_count < 20:
        return False
    
    low_quality_patterns = [
        r'\blow[- ]quality\b',
        r'\bbad\b',
        r'\bpoor\b',
        r'\bterrible\b'
    ]
    
    for pattern in low_quality_patterns:
        if re.search(pattern, report, re.IGNORECASE):
            return False
    
    return has_sentences and has_proper_words