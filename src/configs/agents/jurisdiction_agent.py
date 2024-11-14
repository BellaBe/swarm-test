from src.configs.coordinator import get_agent
from src.swarm.types import Agent

def jurisdiction_instructions(context_variables):
    jurisdiction = context_variables.get("jurisdiction", None)
    contract_type = context_variables.get("contract_type", None)
    return f"""
    You are the JurisdictionAgent.
    Your task is to identify jurisdiction-specific legal requirements for the jurisdiction: {jurisdiction} and contract type: {contract_type}.
    Highlight any mandatory clauses, legal language, or important considerations that should be included in the contract.
    After providing this information, transfer to the LegalContextAgent.
    """

def transfer_to_legal_context():
    return get_agent("LegalContextAgent")

jurisdiction_agent = Agent(
    name="JurisdictionAgent",
    instructions=jurisdiction_instructions,
    functions=[transfer_to_legal_context],
)
