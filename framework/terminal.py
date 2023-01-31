import framework.console.input as terminal_input
import requests
import json
import re

from rich.progress import Progress
from rich.tree import Tree
from rich import print

def terminal():
    cmd = terminal_input.input()

    if cmd.startswith("cloudrun "):
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
                app_info = json.loads(requests.get(applistjson["cloudrun"][re.sub(r'^cloudrun ', '', cmd)]).content)
                progress.update(task1, advance=1)
                app_code = requests.get(app_info["file"]).content
                progress.update(task1, advance=1)
            except KeyError:
                print("[red3]Error![/red3] This cloudrun app might not exist.")
        try:
            exec(app_code)
        except UnboundLocalError: otk = 0

    elif cmd.startswith("cloudsearch "):
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

            searchterm = re.sub(r'^cloudsearch ', '', cmd)
            tree = Tree("[dark_cyan]▄[grey100 on dark_cyan] Results [/grey100 on dark_cyan]▀[/dark_cyan]")

            for app in app_list_json["cloudrun"]["all-cloudrun-apps-list"]:
                app_data = json.loads(requests.get(app_list_json["cloudrun"][app]).content)
                if searchterm in app_data["name"] or searchterm in app:
                    to_add_to = tree.add(app_data["name"].replace(searchterm, f'[green3]{searchterm}[/green3]'))
                    to_add_to.add(f'{app_data["description"]}')
                    to_add_to.add(app_data["file"])
                    to_add_to.add("Run Name").add(app.replace(searchterm, f'[green3]{searchterm}[/green3]'))
                progress.update(task2, advance=(1000-2)/len(app_list_json["cloudrun"]["all-cloudrun-apps-list"]))
            print(tree)

    elif cmd == "cloudlist":
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

            searchterm = re.sub(r'^cloudsearch ', '', cmd)
            tree = Tree("[dark_cyan]▄[grey100 on dark_cyan] Results [/grey100 on dark_cyan]▀[/dark_cyan]")

            for app in app_list_json["cloudrun"]["all-cloudrun-apps-list"]:
                app_data = json.loads(requests.get(app_list_json["cloudrun"][app]).content)
                to_add_to = tree.add(app_data["name"].replace(searchterm, f'[green3]{searchterm}[/green3]'))
                to_add_to.add(f'{app_data["description"]}')
                to_add_to.add(app_data["file"])
                to_add_to.add("Run Name").add(app.replace(searchterm, f'[green3]{searchterm}[/green3]'))
                progress.update(task2, advance=(1000-2)/len(app_list_json["cloudrun"]["all-cloudrun-apps-list"]))
            print(tree)
