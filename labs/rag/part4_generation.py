"""
Part 4: Generation Integration
Atlantic Technological University - RAG Lab

In this part, you will:
1. Connect to an LLM API (Anthropic Claude)
2. Build RAG prompt templates
3. Create a complete RAG pipeline
4. Add source citation tracking

Estimated time: 30 minutes
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer


def initialize_llm():
    """
    Initialize the Anthropic Claude client.
    
    Returns:
        Anthropic client object
    """
    # TODO: Exercise 4.1
    # 1. Load environment variables from .env file using load_dotenv()
    # 2. Get the ANTHROPIC_API_KEY from environment using os.getenv()
    # 3. Create and return an Anthropic client
    #
    # If no API key is set, this will use a mock mode for testing
    #
    # Usage:
    # load_dotenv()
    # api_key = os.getenv("ANTHROPIC_API_KEY")
    # client = Anthropic(api_key=api_key)
    #
    # GitHub Copilot Prompt: "Initialize Anthropic client with API key from environment"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def build_rag_prompt(query, context_chunks):
    """
    Build a prompt that combines the query with retrieved context.
    
    Args:
        query: User's question
        context_chunks: List of relevant text chunks
        
    Returns:
        Formatted prompt string
    """
    # TODO: Exercise 4.2
    # Create a prompt template that:
    # 1. Provides clear instructions to the LLM
    # 2. Includes all context chunks with separators
    # 3. Instructs to use ONLY the provided context
    # 4. Asks for source citations
    # 5. Includes the user's query
    #
    # Template structure:
    # - System instruction
    # - Context section (all chunks)
    # - Query section
    # - Answer instruction
    #
    # GitHub Copilot Prompt: "Create RAG prompt template with context and query sections"
    
    # YOUR CODE HERE
    
    # Example template structure (you can modify this):
    prompt = """You are a helpful computer science teaching assistant for first-year students at Atlantic Technological University.

Answer the student's question using ONLY the information provided in the context below. If the context doesn't contain enough information, say so clearly.

CONTEXT:
---
{context}
---

STUDENT QUESTION: {query}

Provide a clear, accurate answer based on the context above. Be specific and cite which parts of the context you used.

ANSWER:"""
    
    # Format the prompt with actual context and query
    # TODO: Combine all context_chunks with separators
    # TODO: Insert into the template
    
    pass  # Remove this line when you add your code


def call_llm(client, prompt, max_tokens=500):
    """
    Call the LLM API with the given prompt.
    
    Args:
        client: Anthropic client
        prompt: The formatted prompt
        max_tokens: Maximum tokens in response
        
    Returns:
        Generated response text
    """
    # TODO: Part of Exercise 4.3
    # Call the Anthropic API to generate a response
    #
    # Usage:
    # message = client.messages.create(
    #     model="claude-3-5-sonnet-20241022",
    #     max_tokens=max_tokens,
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ]
    # )
    # return message.content[0].text
    #
    # GitHub Copilot Prompt: "Call Anthropic Claude API with a prompt"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def rag_query(question, collection, embedding_model, llm_client, top_k=3):
    """
    Complete RAG pipeline: retrieve → augment → generate.
    
    Args:
        question: User's question
        collection: ChromaDB collection
        embedding_model: SentenceTransformer model
        llm_client: Anthropic client
        top_k: Number of chunks to retrieve
        
    Returns:
        dict with 'answer', 'sources', and 'context_used'
    """
    print(f"\n🔍 Processing query: {question}")
    
    # TODO: Exercise 4.3 - Complete RAG Pipeline
    # 
    # Step 1: Retrieve relevant chunks
    # - Generate query embedding using embedding_model.encode()
    # - Query ChromaDB collection
    # - Get top_k results
    #
    # Step 2: Build the context
    # - Extract chunk texts from results
    # - Combine them appropriately
    #
    # Step 3: Create the prompt
    # - Use build_rag_prompt() with query and context
    #
    # Step 4: Generate response
    # - Call the LLM API using call_llm()
    #
    # Step 5: Return structured result
    # - Return dict with answer, sources, and context
    #
    # GitHub Copilot Prompt: "Implement complete RAG pipeline with retrieval and generation"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def test_rag_system():
    """Test the complete RAG system with sample queries."""
    print("=" * 70)
    print("Part 4: RAG Generation System")
    print("=" * 70)
    print()
    
    # Step 1: Load models and connect to database
    print("🚀 Initializing RAG system...")
    print()
    
    print("  📥 Loading embedding model...")
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    print("  💾 Connecting to vector database...")
    client = chromadb.PersistentClient(path="./chroma_db")
    try:
        collection = client.get_collection(name="cs_knowledge")
        print(f"  ✅ Found {collection.count()} chunks in database")
    except:
        print("  ❌ Database not found. Run part2_embeddings.py first!")
        return
    
    print("  🤖 Initializing LLM...")
    llm_client = initialize_llm()
    
    if llm_client is None:
        print("  ⚠️  No API key found - using mock mode for demonstration")
        print("  💡 To use real LLM: Create .env file with ANTHROPIC_API_KEY")
        print()
        # Continue anyway for testing retrieval
    
    print()
    print("✅ RAG system ready!")
    print("=" * 70)
    print()
    
    # Step 2: Test with sample queries
    test_questions = [
        "What is a variable in programming?",
        "Explain how linked lists work",
        "What are sorting algorithms?",
        "How do databases help with data management?",
    ]
    
    for question in test_questions:
        try:
            result = rag_query(
                question, 
                collection, 
                embedding_model, 
                llm_client,
                top_k=3
            )
            
            if result:
                print("\n" + "=" * 70)
                print(f"❓ Question: {question}")
                print("=" * 70)
                print()
                print("📝 Answer:")
                print(result.get('answer', 'No answer generated'))
                print()
                print(f"📚 Sources: {len(result.get('sources', []))} chunks used")
                print("=" * 70)
            
        except Exception as e:
            print(f"\n❌ Error processing question: {e}")
            print("   Check your implementation and try again")
        
        print()
    
    # Success message
    print()
    print("=" * 70)
    print("🎉 Part 4 Complete!")
    print("=" * 70)
    print()
    print("You've built a complete RAG application! 🚀")
    print()
    print("Next step: Run 'python part5_experiments.py' to analyze RAG vs non-RAG")


def interactive_mode():
    """Interactive mode for asking custom questions."""
    print("\n" + "=" * 70)
    print("💬 Interactive RAG Mode")
    print("=" * 70)
    print("Type your questions (or 'quit' to exit)")
    print()
    
    # Initialize system
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="cs_knowledge")
    llm_client = initialize_llm()
    
    while True:
        question = input("\n❓ Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not question:
            continue
        
        try:
            result = rag_query(question, collection, embedding_model, llm_client)
            if result:
                print(f"\n📝 Answer: {result['answer']}")
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    # Run tests
    test_rag_system()
    
    # Uncomment for interactive mode:
    # interactive_mode()
