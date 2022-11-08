import os
import json
import framework.commands.OpenPyCommands as OpenPyCMDs
from pprint import pprint
from rich.console import Console


class handle:
    def command(cmd: str, githubAPI: str):
        if cmd == "develop":
            jsonPath = os.getcwd() + f'\\apps\\developmentEnviorment\\app.json'
            appInfoFile = open(jsonPath, 'r')
            jsonFile = json.load(appInfoFile)
            OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\developmentEnviorment\\{jsonFile["main-file"]}')

        elif cmd.startswith('run-app '):
            try:
                console = Console()
                apptorun = cmd.lstrip('run-app ')
                print(apptorun)
                jsonPath = os.getcwd() + '\\apps\\' + apptorun + '\\app.json'
                appInfoFile = open(jsonPath, 'r')
                jsonFile = json.load(appInfoFile)
                OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\{apptorun}\\{jsonFile["main-file"]}')
            except FileNotFoundError: 
                console.print(f'[red]Error trying to find the application[/red]')
                console.print(f'The app.json for {apptorun} could not be found.')
            except:
                console.print(f'[red]Unknown Error in handler.py[/red]')


        elif cmd == "exit" or cmd == "quit":
            quit()

        elif cmd == "onlineTest":
            OpenPyCMDs.Online.readFile("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/apps/app-library.json")

        elif cmd == "appList":
            OpenPyCMDs.Apps.outputAppList()

        else:
            console = Console()
            console.print('[red]Invalid cmd[/red]')