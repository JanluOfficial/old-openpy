import os
import api.system as sysapi

# Rich
from rich import print
from rich.console import Console

def input():
    console = Console()
    if sysapi.os.is_mac(): raise OSError("Your operating system is not currently supported by OpenPy")
    cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.getlogin() if sysapi.os.is_windows else os.path.expanduser('~').replace('/home/', '')} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
    return None if cmd == "" else cmd.strip()