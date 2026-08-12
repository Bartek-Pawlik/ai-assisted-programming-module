"""
Part 3: Retrieval System
Atlantic Technological University - RAG Lab

In this part, you will:
1. Implement semantic search
2. Add relevance filtering
3. Manage context windows
4. Test retrieval with queries

Estimated time: 35 minutes
"""

import chromadb
from sentence_transformers import SentenceTransformer


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
    # TODO: Exercise 3.1
    # 1. Generate embedding for the query using model.encode()
    # 2. Query the ChromaDB collection with the query embedding
    # 3. Extract and return the results as (text, score) tuples
    #
    # ChromaDB query usage:
    # results = collection.query(
    #     query_embeddings=[query_embedding.tolist()],
    #     n_results=top_k
    # )
    #
    # Results structure:
    # results['documents'][0] = list of document texts
    # results['distances'][0] = list of distance scores (lower = more similar)
    #
    # GitHub Copilot Prompt: "Query ChromaDB collection with embedding and return top k results"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def filter_by_relevance(results, min_score=0.5):
    """
    Filter search results by minimum relevance score.
    
    Args:
        results: List of (chunk, distance) tuples
        min_score: Minimum similarity score threshold
        
    Returns:
        Filtered list of results
        
    Note: ChromaDB returns DISTANCE scores (lower = more similar)
          We'll convert to similarity: similarity = 1 / (1 + distance)
          Then filter by min_score
    """
    # TODO: Exercise 3.2
    # 1. Convert distance scores to similarity scores using: 1 / (1 + distance)
    # 2. Filter results where similarity >= min_score
    # 3. Return filtered results as (chunk, similarity_score) tuples
    #
    # GitHub Copilot Prompt: "Convert distance scores to similarity and filter by threshold"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def manage_context_window(chunks, max_tokens=1500):
    """
    Combine chunks while staying within token limit.
    
    Args:
        chunks: List of text chunks
        max_tokens: Maximum tokens to use (approximate)
        
    Returns:
        Combined context string that fits within token limit
    """
    # TODO: Exercise 3.3
    # 1. Combine chunks with clear separators (e.g., "\n\n---\n\n")
    # 2. Estimate token count (rough estimate: 4 characters ≈ 1 token)
    # 3. If exceeds max_tokens, truncate to fit
    # 4. Return the combined context
    #
    # Algorithm:
    # - Start with empty context
    # - Add chunks one by one with separator
    # - Check token estimate after each addition
    # - Stop when max_tokens would be exceeded
    #
    # GitHub Copilot Prompt: "Combine text chunks with separators staying within token limit"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def display_results(query, results):
    """Display search results in a nice format."""
    print("=" * 70)
    print(f"🔍 Query: {query}")
    print("=" * 70)
    print()
    
    if not results:
        print("❌ No results found")
        return
    
    for i, (chunk, score) in enumerate(results, 1):
        # Convert distance to similarity for display
        similarity = 1 / (1 + score) if isinstance(score, float) else score
        
        print(f"Result #{i}")
        print(f"Similarity Score: {similarity:.3f}")
        print(f"Text Preview: {chunk[:200]}...")
        print("-" * 70)
        print()


def main():
    """Run retrieval system tests."""
    print("=" * 70)
    print("Part 3: Retrieval System")
    print("=" * 70)
    print()
    
    # Load the embedding model
    print("🧮 Loading embedding model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Model loaded")
    print()
    
    # Connect to ChromaDB
    print("💾 Connecting to ChromaDB...")
    client = chromadb.PersistentClient(path="./chroma_db")
    
    try:
        collection = client.get_collection(name="cs_knowledge")
        print(f"✅ Connected to collection with {collection.count()} chunks")
    except:
        print("❌ Collection not found. Run part2_embeddings.py first!")
        return
    print()
    
    # Test queries
    test_queries = [
        "What is a variable in programming?",
        "How do linked lists work?",
        "Explain sorting algorithms",
        "What are databases used for?",
        "What is HTML?"
    ]
    
    print("🔍 Testing semantic search...")
    print()
    
    for query in test_queries:
        # Perform search
        results = semantic_search(query, collection, model, top_k=3)
        
        if results:
            # Display results
            display_results(query, results)
            
            # Test relevance filtering
            filtered = filter_by_relevance(results, min_score=0.5)
            print(f"   After filtering (min_score=0.5): {len(filtered)} results")
            
            # Test context window management
            chunks_only = [chunk for chunk, _ in results]
            context = manage_context_window(chunks_only, max_tokens=500)
            
            if context:
                token_estimate = len(context) // 4
                print(f"   Context window: ~{token_estimate} tokens")
            
            print()
            print("─" * 70)
            print()
        else:
            print(f"❌ No results for: {query}")
            print("   Check your semantic_search() function")
            print()
    
    # Final summary
    print("=" * 70)
    print("🎉 Part 3 Complete!")
    print("=" * 70)
    print()
    print("Your retrieval system can:")
    print("  ✅ Perform semantic search")
    print("  ✅ Filter by relevance")
    print("  ✅ Manage context windows")
    print()
    print("Next step: Run 'python part4_generation.py' to integrate with an LLM")


if __name__ == "__main__":
    main()
