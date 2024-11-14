from src.configs.coordinator import get_agent
from src.swarm.types import Agent

def compliance_instructions(context_variables):
    structured_document_response = context_variables.get("DocumentStructureAgent_response", "")
    return f"""
    You are the ComplianceAgent.
    Verify that the structured contract complies with the legal and regulatory requirements for the jurisdiction and contract type.
    Check for any potential legal issues or compliance risks in the document: "{structured_document_response}".
    After ensuring compliance, transfer to the QualityAssuranceAgent.
    """

def transfer_to_quality_assurance():
    return get_agent("QualityAssuranceAgent")

compliance_agent = Agent(
    name="ComplianceAgent",
    instructions=compliance_instructions,
    functions=[transfer_to_quality_assurance],
)
