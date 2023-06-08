import requests
import os

def make_cloud(file: str, content: str):
    open(file, "w").write(str(requests.get(content).content.decode()))

def make_empty(file: str):
    open(file, "w").write("")

def make_dir(dir: str):
    os.mkdir(dir)