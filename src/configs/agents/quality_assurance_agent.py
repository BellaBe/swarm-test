from src.swarm.types import Agent

def quality_assurance_instructions(context_variables):
    compliance_response = context_variables.get("ComplianceAgent_response", "")
    return f"""
    You are the QualityAssuranceAgent.
    Perform a final review of the contract to ensure consistency, clarity, completeness, and legal soundness.
    Below is the compliance-checked contract: "{compliance_response}".
    Once the review is completed, finalize the contract and return the full text of the final contract to the user.
    """

def finalize_and_return_contract():
    return "Contract drafting complete. Here is the final contract."

quality_assurance_agent = Agent(
    name="QualityAssuranceAgent",
    instructions=quality_assurance_instructions,
    functions=[finalize_and_return_contract],
)


