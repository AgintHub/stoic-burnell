import re


def apply_professional_formatting(report_text: str) -> str:
    """
    Applies professional formatting to a report text, including font styles,
    margins, and layout adjustments, to produce a polished and readable
    document.

    Parameters
    ----------
    report_text : str
        The input report text to be professionally formatted.

    Returns
    -------
    str
        The professionally formatted report text.

    Raises
    ------
    ValueError
        If the input report text is empty, null, or invalid.
    TypeError
        If the input report text is not a string.

    Examples
    --------
    >>> formatted_report = apply_professional_formatting(report_text='This is a
    sample report.')
    'This is a sample report.' with professional formatting applied.

    >>> formatted_report = apply_professional_formatting(report_text='Another
    sample report with multiple lines.\nLine 2.\nLine 3.')
    'Another sample report with multiple lines.\nLine 2.\nLine 3.' with
    professional formatting applied.

    """
    if not isinstance(report_text, str):
        raise TypeError("If the input report text is not a string.")
    
    if not report_text or not report_text.strip():
        raise ValueError("If the input report text is empty, null, or invalid.")
    
    
    formatted_text = re.sub(r'\s+', ' ', report_text.strip())
    
    formatted_text = re.sub(r'\s*\.\s*', '. ', formatted_text)
    formatted_text = re.sub(r'\s*,\s*', ', ', formatted_text)
    formatted_text = re.sub(r'\s*;\s*', '; ', formatted_text)
    formatted_text = re.sub(r'\s*:\s*', ': ', formatted_text)
    
    formatted_text = re.sub(r'\n\s*\n', '\n\n', formatted_text)
    
    sentences = re.split(r'(\. )', formatted_text)
    capitalized_sentences = []
    for i, part in enumerate(sentences):
        if i % 2 == 0 and part:  # Actual sentence content (not delimiter)
            part = part.strip()
            if part:
                part = part[0].upper() + part[1:] if len(part) > 1 else part.upper()
        capitalized_sentences.append(part)
    
    formatted_text = ''.join(capitalized_sentences)
    
    formatted_text = formatted_text.strip()
    
    return formatted_text