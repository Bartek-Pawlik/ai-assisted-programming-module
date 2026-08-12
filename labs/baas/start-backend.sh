#!/bin/bash
# Start the FastAPI backend server

echo "🚀 Starting FastAPI Backend Server..."
echo ""

# Check if GOOGLE_APPLICATION_CREDENTIALS is set
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "⚠️  Warning: GOOGLE_APPLICATION_CREDENTIALS is not set"
    echo "Setting it now..."
    export GOOGLE_APPLICATION_CREDENTIALS="$CODESPACE_VSCODE_FOLDER/backend/firebase-service-account.json"
fi

# Check if firebase service account file exists
if [ ! -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    echo "❌ Error: Firebase service account file not found at:"
    echo "   $GOOGLE_APPLICATION_CREDENTIALS"
    echo ""
    echo "Please complete Part 2 of the README to set up Firebase."
    exit 1
fi

echo "✅ Firebase credentials found"
echo "📍 Starting server at http://localhost:8000"
echo ""

cd "$CODESPACE_VSCODE_FOLDER/backend" || exit 1
uvicorn app.main:app --reload --port 8000
