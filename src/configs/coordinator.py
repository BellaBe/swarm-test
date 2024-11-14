def get_agent(agent_name):
    """Factory function to return agents by name."""
    if agent_name == "JurisdictionAgent":
        from src.configs.agents.jurisdiction_agent import jurisdiction_agent
        return jurisdiction_agent
    elif agent_name == "ContractTypeAgent":
        from src.configs.agents.contract_type_agent import contract_type_agent
        return contract_type_agent
    elif agent_name == "LegalContextAgent":
        from src.configs.agents.legal_context_agent import legal_context_agent
        return legal_context_agent
    elif agent_name == "DocumentStructureAgent":
        from src.configs.agents.document_structure_agent import document_structure_agent
        return document_structure_agent
    elif agent_name == "ClausesAgent":
        from src.configs.agents.clauses_agent import clauses_agent
        return clauses_agent
    elif agent_name == "ComplianceAgent":
        from src.configs.agents.compliance_agent import compliance_agent
        return compliance_agent
    elif agent_name == "QualityAssuranceAgent":
        from src.configs.agents.quality_assurance_agent import quality_assurance_agent
        return quality_assurance_agent
    else:
        raise ValueError(f"Unknown agent: {agent_name}")
