import os
from rich.console import Console
import framework.console as con
from rich.console import Console
from rich.prompt import Prompt
from time import sleep
from rich.console import Group
from rich.panel import Panel
from rich.progress import track
import subprocess

console = Console()

con.clear()
console.print('[bold][yellow]Open[/yellow][blue]Py[/blue][/bold] [dim]Development Enviorment[/dim]')
print()
console = Console()
console.print(f'[blink]1[/blink] [bold]New Project[/bold] [dim]Create a new Project using OpenPy[dim]')
console.print(f'[blink]2[/blink] [bold]Exit[/bold] [dim]Exit the Development Enviorment[dim]')
value = Prompt.ask("Enter a choice", default="1")
if value == "1":
    con.clear()
    console.print(f'[bold][yellow]Open[/yellow][blue]Py[/blue][/bold] [dim]Development Enviorment[/dim]')
    print()
    name = Prompt.ask("Project Name", default="My App")
    subtitle = Prompt.ask("Subtitle", default="Created with OpenPy")
    description = Prompt.ask("Description", default="A beautiful App made with OpenPy")
    file_name = Prompt.ask("Main File Name", default=f"{name}.py")
    if not file_name.endswith('.py'):
        file_name += '.py'
    sleep(1)
    con.clear()
    console.print(f'[bold][yellow]Open[/yellow][blue]Py[/blue][/bold] [dim]Development Enviorment[/dim]')
    panel_group = Group(
    console.print(f"App Name:       {name}"),
    console.print(f"Description:    {description}"),
    console.print(f'Main File Name: {file_name}')
    )
    console.print(Panel(panel_group))
    confirmation = Prompt.ask("Confirm?", default="N", choices=['Y', 'N'])
    if confirmation == "Y":
        for i in track(range(7), description="Creating Files..."):
            if not os.path.exists(os.getcwd() + f'\\apps\\{name}'):
                os.mkdir(os.getcwd() + f'\\apps\\{name}')
            f = open(os.getcwd() + f'\\apps\\{name}\\{file_name}', 'w')
            f2 = open(os.getcwd() + f'\\apps\\{name}\\app.json', 'w')
            mainFile = [
                'import framework.console as con\n',
                'import framework.getConsoleSize as consize\n',
                'from rich.console import Console\n',
                'from rich.prompt import Prompt\n',
                'from time import sleep\n',
                'from rich.console import Group\n',
                'from rich.panel import Panel\n',
                'import json\n',
                '\n',
                'name = json.loads(open("app.json", "r").read())\n',
                'console = Console()\n',
                'console.print(f"Welcome to your new [yellow]Open[/yellow][blue]Py[/blue] Application")'
            ]
            jsonFile = [
                '{\n'
                f'    "name": "{name}",\n',
                f'    "subtitle": "{subtitle}",\n',
                f'    "version": 1.0,\n',
                f'    "description": "{description}",\n',
                f'    "main-file": "{file_name}",\n',
                f'    "app-type": "openpy"\n'
                '}'
            ]
            f.writelines(mainFile)
            f2.writelines(jsonFile)
            sleep(0.05)
        console.print("[green]The Project has been created.[green]")
        if os.path.exists("C:\Program Files\Microsoft VS Code"):
            console.print(f"An installation of [bold blue]Visual Studio Code[/bold blue] has been detected. Would you like to open your new Project using [bold blue]Visual Studio Code[/bold blue]?")
            vscode = Prompt.ask("Open VS Code?", choices=['Y', 'N'])
            if vscode == "Y":
                console.print("Opening [blue bold]Visual Studio Code[/blue bold]...")
                subprocess.call(f'"C:/Program Files/Microsoft VS Code/Code.exe" "' + os.getcwd() + f'\\apps\\{name}\\"')
            else:
                console.print("Not Opening [red]Visual Studio Code[/red]...")

    else:
        console.print("[red]The Project has not been created[red]")