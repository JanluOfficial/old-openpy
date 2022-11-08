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