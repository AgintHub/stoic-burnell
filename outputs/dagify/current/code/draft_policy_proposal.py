from ._draft_policy_proposal.validate_input_parameters import validate_input_parameters
from ._draft_policy_proposal.analyze_inflation_context import analyze_inflation_context
from ._draft_policy_proposal.generate_policy_strategy import generate_policy_strategy
from ._draft_policy_proposal.create_executive_summary import create_executive_summary
from ._draft_policy_proposal.generate_actionable_recommendations import generate_actionable_recommendations
from ._draft_policy_proposal.calculate_feasibility_score import calculate_feasibility_score

from pydantic import BaseModel, Field
from typing import List


class AnalyzeTrendsAndBenchmarkOutput(BaseModel):
    """Pydantic model for analyze_trends_and_benchmark node outputs."""
    inflation_rate_years: List[int] = (
        Field(..., description="Years corresponding to calculated inflation rates.")
    )
    inflation_rate_values: List[float] = (
        Field(..., description="Inflation rates as percent changes for each calculated year.")
    )
    trend_summary: str = (
        Field(..., description="Narrative summary of inflation trends and benchmarking results.")
    )
    is_analysis_successful: bool = (
        Field(..., description="Flag indicating whether inflation trend analysis and benchmarking were completed successfully.")
    )


class DraftPolicyProposalOutput(BaseModel):
    """Pydantic model for draft_policy_proposal node outputs."""
    policy_proposal_summary: str = (
        Field(..., description="Executive summary of the policy proposal, explaining the inflation context and overarching policy strategy.")
    )
    policy_recommendations: str = (
        Field(..., description="Structured list of concrete, actionable policy recommendations derived from the inflation trends.")
    )
    policy_feasibility_score: float = (
        Field(..., description="Scalar in [0, 1] indicating overall political, fiscal, and administrative feasibility of the proposed package.")
    )
    is_policy_successful: bool = (
        Field(..., description="Flag indicating whether the policy proposal is grounded in a successful and coherent analysis of inflation trends.")
    )


def draft_policy_proposal(analyze_trends_and_benchmark_input: AnalyzeTrendsAndBenchmarkOutput, **kwargs) -> DraftPolicyProposalOutput:
    """
    Drafts an evidence-based policy proposal from inflation rate series and
    trend benchmark analysis.

    Parameters
    ----------
    inflation_rate_years : List[int]
        Years corresponding to calculated inflation rates.
    inflation_rate_values : List[float]
        Inflation rates as percent changes for each calculated year.
    trend_summary : str
        Narrative summary of inflation trends and benchmarking results.
    is_analysis_successful : bool
        Flag indicating whether inflation trend analysis and benchmarking
        were completed successfully.

    Returns
    -------
    dict
        A dictionary containing the policy proposal summary,
        recommendations, feasibility score, and success flag.

    Raises
    ------
    ValueError
        If input parameters are invalid or missing.

    Examples
    --------
    >>> draft_policy_proposal(
    ...     inflation_rate_years=[2020, 2021, 2022],
    ...     inflation_rate_values=[2.5, 3.1, 2.8],
    ...     trend_summary='Inflation is rising.',
    ...     is_analysis_successful=True
    >>> )
    {'policy_proposal_summary': ' Proposal to address rising inflation.',
    'policy_recommendations': 'Increase interest rates.',
    'policy_feasibility_score': 0.8, 'is_policy_successful': True}

    """
    validated_inputs: bool = validate_input_parameters(
        years=analyze_trends_and_benchmark_input.inflation_rate_years,
        values=analyze_trends_and_benchmark_input.inflation_rate_values,
        summary=analyze_trends_and_benchmark_input.trend_summary,
        analysis_success=analyze_trends_and_benchmark_input.is_analysis_successful
    )
    
    if not validated_inputs or not analyze_trends_and_benchmark_input.is_analysis_successful:
        return DraftPolicyProposalOutput(
            policy_proposal_summary="",
            policy_recommendations="",
            policy_feasibility_score=0.0,
            is_policy_successful=False
        )
    
    inflation_context: str = analyze_inflation_context(
        years=analyze_trends_and_benchmark_input.inflation_rate_years,
        values=analyze_trends_and_benchmark_input.inflation_rate_values,
        trend_summary=analyze_trends_and_benchmark_input.trend_summary
    )
    
    policy_strategy: str = generate_policy_strategy(inflation_context=inflation_context)
    
    executive_summary: str = create_executive_summary(
        inflation_context=inflation_context,
        policy_strategy=policy_strategy
    )
    
    actionable_recommendations: str = generate_actionable_recommendations(
        inflation_data=analyze_trends_and_benchmark_input.inflation_rate_values,
        trend_analysis=analyze_trends_and_benchmark_input.trend_summary
    )
    
    feasibility_score: float = calculate_feasibility_score(
        recommendations=actionable_recommendations,
        inflation_severity=inflation_context
    )
    
    return DraftPolicyProposalOutput(
        policy_proposal_summary=executive_summary,
        policy_recommendations=actionable_recommendations,
        policy_feasibility_score=feasibility_score,
        is_policy_successful=True
    )