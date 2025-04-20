🧠 n2c — Natural Language to Linux Command Translator
Transform plain English into safe, precise Linux commands with AI!

n2c is a command-line tool powered by Gemini (Google AI) that translates your everyday language into secure terminal commands — with explanation, safety validation, and editing before execution.

🚀 Features
✅ Translate natural language to Linux commands
✅ Validate and warn about dangerous commands
✅ Edit commands before execution
✅ Works offline after setup
✅ Default model: Gemini 1.5 Pro

📦 Installation
You must have root access to move files to system directories.

First clone the repository:

git clone https://github.com/Swawon/n2c.git

Then run these commands to install system-wide:

sudo mv n2c /usr/share/n2c
sudo cp /usr/share/n2c/n2c.bash /usr/local/bin/n2c
sudo chmod +x /usr/local/bin/n2c

Now you can use n2c from anywhere:

n2c "your natural language command"

🔐 API Setup
Create the configuration file at /usr/share/n2c/.env with these contents:

MODEL=gemini/gemini-1.5-pro
GEMINI_API_KEY=your_gemini_api_key_here

🎛️ Model Switching
To use OpenAI instead, edit the .env file to contain:

MODEL=openai/gpt-4
OPENAI_API_KEY=your_openai_api_key

🧠 Usage Example
Run a command like:

n2c "show me all running processes"

You'll see output like:

Generated Command: ps aux
Description: Shows all running processes

[1] Run command
[2] Edit command
[3] Cancel

👨‍💻 Author
Created by Swawon Mondal
Support: smalltutorialworld@gmail.com
