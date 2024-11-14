from src.configs.coordinator import get_agent
from src.swarm.types import Agent

def clauses_instructions(context_variables):
    legal_context_response = context_variables.get("LegalContextAgent_response", "")
    return f"""
    You are the ClausesAgent.
    Based on the legal context provided: "{legal_context_response}", generate specific clauses for the contract.
    Ensure the clauses align with the legal requirements and cover important aspects such as confidentiality, termination, and governing law.
    After generating the clauses, transfer to the DocumentStructureAgent.
    """

def transfer_to_document_structure():
    return get_agent("DocumentStructureAgent")

clauses_agent = Agent(
    name="ClausesAgent",
    instructions=clauses_instructions,
    functions=[transfer_to_document_structure],
)
