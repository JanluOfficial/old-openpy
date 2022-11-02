import json
import os

def listed():
    appsPath = os.getcwd() + '\\apps'
    dirlist = os.listdir(appsPath)
    for app in dirlist:
        appPath = appsPath + '\\' + app
        appFileList = os.listdir(appPath)
        if 'app-info.json' in appFileList:
            jsonFile = appPath + '\\app-info.json'
            appInfoFile = open(jsonFile, 'r')
            return json.loads(appInfoFile)
        else:
            return 0