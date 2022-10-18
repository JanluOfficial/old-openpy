import os

def getConsoleSize():
    ts = str(os.get_terminal_size()).strip("os.terminal_size(").strip(")").split(",")
    for i in ts:
        if i.startswith("columns="):
            columns = int(i.strip("columns="))
        elif i.startswith("lines="):
            lines = int(i.strip("lines="))
        else:
            ValueError("Value couldn't be converted.")

    return [columns, lines]