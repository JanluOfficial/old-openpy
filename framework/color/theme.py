import json
import os
from rich.prompt import Confirm
from rich.console import Console

def getColor(catigory: str, property: str): 
    try:
        themeSetting = open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\theme.ops').read()
        return json.loads(open(os.getenv('APPDATA') + f'\\OpenPy\\themes\\{themeSetting}').read())[catigory][property]
    except:
        return json.loads(open(os.getenv('APPDATA') + f'\\OpenPy\\themes\\default.json').read())[catigory][property]

def changeSelectedTheme(theme: str):
    console = Console()
    confirmation = Confirm.ask(f"Do you wan't to switch your OpenPy theme to {theme}?")
    if confirmation:
        themeList = os.listdir(os.getenv('APPDATA') + f'\\OpenPy\\themes')
        if theme in themeList:
            try:
                open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\theme.ops', 'w').write(theme)
                console.print(f'Successfully changed the theme to {theme}.')
            except:
                console.print(f'There has been an error changing the theme to {theme}.')
        else:
            console.print(f"The Theme {theme} doesn't seem to be installed.")

def coloredString(string: str, catigory: str, property: str):
    themeSetting = open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\theme.ops').read()
    colors = json.loads(open(os.getenv('APPDATA') + f'\\OpenPy\\themes\\{themeSetting}').read())
    try:
        string = f'[{colors[catigory][property]}]{string}[/{colors[catigory][property]}]'
    except:
        colors = json.loads(open(os.getenv('APPDATA') + f'\\OpenPy\\themes\\default.json', 'r').read())
        string = f'[{colors[catigory][property]}]{string}[/{colors[catigory][property]}]'
    return string