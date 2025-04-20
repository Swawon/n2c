#!/usr/bin/env python3
import sys
import warnings
import subprocess
from n2c.crew import LinuxCmdAutomation
import readline

# Disable some annoying warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def input_with_prefill(prompt, prefill):
    def hook():
        readline.insert_text(prefill)
        readline.redisplay()
    readline.set_pre_input_hook(hook)
    try:
        return input(prompt)
    finally:
        readline.set_pre_input_hook()

def run():
    if len(sys.argv) < 2:
        print(f"{RED}❌ Please provide a natural language input as an argument.{RESET}")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    inputs = {'user_request': user_input}

    try:
        crew = LinuxCmdAutomation().crew()
        result = crew.kickoff(inputs=inputs)

        output = crew.tasks[0].output
        final_output = output.strip() if isinstance(output, str) else getattr(output, 'content', str(output)).strip()
        command_only = final_output.strip().strip('`')

        if not command_only:
            print(f"{RED}❌ No valid command to execute.{RESET}")
            return

        print(f"{CYAN}{BOLD}Generated Command:{RESET} {command_only}")
        print(f"{YELLOW}{BOLD}Explanation:{RESET} {str(crew.tasks[-1].output).strip().strip('`')}")
        print(f"\n{BOLD}Choose an option:{RESET}")
        print(f"[1] Run this command")
        print(f"[2] Edit this command")
        print(f"[3] Abort")

        choice = input(f"{BOLD}Enter your choice (1/2/3) [default: 1]: {RESET}").strip()
        if choice == '':
            choice = '1'

        if choice == '1':
            print(f"{GREEN}✅ Executing command: {command_only}{RESET}")
            subprocess.run(command_only, shell=True, check=True)

        elif choice == '2':
            edited_command = input_with_prefill(f"{BOLD}Edit and run the command: {RESET}", command_only).strip()
            if not edited_command:
                edited_command = command_only

            print(f"{GREEN}✅ Executing edited command: {edited_command}{RESET}")
            subprocess.run(edited_command, shell=True, check=True)

        elif choice == '3':
            print(f"{YELLOW}⚠️ Aborted by user.{RESET}")
        else:
            print(f"{RED}❌ Invalid option. Aborting.{RESET}")

    except subprocess.CalledProcessError as e:
        print(f"{RED}❌ The command failed with error code {e.returncode}.{RESET}")
    except Exception as e:
        print(f"{RED}❌ An error occurred while running the crew: {e}{RESET}")

if __name__ == "__main__":
    run()

