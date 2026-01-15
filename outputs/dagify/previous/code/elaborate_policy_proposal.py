from ._elaborate_policy_proposal.validate_policy_proposal_input import validate_policy_proposal_input
from ._elaborate_policy_proposal.elaborate_policy_summary import elaborate_policy_summary
from ._elaborate_policy_proposal.add_justifications_to_recommendations import add_justifications_to_recommendations
from ._elaborate_policy_proposal.generate_policy_rationales import generate_policy_rationales
from ._elaborate_policy_proposal.generate_implementation_details import generate_implementation_details
from ._elaborate_policy_proposal.combine_policy_sections import combine_policy_sections
from ._elaborate_policy_proposal.reassess_feasibility_score import reassess_feasibility_score

from pydantic import BaseModel, Field


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


class ElaboratePolicyProposalOutput(BaseModel):
    """Pydantic model for elaborate_policy_proposal node outputs."""
    elaborated_policy_proposal: str = (
        Field(..., description="Elaborated policy proposal with detailed justifications and explanations.")
    )
    elaborated_feasibility_score: float = (
        Field(..., description="Updated feasibility score reflecting the elaborated policy proposal.")
    )


def elaborate_policy_proposal(draft_policy_proposal_input: DraftPolicyProposalOutput, **kwargs) -> ElaboratePolicyProposalOutput:
    """
    Elaborates on a drafted policy proposal by providing more details and
    justifications.

    Parameters
    ----------
    policy_proposal_summary : str
        Executive summary of the policy proposal.
    policy_recommendations : str
        Structured list of concrete, actionable policy recommendations.
    policy_feasibility_score : float
        Scalar in [0, 1] indicating overall political, fiscal, and
        administrative feasibility of the proposed package.

    Returns
    -------
    tuple[str, float]
        A tuple containing the elaborated policy proposal and the updated
        feasibility score.

    Raises
    ------
    ValueError
        If the input policy proposal is empty or incomplete.

    Examples
    --------
    >>> elaborate_policy_proposal(policy_proposal_summary='This is a policy
    proposal summary.',
    ...                           policy_recommendations='These are policy
    recommendations.',
    ...                           policy_feasibility_score=0.8)
    ('This is an elaborated policy proposal with detailed justifications and
    explanations.', 0.9)

    """
    validate_policy_proposal_input(policy_summary=draft_policy_proposal_input.policy_proposal_summary, recommendations=draft_policy_proposal_input.policy_recommendations)
    
    elaborated_summary: str = elaborate_policy_summary(summary=draft_policy_proposal_input.policy_proposal_summary)
    
    detailed_recommendations: str = add_justifications_to_recommendations(recommendations=draft_policy_proposal_input.policy_recommendations)
    
    rationales: str = generate_policy_rationales(summary=elaborated_summary, recommendations=detailed_recommendations)
    
    implementation_details: str = generate_implementation_details(recommendations=detailed_recommendations)
    
    complete_elaborated_proposal: str = combine_policy_sections(summary=elaborated_summary, recommendations=detailed_recommendations, rationales=rationales, implementation=implementation_details)
    
    updated_feasibility: float = reassess_feasibility_score(original_score=draft_policy_proposal_input.policy_feasibility_score, elaborated_proposal=complete_elaborated_proposal)
    
    return ElaboratePolicyProposalOutput(
        elaborated_policy_proposal=complete_elaborated_proposal,
        elaborated_feasibility_score=updated_feasibility
    )