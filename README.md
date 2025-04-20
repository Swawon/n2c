# 🧠 n2c — Natural Language to Linux Command Translator

Transform plain English into safe, precise Linux commands with AI!

`n2c` is a command-line tool powered by Gemini (Google AI) that translates your everyday language into secure terminal commands — with explanation, safety validation, and editing before execution.

---

## 🚀 Features

✅ Translate natural language to Linux commands  
✅ Validate and warn about dangerous commands  
✅ Edit commands before execution  
✅ Works offline after setup  
✅ Default model: **Gemini 1.5 Pro**

---

## 📦 Installation Instructions

> You must have root access to move files to system directories.

### 1. Clone the repository

```bash
git clone https://github.com/Swawon/n2c.git


### 📁 Move Files to System Directories

```bash
# Move the entire project to /usr/share
sudo mv n2c /usr/share/n2c

# Copy the launcher script to /usr/local/bin
sudo cp /usr/share/n2c/n2c.bash /usr/local/bin/n2c

# Make it executable
sudo chmod +x /usr/local/bin/n2c

Now, you can use n2c from anywhere in the terminal:
n2c "list all files in the current directory"

###🔐 API Setup
The .env file should be located in the /usr/share/n2c/ directory.

Its contents should look like this:

env

MODEL=gemini/gemini-1.5-pro
GEMINI_API_KEY=your_gemini_api_key_here
