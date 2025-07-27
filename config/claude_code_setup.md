# Claude Code Setup Commands for Deep Graph MCP

## For Public Repositories

# Single repository
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest microsoft/vscode

# Multiple repositories  
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest microsoft/vscode facebook/react vercel/next.js

# Team sharing (project-wide)
claude mcp add -s project "Deep Graph MCP" npx -- -y mcp-code-graph@latest microsoft/vscode

## For Private Repositories

# With API key
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest YOUR_CODEGPT_API_KEY

# With API key and org ID
claude mcp add "Deep Graph MCP" npx -- -y mcp-code-graph@latest YOUR_CODEGPT_API_KEY YOUR_ORG_ID

# Team sharing for private repos
claude mcp add -s project "Deep Graph MCP" npx -- -y mcp-code-graph@latest YOUR_CODEGPT_API_KEY

## Verification Commands

# Verify installation
claude mcp list

# Get server details
claude mcp get "Deep Graph MCP"

# Test with a simple query
claude "Can you analyze the architecture of the repository using Deep Graph MCP?"

## Custom Commands Setup

# Copy custom commands from Deep Graph MCP repository
cp -r .claude/ /path/to/your/project/
git add .claude/commands/
git commit -m "Add Deep Graph MCP custom commands"

# Available custom commands:
# /project:analyze-architecture
# /project:security-audit  
# /project:test-coverage-analyzer
# /project:technical-debt-analyzer
# /project:api-ecosystem-analyzer
# /project:repository-onboarding
# /project:migration-planner [component/technology]
# /project:performance-optimizer [component/function]
# /project:component-onboarding [component/feature]