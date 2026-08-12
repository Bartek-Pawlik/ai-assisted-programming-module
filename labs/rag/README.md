# 🚀 Building Your First RAG Application - Hands-On Lab

**Atlantic Technological University, Galway**  
**AI Assisted Programming Module**  
**Estimated Time: 2 hours**

---

## 🎯 Learning Objectives

By the end of this lab, you will be able to:
- ✅ Process documents and split them into chunks
- ✅ Generate vector embeddings using sentence-transformers
- ✅ Store and query embeddings in a vector database (ChromaDB)
- ✅ Build a semantic search system
- ✅ Integrate retrieval with LLM generation
- ✅ Create a complete working RAG application
- ✅ Understand the difference between standard LLMs and RAG-enhanced LLMs

---

## 📋 Prerequisites

- Basic Python knowledge (variables, functions, loops)
- Familiarity with VS Code
- GitHub account (for Codespaces)
- GitHub Copilot enabled (free for students!)

---

## 🛠️ Setup Instructions

### Option 1: GitHub Codespaces (Recommended)
1. **Fork this repository** to your GitHub account
2. Click the green **Code** button → **Codespaces** → **Create codespace on main**
3. Wait for the environment to build (2-3 minutes)
4. Open the terminal in VS Code
5. Run: `python check_setup.py` to verify everything works

### Option 2: Local Development
```bash
# You already have this lab — it is in your copy of the module repo.
cd labs/rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify setup
python check_setup.py
```

---

## 📚 Lab Structure

| Part | Topic | Time | Difficulty |
|------|-------|------|------------|
| 1 | Setup & Environment | 15 min | 🟢 Easy |
| 2 | Document Processing & Embeddings | 30 min | 🟡 Medium |
| 3 | Retrieval System | 35 min | 🟡 Medium |
| 4 | Generation Integration | 30 min | 🟠 Challenging |
| 5 | Experimentation & Analysis | 10 min | 🟢 Easy |

---

## 🚦 Part 1: Setup & Environment (15 minutes)

### What You'll Learn
- How to set up a RAG development environment
- Load sample documents for retrieval
- Verify all dependencies are working

### Instructions

**Step 1.1: Verify Your Environment**

Run the setup checker:
```bash
python check_setup.py
```

You should see:
```
✅ Python 3.11+ detected
✅ sentence-transformers installed
✅ chromadb installed
✅ All dependencies ready!
```

⚠️ **Troubleshooting**: If you see errors, check that requirements.txt installed correctly.

**Step 1.2: Explore the Sample Documents**

Look in the `data/` directory. You'll find 5 documents about CS topics:
- `introduction_to_programming.txt`
- `data_structures_basics.txt`
- `algorithms_overview.txt`
- `database_fundamentals.txt`
- `web_development_intro.txt`

Open one and read it. These will be your knowledge base!

**Step 1.3: Run Your First Test**

```bash
python test_hello_rag.py
```

This simple script loads a document and prints it. Expected output:
```
📄 Loaded document: introduction_to_programming.txt
📊 Document length: 412 characters
✅ Setup complete!
```

### 💡 GitHub Copilot Tips
- Type `# load a text file` and let Copilot suggest the code
- Use Copilot Chat: "Explain what a vector database is"
- Press `Ctrl+I` (or `Cmd+I` on Mac) to ask Copilot questions inline

### ✅ Check Your Understanding
1. How many sample documents do we have?
2. What Python library will we use for embeddings?
3. What is the vector database we're using?

**Answers**: 5 documents, sentence-transformers, ChromaDB

---

## 📄 Part 2: Document Processing & Embeddings (30 minutes)

### What You'll Learn
- How to split documents into manageable chunks
- Generate vector embeddings from text
- Store embeddings in ChromaDB
- Perform basic similarity searches

### Visual Overview
```
Text Document → Chunk Splitter → Chunks → Embedding Model → Vectors → ChromaDB
   (File)         (500 chars)     (List)   (384 dimensions)  (Arrays)   (Storage)
```

---

### Exercise 2.1: Load Documents (5 minutes)

**File**: `part2_embeddings.py`

Find the function `load_documents()` and complete the TODO:

```python
def load_documents(data_dir="data"):
    """Load all .txt files from the data directory."""
    documents = []
    
    # TODO: Use os.listdir() to get all files in data_dir
    # TODO: Filter for .txt files only
    # TODO: Read each file and append to documents list
    
    return documents
```

**💡 Copilot Prompt**: "Read all text files from a directory and return their contents as a list"

**Expected Output**:
```python
docs = load_documents()
print(f"Loaded {len(docs)} documents")
# Output: Loaded 5 documents
```

---

### Exercise 2.2: Split Documents into Chunks (10 minutes)

**Why chunking?** Large documents won't fit in the LLM context window. We split them into smaller, semantically meaningful pieces.

Complete the `chunk_text()` function:

```python
def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split text into overlapping chunks.
    
    Args:
        text: The full document text
        chunk_size: Maximum characters per chunk (default 500)
        overlap: Characters to overlap between chunks (default 50)
    
    Returns:
        List of text chunks
    """
    chunks = []
    
    # TODO: Split text into chunks of chunk_size characters
    # TODO: Add overlap between chunks to maintain context
    # Hint: Use a loop with start position incrementing by (chunk_size - overlap)
    
    return chunks
```

**💡 Copilot Prompt**: "Split text into overlapping chunks with specified size and overlap"

**Test It**:
```python
sample_text = "Your document text here..." * 100
chunks = chunk_text(sample_text, chunk_size=500, overlap=50)
print(f"Created {len(chunks)} chunks")
print(f"First chunk: {chunks[0][:100]}...")
```

---

### Exercise 2.3: Generate Embeddings (10 minutes)

**What are embeddings?** Numerical representations of text that capture semantic meaning. Similar text = similar vectors!

Complete the `generate_embeddings()` function:

```python
from sentence_transformers import SentenceTransformer

def generate_embeddings(chunks, model_name="all-MiniLM-L6-v2"):
    """
    Generate vector embeddings for text chunks.
    
    Args:
        chunks: List of text chunks
        model_name: Name of the sentence-transformer model
    
    Returns:
        List of embedding vectors (numpy arrays)
    """
    # TODO: Load the SentenceTransformer model
    # TODO: Use model.encode() to generate embeddings for all chunks
    # TODO: Return the embeddings
    
    pass
```

**💡 Copilot Prompt**: "Use sentence-transformers to encode a list of text chunks into embeddings"

**Test It**:
```python
chunks = ["Hello world", "Machine learning is awesome"]
embeddings = generate_embeddings(chunks)
print(f"Generated {len(embeddings)} embeddings")
print(f"Each embedding has {len(embeddings[0])} dimensions")
# Output: Each embedding has 384 dimensions
```

**🎯 Understanding Check**: What does "384 dimensions" mean?
- Each chunk is represented as a list of 384 numbers
- These numbers capture the semantic meaning
- Similar chunks will have similar numbers

---

### Exercise 2.4: Store in ChromaDB (5 minutes)

**What is ChromaDB?** A vector database that stores embeddings and enables fast similarity search.

Complete the `store_in_chromadb()` function:

```python
import chromadb

def store_in_chromadb(chunks, embeddings, collection_name="cs_knowledge"):
    """
    Store chunks and their embeddings in ChromaDB.
    
    Args:
        chunks: List of text chunks
        embeddings: List of embedding vectors
        collection_name: Name for the ChromaDB collection
    
    Returns:
        ChromaDB collection object
    """
    # TODO: Initialize ChromaDB client
    # TODO: Create or get collection
    # TODO: Add documents with embeddings to collection
    # Hint: collection.add(documents=chunks, embeddings=embeddings, ids=[...])
    
    pass
```

**💡 Copilot Prompt**: "Store text chunks and embeddings in a ChromaDB collection"

**Test It**:
```python
collection = store_in_chromadb(chunks, embeddings)
print(f"✅ Stored {collection.count()} chunks in database")
```

---

### 🎉 Part 2 Complete!

Run the full Part 2 script:
```bash
python part2_embeddings.py
```

Expected output:
```
📚 Loading documents...
✅ Loaded 5 documents

✂️ Chunking documents...
✅ Created 47 chunks

🧮 Generating embeddings...
✅ Generated 47 embeddings (384 dimensions each)

💾 Storing in ChromaDB...
✅ Stored 47 chunks in vector database

🎉 Part 2 Complete! Your knowledge base is ready!
```

---

## 🔍 Part 3: Retrieval System (35 minutes)

### What You'll Learn
- Implement semantic search
- Rank results by relevance
- Manage context windows for LLMs
- Visualize retrieval results

### Visual Overview
```
User Query → Embed Query → Search Vector DB → Top-K Chunks → Rerank → Final Context
 "What is     [0.2, 0.5,   Cosine          [Chunk 3,     By Score    "Here are the
  Python?"      ...]       Similarity       Chunk 7, ...]             3 most relevant..."
```

---

### Exercise 3.1: Semantic Search (15 minutes)

**File**: `part3_retrieval.py`

Complete the `semantic_search()` function:

```python
def semantic_search(query, collection, model, top_k=3):
    """
    Search for the most relevant chunks given a query.
    
    Args:
        query: User's question (string)
        collection: ChromaDB collection
        model: SentenceTransformer model for embedding
        top_k: Number of results to return
    
    Returns:
        List of (chunk_text, distance_score) tuples
    """
    # TODO: Generate embedding for the query
    # TODO: Use collection.query() to find similar chunks
    # TODO: Return the top_k most similar chunks with their scores
    
    pass
```

**💡 Copilot Prompt**: "Query a ChromaDB collection with a text query and return top k similar results"

**Test It**:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
collection = ...  # load the collection you built in part 2

query = "What is a variable in programming?"
results = semantic_search(query, collection, model, top_k=3)

for i, (chunk, score) in enumerate(results, 1):
    print(f"\n{i}. Score: {score:.3f}")
    print(f"   {chunk[:150]}...")
```

---

### Exercise 3.2: Relevance Filtering (10 minutes)

Sometimes retrieved chunks aren't relevant enough. Add a relevance threshold!

Complete the `filter_by_relevance()` function:

```python
def filter_by_relevance(results, min_score=0.3):
    """
    Filter search results by minimum relevance score.
    
    Args:
        results: List of (chunk, score) tuples
        min_score: Minimum similarity score (0-1)
    
    Returns:
        Filtered list of results
    """
    # TODO: Filter results where score >= min_score
    # TODO: Return filtered results
    
    pass
```

**💡 Copilot Prompt**: "Filter a list of tuples by score threshold"

---

### Exercise 3.3: Context Window Management (10 minutes)

**The Problem**: LLMs have token limits! We need to fit retrieved chunks within the context window.

Complete the `manage_context_window()` function:

```python
def manage_context_window(chunks, max_tokens=1500):
    """
    Combine chunks while staying within token limit.
    
    Args:
        chunks: List of text chunks
        max_tokens: Maximum tokens to use (approximate)
    
    Returns:
        Combined context string
    """
    # TODO: Combine chunks with separators
    # TODO: Estimate tokens (roughly 4 characters = 1 token)
    # TODO: Truncate if exceeds max_tokens
    # Hint: Use "\n\n---\n\n" as separator between chunks
    
    pass
```

**💡 Copilot Prompt**: "Combine text chunks into a single string staying within a token limit"

**Test It**:
```python
chunks = ["Chunk 1" * 100, "Chunk 2" * 100, "Chunk 3" * 100]
context = manage_context_window(chunks, max_tokens=500)
print(f"Context length: {len(context)} characters")
print(f"Approximate tokens: {len(context) // 4}")
```

---

### 🎉 Part 3 Complete!

Run the full Part 3 script:
```bash
python part3_retrieval.py
```

Test with queries:
```
Query: "What is Python?"
✅ Found 3 relevant chunks
📊 Scores: [0.78, 0.65, 0.52]
📝 Context window: 1,247 tokens

Query: "How do databases work?"
✅ Found 3 relevant chunks
📊 Scores: [0.82, 0.71, 0.68]
📝 Context window: 1,198 tokens
```

---

## 🤖 Part 4: Generation Integration (30 minutes)

### What You'll Learn
- Connect to an LLM API (Anthropic Claude)
- Build effective RAG prompts
- Combine retrieval + generation
- Track source citations

### Visual Overview
```
Query → Retrieve Context → Build Prompt → LLM API → Response + Citations
        [Chunk 1, 2, 3]   "Answer using:  Claude     "Python is... 
                           [contexts]"              [Source: Chunk 1]"
```

---

### Exercise 4.1: Connect to LLM API (10 minutes)

**File**: `part4_generation.py`

We'll use Anthropic's Claude API (free tier available for students).

**Setup API Key**:
```bash
# Create a .env file (already in .gitignore)
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

**Get your API key**: https://console.anthropic.com/

Complete the `initialize_llm()` function:

```python
from anthropic import Anthropic
import os
from dotenv import load_dotenv

def initialize_llm():
    """Initialize the Anthropic Claude client."""
    # TODO: Load environment variables from .env
    # TODO: Get API key from environment
    # TODO: Create and return Anthropic client
    
    pass
```

**💡 Copilot Prompt**: "Initialize Anthropic client with API key from environment variable"

**Test It**:
```python
client = initialize_llm()
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello!"}]
)
print(response.content[0].text)
```

---

### Exercise 4.2: Build RAG Prompt Template (10 minutes)

**The Key to RAG**: Instructing the LLM to use retrieved context!

Complete the `build_rag_prompt()` function:

```python
def build_rag_prompt(query, context_chunks):
    """
    Build a prompt that combines the query with retrieved context.
    
    Args:
        query: User's question
        context_chunks: List of relevant text chunks
    
    Returns:
        Formatted prompt string
    """
    # TODO: Create a prompt template that:
    #   1. Provides the context chunks
    #   2. Instructs the LLM to use ONLY the provided context
    #   3. Asks it to cite which chunks were used
    #   4. Includes the user's query
    
    prompt = """You are a helpful CS instructor assistant. Answer the student's question using ONLY the information provided in the context below.

CONTEXT:
---
{context}
---

STUDENT QUESTION: {query}

Provide a clear, accurate answer based on the context. If the context doesn't contain enough information, say so. Cite which parts of the context you used.

ANSWER:"""
    
    # TODO: Format the prompt with actual context and query
    
    pass
```

**💡 Copilot Prompt**: "Create a RAG prompt template that instructs an LLM to answer using only provided context"

---

### Exercise 4.3: Complete RAG Pipeline (10 minutes)

**This is it!** The complete RAG system!

Complete the `rag_query()` function:

```python
def rag_query(question, collection, model, llm_client):
    """
    Complete RAG pipeline: retrieve → augment → generate.
    
    Args:
        question: User's question
        collection: ChromaDB collection
        model: Embedding model
        llm_client: Anthropic client
    
    Returns:
        dict with 'answer', 'sources', and 'context_used'
    """
    # TODO: 1. Retrieve relevant chunks using semantic_search()
    # TODO: 2. Build context using manage_context_window()
    # TODO: 3. Create prompt using build_rag_prompt()
    # TODO: 4. Call LLM API to generate response
    # TODO: 5. Return answer with metadata
    
    pass
```

**💡 Copilot Prompt**: "Implement a RAG pipeline that retrieves context, builds a prompt, and generates an LLM response"

**Test It**:
```python
question = "What is a variable in programming?"
result = rag_query(question, collection, model, llm_client)

print(f"Question: {question}")
print(f"\nAnswer: {result['answer']}")
print(f"\nSources used: {len(result['sources'])}")
```

---

### 🎉 Part 4 Complete!

Run the full RAG system:
```bash
python part4_generation.py
```

Try these test queries:
```
1. "What is Python used for?"
2. "Explain what an algorithm is"
3. "What are the benefits of using databases?"
```

---

## 📊 Part 5: Experimentation & Analysis (10 minutes)

### What You'll Learn
- Compare RAG vs non-RAG responses
- Experiment with parameters
- Document your findings

---

### Exercise 5.1: Side-by-Side Comparison

**File**: `part5_experiments.py`

Run the comparison script:
```bash
python part5_experiments.py
```

This will show you:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Question: What is a linked list?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🤖 WITHOUT RAG:
[Generic answer from LLM's training...]

✅ WITH RAG:
[Specific answer from your documents...]

Sources Used: 2 chunks from data_structures_basics.txt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Exercise 5.2: Parameter Experiments

Complete the experiments in `results.md`:

```markdown
# RAG Experiments - Results

## Experiment 1: Chunk Size Impact
- Chunk size 300: ___ retrieved, answer quality: ___
- Chunk size 500: ___ retrieved, answer quality: ___
- Chunk size 1000: ___ retrieved, answer quality: ___

**Observation**: [Your findings here]

## Experiment 2: Top-K Retrieval
- Top-1: Answer quality: ___
- Top-3: Answer quality: ___
- Top-5: Answer quality: ___

**Observation**: [Your findings here]

## Experiment 3: Hallucination Test
Query: "What is quantum computing?" (NOT in our documents)

- Without RAG: [Response]
- With RAG: [Response]

**Observation**: [Did RAG prevent hallucination?]
```

---

## 🎉 Lab Complete!

### What You Built
✅ Document processing pipeline  
✅ Vector embedding system  
✅ Semantic search engine  
✅ Complete RAG application  
✅ Comparison analysis

### What You Learned
✅ How RAG improves LLM accuracy  
✅ Vector databases and embeddings  
✅ Context window management  
✅ Prompt engineering for RAG  
✅ Practical AI system design

---

## 🚀 Extension Challenges (Optional)

### Challenge 1: Add a Web Interface 🌐
Use Streamlit to create a chat interface:
```python
import streamlit as st

st.title("RAG Chatbot")
query = st.text_input("Ask a question:")
if query:
    result = rag_query(query, ...)
    st.write(result['answer'])
```

### Challenge 2: Multi-Document RAG 📚
Extend to handle different document types (PDF, DOCX, HTML)

### Challenge 3: Hybrid Search 🔍
Combine semantic search with keyword search (BM25)

### Challenge 4: Evaluation Metrics 📊
Implement retrieval precision/recall measurements

### Challenge 5: Conversation Memory 💬
Add chat history to make it conversational

---

## 📚 Resources

### Documentation
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [Anthropic API](https://docs.anthropic.com/)

### Further Learning
- [LlamaIndex Tutorial](https://docs.llamaindex.ai/)
- [RAG Paper (Lewis et al. 2020)](https://arxiv.org/abs/2005.11401)
- [Vector Database Comparison](https://benchmark.vectorview.ai/)

---

## ❓ Troubleshooting

### "ModuleNotFoundError: No module named 'sentence_transformers'"
```bash
pip install -r requirements.txt
```

### "ChromaDB collection already exists"
```bash
# Delete the collection and recreate
rm -rf ./chroma_db
```

### "API key not found"
Check that `.env` file exists and contains:
```
ANTHROPIC_API_KEY=sk-ant-...
```

### "Out of memory"
Reduce chunk size or process fewer documents

---

## 🎓 Assignment Submission

**What to Submit**:
1. Completed code files (`part2_embeddings.py`, `part3_retrieval.py`, `part4_generation.py`)
2. `results.md` with your experiments
3. Screenshots of working RAG queries
4. (Optional) Your extension challenge code

**Due**: [Your deadline]

**Grading Rubric**:
- Part 2 (Document Processing): 25%
- Part 3 (Retrieval): 25%
- Part 4 (Generation): 30%
- Part 5 (Experiments): 15%
- Code Quality & Documentation: 5%

---

**Created by**: Atlantic Technological University, Galway  
**Module**: AI Assisted Programming  
**Instructor**: [Your Name]  
**Academic Year**: 2024-2025

Good luck, and enjoy building your first RAG application! 🎉
