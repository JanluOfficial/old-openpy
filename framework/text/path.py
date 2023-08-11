import os

class get:
    def openpy_path(): return os.path.expanduser('~/OpenPy-Files').replace("\\", "/")

    def downloaded_apps_path(): return os.path.expanduser('~/OpenPy-Files/apps/downloaded').replace("\\", "/")
    
    def config_path(): return os.path.expanduser('~/OpenPy-Files/configs').replace("\\", "/")