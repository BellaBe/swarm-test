from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def legal_context_instructions(context_variables):
    contract_type = context_variables.get("contract_type", None)
    jurisdiction = context_variables.get("jurisdiction", None)
    return f"""
    You are the Legal Context Agent.
    Ensure that the legal context and regulations related to contract type: {contract_type} and jurisdiction: {jurisdiction} are applied.
    Transfer to DocumentStructureAgent after legal context is handled.
    """
    
def transfer_to_document_structure():
    return get_agent("document_structure")

legal_context_agent = Agent(
    name="Legal Context Agent",
    instructions=legal_context_instructions,
    functions=[transfer_to_document_structure],
)