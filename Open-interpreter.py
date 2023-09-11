# Define ANSI escape codes for color formatting
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

# Header box
print(f"{BLUE}***********************************************{ENDC}")
print(f"{GREEN}*              Open-Interpreter              *{ENDC}")
print(f"{BLUE}***********************************************{ENDC}")
print("\n\n")  # Add two empty lines

import interpreter

interpreter.auto_run = True
interpreter.local = True
#interpreter.model = "gpt-3.5-turbo"
#interpreter.api_key = "your_openai_api_key"

while True:
    print(f"{RED}You:{ENDC}", end="")
    user_input = input() 
    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break
    
    print(f"{YELLOW}O/I:{ENDC}", )
    interpreter.chat(user_input)
