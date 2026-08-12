# CLI Coding Agents Lab - Troubleshooting Guide

## Quick Diagnostics

Run the verification script:
```bash
bash verify_setup.sh
```

This will check all prerequisites and highlight any issues.

---

## GitHub Copilot CLI Issues

### Problem: `copilot` command not found

**Symptoms:**
```
bash: copilot: command not found
```

**Solutions:**

**Option 1: Install GitHub Copilot CLI**
```bash
# Requires Node.js v22 or later
node --version  # Check version first

# Install globally
sudo npm install -g @github/copilot

# Verify installation
copilot --version
```

**Option 2: Already installed but not in PATH**
```bash
which copilot
# If found, add npm global bin to PATH
export PATH=$PATH:$(npm bin -g)
```

**Option 3: Install Node.js if needed**
```bash
# On Debian/Ubuntu - install Node.js 22+
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify
node --version
npm --version

# Now install Copilot CLI
sudo npm install -g @github/copilot
```

---

### Problem: GitHub Authentication Failed

**Symptoms:**
```
Authentication error
Invalid token
```

**Solution:**

**1. Create Personal Access Token (PAT):**
- Visit: https://github.com/settings/personal-access-tokens/new
- Name: "Copilot CLI"
- Expiration: 90 days (or your preference)
- Permissions: Enable "Copilot Requests" (under Account permissions)
- Generate token
- Copy token immediately (you won't see it again)

**2. Set environment variable for current session:**
```bash
export GITHUB_TOKEN="github_pat_YOUR_TOKEN_HERE"
```

**3. Make permanent:**
```bash
echo 'export GITHUB_TOKEN="github_pat_YOUR_TOKEN_HERE"' >> ~/.bashrc
source ~/.bashrc
```

**4. Verify:**
```bash
echo $GITHUB_TOKEN
# Should show your token

# Test with Copilot CLI
copilot
```

---

### Problem: Copilot Access Denied

**Symptoms:**
```
You do not have access to GitHub Copilot
Copilot subscription not found
```

**Solutions:**

1. **Check Copilot subscription:**
   - Visit: https://github.com/settings/copilot
   - Ensure you have an active subscription
   - Options:
     - GitHub Copilot Individual ($10/month)
     - GitHub Copilot Business (through organization)
     - Free through GitHub Education (for students)

2. **Verify PAT has Copilot scope:**
   - Visit: https://github.com/settings/tokens
   - Check your token has "Copilot Requests" permission
   - If not, create new token with correct permission

3. **Set the new token:**
```bash
export GITHUB_TOKEN="github_pat_NEW_TOKEN"
echo 'export GITHUB_TOKEN="github_pat_NEW_TOKEN"' >> ~/.bashrc
```

4. **Restart Copilot CLI:**
```bash
# Close any existing session
# Start fresh
copilot
```

---

### Problem: Copilot Responses Slow or Timeout

**Symptoms:**
- Requests take very long
- Timeout errors
- No response

**Solutions:**

1. **Check internet connection:**
```bash
ping github.com
```

2. **Check GitHub API status:**
   - Visit: https://www.githubstatus.com/

3. **Try simpler query:**
```bash
copilot
> Hello
```

4. **Reinstall Copilot CLI:**
```bash
sudo npm uninstall -g @github/copilot
sudo npm install -g @github/copilot
```

5. **Check Node.js version:**
```bash
node --version
# Should be v22 or later
```

---

## Gemini CLI Issues

### Problem: `gemini` command not found

**Symptoms:**
```
bash: gemini: command not found
```

**Solutions:**

**Option 1: Install Google Gemini CLI**
```bash
# Requires Node.js v18 or later
node --version  # Check version first

# Install globally
sudo npm install -g @google/gemini-cli

# Verify installation
gemini --version
```

**Option 2: Already installed but not in PATH**
```bash
which gemini
# If found, add npm global bin to PATH
export PATH=$PATH:$(npm bin -g)
```

**Option 3: Install Node.js if needed**
```bash
# On Debian/Ubuntu - install Node.js 18+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify
node --version
npm --version

# Now install Gemini CLI
sudo npm install -g @google/gemini-cli
```

---

### Problem: Gemini Authentication Failed

**Symptoms:**
```
Authentication error
Please login
API key not set
```

**Solution - Option 1: OAuth Login (Recommended):**

```bash
# Start Gemini CLI
gemini

# Choose "Login with Google" option
# Follow browser authentication flow
# Free tier: 60 requests/minute
```

**Solution - Option 2: API Key:**

1. **Get API Key:**
   - Visit: https://aistudio.google.com/app/apikey
   - Sign in with Google account
   - Click "Create API Key"
   - Copy the key

2. **Set for current session:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

3. **Make permanent:**
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

**Verify:**
```bash
# With OAuth
gemini
# Should start without errors

# With API key
echo $GEMINI_API_KEY
# Should show your key
```

---

### Problem: Gemini Tool Approval Issues

**Symptoms:**
- Agent asks for tool approval but doesn't work
- File operations fail
- Shell commands not executing

**Solutions:**

1. **Approve tool usage carefully:**
```bash
gemini
You: Write this code to test.py
# Agent will ask: "Allow file write?"
# Type: yes
```

2. **Check file permissions:**
```bash
# Ensure directory is writable
ls -la
chmod u+w .
```

3. **Check working directory:**
```bash
# Gemini operates in current directory
pwd
cd /path/to/your/project
gemini
```

---

### Problem: Gemini API Rate Limit

**Symptoms:**
```
Error: 429 Too Many Requests
Rate limit exceeded
```

**Explanation:**

**With OAuth (Recommended):**
- 60 requests per minute
- 1000 requests per day
- Free tier

**With API Key:**
- 100 requests per day
- Lower rate

**Solutions:**

1. **Wait a moment between requests**

2. **Use OAuth instead of API key:**
```bash
gemini
# Choose "Login with Google"
```

3. **Check usage:**
   - Visit: https://aistudio.google.com/
   - View your quota

4. **Upgrade if needed:**
   - Consider paid tier for higher limits

---

### Problem: Gemini Google Search Not Working

**Symptoms:**
- Agent doesn't use Google Search
- No research context in responses

**Solutions:**

1. **Explicitly request research:**
```bash
gemini
You: Research Python async best practices, then help me implement
```

2. **Check internet connection:**
```bash
ping google.com
```

3. **Verify Gemini CLI version:**
```bash
gemini --version
# Should be latest version
npm update -g @google/gemini-cli
```

---

## Python Environment Issues

> ⚠️ **Note:** Both GitHub Copilot CLI and Gemini CLI are npm packages. No Python packages are required for this lab.

If you're seeing Python errors, you may be using old lab materials. See `part2/PYTHON_FILES_DEPRECATED.md`.

### Problem: Wrong Tool Version

**Solution:**

1. **Verify both tools are npm-based:**
```bash
which copilot
which gemini
# Both should be in npm global bin

copilot --version
gemini --version
```

2. **If you see Python wrapper:**
```bash
# Remove old Python package
pip uninstall google-generativeai

# Install official Gemini CLI
sudo npm install -g @google/gemini-cli
```

---

## Common Usage Issues

### Problem: Copilot Not Understanding Requests

**Issue:** Agent doesn't provide expected code or edits

**Solutions:**

1. **Be more specific:**
```bash
copilot
# Instead of:
> fix this

# Try:
> Add type hints to all functions in utils.py
```

2. **Provide file context:**
```bash
> Refactor the calculate_total function in calculator.py to handle edge cases
```

3. **Use iterative refinement:**
```bash
> Create a user class
# Review output
> Add email validation to that class
> Add password hashing method
```

---

### Problem: Gemini Not Understanding Requests

**Issue:** Agent doesn't provide expected code

**Solutions:**

1. **Be more specific:**
```bash
gemini
# Instead of:
> fix this

# Try:
> Research Python async logging best practices, then create an async logger class with proper error handling
```

2. **Request research explicitly:**
```bash
> Use Google Search to find the latest pandas syntax, then show me how to load CSV
```

3. **Ask for tool usage:**
```bash
> Read the files in part2/, then explain what gemini_cli.py does
```

### Problem: Interactive Mode Issues

**Issue:** Gemini CLI interactive session problems

**Solutions:**

1. **Check Node.js version:**
```bash
node --version
# Should be 18+
```

2. **Run directly:**
```bash
gemini
# Should start interactive session
```

3. **Check authentication:**
```bash
# Login with Google
gemini
# Choose authentication option
```

4. **Clear session if stuck:**
```bash
# Exit and restart
Ctrl+C
gemini
```

5. **Don't pipe into interactive mode:**
```bash
# This won't work:
echo "test" | python part2/gemini_cli.py -i

# Use this instead:
python part2/gemini_cli.py -i
```

---

## Network Issues

### Problem: Connection Timeouts

**Symptoms:**
- Requests hang
- Timeout errors

**Solutions:**

1. **Check internet:**
```bash
ping google.com
ping github.com
```

2. **Check firewall:**
```bash
# Ensure HTTPS (port 443) is allowed
```

3. **Try different network:**
   - Switch from VPN if using one
   - Try mobile hotspot

---

### Problem: SSL Certificate Errors

**Symptoms:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Solutions:**

1. **Update certificates:**
```bash
sudo apt update
sudo apt install ca-certificates
```

2. **Check system time:**
```bash
date
# Ensure time is correct
```

---

## Performance Issues

### Problem: Slow Responses

**Causes & Solutions:**

1. **API load:**
   - Try during off-peak hours
   - No fix, just wait

2. **Large context:**
   - Keep queries concise
   - Start new conversation if needed

3. **Network latency:**
   - Check connection speed
   - Use wired connection if possible

---

### Problem: Out of Memory

**Symptoms:**
```
MemoryError or killed process
```

**Solutions:**

1. **Close other applications**
2. **Restart terminal session**
3. **Use smaller contexts**
4. **Clear conversation history:**
```bash
# In Gemini interactive mode:
You: clear
```

---

## Getting More Help

### Check Documentation
- GitHub Copilot: https://docs.github.com/en/copilot
- Gemini API: https://ai.google.dev/docs

### Search for Similar Issues
- GitHub Copilot: https://github.com/github/gh-copilot/issues
- Gemini: https://developers.googleblog.com/

### Ask for Help
- Instructor office hours
- Lab demonstrators
- Class discussion forum

### Debug Mode

Enable verbose output:

**For Copilot CLI:**
```bash
# Check logs in:
cat ~/.config/copilot/logs/*

# Or run with debug environment
DEBUG=* copilot
```

**For Gemini:**
```python
# Add at start of gemini_cli.py
import logging
logging.basicConfig(level=logging.DEBUG)
```
### Daily Checks
```bash
# Quick health check
echo $GITHUB_TOKEN          # Should show token
copilot --version           # Should show version
gemini --version            # Should show version

# Test both agents
copilot                     # Should start
gemini                      # Should start
```

### Keep Tools Updated
```bash
# Update both CLIs
npm update -g @github/copilot
npm update -g @google/gemini-cli

# Check versions
copilot --version
gemini --version

# Update Python packages
pip install --upgrade google-generativeai
```

### Backup Your Work
```bash
# Commit frequently
git add .
git commit -m "Progress checkpoint"
git push
```

---

## Still Having Issues?

If you've tried everything and still have problems:

1. **Document the issue:**
   - Exact error message
   - Commands you ran
2. **Try a minimal example:**
```bash
# Does this work?
copilot --version
copilot  # Then try a simple request

gemini --version
gemini  # Then try a simple request

python part2/gemini_cli.py "hello"
```

3. **Check lab forum** - Others may have same issue

4. **Contact instructor** - Provide documentation from step 1

---

**Remember:** Most issues are:
- Authentication problems (60%)
- Environment setup (25%)
- Network issues (10%)
- Actual bugs (5%)

Work through systematically and you'll find the solution!
