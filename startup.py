import json
import os
import platform
import framework.getConsoleSize as getConSize
from os.path import exists
from rich.console import Console
from rich.prompt import Prompt

class StartUp:
    def ProgramDataFolder():
        if not exists('C:\\ProgramData\\OpenPy'):
            os.mkdir('C:\\ProgramData\\OpenPy')

    def GithubKey(mode: str):
        if mode == "startup":
            if exists('C:\\ProgramData\\OpenPy\\user\\data\\Github_APIv3_key.json'):
                api_key_file = open('C:\\ProgramData\\OpenPy\\Github_APIv3_key.json', 'r')
                return json.load(api_key_file)['api-key']
            else:
                console = Console()
                console.print('[bold yellow]Open[/bold yellow][bold blue]Py[/bold blue]')
                console.print('Please enter a usable [bold purple]Github API Key[/bold purple]')
                newAPIkey = Prompt.ask('[bold purple]Github API Key[/bold purple]', default='skip')
                if newAPIkey != 'skip':
                    api_kf_w = open('C:\\ProgramData\\OpenPy\\user\\data\\Github_APIv3_key.json', 'w') # api_kf_w stands for API Key File Writable
                    writableList = [
                        '{\n',
                        f'    "api-key": "{newAPIkey}"\n',
                        '}'
                    ]
                    api_kf_w.writelines(writableList)
                    return api_kf_w

class Data_Collector:
    def getStartupJSON():
        infofile = open("info.json", "r").read()
        infoJSON = json.loads(infofile)
        return infoJSON