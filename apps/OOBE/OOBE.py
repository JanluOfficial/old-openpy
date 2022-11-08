from rich.console import Console
from rich.prompt import Prompt
from rich.console import Group
from rich.panel import Panel

import screens.screens as screens

console = Console()

class Setup:
    screens.WelcomeScreen()
    screens.EULAScreen()