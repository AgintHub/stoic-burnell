from pydantic import BaseModel, Field
from typing import List


class DesignOrderManagementOutput(BaseModel):
    """Pydantic model for design_order_management node outputs."""
    order_workflow_description: str = (
        Field(..., description="Description of the order management workflow")
    )
    order_status_options: List[str] = (
        Field(..., description="List of possible order status options")
    )
    data_structures_used: List[str] = (
        Field(..., description="List of data structures used to store order information")
    )
    modification_rules: List[str] = (
        Field(..., description="List of rules for modifying existing orders")
    )
    cancellation_procedures: str = (
        Field(..., description="Description of the procedures for cancelling orders")
    )
    is_order_management_automated: bool = (
        Field(..., description="Whether the order management process is automated")
    )


class DesignRiskControlsOutput(BaseModel):
    """Pydantic model for design_risk_controls node outputs."""
    position_limits: List[float] = (
        Field(..., description="List of position limits for each asset")
    )
    var_constraints: List[float] = (
        Field(..., description="List of Value-at-Risk (VaR) constraints for each asset")
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
        Field(..., description="List of alert channels (e.g., email, SMS, webhook)")
    )
    key_metrics: List[str] = (
        Field(..., description="List of key metrics to be monitored (e.g., PnL, risk limits, system health)")
    )
    threshold_values: List[float] = (
        Field(..., description="List of threshold values for each key metric")
    )


class SetUpDataStorageOutput(BaseModel):
    """Pydantic model for set_up_data_storage node outputs."""
    database_type: str = (
        Field(..., description="Type of the database (e.g., relational, NoSQL, time-series)")
    )
    schema_outline: str = (
        Field(..., description="Detailed outline of the database schema")
    )
    partition_strategy: str = (
        Field(..., description="Strategy used for partitioning data (e.g., by date, by type)")
    )
    retention_policy: str = (
        Field(..., description="Policy for data retention (e.g., time-based, size-based)")
    )
    data_storage_size: int = (
        Field(..., description="Estimated size of the data storage needed")
    )
    is_cloud_based: bool = (
        Field(..., description="Whether the data storage solution is cloud-based")
    )


class SetUpCodeRepositoryOutput(BaseModel):
    """Pydantic model for set_up_code_repository node outputs."""
    repository_layout: str = (
        Field(..., description="Description of the repository layout")
    )
    folder_names: List[str] = (
        Field(..., description="List of folder names in the repository")
    )
    file_templates: List[str] = (
        Field(..., description="List of file templates in the repository")
    )


class GenerateReportsOutput(BaseModel):
    """Pydantic model for generate_reports node outputs."""
    report_markdown: str = (
        Field(..., description="The comprehensive report in Markdown format")
    )
    performance_metrics: List[str] = (
        Field(..., description="List of performance metrics (e.g., cumulative return, Sharpe ratio, max drawdown)")
    )
    risk_assessment: str = (
        Field(..., description="Summary of risk assessment (e.g., volatility, tail risk, position concentration)")
    )
    monitoring_alerts: List[str] = (
        Field(..., description="List of monitoring alerts and their configurations")
    )


class DeployStrategyOutput(BaseModel):
    """Pydantic model for deploy_strategy node outputs."""
    deployment_status: bool = (
        Field(..., description="Whether the deployment was successful")
    )
    deployment_steps: List[str] = (
        Field(..., description="List of steps taken during deployment")
    )
    containerization_details: str = (
        Field(..., description="Details of the containerization process")
    )
    ci_cd_pipeline_config: str = (
        Field(..., description="Configuration of the CI/CD pipeline")
    )
    api_endpoints: List[str] = (
        Field(..., description="List of API endpoints used in the deployment")
    )
    monitoring_hooks: List[str] = (
        Field(..., description="List of monitoring hooks used in the deployment")
    )
    deployment_checklist: List[str] = (
        Field(..., description="List of items in the deployment checklist")
    )


def deploy_strategy(design_order_management_input: DesignOrderManagementOutput, design_risk_controls_input: DesignRiskControlsOutput, design_monitoring_and_alerts_input: DesignMonitoringAndAlertsOutput, set_up_data_storage_input: SetUpDataStorageOutput, set_up_code_repository_input: SetUpCodeRepositoryOutput, generate_reports_input: GenerateReportsOutput, **kwargs) -> DeployStrategyOutput:
    """
    Deploys the strategy to production with containerization, automated
    delivery, and validated post-deployment health. Provides a structured
    artifact detailing steps, endpoints, monitoring, and rollback procedures.

    Parameters
    ----------
    deployment_version : str
        Version tag or git SHA of the deployment artifacts
    canary_percentage : float
        Initial proportion of traffic to route to the new release (0.0 -
        1.0)
    environment : str
        Target deployment environment (staging, production)
    rollback_on_failure : bool
        Whether to automatically rollback on failure
    dependencies : List[str]
        List of dependent nodes/services verified before deploy
    observability_config : str
        Configuration of monitoring, logging, and alerting hooks to enable
        post-deploy validation

    Returns
    -------
    str
        Structured success/failure narrative with deployment metadata

    Raises
    ------
    Exception
        Raised if prerequisites are not met or deployment fails

    Examples
    --------
    >>> deploy_strategy.run(deployment_version='v2.1.0', canary_percentage=0.15,
    environment='production', rollback_on_failure=True,
    dependencies=['design_order_management','design_monitoring_and_alerts'],
    observability_config='default')
    Deployment initiated with 15% canary; rollback on failure enabled.
    Observability hooks streaming to Grafana/Prometheus.

    """
    return DeployStrategyOutput(
        deployment_status=False,
        deployment_steps=[],
        containerization_details="",
        ci_cd_pipeline_config="",
        api_endpoints=[],
        monitoring_hooks=[],
        deployment_checklist=[],
    )