from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def compliance_instructions(context_variables):
    jurisdiction = context_variables.get("jurisdiction", None)
    return f"""
    You are the Compliance Agent.
    Ensure the contract complies with the jurisdiction: {jurisdiction}.
    Once compliance is confirmed, transfer to QualityAssuranceAgent.
    """
    
def transfer_to_quality_assurance():
    return get_agent("quality_assurance")

compliance_agent = Agent(
    name="Compliance Agent",
    instructions=compliance_instructions,
    functions=[transfer_to_quality_assurance],
)