import requests
import json
import random
from rich import Console

def init():
    console = Console()
    try:
        lists = requests.get("https://raw.githubusercontent.com/JanluOfficial/opr-library/master/main.json", 10)
        listjson = json.loads(lists.text)
        quotes = requests.get(listjson["quoteslisturl"])
        print(random.choice(quotes.text.split("\n")))
    except:
        funny_error_list = ["Have you tried reconnecting?", "404: Quotes not found", "It's so sunny that I can't connect to the cloud.", 'A wise man once said "You are not connected to the internet"']
        print(random.choice(funny_error_list))