"""
Deep Graph MCP Tool Integration
Provides code analysis capabilities for multi-agent workflows
"""

import asyncio
import json
import logging
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum

class WorkflowPhase(Enum):
    DISCOVERY = "discovery"
    VERIFICATION = "verification"
    ANALYSIS = "analysis"

@dataclass
class DeepGraphConfig:
    """Configuration for Deep Graph MCP"""
    repository: Optional[str] = None
    api_key: Optional[str] = None
    org_id: Optional[str] = None
    graph_id: Optional[str] = None
    is_public: bool = True

@dataclass
class WorkflowStep:
    """Represents a single workflow step"""
    tool: str
    action: str
    params: Dict[str, Any]
    purpose: str
    priority: int
    phase: WorkflowPhase

class DeepGraphMCPTool:
    """Deep Graph MCP Tool Integration for Multi-Agent Workflows"""
    
    def __init__(self, config: DeepGraphConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
    async def execute_discovery_workflow(self, repository: str) -> Dict[str, Any]:
        """Execute repository discovery workflow"""
        
        discovery_steps = [
            WorkflowStep(
                tool="deep_graph_mcp",
                action="folder-tree-structure", 
                params={"repository": repository},
                purpose="map_repository_structure",
                priority=1,
                phase=WorkflowPhase.DISCOVERY
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="docs-semantic-search",
                params={
                    "repository": repository,
                    "query": "setup installation configuration deployment architecture"
                },
                purpose="find_setup_documentation", 
                priority=2,
                phase=WorkflowPhase.DISCOVERY
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "main entry point application startup initialization"
                },
                purpose="identify_entry_points",
                priority=3,
                phase=WorkflowPhase.DISCOVERY
            ),
            WorkflowStep(
                tool="deep_graph_mcp", 
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "api endpoints routes controllers handlers"
                },
                purpose="map_api_surface",
                priority=4,
                phase=WorkflowPhase.DISCOVERY
            )
        ]
        
        results = {}
        for step in sorted(discovery_steps, key=lambda x: x.priority):
            self.logger.info(f"Executing {step.purpose}: {step.action}")
            result = await self._execute_step(step)
            results[step.purpose] = result
            
        return self._analyze_discovery_results(results)
    
    async def execute_verification_workflow(self, repository: str, target_component: str) -> Dict[str, Any]:
        """Execute component verification workflow"""
        
        verification_steps = [
            WorkflowStep(
                tool="deep_graph_mcp",
                action="get-code",
                params={
                    "repository": repository,
                    "name": target_component
                },
                purpose="examine_implementation",
                priority=1,
                phase=WorkflowPhase.VERIFICATION
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="find-direct-connections", 
                params={
                    "repository": repository,
                    "name": target_component
                },
                purpose="map_dependencies",
                priority=2,
                phase=WorkflowPhase.VERIFICATION
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="get-usage-dependency-links",
                params={
                    "repository": repository,
                    "name": target_component
                },
                purpose="analyze_impact_radius",
                priority=3,
                phase=WorkflowPhase.VERIFICATION
            )
        ]
        
        results = {}
        for step in sorted(verification_steps, key=lambda x: x.priority):
            self.logger.info(f"Executing {step.purpose}: {step.action}")
            result = await self._execute_step(step)
            results[step.purpose] = result
            
        return self._analyze_verification_results(results)
    
    async def execute_security_audit_workflow(self, repository: str) -> Dict[str, Any]:
        """Execute security audit workflow"""
        
        security_steps = [
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "authentication authorization security validation"
                },
                purpose="identify_security_components",
                priority=1,
                phase=WorkflowPhase.ANALYSIS
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository, 
                    "query": "input validation sanitization sql injection xss"
                },
                purpose="find_validation_logic",
                priority=2,
                phase=WorkflowPhase.ANALYSIS
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "password encryption hashing token jwt"
                },
                purpose="analyze_crypto_usage",
                priority=3,
                phase=WorkflowPhase.ANALYSIS
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="docs-semantic-search",
                params={
                    "repository": repository,
                    "query": "security best practices vulnerability disclosure"
                },
                purpose="review_security_docs",
                priority=4,
                phase=WorkflowPhase.ANALYSIS
            )
        ]
        
        results = {}
        for step in sorted(security_steps, key=lambda x: x.priority):
            self.logger.info(f"Executing {step.purpose}: {step.action}")
            result = await self._execute_step(step)
            results[step.purpose] = result
            
        return self._analyze_security_results(results)
    
    async def execute_technical_debt_workflow(self, repository: str) -> Dict[str, Any]:
        """Execute technical debt analysis workflow"""
        
        debt_steps = [
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "todo fixme hack workaround temporary"
                },
                purpose="find_technical_debt_markers",
                priority=1, 
                phase=WorkflowPhase.ANALYSIS
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "deprecated legacy obsolete old version"
                },
                purpose="identify_deprecated_code",
                priority=2,
                phase=WorkflowPhase.ANALYSIS
            ),
            WorkflowStep(
                tool="deep_graph_mcp",
                action="nodes-semantic-search",
                params={
                    "repository": repository,
                    "query": "duplicate repeated similar copy paste"
                },
                purpose="detect_code_duplication",
                priority=3,
                phase=WorkflowPhase.ANALYSIS
            )
        ]
        
        results = {}
        for step in sorted(debt_steps, key=lambda x: x.priority):
            self.logger.info(f"Executing {step.purpose}: {step.action}")
            result = await self._execute_step(step)
            results[step.purpose] = result
            
        return self._analyze_technical_debt_results(results)
    
    async def _execute_step(self, step: WorkflowStep) -> Dict[str, Any]:
        """Execute a single workflow step"""
        # This would integrate with the actual MCP tool calls
        # For now, returning a placeholder structure
        return {
            "step": step.action,
            "purpose": step.purpose,
            "phase": step.phase.value,
            "status": "completed",
            "data": f"Mock result for {step.action} with params {step.params}"
        }
    
    def _analyze_discovery_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze discovery phase results"""
        return {
            "phase": "discovery",
            "summary": "Repository structure and entry points mapped",
            "insights": [
                "Identified main application entry points",
                "Located configuration and setup documentation", 
                "Mapped API surface and key components"
            ],
            "next_steps": [
                "Deep dive into critical components",
                "Analyze security implementation",
                "Review technical debt"
            ],
            "raw_results": results
        }
    
    def _analyze_verification_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze verification phase results"""
        return {
            "phase": "verification",
            "summary": "Component implementation and dependencies analyzed",
            "insights": [
                "Examined component implementation details",
                "Mapped direct and indirect dependencies",
                "Assessed change impact radius"
            ],
            "recommendations": [
                "Review identified dependencies before changes",
                "Consider impact on downstream components",
                "Implement appropriate testing strategy"
            ],
            "raw_results": results
        }
    
    def _analyze_security_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze security audit results"""
        return {
            "phase": "security_analysis",
            "summary": "Security components and practices analyzed",
            "findings": [
                "Authentication/authorization patterns identified",
                "Input validation mechanisms reviewed",
                "Cryptographic usage patterns analyzed"
            ],
            "recommendations": [
                "Review authentication implementation",
                "Validate input sanitization coverage",
                "Ensure secure cryptographic practices"
            ],
            "raw_results": results
        }
    
    def _analyze_technical_debt_results(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze technical debt results"""
        return {
            "phase": "technical_debt_analysis",
            "summary": "Technical debt patterns and markers identified",
            "debt_categories": [
                "Code quality issues (TODO/FIXME markers)",
                "Deprecated functionality",
                "Code duplication patterns"
            ],
            "prioritization": [
                "Address security-related technical debt first",
                "Refactor duplicated critical business logic", 
                "Update deprecated dependencies"
            ],
            "raw_results": results
        }

# Example usage and configuration
class MultiAgentWorkflowOrchestrator:
    """Orchestrates multi-agent workflows with Deep Graph MCP integration"""
    
    def __init__(self):
        self.deep_graph_tool = None
        self.workflow_history = []
        
    def configure_for_public_repository(self, repository: str):
        """Configure for public repository analysis"""
        config = DeepGraphConfig(
            repository=repository,
            is_public=True
        )
        self.deep_graph_tool = DeepGraphMCPTool(config)
        
    def configure_for_private_repository(self, repository: str, api_key: str, org_id: str = None):
        """Configure for private repository analysis"""
        config = DeepGraphConfig(
            repository=repository,
            api_key=api_key,
            org_id=org_id,
            is_public=False
        )
        self.deep_graph_tool = DeepGraphMCPTool(config)
        
    async def execute_comprehensive_analysis(self, repository: str) -> Dict[str, Any]:
        """Execute comprehensive multi-phase analysis"""
        
        if not self.deep_graph_tool:
            self.configure_for_public_repository(repository)
            
        results = {}
        
        # Phase 1: Discovery
        print("🔍 Executing Discovery Phase...")
        results["discovery"] = await self.deep_graph_tool.execute_discovery_workflow(repository)
        
        # Phase 2: Security Analysis  
        print("🔒 Executing Security Analysis...")
        results["security"] = await self.deep_graph_tool.execute_security_audit_workflow(repository)
        
        # Phase 3: Technical Debt Analysis
        print("⚠️ Executing Technical Debt Analysis...")
        results["technical_debt"] = await self.deep_graph_tool.execute_technical_debt_workflow(repository)
        
        # Generate comprehensive report
        return self._generate_comprehensive_report(results)
        
    def _generate_comprehensive_report(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive analysis report"""
        return {
            "analysis_summary": {
                "repository": results.get("discovery", {}).get("raw_results", {}).get("map_repository_structure", {}).get("data", "Unknown"),
                "phases_completed": list(results.keys()),
                "timestamp": "2025-07-27",
                "tool_version": "1.0.0"
            },
            "key_insights": [
                "Repository structure and entry points mapped",
                "Security components and practices analyzed",
                "Technical debt patterns identified"
            ],
            "actionable_recommendations": [
                "Review authentication implementation",
                "Address identified technical debt",
                "Implement comprehensive testing strategy"
            ],
            "detailed_results": results
        }

# Configuration for system prompt integration
SYSTEM_PROMPT_ADDITION = """
Deep Graph MCP Integration:
- Use for comprehensive code repository analysis and understanding
- Available in multi-agent workflows for discovery and verification phases
- Tools: list-graphs, get-code, find-direct-connections, nodes-semantic-search, docs-semantic-search, get-usage-dependency-links, folder-tree-structure
- Discovery Phase: Architecture mapping, documentation search, component identification
- Verification Phase: Dependency analysis, impact assessment, security validation
- Public repositories: Use format username/repository-name (e.g., microsoft/vscode)
- Private repositories: Requires CODEGPT_API_KEY, CODEGPT_ORG_ID
- Integrates with other MCP tools for comprehensive analysis workflows
- Custom commands available: analyze-architecture, security-audit, technical-debt-analyzer, migration-planner
"""