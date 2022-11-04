import startup
import os
import framework.apps.getApps as getApps
import framework.commands.handler as cmdhandler
from rich.console import Console

startJSON = startup.Data_Collector.getStartupJSON()
print("OpenPy")
console = Console()
version = startJSON['version']
secondLine = startJSON['branch-name'] + ' (' + startJSON['shortened-branch-name'] + ')'
console.print(f'OpenPy {version}', justify='center', style='white reverse')
console.print(secondLine, style='cyan reverse', justify='center')
while 1 != 2:
    cmdhandler.handle.command(input('OpenPy> '))