from rich.console import Console
import os

def input():
    console = Console()
    cmd = console.input(f"[deep_pink2]▄[/deep_pink2][grey100 on deep_pink2] OpenPy [/grey100 on deep_pink2][deep_pink2 on dark_cyan]▀[/deep_pink2 on dark_cyan][grey100 on dark_cyan] {os.getlogin()} [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ") 