import os, api.system as sysapi

def clear(): os.system('cls' if sysapi.os.is_windows() else 'clear')