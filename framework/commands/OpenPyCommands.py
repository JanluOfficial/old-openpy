import subprocess
import rich
from rich.console import Console

class Apps:
    def launch(app_path: str):
        console = Console()
        with console.status('[bold purple]Reading Application Data...') as status:
            while open(app_path).read():
                app_data = open(app_path).read()
                console.log('[green]The Application Data has been read and the program will start soon.')
                break
        exec(app_data)