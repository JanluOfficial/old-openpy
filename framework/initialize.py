import requests
import json
import random
import os
import time

#Rich
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress


def init():
    console = Console()
    try:
        lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
        listjson = json.loads(lists.content)
        quotes = requests.get(listjson["quoteslisturl"])
        welcome_panel = Panel(random.choice(quotes.text.split("\n")), border_style="gray100", title="OpenPy")
        print(welcome_panel)
    except KeyboardInterrupt:
        interrupt_list = ["Someone seems to have interrupted something", "Dude, why'd you interrupt me?", 'What you just did is called [orange_red1]▄[/orange_red1][grey100 on orange_red1] KeyboardInterrupt [/grey100 on orange_red1][orange_red1]▀[/orange_red1]']
        print(random.choice(interrupt_list))
    except:
        funny_error_list = ["Have you tried connecting?", "[red3]404[/red3]: Quotes not found", "It's too sunny to connect to the cloud.", 'A wise man once said "You are not connected to the internet"']
        print(random.choice(funny_error_list))

    openpy_path = os.path.dirname(os.path.realpath(__file__)).rstrip("\\framework")

    if not os.path.exists(openpy_path + "\\settings\\home.txt") or open(openpy_path + "\\settings\\home.txt", "r").read() == "":
        home_txt = open(openpy_path + "\\settings\\home.txt", "w")
        while 1 == 1:
            path = console.input("[dark_cyan]▄[/dark_cyan][grey100 on dark_cyan] Input a Path for OpenPy [/grey100 on dark_cyan][dark_cyan]▀[/dark_cyan] ")
            if os.path.exists(path):
                home_txt.write(path)
                break
            else:
                try:
                    os.mkdir(path)
                    home_txt.write(path)
                    break
                except: 
                    print("[red3]Error![/red3] Path couldn't be found or created. Please enter another path.")
                    
    # This part will create and check if all folders in the OpenPy Home Directory are present. If not, they will be created.
    openpy_home_path = open(openpy_path + "\\settings\\home.txt", "r").read()
    try:
        with Progress() as progress:
            task1 = progress.add_task("Checking Paths", total=5)
            while not progress.finished:
                if not os.path.exists(openpy_home_path): 
                    os.mkdir(openpy_home_path)
                    progress.update(task1, advance=1)
                
                if not os.path.exists(openpy_home_path + "\\apps"): 
                    os.mkdir(openpy_home_path + "\\apps")
                    progress.update(task1, advance=1)
                
                if not os.path.exists(openpy_home_path + "\\themes"): 
                    os.mkdir(openpy_home_path + "\\themes")
                    progress.update(task1, advance=1)
                
                if not os.path.exists(openpy_home_path): 
                    os.mkdir(openpy_home_path + "\\settings")
                    progress.update(task1, advance=1)
                
                if not os.path.exists(openpy_home_path + "\\apps\\cloudrun"): 
                    os.mkdir(openpy_home_path + "\\apps\\cloudrun")
                    progress.update(task1, advance=1)
                
                if not os.path.exists(openpy_home_path + "\\apps\\downloaded"): 
                    os.mkdir(openpy_home_path + "\\apps\\downloaded")
                    progress.update(task1, advance=1)

                while not progress.finished:
                    progress.update(task1, advance=1)
    except: 
        print("[red3]Critical Error![/red3] An error has occoured durring the Path Check. OpenPy can not continue.")
        with Progress() as progress:
            task1 = progress.add_task("[red]Closing...", total=10)
            while not progress.finished:
                progress.update(task1, advance=1)
                time.sleep(1)
        
        quit()