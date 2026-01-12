def create_monitoring_summary(dashboard_design: str, alert_rules: str, alert_channels: str, key_metrics: str, threshold_values: str) -> str:
    """
    Generates a monitoring summary with a comprehensive string output containing
    input parameters and user-configured settings.

    Parameters
    ----------
    dashboard_design : str
        The monitoring dashboard design to use.
    alert_rules : str
        The alert rules to apply for monitoring.
    alert_channels : str
        The alert channels to send notifications to.
    key_metrics : str
        The key metrics to focus on for monitoring.
    threshold_values : str
        The threshold values to use for monitoring alerts.

    Returns
    -------
    str
        A string representing the generated monitoring summary.

    Raises
    ------
    ValueError
        Raised if the input parameters do not match the expected formats or
        are invalid.

    Examples
    --------
    >>> monitoring_summary =
    create_monitoring_summary(dashboard_design='design1',
    ...   alert_rules=['rule1', 'rule2'],
    ...   alert_channels=['channel1', 'channel2'],
    ...   key_metrics=['metric1', 'metric2'],
    ...   threshold_values=[100, 200])
    Monitoring Summary:
    design1
    rule1, rule2
    channel1, channel2
    metric1, metric2
    100, 200

    """
    raise NotImplementedError("This is a virtual stub node that needs to be implemented")