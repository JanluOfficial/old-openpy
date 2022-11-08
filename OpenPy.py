import startup
import os
import framework.commands.handler as cmdhandler
from rich.console import Console
from rich.prompt import Prompt
from rich.console import Group
from rich.panel import Panel

try:
    startJSON = startup.Data_Collector.getStartupJSON()
    startup.StartUp.ProgramDataFolder()
    github_API_key = startup.StartUp.GithubKey('startup')
        
    version = startJSON['version']
    branch = startJSON['branch-name']
    console = Console()
    console.print(f'OpenPy {version}', justify='center', style='white reverse')
    if branch == "stable":
        console.print(branch, style='cyan reverse', justify='center')
    elif branch == "beta":
        console.print(branch, style='magenta reverse', justify='center')
    elif branch == "alpha":
        console.print(branch, style='red reverse', justify='center')
    else:
        console.print(branch, style='purple', justify='center')
    while 1 != 2:
        cmdprompt = Prompt.ask('[cyan]Open[/cyan][bold magenta]Py[/bold magenta]> ')
        cmdhandler.handle.command(cmdprompt, github_API_key)

except KeyboardInterrupt:
    print()
    from rich.console import Console
    from rich.console import Group
    from rich.panel import Panel
    console = Console()
    console.print("[red]Exception:[/red] KeyboardInterrupt"),
    console.print("You have [green]succesfully[/green] force quit [bold][yellow]Open[/yellow][blue]Py[/blue][/bold]. Thank you for using it.")
    quit()