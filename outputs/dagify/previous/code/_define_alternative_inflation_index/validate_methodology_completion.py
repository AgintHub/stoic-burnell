def validate_methodology_completion(weights: str, index_name: str) -> bool:
    """
    Validates the completion of a methodology based on the provided weights and
    index name.

    Parameters
    ----------
    weights : str
        The weights to be used for validation.
    index_name : str
        The index name to be used for validation.

    Returns
    -------
    bool
        A boolean indicating whether the methodology is complete.

    Raises
    ------
    ValueError
        When the input validation fails.
    TypeError
        When the input types are incorrect.

    Examples
    --------
    >>> validate_methodology_completion(weights='category1=0.5,category2=0.5',
    index_name='example_index')
    True

    >>> validate_methodology_completion(weights='category1=0.3,category2=0.7',
    index_name='another_index')
    True

    """
    if not isinstance(weights, str):
        raise TypeError("weights must be a string")
    if not isinstance(index_name, str):
        raise TypeError("index_name must be a string")
    
    if not weights.strip():
        raise ValueError("weights cannot be empty")
    if not index_name.strip():
        raise ValueError("index_name cannot be empty")
    
    try:
        weight_pairs = weights.split(',')
        total_weight = 0.0
        
        for pair in weight_pairs:
            if '=' not in pair:
                raise ValueError("Invalid weight format: each pair must contain '='")
            
            category, weight_str = pair.split('=', 1)
            if not category.strip():
                raise ValueError("Category name cannot be empty")
            
            try:
                weight_value = float(weight_str.strip())
            except ValueError:
                raise ValueError(f"Invalid weight value: {weight_str}")
            
            if weight_value < 0 or weight_value > 1:
                raise ValueError(f"Weight values must be between 0 and 1: {weight_value}")
            
            total_weight += weight_value
        
        if abs(total_weight - 1.0) > 1e-10:
            return False
        
        return True
        
    except ValueError:
        raise
    except Exception as e:
        raise ValueError(f"Failed to parse weights: {str(e)}")