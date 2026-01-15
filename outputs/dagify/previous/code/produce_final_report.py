from ._produce_final_report.validate_input_data import validate_input_data
from ._produce_final_report.generate_executive_summary import generate_executive_summary
from ._produce_final_report.extract_and_format_recommendations import extract_and_format_recommendations
from ._produce_final_report.format_feasibility_analysis import format_feasibility_analysis
from ._produce_final_report.generate_conclusion import generate_conclusion
from ._produce_final_report.compile_report_sections import compile_report_sections
from ._produce_final_report.apply_professional_formatting import apply_professional_formatting
from ._produce_final_report.validate_report_quality import validate_report_quality

from pydantic import BaseModel, Field


class ElaboratePolicyProposalOutput(BaseModel):
    """Pydantic model for elaborate_policy_proposal node outputs."""
    elaborated_policy_proposal: str = (
        Field(..., description="Elaborated policy proposal with detailed justifications and explanations.")
    )
    elaborated_feasibility_score: float = (
        Field(..., description="Updated feasibility score reflecting the elaborated policy proposal.")
    )


class ProduceFinalReportOutput(BaseModel):
    """Pydantic model for produce_final_report node outputs."""
    final_report_text: str = (
        Field(..., description="Complete, human-readable report text that compiles the policy proposal summary, recommendations, feasibility score, and a brief conclusion into a single narrative document.")
    )
    is_report_successful: bool = (
        Field(..., description="Boolean flag indicating whether the final report generation succeeded given the inputs.")
    )


def produce_final_report(elaborate_policy_proposal_input: ElaboratePolicyProposalOutput, **kwargs) -> ProduceFinalReportOutput:
    """
    Produces a polished final report text from an elaborated policy proposal.

    Parameters
    ----------
    elaborated_policy_proposal : str
        The elaborated policy proposal with detailed justifications and
        explanations.
    elaborated_feasibility_score : float
        The updated feasibility score reflecting the elaborated policy
        proposal.

    Returns
    -------
    tuple[str, bool]
        A tuple containing the final report text and a boolean indicating
        whether the report generation was successful.

    Raises
    ------
    ValueError
        If the elaborated policy proposal or feasibility score is invalid or
        missing.

    Examples
    --------
    >>> produce_final_report(elaborated_policy_proposal='This is an example
    proposal.', elaborated_feasibility_score=0.8)
    ('This is a comprehensive final report text based on the example proposal.,
    including its feasibility score of 0.8.', True)

    """
    is_valid: bool = validate_input_data(proposal=elaborate_policy_proposal_input.elaborated_policy_proposal, score=elaborate_policy_proposal_input.elaborated_feasibility_score)
    
    if not is_valid:
        raise ValueError("If the elaborated policy proposal or feasibility score is invalid or missing.")
    
    executive_summary: str = generate_executive_summary(proposal=elaborate_policy_proposal_input.elaborated_policy_proposal)
    recommendations_section: str = extract_and_format_recommendations(proposal=elaborate_policy_proposal_input.elaborated_policy_proposal)
    feasibility_analysis: str = format_feasibility_analysis(score=elaborate_policy_proposal_input.elaborated_feasibility_score, proposal=elaborate_policy_proposal_input.elaborated_policy_proposal)
    conclusion_text: str = generate_conclusion(proposal=elaborate_policy_proposal_input.elaborated_policy_proposal, feasibility_score=elaborate_policy_proposal_input.elaborated_feasibility_score)
    
    final_report: str = compile_report_sections(executive_summary=executive_summary, recommendations=recommendations_section, feasibility_analysis=feasibility_analysis, conclusion=conclusion_text)
    
    polished_report: str = apply_professional_formatting(report_text=final_report)
    
    report_quality_check: bool = validate_report_quality(report=polished_report)
    
    return ProduceFinalReportOutput(
        final_report_text=polished_report,
        is_report_successful=report_quality_check
    )