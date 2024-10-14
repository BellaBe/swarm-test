from src.configs.coordinator import get_agent
from src.swarm.types import Agent




def jurisdiction_instructions(context_variables):
    jurisdiction = context_variables.get("jurisdiction", None)
    return f"""
    You are the Jurisdiction Agent.
    Ensure that the contract adheres to the legal framework for the jurisdiction: {jurisdiction}.
    If the jurisdiction is valid, transfer to ContractTypeAgent.
    """
  
def transfer_to_contract_type():
    return get_agent("contract_type")  

jurisdiction_agent = Agent(
    name="Jurisdiction Agent",
    instructions=jurisdiction_instructions,
    functions=[transfer_to_contract_type],
)