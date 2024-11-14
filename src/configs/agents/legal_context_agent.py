from src.configs.coordinator import get_agent
from src.swarm.types import Agent

def legal_context_instructions(context_variables):
    jurisdiction_response = context_variables.get("JurisdictionAgent_response", "")
    contract_type = context_variables.get("contract_type", None)
    return f"""
    You are the LegalContextAgent.
    Use the information provided by the JurisdictionAgent: "{jurisdiction_response}" to add legal context specific to the contract type: {contract_type}.
    Customize the contract to address any unique legal requirements or conditions that apply to this type of agreement.
    Once completed, transfer to the ClausesAgent.
    """

def transfer_to_clauses():
    return get_agent("ClausesAgent")

legal_context_agent = Agent(
    name="LegalContextAgent",
    instructions=legal_context_instructions,
    functions=[transfer_to_clauses],
)
