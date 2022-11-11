import platform

def appType(type: str):
    if type == "openpy":
        return "OpenPy"
    elif type == "py":
        return "Python"
    elif type == "win":
        if platform.system() == "Windows":
            return "Windows"
        else:
            return "!WINDOWS!"
