from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def document_structure_instructions(context_variables):
    return f"""
    You are the Legal Document Structure Agent.
    Ensure that the document follows the legal best practices, with proper sectioning, headings, and formatting.
    After ensuring the structure is correct, transfer to ClausesAgent.
    """

def transfer_to_clauses():
    return get_agent("clauses")

document_structure_agent = Agent(
    name="Document Structure Agent",
    instructions=document_structure_instructions,
    functions=[transfer_to_clauses],
)