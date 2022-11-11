import os
import json
import framework.commands.OpenPyCommands as OpenPyCMDs
from rich.console import Console
import framework.color.theme as theme
import framework.OOBE as OOBE


class handle:
    def command(cmd: str, githubAPI: str):
        if cmd == "develop":
            jsonPath = os.getcwd() + f'\\apps\\developmentEnviorment\\app.json'
            appInfoFile = open(jsonPath, 'r')
            jsonFile = json.load(appInfoFile)
            OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\developmentEnviorment\\{jsonFile["main-file"]}', "openpy")

        elif cmd.startswith('run-app '):
            try:
                console = Console()
                apptorun = cmd.lstrip('run-app ')
                print(apptorun)
                jsonPath = os.getcwd() + '\\apps\\' + apptorun + '\\app.json'
                appInfoFile = open(jsonPath, 'r')
                jsonFile = json.load(appInfoFile)
                OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\{apptorun}\\{jsonFile["main-file"]}', jsonFile['app-type'])
            except FileNotFoundError: 
                errcolor = theme.getColor('indicators', 'error')
                console.print(f'[{errcolor}]Error trying to find the application[/{errcolor}]')
                console.print(f'The app.json for {apptorun} could not be found.')
            except:
                errcolor = theme.getColor('indicators', 'error')
                console.print(f'[{errcolor}]Unknown Error in handler.py[/{errcolor}]')


        elif cmd == "exit" or cmd == "quit":
            quit()

        elif cmd.startswith("appList"):
            if cmd == "appList -c":
                OpenPyCMDs.Apps.appListCompact()
            else:
                OpenPyCMDs.Apps.outputAppList()

        elif cmd.startswith('changeTheme '):
            theme.changeSelectedTheme(cmd.lstrip('changeTheme '))

        elif cmd == "OOBE":
            OOBE.OOBE.start()

        else:
            errcolor = theme.getColor('indicators', 'error')
            console = Console()
            console.print(f'[{errcolor}]Invalid cmd[/{errcolor}]')