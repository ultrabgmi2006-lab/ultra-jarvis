#!/bin/bash

echo "Installing Jarvis Agent..."

pip install requests speechrecognition pyttsx3 pyautogui

echo "Downloading agent..."

curl -O https://your-repo/jarvis_agent.py

echo "Starting agent..."

python jarvis_agent.py
