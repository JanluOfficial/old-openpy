import os
import json
import framework.commands.OpenPyCommands as OpenPyCMDs

class handle:
    def command(cmd: str):
        if cmd == "develop":
            jsonPath = os.getcwd() + f'\\apps\\developmentEnviorment\\app.json'
            appInfoFile = open(jsonPath, 'r')
            jsonFile = json.load(appInfoFile)
            OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\developmentEnviorment\\{jsonFile["main-file"]}')

        elif cmd.startswith('run-app '):
            apptorun = cmd.lstrip('run-app ')
            print(apptorun)
            jsonPath = os.getcwd() + '\\apps\\' + apptorun + '\\app.json'
            appInfoFile = open(jsonPath, 'r')
            jsonFile = json.load(appInfoFile)
            OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\{apptorun}\\{jsonFile["main-file"]}')

        elif cmd == "exit" or cmd == "quit":
            quit()