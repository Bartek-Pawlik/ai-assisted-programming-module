# AI Coding Agents Lab - Quick Start Guide

## 🎯 Lab Goals
By the end of this lab, you'll understand:
1. The three modes of GitHub Copilot (Ask, Edit, Agent)
2. How cloud coding agents work autonomously
3. Differences between GitHub Copilot and Google Jules
4. When to use each type of AI agent
5. How to verify and trust AI-generated code

---

## ⏱️ Time Allocation (Total: 2 hours)

| Part | Topic | Time | Type |
|------|-------|------|------|
| Part 1 | Ask Mode | 20 min | Hands-on |
| Part 2 | Edit Mode | 25 min | Hands-on |
| Part 3 | Agent Mode | 25 min | Hands-on |
| Part 4 | Cloud Agent | 30 min | Async |
| Part 5 | Google Jules | 20 min | Hands-on |

---

## 📋 Prerequisites Checklist

Before starting:
- [ ] GitHub Codespaces environment running
- [ ] GitHub Copilot active (check status bar)
- [ ] Copilot Chat accessible (`Ctrl+Alt+I`)
- [ ] All lab files present

---

## 🗺️ Navigation Guide

```
/
├── README.md                 ← Start here
├── LAB_GUIDE.md             ← You are here!
├── requirements.txt         ← Python dependencies
│
├── part1_ask_mode/          ← Ask Mode (20 min)
│   ├── README.md           ← Instructions
│   ├── mystery_code.py     ← Exercise 1.1
│   ├── buggy_code.py       ← Exercise 1.3
│   └── grades.csv          ← Sample data
│
├── part2_edit_mode/         ← Edit Mode (25 min)
│   ├── README.md
│   ├── validators.py       ← Exercise 2.1 (empty)
│   ├── messy_code.py       ← Exercise 2.2
│   └── broken_calculator.py ← Exercise 2.3
│
├── part3_agent_mode/        ← Agent Mode (25 min)
│   └── README.md           ← Instructions
│
├── part4_cloud_agent/       ← Cloud Agent (30 min)
│   └── README.md
│
└── part5_google_jules/      ← Google Jules (20 min)
    └── README.md
```

---

## 🚀 Quick Start (5 minutes)

### Step 1: Verify Setup
```bash
# Check Python
python --version

# Check Copilot status
# Look at bottom-right of VS Code - should see Copilot icon
```

### Step 2: Test Copilot
1. Press `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac)
2. Type: "Hello, are you working?"
3. You should get a response

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Start Part 1
```bash
cd part1_ask_mode
# Open README.md and follow instructions
```

---

## ⌨️ Essential Keyboard Shortcuts

| Action | Windows/Linux | Mac | Description |
|--------|--------------|-----|-------------|
| **Copilot Chat** | `Ctrl+Alt+I` | `Cmd+Alt+I` | Open Ask mode |
| **Inline Copilot** | `Ctrl+I` | `Cmd+I` | Open Edit mode |
| **Copilot Edits** | `Ctrl+Shift+I` | `Cmd+Shift+I` | Open Agent mode |
| **Accept** | `Ctrl+Enter` | `Cmd+Enter` | Accept suggestion |
| **Reject** | `Esc` | `Esc` | Reject suggestion |
| **Command Palette** | `Ctrl+Shift+P` | `Cmd+Shift+P` | All VS Code commands |

---

## 🎯 Learning Objectives by Part

### Part 1: Ask Mode
**Learn:** How to use Copilot for learning and understanding
- ✓ Get code explanations
- ✓ Learn new concepts
- ✓ Debug assistance
- ✓ Best practices

**Key Skill:** Asking effective questions

---

### Part 2: Edit Mode
**Learn:** Direct code generation and modification
- ✓ Generate new code
- ✓ Refactor existing code
- ✓ Fix bugs
- ✓ Multi-file edits

**Key Skill:** Writing clear instructions

---

### Part 3: Agent Mode
**Learn:** Autonomous multi-step tasks
- ✓ Complex features
- ✓ Multi-file changes
- ✓ Running tests
- ✓ Iterative debugging

**Key Skill:** Planning and delegation

---

### Part 4: Cloud Coding Agent
**Learn:** Asynchronous autonomous development
- ✓ Trigger cloud agents
- ✓ Review PRs
- ✓ Provide feedback
- ✓ Iterate on changes

**Key Skill:** Code review and trust

---

### Part 5: Google Jules
**Learn:** Alternative AI coding agent
- ✓ Issue-driven workflow
- ✓ Comparison with Copilot
- ✓ When to use what
- ✓ Critical evaluation

**Key Skill:** Tool selection

---

## 💡 Tips for Success

### General Tips
1. **Read instructions carefully** before starting each exercise
2. **Don't rush** - understanding is more important than speed
3. **Annotate your code** with what you learn as you go
4. **Test all generated code** before moving on
5. **Ask for help** if you get stuck

### Ask Mode Tips
- ✅ Be specific in your questions
- ✅ Ask follow-up questions
- ✅ Request examples
- ❌ Don't blindly trust answers

### Edit Mode Tips
- ✅ Review all generated code
- ✅ Test before accepting
- ✅ Iterate with refinements
- ❌ Don't accept without understanding

### Agent Mode Tips
- ✅ Provide detailed requirements
- ✅ Let it work autonomously
- ✅ Review thoroughly after
- ❌ Don't use for critical security code

### Cloud Agent Tips
- ✅ Write comprehensive task descriptions
- ✅ Review PRs carefully
- ✅ Test locally if possible
- ❌ Don't merge without review

---

## 🐛 Common Issues & Solutions

### Issue: Copilot Not Responding
**Symptoms:** Chat is empty or suggestions aren't appearing
**Solutions:**
1. Check Copilot icon in status bar (bottom-right)
2. Sign out and sign back in to GitHub
3. Reload VS Code window (`Ctrl+Shift+P` → "Reload Window")
4. Check internet connection

### Issue: Cloud Agent Doesn't Start
**Symptoms:** No branch created or PR appeared
**Solutions:**
1. Verify you used the exact tag: `#github-pull-request_copilot-coding-agent`
2. Check repository permissions
3. Wait longer (can take 10-30 minutes)
4. Check GitHub Actions logs

### Issue: Jules Not Available
**Symptoms:** Can't assign Jules to issue
**Solutions:**
1. Jules may not be available in all organizations
2. Use alternative exercise in Part 5 README
3. Document observations about the different workflows
4. Compare with your Copilot Cloud Agent experience

### Issue: Code Has Errors
**Symptoms:** Generated code doesn't run
**Solutions:**
1. This is expected! Review and fix errors
2. Ask Copilot to fix the issues
3. Debug step by step
4. Document what you learn

---

## ✅ Progress Tracker

Use this to track your progress:

### Part 1: Ask Mode
- [ ] Exercise 1.1: Code Explanation
- [ ] Exercise 1.2: Learning Concepts
- [ ] Exercise 1.3: Debugging Assistant
- [ ] Code annotated with learnings

### Part 2: Edit Mode
- [ ] Exercise 2.1: Code Generation
- [ ] Exercise 2.2: Refactoring
- [ ] Exercise 2.3: Bug Fixing
- [ ] Code samples saved

### Part 3: Agent Mode
- [ ] Exercise 3.1: Multi-step Implementation
- [ ] Exercise 3.2: Bug Investigation
- [ ] All generated files reviewed

### Part 4: Cloud Coding Agent
- [ ] Exercise 4.1: Triggered cloud agent
- [ ] Exercise 4.2: Reviewed PR
- [ ] Exercise 4.3: Iterated with agent

### Part 5: Google Jules
- [ ] Exercise 5.1: Created issue
- [ ] Exercise 5.2: Assigned Jules (or alternative)
- [ ] Exercise 5.3: Reviewed PR

### Lab Complete
- [ ] All 5 parts completed
- [ ] Code tested and working
- [ ] Exercises understood
- [ ] Ready to discuss in class!

---

## 🎓 Learning Outcomes

After completing this lab, you should be able to:

1. **Distinguish** between different AI coding agent modes
2. **Select** the appropriate agent for different tasks
3. **Use** GitHub Copilot effectively in all three modes
4. **Trigger** and manage cloud coding agents
5. **Compare** different AI coding tools through hands-on experience
6. **Review** AI-generated code properly
7. **Verify** code quality and security
8. **Understand** limitations of AI agents
9. **Apply** AI agents to real development tasks
10. **Work** effectively with autonomous coding agents

---

## 📚 Additional Resources

### GitHub Copilot
- [Official Documentation](https://docs.github.com/en/copilot)
- [Copilot Chat Guide](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [Prompt Engineering Tips](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

### Google Jules
- [Jules Announcement](https://developers.googleblog.com/en/introducing-jules-ai-powered-code-agent/)
- [Jules Documentation](https://developers.google.com/jules)

### AI Coding in General
- [AI Pair Programming Best Practices](https://martinfowler.com/articles/ai-assisted-programming.html)
- [GitHub Blog on AI Agents](https://github.blog/2024-01-22-the-rise-of-ai-coding-agents/)

---

## ❓ Frequently Asked Questions

**Q: What if I don't have access to GitHub Copilot?**
A: You need Copilot access for this lab. Check with your instructor about obtaining access through GitHub Education.

**Q: Can I use ChatGPT or other AI tools?**
A: The lab is designed for GitHub Copilot specifically to give you hands-on experience with integrated development agents.

**Q: What if the cloud agent takes too long?**
A: Cloud agents can take 10-30 minutes. Start that part early and work on other parts while waiting.

**Q: Is Jules required?**
A: If Jules isn't available, use the alternative exercise in Part 5 to compare workflows and approaches.

**Q: How much code do I need to write myself?**
A: The goal is to use AI agents, but you must understand and verify all code. You should be able to explain how everything works.

**Q: Can I work with a partner?**
A: Yes! Feel free to work together and help each other learn. Discussion and collaboration are encouraged.

**Q: What if I find bugs in the lab materials?**
A: Great! Let the instructor know so we can fix them for everyone.

---

## 🏆 Success Criteria

You'll know you're successful when:
- ✅ You can explain when to use each Copilot mode
- ✅ You've successfully triggered a cloud coding agent
- ✅ You understand the differences between AI agents through hands-on use
- ✅ You understand how to verify AI-generated code
- ✅ You have concrete examples from hands-on practice
- ✅ You can apply AI agents to solve real coding problems
- ✅ Your code is working and you understand how it was generated

---

## 🎯 Next Steps

1. **Start with Part 1** - Read `part1_ask_mode/README.md`
2. **Follow each part sequentially** - They build on each other
3. **Annotate your code** - Document what you learn
4. **Test everything** - Make sure code works
5. **Ask questions** - When you get stuck
6. **Experiment** - Try different approaches
7. **Have fun!** 🎉 - Explore AI coding agents

---

**Good luck! Remember: The goal is learning, not perfection. Enjoy exploring AI coding agents! 🚀**
