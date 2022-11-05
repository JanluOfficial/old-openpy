import startup
import os
import framework.apps.getApps as getApps
import framework.commands.handler as cmdhandler
from rich.console import Console
from rich.prompt import Prompt

try:
    startJSON = startup.Data_Collector.getStartupJSON()
    print("OpenPy")
    console = Console()
    version = startJSON['version']
    branch = startJSON['branch-name']
    
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
        cmdhandler.handle.command(Prompt.ask('[cyan]Open[/cyan][bold magenta]Py[/bold magenta]> '))

except KeyboardInterrupt:
    print()
    console.print('[red]Force Quitting OpenPy[/red] via [bold blue]KeyboardInterrupt[bold blue]')
    print()
    quit()