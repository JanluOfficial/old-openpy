import subprocess
import rich
from rich.console import Console
from time import sleep
import requests
import base64
import os
import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from os.path import exists

class Directories:
    def checkAndCreate():
        paths = ['OpenPy', 'OpenPy\\user', 'OpenPy\\themes', 'OpenPy\\extensions', 'OpenPy\\languages', 'OpenPy\\user\\data']
        appdata = os.getenv('APPDATA')
        for path in paths:
            if not exists(f'{appdata}\\{path}'):
                os.mkdir(f'{appdata}\\{path}')

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

    def outputAppList():
        console = Console()
        appTable = Table(title='Installed Apps') 
        appTable.add_column('Name', justify='left', style='bold blue')
        appTable.add_column('Subtitle', style="white")
        appTable.add_column('Version', style='bold cyan')
        errCount = 0
        appPath = os.getcwd() + '\\apps'
        appPathList = os.listdir(appPath)
        for folder in appPathList:
            if folder != "__pycache__":
                try:
                    jsonFILE = open(f'{appPath}\\{folder}\\app.json', 'r')
                    appJSON = json.load(jsonFILE)
                    appName = appJSON['name']
                    appSubtitle = appJSON['subtitle']
                    appVersion = str(appJSON['version'])
                    appTable.add_row(appName, appSubtitle, appVersion)
                except:
                    errCount += 1
        console.print(appTable)
        if errCount != 0:
            errCountStr = str(errCount)
            console.print(f'[red]{errCountStr}[/red] Errors occoured.')


class Online: 
    def readFile(raw_url: str): 
        req = requests.get(raw_url)
        if req.status_code == requests.codes.ok:
            print(req)

class startup:
    def GithubKey(mode: str):
        if mode == "startup":
            if exists('C:\\ProgramData\\OpenPy\\user\\data\\Github_APIv3_key.json'):
                api_key_file = open('C:\\ProgramData\\OpenPy\\Github_APIv3_key.json', 'r')
                return json.load(api_key_file)['api-key']
            else:
                console = Console()
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