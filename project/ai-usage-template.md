# AI-USAGE Documentation

## About This Document

This document provides comprehensive documentation of all AI-assisted programming techniques, tools, and methodologies used throughout the development of this project. It demonstrates proficiency in modern AI-assisted development practices and serves as evidence of thoughtful engagement with AI tools. This documentation is a required component of the AIAP module assessment and should be 2-3 pages in length.

**Complete all relevant sections below to document:**
- AI tools and techniques used during development
- Implementation of MCP or RAG (for development or in your app)
- Effective prompting examples with real code
- Challenges faced and lessons learned
- Reflection on AI's impact on your development process

---

## 1. AI Tools Used

List all AI tools you used during development. For each tool, briefly describe how you used it.

**Example:**
- **GitHub Copilot** - Used for code completion and generating boilerplate code
- **Claude 3.5 Sonnet** - Used for architectural decisions and debugging complex issues
- **ChatGPT** - Used for research and learning new Python libraries
- **Cursor AI** - Used for refactoring and code optimisation

**Your Tools:**
- **[Tool Name]** - [How you used it]
- **[Tool Name]** - [How you used it]
- **[Tool Name]** - [How you used it]

---

## 2. Prompting Techniques Applied

Document the specific AI prompting techniques you learned and applied during development.

### Techniques Used:

#### Few-Shot Learning
Describe how you provided examples to the AI to get better results.

**Example:**
```
I showed the AI 2-3 examples of similar functions before asking it to generate a new one,
which resulted in more consistent code style matching my project.
```

#### Chain-of-Thought Prompting
Explain how you broke down complex problems into steps.

**Example:**
```
Instead of asking "build a login system", I asked step-by-step:
1. First, help me design the database schema for users
2. Then, create the authentication endpoint
3. Finally, implement password hashing and JWT tokens
```

#### Prompt Refinement Iterations
Describe how you improved your prompts based on initial results.

**Example:**
```
Initial prompt: "Create a function to process data"
Refined prompt: "Create a Python function that takes a pandas DataFrame, 
removes null values, normalises numeric columns to 0-1 range, and returns 
the cleaned DataFrame with type hints and docstring"
```

#### Context-Aware Prompting
Explain how you provided relevant context to get better responses.

**Example:**
```
I included relevant code snippets, error messages, and project structure in my 
prompts to get more accurate and project-specific suggestions.
```

#### Other Techniques
List any other techniques you used (role-playing, constraint-based prompting, etc.)

---

## 3. Advanced Technique Implementation

**I implemented:** ☐ MCP (Model Context Protocol)  ☐ RAG (Retrieval-Augmented Generation)

**I used this technique:** ☐ For Development (to help me code)  ☐ In My App (as a user feature)

---

### Option A: MCP (Model Context Protocol) Implementation

**⚠️ Only complete this section if you implemented MCP**

#### MCP Server(s) Used
List which MCP server(s) you configured and used:
- **[Server Name]** - [Purpose, e.g., "filesystem access", "GitHub integration"]
- **[Server Name]** - [Purpose]

#### How I Used MCP

**Choose one:**

**☐ For Development:**
Explain how MCP enhanced your coding process:
- What documentation or tools did it connect to?
- How did it improve your AI assistant's responses?
- What specific problems did it help solve?

**Example:**
```
I configured the MCP filesystem server to give Claude access to my project files.
This allowed the AI to understand my entire codebase context and suggest changes
that were consistent with my existing code structure. It significantly reduced
the back-and-forth needed to explain my project setup.
```

**☐ In My App:**
Explain how MCP provides features to your users:
- What external APIs or services does it connect to?
- How do users benefit from this integration?
- What functionality does it enable?

**Example:**
```
My recipe app uses MCP to connect to the Spoonacular API in real-time. When users
ask about nutritional information or ingredient substitutions, the app queries
the API via MCP and provides current, accurate data. This gives users access to
a database of 300,000+ recipes and ingredients.
```

#### Configuration Details
Include relevant configuration (remove sensitive keys):

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"]
    }
  }
}
```

#### Screenshots/Evidence
[Add screenshots showing MCP in action]

#### Code Example (if applicable)
```python
# Include relevant code snippet showing MCP implementation
```

---

### Option B: RAG (Retrieval-Augmented Generation) Implementation

**⚠️ Only complete this section if you implemented RAG**

#### RAG Implementation Approach
Describe your technical implementation:
- What vector database or search technology did you use? (e.g., ChromaDB, FAISS, Pinecone)
- How did you chunk and embed your documents?
- What embedding model did you use? (e.g., OpenAI embeddings, sentence-transformers)

**Example:**
```
I used ChromaDB with OpenAI's text-embedding-3-small model. Documents were split
into 500-token chunks with 50-token overlap. I stored 50+ course PDFs totaling
~200,000 tokens in the vector database.
```

#### How I Used RAG

**Choose one:**

**☐ For Development:**
Explain how RAG helped you code:
- What knowledge base did you create? (your codebase, documentation, etc.)
- How did it improve your development process?
- What specific examples can you share?

**Example:**
```
I implemented RAG over my project's documentation and previous code examples.
When I needed to implement a new feature, I could query similar implementations,
and the AI would provide suggestions based on my actual codebase patterns rather
than generic examples. This maintained consistency across my project.
```

**☐ In My App:**
Explain how RAG provides features to your users:
- What knowledge base do users query?
- How does RAG improve the user experience?
- What kind of questions can users ask?

**Example:**
```
My study app allows students to upload their course materials (PDFs, notes).
Using RAG, students can ask questions like "What topics are covered in Chapter 5?"
or "Explain photosynthesis based on my notes." The AI retrieves relevant sections
from their uploaded materials and generates accurate, personalised answers based
on their specific course content.
```

#### Knowledge Base Details
- **Size:** [Number of documents, total tokens, etc.]
- **Content Type:** [PDFs, markdown files, code files, etc.]
- **Update Frequency:** [Static, user-uploaded, real-time, etc.]

#### Technical Implementation
```python
# Include relevant code snippets showing:
# 1. Document loading and chunking
# 2. Embedding generation
# 3. Vector storage
# 4. Query and retrieval process

# Example:
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Your implementation here
```

#### Screenshots/Evidence
[Add screenshots showing RAG in action - queries and responses]

---

## 4. Effective Prompts Examples

Provide 3-5 examples of effective prompts that generated useful code or solutions.

### Example 1: [Brief Description]

**Original Prompt:**
```
[Your exact prompt here]
```

**AI-Generated Response:**
```python
# Include the relevant code or explanation the AI provided
```

**Why It Was Effective:**
[Explain what made this prompt successful - was it specific? Did it include context? Did it use a particular technique?]

**Refinements Made:**
[If you refined the prompt, show the iterations]

---

### Example 2: [Brief Description]

**Original Prompt:**
```
[Your exact prompt here]
```

**AI-Generated Response:**
```python
# Include the relevant code or explanation the AI provided
```

**Why It Was Effective:**
[Explanation]

**Refinements Made:**
[If applicable]

---

### Example 3: [Brief Description]

**Original Prompt:**
```
[Your exact prompt here]
```

**AI-Generated Response:**
```python
# Include the relevant code or explanation the AI provided
```

**Why It Was Effective:**
[Explanation]

**Refinements Made:**
[If applicable]

---

### Example 4: [Brief Description] (Optional)

[Follow same format as above]

---

### Example 5: [Brief Description] (Optional)

[Follow same format as above]

---

## 5. Challenges and Solutions

### Challenge 1: [Challenge Name]
**Description:** [Describe the problem you faced with AI tools]

**Initial Approach:** [What you tried first]

**Solution:** [How you refined your prompts or approach to overcome the issue]

**Lesson Learned:** [What you learned about effective AI-assisted programming]

---

### Challenge 2: [Challenge Name]
**Description:** [Describe the problem]

**Initial Approach:** [What you tried first]

**Solution:** [How you solved it]

**Lesson Learned:** [What you learned]

---

### Challenge 3: [Challenge Name]
**Description:** [Describe the problem]

**Initial Approach:** [What you tried first]

**Solution:** [How you solved it]

**Lesson Learned:** [What you learned]

---

## 6. Impact Reflection

### Development Speed
[Write 1-2 paragraphs discussing how AI tools impacted your development speed. Consider:]
- How much faster were you able to develop compared to without AI?
- What tasks were accelerated the most?
- Were there any tasks that took longer due to AI assistance?

**Example:**
```
AI tools significantly accelerated my development process, particularly in the initial
setup and boilerplate code generation. Tasks that would typically take hours, such as
setting up authentication or creating CRUD operations, were completed in minutes. However,
I found that debugging AI-generated code sometimes took longer than expected, as I needed
to thoroughly understand the suggestions before integrating them. Overall, I estimate
AI tools increased my productivity by approximately 40-50%.
```

---

### Code Quality
[Write 1-2 paragraphs discussing how AI tools affected your code quality. Consider:]
- Did AI help you write better, cleaner code?
- Did you learn new patterns or best practices from AI suggestions?
- Were there any quality issues with AI-generated code?

**Example:**
```
AI assistance generally improved my code quality by introducing me to best practices and
design patterns I wasn't familiar with. The AI often suggested more efficient algorithms
and better error handling approaches. However, I learned to carefully review all suggestions,
as some generated code lacked proper validation or didn't handle edge cases. The key was
treating AI as a knowledgeable pair programmer rather than accepting suggestions blindly.
```

---

### Future Projects
[Write 1-2 paragraphs discussing what you would do differently in future projects. Consider:]
- What AI techniques were most valuable?
- What would you change about your approach?
- How has this experience changed your view of AI-assisted programming?

**Example:**
```
In future projects, I would invest more time upfront in setting up comprehensive context
for the AI tools, including detailed project documentation and examples. I would also
experiment more with advanced techniques like RAG earlier in the development process
rather than treating it as an add-on. This project has convinced me that AI-assisted
programming is not about replacing programming skills but augmenting them—the developers
who thrive will be those who can effectively communicate with and guide AI tools while
maintaining critical thinking about the solutions provided.
```

---

## Summary

**Total Pages:** [This document should be 2-3 pages in length]

**Key Achievements:**
- ✓ Documented all AI tools used
- ✓ Applied multiple prompting techniques
- ✓ Implemented [MCP/RAG] for [development/app features]
- ✓ Provided concrete examples of effective prompts
- ✓ Reflected on challenges and learning outcomes
- ✓ Analyzed impact on development speed and code quality

---

**Declaration:** I confirm that I understand all code in my project and can explain any section during demonstrations. I have used AI tools responsibly and documented their usage accurately.
