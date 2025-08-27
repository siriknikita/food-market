#!/bin/bash

# Food Market Platform - Development Startup Script

echo "🚀 Starting Food Market Platform in development mode..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

# Start MongoDB and Backend
echo "📦 Starting backend services..."
cd backend

# Install Python dependencies if not already installed
if [ ! -d ".venv" ]; then
    echo "📥 Installing Python dependencies..."
    uv install
fi

# Start backend in background
echo "🔧 Starting FastAPI backend..."
uv run python start.py &
BACKEND_PID=$!

cd ..

# Start Frontend
echo "🎨 Starting React frontend..."
cd frontend

# Install Node.js dependencies if not already installed
if [ ! -d "node_modules" ]; then
    echo "📥 Installing Node.js dependencies..."
    npm install
fi

# Start frontend
echo "⚡ Starting Vite development server..."
npm run dev &
FRONTEND_PID=$!

cd ..

echo ""
echo "✅ Food Market Platform is starting up!"
echo ""
echo "📱 Frontend: http://localhost:5173"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "✅ All services stopped"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Wait for background processes
wait 