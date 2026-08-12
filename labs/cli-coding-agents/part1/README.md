# Part 1: GitHub Copilot CLI (40 minutes)

Learn to use GitHub Copilot CLI - a full-featured terminal-based coding agent.

## Overview

GitHub Copilot CLI is an interactive AI coding agent that runs in your terminal. Unlike simple command generators, it's a full coding assistant that can:
- Have multi-turn conversations about your code
- Read and edit files directly (with your approval)
- Execute shell commands
- Access GitHub context (repos, issues, PRs)
- Maintain session history
- Delegate tasks to background agents

**Key Concept:** Copilot CLI is a **coding agent**, not just a command suggester. It's similar to having an AI pair programmer in your terminal.

## Basic Usage

### Starting Copilot CLI

```bash
# Launch the interactive agent
copilot

# Launch with animated banner
copilot --banner

# Quit a session
/quit

# Resume your last session
copilot --continue
```

### Understanding the Interface

When you launch Copilot CLI, you'll see:

```
╭─────────────────────────────────────────╮
│   Welcome to GitHub COPILOT CLI v1.0   │
│   Claude Sonnet 4.5 • Connected        │
╰─────────────────────────────────────────╯

Working Directory: ~/projects/my-app
User: @yourname
Session: #42

You: _
```

The interface shows:
- **Current model** (Claude Sonnet 4.5, GPT-5, or Claude Haiku)
- **Working directory** (where files will be edited)
- **Your username** and session ID
- **Input prompt** for your requests

### Slash Commands

Copilot CLI has built-in commands prefixed with `/`:

```bash
/help              # Show available commands
/model             # List or switch AI models
/login             # Authenticate with GitHub
/user              # Manage GitHub accounts
/mcp               # Manage MCP servers
/agent             # Use custom agents
/delegate          # Delegate task to background agent
/usage             # View session statistics
/clear             # Clear conversation history
/exit              # Exit the session
```

### Direct Shell Commands

You can execute shell commands directly with `!`:

```bash
!git status
!ls -la
!pwd
```

These bypass the AI and execute immediately.

## Part 1.1: Interactive Conversations (15 minutes)

### Example 1: Simple Code Task

Start Copilot:

```bash
copilot
```

Then interact:

```
You: Create a Python function to calculate fibonacci numbers

Copilot: I'll create a fibonacci function for you.

[Tool: write_file] Creating fibonacci.py

```python
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

✓ File: fibonacci.py

Approve this change?
[1] Yes  [2] No  [3] See diff  [4] Edit

You: 1

✓ Changes applied successfully

Would you like me to add test cases or optimize this?
```

**What just happened:**
1. You made a request in natural language
2. Copilot **proposed** a solution  
3. You **approved** the change (explicit permission)
4. Copilot created the file
5. Copilot asked about next steps

### Example 2: Multi-Turn Conversation

Continue the conversation:

```
You: Yes, add test cases

Copilot: I'll add pytest test cases.

[Tool: write_file] Creating test_fibonacci.py

```python
import pytest
from fibonacci import fibonacci

def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_sequence():
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
```

Approve? [1] Yes  [2] No  [3] See diff

You: 1

✓ test_fibonacci.py created

You: Run the tests

Copilot: I'll run the test suite.

[Tool: shell] Running: pytest test_fibonacci.py

============================= test session starts ==============================
collected 2 items

test_fibonacci.py ..                                                     [100%]

============================== 2 passed in 0.03s ===============================

✓ All tests passed!
```

**Key Observations:**
- Copilot **remembers context** (knows about the fibonacci function)
- Each action requires **approval**
- Copilot can **execute commands** after you approve
- The conversation flows naturally

### Example 3: File Mentions with @

Use `@` to reference files:

```
You: @src/app.js add error handling to the login function

Copilot: I'll read the file first.

[Tool: read_file] Reading src/app.js

Found login function at line 42. I'll add try-catch error handling.

[Tool: write_file] Modifying src/app.js

```javascript
async function login(username, password) {
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify({ username, password })
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Login failed:', error);
    throw new Error('Login failed. Please try again.');
  }
}
```

Approve? [1] Yes  [2] No  [3] See diff

You: 3

[Diff shown...]

You: 1

✓ Changes applied to src/app.js
```

**File Mention Features:**
- Type `@` to open file picker
- Fuzzy search for files
- Recently modified files shown first
- Works with images too (Copilot can analyze screenshots)

## Part 1.2: Permission Model & Safety (10 minutes)

### Understanding Approvals

Copilot CLI requires explicit approval before:
- Creating or modifying files
- Executing shell commands
- Accessing GitHub APIs
- Using MCP tools

**This is a safety feature** - you control everything.

### Approval Options

When Copilot proposes an action:

```
[1] Yes                    # Approve and execute
[2] No                     # Reject and ask for different approach
[3] See diff               # View changes before deciding
[4] Edit                   # Modify the proposal
```

### Managing Permissions

You can pre-approve certain operations:

```bash
# Launch with all paths allowed (skip file permission prompts)
copilot --allow-all-paths

# Allow specific tool patterns
copilot --allow-tool "shell(npm test)"
copilot --allow-tool "shell(git *)"

# Deny dangerous operations
copilot --deny-tool "shell(rm -rf *)"
```

### Safe Testing

Always test safely:

```
You: Find and delete all .log files older than 30 days

Copilot: I'll search for old log files first.

[Tool: shell] Running: find . -name "*.log" -mtime +30 -print

Found 12 log files older than 30 days:
  ./logs/app-2024-09-15.log
  ./logs/app-2024-09-18.log
  ...

Would you like me to delete these? I can show you the delete command first.

You: Show me the command

Copilot: The command would be:
find . -name "*.log" -mtime +30 -delete

This will permanently delete the files. Proceed?

[1] Yes, delete them  [2] No  [3] Create backup first
```

## Part 1.3: GitHub Context Integration (15 minutes)

### Using GitHub MCP Tools

Copilot CLI has built-in GitHub integration through MCP (Model Context Protocol).

### Example: Working with Issues

```
You: Show me open issues labeled "bug"

Copilot: I'll search GitHub issues.

[Tool: github_list_issues] Repository: current
[Tool: github_list_issues] Filter: label:bug state:open

Found 3 open bugs:
#45: Login button not responding on mobile
#47: API timeout on large requests  
#52: Memory leak in background worker

Would you like me to work on any of these?

You: Fix issue #52

Copilot: I'll investigate the memory leak issue.

[Tool: github_get_issue] Reading issue #52...

The issue mentions the background worker in src/workers/processor.js.
Let me examine that file.

[Tool: read_file] Reading src/workers/processor.js

I found the problem - event listeners are not being removed. I'll fix it.

[Tool: write_file] Modifying src/workers/processor.js

[Shows fix...]

Approve? [1] Yes [2] No [3] See full code

You: 1

✓ Changes applied

Would you like me to:
1. Create a test to verify the fix
2. Comment on the issue explaining the fix
3. Create a pull request
```

### Example: Creating Pull Requests

```
You: Create a PR for this fix

Copilot: I'll commit the changes and create a PR.

[Tool: shell] git add src/workers/processor.js
[Tool: shell] git commit -m "Fix: Remove event listeners to prevent memory leak in background worker"
[Tool: shell] git push -u origin fix-memory-leak-52

[Tool: github_create_pr]
  Title: Fix memory leak in background worker (closes #52)
  Body: [Generated description of changes]
  Base: main
  Head: fix-memory-leak-52

✓ Pull request created: #53
  URL: https://github.com/user/repo/pull/53

The PR links to issue #52 and will close it when merged.
```

### Available GitHub Tools

Default GitHub MCP tools:
- `get_file_contents` - Read files from repos
- `search_code` - Search across repositories
- `list_commits` - View commit history
- `get_issue` / `list_issues` - Work with issues
- `pull_request_read` / `list_pull_requests` - Manage PRs
- `list_workflows` - View CI/CD workflows
- `get_workflow_run` - Check build status

Enable ALL GitHub tools:
```bash
copilot --enable-all-github-mcp-tools
```

## Exercise 1: Build a Feature with Copilot (15 minutes)

Explore Copilot CLI by building a simple TODO CLI application. Focus on learning how the tool works rather than documenting everything.

### Task: Build a TODO CLI Application

Try to create a simple command-line TODO application with these features:
1. Add a todo item
2. List all todos
3. Mark todo as complete
4. Delete a todo
5. Save todos to a JSON file

### Your Approach

Experiment with Copilot CLI to build this application. Ask questions and explore different ways to interact with the agent.

### Success Criteria

- ✅ All features working
- ✅ Data persists to JSON file
- ✅ Error handling included
- ✅ Tests pass
- ✅ You understand all the code

### Tips

1. **Start Simple:**
   ```
   You: Create a basic TODO CLI structure in Python
   ```

2. **Iterate:**
   ```
   You: Add functionality to save todos to a JSON file
   You: Add error handling for file operations
   You: Create pytest tests for the add_todo function
   ```

3. **Use File Mentions:**
   ```
   You: @todo_cli.py add a delete command similar to the complete command
   ```

4. **Test as You Go:**
   ```
   You: Run the tests
   You: Try adding a todo item with: python todo_cli.py add "Buy milk"
   ```

5. **Ask for Explanations:**
   ```
   You: Explain how the JSON persistence works
   ```

## Key Takeaways - Part 1

After completing this section, you should understand:

✅ **Copilot CLI is a coding agent** - not just a command suggester  
✅ **Approval workflow** - you control all actions  
✅ **Multi-turn conversations** - maintains context  
✅ **File operations** - can read and write files  
✅ **GitHub integration** - works with issues and PRs  
✅ **Session persistence** - resume where you left off  

### Comparison with Traditional Development

| Task | Traditional | With Copilot CLI |
|------|-------------|------------------|
| Create new file | `touch file.py`, open editor, write code | "Create a Python file for..." → approve |
| Add tests | Research testing framework, write tests | "Add tests" → approve |
| Fix bug from issue | Read issue, find code, debug, fix | "Fix issue #42" → approve fix |
| Create PR | Commit, push, open GitHub, fill form | "Create a PR for this" → approve |

### When to Use Copilot CLI

**Great For:**
- Building new features from scratch
- Refactoring existing code
- Adding tests
- Working with GitHub issues/PRs
- Learning new codebases
- Delegating background tasks

**Less Ideal For:**
- Very simple one-liners (overhead of approval)
- When you need to see code as it's being written
- Operations requiring real-time feedback

## What's Next?

In Part 2, you'll explore Google Gemini CLI, which offers a different approach:
- No approval workflow (direct execution)
- Different conversation style
- Different strengths and use cases

You'll then compare both agents to understand when to use each one.

---

**Time Check:** You should have spent about 40 minutes on this section.

**Ready to continue?** Move on to [Part 2: Google Gemini CLI](../part2/README.md)
