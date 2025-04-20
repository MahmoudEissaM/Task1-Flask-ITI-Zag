#!/bin/bash

PORT=5000

PID=$(lsof -t -i:$PORT)

if [ -z "$PID" ]; then
  echo "✅ Port $PORT is free. Starting the Flask app..."
  python app.py
else
  echo "🔪 Killing process $PID using port $PORT"
  kill -9 $PID
  echo "✅ Port $PORT is now free. Starting the Flask app..."
  python app.py
fi
