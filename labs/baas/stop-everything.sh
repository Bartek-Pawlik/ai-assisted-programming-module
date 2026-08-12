#!/bin/bash
# Kill all frontend and backend processes

echo "🛑 Stopping All Servers"
echo "========================================"
echo ""

killed=0

# Kill backend processes
echo "🔧 Stopping Backend Server..."
if pkill -f "uvicorn app.main:app" > /dev/null 2>&1; then
    echo "   ✅ Backend server stopped"
    ((killed++))
else
    echo "   ℹ️  No backend server running"
fi

# Also try to kill by PID file
if [ -f /tmp/backend.pid ]; then
    backend_pid=$(cat /tmp/backend.pid)
    if kill "$backend_pid" > /dev/null 2>&1; then
        echo "   ✅ Backend process (PID: $backend_pid) killed"
    fi
    rm /tmp/backend.pid
fi

echo ""

# Kill frontend processes
echo "🎨 Stopping Frontend Server..."
if pkill -f "npm run dev" > /dev/null 2>&1; then
    echo "   ✅ Frontend npm process stopped"
    ((killed++))
fi

if pkill -f "node.*vite" > /dev/null 2>&1; then
    echo "   ✅ Frontend vite process stopped"
    ((killed++))
fi

# Also try to kill by PID file
if [ -f /tmp/frontend.pid ]; then
    frontend_pid=$(cat /tmp/frontend.pid)
    if kill "$frontend_pid" > /dev/null 2>&1; then
        echo "   ✅ Frontend process (PID: $frontend_pid) killed"
    fi
    rm /tmp/frontend.pid
fi

# Check for any remaining processes on ports
echo ""
echo "🔍 Checking ports..."
if lsof -ti:8000 > /dev/null 2>&1; then
    echo "   🧹 Cleaning up port 8000..."
    lsof -ti:8000 | xargs kill -9 2>/dev/null
    echo "   ✅ Port 8000 cleared"
fi

if lsof -ti:5173 > /dev/null 2>&1; then
    echo "   🧹 Cleaning up port 5173..."
    lsof -ti:5173 | xargs kill -9 2>/dev/null
    echo "   ✅ Port 5173 cleared"
fi

if lsof -ti:5174 > /dev/null 2>&1; then
    echo "   🧹 Cleaning up port 5174..."
    lsof -ti:5174 | xargs kill -9 2>/dev/null
    echo "   ✅ Port 5174 cleared"
fi

echo ""
echo "========================================"
if [ $killed -gt 0 ]; then
    echo "✅ All servers stopped successfully!"
else
    echo "ℹ️  No servers were running"
fi
echo "========================================"
echo ""
echo "💡 To start again, run: ./start-everything.sh"
echo ""
