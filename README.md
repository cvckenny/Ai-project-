# Kenny AI - South Park Style ChatGPT Clone

A **South Park-themed AI chatbot** built with **Tkinter GUI** and **ChatGPT-quality intelligence** powered by OpenAI.

## 🧡 Features

✅ **South Park Visual Style** - Bold outlines, flat design, Comic Sans fonts  
✅ **ChatGPT Intelligence** - Powered by OpenAI's GPT-3.5/GPT-4  
✅ **Kenny McCormick Branding** - Orange parka colors, "Mmph mrmph!" personality  
✅ **Conversation Memory** - Maintains context across multiple messages  
✅ **Tkinter GUI** - No web server needed, runs locally  
✅ **Easy Setup** - Python-only, minimal dependencies  

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install openai python-dotenv
```

### 2. Setup OpenAI API Key

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

Get your API key from: https://platform.openai.com/account/api-keys

### 3. Run the App

```bash
python kenny_ai_app.py
```

## 📋 GUI Components

### Header
- Title: "🧡 KENNY AI - South Park Edition"
- Subtitle: "Mmph mrmph! Ask me anything..."
- Orange background with white text

### Avatar Section
- ASCII Kenny character with orange parka
- Status indicator (🟢 Online)
- Welcoming message

### Chat Display
- **User Messages** (Blue bubbles, right side)
- **Kenny Responses** (Orange bubbles, left side)
- **System Messages** (Gold, center)
- Timestamps for each message
- Auto-scrolling

### Input Area
- Multi-line text input
- Ctrl+Enter to send
- Placeholder text
- Clear and Send buttons

### Buttons
- **🗑️ Clear** - Clear all chat history
- **▶️ SEND** - Send message (orange, South Park style)

## 🎨 Color Palette

```
Kenny Orange:     #FF6600 (Primary accent)
User Blue:        #E3F2FD (User message background)
Kenny Orange BG:  #FFE0B2 (Kenny message background)
Black Borders:    #000000 (South Park style outlines)
White:            #FFFFFF (Main background)
```

## 🛠️ How It Works

1. **GUI Setup** - Tkinter creates South Park-styled interface
2. **User Input** - Type message and press Ctrl+Enter or click Send
3. **API Call** - Message sent to OpenAI in separate thread (non-blocking)
4. **Kenny Response** - AI responds as Kenny McCormick character
5. **Display** - Response shown in chat with timestamp

## 📝 System Prompt (Kenny's Personality)

Kenny is configured to:
- Respond as Kenny McCormick from South Park
- Say "Mmph mrmph!" occasionally (muffled speech)
- Reference South Park and character experiences
- Be genuinely helpful and kind
- Make light self-deprecating jokes
- Keep a casual, friendly tone

## ⚙️ Configuration

Edit `kenny_ai_app.py` to customize:

```python
self.system_prompt = """Your custom prompt here"""
```

Or use environment variables in `.env`:

```
OPENAI_MODEL=gpt-4  # Use GPT-4 instead of GPT-3.5
```

## 📦 Project Structure

```
Ai-project-/
├── kenny_ai_app.py          # Main Tkinter application
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── design/                 # Design documentation
    ├── design_brief.md
    └── south_park_ui_mockup.md
```

## 🔧 Advanced Options

### Use Different OpenAI Models

```python
# In kenny_ai_app.py, change:
model="gpt-3.5-turbo"  # to gpt-4 or gpt-4-turbo
```

### Adjust Response Behavior

```python
response = self.client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.7,      # Higher = more creative (0-1)
    max_tokens=500,       # Max response length
)
```

### Customize Colors

Edit the `COLORS` dictionary in `kenny_ai_app.py`:

```python
COLORS = {
    "kenny_orange": "#FF6600",
    "user_blue": "#E3F2FD",
    # ... etc
}
```

## 🐛 Troubleshooting

### API Key Error
```
Error: OpenAI API not configured
```
- Create `.env` file with `OPENAI_API_KEY=your_key`
- Ensure `openai` package is installed

### Import Error
```
ModuleNotFoundError: No module named 'openai'
```
- Install: `pip install openai python-dotenv`

### GUI Not Displaying
- Ensure Python 3.7+ is installed
- On Linux, may need: `sudo apt-get install python3-tk`

## 🚀 Future Features

- [ ] Conversation history persistence (SQLite)
- [ ] Web version (Flask/React frontend)
- [ ] Voice input/output
- [ ] Custom avatar images
- [ ] Multiple conversation threads
- [ ] Export chat as PDF/TXT
- [ ] Settings/preferences panel

## 📄 License

This project is open source. Feel free to modify and redistribute!

## 🎬 Credits

**South Park** - Trey Parker & Matt Stone  
**OpenAI ChatGPT** - OpenAI  
**Built with** - Python, Tkinter, OpenAI API

---

**Status**: Ready to Use  
**Last Updated**: 2026-06-26  
**Version**: 1.0.0
