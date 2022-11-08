try:
    import os
    import framework.commands.handler as cmdhandler
    from rich.console import Console
    from rich.prompt import Prompt
    from rich.console import Group
    from rich.panel import Panel
    import framework.commands.OpenPyCommands as OpenPyCMDs
    import platform
    from time import sleep
except: print("OpenPy has failed to import one or more Modules. Please make sure all Modules are installed before running OpenPy Again.")


if os.name != 'nt':
    console = Console()
    console.print('OpenPy is currently [red]NOT[/red] supported on your Operating System.')
    console.print('If you are using a [bold red]Mac[/bold red] or [green]Linux[green], please set up a virtual machine running [bold blue]Windows[/bold blue] using something like [bold red]Oracle[/bold red] [bold blue]Virtual Box[/bold blue] or [yellow]VMware Workstation[/yellow]')
    print()
    console.print('OpenPy will quit in [red]10 seconds[/red]')
    sleep(10)

try:
    startJSON = OpenPyCMDs.Data_Collector.getStartupJSON()
    OpenPyCMDs.Directories.checkAndCreate()
    github_API_key = OpenPyCMDs.startup.GithubKey('startup')
        
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