import json
import os
import platform
import framework.getConsoleSize as getConSize

class Data_Collector:
    def getStartupJSON():
        infofile = open("info.json", "r").read()
        infoJSON = json.loads(infofile)
        return infoJSON
