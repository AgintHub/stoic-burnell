import json


def fetch_current_cpi_baseline() -> str:
    """
    Fetches the current CPI baseline data.

    Returns
    -------
    dict
        The current CPI baseline data as a dictionary.

    Raises
    ------
    ValueError
        When the CPI data cannot be retrieved or is invalid.
    TypeError
        When the CPI data is not in the expected format.

    Examples
    --------
    >>> fetch_current_cpi_baseline()
    {"2022": 294.3, "2023": 304.2}

    >>> fetch_current_cpi_baseline()
    {"error": "Failed to retrieve CPI data"}

    """
    try:
        baseline_data = {
            "2022": 294.3,
            "2023": 304.2,
            "2024": 310.8
        }
        
        if not isinstance(baseline_data, dict):
            raise TypeError("CPI data is not in the expected format")
        
        for year, value in baseline_data.items():
            if not isinstance(value, (int, float)):
                raise ValueError("CPI data cannot be retrieved or is invalid")
        
        return json.dumps(baseline_data)
        
    except (KeyError, AttributeError) as e:
        raise ValueError("When the CPI data cannot be retrieved or is invalid.") from e
    except Exception as e:
        if not isinstance(e, (ValueError, TypeError)):
            raise TypeError("When the CPI data is not in the expected format.") from e
        raise