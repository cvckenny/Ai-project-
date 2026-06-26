"""
Kenny AI - Simple Installation & Setup Guide
"""

# ==========================================
# STEP 1: Install Python (if not already)
# ==========================================
# Download from: https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation


# ==========================================
# STEP 2: Install Required Packages
# ==========================================

# Open Command Prompt or Terminal and run:

pip install openai python-dotenv


# ==========================================
# STEP 3: Get OpenAI API Key
# ==========================================

# 1. Go to: https://platform.openai.com/account/api-keys
# 2. Click "Create new secret key"
# 3. Copy the key (it won't be shown again!)
# 4. Save it somewhere safe


# ==========================================
# STEP 4: Setup .env File
# ==========================================

# Create a file named: .env (in the same folder as kenny_ai_app.py)
# Add these lines:

OPENAI_API_KEY=sk-YOUR_API_KEY_HERE
OPENAI_MODEL=gpt-3.5-turbo

# Replace "YOUR_API_KEY_HERE" with your actual API key from Step 3


# ==========================================
# STEP 5: Run the App
# ==========================================

# In Command Prompt/Terminal, navigate to the project folder and run:

python kenny_ai_app.py

# OR (if python is not in PATH):

python3 kenny_ai_app.py


# ==========================================
# TROUBLESHOOTING
# ==========================================

# If you get "No module named 'openai'"
# Run: pip install openai --upgrade

# If GUI doesn't show on Linux
# Run: sudo apt-get install python3-tk

# If API key error appears
# Check your .env file has correct API key
# Make sure you're not sharing your API key!

# ==========================================
# COSTS
# ==========================================

# OpenAI API is NOT free, but very cheap:
# GPT-3.5: ~$0.0015 per 1K tokens (very affordable)
# GPT-4: ~$0.03 per 1K tokens (more expensive)

# You can set usage limits in OpenAI dashboard
# to avoid unexpected charges


# ==========================================
# USAGE
# ==========================================

# 1. Type your message in the text box
# 2. Press Ctrl+Enter or click SEND button
# 3. Wait for Kenny AI to respond (orange bubble)
# 4. Continue conversation
# 5. Click CLEAR to reset chat


print("✅ Setup complete! Run: python kenny_ai_app.py")
