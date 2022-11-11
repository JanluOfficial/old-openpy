import subprocess
from time import sleep
import base64
import os
import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from os.path import exists
import framework.color.theme as theme
import framework.commands.appType as appTypeHandler

class Directories:
    def checkAndCreate():
        paths = ['OpenPy', 'OpenPy\\user', 'OpenPy\\themes', 'OpenPy\\extensions', 'OpenPy\\languages', 'OpenPy\\user\\settings']
        appdata = os.getenv('APPDATA')
        for path in paths:
            if not exists(f'{appdata}\\{path}'):
                os.mkdir(f'{appdata}\\{path}')

class Files:
    def checkAndCopyDefaultFiles():
        appdata = os.getenv('APPDATA')
        if not exists(appdata + '\\OpenPy\\themes\\default.json'):
            defaultTheme = open(os.getcwd() + '\\framework\\color\\defaultTheme.json', 'r').read()
            newFile = open(appdata + '\\OpenPy\\themes\\default.json', "w")
            newFile.write(defaultTheme)
        else:
            defaultTheme = open(os.getcwd() + '\\framework\\color\\defaultTheme.json', 'r').read()
            themeFile = open(appdata + '\\OpenPy\\themes\\default.json', "r").read()

            if defaultTheme != themeFile:
                themeFile = open(appdata + '\\OpenPy\\themes\\default.json', "w")
                themeFile.write(defaultTheme)

        if not exists(appdata + '\\OpenPy\\user\\settings\\theme.ops') or open(appdata + '\\OpenPy\\user\\settings\\theme.ops', 'r').read() == '':
            open(appdata + '\\OpenPy\\user\\settings\\theme.ops', 'w').write('default.json')
        if not exists(appdata + '\\OpenPy\\user\\settings\\oobeHasRan.ops') or open(appdata + '\\OpenPy\\user\\settings\\theme.ops', 'r').read() == '':
            open(appdata + '\\OpenPy\\user\\settings\\oobeHasRan.ops', 'w').write('false')

class Apps:
    def launch(app_path: str, app_type: str):
        console = Console()
        if app_type == 'openpy':
            try:
                with console.status('[bold purple]Reading Application Data...') as status:
                    while 1 != 2:
                        app_data = open(app_path).read()
                        console.log('[green]The Application Data has been read and the program will start soon.')
                        break
                sleep(1)
                exec(app_data)

            except FileNotFoundError: 
                console.print(f'[red]Error trying to find the application[/red]')
                console.print(f'The app.json for {app_path} could not be found.')
            except:
                console.print(f'[red]Unknown Error in OpenPyCommands.py[/red]')
        elif app_type.startswith('py'):
            subprocess.call(f'python {app_path}')
        else:
            subprocess.call(app_path)

    def launchDebug(app_path: str, app_type: str):
        console = Console()
        if app_type == 'openpy':
            with console.status('[bold purple]Reading Application Data...') as status:
                while 1 != 2:
                    app_data = open(app_path).read()
                    console.log('[green]The Application Data has been read and the program will start soon.')
                    break
            sleep(1)
            exec(app_data)
        elif app_type.startswith('py'):
            subprocess.call(f'python {app_path}')
        else:
            subprocess.call(app_path)

    def outputAppList():
        console = Console()
        appTable = Table(title='Installed Apps') 
        appTable.add_column('Name', justify='left', style='bold blue')
        appTable.add_column('Subtitle', style="white")
        appTable.add_column('Launch Name', style='purple')
        appTable.add_column('Type', style='bold cyan')
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
                    appTypeRaw = appJSON['app-type']
                    appLaunchName = folder
                    appTable.add_row(appName, appSubtitle, appLaunchName, appTypeRaw, appVersion)
                except:
                    errCount += 1
        console.print(appTable)
        if errCount != 0:
            errCountStr = str(errCount)
            console.print(f'[red]{errCountStr}[/red] Errors occoured.')

    def appListCompact():
        console = Console()
        appTable = Table(title='Installed Apps') 
        appTable.add_column('Name', justify='left', style='bold blue')
        appTable.add_column('Launch Name', style='purple')
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
                    appVersion = str(appJSON['version'])
                    appLaunchName = folder
                    appTable.add_row(appName, appLaunchName, appVersion)
                except:
                    errCount += 1
        console.print(appTable)
        if errCount != 0:
            errCountStr = str(errCount)
            console.print(f'[red]{errCountStr}[/red] Errors occoured.')

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

class Strings:
    def OpenPyString():
        return theme.coloredString("Open", "OpenPy", "1") + theme.coloredString("Py", "OpenPy", "2")

class console:
    def getConsoleSize():
        ts = str(os.get_terminal_size()).strip("os.terminal_size(").strip(")").split(",")
        for i in ts:
            if i.startswith("columns="):
                columns = int(i.lstrip("columns="))
            elif i.startswith("lines="):
                lines = int(i.lstrip("lines="))
            else:
                ValueError("Value couldn't be converted.")

        return [columns, lines]

