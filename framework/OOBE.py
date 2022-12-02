import framework.OOBEscreens as screens
import framework.OOBEapply as OOBEapply
import os

class OOBE:
    def start():
        screens.WelcomeScreen()
        screens.EULAScreen()
        username = screens.UsernameScreen()
        screens.ColorScreen()
        OOBEapply.apply(username)
        screens.ThankYouScreen(username)

def OpenPyOOBE():
    hasOOBEran = open(os.getenv('APPDATA') + '\\OpenPy\\user\\settings\\oobeHasRan.ops', 'r').read()
    if hasOOBEran != 'true':
        OOBE.start()