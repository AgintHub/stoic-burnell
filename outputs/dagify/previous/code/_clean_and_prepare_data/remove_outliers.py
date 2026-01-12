def remove_outliers(dataset: str, method: str) -> str:
    """
    Remove outliers from the dataset based on the specified method and return
    the cleaned dataset as a string.

    Parameters
    ----------
    dataset : str
        A serialized string representing the dataset to process.
    method : str
        The outlier removal method to apply, e.g., 'zscore' or 'iqr'.

    Returns
    -------
    str
        A serialized string of the dataset after outlier removal has been
        applied.

    Raises
    ------
    ValueError
        If the specified method is not supported or if dataset format is
        invalid.
    TypeError
        If input types for dataset or method are incorrect.

    Examples
    --------
    >>> remove_outliers('dataset_string', method='zscore')
    'cleaned_dataset_string'

    >>> remove_outliers('another_dataset_string', method='iqr')
    'processed_dataset_string'

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")