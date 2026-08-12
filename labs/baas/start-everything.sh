#!/bin/bash
# Start both frontend and backend servers

echo "🚀 Starting Full 3-Tier Application"
echo "========================================"
echo ""

# Check if GOOGLE_APPLICATION_CREDENTIALS is set
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "⚙️  Setting up Firebase credentials..."
    export GOOGLE_APPLICATION_CREDENTIALS="$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json"
    echo 'export GOOGLE_APPLICATION_CREDENTIALS="$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json"' >> ~/.bashrc
fi

# Check if firebase service account file exists
if [ ! -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "❌ Error: Firebase service account file not found"
    echo "Please complete Part 2 of the README to set up Firebase."
    exit 1
fi

# Check and create .env for frontend if needed
if [ ! -f "$CODESPACE_VSCODE_FOLDER/frontend/.env" ]; then
    echo "⚙️  Creating frontend .env file..."
    cp "$CODESPACE_VSCODE_FOLDER/frontend/.env.example" "$CODESPACE_VSCODE_FOLDER/frontend/.env"
fi

echo "🔧 Starting Backend Server..."
cd "$CODESPACE_VSCODE_FOLDER/backend" || exit 1
uvicorn app.main:app --reload --port 8000 > /tmp/backend.log 2>&1 &
BACKEND_PID=$!
echo "   ✅ Backend started (PID: $BACKEND_PID) on http://localhost:8000"

# Wait a moment for backend to start
sleep 2

echo ""
echo "🎨 Starting Frontend Server..."
cd "$CODESPACE_VSCODE_FOLDER/frontend" || exit 1

# Dynamically set VITE_API_URL for Codespaces
if [ -n "$CODESPACE_NAME" ]; then
    API_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "🌍 Codespaces detected: Writing VITE_API_URL to .env.local"
    echo "VITE_API_URL=$API_URL" > "$CODESPACE_VSCODE_FOLDER/frontend/.env.local"
fi

npm run dev -- --host > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!

# Wait for frontend to start and capture the actual port
sleep 3
FRONTEND_URL=$(grep -o "http://localhost:[0-9]*" /tmp/frontend.log | head -1)
if [ -z "$FRONTEND_URL" ]; then
    FRONTEND_URL="http://localhost:5173"
fi

echo "   ✅ Frontend started (PID: $FRONTEND_PID) on $FRONTEND_URL"
if [ -n "$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN" ] && [ -n "$CODESPACE_NAME" ]; then
    PORT=$(echo "$FRONTEND_URL" | cut -d":" -f3)
    FORWARDED="http://$PORT-$CODESPACE_NAME.$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN"
    echo "   🔗 Codespaces forwarded: $FORWARDED"
fi

echo ""
echo "========================================"
echo "✅ All servers started!"
echo "========================================"
echo ""
echo "📱 Frontend: $FRONTEND_URL"
echo "⚙️  Backend:  http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "📋 Process IDs:"
echo "   Backend:  $BACKEND_PID"
echo "   Frontend: $FRONTEND_PID"
echo ""
echo "💡 Tips:"
echo "   - View backend logs:  tail -f /tmp/backend.log"
echo "   - View frontend logs: tail -f /tmp/frontend.log"
echo "   - Stop all servers:   ./stop-everything.sh"
echo "   - Verify setup:       ./verify-setup.sh"
echo ""
echo "🌐 Open your app. Hold down the **ctrl** key and click on this link: $FRONTEND_URL"
echo ""

# Save PIDs for later cleanup
echo $BACKEND_PID > /tmp/backend.pid
echo $FRONTEND_PID > /tmp/frontend.pid
