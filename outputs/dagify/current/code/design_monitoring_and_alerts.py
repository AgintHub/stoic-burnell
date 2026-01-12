from ._design_monitoring_and_alerts.identify_key_metrics import identify_key_metrics
from ._design_monitoring_and_alerts.merge_risk_and_custom_thresholds import merge_risk_and_custom_thresholds
from ._design_monitoring_and_alerts.generate_alert_rules import generate_alert_rules
from ._design_monitoring_and_alerts.validate_and_configure_alert_channels import validate_and_configure_alert_channels
from ._design_monitoring_and_alerts.design_monitoring_dashboard import design_monitoring_dashboard
from ._design_monitoring_and_alerts.deploy_monitoring_platform import deploy_monitoring_platform

from pydantic import BaseModel, Field
from typing import List


class DesignRiskControlsOutput(BaseModel):
    """Pydantic model for design_risk_controls node outputs."""
    position_limits: List[float] = (
        Field(..., description="List of position limits for each asset")
    )
    var_constraints: List[float] = (
        Field(..., description = (
            "List of Value-at-Risk (VaR) constraints for each asset")
        )
    )
    stop_loss_thresholds: List[float] = (
        Field(..., description="List of stop-loss thresholds for each asset")
    )
    risk_control_rules: List[str] = (
        Field(..., description="List of risk control rules")
    )
    is_risk_control_satisfied: bool = (
        Field(..., description="Whether the risk control rules are satisfied")
    )


class DesignMonitoringAndAlertsOutput(BaseModel):
    """Pydantic model for design_monitoring_and_alerts node outputs."""
    monitoring_dashboard_design: str = (
        Field(..., description="Description of the monitoring dashboard design")
    )
    alert_rules: List[str] = (
        Field(..., description="List of alert rules for key metrics")
    )
    alert_channels: List[str] = (
        Field(..., description = (
            "List of alert channels (e.g., email, SMS, webhook)")
        )
    )
    key_metrics: List[str] = (
        Field(..., description = (
            "List of key metrics to be monitored (e.g., PnL, risk limits, system health)")
        )
    )
    threshold_values: List[float] = (
        Field(..., description="List of threshold values for each key metric")
    )


def design_monitoring_and_alerts(design_risk_controls_input: DesignRiskControlsOutput, **kwargs) -> DesignMonitoringAndAlertsOutput:
    """
    Design and deploy a scalable monitoring platform to track crucial
    performance indicators and ensure prompt issue detection.

    Parameters
    ----------
    threshold_values : List[float]
        Threshold values for each key metric.
    alert_channels : List[str]
        Alert channels to use.

    Returns
    -------
    Dict[str, object]
        The output of the monitoring and alerting system.

    Raises
    ------
    Exception
        Raises an exception if there's an error setting up the monitoring
        system.

    Examples
    --------
    >>> Create a monitoring system using design_monitoring_and_alerts.
    The monitoring system has been successfully created and is ready for use.

    """
    threshold_values: List[float] = kwargs.get('threshold_values', [])
    alert_channels: List[str] = kwargs.get('alert_channels', [])
    
    key_metrics: List[str] = identify_key_metrics(risk_controls=design_risk_controls_input)
    
    merged_thresholds: List[float] = merge_risk_and_custom_thresholds(
        risk_limits=design_risk_controls_input.position_limits,
        var_constraints=design_risk_controls_input.var_constraints,
        stop_loss_thresholds=design_risk_controls_input.stop_loss_thresholds,
        custom_thresholds=threshold_values
    )
    
    alert_rules: List[str] = generate_alert_rules(
        metrics=key_metrics,
        thresholds=merged_thresholds,
        risk_rules=design_risk_controls_input.risk_control_rules
    )
    
    validated_channels: List[str] = validate_and_configure_alert_channels(channels=alert_channels)
    
    dashboard_design: str = design_monitoring_dashboard(
        metrics=key_metrics,
        thresholds=merged_thresholds,
        alert_rules=alert_rules
    )
    
    deploy_monitoring_platform(
        dashboard=dashboard_design,
        alert_rules=alert_rules,
        channels=validated_channels
    )
    
    return DesignMonitoringAndAlertsOutput(
        monitoring_dashboard_design=dashboard_design,
        alert_rules=alert_rules,
        alert_channels=validated_channels,
        key_metrics=key_metrics,
        threshold_values=merged_thresholds
    )