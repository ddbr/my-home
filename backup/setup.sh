#!/bin/bash

echo "🚀 Setting up Python virtual environment..."
python3 -m venv .venv

echo "📦 Activating virtual environment..."
source .venv/bin/activate

echo "🔍 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup complete! To start, run:"
echo "source .venv/bin/activate"
echo "python -m src.main"
