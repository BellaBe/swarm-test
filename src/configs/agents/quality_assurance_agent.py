from src.configs.coordinator import get_agent
from src.swarm.types import Agent


def quality_assurance_instructions(context_variables):
    return f"""
    You are the Quality Assurance Agent.
    Perform the final review of the contract for consistency, clarity, completeness, and legal soundness.
    Once all checks are complete, resolve the case.
    """
    
def case_resolved():
    return "Contract drafting complete. Case resolved."

quality_assurance_agent = Agent(
    name="Quality Assurance Agent",
    instructions=quality_assurance_instructions,
    functions=[case_resolved],
)

