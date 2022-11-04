import subprocess

class Apps:
    def launch(app_path: str):
        exec(open(app_path).read())