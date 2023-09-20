from rich.console import Console
from rich.prompt import Prompt

console = Console()

def yes_or_no(question: str, default: str):
    # Ask a yes/no question via raw_input() and return their answer
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    while True:
        choice = Prompt.ask(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] Yes or No [/grey100 on deep_pink2][deep_pink2]▀ {question}", default=default).lower()
        if choice in valid: return valid[choice]
        else: console.print("Please respond with 'yes' or 'no' "
                          "(or 'y' or 'n').")
            
def input_prompt(question: str, default: str = None):
    # Ask for user input and return their answer
    while True:
        console.print(question)
        answer = Prompt.ask(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] Input [/grey100 on deep_pink2][deep_pink2]▀ {question}", default=default)
        if answer is not None: return answer
        else: console.print(f"[red3]Error:[/red3] Invalid Choice")