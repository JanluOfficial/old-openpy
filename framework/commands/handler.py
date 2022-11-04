import os
import json
import framework.commands.OpenPyCommands as OpenPyCMDs

class handle:
    def command(cmd: str):
        if cmd == "develop":
            jsonFile = os.getcwd() + f'\\apps\\developmentEnviorment\\app.json'
            appInfoFile = open(jsonFile, 'r')
            jsonFile = json.load(appInfoFile)
            OpenPyCMDs.Apps.launch(os.getcwd() + f'\\apps\\developmentEnviorment\\{jsonFile["main-file"]}')
