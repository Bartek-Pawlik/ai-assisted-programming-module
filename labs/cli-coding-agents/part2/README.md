# Part 2: Google Gemini CLI (40 minutes)

Learn to use Google's official Gemini CLI - a powerful terminal-based coding agent with built-in tools and MCP extensibility.

> **Important:** This is the **official Google Gemini CLI** (npm package), NOT a custom Python wrapper. It's a full-featured terminal agent similar to GitHub Copilot CLI.

## Overview

Google Gemini CLI is an open-source terminal-based AI agent that brings the power of Gemini directly into your command line:
- **Built-in tools** - Google Search grounding, file operations, shell commands, web fetching
- **MCP extensibility** - Connect custom tools via Model Context Protocol
- **Multi-turn conversations** - maintains context across queries
- **Free tier available** - 60 req/min, 1000 req/day with Google OAuth
- **Gemini 2.5 Pro** - Access to 1M token context window

### Gemini CLI vs GitHub Copilot CLI

Both are **npm-based terminal coding agents**, but with different focuses:

| Feature | GitHub Copilot CLI | Gemini CLI |
|---------|-------------------|------------|
| **Installation** | `sudo npm install -g @github/copilot` | `sudo npm install -g @google/gemini-cli` |
| **Launch** | `copilot` | `gemini` |
| **Authentication** | GitHub PAT or `/login` | Google OAuth or API key |
| **Primary Focus** | GitHub-integrated development | General development + search |
| **Built-in Tools** | GitHub operations, MCP servers | Google Search, file ops, shell, MCP |
| **Approval Model** | Shows diffs, requires approval | Tool-based approvals |
| **Best For** | GitHub workflows, file editing | Research, automation, multi-tool tasks |
| **Free Tier** | Requires Copilot subscription | 60 req/min with Google account |

## Setup

### Installation

```bash
# Install globally
sudo npm install -g @google/gemini-cli

# Verify installation
gemini --version
```

### Authentication

You have three options:

#### Option 1: OAuth Login (Recommended)

**Best for:** Individual developers, learning

**Benefits:**
- Free tier: 60 requests/min, 1000 requests/day
- Gemini 2.5 Pro with 1M token context window
- No API key management

**Steps:**
```bash
# Launch Gemini CLI
gemini

# Choose "Login with Google" when prompted
# Follow the browser authentication flow
```

#### Option 2: API Key

**Best for:** Specific model control, scripting

**Benefits:**
- Free tier: 100 requests/day
- Model selection control
- Usage-based billing option

**Steps:**
```bash
# Get API key from https://aistudio.google.com/apikey
export GEMINI_API_KEY="YOUR_API_KEY"

# Make it permanent
echo 'export GEMINI_API_KEY="your-key"' >> ~/.bashrc
source ~/.bashrc

# Launch
gemini
```

## Part 2.1: Basic Usage (15 minutes)

### Starting Gemini CLI

```bash
# Start in current directory
gemini

# Start with specific directories included
gemini --include-directories ../lib,../docs

# Use specific model
gemini -m gemini-2.5-flash
```

### Example 1: Code Generation

```bash
gemini
```

In the Gemini CLI prompt:
```
> Create a Python function to validate email addresses with regex, including type hints and docstrings
```

**What you'll get:**
- Complete function with type hints
- Comprehensive docstring
- Regex pattern for email validation
- Example usage
- Edge case handling

### Example 2: Code Understanding

```bash
# Navigate to a codebase
cd ~/my-project
gemini
```

```
> Explain the architecture of this codebase and identify the main components
```

**Gemini will:**
- Analyze your project structure
- Identify key modules and dependencies
- Explain the overall architecture
- Highlight important patterns

### Example 3: Using Built-in Tools

**Google Search Grounding:**
```
> What are the latest best practices for React hooks in 2025?
# Gemini will search Google and provide current information
```

**File Operations:**
```
> List all Python files in this directory and show me which ones import requests
```

**Shell Commands:**
```
> Run the tests and tell me which ones failed
```

### Practice: Try These Tasks

1. **Generate a utility function:**
   ```
   > Create a Python function to calculate fibonacci numbers with memoization
   ```

2. **Analyze existing code:**
   ```
   > Review the main.py file and suggest improvements
   ```

3. **Research with grounding:**
   ```
   > What's the difference between asyncio and threading in Python? Use Google Search to get current best practices
   ```

4. **File operations:**
   ```
   > Find all TODO comments in this codebase and create a summary
   ```

## Part 2.2: Interactive Development (10 minutes)

Gemini CLI's real power is in multi-turn conversations with tool usage.

### Scenario 1: Build a CLI Tool

```bash
gemini
```

**Conversation Flow:**

```
You: Create a command-line weather app that fetches weather from wttr.in

Gemini: [Generates initial Python script with requests]

You: Add caching so we don't hit the API repeatedly

Gemini: [Adds file-based caching with expiration]

You: Add command-line arguments for city and units

Gemini: [Adds argparse with city and units options]

You: Add colored output for temperature ranges

Gemini: [Adds colorama for temperature-based coloring]

You: Create unit tests for this

Gemini: [Generates pytest test file]
```

### Scenario 2: Debug with Context

```
You: I'm getting a "TypeError: 'NoneType' object is not iterable" error. Here's my code:
def process_data(data):
    return [item['value'] * 2 for item in data]

Gemini: [Identifies the issue - data might be None]
Gemini: [Suggests adding None check and validation]

You: How do I make this more robust?

Gemini: [Suggests type hints, Optional handling, error messages]

You: Show me the improved version with logging

Gemini: [Provides complete version with logging]
```

### Your Turn: Build a Project

Choose one project and build it through conversation:

#### Option A: Log Analyzer
```
1. Create a script to parse log files
2. Count ERROR, WARN, INFO levels
3. Find most common error messages
4. Generate HTML report
5. Add command-line options
6. Create tests
```

#### Option B: Git Helper
```
1. Script to analyze git history
2. Find contributors and their commit counts
3. Identify files changed most often
4. Generate summary report
5. Add options for date ranges
6. Create tests
```

#### Option C: File Organizer
```
1. Script to organize files by type
2. Move files to category folders
3. Handle duplicates safely
4. Log all operations
5. Add dry-run mode
6. Create tests
```

## Part 2.3: Advanced Features (15 minutes)

### Slash Commands

Gemini CLI has built-in commands for various operations:

```
/help          # Show all available commands
/chat          # Start a new conversation
/clear         # Clear conversation history
/checkpoint    # Save current conversation
/restore       # Restore saved conversation
/model         # Switch between models
/settings      # View/modify settings
/bug           # Report a bug
```

### Non-Interactive Mode (Scripting)

**Simple text output:**
```bash
gemini -p "Explain the architecture of this codebase"
```

**JSON output for parsing:**
```bash
gemini -p "List all function names in main.py" --output-format json
```

**Stream JSON for real-time events:**
```bash
gemini -p "Run all tests and deploy" --output-format stream-json
```

**Use in scripts:**
```bash
#!/bin/bash
RESULT=$(gemini -p "What's the latest version in package.json?" --output-format json)
VERSION=$(echo $RESULT | jq -r '.text')
echo "Current version: $VERSION"
```

### Context Files (GEMINI.md)

Create a `GEMINI.md` file in your project root to provide persistent context:

```markdown
# Project Context

## Architecture
This is a FastAPI application with PostgreSQL database.

## Key Files
- `main.py` - Application entry point
- `models/` - SQLAlchemy models
- `api/` - API routes
- `tests/` - pytest tests

## Development Commands
- `pytest` - Run tests
- `uvicorn main:app` - Start server
- `alembic upgrade head` - Run migrations

## Code Style
- Use type hints
- Follow PEP 8
- Write docstrings for all public functions
```

Now when you ask questions, Gemini will use this context automatically.

### Checkpointing

Save and resume complex sessions:

```bash
# In Gemini CLI
> /checkpoint save refactoring-session

# Later, resume
> /checkpoint restore refactoring-session
```

### MCP Server Integration

Extend Gemini CLI with custom tools via MCP servers.

**Example: Configure GitHub MCP Server**

Edit `~/.gemini/settings.json`:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

**Use it:**
```
> @github List my open pull requests
> @github Show recent issues assigned to me
```

## Part 2.4: Comparison Exercise (5 minutes)

Complete the same task with both agents and compare.

### Task: Refactor a Function

**With GitHub Copilot CLI:**
```bash
copilot
> Refactor the process_data function in utils.py to add type hints and error handling
# Shows diff → Review → Approve → File updated
```

**With Gemini CLI:**
```bash
gemini
> Show me the process_data function from utils.py refactored with type hints and error handling
# Shows refactored code → You manually update file
```

### Create Comparison Notes

In `part2/comparison.md`:

```markdown
# Agent Comparison

## Task: Refactor function

### Copilot CLI
- Workflow: Request → Diff → Approve → Done
- File handling: Automatic
- Pros: Safe, tracks changes, no manual work
- Cons: Slower (approval step)

### Gemini CLI
- Workflow: Request → Output → Manual copy
- File handling: Manual
- Pros: Fast, see full context
- Cons: Manual work, no automatic tracking

## When to Use Which?

Copilot CLI:
- Editing existing files safely
- GitHub-integrated workflows
- Team environments

Gemini CLI:
- Research with Google Search
- Quick code generation
- Complex multi-step automation
- Learning and exploration
```

## Exercise 2: Build with Gemini CLI (15 minutes)

Build the **Log Analyzer** tool using Gemini CLI.

### Requirements

Your tool should:
1. Parse log files for ERROR, WARN, INFO
2. Count occurrences of each level
3. Identify top 5 most common errors
4. Generate summary report
5. Support command-line arguments
6. Include tests

### Step-by-Step

```bash
# Create project directory
mkdir -p part2/exercise/log-analyzer
cd part2/exercise/log-analyzer

# Start Gemini CLI
gemini
```

**Conversation:**
```
You: Create a Python CLI tool to analyze log files. It should:
- Parse log lines for ERROR, WARN, INFO levels
- Count each level
- Find top 5 most common error messages
- Display a summary report
- Accept log file path as argument
Use argparse and include type hints

[Wait for code]

You: Add a feature to export results to JSON

[Wait for update]

You: Create pytest tests for this tool

[Wait for tests]
```

### Test Your Tool

```bash
# Create sample log
cat > sample.log << 'EOF'
2025-11-03 10:00:00 INFO Starting application
2025-11-03 10:00:01 ERROR Database connection failed
2025-11-03 10:00:02 WARN Retrying connection
2025-11-03 10:00:03 ERROR Database connection failed
2025-11-03 10:00:04 INFO Application started
EOF

# Run analyzer
python log_analyzer.py sample.log

# Run tests
pytest test_analyzer.py
```

## Tips for Using Gemini CLI Effectively

### 1. Leverage Built-in Tools

```
# Use Google Search for current info
> Search for "Python async best practices 2025" and summarize

# Use file operations
> List all files modified in the last week

# Use shell commands
> Run the test suite and analyze failures
```

### 2. Provide Clear Context

**Bad:**
```
> Fix the bug
```

**Good:**
```
> I'm getting a KeyError in the process_user function in auth.py. Here's the error:
KeyError: 'email'
The function expects a user dict but sometimes the email key is missing. How should I handle this?
```

### 3. Use Non-Interactive Mode for Automation

```bash
# In CI/CD pipeline
gemini -p "Review the changes in this PR and list potential issues" --output-format json
```

### 4. Create Project Context Files

Always create a `GEMINI.md` in your projects to help Gemini understand your codebase better.

### 5. Use Checkpointing for Complex Tasks

```
> /checkpoint save before-refactoring
# Do your work
# If something goes wrong
> /checkpoint restore before-refactoring
```

## Common Issues & Solutions

### Issue: Rate Limiting

**Symptom:** "Rate limit exceeded"

**Solution:**
- OAuth login has higher limits (60 req/min vs 100 req/day for API key)
- Consider Vertex AI for production workloads

### Issue: Tool Approval Required

**Symptom:** Gemini asks permission for every tool use

**Solution:**
```bash
# Allow all tools (be cautious!)
gemini --allow-all-tools

# Allow specific tool
gemini --allow-tool=shell

# Configure in settings for persistence
```

### Issue: Large Context

**Symptom:** Responses are slow with large codebases

**Solution:**
```bash
# Be specific about directories
gemini --include-directories src,tests

# Exclude large directories
gemini --exclude-directories node_modules,dist
```

## Key Takeaways

After completing Part 2, you should be able to:

✅ Install and authenticate Gemini CLI  
✅ Use built-in tools (Search, file ops, shell)  
✅ Build projects through multi-turn conversations  
✅ Understand tool-based approvals  
✅ Use non-interactive mode for scripting  
✅ Configure MCP servers for extensions  
✅ Compare Gemini CLI vs Copilot CLI workflows  

## What's Next?

In Part 3, you'll:
- Learn advanced comparison strategies
- Complete real-world scenarios
- Build custom workflows
- Develop tool selection expertise

---

**Time Check:** You should have spent about 40 minutes on this section.

## Bonus: Advanced Techniques (Optional)

### Bonus 1: GitHub Action Integration

Use Gemini CLI in CI/CD:

```yaml
name: AI Code Review
on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '20'
      - run: npm install -g @google/gemini-cli
      - run: |
          gemini -p "Review the changes in this PR" \
            --output-format json \
            > review.json
      - uses: actions/github-script@v6
        with:
          script: |
            const review = require('./review.json')
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: review.text
            })
```

### Bonus 2: Custom MCP Servers

Create your own tools:

```json
{
  "mcpServers": {
    "database": {
      "command": "node",
      "args": ["./mcp-servers/database-server.js"],
      "env": {
        "DB_CONNECTION": "postgresql://..."
      }
    }
  }
}
```

### Bonus 3: Token Caching

Optimize for cost and performance:

```bash
# Gemini CLI automatically caches tokens
# View cache status
gemini --show-cache-info

# Clear cache if needed
gemini --clear-cache
```

---

**Ready to continue?** Move on to [Part 3: Advanced Features & Comparison](../part3/README.md)
