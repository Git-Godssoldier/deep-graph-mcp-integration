# Deep Graph MCP Integration for Multi-Agent Workflows

This integration adds sophisticated code analysis capabilities to multi-agent workflows using the Deep Graph MCP tool.

## Overview

Deep Graph MCP provides semantic code analysis, dependency mapping, and repository understanding capabilities that enhance multi-agent workflows in discovery and verification phases.

## Features

### 🔍 Discovery Phase Tools
- **Repository Structure Mapping**: Get comprehensive folder tree and file organization
- **Semantic Code Search**: Find functionality using natural language queries
- **Documentation Discovery**: Locate setup guides, architecture docs, and explanations
- **Entry Point Identification**: Discover main application entry points and key components

### ✅ Verification Phase Tools
- **Dependency Analysis**: Map direct and indirect code dependencies
- **Impact Assessment**: Analyze which components are affected by changes
- **Code Implementation Review**: Examine actual implementation details
- **Connection Mapping**: Understand relationships between code entities

### 🛡️ Analysis Phase Tools
- **Security Audit**: Identify authentication, authorization, and validation patterns
- **Technical Debt Assessment**: Find TODO markers, deprecated code, and duplication
- **Performance Analysis**: Locate performance-critical code paths
- **Architecture Review**: Comprehensive architectural overview

## Quick Start

### 1. For Public Repositories

```bash
# Claude Code setup
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest microsoft/vscode

# Claude Desktop config
{
  "mcpServers": {
    "Deep Graph MCP": {
      "command": "npx",
      "args": ["-y", "mcp-code-graph@latest", "microsoft/vscode"]
    }
  }
}
```

### 2. For Private Repositories

```bash
# Get API key from https://app.codegpt.co/user/api-keys
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest YOUR_CODEGPT_API_KEY
```

### 3. Multi-Repository Analysis

```bash
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest microsoft/vscode facebook/react vercel/next.js
```

## Available Tools

| Tool | Purpose | Phase |
|------|---------|-------|
| `list-graphs` | List available repository graphs | Discovery |
| `get-code` | Retrieve complete code implementation | Discovery/Verification |
| `find-direct-connections` | Explore immediate relationships | Verification |
| `nodes-semantic-search` | Semantic search for code functionalities | Discovery |
| `docs-semantic-search` | Search repository documentation | Discovery |
| `get-usage-dependency-links` | Analyze change impact | Verification |
| `folder-tree-structure` | Get folder tree structure | Discovery |

## Workflow Integration

### Discovery Workflow
```python
# 1. Map repository structure
folder-tree-structure → Understanding codebase organization

# 2. Find documentation  
docs-semantic-search: "setup installation configuration" → Setup guides

# 3. Identify entry points
nodes-semantic-search: "main entry point application startup" → Key components

# 4. Map API surface
nodes-semantic-search: "api endpoints routes controllers" → API structure
```

### Verification Workflow  
```python
# 1. Examine implementation
get-code: component_name → Code details

# 2. Map dependencies
find-direct-connections: component_name → Direct relationships

# 3. Analyze impact
get-usage-dependency-links: component_name → Change impact radius
```

### Security Audit Workflow
```python
# 1. Find security components
nodes-semantic-search: "authentication authorization security" → Security patterns

# 2. Check validation
nodes-semantic-search: "input validation sanitization" → Validation logic

# 3. Review crypto usage
nodes-semantic-search: "password encryption hashing jwt" → Crypto implementation
```

## Custom Commands

After setup, these commands become available:

```bash
/project:analyze-architecture          # Complete architectural overview
/project:security-audit               # Comprehensive security analysis
/project:technical-debt-analyzer      # Technical debt assessment
/project:migration-planner [tech]     # Smart migration planning
/project:performance-optimizer [comp] # Performance optimization
/project:component-onboarding [comp]  # Component-specific training
```

## Usage Examples

### Repository Analysis
```
"Can you analyze the architecture of microsoft/vscode using Deep Graph MCP?"
```

### Component Investigation  
```
"Use Deep Graph MCP to examine the authentication system in the repository and show me its dependencies"
```

### Security Review
```
"Perform a security audit of the codebase focusing on input validation and authentication patterns"
```

### Migration Planning
```
"/project:migration-planner React to Vue.js"
```

## Multi-Agent Workflow Benefits

1. **Enhanced Discovery**: Semantic search finds relevant code using natural language
2. **Improved Verification**: Dependency analysis reveals change impact
3. **Automated Analysis**: Custom commands provide comprehensive insights
4. **Team Alignment**: Shared understanding of codebase structure
5. **Quality Assurance**: Built-in security and technical debt analysis

## Repository Support

### Public Repositories
- Any repository on https://deepgraph.co/
- Format: `username/repository-name`
- No authentication required

### Private Repositories  
- Requires CodeGPT account and API key
- Upload repository to CodeGPT Code Graph
- Get API key from https://app.codegpt.co/user/api-keys

## Next Steps

1. Configure for your repositories
2. Integrate into existing workflows  
3. Train team on available commands
4. Customize analysis phases for your needs
5. Set up automated analysis pipelines