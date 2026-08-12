"""
Setup Verification Script
Atlantic Technological University - RAG Lab

Run this script to verify your environment is correctly configured.
"""

import sys


def check_python_version():
    """Check if Python version is 3.11 or higher."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 11:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} detected. Please use Python 3.11+")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    required_packages = [
        "sentence_transformers",
        "chromadb",
        "anthropic",
        "dotenv"
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            all_installed = False
    
    return all_installed


def check_data_files():
    """Check if sample data files exist."""
    import os
    
    data_files = [
        "introduction_to_programming.txt",
        "data_structures_basics.txt",
        "algorithms_overview.txt",
        "database_fundamentals.txt",
        "web_development_intro.txt"
    ]
    
    all_exist = True
    for filename in data_files:
        filepath = os.path.join("data", filename)
        if os.path.exists(filepath):
            print(f"✅ {filename} found")
        else:
            print(f"❌ {filename} NOT found")
            all_exist = False
    
    return all_exist


def main():
    """Run all setup checks."""
    print("=" * 60)
    print("RAG Lab - Environment Setup Checker")
    print("=" * 60)
    print()
    
    print("🔍 Checking Python version...")
    python_ok = check_python_version()
    print()
    
    print("📦 Checking dependencies...")
    deps_ok = check_dependencies()
    print()
    
    print("📄 Checking data files...")
    data_ok = check_data_files()
    print()
    
    print("=" * 60)
    if python_ok and deps_ok and data_ok:
        print("🎉 All checks passed! You're ready to start the lab!")
    else:
        print("⚠️  Some checks failed. Please review the errors above.")
        print("\n💡 To install dependencies, run: pip install -r requirements.txt")
    print("=" * 60)


if __name__ == "__main__":
    main()
