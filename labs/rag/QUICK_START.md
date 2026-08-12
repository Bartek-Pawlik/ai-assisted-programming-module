# Quick Start Guide - RAG Lab

**For Instructors at Atlantic Technological University**

---

## 🚀 Getting Started in 5 Minutes

### Step 1: Review the Lab
1. Open `README.md` - Main student instructions
2. Open `INSTRUCTOR_GUIDE.md` - Comprehensive teaching guide
3. Skim through the 5 parts in `part2_embeddings.py` through `part5_experiments.py`

### Step 2: Test the Lab
```bash
# Clone this repository
cd rag-lab

# Run setup check
python check_setup.py

# Test each part
python test_hello_rag.py
python solutions/part2_embeddings_solution.py
python solutions/part3_retrieval_solution.py
```

### Step 3: Prepare for Students
1. Fork repository to your GitHub organization
2. Share link with students 1 week before
3. (Optional) Set up shared Anthropic API key
4. Review common issues in INSTRUCTOR_GUIDE.md

---

## 📋 Lab Overview

**Duration:** 2 hours  
**Level:** First-year CS students  
**Prerequisites:** Basic Python  
**Tools:** GitHub Codespaces + Copilot

### What Students Build
A complete RAG application that:
- Processes documents into chunks
- Generates vector embeddings
- Stores in vector database (ChromaDB)
- Performs semantic search
- Integrates with LLM (Claude)
- Compares RAG vs non-RAG responses

---

## 📁 Key Files

| File | Purpose | Students Need? |
|------|---------|----------------|
| README.md | Main lab instructions | ✅ READ FIRST |
| INSTRUCTOR_GUIDE.md | Teaching guide | Instructor only |
| requirements.txt | Dependencies | Auto-installed |
| check_setup.py | Environment test | Run first |
| part2-5 .py files | Lab exercises | Complete these |
| solutions/*.py | Complete code | Reference only |
| results.md | Results template | Fill in |

---

## ⏱️ Timeline

| Minutes | Part | What Happens |
|---------|------|--------------|
| 0-15 | Setup | Environment, data loading |
| 15-45 | Part 2 | Embeddings (hardest concept) |
| 45-80 | Part 3 | Retrieval system |
| 80-110 | Part 4 | LLM integration |
| 110-120 | Part 5 | Analysis & comparison |

---

## 🎯 Learning Outcomes

Students will be able to:
- ✅ Explain how RAG works
- ✅ Process documents for retrieval
- ✅ Use vector embeddings
- ✅ Implement semantic search
- ✅ Build a complete RAG pipeline
- ✅ Evaluate RAG effectiveness

---

## 💡 Teaching Tips

### Part 2 (Hardest)
**Concept:** Vector embeddings  
**Tip:** Show concrete examples - print actual arrays!  
**Analogy:** GPS coordinates for ideas

### Part 3 (Most Practical)
**Concept:** Semantic search  
**Tip:** Compare to Google - it finds meaning, not just keywords  
**Demo:** Search for synonyms

### Part 4 (Most Satisfying)
**Concept:** RAG pipeline  
**Tip:** Celebrate when it works - they built a real AI app!  
**Show:** Side-by-side with/without RAG

### Part 5 (Eye-Opening)
**Concept:** Hallucination prevention  
**Tip:** Ask out-of-domain question, see RAG refuse  
**Discuss:** When to use RAG vs other approaches

---

## ⚠️ Common Issues

**"pip install failing"**
→ Use Codespaces (pre-configured)

**"ChromaDB error"**
→ Delete ./chroma_db folder

**"No API key"**
→ Parts 1-3 work without it

**"Embeddings slow"**
→ First run downloads model (~100MB), then fast

**"Don't understand embeddings"**
→ GPS analogy + show actual numbers

---

## 📊 Assessment

**Quick Grading:**
1. Check if each part runs without errors (50%)
2. Review results.md for understanding (30%)
3. Code quality and comments (20%)

**Detailed Rubric:** See INSTRUCTOR_GUIDE.md

---

## 🔧 Customization

**Shorter lab (60 min)?**
→ Do Parts 1-3 only

**Advanced students?**
→ See extension challenges in README.md

**Different domain?**
→ Replace files in data/ directory

---

## 📞 Getting Help

- **Technical issues:** See INSTRUCTOR_GUIDE.md troubleshooting
- **Conceptual questions:** Use analogies in teaching tips
- **Student stuck:** Encourage Copilot use, then show solutions

---

## ✅ Pre-Lab Checklist

**1 Week Before:**
- [ ] Fork repository to your org
- [ ] Test all parts work
- [ ] Share link with students

**1 Day Before:**
- [ ] Remind students to fork repo
- [ ] Check Codespaces enabled
- [ ] Prepare demo environment

**Day Of:**
- [ ] Quick Copilot reminder
- [ ] Emphasize understanding > completion
- [ ] Have solutions ready for reference

---

## 🎬 5-Minute Demo Script

```bash
# Show what they'll build
python test_hello_rag.py          # Load data
python part2_embeddings.py        # Create knowledge base
python part3_retrieval.py         # Test search
python part4_generation.py        # Full RAG!
```

Narrate: "In 2 hours, you'll build this entire RAG system!"

---

## 📈 Success Looks Like

- Students complete all 5 parts
- Understanding shows in results.md
- Able to explain RAG to peers
- Excited about building more AI apps

---

## 🎓 After the Lab

**Immediate:**
- Collect student feedback
- Note common issues for next time

**Follow-Up:**
- Assign extension project
- Connect to next module topic
- Share interesting student solutions

---

## 📚 Additional Resources

**For deeper learning:**
- LlamaIndex docs: https://docs.llamaindex.ai/
- RAG paper: https://arxiv.org/abs/2005.11401
- Anthropic guides: https://docs.anthropic.com/

**For teaching:**
- INSTRUCTOR_GUIDE.md (comprehensive!)
- Solutions directory (working code)
- results.md template (grading guide)

---

**Ready to run the lab? You've got this! 🚀**

Any questions? Check INSTRUCTOR_GUIDE.md for detailed answers.

---

**Created for Atlantic Technological University, Galway**  
**Module:** AI Assisted Programming  
**Target:** First-year Computer Science Students  
**October 2025**
