# AIAP Project

**Worth 60% of the module.** Due at the end of week 12.

Published in week 2 — and that is deliberate. This is the largest single
piece of work in the module and it is assessed on your commit history as
well as the finished application, so a project started in week 10 cannot
score well no matter how good the last commit is.

- **[Grading rubric](rubric.md)** — how this is marked
- **[AI-USAGE.md template](ai-usage-template.md)** — a required deliverable

## 📱 Project Overview
For this project you are required to design and develop an application using AI-Assisted Programming tools. Your app will utilise the learning of labs and lectures throughout the semester. 

## 👣Getting Started
Your application must follow a topic selected from the `Project App Choice List` on the Moodle page. The application will be like the applications we developed in labs but with improved design and additional functionality.

## ⚡ Minimum Project Requirements
- You must use the Project GitHub Repository provided to you on the Moodle page. No other development setup will be acceptable. This link to create your repository can be found under the `Project Assessment` section on Moodle.
- This application must be developed using GitHub Codespaces.
- Project development must be tracked on GitHub via regular commits. Your GitHub repository must have at minimum two commits per week, if not I may contact you for a live project demonstration. The project should be completed progressively as commits over time. This is a learning journal. I do not expect to see commits all happening at the end.
- The README file should contain clear instructions for compiling, deploying, and running the application. It should also briefly outline the nature of the project and detail the set of features it contains.
- **An AI-USAGE.md file documenting your use of AI-assisted programming tools (see requirements below)**

## 🛠️ Minimum Feature Requirements
- Use of AI Tools (see detailed requirements below)
- Backend as a Service (BaaS) integration (e.g., Firebase, Supabase, etc.)
- CICD pipeline via GitHub Actions
- AI integration (e.g., AI API integration, AI-powered features)
- **Implementation of at least ONE advanced AI technique:**
  - **MCP Integration**: Implement Model Context Protocol to assist your development process OR as a feature in your app, OR
  - **RAG Implementation**: Use Retrieval-Augmented Generation to assist your development process OR as a feature in your app
  
  **Note:** You can use MCP/RAG in either of these ways:
  - **For Development**: Use MCP/RAG in your AI coding assistant to help you write code (e.g., MCP to access documentation, RAG to search your codebase)
  - **In Your App**: Implement MCP/RAG as features that end-users interact with (e.g., RAG for searching user documents, MCP to connect to external APIs)

## 🤖 AI-Assisted Programming Requirements
Students must demonstrate proficiency in AI-assisted development by maintaining an **AI-USAGE.md** file that documents:

### Required Documentation Sections

#### 1. AI Tools Used
List all AI tools used during development (e.g., GitHub Copilot, Claude, ChatGPT, Cursor, etc.)

#### 2. Prompting Techniques Applied
Document specific techniques used:
- Few-shot learning examples
- Chain-of-thought prompting
- Prompt refinement iterations
- Context-aware prompting
- Any other techniques learned in the module

#### 3. Advanced Technique Implementation
**You must implement at least ONE of the following:**

**Option A: MCP (Model Context Protocol) Integration**
- Document which MCP server(s) you used
- **Specify whether you used MCP:**
  - **For Development**: How it enhanced your coding process (e.g., accessing docs, connecting to tools)
  - **In Your App**: How it provides features to end-users (e.g., connecting to external APIs/databases)
- Provide specific examples and screenshots
- Include configuration details

**Option B: RAG (Retrieval-Augmented Generation) Implementation**
- Describe your RAG implementation approach
- **Specify whether you used RAG:**
  - **For Development**: How it helped you code (e.g., searching your codebase, finding examples)
  - **In Your App**: How it provides features to end-users (e.g., searching user documents, context-aware responses)
- Explain what knowledge base or documentation you used
- Provide specific examples and screenshots
- Include code snippets showing implementation

#### 4. Effective Prompts Examples
Provide 3-5 examples of effective prompts that generated useful code or solutions:
- Include the original prompt
- Show the AI-generated response
- Explain why it was effective
- Document any refinements made

#### 5. Challenges and Solutions
- Document challenges faced with AI tools
- Explain how you refined prompts to overcome issues
- Share lessons learned about effective AI-assisted programming

#### 6. Impact Reflection (1-2 paragraphs)
- How did AI tools impact your development speed?
- How did they affect your code quality?
- What would you do differently in future projects?

**Note:** This documentation should be 2-3 pages in length and demonstrate thoughtful engagement with AI-assisted programming techniques.

## 🛠️ Technology Stack Requirements

### Backend (REQUIRED)
- **Python is REQUIRED** for all AI/RAG/database logic
- All core AI-assisted programming techniques must be implemented in Python
- Python virtual environment setup with `requirements.txt`
- Follow PEP 8 coding standards

### Frontend (FLEXIBLE)
Students may choose any of the following for their frontend:
- **Modern JavaScript Frameworks**: React, Vue, Svelte, etc.
- **Python-based UI**: Streamlit, Gradio, Flask templates, Django templates
- **Plain Web Technologies**: HTML, CSS, vanilla JavaScript
- **Other Modern Frameworks**: Any current, well-documented framework

### Backend as a Service (BaaS)
- **Firebase**, **Supabase**, or other approved BaaS platforms
- Must include authentication and/or database functionality

### Development Environment
- **GitHub Codespaces** (REQUIRED)
- All development must occur in the provided Codespaces environment

### Architecture Requirements
- **Clear separation** between frontend and backend code
- Backend handles all AI/RAG processing, database operations, and business logic
- Frontend focuses on user interface and user experience
- Well-defined API or communication layer between frontend and backend

## 📝 Coding Standards

### General Standards
- Your code must compile/run without errors
- Consistent code formatting throughout the project
- Comprehensive documentation through comments
  - Module/file-level documentation
  - Class-level documentation
  - Function/method-level documentation
  - Complex logic documentation
- Proper error handling and logging

### Python-Specific Standards (Backend)
- Follow **PEP 8** style guide for Python code
- Use type hints where appropriate
- Include docstrings for all functions, classes, and modules
- Maintain a `requirements.txt` file with all dependencies
- Use virtual environments (venv or similar)
- Organize code into logical modules and packages
- Write clean, readable, maintainable code

### Frontend Standards
- Follow best practices for your chosen framework/technology
- Consistent naming conventions
- Responsive design principles
- Accessible UI components
- Clean separation of concerns (UI logic vs. presentation)

## 🎯 AI-Generated Code Standards
While AI tools are encouraged and required, you are responsible for:
- **Understanding all code in your submission** - You must be able to explain any section of code
- Ensuring AI-generated code follows project standards
- Properly adapting and integrating AI suggestions (not just copy-paste)
- Testing and validating all AI-generated code
- Refactoring AI suggestions to match your application's architecture
- **Be prepared to explain any code section during demonstrations**

## ⭐ Enhanced Features
To achieve a higher grade, consider implementing:
- **AI-Enhanced Features**:
  - Implementation of BOTH MCP and RAG (if you only did one for minimum requirements)
  - Using MCP/RAG in BOTH contexts (development AND in your app)
  - Custom AI-powered features using multiple API integrations
  - CLI coding agent integration (e.g., Claude Code) demonstrated in your workflow
  - Advanced prompting techniques beyond course material
- Additional design features not seen in labs
- Additional functionality not seen in labs
- App store deployment
- Particularly creative or innovative use of AI assistance

## 📊 Project Submission Process
You **must** follow this submission process carefully. If you miss any part, especially the screencast, you will be penalised.

### 1. Screencast Demonstration
- **7-10 minute** screen recording using [MS Stream](https://www.microsoft365.com/launch/stream), YouTube or any screencasting tool that works for you. 
- **AI Tool Demonstration (REQUIRED - 3-4 minutes)**:
  - Show your AI-USAGE.md file and briefly explain your documentation
  - Demonstrate 1-2 examples of effective prompts you used during development
  - **Show your MCP or RAG implementation in action** - clearly explain whether you used it:
    - For development (show how it helped you code), OR
    - In your app (demonstrate the feature to users)
  - Explain how AI assistance improved your development process
  - Demonstrate any advanced AI techniques you implemented
- **Code Walkthrough (3-4 minutes)**:
  - Highlight areas where you expended most effort
  - Show integration of AI-generated code
  - Explain your code architecture and design decisions
- **Application Demonstration (2-3 minutes)**:
  - Demonstrate your application running
  - Show all key features in operation
  - Highlight any additional functionality implemented
- **MAKE SURE YOUR SCREENCAST IS ACCESSIBLE BY ME**. CHECK STREAMS/OneDrive/YouTube PERMISSIONS and make sure it can be seen by me.

### 2. Moodle Submission
- [Download a copy of your final Git repository from the GitHub website.](https://youtube.com/shorts/4bDLccFjQyc?si=dWUDWoW4B_tnADty)
- Upload this zip file under the submission link on Moodle. You can find the submission link under the Final Project section on the Moodle page.
- In the submission area on Moodle, where you upload your project, you will see a text box in which you will be able to enter text (See sample below). Put the URL link to your project GitHub repository and screencast video in this text box.
- Submit the zip file to Moodle before the due date. The due date can be found by clicking on the submission link on Moodle. Late submissions will incur a 10% penalty per day. 

  #### Sample Textbox Input
  <pre>
  <b>Screencast Link:</b> https://atlantictu-my.sharepoint.com/:v:/g/personal/.../your-recording
  <b>GitHub Link:</b> https://github.com/your-username/your-project-repo
  </pre>

## ⚠️ Important Notes
1. Only materials within this GitHub repository will be graded. (40% grade cap if missed)
2. Missing AI-USAGE.md file will result in a maximum grade of 40%
3. Insufficient commits may require a live demonstration (40% grade cap if missed)
4. Late submissions incur a 10% penalty per day
5. You must implement at least ONE advanced technique (MCP or RAG) to pass

