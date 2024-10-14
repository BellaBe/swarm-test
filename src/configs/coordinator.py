def get_agent(agent_name):
    """Factory function to return agents by name."""
    if agent_name == "jurisdiction":
        from src.configs.agents.jurisdiction_agent import jurisdiction_agent
        return jurisdiction_agent
    elif agent_name == "contract_type":
        from src.configs.agents.contract_type_agent import contract_type_agent
        return contract_type_agent
    elif agent_name == "legal_context":
        from src.configs.agents.legal_context_agent import legal_context_agent
        return legal_context_agent
    elif agent_name == "document_structure":
        from src.configs.agents.document_structure_agent import document_structure_agent
        return document_structure_agent
    elif agent_name == "clauses":
        from src.configs.agents.clauses_agent import clauses_agent
        return clauses_agent
    elif agent_name == "compliance":
        from src.configs.agents.compliance_agent import compliance_agent
        return compliance_agent
    elif agent_name == "quality_assurance":
        from src.configs.agents.quality_assurance_agent import quality_assurance_agent
        return quality_assurance_agent
    else:
        raise ValueError(f"Unknown agent: {agent_name}")
