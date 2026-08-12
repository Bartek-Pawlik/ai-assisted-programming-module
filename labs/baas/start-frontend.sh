#!/bin/bash
# Start the React frontend development server

echo "🚀 Starting React Frontend Server..."
echo ""

# Check if node_modules exists
if [ ! -d "$CODESPACE_VSCODE_FOLDER/frontend/node_modules" ]; then
    echo "📦 Installing dependencies first..."
    cd "$CODESPACE_VSCODE_FOLDER/frontend" || exit 1
    npm install
    echo ""
fi

# Check if .env exists, if not create it from .env.example
if [ ! -f "$CODESPACE_VSCODE_FOLDER/frontend/.env" ]; then
    echo "⚙️  Creating .env file from .env.example..."
    cp "$CODESPACE_VSCODE_FOLDER/frontend/.env.example" "$CODESPACE_VSCODE_FOLDER/frontend/.env"
    echo "✅ .env file created"
fi

echo "📍 Starting server (will be at http://localhost:5173 or similar)"
echo ""

cd "$CODESPACE_VSCODE_FOLDER/frontend" || exit 1

# Dynamically set VITE_API_URL for Codespaces
if [ -n "$CODESPACE_NAME" ]; then
    API_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "🌍 Codespaces detected: Writing VITE_API_URL to .env.local"
    echo "VITE_API_URL=$API_URL" > "$CODESPACE_VSCODE_FOLDER/frontend/.env.local"
fi

echo "👉 Running Vite with --host so Codespaces can forward the port"
npm run dev -- --host > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!

# Wait briefly for Vite to start
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
