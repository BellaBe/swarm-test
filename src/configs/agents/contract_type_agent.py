
from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def contract_type_instructions(context_variables):
    contract_type = context_variables.get("contract_type", None)
    jurisdiction = context_variables.get("jurisdiction", None)
    return f"""
    You are the Contract Type Agent.
    Select the appropriate template for contract type: {contract_type} in jurisdiction: {jurisdiction}.
    Once the template is selected, transfer to LegalContextAgent.
    """

def transfer_to_legal_context():
    return get_agent("legal_context")

contract_type_agent = Agent(
    name="Contract Type Agent",
    instructions=contract_type_instructions,
    functions=[transfer_to_legal_context],
)
