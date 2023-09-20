import framework.console.input as terminal_input
import framework.oii.interpret as interpret
import framework.text.path as path
from rich import print
from rich.table import Table
import os
import logging
import subprocess
#import tkinter as tk
import shutil
import api.terminal as termapi

while 1 == 1:
    try:
        import requests
        break
    except: os.system("python -m pip install requests")

import json
while 1 == 1:
    try:
        from rich.progress import Progress
        from rich.tree import Tree
        from rich import print
        break
    except:
        os.system("python -m pip install rich")



def terminal():
    cmdstr = terminal_input.input()
    if cmdstr.repalce(" ", "") == "": return None 
    cmd = cmdstr.split()

    cmd.append("rando-key1")
    cmd.append("rando-key2")
    cmd.append("rando-key3")

    # General Commands

    if cmd[0] == "help":
        table = Table()
        table.add_column("Command")
        table.add_column("Description")
        table.add_row("help", "Print this help")
        table.add_row("clear", "Clear the screen")
        table.add_row("exit", "Exit the program")
        table.add_row("version", "Print the version of OpenPy")
        table.add_row("")
        table.add_row("run", "Run a local app")
        table.add_row("search", "Search for a local app")
        table.add_row("list", "List all local apps")
        table.add_row("")
        table.add_row("cloudrun", "Run a cloudrun app")
        table.add_row("cloudsearch", "Search for a cloudrun app")
        table.add_row("cloudsearch", "List all cloudrun apps")

        print(table)

    elif cmd[0] == "version":
        print("OpenPy v1.0.0")

    elif cmd[0] == "clear" or cmd[0] == "cls":
        termapi.clear()

    elif cmd[0] == "exit" or cmd[0] == "quit" or cmd[0] == "bye":
        quit()

    # Cloud Commands

    elif cmd[0] == "cloudrun":
        with Progress() as progress:
            try:
                task1 = progress.add_task("[purple4]▄[grey100 on purple4] Start [/grey100 on purple4]▀[/purple4]", total=6)

                lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
                progress.update(task1, advance=1)
                listjson = json.loads(lists.content)
                progress.update(task1, advance=1)
                applist = requests.get(listjson["applisturl"])
                progress.update(task1, advance=1)
                applistjson = json.loads(applist.content)
                progress.update(task1, advance=1)
                app_info = json.loads(requests.get(applistjson["cloudrun"][cmd[1]]).content)
                progress.update(task1, advance=1)
                app_code = requests.get(app_info["file"]).content
                progress.update(task1, advance=1)
            except KeyError:
                print("[red3]Error![/red3] This cloudrun app does not exist.")
        try:
            exec(app_code)
        except UnboundLocalError: otk = 0

    elif cmd[0] == "cloudsearch":
        with Progress() as progress:
            task1 = progress.add_task("[purple4]▄[grey100 on purple4] Gathering List [/grey100 on purple4]▀[/purple4]", total=2)
            task2 = progress.add_task("[purple4]▀[grey100 on purple4] Processing [/grey100 on purple4]▀[/purple4]", total=1000)

            lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
            progress.update(task1, advance=1)
            list_json = json.loads(lists.content)
            progress.update(task2, advance=1)
            app_list = requests.get(list_json["applisturl"])
            progress.update(task1, advance=1)
            app_list_json = json.loads(app_list.content)
            progress.update(task2, advance=1)

            searchterm = cmd[1]
            tree = Tree("[dark_cyan]▄[grey100 on dark_cyan] Results [/grey100 on dark_cyan]▀[/dark_cyan]")

            for app in app_list_json["cloudrun"]["all-cloudrun-apps-list"]:
                app_data = json.loads(requests.get(app_list_json["cloudrun"][app]).content)
                if searchterm in app_data["name"] or searchterm in app:
                    to_add_to = tree.add(app_data["name"].replace(searchterm, f'[green3]{searchterm}[/green3]'))
                    to_add_to.add(f'{app_data["description"]}')
                    to_add_to.add("Author").add(app_data["author"])
                    to_add_to.add(app_data["file"])
                    to_add_to.add("Run Name").add(app.replace(searchterm, f'[green3]{searchterm}[/green3]'))
                progress.update(task2, advance=(1000-2)/len(app_list_json["cloudrun"]["all-cloudrun-apps-list"]))
            print(tree)

    elif cmd[0] == "cloudlist":
        with Progress() as progress:
            task1 = progress.add_task("[purple4]▄[grey100 on purple4] Gathering List [/grey100 on purple4]▀[/purple4]", total=2)
            task2 = progress.add_task("[purple4]▀[grey100 on purple4] Processing [/grey100 on purple4]▀[/purple4]", total=1000)

            lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
            progress.update(task1, advance=1)
            list_json = json.loads(lists.content)
            progress.update(task2, advance=1)
            app_list = requests.get(list_json["applisturl"])
            progress.update(task1, advance=1)
            app_list_json = json.loads(app_list.content)
            progress.update(task2, advance=1)
            tree = Tree("[dark_cyan]▄[grey100 on dark_cyan] Results [/grey100 on dark_cyan]▀[/dark_cyan]")

            for app in app_list_json["cloudrun"]["all-cloudrun-apps-list"]:
                app_data = json.loads(requests.get(app_list_json["cloudrun"][app]).content)
                to_add_to = tree.add(app_data["name"])
                to_add_to.add(f'{app_data["description"]}')
                to_add_to.add("Author").add(app_data["author"])
                to_add_to.add(app_data["file"])
                to_add_to.add("Run Name").add(app)
                progress.update(task2, advance=(1000-2)/len(app_list_json["cloudrun"]["all-cloudrun-apps-list"]))
            print(tree)

    # Local Commands

    elif cmd[0] == "install":
        app = cmd[1]
        with Progress() as progress: 
            while 1 == 1:
                task1 = progress.add_task("[purple4]▄[grey100 on purple4] Getting oii script [/grey100 on purple4]▀[/purple4]", total=6)

                lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
                progress.update(task1, advance=1)
                listjson = json.loads(lists.content)
                progress.update(task1, advance=1)
                applist = requests.get(listjson["applisturl"])
                progress.update(task1, advance=1)
                applistjson = json.loads(applist.content)
                progress.update(task1, advance=1)
                logging.log(msg=applistjson["downloadable"]["all-downloadable-apps-list"], level=1)
                if app in applistjson["downloadable"]["all-downloadable-apps-list"]:
                    app_info = json.loads(requests.get(applistjson["downloadable"][app]).content)
                else:
                    print("[red3]Error![/red3] This app does not exist on the opr-library repository")
                    break
                progress.update(task1, advance=1)
                oii = requests.get(app_info["oii-script"]).content.decode().splitlines()
                progress.update(task1, advance=1)

                interpret.interp(app, oii)
                break
    
    elif cmd[0] == "downloadlist":
        with Progress() as progress:
            task1 = progress.add_task("[purple4]▄[grey100 on purple4] Gathering List [/grey100 on purple4]▀[/purple4]", total=2)
            task2 = progress.add_task("[purple4]▀[grey100 on purple4] Processing [/grey100 on purple4]▀[/purple4]", total=1000)

            lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json")
            progress.update(task1, advance=1)
            list_json = json.loads(lists.content)
            progress.update(task2, advance=1)
            app_list = requests.get(list_json["applisturl"])
            progress.update(task1, advance=1)
            app_list_json = json.loads(app_list.content)
            progress.update(task2, advance=1)
            tree = Tree("[dark_cyan]▄[grey100 on dark_cyan] Results [/grey100 on dark_cyan]▀[/dark_cyan]")

            for app in app_list_json["downloadable"]["all-downloadable-apps-list"]:
                app_data = json.loads(requests.get(app_list_json["downloadable"][app]).content)
                to_add_to = tree.add(app_data["name"])
                to_add_to.add(f'{app_data["description"]}')
                to_add_to.add("Author").add(app_data["author"])
                to_add_to.add(app_data["oii-script"])
                to_add_to.add("Run Name").add(app)
                progress.update(task2, advance=(1000-2)/len(app_list_json["cloudrun"]["all-cloudrun-apps-list"]))
            print(tree)

    elif cmd[0] == "run":
        try:
            app = cmd[1]
            app_path = path.get.downloaded_apps_path() + f'/{app}'
            app_info_list = json.loads(open(app_path + f'/{app}.json', 'r').read())
            with Progress() as progress:
                task1 = progress.add_task("[purple4]▄[grey100 on purple4] Running App [/grey100 on purple4]▀[/purple4]", total=2)

                progress.update(task1, advance=1)
                app_file = app_info_list["file"]
                progress.update(task1, advance=1)

            if app_info_list["run-as"] == "openpy": 
                exec(open(f"{app_path}/{app_file}", "r").read())
            else: subprocess.run(f'python {app_path}/{app_file}')
        except FileNotFoundError:
            print("[red3]▄[grey100 on red3] Error [/grey100 on red3]▀[/red3] Application has not been found!\nPlease make sure that it is installed.\n")
        
    elif cmd[0] == "uninstall":
        app = cmd[1]
        app_path = path.get.downloaded_apps_path() + f'/{app}'
        if os.path.exists(f"{app_path}/{app}.json"):
            with Progress() as progress:
                task1 = progress.add_task("[purple4]▄[grey100 on purple4] Uninstalling App [/grey100 on purple4]▀[/purple4]", total=1)

                shutil.rmtree(app_path, ignore_errors=False, onerror=None)
                progress.update(task1, advance=1)
   
                    
        else:
            print(f"[red3]▄[grey100 on red3] Error [/grey100 on red3]▀[/red3] Application is not installed.\nUnable to find {app_path}/{app}/{app}.json.")

    else:
        print(f"[red3]▄[grey100 on red3] Error [/grey100 on red3]▀[/red3] Command not found!\nPlease use the help command to see a list of available commands.\n")

if __name__ == "__main__":
    print("[red3]▄[grey100 on red3] Error [/grey100 on red3]▀[/red3] Please run the main open.py file to start OpenPy.\n")