import os
import platform

# Rich
from rich import print
from rich.console import Console

def input():
    console = Console()
    if platform.system() == "Windows": cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.getlogin()} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
    elif platform.system() == "Linux": cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.path.expanduser('~').replace('/home/', '')} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
    else: raise OSError("This Operating System is not supported by OpenPy")
    print()
    return cmd