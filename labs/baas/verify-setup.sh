#!/bin/bash
# Verify the 3-tier architecture setup

echo "🔍 Verifying 3-Tier Architecture Setup"
echo "========================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

errors=0

# 1. Check Backend Dependencies
echo "📦 [1/9] Checking Backend Dependencies..."
if [ -d "$CODESPACE_VSCODE_FOLDER/backend" ]; then
    cd "$CODESPACE_VSCODE_FOLDER/backend" || exit 1
    if python -c "import fastapi, uvicorn, firebase_admin" 2>/dev/null; then
        echo -e "${GREEN}✅ Backend Python packages installed${NC}"
    else
        echo -e "${RED}❌ Backend dependencies missing. Run: cd backend && pip install -r requirements.txt${NC}"
        ((errors++))
    fi
else
    echo -e "${RED}❌ Backend directory not found${NC}"
    ((errors++))
fi
echo ""

# 2. Check Frontend Dependencies
echo "📦 [2/9] Checking Frontend Dependencies..."
if [ -d "$CODESPACE_VSCODE_FOLDER/frontend/node_modules" ]; then
    echo -e "${GREEN}✅ Frontend node_modules installed${NC}"
else
    echo -e "${RED}❌ Frontend dependencies missing. Run: cd frontend && npm install${NC}"
    ((errors++))
fi
echo ""

# 3. Check Firebase Service Account
echo "🔥 [3/9] Checking Firebase Service Account..."
if [ -f "$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json" ]; then
    echo -e "${GREEN}✅ Firebase service account file exists${NC}"
else
    echo -e "${RED}❌ Firebase service account file missing${NC}"
    echo -e "${YELLOW}   Complete Part 2 of README to set up Firebase${NC}"
    ((errors++))
fi
echo ""

# 4. Check Environment Variable
echo "⚙️  [4/9] Checking GOOGLE_APPLICATION_CREDENTIALS..."
if [ -n "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo -e "${GREEN}✅ GOOGLE_APPLICATION_CREDENTIALS is set${NC}"
    echo "   Path: $GOOGLE_APPLICATION_CREDENTIALS"
else
    echo -e "${YELLOW}⚠️  GOOGLE_APPLICATION_CREDENTIALS not set${NC}"
    echo -e "${YELLOW}   Run: export GOOGLE_APPLICATION_CREDENTIALS=\"\$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json\"${NC}"
fi
echo ""

# 5. Check Frontend .env file
echo "⚙️  [5/9] Checking Frontend .env file..."
if [ -f "$CODESPACE_VSCODE_FOLDER/frontend/.env" ]; then
    echo -e "${GREEN}✅ Frontend .env file exists${NC}"
else
    echo -e "${YELLOW}⚠️  Frontend .env file missing${NC}"
    echo -e "${YELLOW}   Creating from .env.example...${NC}"
    if [ -f "$CODESPACE_VSCODE_FOLDER/frontend/.env.example" ]; then
        cp "$CODESPACE_VSCODE_FOLDER/frontend/.env.example" "$CODESPACE_VSCODE_FOLDER/frontend/.env"
        echo -e "${GREEN}✅ Created .env file${NC}"
    fi
fi
echo ""

# 6. Check Backend Server
echo "🌐 [6/9] Checking Backend Server (port 8000)..."
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    response=$(curl -s http://localhost:8000/health)
    echo -e "${GREEN}✅ Backend server is running${NC}"
    echo "   Response: $response"
else
    echo -e "${YELLOW}⚠️  Backend server not running${NC}"
    echo -e "${YELLOW}   Start it with: ./start-backend.sh${NC}"
fi
echo ""

# 7. Check Frontend Server
echo "🌐 [7/9] Checking Frontend Server (port 5173)..."
if curl -s http://localhost:5173 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Frontend server is running on port 5173${NC}"
elif curl -s http://localhost:5174 > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Frontend server is running on port 5174${NC}"
else
    echo -e "${YELLOW}⚠️  Frontend server not running${NC}"
    echo -e "${YELLOW}   Start it with: ./start-frontend.sh${NC}"
fi
echo ""

# 8. Test Backend API
echo "🔌 [8/9] Testing Backend API Endpoints..."
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    # Test GET /notes
    if curl -s http://localhost:8000/notes > /dev/null 2>&1; then
        note_count=$(curl -s http://localhost:8000/notes | python3 -c "import sys, json; print(len(json.load(sys.stdin)))" 2>/dev/null || echo "?")
        echo -e "${GREEN}✅ GET /notes working ($note_count notes in database)${NC}"
    else
        echo -e "${RED}❌ GET /notes failed${NC}"
        ((errors++))
    fi
else
    echo -e "${YELLOW}⚠️  Cannot test API (backend not running)${NC}"
fi
echo ""

# 9. Check Firestore Connection
echo "🔥 [9/9] Testing Firestore Connection..."
if [ -f "$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json" ] && [ -n "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    if curl -s http://localhost:8000/notes > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Firestore connection working${NC}"
    else
        echo -e "${YELLOW}⚠️  Cannot verify Firestore (backend not running)${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  Cannot verify Firestore (credentials not configured)${NC}"
fi
echo ""

# Summary
echo "========================================"
echo "📊 SUMMARY"
echo "========================================"
if [ $errors -eq 0 ]; then
    echo -e "${GREEN}✅ All critical checks passed!${NC}"
    echo ""
    echo "🎉 Your 3-tier architecture is ready:"
    echo "   📱 Frontend: http://localhost:5173"
    echo "   ⚙️  Backend:  http://localhost:8000"
    echo "   🔥 Database: Firebase Firestore"
    echo ""
    echo "If servers aren't running, start them with:"
    echo "   ./start-backend.sh   (in one terminal)"
    echo "   ./start-frontend.sh  (in another terminal)"
else
    echo -e "${RED}❌ Found $errors error(s)${NC}"
    echo ""
    echo "Please fix the errors above before proceeding."
    echo "See README.md for detailed setup instructions."
fi
echo ""
