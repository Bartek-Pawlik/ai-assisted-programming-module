"""
Part 5: Experimentation & Analysis
Atlantic Technological University - RAG Lab

In this part, you will:
1. Compare RAG vs non-RAG responses
2. Experiment with different parameters
3. Document your observations
4. Test hallucination prevention

Estimated time: 10 minutes
"""

from anthropic import Anthropic
import chromadb
from sentence_transformers import SentenceTransformer
from part4_generation import rag_query, initialize_llm
import os
from dotenv import load_dotenv


def query_without_rag(question, llm_client, max_tokens=300):
    """
    Query the LLM without RAG (no context provided).
    
    Args:
        question: User's question
        llm_client: Anthropic client
        max_tokens: Maximum response tokens
        
    Returns:
        LLM response text
    """
    try:
        message = llm_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "user", 
                    "content": f"You are a computer science teaching assistant. Answer this question briefly: {question}"
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        return f"Error: {e}"


def compare_responses(question, rag_response, no_rag_response):
    """Display side-by-side comparison of RAG vs no-RAG."""
    print("\n" + "━" * 80)
    print(f"❓ Question: {question}")
    print("━" * 80)
    print()
    
    print("🤖 WITHOUT RAG (Standard LLM):")
    print("─" * 80)
    print(no_rag_response)
    print("─" * 80)
    print()
    
    print("✅ WITH RAG (Context-Enhanced):")
    print("─" * 80)
    print(rag_response.get('answer', 'No answer'))
    print("─" * 80)
    print()
    
    if rag_response.get('sources'):
        print(f"📚 Sources Used: {len(rag_response['sources'])} chunks from knowledge base")
    print()
    print("━" * 80)


def test_hallucination_prevention():
    """Test if RAG prevents hallucinations on out-of-domain questions."""
    print("\n" + "=" * 80)
    print("🧪 Experiment: Hallucination Prevention")
    print("=" * 80)
    print()
    print("Testing with a question NOT covered in our documents...")
    print()
    
    # Initialize systems
    load_dotenv()
    llm_client = initialize_llm()
    
    if not llm_client:
        print("⚠️  No API key - skipping this experiment")
        return
    
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="cs_knowledge")
    
    # Question NOT in our knowledge base
    out_of_domain_question = "What is quantum computing and how does it work?"
    
    print(f"Question: {out_of_domain_question}")
    print()
    
    # Get both responses
    print("Querying standard LLM...")
    no_rag = query_without_rag(out_of_domain_question, llm_client)
    
    print("Querying RAG system...")
    with_rag = rag_query(
        out_of_domain_question,
        collection,
        embedding_model,
        llm_client,
        top_k=3
    )
    
    # Compare
    compare_responses(out_of_domain_question, with_rag, no_rag)
    
    print("💡 Observation:")
    print("  - Standard LLM: Likely provides a confident answer from training data")
    print("  - RAG system: Should indicate insufficient information in knowledge base")
    print()


def parameter_experiments():
    """Run experiments with different RAG parameters."""
    print("\n" + "=" * 80)
    print("🔬 Experiment: Parameter Tuning")
    print("=" * 80)
    print()
    
    # Initialize
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="cs_knowledge")
    llm_client = initialize_llm()
    
    test_question = "What is a linked list?"
    
    # Experiment 1: Different top-k values
    print("📊 Experiment 1: Number of Retrieved Chunks (top-k)")
    print("-" * 80)
    
    for k in [1, 3, 5]:
        print(f"\nTesting with top_k={k}...")
        
        # Generate query embedding
        query_embedding = embedding_model.encode(test_question)
        
        # Query database
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k
        )
        
        num_results = len(results['documents'][0])
        total_chars = sum(len(doc) for doc in results['documents'][0])
        avg_score = sum(results['distances'][0]) / len(results['distances'][0])
        
        print(f"  Retrieved: {num_results} chunks")
        print(f"  Total context: {total_chars} characters (~{total_chars // 4} tokens)")
        print(f"  Average distance score: {avg_score:.3f}")
    
    print()
    print("💡 Observation: More chunks = more context but also more tokens used")
    print()
    
    # Experiment 2: Chunk size impact (would require re-running Part 2)
    print("📊 Experiment 2: Chunk Size Impact")
    print("-" * 80)
    print("Note: To test this, you would re-run Part 2 with different chunk_size values")
    print("  - Smaller chunks (200-300): More precise retrieval, less context per chunk")
    print("  - Medium chunks (500): Good balance (our current setting)")
    print("  - Larger chunks (1000+): More context per chunk, but less precise")
    print()


def main():
    """Run all experiments."""
    print("=" * 80)
    print("Part 5: Experimentation & Analysis")
    print("=" * 80)
    print()
    
    # Check if we have everything we need
    if not os.path.exists("./chroma_db"):
        print("❌ Vector database not found. Run part2_embeddings.py first!")
        return
    
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("⚠️  No ANTHROPIC_API_KEY found in .env file")
        print("Some experiments require an API key to run.")
        print()
        print("To get an API key:")
        print("1. Go to https://console.anthropic.com/")
        print("2. Create an account (free tier available)")
        print("3. Generate an API key")
        print("4. Create a .env file with: ANTHROPIC_API_KEY=your-key-here")
        print()
        response = input("Continue with limited experiments? (y/n): ")
        if response.lower() != 'y':
            return
        print()
    
    # Run experiments
    try:
        # Experiment 1: Parameter tuning (doesn't require API key)
        parameter_experiments()
        
        # Experiment 2: RAG comparison (requires API key)
        if api_key:
            print("\n" + "=" * 80)
            print("🆚 Experiment: RAG vs Non-RAG Comparison")
            print("=" * 80)
            print()
            
            llm_client = initialize_llm()
            embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            client = chromadb.PersistentClient(path="./chroma_db")
            collection = client.get_collection(name="cs_knowledge")
            
            # Test questions
            test_questions = [
                "What is a variable in programming?",
                "How do sorting algorithms work?",
            ]
            
            for question in test_questions:
                # Get both responses
                no_rag = query_without_rag(question, llm_client)
                with_rag = rag_query(question, collection, embedding_model, llm_client)
                
                # Compare
                compare_responses(question, with_rag, no_rag)
            
            # Test hallucination prevention
            test_hallucination_prevention()
        
        # Final summary
        print("\n" + "=" * 80)
        print("🎉 All Experiments Complete!")
        print("=" * 80)
        print()
        print("Key Takeaways:")
        print("  ✅ RAG provides context-grounded responses")
        print("  ✅ Standard LLMs rely on training data (may be outdated)")
        print("  ✅ RAG can prevent hallucinations by refusing to answer without context")
        print("  ✅ Parameter tuning (top-k, chunk size) affects quality and cost")
        print()
        print("📝 Next step: Document your findings in results.md")
        print()
        
    except Exception as e:
        print(f"\n❌ Error during experiments: {e}")
        print("Check your implementation and try again")


if __name__ == "__main__":
    main()
