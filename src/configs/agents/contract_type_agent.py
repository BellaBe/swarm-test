
from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def contract_type_instructions(context_variables):
    contract_type = context_variables.get("contract_type", None)
    jurisdiction_legal_details = context_variables.get("JurisdictionAgent_response", None)
    
    return f"""
    You are the Contract Type Agent.
    Use the legal details provided: {jurisdiction_legal_details} and select the appropriate template for the contract type: {contract_type}.
    After selecting the template, you will transfer the task to the LegalContextAgent.
    """

def transfer_to_legal_context(context_variables):
    return get_agent("legal_context")

contract_type_agent = Agent(
    name="ContractTypeAgent",
    instructions=contract_type_instructions,
    functions=[transfer_to_legal_context],
)


