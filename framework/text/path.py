import os

class get:
    def openpy_path():
        openpy_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").removesuffix("/framework/text")
        return open(openpy_path + "/settings/home.txt", "r").read()

    def downloaded_apps_path():
        openpy_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/").removesuffix("/framework/text")
        return open(openpy_path + "/settings/home.txt", "r").read() + "/apps/downloaded"