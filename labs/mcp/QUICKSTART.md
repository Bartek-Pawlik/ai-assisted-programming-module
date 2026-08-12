# Quick Start Guide

## For Students

### Setup (5 minutes)
```bash
# 1. You already have this lab — it is in your copy of the module repo.
#    Open a Codespace on your copy, then:
cd labs/mcp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify installation
python -c "import mcp; print('✅ Ready to go!')"
```

### Part 1: Calculator (30 minutes)
```bash
cd part1

# Optional: Start with visual demo (recommended!)
"$BROWSER" mcp_demo.html  # Interactive MCP protocol visualization

# Then run the code demo
python mcp_client.py
```
Watch the colored JSON-RPC traffic, then add a `power` tool.

### Part 2: Weather (40 minutes)
```bash
cd part2
python mcp_client_weather.py
```
Learn external API integration, then add sunrise/sunset tool.

**Bonus:** Connect your weather server to GitHub Copilot and chat with it!

### Part 3: News Server (40 minutes)
```bash
cd part3_student_exercise
# Edit student_news_mcp_server.py
python student_news_mcp_client.py
```
Build your own server from scratch!

## For Instructors

### Before Class
```bash
# Test all parts
cd part1 && python mcp_client.py
cd ../part2 && python mcp_client_weather.py
cd ../solutions && python solution_news_mcp_client.py
```

### During Class
1. Demo Part 1 (5 min)
2. Students do Part 1 (30 min)
3. Demo Part 2 (5 min)
4. Students do Part 2 (40 min)
5. Students do Part 3 (40 min)

### Solutions
All solution files are in the `solutions/` directory.

## Need Help?
- Check `INSTRUCTOR_NOTES.md` for detailed guidance
- See part-specific README files in each directory
- Review the main `README.md` for full documentation

## Quick Commands

**Test everything:**
```bash
# Part 1
cd part1 && python mcp_client.py && cd ..

# Part 2  
cd part2 && python mcp_client_weather.py && cd ..

# Solution
cd solutions && python solution_news_mcp_client.py && cd ..
```

**Validate student work:**
```bash
cd part3_student_exercise
python student_news_mcp_client.py
```

**Check dependencies:**
```bash
pip list | grep mcp
```

That's it! You're ready to run the lab. 🚀
