import sys
import os
import framework.commands.handler as cmdhandler
from rich.console import Console
from rich.prompt import Prompt
from rich.console import Group
from rich.panel import Panel
import framework.commands.OpenPyCommands as OpenPyCMDs
import framework.console as con
import platform
from time import sleep
import framework.color.theme as themes
import json
import framework.OOBE as OOBE

con.clear()

if os.name != 'nt':
    console = Console()
    console.print('OpenPy is currently [red]NOT[/red] supported on your Operating System.')
    console.print('If you are using a [bold red]Mac[/bold red] or [green]Linux[green], please set up a virtual machine running [bold blue]Windows[/bold blue] using something like [bold red]Oracle[/bold red] [bold blue]Virtual Box[/bold blue] or [yellow]VMware Workstation[/yellow]')
    print()
    console.print('OpenPy will quit in [red]10 seconds[/red]')
    sleep(10)
    quit()

args = sys.argv
args.append('undefined')
args.append('undefined')
args.append('undefined')
args.append('undefined')

if args[1] == '-d':
    startJSON = OpenPyCMDs.Data_Collector.getStartupJSON()
    OpenPyCMDs.Directories.checkAndCreate()
    OpenPyCMDs.Files.checkAndCopyDefaultFiles()
    OOBE.OpenPyOOBE()

    version = startJSON['version']
    console = Console()

    appdata = os.getenv('APPDATA')

    console.print(f'OpenPy {version}', justify='center', style=themes.getColor('OpenPy', 'title'))
    console.print("debug", style=themes.getColor('tags', 'debug'), justify='center')
    with console.status('[bold purple]Reading Application Data...') as status:
        while 1 != 2:
            app_data = open(sys.argv[2]).read()
            console.log('[green]The Application Data has been read and the program will start soon.')
            break
    sleep(1)
    exec(app_data)
else:
    try:
        startJSON = OpenPyCMDs.Data_Collector.getStartupJSON()
        OpenPyCMDs.Directories.checkAndCreate()
        OpenPyCMDs.Files.checkAndCopyDefaultFiles()

        appdata = os.getenv('APPDATA')
        theme = open(appdata + '\\OpenPy\\themes\\default.json', 'r')

        version = startJSON['version']
        branch = startJSON['branch-name']
        console = Console()
        console.print(f'OpenPy {version}', justify='center', style=themes.getColor('OpenPy', 'title'))
        if branch == "stable":
            console.print(branch, style=themes.getColor('tags', 'stable'), justify='center')
        elif branch == "beta":
            console.print(branch, style=themes.getColor('tags', 'beta'), justify='center')
        elif branch == "alpha":
            console.print(branch, style=themes.getColor('tags', 'alpha'), justify='center')
        else:
            console.print(branch, style=themes.getColor('tags', 'unknown'), justify='center')
        while 1 != 2:
            cmdprompt = Prompt.ask(OpenPyCMDs.Strings.OpenPyString())
            cmdhandler.handle.command(cmdprompt, "not_present")

    except KeyboardInterrupt:
        from rich.console import Console
        from rich.console import Group
        from rich.panel import Panel
        console = Console()
        console.print("[red]Exception:[/red] KeyboardInterrupt"),
        console.print("You have [green]succesfully[/green] force quit [bold][yellow]Open[/yellow][blue]Py[/blue][/bold]. Thank you for using it.")
        quit()