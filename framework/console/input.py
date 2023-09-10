import os
import api.system as sysapi

# Rich
from rich import print
from rich.console import Console

def input():
    console = Console()
    if sysapi.os.is_windows(): cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.getlogin()} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
    elif sysapi.os.is_linux(): cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.path.expanduser('~').replace('/home/', '')} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
    else: raise OSError("Your operating system is not currently supported by OpenPy")
    if cmd == "": return None
    else: return cmd