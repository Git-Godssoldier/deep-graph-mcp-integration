"""
Deep Graph MCP Integration Demonstration
Shows practical usage in multi-agent workflows
"""

import asyncio
import json
from datetime import datetime
from deep_graph_mcp_tool import MultiAgentWorkflowOrchestrator, DeepGraphMCPTool, DeepGraphConfig

async def demo_repository_analysis():
    """Demonstrate comprehensive repository analysis"""
    
    print("🚀 Deep Graph MCP Integration Demo")
    print("=" * 50)
    
    # Initialize orchestrator
    orchestrator = MultiAgentWorkflowOrchestrator()
    
    # Example 1: Analyze a popular open source repository
    repository = "microsoft/vscode"
    print(f"\n📁 Analyzing repository: {repository}")
    
    try:
        # Execute comprehensive analysis
        results = await orchestrator.execute_comprehensive_analysis(repository)
        
        print("\n✅ Analysis Complete!")
        print(f"📊 Analysis Summary:")
        print(f"   Repository: {results['analysis_summary']['repository']}")
        print(f"   Phases: {', '.join(results['analysis_summary']['phases_completed'])}")
        
        print(f"\n🔍 Key Insights:")
        for insight in results['key_insights']:
            print(f"   • {insight}")
            
        print(f"\n💡 Recommendations:")
        for rec in results['actionable_recommendations']:
            print(f"   • {rec}")
            
    except Exception as e:
        print(f"❌ Error during analysis: {e}")

async def demo_component_analysis():
    """Demonstrate component-specific analysis"""
    
    print("\n🔧 Component Analysis Demo")
    print("=" * 30)
    
    # Configure for specific repository
    config = DeepGraphConfig(repository="facebook/react", is_public=True)
    tool = DeepGraphMCPTool(config)
    
    # Analyze specific component
    component = "useState"
    print(f"\n🎯 Analyzing component: {component}")
    
    try:
        results = await tool.execute_verification_workflow("facebook/react", component)
        
        print("\n✅ Component Analysis Complete!")
        print(f"📋 Summary: {results['summary']}")
        
        print(f"\n🔍 Insights:")
        for insight in results['insights']:
            print(f"   • {insight}")
            
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"   • {rec}")
            
    except Exception as e:
        print(f"❌ Error during component analysis: {e}")

async def demo_security_audit():
    """Demonstrate security audit workflow"""
    
    print("\n🔒 Security Audit Demo")
    print("=" * 25)
    
    config = DeepGraphConfig(repository="vercel/next.js", is_public=True)
    tool = DeepGraphMCPTool(config)
    
    print(f"\n🛡️ Running security audit on: vercel/next.js")
    
    try:
        results = await tool.execute_security_audit_workflow("vercel/next.js")
        
        print("\n✅ Security Audit Complete!")
        print(f"📋 Summary: {results['summary']}")
        
        print(f"\n🔍 Security Findings:")
        for finding in results['findings']:
            print(f"   • {finding}")
            
        print(f"\n🛡️ Security Recommendations:")
        for rec in results['recommendations']:
            print(f"   • {rec}")
            
    except Exception as e:
        print(f"❌ Error during security audit: {e}")

async def demo_multi_phase_workflow():
    """Demonstrate multi-phase workflow for unknown repository"""
    
    print("\n🔄 Multi-Phase Workflow Demo")
    print("=" * 35)
    
    # Scenario: New team member needs to understand unfamiliar codebase
    repository = "nodejs/node" 
    
    config = DeepGraphConfig(repository=repository, is_public=True)
    tool = DeepGraphMCPTool(config)
    
    print(f"\n📚 Onboarding workflow for: {repository}")
    print("   Simulating new team member exploring codebase...")
    
    # Phase 1: Discovery
    print("\n🔍 Phase 1: Repository Discovery")
    discovery_results = await tool.execute_discovery_workflow(repository)
    print(f"   ✅ {discovery_results['summary']}")
    
    # Phase 2: Security Review  
    print("\n🔒 Phase 2: Security Analysis")
    security_results = await tool.execute_security_audit_workflow(repository)
    print(f"   ✅ {security_results['summary']}")
    
    # Phase 3: Technical Debt Assessment
    print("\n⚠️ Phase 3: Technical Debt Analysis")
    debt_results = await tool.execute_technical_debt_workflow(repository)
    print(f"   ✅ {debt_results['summary']}")
    
    # Generate onboarding report
    onboarding_report = {
        "repository": repository,
        "analysis_date": datetime.now().isoformat(),
        "onboarding_phases": {
            "discovery": discovery_results,
            "security": security_results, 
            "technical_debt": debt_results
        },
        "recommended_next_steps": [
            "Review main entry points identified in discovery",
            "Examine security implementation patterns",
            "Prioritize technical debt items for immediate attention",
            "Set up development environment using found documentation"
        ]
    }
    
    print("\n📄 Onboarding Report Generated!")
    print(f"   Repository: {onboarding_report['repository']}")
    print(f"   Phases completed: {len(onboarding_report['onboarding_phases'])}")
    print(f"   Next steps: {len(onboarding_report['recommended_next_steps'])}")

def demo_configuration_examples():
    """Show configuration examples for different scenarios"""
    
    print("\n⚙️ Configuration Examples")
    print("=" * 30)
    
    # Public repository configurations
    public_configs = [
        {"name": "Single Public Repo", "repos": ["microsoft/vscode"]},
        {"name": "Multiple Public Repos", "repos": ["facebook/react", "vercel/next.js", "nodejs/node"]},
        {"name": "Open Source Analysis", "repos": ["tensorflow/tensorflow", "pytorch/pytorch"]}
    ]
    
    print("\n📂 Public Repository Configurations:")
    for config in public_configs:
        print(f"   {config['name']}: {', '.join(config['repos'])}")
    
    # Usage scenarios
    scenarios = [
        {
            "scenario": "Code Review",
            "tools": ["get-code", "find-direct-connections", "get-usage-dependency-links"],
            "description": "Analyze impact of proposed changes"
        },
        {
            "scenario": "Security Assessment", 
            "tools": ["nodes-semantic-search", "docs-semantic-search"],
            "description": "Find security-related code and documentation"
        },
        {
            "scenario": "Architecture Analysis",
            "tools": ["folder-tree-structure", "nodes-semantic-search", "find-direct-connections"],
            "description": "Understand codebase structure and relationships"
        },
        {
            "scenario": "Onboarding",
            "tools": ["docs-semantic-search", "folder-tree-structure", "nodes-semantic-search"],
            "description": "Help new team members understand the codebase"
        }
    ]
    
    print("\n🎯 Usage Scenarios:")
    for scenario in scenarios:
        print(f"   {scenario['scenario']}:")
        print(f"     Tools: {', '.join(scenario['tools'])}")
        print(f"     Purpose: {scenario['description']}")

async def main():
    """Run all demonstrations"""
    
    print("🎉 Starting Deep Graph MCP Integration Demonstrations")
    print("=" * 60)
    
    # Run configuration examples (synchronous)
    demo_configuration_examples()
    
    # Run async demonstrations
    await demo_repository_analysis()
    await demo_component_analysis() 
    await demo_security_audit()
    await demo_multi_phase_workflow()
    
    print("\n🎊 All demonstrations completed!")
    print("\n📚 Next Steps:")
    print("   1. Configure Deep Graph MCP for your repositories")
    print("   2. Integrate into your multi-agent workflows")
    print("   3. Customize analysis phases for your specific needs")
    print("   4. Set up team sharing for collaborative analysis")

if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())