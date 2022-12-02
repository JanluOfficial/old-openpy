import os
from rich.console import Console
import framework.console as con
from rich.console import Console
from rich.prompt import Prompt
from time import sleep
from rich.console import Group
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Confirm
import subprocess
import framework.commands.OpenPyCommands as OpenPyCMDs
import framework.color.theme as theme

opstr = OpenPyCMDs.Strings.OpenPyString()
console = Console()

def DevTitle():
    console.print(f'{opstr} [dim]Development Enviorment[/dim]')

def printChoice(number: str, option: str, description: str):
    numberStr = theme.coloredString(f'{number}', 'devEnv', 'number')
    optionStr = theme.coloredString(f'{option}', 'devEnv', 'option')
    descriptionStr = theme.coloredString(f'{description}', 'devEnv', 'description')
    console.print(f'{numberStr} {optionStr} {descriptionStr}')

con.clear()
DevTitle()
print()
console = Console()
printChoice('1', 'New App', ' Create a new App using OpenPy')
printChoice('2', 'New Theme' ,'Create a new OpenPy Theme')
printChoice('3', 'Exit', 'Exit the Development Enviorment')
value = Prompt.ask("Enter a choice", default="1", choices=['1', '2', '3'], show_choices=False)
if value == "1":
    con.clear()
    DevTitle()
    print()
    name = Prompt.ask("Project Name", default="My App")
    subtitle = Prompt.ask("Subtitle", default="Created with OpenPy")
    description = Prompt.ask("Description", default="A beautiful App made with OpenPy")
    file_name = Prompt.ask("Main File Name", default=f"{name}.py")
    if not file_name.endswith('.py'):
        file_name += '.py'
    con.clear()
    panel_group = Group(
    Panel(f"[white]{name}[/white]", style='orange_red1', title="App Name"),
    Panel(f'[white]{subtitle}[/white]', style='red', title='Subtitle'),
    Panel(f"[white]{description}[/white]", style='purple', title="Description"),
    Panel(f'[white]{file_name}[/white]',style='purple4', title='File Name')
    )
    console.print(Panel(panel_group))
    confirmation = Confirm.ask("Confirm?")
    if confirmation:
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
            vsstr = theme.coloredString('Visual Studio Code', 'devEnv', 'VS-Code')
            console.print(f"An installation of {vsstr} has been detected. Would you like to open your new Project using {vsstr}?")
            vscode = Confirm.ask(f"Open {vsstr}?")
            if vscode:
                try:
                    console.print(f"Opening {vsstr}...")
                    subprocess.call(f'"C:/Program Files/Microsoft VS Code/Code.exe" "' + os.getcwd() + f'\\apps\\{name}\\"')
                except:
                    console.print(f'There has been an error opening {vsstr}.')
            else:
                console.print(f"{vsstr} has not been opened.")

    else:
        console.print("[red]The Project has not been created[red]")

elif value == '2':
    con.clear()
    DevTitle()
    name = Prompt.ask("Theme Name", default="My Theme")
    subtitle = Prompt.ask("Subtitle", default="A beautiful Theme for OpenPy")
    file_name = Prompt.ask('File Name', default="MyTheme.json")
    if not file_name.endswith('.json'):
        file_name += '.json'
    con.clear()
    DevTitle()
    panel_group = Group(
    Panel(f"[white]{name}[/white]", style='orange_red1', title="App Name"),
    Panel(f'[white]{subtitle}[/white]', style='red', title='Subtitle'),
    Panel(f"[white]{file_name}[/white]", style='purple', title="Description"),
    )
    console.print(Panel(panel_group))
    confirmation = Confirm.ask("Confirm?")
    if confirmation:
        for i in track(range(7), description="Creating Files..."):
            defaultFile = open(os.getcwd() + '\\framework\\color\\defaultTheme.json', 'r').read()
            defaultTemp1 = defaultFile.replace('"name": "Default",', f'"name": "{name}",')
            default = defaultTemp1.replace('"subtitle": "The default theme for OpenPy",', f'"subtitle": "{subtitle}",')
            open(os.getenv('APPDATA') + f'\\OpenPy\\themes\\{file_name}', 'w').write(default)