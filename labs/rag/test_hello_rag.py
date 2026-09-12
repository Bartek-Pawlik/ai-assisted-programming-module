"""
Hello RAG! - Simple Test Script
RAG Lab

This script loads and displays a sample document to verify basic file operations work.
"""

import os


def load_sample_document():
    """Load and display a sample document."""
    filepath = os.path.join("data", "introduction_to_programming.txt")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("=" * 60)
        print("📄 Loaded document: introduction_to_programming.txt")
        print("=" * 60)
        print()
        print(f"📊 Document length: {len(content)} characters")
        print(f"📊 Document word count: {len(content.split())} words")
        print()
        print("First 300 characters:")
        print("-" * 60)
        print(content[:300] + "...")
        print("-" * 60)
        print()
        print("✅ Setup complete! You're ready to start Part 2.")
        print("=" * 60)
        
        return content
        
    except FileNotFoundError:
        print("❌ Error: Could not find the data file.")
        print("💡 Make sure you're running this script from the rag-lab directory.")
        return None


if __name__ == "__main__":
    load_sample_document()
