"""
Part 2: Document Processing & Embeddings
Atlantic Technological University - RAG Lab

In this part, you will:
1. Load documents from the data directory
2. Split documents into chunks
3. Generate vector embeddings
4. Store embeddings in ChromaDB

Estimated time: 30 minutes
"""

import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings


def load_documents(data_dir="data"):
    """
    Load all .txt files from the data directory.
    
    Args:
        data_dir: Path to directory containing text files
        
    Returns:
        List of (filename, content) tuples
    """
    documents = []
    
    # TODO: Exercise 2.1
    # Use os.listdir() to get all files in data_dir
    # Filter for .txt files only
    # Read each file and append (filename, content) tuple to documents list
    # 
    # Hints:
    # - Use os.path.join() to create full file paths
    # - Use .endswith('.txt') to filter for text files
    # - Use 'with open(filepath, 'r', encoding='utf-8')' to read files
    #
    # GitHub Copilot Prompt: "Read all text files from a directory and return list of tuples"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code
    
    return documents


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
    
    # TODO: Exercise 2.2
    # Split text into chunks of chunk_size characters
    # Add overlap between chunks to maintain context
    # 
    # Algorithm:
    # 1. Start at position 0
    # 2. Extract chunk from position to position + chunk_size
    # 3. Add chunk to list
    # 4. Move position forward by (chunk_size - overlap)
    # 5. Repeat until text is exhausted
    #
    # GitHub Copilot Prompt: "Split text into overlapping chunks with specified size and overlap"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code
    
    return chunks


def generate_embeddings(chunks, model_name="all-MiniLM-L6-v2"):
    """
    Generate vector embeddings for text chunks.
    
    Args:
        chunks: List of text chunks
        model_name: Name of the sentence-transformer model
        
    Returns:
        numpy array of embedding vectors
    """
    print(f"🧮 Loading embedding model: {model_name}...")
    
    # TODO: Exercise 2.3
    # 1. Load the SentenceTransformer model using model_name
    # 2. Use model.encode() to generate embeddings for all chunks
    # 3. Return the embeddings
    #
    # Note: model.encode() can take a list of strings and return all embeddings at once!
    #
    # GitHub Copilot Prompt: "Use sentence-transformers to encode a list of text chunks"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


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
    # TODO: Exercise 2.4
    # 1. Initialize ChromaDB client (use PersistentClient for saving to disk)
    # 2. Delete collection if it exists (to start fresh each time)
    # 3. Create a new collection with the specified name
    # 4. Add documents to the collection with their embeddings
    #
    # ChromaDB usage:
    # - Client: chromadb.PersistentClient(path="./chroma_db")
    # - Delete: client.delete_collection(name=collection_name) [wrap in try/except]
    # - Create: client.create_collection(name=collection_name)
    # - Add: collection.add(
    #           documents=chunks,
    #           embeddings=embeddings.tolist(),
    #           ids=[f"chunk_{i}" for i in range(len(chunks))]
    #        )
    #
    # GitHub Copilot Prompt: "Store text chunks and embeddings in a ChromaDB collection"
    
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


def main():
    """Run the complete Part 2 pipeline."""
    print("=" * 70)
    print("Part 2: Document Processing & Embeddings")
    print("=" * 70)
    print()
    
    # Step 1: Load documents
    print("📚 Loading documents...")
    documents = load_documents("data")
    
    if not documents:
        print("❌ No documents loaded. Check your load_documents() function.")
        return
    
    print(f"✅ Loaded {len(documents)} documents")
    for filename, _ in documents:
        print(f"   - {filename}")
    print()
    
    # Step 2: Chunk documents
    print("✂️  Chunking documents...")
    all_chunks = []
    chunk_metadata = []  # Track which document each chunk came from
    
    for filename, content in documents:
        chunks = chunk_text(content, chunk_size=500, overlap=50)
        all_chunks.extend(chunks)
        chunk_metadata.extend([filename] * len(chunks))
    
    if not all_chunks:
        print("❌ No chunks created. Check your chunk_text() function.")
        return
    
    print(f"✅ Created {len(all_chunks)} chunks")
    print(f"   Average chunk size: {sum(len(c) for c in all_chunks) // len(all_chunks)} characters")
    print()
    
    # Step 3: Generate embeddings
    print("🧮 Generating embeddings...")
    embeddings = generate_embeddings(all_chunks)
    
    if embeddings is None:
        print("❌ No embeddings generated. Check your generate_embeddings() function.")
        return
    
    print(f"✅ Generated {len(embeddings)} embeddings")
    print(f"   Embedding dimensions: {len(embeddings[0])}")
    print()
    
    # Step 4: Store in ChromaDB
    print("💾 Storing in ChromaDB...")
    collection = store_in_chromadb(all_chunks, embeddings)
    
    if collection is None:
        print("❌ Failed to create collection. Check your store_in_chromadb() function.")
        return
    
    print(f"✅ Stored {collection.count()} chunks in vector database")
    print()
    
    # Success!
    print("=" * 70)
    print("🎉 Part 2 Complete! Your knowledge base is ready!")
    print("=" * 70)
    print()
    print("Next step: Run 'python part3_retrieval.py' to build the retrieval system")


if __name__ == "__main__":
    main()
