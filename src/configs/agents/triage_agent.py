from coordinator import (
    transfer_to_jurisdiction_agent,
    transfer_to_contract_type,
    transfer_to_legal_context,
    transfer_to_document_structure,
    transfer_to_clauses,
    transfer_to_compliance,
    transfer_to_quality_assurance,
)
from src.swarm.types import Agent

def triage_instructions(context_variables):
    return f"""
    You are the Triage Agent.
    Based on the contract type and jurisdiction, determine which agent should handle the request next.
    Transfer to the appropriate agent once the context is clear.
    """

triage_agent = Agent(
    name="Triage Agent",
    instructions=triage_instructions,
    functions=[
        transfer_to_jurisdiction_agent,
        transfer_to_contract_type,
        transfer_to_legal_context,
        transfer_to_document_structure,
        transfer_to_clauses,
        transfer_to_compliance,
        transfer_to_quality_assurance,
    ],
)
