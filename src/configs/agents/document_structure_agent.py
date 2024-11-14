from src.configs.coordinator import get_agent
from src.swarm.types import Agent

def document_structure_instructions(context_variables):
    clauses_response = context_variables.get("ClausesAgent_response", "")
    return f"""
    You are the DocumentStructureAgent.
    Ensure that the contract is structured properly, incorporating the following clauses: "{clauses_response}".
    Pay attention to headings, sections, and the overall organization of the document.
    Once structured, transfer to the ComplianceAgent.
    """

def transfer_to_compliance():
    return get_agent("ComplianceAgent")

document_structure_agent = Agent(
    name="DocumentStructureAgent",
    instructions=document_structure_instructions,
    functions=[transfer_to_compliance],
)
