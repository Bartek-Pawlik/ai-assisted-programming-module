# AI Coding Agents Lab

## Overview
In this 2-hour lab, you will explore and compare different AI coding agents, learning how they assist developers through various interaction modes. You'll work hands-on with GitHub Copilot's three modes (Ask, Edit, and Agent) and experiment with cloud-based autonomous coding agents.

### What are AI Coding Agents?
AI coding agents are intelligent assistants that help developers write, understand, and modify code. Unlike simple code completion tools, modern coding agents can:
- Understand natural language instructions
- Navigate entire codebases
- Make multi-file changes
- Run tests and fix errors autonomously
- Create pull requests with complete implementations

```mermaid
graph TB
    A[Developer Request] --> B{AI Coding Agent}
    
    B --> C[Ask Mode]
    B --> D[Edit Mode]
    B --> E[Agent Mode]
    B --> F[Cloud Agent]
    
    C --> C1[Answer Questions]
    C --> C2[Explain Code]
    C --> C3[Provide Examples]
    
    D --> D1[Generate Code]
    D --> D2[Refactor Files]
    D --> D3[Fix Bugs]
    
    E --> E1[Multi-file Changes]
    E --> E2[Run Commands]
    E --> E3[Execute Tools]
    
    F --> F1[Autonomous Work]
    F --> F2[Create PR]
    F --> F3[Run Tests]
    
    style A fill:#0288d1,stroke:#01579b,stroke-width:3px,color:#fff
    style B fill:#7b1fa2,stroke:#4a0072,stroke-width:3px,color:#fff
    style C fill:#f57c00,stroke:#e65100,stroke-width:3px,color:#fff
    style D fill:#0097a7,stroke:#006064,stroke-width:3px,color:#fff
    style E fill:#388e3c,stroke:#1b5e20,stroke-width:3px,color:#fff
    style F fill:#d84315,stroke:#bf360c,stroke-width:3px,color:#fff
```

### The Three Modes of GitHub Copilot

```mermaid
flowchart LR
    A[GitHub Copilot] --> B[Ask Mode]
    A --> C[Edit Mode]
    A --> D[Agent Mode]
    
    B --> B1[💬 Chat Interface]
    B --> B2[📚 Code Explanations]
    B --> B3[❓ Questions & Answers]
    
    C --> C1[✏️ Code Generation]
    C --> C2[🔄 Refactoring]
    C --> C3[📝 Single/Multi-file Edits]
    
    D --> D1[🤖 Autonomous Actions]
    D --> D2[🛠️ Tool Execution]
    D --> D3[🔍 Workspace Navigation]
    
    style A fill:#6200ea,stroke:#311b92,stroke-width:3px,color:#fff
    style B fill:#f57f17,stroke:#f57f17,stroke-width:3px,color:#000
    style C fill:#0277bd,stroke:#01579b,stroke-width:3px,color:#fff
    style D fill:#2e7d32,stroke:#1b5e20,stroke-width:3px,color:#fff
```

**Ask Mode** - Conversational assistance:
- Answer coding questions
- Explain existing code
- Provide code examples
- Suggest best practices
- No direct code editing

**Edit Mode** - Direct code modification:
- Generate new code
- Modify existing files
- Refactor code
- Apply changes directly to files
- Single or multiple file edits

**Agent Mode** - Autonomous task execution:
- Break down complex tasks
- Navigate workspace autonomously
- Execute terminal commands
- Run tests and validate changes
- Multi-step problem solving

### Learning Objectives
By the end of this lab, you will be able to:
- Distinguish between Ask, Edit, and Agent modes
- Use each Copilot mode effectively for different tasks
- Leverage cloud coding agents for autonomous development
- Compare different AI coding assistants (GitHub Copilot vs Google Jules)
- Understand when to use each type of agent
- Evaluate agent-generated code critically

## 1. 🚀 Quick Start
1. **Verify GitHub Copilot Access**: Ensure you have GitHub Copilot enabled
2. **Open in Codespace**: Click "Code" → "Create codespace on main"
3. **Wait for Setup**: Codespace will configure automatically
4. **Verify Copilot**: Check the Copilot icon in the bottom-right status bar
5. **Start Learning**: Begin with Part 1

## 2. 🛠️ Setup (5 minutes)

### Verify GitHub Copilot is Active
Look for the Copilot icon in the VS Code status bar (bottom right). It should show as active.

### Open Copilot Chat
- Press `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac)
- Or click the chat icon in the sidebar

### Test Copilot
In the chat, type:
```
Hello! Are you working?
```

You should get a response from Copilot.

## 3. 📚 Lab Structure

```mermaid
flowchart TD
    A[Setup & Introduction] --> B[Part 1: Ask Mode]
    B --> C[Part 2: Edit Mode]
    C --> D[Part 3: Agent Mode]
    D --> E[Part 4: Cloud Coding Agent]
    E --> F[Part 5: Google Jules]
    F --> G[Reflection & Comparison]
    
    B --> B1[Code Explanation]
    B --> B2[Question Answering]
    B --> B3[Learning Exercise]
    
    C --> C1[Code Generation]
    C --> C2[Refactoring]
    C --> C3[Bug Fixing]
    
    D --> D1[Multi-file Changes]
    D --> D2[Testing Integration]
    D --> D3[Complex Tasks]
    
    E --> E1[Create Issue]
    E --> E2[Autonomous Work]
    E --> E3[PR Review]
    
    F --> F1[Jules Setup]
    F --> F2[Feature Implementation]
    F --> F3[Comparison]
    
    style A fill:#2e7d32,stroke:#1b5e20,stroke-width:3px,color:#fff
    style B fill:#f57f17,stroke:#f57f17,stroke-width:3px,color:#000
    style C fill:#0277bd,stroke:#01579b,stroke-width:3px,color:#fff
    style D fill:#388e3c,stroke:#1b5e20,stroke-width:3px,color:#fff
    style E fill:#d84315,stroke:#bf360c,stroke-width:3px,color:#fff
    style F fill:#7b1fa2,stroke:#4a0072,stroke-width:3px,color:#fff
    style G fill:#d84315,stroke:#bf360c,stroke-width:3px,color:#fff
```

---

_Continue to the full lab content by following the exercises in each part folder..._

## Quick Reference Card

```mermaid
flowchart LR
    A[Need Help?] --> B{What do you need?}
    
    B -->|Explanation| C[Ask Mode<br/>Ctrl+Alt+I]
    B -->|Code Change| D[Edit Mode<br/>Ctrl+I]
    B -->|Big Feature| E[Agent/Cloud<br/>Ctrl+Shift+I]
    
    C --> F[💬 Chat]
    D --> G[✏️ Inline Edit]
    E --> H[🤖 Autonomous]
    
    style A fill:#0288d1,stroke:#01579b,stroke-width:3px,color:#fff
    style C fill:#f57f17,stroke:#f57f17,stroke-width:3px,color:#000
    style D fill:#0277bd,stroke:#01579b,stroke-width:3px,color:#fff
    style E fill:#2e7d32,stroke:#1b5e20,stroke-width:3px,color:#fff
```

**Keyboard Shortcuts:**
- `Ctrl+Alt+I` - Open Copilot Chat (Ask Mode)
- `Ctrl+I` - Inline Copilot (Edit Mode)
- `Ctrl+Shift+I` - Copilot Edits (Agent Mode)
- `Ctrl+Enter` - Accept suggestion
- `Esc` - Reject suggestion

---
