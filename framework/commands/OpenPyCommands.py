import subprocess
import rich
from rich.console import Console
from time import sleep

class Apps:
    def launch(app_path: str):
        console = Console()
        with console.status('[bold purple]Reading Application Data...') as status:
            while 1 != 2:
                app_data = open(app_path).read()
                console.log('[green]The Application Data has been read and the program will start soon.')
                break
        sleep(1)
        exec(app_data)