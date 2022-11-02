import startup
import os
import framework.apps.getApps as getApps
import framework.commands.handler as cmdhandler
from rich.console import Console

class start:
    startJSON = startup.Data_Collector.getStartupJSON()
    print(startJSON[f'version'])
    console = Console()
    while 1 != 1:
        cmdhandler.handle.command(input(f'OpenPy'))