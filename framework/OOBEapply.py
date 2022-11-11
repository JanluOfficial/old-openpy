import os

def apply(username: str):
    open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\username.ops', 'w').write(username)
    open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\oobeHasRan.ops', 'w').write('true')