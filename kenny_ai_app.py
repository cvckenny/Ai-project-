#!/usr/bin/env python3
"""
🧡 Kenny AI - South Park Themed ChatGPT Clone
A fun, South Park-styled AI chatbot built with Tkinter and OpenAI API
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI, APIError

# Load environment variables
load_dotenv()

# Color Palette (South Park Style)
COLORS = {
    "kenny_orange": "#FF6600",
    "kenny_orange_light": "#FFE0B2",
    "user_blue": "#E3F2FD",
    "black": "#000000",
    "white": "#FFFFFF",
    "gray": "#F5F5F5",
    "gold": "#FFD700",
}

FONTS = {
    "title": ("Comic Sans MS", 16, "bold"),
    "subtitle": ("Comic Sans MS", 10),
    "chat": ("Arial", 10),
    "button": ("Comic Sans MS", 9, "bold"),
}

# Kenny ASCII Art
KENNY_ASCII = """
    /\\___/\\
    (  o.o  )  🧡
     > ^ <
    /|   |\\
      | |
     /   \\
"""

class KennyAIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧡 KENNY AI - South Park Edition")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Initialize OpenAI client
        try:
            self.api_key = os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            self.client = OpenAI(api_key=self.api_key)
            self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        except (APIError, ValueError) as e:
            messagebox.showerror("API Error", f"Failed to initialize OpenAI: {e}")
            self.client = None
        
        # Conversation history for context
        self.conversation_history = []
        self.is_sending = False
        
        # System prompt - Kenny's personality
        self.system_prompt = """You are Kenny McCormick from South Park. You speak like Kenny would - sometimes saying "Mmph mrmph!" (your muffled speech), 
referencing your experiences in South Park, and making self-deprecating jokes. You're genuinely helpful and kind despite your tough circumstances. 
Keep responses relatively brief (2-3 sentences usually) and maintain Kenny's casual, friendly tone. Occasionally reference dying or your poverty, 
but keep it light and humorous. Answer all questions helpfully while staying in character."""
        
        self.setup_ui()
        
    def setup_ui(self):
        """Create the South Park-themed GUI"""
        
        # === HEADER ===
        header_frame = tk.Frame(self.root, bg=COLORS["kenny_orange"], height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="🧡 KENNY AI",
            font=FONTS["title"],
            bg=COLORS["kenny_orange"],
            fg=COLORS["white"],
        )
        title_label.pack(pady=(10, 0))
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="South Park Edition | Mmph mrmph! Ask me anything...",
            font=FONTS["subtitle"],
            bg=COLORS["kenny_orange"],
            fg=COLORS["white"],
        )
        subtitle_label.pack(pady=(0, 10))
        
        # === AVATAR & STATUS ===
        avatar_frame = tk.Frame(self.root, bg=COLORS["kenny_orange_light"], height=70)
        avatar_frame.pack(fill=tk.X, padx=0, pady=0)
        avatar_frame.pack_propagate(False)
        
        avatar_text = tk.Label(
            avatar_frame,
            text=KENNY_ASCII,
            font=("Courier", 8),
            bg=COLORS["kenny_orange_light"],
            fg=COLORS["kenny_orange"],
            justify=tk.LEFT,
        )
        avatar_text.pack(side=tk.LEFT, padx=10)
        
        status_label = tk.Label(
            avatar_frame,
            text="🟢 Online\n\nHey! It's me, Kenny!\nWhat do you wanna talk about?",
            font=FONTS["chat"],
            bg=COLORS["kenny_orange_light"],
            fg=COLORS["black"],
            justify=tk.LEFT,
        )
        status_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        # === CHAT DISPLAY AREA ===
        chat_frame = tk.Frame(self.root, bg=COLORS["white"])
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            bg=COLORS["white"],
            fg=COLORS["black"],
            font=FONTS["chat"],
            state=tk.DISABLED,
            relief=tk.RIDGE,
            borderwidth=2,
            height=15,
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for different message types
        self.chat_display.tag_config("user_msg", foreground=COLORS["black"], background=COLORS["user_blue"], relief=tk.RAISED, borderwidth=1)
        self.chat_display.tag_config("kenny_msg", foreground=COLORS["black"], background=COLORS["kenny_orange_light"], relief=tk.RAISED, borderwidth=1)
        self.chat_display.tag_config("system_msg", foreground=COLORS["kenny_orange"], font=("Arial", 9, "bold"))
        self.chat_display.tag_config("timestamp", foreground="#999999", font=("Arial", 8, "italic"))
        
        # === INPUT AREA ===
        input_frame = tk.Frame(self.root, bg=COLORS["gray"], relief=tk.RIDGE, borderwidth=2)
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        self.input_text = tk.Text(
            input_frame,
            height=4,
            wrap=tk.WORD,
            font=FONTS["chat"],
            bg=COLORS["white"],
            fg=COLORS["black"],
            relief=tk.FLAT,
            borderwidth=1,
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        self.input_text.bind("<Control-Return>", lambda e: self.send_message())
        
        # === BUTTON AREA ===
        button_frame = tk.Frame(self.root, bg=COLORS["white"])
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️  CLEAR",
            command=self.clear_chat,
            bg=COLORS["gray"],
            fg=COLORS["black"],
            font=FONTS["button"],
            relief=tk.RAISED,
            borderwidth=2,
            width=15,
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        send_btn = tk.Button(
            button_frame,
            text="▶️  SEND",
            command=self.send_message,
            bg=COLORS["kenny_orange"],
            fg=COLORS["white"],
            font=FONTS["button"],
            relief=tk.RAISED,
            borderwidth=3,
            width=15,
            activebackground="#FF8800",
        )
        send_btn.pack(side=tk.RIGHT, padx=5)
        
    def add_message(self, sender, message):
        """Add a message to the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Determine tag and formatting
        if sender == "User":
            tag = "user_msg"
            prefix = "👤 You"
        else:
            tag = "kenny_msg"
            prefix = "🧡 Kenny"
        
        # Add timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        # Add message
        self.chat_display.insert(tk.END, f"{prefix}: {message}\n\n", tag)
        
        # Auto-scroll to bottom
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def add_system_message(self, message):
        """Add a system message to the chat"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"✦ {message}\n\n", "system_msg")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def send_message(self):
        """Send user message and get Kenny's response"""
        if self.is_sending:
            messagebox.showwarning("Wait", "Kenny is still thinking... Mmph mrmph!")
            return
        
        user_input = self.input_text.get("1.0", tk.END).strip()
        
        if not user_input:
            messagebox.showwarning("Empty Message", "Dude, say something!")
            return
        
        if not self.client:
            messagebox.showerror("Error", "OpenAI API not configured!")
            return
        
        # Clear input
        self.input_text.delete("1.0", tk.END)
        
        # Add user message to display
        self.add_message("User", user_input)
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Get response in separate thread to avoid freezing GUI
        self.is_sending = True
        threading.Thread(target=self.get_kenny_response, daemon=True).start()
    
    def get_kenny_response(self):
        """Get response from OpenAI API as Kenny"""
        try:
            self.add_system_message("Kenny is thinking... 🤔")
            
            # Prepare messages for API
            messages = [{"role": "system", "content": self.system_prompt}] + self.conversation_history
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )
            
            kenny_response = response.choices[0].message.content
            
            # Add to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": kenny_response
            })
            
            # Add response to display
            self.add_message("Kenny", kenny_response)
            
        except APIError as e:
            self.add_system_message(f"⚠️  API Error: {str(e)}")
        except Exception as e:
            self.add_system_message(f"⚠️  Error: {str(e)}")
        finally:
            self.is_sending = False
    
    def clear_chat(self):
        """Clear chat history"""
        if messagebox.askyesno("Clear Chat", "Clear all messages? You can't get them back!"):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete("1.0", tk.END)
            self.chat_display.config(state=tk.DISABLED)
            self.conversation_history = []
            self.add_system_message("Chat cleared. Let's start fresh! 🧡")


def main():
    """Run the Kenny AI app"""
    root = tk.Tk()
    app = KennyAIApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
