from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def clauses_instructions(context_variables):
    contract_type = context_variables.get("contract_type", None)
    return f"""
    You are the Clauses Agent.
    Generate clauses for the contract type: {contract_type}.
    Once the clauses are generated, transfer to ComplianceAgent.
    """
    
def transfer_to_compliance():
    return get_agent("compliance")

clauses_agent = Agent(
    name="Clauses Agent",
    instructions=clauses_instructions,
    functions=[transfer_to_compliance],
)